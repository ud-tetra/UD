"""Selected exact retained residuals via direct matrix subtraction.

Selection: first parent record and first new protocol record, fixed before this
arithmetic. No parent code import, estimator invocation, raw or N file writes.
"""
import sys
sys.dont_write_bytecode=True
import hashlib,json,time,gc
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import fmpz_mat
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;P=ROOT/'cutoff-campaign-work'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def encode(x):
 assert x.dtype==np.float64 and np.all(np.isfinite(x))
 p=[float(v).as_integer_ratio() for v in x.flat];b=max(d.bit_length()-1 for n,d in p)
 n=np.array([v<<(b-(d.bit_length()-1)) for v,d in p],dtype=object).reshape(x.shape)
 return n,b

def sketch():
 left=np.random.Generator(np.random.PCG64(172026)).choice([-1.,1.],size=(2294,160)).astype(np.int64)
 right=np.random.Generator(np.random.PCG64(184052)).choice([-1.,1.],size=(2294,160)).astype(np.int64)
 v=np.pad(np.array(load(P/'inputs/NULL_VECTOR.json')['vector'],np.int64),(0,1974))
 assert v@v==16228 and np.all(v@left==0)
 return np.column_stack((2*left,v,2*right))

def projection(baseline,record,is_parent):
 assert sha(baseline)==load(P/'PROTOCOL_FREEZE.json')['baseline_sha256']
 Y=np.memmap(baseline,dtype='<i8',mode='r',shape=(37,8191,62));M=np.array(record['transform_integer_matrix'],np.int64);den=record['transform_denominator'];A=sketch();mx=max(abs(int(Y.min())),abs(int(Y.max())))
 assert M.shape==(37,37) and den in (1,5,25) and np.array_equal(M@M.T,np.eye(37,dtype=np.int64)*den*den)
 rowL1=int(np.abs(M).sum(axis=1).max());assert rowL1<=49 and rowL1*mx+25<2**63
 scalar_bound=(rowL1*mx)//den+2;assert scalar_bound*int(np.abs(A).sum(axis=0).max())<2**63
 if is_parent:
  rng=np.random.Generator(np.random.PCG64(record['recipe']['noise_seed']));channels=rng.integers(0,62,size=(37,8191));signs=2*rng.integers(0,2,size=(37,8191))-1
 else:
  assert record['recipe']['noise']=='stationary','predetermined first-new selection changed'
  channels=np.zeros((37,8191),np.int64);signs=np.ones_like(channels)
 N=np.zeros((8191,321),np.int64);raw_hash=hashlib.sha256();nom_hash=hashlib.sha256();t=np.arange(8191);maxraw=0
 for j in range(37):
  numerator=np.zeros((8191,62),np.int64)
  for k in np.flatnonzero(M[j]):numerator+=int(M[j,k])*np.array(Y[k],np.int64)
  if den==1:v=numerator
  else:
   quotient=numerator//den;rem=numerator-den*quotient;v=quotient+(rem>den//2);assert np.max(np.abs(den*v-numerator))<=den//2
  nom_hash.update(v.astype('<i8').tobytes());v[t,channels[j]]+=signs[j];raw_hash.update(v.astype('<i8').tobytes());maxraw=max(maxraw,max(abs(int(v.min())),abs(int(v.max()))))
  N+=v@A[np.arange(62)*37+j,:]
 assert raw_hash.hexdigest()==record['record_sha256'] and nom_hash.hexdigest()==record['nominal_sha256']
 nmax=max(abs(int(N.min())),abs(int(N.max())));assert nmax<2**53
 rec={'partial_sum_bound':maxraw*int(np.abs(A).sum(axis=0).max()),'numerator_max':nmax,'integer_bytes_sha256':hashlib.sha256(N.astype('<i8').tobytes()).hexdigest(),'projection_bytes_sha256':hashlib.sha256((N.astype(np.float64)/2.**55).astype('<f8').tobytes()).hexdigest()}
 assert sha(baseline)==load(P/'PROTOCOL_FREEZE.json')['baseline_sha256']
 return N,rec

def run():
 f=load(HERE/'DIRECT_RESIDUAL_FREEZE.json')
 for p,h in f['files'].items():assert sha(ROOT/p)==h,p
 protocol=load(P/'PROTOCOL_FREEZE.json');parent=ROOT/'ud-repo/captures'/protocol['parent_capture']['capture'];rows=[]
 new_record=load(P/'DATA_FREEZE.json')['records'][0]
 choices=[('parent',parent,load(parent/'DATA_FREEZE.json')['records'][0],load(parent/'RUN_EXECUTIONS.json')['rows'][0]),('new',P,new_record,load(P/'results'/new_record['case']/'RUN.json'))]
 for kind,folder,record,runrow in choices:
  started=time.monotonic();case=folder/'results'/record['case'];assert record['case']==runrow['case'] and record['record_sha256']==runrow['record_sha256']
  for n,h in runrow['numeric_witnesses'].items():assert sha(case/n)==h,n
  if runrow['execution_status']!='COMPLETED' or runrow['learned_order']!=209:
   rows.append({'kind':kind,'case':record['case'],'status':'HOLD_SELECTED_EXECUTION_OR_ORDER_RETAINED'});continue
  N,proj=projection(ROOT/f['baseline_relative'],record,kind=='parent');assert proj==runrow['projection']
  U=np.vstack([np.load(case/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)])
  with np.load(case/'SVD_META.npz',allow_pickle=False) as z:s=z['singular'][:209];vt=z['right_transpose'][:209]
  un,bu=encode(U);sn,bs=encode(s);vn,bv=encode(vt);cn=sn[:,None]*vn;bc=bs+bv;scale=max(55,bu+bc)
  # Direct full matrix residual, independent of parent expanded-Gram formula.
  R=fmpz_mat(N.astype(object).tolist())*(1<<(scale-55))-(fmpz_mat(un.tolist())*fmpz_mat(cn.tolist()))*(1<<(scale-bu-bc))
  squared=F(sum(int(R[i,j])**2 for i in range(8191) for j in range(321)),1<<(2*scale))
  row={'kind':kind,'case':record['case'],'record_sha256':record['record_sha256'],'status':'DIRECT_EXACT_RETAINED_RESIDUAL_COMPLETE','projection':proj,'direct_residual_squared':[str(squared.numerator),str(squared.denominator)],'scale_bits':scale,'elapsed_seconds':time.monotonic()-started}
  rows.append(row);print(json.dumps({'kind':kind,'case':record['case'],'status':row['status'],'elapsed_seconds':row['elapsed_seconds']}),flush=True)
  del R,N,U,un,sn,vn,cn;gc.collect()
 for p,h in f['files'].items():assert sha(ROOT/p)==h,p
 out=HERE/'DIRECT_RESIDUAL.json';assert not out.exists();out.write_text(json.dumps({'status':'SELECTED_DIRECT_RETAINED_RESIDUALS_COMPLETE','rows':rows,'all_hashes_before_after_equal':True,'freeze_sha256':sha(HERE/'DIRECT_RESIDUAL_FREEZE.json'),'completed_utc':datetime.now(timezone.utc).isoformat(),'scope':'Same-team independent expression. Baseline read-only, raw/N formed only in memory; no parent helper import, estimator/SVD call or parent mutation. Certificate fraction comparison is subsequent.','physical_promotion':0,'external_review':'PENDING'},indent=2))

if __name__=='__main__':run()
