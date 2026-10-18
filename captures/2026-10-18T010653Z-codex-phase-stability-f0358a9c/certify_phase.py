"""All-readings exact reference fit plus finite-window phase constants."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from pathlib import Path
from fractions import Fraction as F
import time,json,hashlib,resource
import numpy as np
from flint import ctx,arb,acb,fmpq
from proof_math import fm,arr,dyad,up,down
from phase_math import bound
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run():
 start=time.monotonic();freeze=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());raw=P/freeze['reference_record_path'];before=sha(raw)
 assert before==freeze['reference_record_sha256']
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:theta=z['theta'];coeff=z['coeff']
 assert theta.shape==(52,) and coeff.shape==(105,2294)
 Y=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62));X=np.array(Y.transpose(1,2,0).reshape(8191,2294),dtype=np.int64)
 W=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
 v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],dtype=np.int64),(0,1974));A=np.column_stack((2*W,v))
 assert max(abs(int(X.min())),abs(int(X.max())))*max(sum(abs(int(x)) for x in A[:,j]) for j in range(161))<2**63
 Z=X@A;del X
 C=arr(fm(coeff)*fm(A));pp=np.zeros((8191,105),np.int64);pp[:,0]=1<<60;gate=arb(1)/(1<<60)
 for j,t in enumerate(theta):
  for k in range(8191):
   z=acb(0,arb(int(t))*k/(1<<60)).exp();x,y=dyad(z.real),dyad(z.imag)
   assert abs(z.real-arb(x)/(1<<60))<gate and abs(z.imag-arb(y)/(1<<60))<gate
   pp[k,2*j+1]=x;pp[k,2*j+2]=y
 weighted=0
 for k in range(0,8191,128):
  model=arr(fm(pp[k:k+128])*fm(C));diff=model-Z[k:k+len(model)].astype(object)*(1<<72)
  weighted+=sum(int(x)**2 for x in diff.flat)
 sq=F(weighted,1<<254);fit=arb(sq.numerator).sqrt()/arb(sq.denominator).sqrt()
 cmax=sum(max(abs(int(x)) for x in row) for row in C[1:]);phase=arb(8191*161).sqrt()*arb(cmax)/(1<<127);e0=fit+phase
 freq=[arb(0)]+[sign*arb(int(t))/(1<<60) for t in theta for sign in [1,-1]]
 rows=[];seps=[]
 for i,u in enumerate(freq):
  row=arb(0)
  for j,w in enumerate(freq):
   if i==j:continue
   d=w-u;den=acb(0,d).exp()-1;assert abs(den)>0
   row+=abs((acb(0,8191*d).exp()-1)/(8191*den))
   if j>i:seps.append(down(abs(den)))
  rows.append(up(row))
 maximum=max(x[0] for x in rows);den=1<<100;minimum=min(x[0] for x in seps)
 baseline=json.loads((P/'inputs/BASELINE_SKETCH_CERTIFICATE.json').read_text())
 constants={'time_rows':8191,'temporal_order':105,'reference_model_sketch_residual_upper':up(e0),'exact_squared_dyadic_phase_residual':[sq.numerator,sq.denominator],'phase_rounding_sketch_residual_upper':up(phase),'frame_Gram_lower':[den-maximum,den],'frame_Gram_upper':[den+maximum,den],'minimum_chord_separation_lower':[minimum,den],'baseline_sigma105_lower':baseline['retained_sigma_lower'],'noise_transfer_squared':[37*8191*371097,4096]}
 assert constants['frame_Gram_lower'][0]>0 and minimum>0
 results=[bound(F(1,2**k),constants) for k in freeze['phase_bound_dyadic_exponents']];results.append(bound(F(0),constants))
 passed=[r for r in results if r['unique_phase_matching'] and F(*r['delta'])>0];assert passed
 chosen=max(passed,key=lambda r:F(*r['delta']))
 assert sha(raw)==before
 result={'status':'CONDITIONAL_FINITE_WINDOW_PHASE_STABILITY','physical_promotion':0,'independent_review':'pending','reference_record_sha256':before,'reference_proposal_sha256':sha(P/'inputs/REFERENCE_PROPOSAL.npz'),'source_nominal_modes_loaded':False,'scalar_readings_used':18790154,'reference_phases_are_fitted_not_physical_truth':True,'constants':constants,'dyadic_grid':results,'largest_certified_radius_on_frozen_grid':chosen,'full_2neg20_uniqueness_proof':results[0]['unique_phase_matching'],'floating_proposer_accuracy_certified':False,'wall_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
 (P/'PHASE_STABILITY_CERTIFICATE.json').write_text(json.dumps(result,indent=2));print(json.dumps({'best':chosen,'full_ball':results[0],'e0':float(e0.upper())},indent=2))
if __name__=='__main__':run()
