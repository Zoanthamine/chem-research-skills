"""Prepare or execute a local xTB/GROMACS sampling job in a new directory.

GROMACS requires a reviewed, molecule-specific topology and MDP; this tool never
reuses another molecule's RESP charges. Plans do not run until --execute is set.
"""
from __future__ import annotations
import argparse,hashlib,json,math,os,re,shutil,subprocess,sys
from pathlib import Path

def executable(value):
    found=str(Path(value).resolve()) if Path(value).is_file() else shutil.which(value)
    if not found:raise FileNotFoundError('Executable not configured: '+value)
    return found
def record(p):
    p=Path(p).resolve(strict=True);return {'source':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def topology_includes(source,destination,seen):
    source=source.resolve()
    if source in seen:return
    seen.add(source)
    for name in re.findall(r'^\s*#include\s+"([^"]+)"',source.read_text(encoding='utf-8'),re.M):
        rel=Path(name)
        if rel.is_absolute() or '..' in rel.parts:raise ValueError('Use a self-contained topology or installed force-field paths')
        candidate=source.parent/rel
        if candidate.is_file():
            out=destination.parent/rel;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(candidate,out);topology_includes(candidate,out,seen)
        # Installed .ff include paths are resolved by grompp; warnings are never suppressed.
def prepare(a):
    out=Path(a.output).resolve()
    if out.exists():raise FileExistsError('Choose a new output directory')
    source=Path(a.input).resolve(strict=True)
    if a.backend=='xtb':
        if source.suffix.lower()!='.xyz':raise ValueError('xTB sampling requires validated XYZ and a retained graph/atom map')
        if a.charge is None or a.unpaired is None:raise ValueError('Explicit charge and unpaired electrons required')
        if any(v is None or not math.isfinite(v) or v<=0 for v in [a.time_ps,a.temperature,a.step_fs]):raise ValueError('Explicit positive MD time, temperature and timestep required')
        binary=executable(a.executable or os.environ.get('CODEX_CHEM_XTB_PATH','xtb'))
        control=f'$md\n temp={a.temperature}\n time={a.time_ps}\n step={a.step_fs}\n dump=100\n hmass=0\n shake=0\n nvt=true\n$end\n'
        commands=[[binary,'start.xyz','--gfnff','--chrg',str(a.charge),'--uhf',str(a.unpaired),'--md','--input','md.inp']]
        inputs=[record(source)];expected=['xtb.trj']
    else:
        if not a.topology or not a.mdp:raise ValueError('GROMACS requires reviewed topology and MDP for this molecule')
        binary=executable(a.executable or 'gmx');top=Path(a.topology).resolve(strict=True);mdp=Path(a.mdp).resolve(strict=True)
        if a.threads<1:raise ValueError('Positive thread count required')
        commands=[[binary,'grompp','-f','search.mdp','-c','start'+source.suffix,'-p','topol.top','-o','search.tpr'],[binary,'mdrun','-deffnm','search','-ntmpi','1','-ntomp',str(a.threads)], [binary,'trjconv','-s','search.tpr','-f','search.xtc','-o','frames.pdb','-dt',str(a.frame_interval)]]
        inputs=[record(p) for p in [source,top,mdp]];expected=['search.tpr','search.gro','search.xtc','frames.pdb']
    out.mkdir(parents=True)
    if a.backend=='xtb':shutil.copy2(source,out/'start.xyz');(out/'md.inp').write_text(control,encoding='ascii')
    else:
        shutil.copy2(source,out/('start'+source.suffix));shutil.copy2(top,out/'topol.top');shutil.copy2(mdp,out/'search.mdp');topology_includes(top,out/'topol.top',set())
    plan={'backend':a.backend,'inputs':inputs,'commands':commands,'expected_outputs':expected,'execute':a.execute,'limits':['Sampling candidates are not equilibrium populations or guaranteed global coverage.','Inspect atom order, connectivity and stereo after sampling and optimization.','GROMACS MDP must explicitly write XTC for frame extraction.','Run xTB refinement/ranking before selecting up to the agreed number of DFT candidates.'],'state':'prepared'}
    (out/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    if a.execute:
        env=os.environ.copy();env['OMP_NUM_THREADS']=str(a.threads)
        try:
            for i,command in enumerate(commands):
                with (out/f'stage-{i+1}.log').open('w',encoding='utf-8') as log:
                    subprocess.run(command,cwd=out,env=env,input='0\n' if a.backend=='gromacs' and i==2 else None,text=True,stdout=log,stderr=subprocess.STDOUT,timeout=a.timeout,check=True)
            missing=[f for f in expected if not (out/f).is_file() or not (out/f).stat().st_size]
            if missing:raise RuntimeError('Missing expected output: '+','.join(missing))
            plan['state']='completed_candidates_require_chemical_review'
        except Exception as exc:plan.update(state='failed',error=str(exc));raise
        finally:(out/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    return plan
def main():
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--backend',choices=['xtb','gromacs'],required=True);p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--executable');p.add_argument('--charge',type=int);p.add_argument('--unpaired',type=int);p.add_argument('--time-ps',type=float);p.add_argument('--temperature',type=float);p.add_argument('--step-fs',type=float);p.add_argument('--topology');p.add_argument('--mdp');p.add_argument('--threads',type=int,default=2);p.add_argument('--frame-interval',type=float,default=1.0);p.add_argument('--timeout',type=int,default=600);p.add_argument('--execute',action='store_true');a=p.parse_args();print(json.dumps(prepare(a),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
