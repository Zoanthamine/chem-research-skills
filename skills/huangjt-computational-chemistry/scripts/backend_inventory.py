"""Inspect configured executable availability without launching software or network."""
import argparse,json,shutil,sys
from pathlib import Path

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--config',type=Path,required=True);a=p.parse_args()
 cfg=json.loads(a.config.read_text(encoding='utf-8-sig'));rows={}
 executables=dict(cfg.get('executables',{}));executables.update(cfg.get('tools',{}))
 for name,key in [('xtb','CODEX_CHEM_XTB_PATH')]:
  if cfg.get('shared_environment',{}).get(key):executables[name]=cfg['shared_environment'][key]
 for runtime in cfg.get('environments',[]):
  if runtime.get('key')=='dials':executables['dials_python']=runtime.get('python')
 for name,path in executables.items():
  if not isinstance(path,str):continue
  found=(str(Path(path).resolve()) if Path(path).is_file() else shutil.which(path)) if path else None
  rows[name]={'configured':bool(path),'available':bool(found),'path':found,'launched':False}
 print(json.dumps({'capabilities':rows,'network_used':False,'license_validated':False},indent=2))
if __name__=='__main__':main()
