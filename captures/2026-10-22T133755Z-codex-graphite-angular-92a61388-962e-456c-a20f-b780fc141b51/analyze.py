"""Source-bound angular-knot and archived-stencil audit; no LAMMPS execution."""
import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
import numpy as np

POTENTIAL_SHA = '70b77656397c0468631af41883d3b781f30432189f749eb0c3d724141055cbd4'
SOURCE_SHA = 'cbe2b802e554212d2a2244d30ecd26f4d48c1fcebe5a9cb20610b643c12b0a58'
LADDER_SHA = '35e90cb6f5951de3a5c324c0aa4d4c17cfa8c162e814d09d129b0a3cde6c639d'
RAW_SHA = {
    '21_dir_0': '2543d68fb4d2ca6ecb70eee5ff1754a566350496a9074cdaf9ec8b3674e44684',
    '21_dir_10024': 'bd670bbe7dccb52d75f485482b99c009d7e1a64ce83e4792ed52c7bba35c430c',
}

def check(path, expected):
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise ValueError(f'byte identity mismatch: {path}: {actual}')


def derivative_at(coeff, x, n):
    from math import factorial
    return sum(coeff[k] * Decimal(factorial(k) // factorial(k-n)) * x**(k-n)
               for k in range(n, 6))


def hinge_kernel(h, t):
    """One-sided second-order difference Qplus-Qminus for B*(x-t)_+^2."""
    p = lambda x: np.maximum(x-t, 0.)**2
    return (-6*p(0.)+4*p(h)+4*p(-h)-p(2*h)-p(-2*h))/(2*h)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--potential', type=Path, required=True)
    ap.add_argument('--source', type=Path, required=True)
    ap.add_argument('--ladder', type=Path, required=True)
    ap.add_argument('--raw-dir', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args=ap.parse_args()
    for path, sha in ((args.potential,POTENTIAL_SHA),(args.source,SOURCE_SHA),(args.ladder,LADDER_SHA)):
        check(path, sha)
    source=args.source.read_text()
    assert 'if (Nij <= NCmin)' in source and 'if (Nij >= NCmax)' in source
    assert 'if (costh >= gCdom[i] && costh <= gCdom[i+1])' in source
    assert 'g = gSpline(cosjik,(NijC+NijH),itype,&dgdc,&dgdN)' in source
    getcontext().prec=50
    block=args.potential.read_text().split('# gC1 and gC2',1)[1].split('# gH',1)[0].split()
    assert block[:6]==['5','-1.0','-0.6666666667','-0.5','-0.3333333333','1.0']
    coeff=[list(map(Decimal,block[6+6*i:12+6*i])) for i in range(8)]
    assert len(block)==54
    x=Decimal('-.5')
    delta={}
    for name,i in (('gC1',0),('gC2',4)):
        delta[name]=[str(derivative_at(coeff[i+2],x,n)-derivative_at(coeff[i+1],x,n)) for n in range(6)]
        assert all(Decimal(z)==0 for z in delta[name][:3])
    assert coeff[:3]==coeff[4:7]  # identical polynomials for all segments below -1/3
    records=json.loads(args.ladder.read_text())
    out={'source_commit':'611ca3b7f8525ba802373b04f9e3d632d515f7e3',
         'source_and_input_sha256':{'pair_airebo.cpp':SOURCE_SHA,'CH.rebo':POTENTIAL_SHA,'LADDER.json':LADDER_SHA,**RAW_SHA},
         'angular_join_cos':-0.5,'right_minus_left_derivatives_order_0_to_5':delta,
         'gC1_gC2_identical_first_three_segments':True,
         'model':'DESCRIPTIVE single quadratic force hinge plus cubic-in-h smooth remainder; no atom-resolved identification or physical fit',
         'cases':{}}
    for case, rec in records.items():
        path=args.raw_dir/f'{case}_ladder_raw.npz'; check(path,RAW_SHA[case])
        z=np.load(path)
        h=np.array([r['h_A'] for r in rec['step_ladder']]); s=np.array([r['side_fixed_eV_per_A2'] for r in rec['step_ladder']])
        assert np.array_equal(h,z['steps_A'])
        assert np.max(abs(z['projected_forces'][:,:,rec['component']])) > 0
        # Recompute each one-sided difference directly from the archived projected forces.
        f0=z['baseline'][rec['component']]; f=z['projected_forces'][:,:,rec['component']]
        qp=-(-3*f0+4*f[:,0]-f[:,1])/(2*h)
        qm=-(3*f0-4*f[:,2]+f[:,3])/(2*h)
        assert np.max(abs(qp-qm-s)) < 1e-10
        # The sign of t cannot be inferred from this symmetric side-difference kernel.
        best=None
        for t in np.linspace(0.1e-6,15e-6,1491):
            X=np.stack((hinge_kernel(h,t),h**3),axis=1)
            beta=np.linalg.lstsq(X,s,rcond=None)[0]
            err=X@beta-s
            if best is None or np.linalg.norm(err)<best[0]: best=(np.linalg.norm(err),t,beta,err)
        _,t,beta,err=best
        out['cases'][case]={'probe':rec['probe'],'component':rec['component'],
           'h_A':h.tolist(),'observed_side_eV_per_A2':s.tolist(),
           'coarse_to_fine_absolute_ratio':float(abs(s[0]/s[-1])),
           'single_hinge_descriptive_fit':{'absolute_t_A':float(t),'B_eV_per_A3':float(beta[0]),
               'cubic_remainder_coefficient_eV_per_A5':float(beta[1]),
               'max_abs_residual_eV_per_A2':float(np.max(abs(err))),
               'rms_residual_eV_per_A2':float(np.sqrt(np.mean(err**2)))},
           'raw_replay_max_difference_eV_per_A2':float(np.max(abs(qp-qm-s)))}
    assert hinge_kernel(np.array([8e-5,1e-6]),0.).tolist()==[0.,0.]
    args.output.write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__': main()
