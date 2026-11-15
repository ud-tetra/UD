#!/usr/bin/env python3
"""Independent, source-bound math audit of historical Distinction Theory Gap 2.

Scope: March Ω(n) ansatz, constant Phi, and log-linear scale map. No empirical
prediction is fitted or validated. Prints JSON receipt and writes a copy.

Run: python UD_GAP2_SIGN_SCALE_INDEPENDENT_CHECK_v0.2.py
"""
from pathlib import Path
import hashlib
import json
import mpmath as mp
import sympy as sp

ROOT=Path(__file__).resolve().parent
SOURCE_FILES=[
    'Gap2_REVISED_Omega_Convergence.md',
    'Gap2_FINAL_STATUS.md',
    'v07_Diagnostic_Analysis.md',
    'coherence_equation.md',
    'DistinctionTheory_MasterTheory_v1.md',
    'UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md',
]

n,D,Oi,rho,L,q=sp.symbols('n Delta Omega_inf rho L q',positive=True)
om=Oi-D*rho**n
# P(n) = P0/[Omega(n)*constant_Phi], with log-linear k(n).
ns_minus_1=sp.simplify(-q*sp.diff(sp.log(om),n))
alpha_s=sp.simplify(q*sp.diff(ns_minus_1,n))
alpha_expected=sp.simplify((q**2)*D*Oi*rho**n*sp.log(rho)**2/om**2)
assert sp.simplify(alpha_s-alpha_expected)==0
assert sp.simplify(alpha_s.subs(q,1/L)-alpha_s.subs(q,-1/L))==0

# Arbitrary positive Phi(n) can change the sign only if its log curvature exceeds
# the fixed positive Omega contribution.
Phi=sp.Function('Phi')(n)
alpha_phi=sp.simplify(-q*q*sp.diff(sp.log(om*Phi),n,2))
assert sp.simplify(alpha_phi-(alpha_s-q*q*sp.diff(sp.log(Phi),n,2)))==0

# General nonlinear map n(t), with t=ln(k/k0), has an extra n'' term.
t=sp.symbols('t',real=True)
nt=sp.Function('n_of_logk')(t)
general=sp.simplify(sp.diff(-sp.diff(sp.log(Oi-D*rho**nt),t),t))
expected_general=sp.simplify(
    (D*Oi*rho**nt*sp.log(rho)**2/(Oi-D*rho**nt)**2)*sp.diff(nt,t)**2
    + (D*rho**nt*sp.log(rho)/(Oi-D*rho**nt))*sp.diff(nt,t,2)
)
assert sp.simplify(general-expected_general)==0

mp.mp.dps=60
R=mp.power(4,-mp.mpf(1)/3)
LOG_SCALE=mp.log(1/R)
OMEGA_INF=mp.mpf('1.10')
DELTA=mp.mpf('0.477')
RHO=mp.mpf('0.898')
LAM=-mp.log(RHO)
N_TARGET=mp.mpf('0.9649') # Historical Planck input; NOT independent prediction.
d=1-N_TARGET
A_APPROX=DELTA*LAM/(OMEGA_INF*LOG_SCALE)
n_approx=mp.log(d/A_APPROX)/mp.log(RHO)
x_target=(d*LOG_SCALE)/(LAM+d*LOG_SCALE)
n_exact=mp.log(x_target*OMEGA_INF/DELTA)/mp.log(RHO)

def omega(nn): return OMEGA_INF-DELTA*RHO**nn

def ns(nn,s):
    return 1-s/LOG_SCALE*DELTA*LAM*RHO**nn/omega(nn)

def alpha_formula(nn):
    return DELTA*OMEGA_INF*LAM**2*RHO**nn/(LOG_SCALE**2*omega(nn)**2)

def alpha_fd(nn,s,step=mp.mpf('0.00001')):
    # t=ln(k/k_ref), n(t)=nn+s*t/L; central difference in t.
    return (ns(nn+s*step/LOG_SCALE,s)-ns(nn-s*step/LOG_SCALE,s))/(2*step)

alpha_exact=alpha_formula(n_exact)
alpha_approx=d*LAM/LOG_SCALE
alpha_direct_identity=alpha_approx+d**2
assert abs(alpha_exact-alpha_direct_identity)<mp.mpf('1e-45')
for sign in [1,-1]:
    assert alpha_formula(n_exact)>0
    assert abs(alpha_fd(n_exact,sign)-alpha_formula(n_exact))<mp.mpf('1e-10')
