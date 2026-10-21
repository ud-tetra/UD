from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
p=argparse.ArgumentParser();p.add_argument('--workspace',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();P=a.workspace;a.out.mkdir(parents=True,exist_ok=False);H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rd=lambda n:list(map(int,(P/n).read_text().split()));new=json.loads((P/'c31_math/NATIVE_CONSTANTS.json').read_text());old=json.loads((P/'c30_math/ACTION_CONSTANTS.json').read_text());S=2**96;x=rd('c30_x_boundary.txt');y=rd('c30_y.txt');f=rd('c31_Fxb_final.txt');t=rd('c31_Fty_final.txt');assert len(x)==len(t)==2640 and len(y)==len(f)==253952;assert sum(v*v for v in x)<(2048*S)**2 and sum(v*v for v in y)<(2049*S)**2
rows=[]
for mode,ni,oi,key in [('forward','c31_Fxb_final.txt','c30_Fxb.txt','forward_error_upper'),('adjoint','c31_Fty_final.txt','c30_Fty.txt','adjoint_error_upper')]:
 v=rd(ni);w=rd(oi);d2=F(sum((r-s)**2 for r,s in zip(v,w)),S*S);budget=F(new[key])+F(old[key]);assert d2<budget**2
 rows.append({'mode':mode,'status':'PASS_COMBINED_PROVED_ERROR_ENVELOPE','dimension':len(v),'difference_norm_squared':str(d2),'absolute_difference_bound':str(budget),'native_output_sha256':H(P/ni),'GMP_reference_output_sha256':H(P/oi),'changed_coordinates':sum(r!=s for r,s in zip(v,w)),'bit_equality_required':False})
dual=F(sum(v*w for v,w in zip(f,y))-sum(v*w for v,w in zip(x,t)),S*S);dualcap=F(new['forward_error_upper'])*2049+F(new['adjoint_error_upper'])*2048;assert abs(dual)<dualcap
# Exact native output replays; the root historical pair spans a parser-only source fix.
assert(P/'c31_Fxb.txt').read_bytes()==(P/'c31_Fxb_final.txt').read_bytes();assert(P/'c31_Fty.txt').read_bytes()==(P/'c31_Fty_final.txt').read_bytes()
j={'status':'PASS_ACTUAL_NATIVE_ACTION_REFERENCE_CONFORMANCE','comparisons':rows,'duality_residual':str(dual),'duality_absolute_bound':str(dualcap),'native_replay_bytes_identical':True,'source_sha256':H(P/'c31_action.cpp'),'build_receipt_sha256':H(P/'c31_BUILD_RECEIPT.json'),'operator_sha256':H(P/'c31_math/OPERATOR.txt'),'physical_promotion':0,'external_promotion_review':'PENDING','full8192_run':False};(a.out/'CONFORMANCE.json').write_text(json.dumps(j,indent=2,sort_keys=True)+'\n');print('PASS two full native/reference comparisons, duality and native replays')
