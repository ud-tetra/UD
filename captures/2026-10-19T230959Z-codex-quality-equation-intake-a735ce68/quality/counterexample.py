"""Two prospectively fixed encoded records; exact dyadic compression tail lower bound.
No runtime estimator, SVD or physical-data call. Source archives are read as arrays only.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import sys
sys.dont_write_bytecode=True
import argparse,hashlib,json,zipfile,io
from pathlib import Path
from fractions import Fraction
import numpy as np
from flint import arb,arb_mat,fmpz_mat,fmpq,ctx
ctx.prec=512
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load_member(repo,row):
 p=repo/row['archive'];assert sha(p)==row['archive_sha256']
 with zipfile.ZipFile(p) as z:
  blob=z.read(row['member'])
 assert hashlib.sha256(blob).hexdigest()==row['sha256']
 return blob

def encode(a):
 vals=[float(x).as_integer_ratio() for x in a.flat];bits=max(d.bit_length()-1 for n,d in vals)
 return np.array([n*(1<<(bits-(d.bit_length()-1))) for n,d in vals],object).reshape(a.shape),bits

def fm(a):return fmpz_mat([[int(v) for v in row] for row in a])
def am(a,bits):return arb_mat([[arb(fmpq(int(v),1<<bits)) for v in row] for row in a])
def bound(x,upward=True):
 y=(arb(x.upper() if upward else x.lower())*(1<<200));z=y.ceil().unique_fmpz() if upward else y.floor().unique_fmpz();assert z is not None
 return [int(z),1<<200]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--baseline',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();repo=Path(a.repo).resolve();base=Path(a.baseline).resolve();out=Path(a.out).resolve();assert HERE not in out.parents and out!=HERE;out.mkdir(exist_ok=False)
 f=json.loads((HERE/'FREEZE.json').read_text());assert sha(HERE/'counterexample.py')==f['code_sha256'];assert sha(base)==f['baseline_sha256'];assert base.stat().st_size==37*8191*62*8
 for p,h in f['sources'].items():assert sha(repo/p)==h,(p,h)
 arrays={}
 for row in f['members']:
  blob=load_member(repo,row)
  with np.load(io.BytesIO(blob),allow_pickle=False) as z:arrays[row['label']]={k:z[k].copy() for k in z.files}
 U=np.vstack([arrays['ua']['basis'],arrays['ub']['basis']]);Ui,bu=encode(U);assert bu==77
 C0=arrays['coeff']['coefficient'];H=np.array([[int(x) for x in row] for row in arrays['gram']['cross_gram_decimal']],object)
 G=np.array([[int(x) for x in row] for row in arrays['gram']['basis_gram_decimal']],object);assert fm(Ui).transpose()*fm(Ui)==fm(G)
 v=np.pad(np.array(json.loads((repo/f['null_path']).read_text())['vector'],np.int64),(0,1974))
 old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64);A=np.column_stack((2*old,v,2*new));assert np.array_equal(A.T@A,arrays['gram']['sketch_gram'])
 u=np.where(np.arange(8191)%2==0,1,-1).astype(np.int64);Y=np.memmap(base,dtype='<i8',mode='r',shape=(37,8191,62));alt=np.zeros(2294,object)
 # Each sum has at most8191 int64 source values; Python integers prohibit overflow.
 for c in range(62):
  for prep in range(37):alt[37*c+prep]=sum(int(x)*int(s) for x,s in zip(Y[prep,:,c],u))
 altZ=(fm(alt.reshape(1,-1))*fm(A)).tolist()[0];cu=(fm(Ui).transpose()*fm(u.reshape(-1,1))).tolist();cu=np.array([int(r[0]) for r in cu],object)
 Lgram=np.empty((210,210),object);Lgram[:209,:209]=G;Lgram[:209,209]=cu*(1<<70);Lgram[209,:209]=Lgram[:209,209];Lgram[209,209]=8191*(1<<140)
 Lbound=arb(max(sum(abs(int(x)) for x in row) for row in Lgram)/(1<<154)).sqrt()
 # Float division above is NOT used as certificate: overwrite with exact rational.
 Lbound=arb(fmpq(max(sum(abs(int(x)) for x in row) for row in Lgram),1<<154)).sqrt()
 results=[]
 for count in [1,2]:
  w=np.zeros(2294,np.int64);chosen=[]
  for prep in range(37):
   cs=sorted(range(62),key=lambda c:(-abs(int(v[37*c+prep])),c))[:count]
   for c in cs:w[37*c+prep]=1 if int(v[37*c+prep])>=0 else -1
   chosen.append(cs)
  assert all(sum(int(w[37*c+p])**2 for c in range(62))==count for p in range(37));assert 4*count<=9
  bi=np.array([int(x) for x in (fm(w.reshape(1,-1))*fm(A)).tolist()[0]],object);b=np.array([float(int(x))/128 for x in bi])
  # QR proposes only dyadic test columns; no spectral result is assumed from it.
  R,_=np.linalg.qr(np.column_stack((C0.T,b)),mode='reduced');Ri,br=encode(R)
  RG=(fm(Ri).transpose()*fm(Ri)).tolist();Rbound=arb(fmpq(max(sum(abs(int(x)) for x in row) for row in RG),1<<(2*br))).sqrt()
  top=H+cu[:,None]*bi[None,:];bottom=np.array([(int(x)+8191*int(y))*(1<<70) for x,y in zip(altZ,bi)],object)[None,:];Dint=(fm(np.vstack((top,bottom)))*fm(Ri)).tolist();D=am(Dint,132+br)
  inv=D.inv();ifro=arb(0)
  for i in range(210):
   for j in range(210):ifro+=inv[i,j]*inv[i,j]
  lower=1/ifro.sqrt()/Lbound/Rbound
  # Verify inverse both ways as Arb512 with interval containment.
  prod=D*inv;assert all((prod[i,j]-int(i==j)).contains(0) for i in range(210) for j in range(210))
  rawhash=hashlib.sha256();normmax=0;diffcount=0
  for prep in range(37):
   W=w.reshape(62,37)[:,prep];row=np.array(Y[prep],dtype='<i8',copy=True);change=u[:,None]*W[None,:];row+=change
   assert np.all((row.astype(object)-np.array(Y[prep],object))==change.astype(object));rawhash.update(row.tobytes());normmax=max(normmax,int(np.max(np.sum(change*change,axis=1))));diffcount+=int(np.count_nonzero(change))
  row={'id':f'null_top{count}_alternating','selected_channels_by_preparation':chosen,'w_int64le_sha256':hashlib.sha256(w.astype('<i8').tobytes()).hexdigest(),'raw_int64le_sha256':rawhash.hexdigest(),'baseline_sha256':f['baseline_sha256'],'local_vector_integer_squared_norm_max':normmax,'local_vector_count':37*8191,'changed_scalars':diffcount,'q_raw':[1,1<<48],'membership_delta':[3,1<<49],'sigma210_lower':bound(lower,False),'readable_sigma210_lower':float(lower.lower()),'epsilon_cap':[1,1<<41],'strictly_above_cap':bool(lower>arb(fmpq(1,1<<41))),'left_test_frame_norm_upper':bound(Lbound),'right_test_frame_norm_upper':bound(Rbound),'compression_inverse_F_norm_upper':bound(ifro.sqrt()),'compression_bits':132+br,'test_right_scale_bits':br,'new_estimator_calls':0,'status':'CERTIFIED_NO_RANK209_APPROXIMATION_AT_CAP' if lower>arb(fmpq(1,1<<41)) else 'HOLD_BOUND_NOT_SUFFICIENT'}
  np.savez_compressed(out/f'TEST_FRAME_{count}.npz',right=R,w=w,compression_decimal=np.array([[str(x) for x in rr] for rr in Dint]),left_gram_decimal=np.array([[str(x) for x in rr] for rr in Lgram]),right_gram_decimal=np.array([[str(x) for x in rr] for rr in RG]))
  results.append(row);print(json.dumps(row),flush=True)
 cert={'status':'COMPLETE_TWO_FROZEN_RECIPES','freeze_sha256':sha(HERE/'FREEZE.json'),'rows':results,'arithmetic':'Python integers / FLINT fmpz exact dyadic compression; Arb512 inverse/Frobenius lower bound','source_cross_Gram_scope':'Pinned prior exact cross-Gram inherited, not newly recomputed here','physical_promotion':0,'external_review':'PENDING','claim_scope':'Necessary retained-rank209-quality feasibility only; no phase-failure, six-ratio or physical claim','new_estimator_calls':0}
 (out/'CERTIFICATE.json').write_text(json.dumps(cert,indent=2)+'\n')
if __name__=='__main__':main()
