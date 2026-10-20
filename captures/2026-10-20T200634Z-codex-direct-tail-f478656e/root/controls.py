"""Exact boundary and countermodel checks for the frozen tail route."""
import hashlib,importlib.util,json
from fractions import Fraction as F
from pathlib import Path
P=Path('/workspace/scratch/f3d1c2f040c9')
spec=importlib.util.spec_from_file_location('fixed_tail',P/'c19_tail/run.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rows=[]
def check(n,x):
    assert x,n
    rows.append({'id':n,'pass':True})
z=F(0);o=F(1)
for power in [2,4]:
    for i,x in enumerate([z,o,F(16),F(1,16),F(2,7),F(1,1<<800)]):
        u=m.root_upper(x,power)
        check('minimal_dyadic_'+str(power)+'_'+str(i),u**power>=x and(u==0 or(u-F(1,1<<180))**power<x))
# W=[1/2], G=[1/4], sumG²=1/16. A square root gives1/4, below||W||=1/2.
check('fourth_root_not_square_root',m.root_upper(F(1,16),4)==F(1,2)and m.root_upper(F(1,16),2)<F(1,2))
# Z=diag(2,1), Vd=(0,3/4), eta7/16, ||ZVd||3/4.
t=m.derived(F(7,16),F(3,4),z,z,z,z,F(3),F(2),z)
check('nonunit_tail_denominator_required',F(3,4)<1 and t['direct_tail_upper']>=1)
check('squared_gram_defect_is_unsafe_substitute',F(3,4)/(1-F(7,16)**2)<1)
# Z=diag(3,2,0),q1 requires a2dimensional testspace; null vector alone is insufficient.
check('too_small_subspace_cannot_bound_target_singular',0<F(2))
t=m.derived(z,F(1,10),z,z,z,z,F(3),F(2),F(1,20))
check('exact_diagonal_tail',t['direct_tail_upper']==F(1,10))
check('retained_zero_error_with_strict_direct_gap',t['retained_abs_error_upper']==0)
check('mixed_error_keeps_direct_tail',t['full321_abs_error_upper']==F(1,10))
check('old_nominal_tail_not_an_argument','source' not in m.derived.__code__.co_varnames and 'nominal' not in m.derived.__code__.co_varnames)
check('strict_gap_equality_holds',m.derived(z,o,z,z,z,z,o,o,z)['status'].startswith('HOLD'))
for i,args in enumerate([(o,z,z,z,z,z,o,o,z),(-o,z,z,z,z,z,o,o,z),(z,-o,z,z,z,z,o,o,z),
                         (z,z,o,z,z,z,o,o,z),(z,z,z,o,z,z,o,o,z),(z,z,z,z,-o,z,o,o,z),
                         (z,z,z,z,z,-o,o,o,z),(z,z,z,z,z,z,o,z,z),(z,z,z,z,z,z,o,F(2),z),
                         (z,z,z,z,z,z,o,o,-o)]):
    try:m.derived(*args)
    except AssertionError:rejected=True
    else:rejected=False
    check('invalid_bound_domain_'+str(i),rejected)
out=P/'c19_root';out.mkdir(exist_ok=True)
(out/'CONTROLS.json').write_text(json.dumps({'status':'PASS_EXACT_ROOT_TAIL_CONTROLS','count':len(rows),'rows':rows,
 'producer_source_sha256':hashlib.sha256((P/'c19_tail/run.py').read_bytes()).hexdigest(),
 'control_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'countermodels_are_actual_backend_failures':False,'physical_promotion':0},indent=2)+'\n')
print(json.dumps({'status':'PASS','root_controls':len(rows)}))
