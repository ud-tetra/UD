from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
P=Path(__file__).resolve().parent;W=P.parent
read=lambda p:list(map(int,p.read_text().split()))
x=read(W/'c30_x_boundary.txt');y=read(W/'c30_y.txt');fx=read(W/'c31_Fxb_final.txt');fty=read(W/'c31_Fty_final.txt')
assert len(x)==len(fty)==2640 and len(y)==len(fx)==253952
assert sum(v*v for v in x)<=(2048*2**96)**2 and sum(v*v for v in y)<=(2049*2**96)**2
b=json.loads((P/'BOUND_CHECKS.json').read_text());fw=Q(*b['exact']['forward_error']);ad=Q(*b['exact']['adjoint_error'])
res=abs(Q(sum(a*b for a,b in zip(fx,y))-sum(a*b for a,b in zip(x,fty)),2**192));budget=2049*fw+2048*ad
assert res<=budget
out={'status':'PASS','exact_duality_residual':[res.numerator,res.denominator],'conservative_budget':[budget.numerator,budget.denominator],'scope':'full supplied boundary state/data duality within absolute action budgets; no rounded-map linearity claim','physical_promotion':0}
(P/'DUALITY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS exact full-vector duality budget')
