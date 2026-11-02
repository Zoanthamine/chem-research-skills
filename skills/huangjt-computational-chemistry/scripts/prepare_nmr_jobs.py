"""Prepare auditable Gaussian opt/freq and NMR inputs from selected XYZ conformers.

Does not submit jobs, invent shifts, choose an unverified calibration, or treat
xTB energies as DFT Gibbs free energies. Geometry and property settings remain explicit.
"""
from __future__ import annotations
import argparse,hashlib,json,math,re,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def xyz(path,charge,multiplicity):
    from rdkit import Chem
    lines=path.read_text(encoding='utf-8-sig').splitlines();n=int(lines[0]);atoms=[];pt=Chem.GetPeriodicTable()
    if len(lines)<n+2 or n<1:raise ValueError('Incomplete XYZ: '+str(path))
    for i,line in enumerate(lines[2:n+2],1):
        fields=line.split()
        if len(fields)<4:raise ValueError('Malformed XYZ atom '+str(i))
        element=fields[0];z=pt.GetAtomicNumber(element)
        coords=[float(v) for v in fields[1:4]]
        if not z or not all(math.isfinite(x) for x in coords):raise ValueError('Invalid atom/coordinate')
        atoms.append((element,coords,z))
    electrons=sum(a[2] for a in atoms)-charge
    if electrons<1 or multiplicity<1 or (electrons-(multiplicity-1))%2 or multiplicity-1>electrons:raise ValueError('Charge/multiplicity inconsistent with electron count')
    return atoms

def build(paths,out,charge,multiplicity,geometry_method,geometry_basis,property_method,property_basis,solvent,kind='shifts',cores=2,memory='2GB',cap=6):
    out=Path(out).resolve()
    if out.exists():raise FileExistsError('Use a new output directory')
    if not paths or len(paths)>cap:raise ValueError('Select 1..'+str(cap)+' conformers explicitly')
    if cores<1 or not re.fullmatch(r'\d+(MB|GB)',memory.upper()):raise ValueError('Invalid CPU/memory settings')
    for token in [geometry_method,geometry_basis,property_method,property_basis,solvent]:
        if not token or any(c in token for c in '\r\n#%'):raise ValueError('Use single-line Gaussian method/basis/solvent tokens')
    ids=[Path(p).stem for p in paths]
    if len(set(ids))!=len(ids) or any(not re.fullmatch(r'[\w.-]+',x) for x in ids):raise ValueError('Unique plain conformer IDs required')
    records=[];prepared=[]
    for path,cid in zip(paths,ids):
        path=Path(path).resolve(strict=True);atoms=xyz(path,charge,multiplicity)
        if kind in {'bally','du4'} and any(a[0] not in {'C','H','O'} for a in atoms):raise ValueError('Bundled coupling basis only supports C/H/O; review unsupported elements explicitly')
        geom_solvent='' if solvent.lower()=='gas' else f' SCRF=(SMD,Solvent={solvent})'
        if kind in {'bally','du4'}:
            if geometry_method.lower()!='b3lyp' or geometry_basis.lower()!='6-31g(d)':raise ValueError('Bundled FC protocols require their prescribed B3LYP/6-31G(d) geometry')
            geom_solvent=''
        coordinates='\n'.join(e+' '+ ' '.join(f'{v:.10f}' for v in pos) for e,pos,_ in atoms)
        opt=f'%chk=optfreq.chk\n%nprocshared={cores}\n%mem={memory}\n# {geometry_method}/{geometry_basis} Opt Freq SCF=XQC NoSymm{geom_solvent}\n\n{cid} opt/freq\n\n{charge} {multiplicity}\n{coordinates}\n\n'
        if kind=='shifts':
            route=f'{property_method}/{property_basis} NMR=GIAO Geom=AllCheck Guess=Read SCF=XQC NoSymm{geom_solvent}'
            prop=f'%oldchk=optfreq.chk\n%chk=nmr.chk\n%nprocshared={cores}\n%mem={memory}\n# {route}\n\n'
        else:
            basis=ROOT/'assets/basis'/('Bally-H-uplus1s.gbs' if kind=='bally' else 'DU4-CHO.gbs')
            # Gen/ReadAtoms needs the original, reviewed block, including blank lines.
            block=basis.read_text(encoding='utf-8').strip()+'\n\natoms=H\n\n'
            prop=f'%oldchk=optfreq.chk\n%chk=nmr.chk\n%nprocshared={cores}\n%mem={memory}\n# B3LYP/Gen NMR=(FCOnly,ReadAtoms) 6D Int=NoBasisTransform G09Defaults SCF=XQC NoSymm Geom=AllCheck Guess=Read\n\n'+block
        prepared.append((cid,opt,prop))
        records.append({'id':cid,'input':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'atoms':len(atoms),'charge':charge,'multiplicity':multiplicity,'atom_order':'XYZ row order, one-based in Gaussian','geometry':geometry_method+'/'+geometry_basis,'property':property_method+'/'+property_basis if kind=='shifts' else 'prescribed '+kind+' FC basis','solvent':solvent if kind=='shifts' else 'gas','frequency_required':True})
    out.mkdir(parents=True)
    for cid,opt,prop in prepared:
        target=out/cid;target.mkdir();(target/'01-optfreq.gjf').write_text(opt,encoding='utf-8');(target/'02-nmr.gjf').write_text(prop,encoding='utf-8')
    manifest={'kind':kind,'conformers':records,'submitted':False,'gates':['Review graph/stereo and XYZ atom mapping before running.','Confirm minimum/frequencies and intended geometry before property stage.','Do not run property stage unless its parent checkpoint is valid.','Output shieldings/FC first; apply only a matched calibration/reference and explicit ensemble weights.'],'solver':'Gaussian input syntax; Gaussian installation/license is separate.'}
    (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    return manifest

def main():
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('xyz',nargs='+');p.add_argument('--output',required=True);p.add_argument('--charge',type=int,required=True);p.add_argument('--multiplicity',type=int,required=True)
    p.add_argument('--geometry-method',required=True);p.add_argument('--geometry-basis',required=True);p.add_argument('--property-method',required=True);p.add_argument('--property-basis',required=True);p.add_argument('--solvent',required=True,help='Gaussian solvent name, or gas')
    p.add_argument('--kind',choices=['shifts','bally','du4'],default='shifts');p.add_argument('--cores',type=int,default=2);p.add_argument('--memory',default='2GB');p.add_argument('--cap',type=int,default=6)
    a=p.parse_args();result=build(a.xyz,a.output,a.charge,a.multiplicity,a.geometry_method,a.geometry_basis,a.property_method,a.property_basis,a.solvent,a.kind,a.cores,a.memory,a.cap);print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
