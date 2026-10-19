"""v2 source-certified shift allowance conditional on seven frozen engineering maxima.

No record outcome enters derive(). Strict acceptance; inconclusive comparisons HOLD.
The old eight-gate policy and its HOLD remain separate immutable evidence.
"""
import json, hashlib
from pathlib import Path
from flint import arb, fmpq, ctx
ctx.prec = 512
P = Path(__file__).resolve().parent
BITS = 180
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

def a(pair):
    assert len(pair) == 2 and all(type(x) is int for x in pair) and pair[1] > 0
    return arb(fmpq(*pair))

def up(x):
    n = (x * (1 << BITS)).ceil().unique_fmpz()
    assert n is not None
    return [int(n), 1 << BITS]

def down(x):
    n = (x * (1 << BITS)).floor().unique_fmpz()
    assert n is not None
    return [int(n), 1 << BITS]

def freeze():
    f = json.loads((P/'FREEZE.json').read_text())
    for n, h in f['code_sha256'].items():
        assert sha(P/n) == h, ('frozen code', n)
    for n, h in f['input_sha256'].items():
        assert sha(P/'inputs'/n) == h, ('frozen input', n)
    return f

def terms():
    freeze()
    old = json.loads((P/'inputs/PR210_FREEZE.json').read_text())
    g = {k:v for k,v in old['gates'].items() if k != 'raw_shift_residual'}
    u = json.loads((P/'inputs/PARENT_UNIFORM.json').read_text())
    m = json.loads((P/'inputs/PARENT_PHASE.json').read_text())['metrics']
    o = json.loads((P/'inputs/PARENT_ORDER.json').read_text())
    eta, eps = a(g['full_left_orthogonality']), a(g['full_SVD_error'])
    r, C = a(u['baseline_low_rank_residual_upper']), a(u['per_vector_noise_multiplier_upper'])
    delta = a(old['encoded_vector_noise'])
    s0, tail0, cut = a(o['qth_sigma_lower']), a(o['qplus1_sigma_upper']), a(old['source_cutoff'])
    alpha, e = s0-r, r+C*delta+eps
    assert 0 <= eta < 1 and alpha > 2*e
    sine = e/(alpha-e)
    polar = eta/(1+(1-eta).sqrt())
    distance = (2-2*(1-sine*sine).sqrt()).sqrt()+2*polar
    beta = a(u['deleted_two_rows_beta_lower'])
    assert beta > distance
    eta0 = a(m['basis_orthogonality_upper'])
    rho = a(g['inverse_residual'])
    assert 0 <= eta0 < 1 and 0 <= rho < 1
    k0, ka = ((1+eta0)/(1-eta0)).sqrt(), ((1+eta)/(1-eta)).sqrt()
    hD = a(m['source_inverse_norm_upper'])/(1-a(m['source_inverse_residual_upper']))
    K = k0*hD*a(m['source_reduction_norm_upper'])
    L = hD*a(m['intertwining_residual_upper'])
    E = a(g['eigenpair_residual'])*a(g['proposed_inverse_norm'])/(1-rho)
    gamma = (1-eta).sqrt()
    sep, arg = a(m['minimum_target_chord_lower']), a(g['emitted_argument_error'])
    x = sep/2-arg
    assert K > 0 and 0 < x < arb.pi()/2 and sep <= 2
    # sin(x)<x<=sep/2 simultaneously enforces disk and angular separation.
    Rlim = x.sin()
    sigma0, M0 = a(u['comparison_shift_residual_upper']), a(u['comparison_shift_norm_upper'])
    Scrit = gamma*((beta-distance)*((Rlim-L)/K-ka*E)-sigma0-distance*(1+M0))
    assert Scrit > 0
    order = bool(s0-C*delta-eps > cut and tail0+C*delta+eps < cut)
    assert order
    return dict(g=g, distance=distance, beta=beta, gamma=gamma, K=K, L=L,
                E=E, ka=ka, sigma0=sigma0, M0=M0, sep=sep, arg=arg,
                Rlim=Rlim, Scrit=Scrit, order=order)

def derive():
    t = terms()
    return {'status':'CERTIFIED_SOURCE_CONDITIONAL_SHIFT_ALLOWANCE_V2',
            'other_seven_gates':t['g'], 'raw_shift_strict_upper_allowance_lower':down(t['Scrit']),
            'raw_shift_allowance_upper':up(t['Scrit']), 'eigenvalue_radius_limit_lower':down(t['Rlim']),
            'subspace_distance_upper':up(t['distance']), 'target_chord_lower':down(t['sep']),
            'threshold_count209':t['order'], 'equality_or_inconclusive':'HOLD',
            'readable':{'shift_allowance_lower':float(a(down(t['Scrit'])).lower()),
                        'half_target_chord_lower':float((t['sep']/2).lower())},
            'old_policy_modified':False, 'universal_solver_admission_claimed':False,
            'physical_promotion':0, 'external_review':'PENDING'}

def evaluate(metrics, eligible):
    t = terms()
    checks = {n:bool(0 <= a(metrics[n]) <= a(v)) for n,v in t['g'].items()}
    s = a(metrics['raw_shift_residual'])
    allowance = a(down(t['Scrit']))
    checks['encoded_input_eligible'] = eligible is True
    checks['source_calculated_shift_allowance'] = bool(0 <= s < allowance)
    radius = t['L']+t['K']*((t['sigma0']+s/t['gamma']+t['distance']*(1+t['M0']))/(t['beta']-t['distance'])+t['ka']*t['E'])
    angle = radius.asin()+t['arg'] if bool(0 <= radius < 1) else None
    checks['strict_source_matching'] = bool(angle is not None and 2*radius < t['sep'] and 2*angle < t['sep'])
    passed = all(checks.values())
    result = {'status':'CERTIFIED_RETURNED_OUTPUT_V2' if passed else 'HOLD_V2',
              'checks':checks, 'failed':[k for k,v in checks.items() if not v],
              'radius_upper':up(radius),
              'phase_error_upper_if_certified':up(angle) if passed else None,
              'original_policy_status_unchanged':True, 'physical_promotion':0}
    if passed:
        result['readable_phase_error_upper'] = float(angle.upper())
        result['matching_margin_lower'] = down(t['sep']/2-angle)
    return result

if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');args=p.parse_args()
    r=derive();dest=P/'SOURCE_ALLOWANCE.json'
    if args.replay: assert json.loads(dest.read_text()) == r
    else:
        assert not dest.exists();dest.write_text(json.dumps(r,indent=2))
    print(json.dumps(r),flush=True)
