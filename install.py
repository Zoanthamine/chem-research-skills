"""Install the six chemistry/research skills for Codex or DeepSeek Harness."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,re,shutil,sys

NAMES=['scxrd-refinement','huangjt-computational-chemistry','huangjt-spectral-structure-analysis','organic-chemistry-reasoning','huangjt-academic-research','huangjt-academic-writing']
BEGIN='<!-- huangjt-chemistry-defaults:begin -->'
END='<!-- huangjt-chemistry-defaults:end -->'

def fingerprint(root):
    h=hashlib.sha256()
    for p in sorted(root.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts:
            h.update(p.relative_to(root).as_posix().encode());h.update(hashlib.sha256(p.read_bytes()).digest())
    return h.hexdigest()

def verify(root):
    records=json.loads((root/'MANIFEST.json').read_text(encoding='utf-8'))
    expected=set()
    for row in records:
        p=(root/row['path']).resolve()
        if not p.is_relative_to(root.resolve()) or not p.is_file():raise ValueError('Missing/unsafe file: '+row['path'])
        content=p.read_bytes()
        if row.get('normalize_lf'):content=content.replace(b'\r\n',b'\n')
        if hashlib.sha256(content).hexdigest()!=row['sha256']:raise ValueError('Checksum mismatch: '+row['path'])
        expected.add(p)
    actual={p.resolve() for p in root.rglob('*') if p.is_file() and p!=root/'MANIFEST.json' and not any(x in p.relative_to(root).parts for x in {'.git','__pycache__','.venv'})}
    if actual!=expected:raise ValueError('Unexpected package files; use a clean checkout or release extraction')
    for name in NAMES:
        if not (root/'skills'/name/'SKILL.md').is_file():raise ValueError('Missing skill: '+name)
    nested=list((root/'skills').rglob('SKILL.md'))
    if len(nested)!=6:raise ValueError('Expected exactly six registered skills')
    return len(records)

def profile(host,args):
    if host=='codex':
        # Codex's standard user skill directory is AGENTS_HOME/skills.
        agent_home=Path(os.environ.get('AGENTS_HOME',str(Path.home()/'.agents'))).expanduser()
        codex_home=Path(args.codex_home or os.environ.get('CODEX_HOME',str(Path.home()/'.codex'))).expanduser()
        return Path(args.target).expanduser() if args.target else agent_home/'skills',codex_home/'AGENTS.md'
    dsh_home=Path(args.dsh_home or os.environ.get('DSH_HOME',str(Path.home()/'.dsh'))).expanduser()
    return Path(args.target).expanduser() if args.target else dsh_home/'skills',dsh_home/'AGENTS.md'

def route_block(root,template):return BEGIN+'\n'+template.replace('{{SKILL_ROOT}}',root.resolve().as_posix()).strip()+'\n'+END+'\n'

def write_defaults(p,root,template,backup):
    existing=p.read_text(encoding='utf-8-sig') if p.exists() else ''
    block=route_block(root,template)
    if BEGIN in existing:
        if END not in existing:raise ValueError('Incomplete managed global block: '+str(p))
        updated=re.sub(re.escape(BEGIN)+r'[\s\S]*?'+re.escape(END)+r'\n?',lambda _:block,existing,count=1)
    else:updated=block+'\n'+existing
    if updated==existing:return
    if p.exists():
        target=backup/'instructions'/p.parent.name/p.name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(updated,encoding='utf-8')

def install(root,targets,args):
    stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    actions=[]
    for host,(target,instructions) in targets:
        target=target.resolve();marker=target/'.huangjt-chemistry-install.json'
        managed=json.loads(marker.read_text(encoding='utf-8')) if marker.exists() else {}
        for name in NAMES:
            dst=target/name
            if dst.exists():
                same=fingerprint(dst)==fingerprint(root/'skills'/name)
                if not same and not args.replace:raise FileExistsError('Existing different skill; compare first, or use --replace to back it up: '+str(dst))
            actions.append((host,target,instructions,name))
        if instructions.exists() and BEGIN in instructions.read_text(encoding='utf-8-sig') and END not in instructions.read_text(encoding='utf-8-sig'):raise ValueError('Incomplete managed instruction block: '+str(instructions))
    backups={}
    for host,target,instructions,name in actions:
        backup=backups.setdefault(str(target),target.parent/'chemistry-skill-backups'/stamp)
        if not backup.resolve().is_relative_to(target.parent.resolve()):raise ValueError('Backup escapes the selected installation parent')
        dst=target/name;src=root/'skills'/name
        if dst.exists() and fingerprint(dst)==fingerprint(src):continue
        target.mkdir(parents=True,exist_ok=True)
        if dst.exists():
            # Rename only the exact checked child; never recursively delete a target.
            if dst.parent.resolve()!=target:raise ValueError('Unsafe target parent')
            archived=backup/'skills'/name
            if not archived.resolve().is_relative_to(backup.resolve()):raise ValueError('Unsafe backup target')
            archived.parent.mkdir(parents=True,exist_ok=True);dst.rename(archived)
        shutil.copytree(src,dst)
    for host,(target,instructions) in targets:
        target=target.resolve();backup=backups[str(target)]
        marker={'package':'huangjt-chemistry-skills','version':(root/'VERSION').read_text(encoding='utf-8').strip() if (root/'VERSION').exists() else 'unversioned','host':host,'fingerprints':{n:fingerprint(target/n) for n in NAMES}}
        (target/'.huangjt-chemistry-install.json').write_text(json.dumps(marker,ensure_ascii=False,indent=2),encoding='utf-8')
        if not args.no_defaults:write_defaults(instructions,target,(root/'routing/global-defaults.md').read_text(encoding='utf-8'),backup)
    return [{'host':host,'skills':str(target.resolve()),'global_instructions':str(instructions),'defaults_installed':not args.no_defaults} for host,(target,instructions) in targets]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--host',choices=['codex','dsh','both'],default='codex')
    p.add_argument('--target',help='Explicit skill directory; use with a single host')
    p.add_argument('--codex-home');p.add_argument('--dsh-home')
    p.add_argument('--check',action='store_true');p.add_argument('--replace',action='store_true',help='Back up different existing skills before replacing them')
    p.add_argument('--no-defaults',action='store_true',help='Install skills without adding the managed global routing block')
    a=p.parse_args();root=Path(__file__).resolve().parent
    count=verify(root)
    if a.check:print(json.dumps({'verified_files':count,'skills':NAMES,'installed':False}));return
    if a.host=='both' and a.target:p.error('--target requires a single --host')
    hosts=['codex','dsh'] if a.host=='both' else [a.host]
    targets=[(h,profile(h,a)) for h in hosts]
    print(json.dumps({'installation':install(root,targets,a),'refresh':'Start a new chat or refresh the skill catalog'},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
