"""Exact rational consequences of inherited retained-factor norm certificates.

No estimator, raw reconstruction, or large factor arithmetic occurs here.
The source norm statements remain inherited premises, not authenticated by hashes.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

SOURCE = 'captures/2026-10-20T183427Z-codex-maximal-noise-e5831029'
BACKEND = 'captures/2026-10-20T190406Z-codex-backend-contract-a14abe64'
CASES = ('boundary_pair_block', 'boundary_pair_rotating')


def pair(x):
    return [str(x.numerator), str(x.denominator)]


def rat(p):
    return F(int(p[0]), int(p[1]))


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def bounds(a, b, r, small, large):
    if not (0 <= a < 1 and 0 <= b < 1 and r >= 0 and 0 < small <= large):
        raise ValueError('invalid partial-factor bound domain')
    numerator = (1-a)*small-r
    if numerator <= 0:
        return {'status': 'HOLD_NO_POSITIVE_LOWER_BOUND'}
    lower = numerator/(1+b)
    upper = ((1+a)*large+r)/(1-b)
    debit = (small*(a+b)+r)/(1+b)
    assert small-lower == debit
    return dict(status='POSITIVE_PARTIAL_FACTOR_LOWER_BOUND', lower=lower,
                upper=upper, debit=debit, condition=upper/lower,
                inverse_restriction_upper=1/lower)


def controls():
    rows = []
    def check(name, condition):
        assert condition, name
        rows.append({'id': name, 'pass': True})
    z=F(0); o=F(1)
    b=bounds(z,z,z,F(2),F(3))
    check('orthonormal_exact_diagonal', b['lower']==2 and b['upper']==3 and b['condition']==F(3,2))
    check('retained_equation_debits_floor', bounds(z,z,F(1,10),o,o)['lower']==F(9,10))
    # Scalar U=6/5,V=5/4,S=1,Z=24/25, E=0. Gram defects <1.
    a=F(11,25); v=F(9,16)
    t=bounds(a,v,z,o,o)
    check('nonunit_frames_safe_lower', t['lower'] <= F(24,25))
    check('nonunit_frames_safe_upper', t['upper'] >= F(24,25))
    check('debit_identity_nonunit', t['debit']==o-t['lower'])
    check('zero_numerator_holds', bounds(z,z,o,o,o)['status'].startswith('HOLD'))
    check('negative_numerator_holds', bounds(z,z,F(2),o,o)['status'].startswith('HOLD'))
    invalid=[(o,z,z,o,o),(z,o,z,o,o),(-o,z,z,o,o),(z,-o,z,o,o),
             (z,z,-o,o,o),(z,z,z,z,o),(z,z,z,F(2),o)]
    for i,args in enumerate(invalid):
        try:
            bounds(*args)
        except ValueError:
            rejected=True
        else:
            rejected=False
        check('invalid_domain_'+str(i), rejected)
    # Z=diag(5/3,1,0), U=[e1,e2], V=[(3/5,0,4/5),e2], S=I.
    # Both Grams=I, equation=0, but sigma1(Z)=5/3 vs proposal1=1.
    Z=[[F(5,3),z,z],[z,o,z],[z,z,z]]
    V=[[F(3,5),z],[z,o],[F(4,5),z]]
    U=[[o,z],[z,o],[z,z]]
    product=[[sum(Z[i][k]*V[k][j] for k in range(3)) for j in range(2)] for i in range(3)]
    gram=[[sum(V[k][i]*V[k][j] for k in range(3)) for j in range(2)] for i in range(2)]
    check('reverse_countermodel_equation_exact',product==U)
    check('reverse_countermodel_right_gram_exact',gram==[[o,z],[z,o]])
    check('no_two_sided_singular_error_inference',F(5,3)-1 > F(1,1<<41))
    check('restricted_is_not_ambient_condition',F(5,3)>bounds(z,z,z,o,o)['condition'])
    # Z=diag(2,1), q=1,U=V=e1,S=2: retained lower alone gives no tail bound.
    check('missing_tail_can_hide_extra_cutoff_value', F(1)>F(1,2))
    check('lower_cutoff_equality_does_not_certify_strict', not (F(1,2)>F(1,2)))
    check('upper_cutoff_equality_does_not_certify_strict', not (F(1,2)<F(1,2)))
    return {'status':'PASS_EXACT_PARTIAL_FACTOR_CONTROLS','count':len(rows),'rows':rows,
            'countermodels_are_actual_backend_failures':False}


def run(repo, out):
    import numpy as np
    here=Path(__file__).resolve().parent
    freeze=json.loads((here/'FREEZE.json').read_text())
    for rel,digest in freeze['code'].items():
        assert sha(here/rel)==digest, ('code identity',rel)
    for rel,pin in freeze['sources'].items():
        p=repo/rel
        assert p.stat().st_size==pin['size_bytes'] and sha(p)==pin['sha256'], ('source identity',rel)
    out.mkdir(parents=True,exist_ok=False)
    prior=json.loads((repo/BACKEND/'primary/CERTIFICATE.json').read_text())
    # The previous certificate supplies the SAME exact rational source multiplier.
    C=rat(prior['source_constants']['C'])
    assert C==rat(freeze['inherited_noise_multiplier_upper'])
    records=[]
    for name in CASES:
        cert=json.loads((repo/SOURCE/'primary'/name/'CERTIFICATE.json').read_text())
        m=cert['row']['measured']
        a,b,r=map(rat,[m['etaU'],m['etaV'],m['xi']])
        # Check exact square-enclosure consistency, not the original matrix computations.
        for val,key in [(a,'left_Gram_F'),(b,'right_Gram_F'),(r,'singular_equation_F')]:
            assert val>=0 and val*val >= rat(m['exact_squared'][key])
        with np.load(repo/SOURCE/'campaign/cases'/name/'results'/name/'SVD_META.npz',allow_pickle=False) as data:
            s=data['singular']
        assert s.shape==(321,) and s.dtype==np.float64
        assert all(math.isfinite(float(x)) and float(x)>=0 for x in s)
        sv=[F(*float(x).as_integer_ratio()) for x in s]
        assert all(x>=y for x,y in zip(sv,sv[1:]))
        tau=F(1,1<<24)
        assert tau not in sv and sum(x>tau for x in sv)==209
        small,large=sv[208],sv[0]
        assert small==rat(m['proposed_smin'])
        answer=bounds(a,b,r,small,large)
        assert answer['status']=='POSITIVE_PARTIAL_FACTOR_LOWER_BOUND'
        parent=json.loads((repo/SOURCE/'campaign/cases'/name/'inputs/PARENT_ORDER.json').read_text())
        tail=rat(parent['qplus1_sigma_upper'])+C*F(3,1<<49)
        source_lower=rat(parent['qth_sigma_lower'])-C*F(3,1<<49)
        assert tail==rat(prior['data_singular_enclosures']['s210_upper'])
        assert source_lower==rat(prior['data_singular_enclosures']['s209_lower'])
        gates={'positive_lower':answer['lower']>0,
               'true_qth_above_cutoff':answer['lower']>tau,
               'inherited_tail_below_cutoff':tail<tau,
               'one_sided_overstatement_below_2^-41':answer['debit']<F(1,1<<41),
               'restricted_condition_below_reporting_1888':answer['condition']<1888,
               'posterior_lower_improves_inherited_source_lower':answer['lower']>source_lower}
        assert all(gates.values())
        records.append({'case':name,'q':209,'shape':[8191,321],
          'inherited_etaU':pair(a),'inherited_etaV':pair(b),'inherited_equation_upper':pair(r),
          'saved_s209':pair(small),'saved_s1':pair(large),
          'exact_rational_bounds':{k:pair(answer[k]) for k in ['lower','upper','debit','condition','inverse_restriction_upper']},
          'inherited_tail_upper':pair(tail),'inherited_source_lower':pair(source_lower),
          'gates':gates,'readable':{k:float(answer[k]) for k in ['lower','upper','debit','condition','inverse_restriction_upper']},
          'retained_norm_certificate_is_inherited':True,'fresh_matrix_norm_recomputation':False,
          'all_indexed_singular_values_two_sided_accuracy_certified':False,
          'ambient_condition_certified':False})
    result={'status':'DERIVED_FINITE_PARTIAL_FACTOR_POSTERIOR_CONDITIONAL_ON_INHERITED_NORMS',
            'records':records,'source_freeze_sha256':sha(here/'FREEZE.json'),
            'rank_statement':'Exactly209 singular values exceed cutoff, conditional on inherited source tail and retained norm premises',
            'condition_object':'Z restricted to span of the saved retained RIGHT factor, with induced Euclidean metric',
            'normalization':'Normalized projected real matrix; not SI or finite-field arithmetic',
            'two_sided_B1_closed':False,'uniform_backend_conformance':'OPEN',
            'new_estimator_calls':0,'new_raw_records':0,'new_factor_copies':0,
            'physical_promotion':0,'external_promotion_review':'PENDING'}
    for file,data in [('CERTIFICATE.json',result),('CONTROLS.json',controls())]:
        (out/file).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'cases':[{**{'case':x['case']},**x['readable']} for x in records]}))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True)
    args=p.parse_args();run(Path(args.repo).resolve(),Path(args.out).resolve())
