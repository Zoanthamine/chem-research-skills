"""Portable numerical evidence helpers. No automatic structural assignment."""
import argparse,json,re,sys,importlib.util,platform
from pathlib import Path
M={'C':12.,'H':1.00782503223,'N':14.00307400443,'O':15.99491461957,'S':31.9720711744,'F':18.99840316273,'Cl':34.968852682,'Br':78.9183376,'P':30.97376199842,'Si':27.97692653465}
def masses(formula):
 parts=re.findall(r'([A-Z][a-z]?)(\d*)',formula)
 if ''.join(e+n for e,n in parts)!=formula or not parts:raise ValueError('Unsupported formula syntax')
 if any(e not in M or (n and int(n)<1) for e,n in parts):raise ValueError('Unsupported element/count')
 mass=sum(M[e]*int(n or 1)for e,n in parts)
 return {'formula':formula,'neutral_monoisotopic_Da':mass,'positive_singly_charged_mz':{k:mass+v for k,v in {'M+H':1.007276466621,'M+NH4':18.033825553,'M+Na':22.989220702,'M+K':38.963157906}.items()}}
def effective(weights,distances):
 import numpy as np
 w=np.asarray(weights,float);d=np.asarray(distances,float)
 if w.ndim!=1 or d.ndim!=2 or d.shape[1]!=len(w)or not np.all(np.isfinite(w))or not np.all(np.isfinite(d))or (w<0).any()or(d<=0).any()or abs(w.sum()-1)>1e-6:raise ValueError('Require normalized nonnegative weights and positive pair-by-conformer distances')
 return (np.sum(w*d**-6,axis=1)**(-1/6)).tolist()
def integrate(data,x,y,signals,pairs,scales=(.8,1.,1.2)):
 import numpy as np
 z=np.asarray(data,float);x=np.asarray(x,float);y=np.asarray(y,float)
 if x.ndim!=1 or y.ndim!=1 or z.shape!=(len(y),len(x))or min(len(x),len(y))<3:raise ValueError('Expected data(y,x) and 1D axes')
 for a in [x,y]:
  dd=np.diff(a)
  if not(np.all(dd>0)or np.all(dd<0))or not np.allclose(dd,dd[0],rtol=1e-4,atol=1e-10):raise ValueError('Need monotonic uniform ppm axes')
 if not np.isfinite(z).all():raise ValueError('Nonfinite spectrum')
 ans=[]
 for a,b in pairs:
  for scale in scales:
   vs=[]
   for q,r in [(a,b),(b,a)]:
    cx,wx=signals[q];cy,wy=signals[r];wx*=scale;wy*=scale
    if wx<=0 or wy<=0:raise ValueError('Positive halfwidth required')
    ix=abs(x-cx)<wx;iy=abs(y-cy)<wy;ox=abs(x-cx)<2*wx;oy=abs(y-cy)<2*wy
    if not ix.any()or not iy.any():raise ValueError('Empty window')
    # Background ring excludes signal box, unlike a whole-box median.
    outer=z[np.ix_(oy,ox)];ring=~((abs(y[oy]-cy)<wy)[:,None]&(abs(x[ox]-cx)<wx)[None,:])
    if not ring.any():raise ValueError('No background ring')
    bg=float(np.median(outer[ring]));v=float((z[np.ix_(iy,ix)]-bg).sum()*abs(x[1]-x[0])*abs(y[1]-y[0]));vs.append(v)
   ans.append({'a':a,'b':b,'window_scale':scale,'signed_ab':vs[0],'signed_ba':vs[1],'mean_signed':sum(vs)/2,'note':'Uncalibrated crosspeak volume; not distance or assignment'})
 return ans
def selftest():
 import numpy as np
 assert abs(masses('C27H34O7')['neutral_monoisotopic_Da']-470.23045343281)<1e-8
 assert 2.23<effective([.5,.5],[[2,4]])[0]<2.25
 x=np.linspace(0,8,801);xx,yy=np.meshgrid(x,x);z=7-100*np.exp(-((xx-2)**2+(yy-6)**2)/.003)-100*np.exp(-((xx-6)**2+(yy-2)**2)/.003)
 r=integrate(z,x,x,{'a':[2,.1],'b':[6,.1]},[['a','b']]);assert all(v['signed_ab']<0 and abs(v['signed_ab']-v['signed_ba'])<1e-9 for v in r)
 # Wrong axes and non-normalized ensembles must fail instead of silently normalizing.
 for w,d in [([.2],[[2]]),([1],[[-2]])]:
  try:effective(w,d)
  except ValueError:pass
  else:raise AssertionError('invalid ensemble accepted')
 return {'status':'passed','checks':['formula/adduct','r^-6 average','signed reciprocal integration with background','invalid weights/distances']}
def main():
 p=argparse.ArgumentParser();sub=p.add_subparsers(dest='cmd',required=True)
 sub.add_parser('doctor');sub.add_parser('selftest');m=sub.add_parser('mass');m.add_argument('formula')
 for cmd in ['distance','noe']:
  a=sub.add_parser(cmd);a.add_argument('--input',required=True);a.add_argument('--output',required=True)
  if cmd=='noe':a.add_argument('--config',required=True)
 a=p.parse_args()
 if a.cmd=='doctor':out={'python':sys.version,'platform':platform.platform(),'modules':{k:bool(importlib.util.find_spec(k))for k in ['numpy','scipy','matplotlib','nmrglue','rdkit','datamol','matchms','pyopenms']},'external_models_licenses_and_services':'not tested'}
 elif a.cmd=='selftest':out=selftest()
 elif a.cmd=='mass':out=masses(a.formula)
 elif a.cmd=='distance':
  d=json.loads(Path(a.input).read_text(encoding='utf-8-sig'));out={'effective_distance_A':effective(d['weights'],d['distances'])}
 else:
  import numpy as np
  d=np.load(a.input,allow_pickle=False);cfg=json.loads(Path(a.config).read_text(encoding='utf-8-sig'));out=integrate(d['data'],d['x_ppm'],d['y_ppm'],cfg['signals'],cfg['pairs'])
 text=json.dumps(out,ensure_ascii=False,indent=2)
 if hasattr(a,'output'):
  target=Path(a.output)
  with target.open('x',encoding='utf-8')as f:f.write(text+'\n')
 else:print(text)
if __name__=='__main__':main()
