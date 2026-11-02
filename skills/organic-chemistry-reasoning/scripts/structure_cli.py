"""Portable structure normalization, drawing, conversion and offline image recognition.

Uses RDKit for chemistry and optional MolVec for local OCSR. Recognition produces
a candidate; compare bonds, labels and stereo with the input before adoption.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

def data_home():
    if os.environ.get('CHEM_WORKBENCH_HOME'): return Path(os.environ['CHEM_WORKBENCH_HOME']).expanduser()
    installed=Path(__file__).resolve().parents[3]/'dependencies/chem-workbench'
    if (installed/'workbench.json').is_file():return installed
    if os.environ.get('CODEX_HOME'): return Path(os.environ['CODEX_HOME'])/'dependencies/chem-workbench'
    if os.environ.get('DSH_HOME'): return Path(os.environ['DSH_HOME'])/'dependencies/chem-workbench'
    return Path.home()/'.local/share/chem-workbench'

def configuration(path=None):
    p=Path(path) if path else data_home()/'workbench.json'
    return json.loads(p.read_text(encoding='utf-8')) if p.is_file() else {}

def load_molecule(value):
    from rdkit import Chem
    p=Path(value)
    try: is_file=p.is_file()
    except OSError:is_file=False
    if is_file:
        if p.suffix.lower()=='.sdf':
            mols=list(Chem.SDMolSupplier(str(p),removeHs=False))
            if len(mols)!=1: raise ValueError('Expected one SDF record; split a batch explicitly.')
            mol=mols[0]
        elif p.suffix.lower() in {'.mol','.mdl'}:mol=Chem.MolFromMolFile(str(p),removeHs=False)
        else: raise ValueError('Use a MOL/SDF file or a SMILES string.')
    else: mol=Chem.MolFromSmiles(value)
    if mol is None: raise ValueError('Invalid/unsupported structure; source retained.')
    return mol

def identity(mol):
    from rdkit import Chem
    from rdkit.Chem import rdMolDescriptors
    return {'smiles':Chem.MolToSmiles(mol,isomericSmiles=True),'formula':rdMolDescriptors.CalcMolFormula(mol),'exact_mass':rdMolDescriptors.CalcExactMolWt(mol),'formal_charge':Chem.GetFormalCharge(mol),'atoms':mol.GetNumAtoms(),'unassigned_stereocentres':Chem.FindMolChiralCenters(mol,includeUnassigned=True)}

def draw(mol,output):
    from rdkit.Chem import Draw
    p=Path(output);p.parent.mkdir(parents=True,exist_ok=True)
    if p.suffix.lower() not in {'.svg','.png'}:raise ValueError('Drawing output must be .svg or .png')
    Draw.MolToFile(mol,str(p),size=(900,600))
    return str(p.resolve())

def recognize(image,config,output=None):
    from rdkit import Chem
    source=Path(image).resolve()
    if not source.is_file():raise FileNotFoundError(source)
    java=config.get('java') or shutil.which('java');jar=config.get('molvec_jar')
    if not java or not jar or not Path(jar).is_file():raise RuntimeError('MolVec not configured; run tools/workbench.py setup --profile ocsr --apply.')
    temp_parent=Path(output).resolve().parent if output else Path.cwd()
    temp_parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='chem-ocsr-',dir=temp_parent) as temp:
        molfile=Path(temp)/'candidate.mol'
        result=subprocess.run([str(java),'-Djava.awt.headless=true','-jar',str(jar),'-f',str(source),'-o',str(molfile)],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=120)
        if result.returncode or not molfile.exists():raise RuntimeError('MolVec failed: '+result.stderr[-1600:]+result.stdout[-1600:])
        mol=Chem.MolFromMolFile(str(molfile),removeHs=False)
        if mol is None:raise ValueError('OCSR produced an invalid molecular graph; inspect original image.')
        payload=identity(mol)|{'engine':'MolVec','version':config.get('molvec_version'),'status':'candidate_requires_review','input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'molfile':molfile.read_text(encoding='utf-8'),'limitations':['Not a reaction-scheme parser.','No assertion of correct abbreviation expansion or stereochemistry.']}
        if output:
            out=Path(output);out.parent.mkdir(parents=True,exist_ok=True)
            if out.suffix.lower()=='.mol':shutil.copyfile(molfile,out)
            else:out.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
    return payload

def selftest(config,output):
    from rdkit import Chem
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    results=[]
    for name,smiles in [('benzene','c1ccccc1'),('aspirin','CC(=O)Oc1ccccc1C(=O)O')]:
        mol=load_molecule(smiles);image=out/(name+'.png');draw(mol,image)
        row={'sample':name,'identity':identity(mol),'drawing':str(image.resolve())}
        if config.get('molvec_jar'):
            found=recognize(image,config,out/(name+'.ocsr.json'))
            row.update(ocsr_smiles=found['smiles'],connectivity_matches=Chem.MolToSmiles(Chem.MolFromSmiles(found['smiles']))==Chem.MolToSmiles(mol))
        results.append(row)
    report={'results':results,'scope':'Two synthetic images only; not an accuracy benchmark on research figures.'}
    (out/'selftest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    if any(r.get('connectivity_matches') is False for r in results):raise RuntimeError('OCSR smoke test mismatch; see '+str(out/'selftest.json'))
    return report

def main():
    for stream in (sys.stdout,sys.stderr):
        if hasattr(stream,'reconfigure'):stream.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',help='Machine-local workbench.json; never copy author drive paths')
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('doctor')
    q=sub.add_parser('info');q.add_argument('structure')
    q=sub.add_parser('draw');q.add_argument('structure');q.add_argument('--output',required=True)
    q=sub.add_parser('convert');q.add_argument('structure');q.add_argument('--output',required=True)
    q=sub.add_parser('ocsr');q.add_argument('image');q.add_argument('--output',required=True)
    q=sub.add_parser('selftest');q.add_argument('--output',required=True)
    a=p.parse_args();config=configuration(a.config)
    if a.command=='doctor':result={'rdkit_module':importlib.util.find_spec('rdkit') is not None,'java_file':bool(config.get('java') and Path(config['java']).is_file()),'molvec_file':bool(config.get('molvec_jar') and Path(config['molvec_jar']).is_file()),'ketcher_frontend':bool(config.get('ketcher_dist') and (Path(config['ketcher_dist'])/'index.html').is_file()),'status':'presence_only; run selftest for behavior'}
    elif a.command=='ocsr':result=recognize(a.image,config,a.output)
    elif a.command=='selftest':result=selftest(config,a.output)
    else:
        mol=load_molecule(a.structure);result=identity(mol)
        if a.command=='draw':result['output']=draw(mol,a.output)
        if a.command=='convert':
            from rdkit import Chem
            out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
            if out.suffix.lower()=='.mol':Chem.MolToMolFile(mol,str(out))
            elif out.suffix.lower()=='.sdf':
                with Chem.SDWriter(str(out)) as writer:writer.write(mol)
            elif out.suffix.lower() in {'.smi','.smiles'}:out.write_text(result['smiles']+'\n',encoding='utf-8')
            else:raise ValueError('Conversion supports MOL/SDF/SMI; 3D generation uses the computational conformer module.')
            result['output']=str(out.resolve())
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
