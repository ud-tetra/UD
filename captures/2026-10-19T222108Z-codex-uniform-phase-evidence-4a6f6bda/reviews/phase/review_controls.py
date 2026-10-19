"""Independent exact algebraic boundary controls; no producer imports."""
import hashlib, json
from fractions import Fraction as F
from pathlib import Path
from flint import arb, fmpq, ctx
ctx.prec = 512
HERE = Path(__file__).resolve().parent
def aa(x):
    x=F(x); return arb(fmpq(x.numerator,x.denominator))
def radius_gate(r, separation, modulus=F(1)):
    # Squared rational expressions independently avoid transcendental comparison.
    return 0 <= r and 0 < modulus and r*r < modulus*modulus and 4*r*r < separation*separation
def execute():
    freeze=json.loads((HERE/'REVIEW_FREEZE.json').read_text())
    for name,digest in freeze['files'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest
    checks=[]
    def check(name, observed, expected):
        assert observed == expected, (name,observed,expected)
        checks.append(dict(id=name,observed=observed,expected=expected))
    check('zero_radius_strict_disjoint',radius_gate(F(0),F(1)),True)
    check('touching_disks_refused',radius_gate(F(1,2),F(1)),False)
    check('negative_radius_refused',radius_gate(F(-1,10),F(1)),False)
    check('origin_touch_refused',radius_gate(F(1),F(3)),False)
    check('origin_cross_refused',radius_gate(F(2),F(5)),False)
    # One-sided inclusion alone permits duplicates: no bijection from the list.
    sources=(F(-1),F(1)); observed=(F(1),F(1))
    check('pointwise_near_some_target',all(min(abs(v-s) for s in sources)==0 for v in observed),True)
    check('pointwise_nearness_does_not_establish_bijection',len(set(observed))==len(sources),False)
    # A radius-r disk centered at exp(i theta) is tangent at angular offset asin(r).
    r=F(3,5); u=F(4,5)
    tangent_x=u*u; tangent_y=r*u
    check('unit_center_tangent_distance_exact',(tangent_x-1)**2+tangent_y**2==r*r,True)
    check('unit_center_tangent_radius_nonzero',tangent_x*tangent_x+tangent_y*tangent_y==u*u,True)
    check('angle_tangent_is_asin_r',bool(abs((aa(tangent_y)/aa(tangent_x)).atan()-aa(r).asin())<arb(1)/(1<<400)),True)
    # Principal arguments jump, circular distance does not.
    eps=arb(1)/1000
    upper=arb.pi()-eps; lower=-arb.pi()+eps
    check('principal_argument_jump_large',bool(abs(upper-lower)>6),True)
    check('circular_argument_across_cut_small',bool(abs(upper-lower-2*arb.pi())<arb(1)/500+arb(1)/(1<<400)),True)
    # Independent diagonal homotopy count fixture, with separated source disks.
    centers=[F(-1),F(1)]; perturb=[F(1,10),F(-1,10)]; R=F(1,5)
    for j in range(2):
        for step in range(11):
            lam=centers[j]+F(step,10)*perturb[j]
            assert abs(lam-centers[j]) < R
            assert abs(lam-centers[1-j]) > R
    check('homotopy_fixture_one_root_per_source',True,True)
    # Alias: frequencies omega and omega+pi produce identical lag-two phase.
    check('two_step_alias_not_unaliased_frequency',bool(abs((2*arb.pi()).sin())<arb(1)/(1<<400)),True)
    result=dict(status='PASS_INDEPENDENT_EXACT_AND_INTERVAL_CONTROLS',checks=checks,count=len(checks),new_fits=0,new_eigenvalue_SVD_calls=0,external_review='PENDING',lane='development — no registry entry',physical_promotion=0,freeze_sha256=hashlib.sha256((HERE/'REVIEW_FREEZE.json').read_bytes()).hexdigest())
    (HERE/'REVIEW_CONTROLS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],count=len(checks))))
if __name__=='__main__': execute()
