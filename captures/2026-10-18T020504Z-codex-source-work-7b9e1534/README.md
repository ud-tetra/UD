# Controlled source and defect work — SDW v0.1

DERIVED CONDITIONAL; development, no registry entry; constructor verification only; independent review pending; physical promotion 0. The nominal action and ledger remain unchanged.

The seven-page theorem extends the frozen endpoint admission gate to positive varying species norms and continuous tangent non-Hamiltonian defects. In addition to the existing initial geometry/actual-energy and mixed-amplitude contracts, require

    eta*T_parameter + 10*eta^2*L_norm_positive + W_defect_prefix <= B/4.

Absolute norm variation still enlarges the centered-curvature envelope: beta_total=beta_other+20*(D_initial+L_norm_absolute). A graph Rayleigh bound gives f(U,z)+rho>=0 globally; near the orbit it is <=10*d². Thus pure base norm loss spends no positive norm-work budget, while norm gain does. Other norm-dependent errors require their separate parameter-derivative contribution in T_parameter.

W_defect_prefix must bound signed defect work at EVERY time prefix. Terminal net energy cancellation can hide an earlier exit; an exact canonical-oscillator counterexample is included. A certified direct prefix-work bound may sharpen the conservative full-tube gradient-times-path-length bound. The constant-rate inequality includes a quadratic duration term because norm drift enlarges the defect-work coefficient.

The exact source equation is Gdot=S in temporal gauge, with S=d_xG[Y]−ell_q*q*q†+ell_w*w*w†, and its covariant multiplier version. Summed trace(S)=ell_w−ell_q. The Gauss norm can drift by at most K_G*L_Y+L_norm_absolute, with K_G explicit. Exact zero-source admissibility requires initial zero Gauss and S=0 pointwise; energy confinement or a small drift bound is not repair. An external charge satisfying the same source equation is only a compatibility prescription, not a physical source sector constructed from UD.

Additive raw matter forcing is decomposed exactly into norm flux and normalized sphere-tangent forcing. A declared radial-loss control can leave normalized distance and relative energy zero while creating Gauss charge. White noise, jumps without a certified bridge, nonunitary/off-sphere outputs and arbitrary integrators are outside this continuous finite-variation theorem.

## Replay and inputs

- `python3 verify_source_work.py`: standard library; 43 exact finite/rational checks, twelve budget examples, invalid-input controls, raw projection and commutator algebra, terminal-work counterexample and rate-horizon identity. Full analytic arguments remain in the manuscript.
- `OPENBLAS_NUM_THREADS=1 python3 check_source_balance.py`: NumPy/SciPy floating diagnostics at ranks 1,2,3,5; four full-matrix source/trace/raw-force controls and eight centered ground-shift controls. General derivative fixtures with electric norm 0.1 are not endpoint-tube preparations; no trajectories or empirical data.
- `python3 source_work_budget.py INPUT.json`: use any fixture's `input` object from SOURCE_WORK_CERTIFICATE_v0.1.json. Rational strings are required for exact noninteger input. Initial norm intervals default to [N,N] as an illustrative assumption. Every bound requires guaranteed joint coverage; no measurement is inferred from the defaults.

Keys: a,N,eta,nq0,nw0,leakage_q,leakage_w,norm_gain_q,norm_gain_w,parameter_variation,defect_length,work_upper,score_upper,energy_upper,nu,beta_other,g0_upper,source_integral_upper. Norm initial intervals have two positive ordered endpoints. Absolute leakage bounds total variation, not terminal norm change. Optional gain bounds cover positive variation; otherwise absolute variation is used conservatively. `parameter_variation` covers actual explicit and norm-parameter potential derivatives. `work_upper` is an EVERY-PREFIX signed-work upper; `source_integral_upper` bounds the integral of the source norm. The calculator takes the tighter of supplied and speed-derived valid bounds. It does not infer source cancellation or data realizability. Initial Gauss is not assumed zero if its optional bound is absent.

At a=N=1 and inherited eta=1/829538022: B/4≈3.30e-40, norm-only absolute variation amplitude cap≈5.68e-24, and speed-only defect path cap≈1.09e-32 in model units. These are conservative sufficient bounds, not necessary physical precision or feasibility specifications. Mixed inputs share one budget.

Unchanged ERA/PET/GPC support files are hash-bound. Next: select a measurable realization or certify a reconstructed trajectory, then audit published data for the required observables and uncertainty information. No coupling unification, proton decay, monopole or other physical GUT conclusion is promoted. The separate 600-cell observer/sketch/estimator workstream is unchanged.
