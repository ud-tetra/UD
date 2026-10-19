"""Exact/refusal controls for mistakes specific to the weighted certificate."""
import argparse,json,itertools,tempfile,shutil
from pathlib import Path
from fractions import Fraction as F
from flint import arb
from common import P,check_evidence
def verify(evidence):
 # A right inverse outside row(C) can falsely erase a weighted forcing.
 C=(F(1),F(0));J=(F(1),F(1));K=(F(1),F(0));forcing=(F(1),F(-1))
 dot=lambda x,y:sum(a*b for a,b in zip(x,y))
 assert dot(C,J)==dot(C,K)==1 and dot(forcing,J)==0 and dot(forcing,K)==1
 rows=[[(2,1),(0,3)],[(1,2),(-2,0)]];choices=[]
 for block in rows:choices.append([(0,0)]+[(s*x,s*y) for x,y in block for s in [-1,1]])
 bound=sum(arb(max(x*x+y*y for x,y in block)).sqrt() for block in rows)
 for u,v in itertools.product(*choices):assert (u[0]+v[0])**2+(u[1]+v[1])**2<=bound*bound
 # Same row-max rule fails on a REAL Euclidean ball: (3/5,4/5) has norm1 but maps to7/5.
 assert F(3,5)**2+F(4,5)**2==1 and F(3,5)+F(4,5)>1
 H11,H12,H22,R,W=F(4),F(1,2),F(1,16),F(4),F(1,8)
 mapped=H12/R+H22*W/R-W*(H11-R)/R-W*H12*W/R
 assert mapped==W and H11+H12*W==F(65,16) and H12+H22*W==F(65,16)*W
 with tempfile.TemporaryDirectory() as td:
  for row in json.loads((P/'INPUT_INDEX.json').read_text())['members']:shutil.copy2(Path(evidence)/row['destination'],Path(td)/row['destination'])
  check_evidence(td);q=Path(td)/'C.npz';data=q.read_bytes();q.write_bytes(bytes([data[0]^1])+data[1:])
  try:check_evidence(td)
  except AssertionError:pass
  else:raise AssertionError('altered coefficient accepted')
 return {'status':'PASS_FIVE_WEIGHTED_SCOPE_AND_REFUSAL_CONTROLS','checks':['arbitrary_right_inverse_counterexample','finite_encoded_rowmax_exhaustion','real_ball_rowmax_counterexample','exact_Riccati_invariant_graph_fixture','altered_coefficient_hash_refused'],'physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',required=True);args=p.parse_args();print(json.dumps(verify(args.evidence)),flush=True)
