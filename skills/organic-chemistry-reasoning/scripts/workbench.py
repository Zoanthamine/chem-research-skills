"""Find bundled capabilities and configure a small, machine-local chemistry workbench.

Default commands inspect/plan only. setup --apply installs the selected profile;
optional solvers, accounts and clusters are never installed by the base profile.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, platform, shutil, subprocess, sys, tarfile, urllib.request, venv, zipfile
from pathlib import Path, PurePosixPath

SKILL=Path(__file__).resolve().parents[1]
ROOT=SKILL.parent.parent
PROFILES={
 'foundation':{'packages':['rdkit','Pillow'],'modules':['rdkit','PIL']},
 'spectra':{'packages':['numpy','scipy','matplotlib','nmrglue'],'modules':['numpy','scipy','matplotlib','nmrglue']},
 'crystal':{'packages':['gemmi','numpy','requests'],'modules':['gemmi','numpy','requests']},
 'documents':{'packages':['python-docx','python-pptx','pypdf','Pillow'],'modules':['docx','pptx','pypdf','PIL']},
 'ocsr':{'packages':['rdkit','Pillow'],'modules':['rdkit','PIL']},
}
MOLVEC_URL='https://repo.maven.apache.org/maven2/gov/nih/ncats/molvec/0.9.8/molvec-0.9.8-jar-with-dependencies.jar'
MOLVEC_SHA='7012c1fa602e54c68bbac60d3ea737b400b698ba60e99c7bb0beffc88ebe2b19'

def data_home(value=None):
    if value:return Path(value).expanduser().resolve()
    if os.environ.get('CHEM_WORKBENCH_HOME'):return Path(os.environ['CHEM_WORKBENCH_HOME']).expanduser().resolve()
    installed=Path(__file__).resolve().parents[3]/'dependencies/chem-workbench'
    if (installed/'workbench.json').is_file():return installed
    if os.environ.get('CODEX_HOME'):return Path(os.environ['CODEX_HOME']).expanduser().resolve()/'dependencies/chem-workbench'
    if os.environ.get('DSH_HOME'):return Path(os.environ['DSH_HOME']).expanduser().resolve()/'dependencies/chem-workbench'
    return Path.home()/'.local/share/chem-workbench'

def load(home):
    p=home/'workbench.json'
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}

def download(url,path,expected=None):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists() and expected and hashlib.sha256(path.read_bytes()).hexdigest()==expected:return path
    part=path.with_suffix(path.suffix+'.part')
    request=urllib.request.Request(url,headers={'User-Agent':'chem-research-skills/1.1'})
    with urllib.request.urlopen(request,timeout=60) as response,part.open('wb') as out:
        while chunk:=response.read(1024*1024):out.write(chunk)
    if expected and hashlib.sha256(part.read_bytes()).hexdigest()!=expected:raise ValueError('Download checksum mismatch: '+url)
    part.replace(path);return path

def safe_extract(archive,destination):
    destination=destination.resolve();destination.mkdir(parents=True,exist_ok=True)
    def checked(name):
        # Reject Windows absolute paths and backslash traversal on all hosts.
        if '\\' in name or ':' in name or PurePosixPath(name).is_absolute():raise ValueError('Unsafe archive member')
        p=(destination/name).resolve()
        if not p.is_relative_to(destination):raise ValueError('Archive escapes destination')
        return p
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as z:
            for item in z.infolist():
                out=checked(item.filename)
                if (item.external_attr>>16)&0o170000==0o120000:raise ValueError('Archive symlink refused')
                if item.is_dir():out.mkdir(parents=True,exist_ok=True);continue
                out.parent.mkdir(parents=True,exist_ok=True)
                with z.open(item) as src,out.open('wb') as dst:shutil.copyfileobj(src,dst)
                mode=(item.external_attr>>16)&0o777
                if mode:out.chmod(mode)
    else:
        with tarfile.open(archive) as tar:
            for item in tar:
                out=checked(item.name)
                if item.isdir():out.mkdir(parents=True,exist_ok=True);continue
                if not item.isfile():raise ValueError('Archive links/devices refused')
                out.parent.mkdir(parents=True,exist_ok=True)
                with tar.extractfile(item) as src,out.open('wb') as dst:shutil.copyfileobj(src,dst)
                out.chmod(item.mode&0o777)

def probe_python(python,modules):
    code='import importlib.util,json; print(json.dumps({n:importlib.util.find_spec(n) is not None for n in '+repr(modules)+'}))'
    return json.loads(subprocess.check_output([str(python),'-c',code],text=True,encoding='utf-8'))

def setup(args):
    home=data_home(args.data_dir);conf=load(home);spec=PROFILES[args.profile]
    python=Path(args.python or conf.get('python') or sys.executable).resolve()
    available=probe_python(python,spec['modules'])
    plan={'profile':args.profile,'data_directory':str(home),'python':str(python),'existing_modules':available,'missing':[n for n,v in available.items() if not v],'optional_cluster':False,'will_install':bool(args.apply)}
    if not args.apply:return plan
    home.mkdir(parents=True,exist_ok=True)
    if not all(available.values()):
        # Do not change an existing shared Python environment to satisfy one profile.
        environment=home/'environments'/args.profile
        python=environment/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
        if not python.exists():
            subprocess.run([args.python or sys.executable,'-m','venv',str(environment)],check=True)
        subprocess.run([str(python),'-m','pip','install',*spec['packages']],check=True)
        if not all(probe_python(python,spec['modules']).values()):raise RuntimeError('Installed profile did not pass presence checks')
    conf.setdefault('profiles',{})[args.profile]={'python':str(python),'packages':spec['packages']}
    if args.profile in {'foundation','ocsr'}:conf['python']=str(python)
    if args.ketcher_dist:
        ketcher=Path(args.ketcher_dist).resolve()
        if not (ketcher/'index.html').is_file():raise ValueError('Ketcher frontend index.html missing')
        conf['ketcher_dist']=str(ketcher)
    if args.profile=='ocsr':
        jar=download(MOLVEC_URL,home/'binaries/molvec-0.9.8.jar',MOLVEC_SHA)
        java=conf.get('java') or shutil.which('java')
        if not java:
            system={'Windows':'windows','Linux':'linux','Darwin':'mac'}.get(platform.system())
            arch={'AMD64':'x64','x86_64':'x64','arm64':'aarch64','aarch64':'aarch64'}.get(platform.machine())
            if not system or not arch:raise RuntimeError('Configure an existing Java runtime for this platform')
            url=f'https://api.adoptium.net/v3/assets/latest/21/hotspot?architecture={arch}&heap_size=normal&image_type=jre&jvm_impl=hotspot&os={system}&vendor=eclipse'
            request=urllib.request.Request(url,headers={'User-Agent':'chem-research-skills/1.1'})
            with urllib.request.urlopen(request,timeout=45) as response:package=json.load(response)[0]['binary']['package']
            archive=download(package['link'],home/'downloads'/package['name'],package['checksum'])
            safe_extract(archive,home/'java')
            found=sorted((home/'java').rglob('java.exe' if os.name=='nt' else 'java'))
            found=[p for p in found if p.parent.name=='bin' and p.is_file()]
            if not found:raise RuntimeError('Downloaded JRE has no java executable')
            java=str(found[0]);conf['java_download']={'url':package['link'],'sha256':package['checksum']}
        subprocess.run([java,'-version'],check=True,capture_output=True)
        conf.update(java=str(java),molvec_jar=str(jar),molvec_version='0.9.8',molvec_sha256=MOLVEC_SHA)
    target=home/'workbench.json';temp=home/'workbench.json.new'
    temp.write_text(json.dumps(conf,ensure_ascii=False,indent=2),encoding='utf-8');temp.replace(target)
    return plan|{'configured':str(target),'python':str(python),'verification':'Run verify to test behavior; installation alone is not validation.'}

def catalog(args):
    rows=json.loads((SKILL/'assets/module-catalog.json').read_text(encoding='utf-8'))
    query=(args.query or '').casefold()
    selected=[r for r in rows if query in json.dumps(r,ensure_ascii=False).casefold()]
    if args.details:return selected
    return [{'owner':r['owner'],'module':r['module'],'description':r['description'][:240],'workflow':r['workflow'],'scripts':len(r['scripts']),'references':len(r['references']),'templates':len(r['templates']),'delivery':r['delivery']} for r in selected]

def fetch_source(args):
    evidence={r['key']:r for r in json.loads((SKILL/'assets/upstream-evidence.json').read_text(encoding='utf-8'))}
    row=evidence[args.source];home=data_home(args.data_dir)
    destination=home/'sources'/row['key']/row['commit']
    if destination.exists():return {'source':row['repo'],'path':str(destination),'existing':True}
    archive=download(f"https://codeload.github.com/{row['repo']}/zip/{row['commit']}",home/'downloads'/(row['key']+'-'+row['commit']+'.zip'))
    safe_extract(archive,destination)
    return {'source':row['repo'],'revision':row['commit'],'path':str(destination),'executed':False,'note':'Original source retained separately; no additional skill registration or upstream installer execution.'}

def main():
    for stream in (sys.stdout,sys.stderr):
        if hasattr(stream,'reconfigure'):stream.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    q=sub.add_parser('search');q.add_argument('query',nargs='?',default='');q.add_argument('--details',action='store_true')
    q=sub.add_parser('setup');q.add_argument('--profile',choices=PROFILES,default='foundation');q.add_argument('--data-dir');q.add_argument('--python');q.add_argument('--ketcher-dist');q.add_argument('--apply',action='store_true')
    q=sub.add_parser('verify');q.add_argument('--data-dir');q.add_argument('--output',required=True)
    q=sub.add_parser('fetch-source');q.add_argument('source',choices=['hpc','office','organic','paper','conformer','crystal','ars','nature']);q.add_argument('--data-dir')
    a=p.parse_args()
    if a.command=='setup':result=setup(a)
    elif a.command=='search':result=catalog(a)
    elif a.command=='fetch-source':result=fetch_source(a)
    else:
        home=data_home(a.data_dir);conf=load(home)
        script=SKILL/'scripts/structure_cli.py'
        subprocess.run([conf.get('python') or sys.executable,str(script),'--config',str(home/'workbench.json'),'selftest','--output',a.output],check=True)
        result={'verified_output':str(Path(a.output).resolve())}
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
