#!/usr/bin/env python3
"""Regression fixtures for paired rank selection and discarded temporal-frame bounds."""
from pathlib import Path
from fractions import Fraction as F
import tempfile,json
import numpy as np
from flint import arb
from proof_math import verify
P=Path(__file__).resolve().parent;contract=json.loads((P/'inputs/FROZEN_CONTRACT.json').read_text());checks=[]
class StopAllocation(Exception):pass
# One station direction and two complex directions dominate small offset/noise directions.
C=np.zeros((3,2294),np.int64)
for k,v in enumerate([.3,1e-6,1e-6]):C[0,k*37+k]=round(v*2**60)
for k,v in enumerate([.4,.2,1e-6]):C[1,k*37+k]=round(2*v*2**60)
c=json.loads(json.dumps(contract));c['spectral_rule']['target_count']=5;observed={}
def inspect(stage,**kw):
 if stage=='global_rank_allocation':observed.update(kw);raise StopAllocation()
with tempfile.TemporaryDirectory() as t:
 try:verify(np.array([round(.3*2**60)],np.int64),C,arb(0),c,Path(t),inspect)
 except StopAllocation:pass
assert observed['allocation']==[1,2];checks.append('shared rank budget rejects tiny coherent offset directions')
# A discarded nonzero mode near a retained frequency must remain in the error-frame bound.
C=np.zeros((5,2294),np.int64);C[0,0]=round(.5*2**60);C[1,0]=round(.1*2**60);C[3,0]=round(.1*2**60);c=json.loads(json.dumps(contract));c['spectral_rule']['target_count']=1
with tempfile.TemporaryDirectory() as t:
 z=verify(np.array([round(.3*2**60),round(.30000001*2**60)],np.int64),C,arb(0),c,Path(t),lambda *a,**k:None)
 assert F(*z['frame_max_upper'])>F('1.9') and z['status']=='HOLD'
checks.append('discarded nonzero temporal modes enter the truncation error bound')
# Entirely nonstationary test, with a zero-dimensional stationary factor.
C=np.zeros((3,2294),np.int64);C[1,0]=round(.1*2**60);c=json.loads(json.dumps(contract));c['spectral_rule']['target_count']=2
with tempfile.TemporaryDirectory() as t:
 z=verify(np.array([round(.3*2**60)],np.int64),C,arb(0),c,Path(t),lambda *a,**k:None)
 assert z['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE' and z['target_count']==2
checks.append('zero stationary rank uses the paired real-factor transform correctly')
gap=json.loads((P/'DISCOVERY_GAP_CERTIFICATE.json').read_text());eta2=F(*gap['sketch_noise_squared_ceiling']);assert F(*gap['sigma105_baseline_lower'])**2>9*eta2 and F(*gap['sigma106_baseline_upper'])**2<eta2
checks.append('exact uniform temporal separation inequalities')
rows=json.loads((P/'RECORD_MANIFEST.json').read_text())['records'];assert all(r['per_vector_budget_met'] for r in rows if r['case']!='strong_rank_breach');assert not next(r for r in rows if r['case']=='strong_rank_breach')['per_vector_budget_met'];checks.append('all bounded recipes fit the exact vector budget; strong control does not')
new=json.loads((P/'NEW_PROPOSER_RESULTS.json').read_text());assert all(r['proposal_written'] and r['temporal_dimension']==105 for r in new if r['case']!='strong_rank_breach');assert next(r for r in new if r['case']=='strong_rank_breach')['status']=='HOLD';checks.append('all bounded proposals discovered; out-of-budget control held')
result={'status':'PASS','checks':checks,'physical_promotion':0,'independent_review':'pending'};(P/'TEST_RESULTS.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
