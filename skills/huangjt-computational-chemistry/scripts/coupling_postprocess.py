"""Scale one FC protocol at a time; optional signed, explicit conformer weighting."""
import argparse,csv,hashlib,json,math
from pathlib import Path
FITS={'sp3_general':(1.240,.57),'sp3_alpha_pi':(1.072,-1.66),'small_ring':(1.249,1.05),'sp2':(1.337,.52)}

def read(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def pair(row):
 a,b=int(row['H_a']),int(row['H_b'])
 if a<1 or b<1 or a==b:raise ValueError('Invalid one-based H pair')
 return tuple(sorted((a,b)))
def finite(v):
 f=float(v)
 if not math.isfinite(f):raise ValueError('Nonfinite value')
 return f
def process(raw,method,mapping=None,weights=None):
 if method not in ('bally','du4'):raise ValueError('Unknown protocol')
 if not raw:raise ValueError('Empty raw matrix')
 rows={};sets={}
 for r in raw:
  cid=r['conformer'].strip();key=pair(r)
  if not cid or (cid,key) in rows:raise ValueError('Blank ID or duplicate unordered pair')
  rows[cid,key]=finite(r['FC_raw_Hz']);sets.setdefault(cid,set()).add(key)
 if any(s!=next(iter(sets.values())) for s in sets.values()):raise ValueError('Missing conformer pair values')
 maprows={}
 if method=='du4':
  if not mapping:raise ValueError('DU4 needs explicitly reviewed CH2 mapping')
  for r in mapping:
   key=pair(r)
   if key in maprows or r['environment'] not in FITS:raise ValueError('Duplicate mapping or unsupported environment')
   carbon=int(r['carbon_atom']);flag=str(r['extrapolative']).lower()
   if carbon<1 or carbon in key or flag not in ('true','false'):raise ValueError('Invalid CH2 metadata')
   maprows[key]={'carbon_atom':carbon,'environment':r['environment'],'extrapolative':flag=='true'}
  if not maprows.keys()<=next(iter(sets.values())):raise ValueError('Mapped CH2 absent from FC matrix')
 targets=sorted(maprows if method=='du4' else next(iter(sets.values())))
 jcol='J_Bally_Hz' if method=='bally' else 'J_DU4_Hz';out=[]
 for cid in sorted(sets):
  for key in targets:
   fc=rows[cid,key];meta=maprows.get(key,{})
   slope,intercept=(.9155,0.) if method=='bally' else FITS[meta['environment']]
   out.append(dict(conformer=cid,H_a=key[0],H_b=key[1],**meta,FC_raw_Hz=fc,slope=slope,intercept_Hz=intercept,**{jcol:slope*fc+intercept}))
 averaged=[]
 if weights is not None:
  if set(weights)!=set(sets):raise ValueError('Weight IDs do not match input conformers')
  weights={k:finite(v) for k,v in weights.items()}
  if any(v<0 for v in weights.values()) or abs(sum(weights.values())-1)>1e-7:raise ValueError('Weights must be normalized, finite and nonnegative')
  for key in targets:
   value=sum(weights[r['conformer']]*r[jcol] for r in out if (r['H_a'],r['H_b'])==key)
   averaged.append(dict(H_a=key[0],H_b=key[1],**maprows.get(key,{}),**{jcol:value,'abs_'+jcol:abs(value)}))
 return out,averaged
def write(path,rows):
 with path.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--method',choices=['bally','du4'],required=True);p.add_argument('--raw',type=Path,required=True);p.add_argument('--map',type=Path);p.add_argument('--weights',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.out.exists():raise ValueError('Output exists; choose a new output directory')
 weights=json.loads(a.weights.read_text(encoding='utf-8-sig')) if a.weights else None
 rows,avg=process(read(a.raw),a.method,read(a.map) if a.map else None,weights)
 a.out.mkdir(parents=True);write(a.out/'per-conformer.csv',rows)
 if avg:write(a.out/'weighted.csv',avg)
 inputs=[a.raw,*([a.map] if a.map else []),*([a.weights] if a.weights else [])]
 (a.out/'provenance.json').write_text(json.dumps({'method':a.method,'input_sha256':{str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in inputs},'weights':weights,'signed':True,'method_averaging':False,'CH2_connectivity':'User-reviewed mapping required; not inferred by this script','citation':'10.1021/jo200513q' if a.method=='bally' else '10.1021/jo501781b'},indent=2),encoding='utf-8')
 print(json.dumps({'per_conformer_rows':len(rows),'weighted_pairs':len(avg),'method':a.method}))
if __name__=='__main__':main()
