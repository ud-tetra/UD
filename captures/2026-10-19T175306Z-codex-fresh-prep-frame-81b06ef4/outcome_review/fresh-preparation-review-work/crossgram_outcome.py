"""Exact expanded cross-Gram check of fresh retained frames; no estimator.

This review script is frozen before its arithmetic execution. Data and fitted
outputs already exist; no blinded or preregistered outcome claim is made.
"""
import sys
sys.dont_write_bytecode=True
import json,hashlib,time
from datetime import datetime,timezone
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import fmpz_mat

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
P=ROOT/'prospective-frame-work'
E=ROOT/'prospective-frame-source'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def encode(x):
 assert x.dtype==np.float64 and np.all(np.isfinite(x))
 pairs=[float(v).as_integer_ratio() for v in x.flat]
 bits=max(d.bit_length()-1 for n,d in pairs)
 z=np.array([n<<(bits-(d.bit_length()-1)) for n,d in pairs],dtype=object).reshape(x.shape)
 return fmpz_mat(z.tolist()),bits

def trace(M):return sum(int(M[i,i]) for i in range(M.nrows()))

def run():
 frozen=load(HERE/'OUTCOME_CHECK_FREEZE.json')
 for p,h in frozen['files'].items():assert sha(ROOT/p)==h,p
 protocol=load(P/'PROTOCOL_FREEZE.json');inputs=load(P/'INPUT_INDEX.json')['members'];af=load(P/'ALIGNMENT_FREEZE.json');runs=load(P/'RUN_EXECUTIONS.json')['rows'];data=load(P/'DATA_FREEZE.json')
 assert protocol['fixed_budget']==load(P/'inputs/FIXED_BUDGET.json')['source_budget']
 assert sha(P/'inputs/FIXED_BUDGET.json')==sha(ROOT/'floating-budget-work/BUDGET_CERTIFICATE.json')
 assert sha(P/'RUN_EXECUTIONS.json')==af['run_executions_sha256'] and sha(P/'DATA_FREEZE.json')==af['data_freeze_sha256']
 assert data['protocol_sha256']==sha(P/'PROTOCOL_FREEZE.json')
 for p,h in protocol['files'].items():assert sha(P/p)==h,p
 for p,h in af['files'].items():assert sha(P/p)==h,p
 for entry in inputs:assert sha(E/entry['destination'])==entry['sha256'],entry['destination']
 U0=np.vstack([np.load(E/('U0_'+n+'.npz'),allow_pickle=False)['basis'] for n in ['A','B']]);U0n,b0=encode(U0);G0=U0n.transpose()*U0n
 rows=[]
 for recipe,record,receipt in zip(protocol['cases'],data['records'],runs):
  start=time.monotonic();case=recipe['case'];folder=P/'results'/case
  assert receipt==load(folder/'RUN.json') and case==record['case']==receipt['case'] and record['recipe']==recipe
  assert record['record_sha256']==receipt['record_sha256']
  for p,h in receipt['numeric_witnesses'].items():assert sha(folder/p)==h,p
  row={'case':case,'record_sha256':record['record_sha256'],'learned_order':receipt['learned_order'],'execution_status':receipt['execution_status']}
  if receipt['execution_status']!='COMPLETED' or receipt['learned_order']!=209:
   row['status']='HOLD_SCOPE_OR_EXECUTION_RETAINED';rows.append(row);continue
  U1=np.vstack([np.load(folder/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)])
  X=np.load(P/'alignments'/f'{case}.npz',allow_pickle=False)['alignment']
  assert U1.shape==U0.shape==(8191,209) and X.shape==(209,209)
  U1n,b1=encode(U1);Xn,bx=encode(X);G1=U1n.transpose()*U1n;H01=U0n.transpose()*U1n
  cross=sum(int(Xn[i,j])*int(H01[i,j]) for i in range(209) for j in range(209))
  r2=F(trace(G1),1<<(2*b1))+F(trace(Xn.transpose()*G0*Xn),1<<(2*b0+2*bx))-2*F(cross,1<<(b0+b1+bx))
  eta2=F(sum((int(G1[i,j])-int(i==j)*(1<<(2*b1)))**2 for i in range(209) for j in range(209)),1<<(4*b1))
  assert r2>=0 and eta2>=0
  row.update(status='EXACT_CROSSGRAM_MEASUREMENT_COMPLETE',alignment_residual_squared=[str(r2.numerator),str(r2.denominator)],retained_Gram_defect_squared=[str(eta2.numerator),str(eta2.denominator)],scale_bits={'U0':b0,'U1':b1,'X':bx},elapsed_seconds=time.monotonic()-start)
  rows.append(row);print(json.dumps({'case':case,'status':row['status'],'elapsed_seconds':row['elapsed_seconds']}),flush=True)
 for p,h in frozen['files'].items():assert sha(ROOT/p)==h,p
 result={'status':'THREE_FROZEN_FRESH_FRAME_CROSSGRAM_MEASUREMENTS_COMPLETE','rows':rows,'protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'source_policy_sha256':sha(P/'inputs/FIXED_BUDGET.json'),'review_freeze_sha256':sha(HERE/'OUTCOME_CHECK_FREEZE.json'),'all_frozen_hashes_before_after_equal':True,'completed_utc':datetime.now(timezone.utc).isoformat(),'scope':'Same-team exact expanded cross-Gram expression. No parent helper imported, raw regeneration/projection/estimator/SVD run or parent mutation. No original-baseline-ball/all8gate/phase/external/uniform solver claim.','physical_promotion':0,'external_review':'PENDING'}
 out=HERE/'CROSSGRAM_OUTCOME.json';assert not out.exists();out.write_text(json.dumps(result,indent=2))

if __name__=='__main__':run()
