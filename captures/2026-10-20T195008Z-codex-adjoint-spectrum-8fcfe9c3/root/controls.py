"""Boundary/countermodel controls for the frozen exact adjoint proof implementation."""
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np

P=Path('/workspace/scratch/f3d1c2f040c9')
spec=importlib.util.spec_from_file_location('frozen_adjoint',P/'c18_adjoint/run.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rows=[]
def check(name,value):
    assert value,name
    rows.append({'id':name,'pass':True})
z=F(0);o=F(1)
for i,x in enumerate([z,o,F(4),F(2,9),F(3,7),F(1,1<<400)]):
    r=m.root_upper(x)
    check('dyadic_ceiling_'+str(i),r*r>=x and (r==0 or (r-F(1,1<<180))**2<x))
nums,b=m.encode(np.array([[0.,-0.125],[0.75,1.]],dtype=np.float64))
check('exact_signed_encoding',nums.tolist()==[[0,-1],[6,8]] and b==3)
for label,x in [('float32',np.array([1.],dtype=np.float32)),('nonfinite',np.array([np.nan]))]:
    try:m.encode(x)
    except AssertionError:rejected=True
    else:rejected=False
    check('reject_'+label,rejected)
t=m.consequences(z,z,z,z,F(3),F(2),z,z,F(2))
check('exact_diagonal_error_zero',t['retained_abs_error_upper']==0)
check('exact_diagonal_ambient_condition',t['ambient_leading_condition_upper']==F(3,2))
t=m.consequences(z,z,F(1,100),F(1,50),F(3),F(2),z,z,F(2))
check('offdiagonal_uses_max_not_sum',t['offdiagonal_upper']==F(1,50))
check('forward_compression_plus_cross',t['retained_abs_error_upper']==F(3,100))
# Exact adjoint-omission countermodel: Z=diag(5/3,1,0), U=[e1,e2],
# V=[(3/5,0,4/5),e2], S=I. Forward residual0, adjoint Frobenius4/3.
check('adjoint_countermodel_norm',F(16,15)**2+F(4,5)**2==F(4,3)**2)
check('adjoint_countermodel_fails_matching',m.consequences(z,z,z,F(4,3),o,o,z,z,o)['status'].startswith('HOLD'))
check('omitting_adjoint_would_miss_underestimate',m.consequences(z,z,z,z,o,o,z,z,o)['retained_abs_error_upper']==0 and F(5,3)-1>0)
# q=1,Z=diag(2,1),U=V=e2,S=1: exact equations, but source tail equals1.
check('strict_gap_equality_rejected',m.consequences(z,z,z,z,o,o,o,z,o)['status'].startswith('HOLD'))
check('tail_not_charged_retained_when_matched',m.consequences(z,z,z,z,F(3),F(2),F(1,10),F(1,20),F(2))['retained_abs_error_upper']==0)
check('mixed_list_keeps_tail_budget',m.consequences(z,z,z,z,F(3),F(2),F(1,10),F(1,20),F(2))['all321_abs_error_upper']==F(1,10))
for i,args in enumerate([(o,z,z,z,o,o,z,z,o),(z,o,z,z,o,o,z,z,o),
                         (z,z,-o,z,o,o,z,z,o),(z,z,z,-o,o,o,z,z,o),
                         (z,z,z,z,o,z,z,z,o),(z,z,z,z,o,F(2),z,z,o),
                         (z,z,z,z,o,o,-o,z,o),(z,z,z,z,o,o,z,-o,o)]):
    try:m.consequences(*args)
    except AssertionError:rejected=True
    else:rejected=False
    check('invalid_theorem_domain_'+str(i),rejected)
out=P/'c18_root';out.mkdir(exist_ok=True)
(out/'CONTROLS.json').write_text(json.dumps({'status':'PASS_EXACT_ROOT_BOUNDARY_AND_COUNTERMODEL_CONTROLS',
 'count':len(rows),'rows':rows,'control_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'producer_source_sha256':hashlib.sha256((P/'c18_adjoint/run.py').read_bytes()).hexdigest(),
 'countermodels_are_actual_backend_failures':False,'physical_promotion':0},indent=2)+'\n')
print(json.dumps({'root_controls':len(rows),'status':'PASS'}))