assert ns(n_exact,1)-N_TARGET < mp.mpf('1e-45')
assert ns(n_exact,-1)>1

# The later Gap 2 status is a distinct fit stratum; cannot splice A or rho from it.
A_LATE=mp.mpf('0.051')
RHO_LATE=mp.mpf('0.891')
n_late_approx=mp.log(d/A_LATE)/mp.log(RHO_LATE)
alpha_late_approx=d*(-mp.log(RHO_LATE))/LOG_SCALE

# A separate constant-retention route gives a fixed index but no running.
ns_eta=1+mp.log(mp.mpf(61)/62)/LOG_SCALE

# The early 9-value series is not monotone, contrary to the historical prose.
initial_omega=[mp.mpf(s) for s in ['0.674','0.626','0.693','0.735','0.798','0.837','0.863','0.884','0.897']]
assert initial_omega[1]<initial_omega[0]

fmt=lambda v:mp.nstr(v,18)
checks={
    'symbolic_exact_model':str(om),
    'spectral_tilt_minus_one':str(ns_minus_1),
    'spectral_running_exact':str(alpha_s),
    'spectral_running_positive_form':str(alpha_expected),
    'orientation_reversal_same_running':True,
    'Phi_variation_symbolic_identity':str(alpha_phi),
    'general_logk_map_symbolic_identity':str(general),
    'historical_pivot_ns_used_as_input':fmt(N_TARGET),
    'historical_early_approx_A_computed':fmt(A_APPROX),
    'historical_early_approx_n_inferred':fmt(n_approx),
    'historical_early_exact_n_inferred':fmt(n_exact),
    'historical_early_approx_running_positive':fmt(alpha_approx),
    'historical_early_exact_running_positive':fmt(alpha_exact),
    'historical_early_exact_running_crosscheck':fmt(alpha_direct_identity),
    'historical_early_finite_diff_positive':fmt(alpha_fd(n_exact,1)),
    'historical_early_reverse_orientation_ns':fmt(ns(n_exact,-1)),
    'historical_early_reverse_orientation_running_positive':fmt(alpha_fd(n_exact,-1)),
    'later_distinct_fit_approx_n_inferred':fmt(n_late_approx),
    'later_distinct_fit_approx_running_positive':fmt(alpha_late_approx),
    'coherence_independent_constant_eta_ns':fmt(ns_eta),
    'coherence_independent_constant_eta_running':0,
    'early_Omega_monotonicity_claim_refuted_by_level_0_to_1':True,
    'source_gaps_unclosed':['derivation_of_mode_creation_index','fixed_lattice_to_3D_curvature_power','physical_pivot_scale_map','sourced_Phi_evolution','raw_replay','target_blind_registration'],
}
receipt={
    'artifact':'UD_GAP2_SIGN_SCALE_INDEPENDENT_CHECK_v0.2',
    'claim_bin':'EXACT_CONDITIONAL_NO_GO + NUMERICAL_SOURCE_REPLAY',
    'physical_promotion':0,
    'assumptions':{
        'Omega':'Omega_inf - Delta*rho**n',
        'domain':'0<rho<1, 0<r<1, Delta>0, Omega_inf>Delta, n>=0',
        'Phi':'constant positive in base case',
        'source_spectrum':'P(k) proportional to 1/[Omega(n(k))*Phi]',
        'scale_map':'ln(k/k0) = s*n*ln(1/r), s in {-1,+1}',
        'target_bearing_numbers_are_illustrations':'all historical comparison values are already target exposed',
    },
    'source_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in SOURCE_FILES},
    'checks':checks,
    'verdicts':{
        'sign_repair':'alpha_s POSITIVE for both orientations in stated ansatz',
        'joint_red_tilt_negative_running':'NO-GO under fixed Phi + exponential Omega + affine log-k map',
        'physical_claim':'OPEN; nothing promoted',
        'historical_sources':'unchanged',
    },
}
report_path=ROOT/'UD_GAP2_SIGN_SCALE_CHECK_RECEIPT_v0.2.json'
report_path.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'receipt':str(report_path),'math':checks,'result':receipt['verdicts']},indent=2))