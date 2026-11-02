"""Run one prepared conformer's Gaussian stages, preserving inputs and all logs.

Opt/freq must finish as a minimum before the separate NMR stage. No scheduler or
SSH is used. The caller must have authorized these local computations.
"""
from pathlib import Path
import argparse,csv,hashlib,json,os,re,subprocess,sys

def run(directory,gaussian,stage,timeout=1800):
    directory=Path(directory).resolve(strict=True);exe=Path(gaussian).resolve(strict=True)
    if stage=='nmr':
        parent=directory/'01-optfreq.log'
        text=parent.read_text(encoding='utf-8',errors='replace')
        frequencies=[float(x.replace('D','E')) for line in re.findall(r'Frequencies\s+--\s*([^\n]+)',text) for x in line.split()]
        if 'Normal termination' not in text or not frequencies or any(v<0 for v in frequencies):raise ValueError('Parent geometry lacks a normal minimum/frequency result; inspect it before NMR')
        if not (directory/'optfreq.chk').is_file():raise ValueError('Missing parent checkpoint')
    stem='01-optfreq' if stage=='optfreq' else '02-nmr'
    inp=directory/(stem+'.gjf');log=directory/(stem+'.log');receipt=directory/(stem+'.receipt.json')
    if log.exists() or receipt.exists():raise FileExistsError('Use a fresh job directory; existing result retained')
    scratch=directory/(stem+'-scratch');scratch.mkdir()
    env=os.environ.copy();env.update(GAUSS_EXEDIR=str(exe.parent),GAUSS_SCRDIR=str(scratch),PATH=str(exe.parent)+os.pathsep+env.get('PATH',''))
    record={'stage':stage,'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),'executable':str(exe),'command':[str(exe),inp.name,log.name],'state':'running'}
    receipt.write_text(json.dumps(record,indent=2),encoding='utf-8')
    try:
        with (directory/(stem+'.console.txt')).open('w',encoding='utf-8') as console:
            child=subprocess.run(record['command'],cwd=directory,env=env,stdout=console,stderr=subprocess.STDOUT,timeout=timeout,check=False,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        text=log.read_text(encoding='utf-8',errors='replace') if log.exists() else ''
        if child.returncode or 'Normal termination' not in text:raise RuntimeError('Gaussian did not terminate normally; inspect retained logs')
        if stage=='optfreq':
            frequencies=[float(x.replace('D','E')) for line in re.findall(r'Frequencies\s+--\s*([^\n]+)',text) for x in line.split()]
            if not frequencies or any(v<0 for v in frequencies):raise ValueError('Not a verified minimum; inspect frequency modes')
            record['frequencies_cm-1']=frequencies
        else:
            values=re.findall(r'^\s*(\d+)\s+([A-Z][a-z]?)\s+Isotropic\s*=\s*([-+0-9.DEde]+)',text,re.M)
            if not values:raise ValueError('No isotropic shieldings parsed; do not invent shifts')
            with (directory/'shieldings.csv').open('w',newline='',encoding='utf-8') as out:
                writer=csv.writer(out);writer.writerow(['atom_id','element','shielding_ppm']);writer.writerows((i,e,float(v.replace('D','E'))) for i,e,v in values)
            record['shieldings']=len(values);record['chemical_shifts']='not derived; matched reference/calibration required'
        record.update(state='completed',log_sha256=hashlib.sha256(log.read_bytes()).hexdigest())
    except Exception as error:record.update(state='failed',error=str(error));raise
    finally:receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    return record
def main():
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('directory');p.add_argument('--gaussian',required=True);p.add_argument('--stage',choices=['optfreq','nmr'],required=True);p.add_argument('--timeout',type=int,default=1800);a=p.parse_args();print(json.dumps(run(a.directory,a.gaussian,a.stage,a.timeout),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
