"""Compare new and old complete action bytes under independently derived budgets."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json,hashlib
P=Path(__file__).resolve().parent;W=P.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
tau=Q(5,2)**41/factorial(41)/(1-Q(5,84))
old=4096*(tau*2**18+Q(6240,2**128))
new=4096*(tau*4096+Q(6240,2**104))
cases=[]
for mode,n,roundcoords,inputname in [('forward',253952,504,'c30_x_boundary.txt'),('adjoint',2640,52,'c30_y.txt')]:
 suffix='Fxb' if mode=='forward' else 'Fty'
 a=W/f'c30_{suffix}.txt';b=W/f'c31_{suffix}.txt'
 va=list(map(int,a.read_text().split()));vb=list(map(int,b.read_text().split()));assert len(va)==len(vb)==n
 sq=sum((x-y)**2 for x,y in zip(va,vb));sqscaled=Q(sq,2**192)
 budget=old+new+Q(2*roundcoords,2**96)
 assert sqscaled<=budget*budget
 inp=W/inputname;iv=list(map(int,inp.read_text().split()));radius=2048 if mode=='forward' else 2049
 assert len(iv)==(2640 if mode=='forward' else 253952)
 assert sum(x*x for x in iv)<=(radius*2**96)**2
 runtime=W/f'c31_{mode}_runtime.json';res=json.loads(runtime.read_text())
 cases.append({'mode':mode,'coordinates':n,'different_coordinates':sum(x!=y for x,y in zip(va,vb)),'difference_numerator_squared':sq,'difference_grid_denominator':2**192,'joint_error_budget':[budget.numerator,budget.denominator],'difference_norm_le_joint_proved_bounds':True,'old_output_sha256':sha(a),'new_output_sha256':sha(b),'input_sha256':sha(inp),'runtime_receipt_sha256':sha(runtime),'observed_runtime':res})
(P/'COMPARISON_CHECKS.json').write_text(json.dumps({'status':'PASS','cases':cases,'scope':{'compares_supplied_existing_outputs_not_independent_full_action_rerun':True,'no_bit_equality_required_between_distinct_grids':True,'not_full8192_decoder_benchmark':True,'not_worst_case_runtime':True,'physical_promotion':0}},indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','cases':len(cases),'different':[c['different_coordinates'] for c in cases]}))
