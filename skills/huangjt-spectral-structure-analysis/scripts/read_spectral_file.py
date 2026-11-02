"""Read supported NMR/MS files into a new evidence directory; retain acquisition metadata.

Reading is separate from phasing, assignment, quantitation and identification.
Bruker/Varian inputs are complete acquisition directories, not an isolated fid.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,sys,os,shutil,subprocess
from pathlib import Path

FORMATS=('auto','bruker','bruker-pdata','varian','nmrpipe','thermo-raw','mzml','mzxml','mgf','jcamp','csv')

def identify(path,selected):
    if selected!='auto':return selected
    if path.is_dir():
        if (path/'procs').is_file():return 'bruker-pdata'
        if (path/'acqus').is_file() and any((path/f).is_file() for f in ['fid','ser']):return 'bruker'
        if (path/'procpar').is_file() and (path/'fid').is_file():return 'varian'
        raise ValueError('Unrecognised directory. Supply complete Bruker/Varian acquisition folder or explicit format.')
    suffix=path.suffix.lower()
    if suffix=='.raw' and path.is_file():
        with path.open('rb') as f:header=f.read(512).decode('utf-16le',errors='ignore')
        if 'Finnigan' in header or 'Thermo' in header:return 'thermo-raw'
    if suffix in {'.mzml','.mzxml','.mgf'}:return suffix[1:]
    if suffix in {'.jdx','.dx'}:return 'jcamp'
    if suffix=='.csv':return 'csv'
    if suffix in {'.ft1','.ft2','.ft3','.pipe'}:return 'nmrpipe'
    if suffix in {'.raw','.d','.mnova','.mestre','.fid'}:
        raise ValueError('Vendor-specific input: identify instrument and retain all companion files. Thermo RAW needs ThermoRawFileParser; Waters/Agilent need their compatible converter. MNova needs an authorized export. Use mzML/MGF or a complete acquisition folder; no silent text fallback.')
    raise ValueError('Unknown format; specify --format only after checking the actual file format.')

def jsonable(x):
    if isinstance(x,dict):return {str(k):jsonable(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [jsonable(v) for v in x]
    if hasattr(x,'tolist'):return x.tolist()
    if isinstance(x,(str,int,float,bool)) or x is None:return x
    return str(x)

def fingerprints(path):
    result=[]
    inputs=sorted(p for p in path.rglob('*') if p.is_file()) if path.is_dir() else [path]
    for p in inputs:
        h=hashlib.sha256()
        with p.open('rb') as f:
            while block:=f.read(1024*1024):h.update(block)
        result.append({'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':h.hexdigest()})
    return result

def read_nmr(path,fmt,out):
    import nmrglue as ng
    import numpy as np
    if fmt=='bruker':metadata,data=ng.bruker.read(str(path))
    elif fmt=='bruker-pdata':metadata,data=ng.bruker.read_pdata(str(path))
    elif fmt=='varian':metadata,data=ng.varian.read(str(path))
    elif fmt=='nmrpipe':metadata,data=ng.pipe.read(str(path))
    else:raise ValueError(fmt)
    data=np.asarray(data)
    if not np.isfinite(data).all():raise ValueError('Nonfinite NMR data; investigate input before processing')
    # Preserve actual metadata rather than inventing spectral widths, carriers or phase.
    arrays={'data':data};axes=[]
    if fmt=='bruker-pdata':
        for dim in range(data.ndim):
            key='procs' if dim==data.ndim-1 else f'proc{data.ndim-dim}s'
            values=metadata.get(key,{})
            try:
                sf=float(values['SF']);sw=float(values['SW_p']);size=int(values['SI']);offset=float(values['OFFSET'])
                if sf<=0 or sw<=0 or size!=data.shape[dim] or int(values.get('STSR',0))!=0:raise ValueError('Submatrix/axis requires explicit review')
                arrays[f'axis_{dim}_ppm']=offset-np.arange(size)*sw/sf/size
                axes.append({'dimension':dim,'unit':'ppm','source':key,'calibration':'as stored; no solvent correction applied'})
            except (KeyError,ValueError,TypeError):axes.append({'dimension':dim,'unit':None,'source':key,'calibration':'unresolved; inspect actual processing metadata'})
    np.savez_compressed(out/'nmr-data.npz',**arrays)
    (out/'acquisition.json').write_text(json.dumps(jsonable(metadata),ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')
    return {'kind':'nmr','format':fmt,'shape':list(data.shape),'points':int(data.size),'complex':bool(np.iscomplexobj(data)),'nmrglue':ng.__version__,'output_data':'nmr-data.npz','metadata':'acquisition.json','axes':axes,'processing_applied':[],'next':'Check acquisition settings, digital filter, axis calibration, phase and baseline before integration/assignment. process_1d.py supports explicitly configured 1D FID processing.'}

def read_ms(path,fmt,out):
    import pyopenms as ms
    experiment=ms.MSExperiment()
    loader={'mzml':ms.MzMLFile,'mzxml':ms.MzXMLFile,'mgf':ms.MascotGenericFile}[fmt]()
    loader.load(str(path),experiment)
    counts={};total=0
    with (out/'spectra.csv').open('w',encoding='utf-8',newline='') as f,(out/'peaks.csv').open('w',encoding='utf-8',newline='') as p:
        spectra=csv.writer(f);peaks=csv.writer(p)
        spectra.writerow(['spectrum','native_id','ms_level','rt_seconds','peak_count','tic','precursors_json'])
        peaks.writerow(['spectrum','mz','intensity'])
        for i,spec in enumerate(experiment):
            mz,intensity=spec.get_peaks();level=int(spec.getMSLevel());counts[level]=counts.get(level,0)+1;total+=len(mz)
            precursors=[{'mz':p.getMZ(),'charge':p.getCharge()} for p in spec.getPrecursors()]
            spectra.writerow([i,spec.getNativeID(),level,spec.getRT(),len(mz),float(intensity.sum()),json.dumps(precursors)])
            peaks.writerows((i,float(m),float(v)) for m,v in zip(mz,intensity))
    if not experiment.getNrSpectra() and not experiment.getNrChromatograms():raise ValueError('No spectra or chromatograms decoded')
    instrument=experiment.getInstrument()
    metadata={'name':instrument.getName(),'vendor':instrument.getVendor()}
    (out/'instrument.json').write_text(json.dumps(jsonable(metadata),ensure_ascii=False,indent=2),encoding='utf-8')
    # Chromatograms are separate from spectra; retain their actual time/intensity pairs.
    with (out/'chromatograms.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f);writer.writerow(['chromatogram','rt_seconds','intensity'])
        for i,chrom in enumerate(experiment.getChromatograms()):
            rt,intensity=chrom.get_peaks();writer.writerows((i,float(t),float(v)) for t,v in zip(rt,intensity))
    return {'kind':'ms','format':fmt,'spectra':experiment.getNrSpectra(),'chromatograms':experiment.getNrChromatograms(),'ms_levels':counts,'total_peaks':total,'pyopenms':ms.__version__,'processing_applied':[],'next':'Check profile/centroid state, polarity, mass calibration, adduct and precursor/isotope metadata before annotation. TIC is not purity or yield.'}

def read_text(path,fmt,out):
    import numpy as np
    if fmt=='jcamp':
        import nmrglue as ng
        metadata,values=ng.jcampdx.read(str(path))
        if values is None:raise ValueError('JCAMP contains no supported numeric spectrum')
        arrays=[np.asarray(v) for v in values] if isinstance(values,list) else [np.asarray(values)]
        np.savez_compressed(out/'text-data.npz',**{'data_'+str(i):v for i,v in enumerate(arrays)})
        (out/'acquisition.json').write_text(json.dumps(jsonable(metadata),ensure_ascii=False,indent=2),encoding='utf-8')
        return {'kind':'text_spectrum','format':'jcamp','arrays':[list(v.shape) for v in arrays],'axis':'Read actual JCAMP units and FIRSTX/LASTX before interpretation','processing_applied':[]}
    with path.open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f);header=reader.fieldnames
        if not header:raise ValueError('CSV needs an explicit column header and units')
        rows=list(reader)
    (out/'table.json').write_text(json.dumps({'columns':header,'rows':rows},ensure_ascii=False,indent=2),encoding='utf-8')
    return {'kind':'table','format':'csv','rows':len(rows),'columns':header,'processing_applied':[]}

def thermo_parser(configured=None):
    if configured:return Path(configured).resolve(strict=True)
    profiles=[Path.home()/'.local/share/chem-workbench/workbench.json']
    if os.environ.get('CHEM_WORKBENCH_HOME'):profiles.insert(0,Path(os.environ['CHEM_WORKBENCH_HOME'])/'workbench.json')
    for profile in profiles:
        if profile.is_file():
            value=json.loads(profile.read_text(encoding='utf-8')).get('thermo_parser')
            if value and Path(value).is_file():return Path(value)
    roots=[Path(__file__).resolve().parents[3]]
    if os.environ.get('CODEX_HOME'):roots.insert(0,Path(os.environ['CODEX_HOME']))
    for root in roots:
        p=root/'dependencies/thermorawfileparser-1.4.5/ThermoRawFileParser.exe'
        if p.is_file():return p
    found=shutil.which('ThermoRawFileParser.exe') or shutil.which('ThermoRawFileParser')
    if not found:raise FileNotFoundError('Configure --thermo-parser or install the official CompOmics ThermoRawFileParser; this RAW format was identified as Thermo.')
    return Path(found)

def run(source,output,selected='auto',parser_path=None,centroid=False):
    source=Path(source).resolve(strict=True);out=Path(output).resolve()
    if out.exists():raise FileExistsError('Choose a new output directory')
    if out==source or source.is_dir() and out.is_relative_to(source):raise ValueError('Output must be outside the acquisition directory')
    fmt=identify(source,selected)
    inputs=fingerprints(source)
    out.mkdir(parents=True)
    try:
        if fmt in {'bruker','bruker-pdata','varian','nmrpipe'}:report=read_nmr(source,fmt,out)
        elif fmt in {'mzml','mzxml','mgf'}:report=read_ms(source,fmt,out)
        elif fmt=='thermo-raw':
            parser=thermo_parser(parser_path);converted=out/'converted';converted.mkdir()
            # A local ASCII-named working copy avoids cloud-sync/native-reader sharing conflicts.
            working=out/'input.raw';shutil.copy2(source,working)
            if fingerprints(working)[0]['sha256']!=inputs[0]['sha256']:raise ValueError('RAW working copy differs from source')
            command=[str(parser),'-i='+str(working),'-o='+str(converted),'-f=1','-m=0']
            if not centroid:command.append('-p')
            with (out/'conversion.log').open('w',encoding='utf-8') as log:subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,check=True,timeout=600)
            mzml=list(converted.glob('*.mzML'))
            if len(mzml)!=1:raise ValueError('Expected exactly one converted mzML')
            report=read_ms(mzml[0],'mzml',out)
            report.update(format='thermo-raw',conversion={'command':command,'peak_picking':'vendor' if centroid else 'disabled; preserve profile data','mzml_sha256':fingerprints(mzml[0])[0]['sha256']})
        else:report=read_text(source,fmt,out)
    except Exception as e:
        (out/'failure.json').write_text(json.dumps({'error':str(e),'format':fmt,'input_files':inputs},ensure_ascii=False,indent=2),encoding='utf-8');raise
    report.update(input_files=inputs,status='decoded_not_assigned')
    (out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return report

def main():
    for stream in (sys.stdout,sys.stderr):
        if hasattr(stream,'reconfigure'):stream.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input');p.add_argument('--format',choices=FORMATS,default='auto');p.add_argument('--output',required=True);p.add_argument('--thermo-parser');p.add_argument('--centroid',action='store_true',help='Opt into vendor peak picking; default preserves profile data')
    a=p.parse_args();print(json.dumps(run(a.input,a.output,a.format,a.thermo_parser,a.centroid),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
