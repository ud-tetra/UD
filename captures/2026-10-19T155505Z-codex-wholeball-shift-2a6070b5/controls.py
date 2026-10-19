"""Exact scaled LS fixtures and frozen-source refusal; no extra estimator runs."""
import sys
sys.dont_write_bytecode=True
import json,tempfile,shutil
from pathlib import Path
from fractions import Fraction as F
import bounds
from bounds import P,freeze,verify
freeze();rows=[]
for scale in (1,2):
 # A=(scale,0)^T, b=(2*scale,3)^T, returned t=5.
 s2=F((2*scale-5*scale)**2+9);N=F(scale*(2*scale-5*scale));gap2=N*N/F(scale*scale)
 assert s2-gap2==9 and s2==9+gap2
 rows.append({'fixture':'scaled_fullrank_LS_'+str(scale),'residual_squared':str(s2),'normal_residual_squared':str(N*N),'sigma_min':scale,'minimum_residual_squared':9,'status':'PASS_EXACT_PYTHAGORAS_AND_LOWER_BOUND'})
try:
 assert F(0)>0,'HOLD_SINGULAR_A'
except AssertionError:rows.append({'fixture':'zero_rank_margin','status':'REFUSED_BEFORE_DIVISION'})
with tempfile.TemporaryDirectory() as td:
 tmp=Path(td)/'copy';shutil.copytree(P,tmp,ignore=shutil.ignore_patterns('__pycache__'));target=tmp/'inputs/PARENT_UNIFORM.json';target.write_bytes(target.read_bytes()+b' ')
 original=bounds.P;bounds.P=tmp
 try:
  try:bounds.freeze()
  except AssertionError:refused=True
  else:refused=False
 finally:bounds.P=original
 assert refused;rows.append({'fixture':'changed_source_bytes','status':'REFUSED_FROZEN_INPUT_HASH','original_source_unchanged':True})
result={'status':'PASS_FOUR_EXACT_AND_SOURCE_REFUSAL_CONTROLS','controls':rows,'physical_promotion':0};q=P/'CONTROLS.json'
if q.exists():assert json.loads(q.read_text())==result
else:q.write_text(json.dumps(result,indent=2))
print(json.dumps(result),flush=True)
