"""Replay phase-frame arithmetic and conditional bounds; raw residual remains a pinned receipt."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import numpy as np
from flint import ctx,arb,acb,fmpq
from proof_math import fm,arr,up,down
from phase_math import bound
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def replay():
 freeze=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());cert=json.loads((P/'PHASE_STABILITY_CERTIFICATE.json').read_text());c=cert['constants']
 for n,h in freeze['code_sha256'].items():assert sha(P/n)==h,(n,'frozen source changed')
 for n,h in freeze['inputs_sha256'].items():assert sha(P/'inputs'/n)==h
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:theta=z['theta'];coeff=z['coeff']
 baseline=json.loads((P/'inputs/BASELINE_SKETCH_CERTIFICATE.json').read_text())
 assert baseline['record_sha256']==cert['reference_record_sha256']==freeze['reference_record_sha256']
 assert cert['reference_proposal_sha256']==sha(P/'inputs/REFERENCE_PROPOSAL.npz')
 assert c['baseline_sigma105_lower']==baseline['retained_sigma_lower']
 freq=[arb(0)]+[s*arb(int(t))/(1<<60) for t in theta for s in [1,-1]];rows=[];sep=[]
 for i,u in enumerate(freq):
  row=arb(0)
  for j,v in enumerate(freq):
   if i==j:continue
   d=v-u;den=acb(0,d).exp()-1;assert abs(den)>0
   row+=abs((acb(0,8191*d).exp()-1)/(8191*den))
   if j>i:sep.append(down(abs(den))[0])
  rows.append(up(row)[0])
 assert c['frame_Gram_lower']==[(1<<100)-max(rows),1<<100]
 assert c['frame_Gram_upper']==[(1<<100)+max(rows),1<<100]
 assert c['minimum_chord_separation_lower']==[min(sep),1<<100]
 W=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974));A=np.column_stack((2*W,v));C=arr(fm(coeff)*fm(A))
 cmax=sum(max(abs(int(x)) for x in row) for row in C[1:]);phase=arb(8191*161).sqrt()*arb(cmax)/(1<<127)
 assert up(phase)==c['phase_rounding_sketch_residual_upper']
 sq=F(*c['exact_squared_dyadic_phase_residual']);efit=arb(sq.numerator).sqrt()/arb(sq.denominator).sqrt()+phase
 assert up(efit)==c['reference_model_sketch_residual_upper']
 grid=[bound(F(1,2**k),c) for k in freeze['phase_bound_dyadic_exponents']]+[bound(F(0),c)]
 assert grid==cert['dyadic_grid']
 best=max((r for r in grid if r['unique_phase_matching'] and F(*r['delta'])>0),key=lambda r:F(*r['delta']))
 assert best==cert['largest_certified_radius_on_frozen_grid'] and F(*best['delta'])==F(1,2**27)
 assert not cert['full_2neg20_uniqueness_proof'] and not cert['floating_proposer_accuracy_certified']
 return {'status':'PASS','reference_frame_pairs_checked':5460,'dyadic_radii_checked':21,'zero_noise_radius_checked':True,'reference_raw_sketch_residual_recomputed':False,'raw_residual_scope':'Exact all-readings certificate from certify_phase.py; portable replay checks its arithmetic/bindings, not the omitted raw record product','independent_review':'pending; same-constructor replay only','physical_promotion':0}
if __name__=='__main__':
 r=replay();(P/'PHASE_REPLAY_RESULTS.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
