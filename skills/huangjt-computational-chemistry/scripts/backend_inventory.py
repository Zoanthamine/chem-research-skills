"""Inspect configured executable availability without launching software or network."""
import argparse,json,shutil,sys
from pathlib import Path

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--config',type=Path,required=True);a=p.parse_args()
 cfg=json.loads(a.config.read_text(encoding='utf-8-sig'));rows={}
 for name,path in cfg.get('executables',{}).items():
  found=(str(Path(path).resolve()) if Path(path).is_file() else shutil.which(path)) if path else None
  rows[name]={'configured':bool(path),'available':bool(found),'path':found,'launched':False}
 print(json.dumps({'capabilities':rows,'network_used':False,'license_validated':False},indent=2))
if __name__=='__main__':main()
