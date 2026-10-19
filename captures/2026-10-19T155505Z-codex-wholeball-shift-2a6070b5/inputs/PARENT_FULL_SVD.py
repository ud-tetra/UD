"""Exact dyadic full-factor SVD admission. No assumed LAPACK error constant."""
import json,hashlib
from pathlib import Path
from fractions import Fraction
import numpy as np
from flint import fmpz_mat,arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def encode(a):
 a=np.asarray(a);assert a.dtype==np.float64 and np.all(np.isfinite(a))
 pairs=[float(v).as_integer_ratio() for v in a.flat];b=max(d.bit_length()-1 for n,d in pairs)
 return np.array([n<<(b-d.bit_length()+1) for n,d in pairs],object).reshape(a.shape),b
def fm(a):return fmpz_mat(np.asarray(a).tolist())
def ar(a):return np.array(a.tolist(),object)
def up(x):
 v=(x*(1<<180)).ceil().unique_fmpz();assert v is not None
 return [int(v),1<<180]
def val(pair):return arb(fmpq(*pair))
def nn(a,b):return arb(sum(int(x)**2 for x in a.flat)).sqrt()/(1<<b)
def certify(mode,write=False):
 d=P/'results'/mode;N=[];U=[];Z=[]
 for k in range(3):
  with np.load(P/'results'/f'INTEGER_{k}.npz') as a:n=a['numerator']
  with np.load(d/f'FACTOR_{k}.npz',allow_pickle=False) as a:
   u=a['left'];delta=a['delta'];b=int(a['projection_bits']);assert b>=55
   znum=n.astype(object)*(1<<(b-55))+delta.astype(object)
   z=np.array([float(Fraction(int(x),1<<b)) for x in znum.flat],np.float64).reshape(n.shape)
   assert hashlib.sha256(z.astype('<f8').tobytes()).hexdigest()==str(a['projection_sha256'])
   zn,bz=encode(z);assert np.array_equal(zn*(1<<(max(b,bz)-bz)),znum*(1<<(max(b,bz)-b)))
  N.append(n);U.append(u);Z.append(z)
 N=np.vstack(N);U=np.vstack(U);Z=np.vstack(Z);un,bu=encode(U);zn,bz=encode(Z)
 with np.load(d/'SVD_META.npz') as a:s=a['singular'];vt=a['right_transpose']
 assert s.shape==(321,) and U.shape==(8191,321) and vt.shape==(321,321)
 assert np.all(s>=0) and np.all(s[:-1]>=s[1:])
 sn,bs=encode(s);vn,bv=encode(vt);cn=sn[:,None]*vn;bc=bs+bv
 uf=fm(un);zf=fm(zn);vf=fm(vn);cf=fm(cn)
 print(mode,'exact left Gram',flush=True);G=uf.transpose()*uf
 print(mode,'exact cross Gram',flush=True);H=uf.transpose()*zf
 etaU=nn(ar(G)-np.eye(321,dtype=object)*(1<<(2*bu)),2*bu)
 etaV=nn(ar(vf*vf.transpose())-np.eye(321,dtype=object)*(1<<(2*bv)),2*bv)
 assert etaU<1 and etaV<1
 L=max(2*bz,2*bu+2*bc,bu+bz+bc)
 normz=sum(int(x)**2 for x in zn.flat)
 gc=ar(G*cf);h=ar(H)
 quadratic=sum(int(a)*int(b) for a,b in zip(cn.flat,gc.flat))
 cross=sum(int(a)*int(b) for a,b in zip(cn.flat,h.flat))
 residual_num=(normz<<(L-2*bz))+(quadratic<<(L-2*bu-2*bc))-2*(cross<<(L-bu-bz-bc))
 assert residual_num>=0,'HOLD negative exact residual numerator'
 residual=arb(residual_num).sqrt()/arb(2)**(arb(L)/2)
 p=lambda e:e/(1+(1-e).sqrt())
 svderr=residual+arb(float(s[0]))*(p(etaU)*(1+etaV).sqrt()+p(etaV))
 common=max(55,bz);diff=zn*(1<<(common-bz))-N.astype(object)*(1<<(common-55));projection=nn(diff,common)
 total=projection+svderr;cut=arb(1)/(1<<24);q=int(np.count_nonzero(s>2.**-24))
 admit=all((arb(float(v))-total>cut) if j<q else (arb(float(v))+total<cut) for j,v in enumerate(s))
 result={'status':'CERTIFIED_ACTUAL_SVD_ORDER' if admit else 'HOLD_CUTOFF_ENCLOSURE','mode':mode,'learned_order':q,'cutoff':[1,1<<24],'eta_left_upper':up(etaU),'eta_right_upper':up(etaV),'reconstruction_residual_upper':up(residual),'projection_error_upper':up(projection),'singular_error_upper':up(total),'sigma_q_lower':[-int((-(arb(float(s[q-1]))-total)*(1<<180)).ceil().unique_fmpz()),1<<180],'sigma_qplus1_upper':up(arb(float(s[q]))+total),'exact_residual_squared':[str(residual_num),str(1<<L)],'readable':{'projection_error_upper':float(projection.upper()),'svd_error_upper':float(svderr.upper()),'singular_error_upper':float(total.upper()),'sigma_q':float(s[q-1]),'sigma_qplus1':float(s[q])},'physical_promotion':0,'external_independent_review':'PENDING','uniform_SVD_or_phase_guarantee':False}
 if write:(d/'CERTIFICATE.json').write_text(json.dumps(result,indent=2))
 else:assert json.loads((d/'CERTIFICATE.json').read_text())==result
 print(json.dumps({k:result[k] for k in ['mode','status','learned_order','readable']}),flush=True)
 return result
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
 for mode in ['legacy_gemm','integer_projection']:certify(mode,a.write)
