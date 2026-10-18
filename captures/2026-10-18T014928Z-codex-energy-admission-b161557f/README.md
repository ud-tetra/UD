# Energy and residual admission — ERA v0.1

DERIVED CONDITIONAL; development, no registry entry. Constructor verification only; independent review pending; physical promotion 0. Nominal action and coefficient ledger unchanged.

The seven-page theorem adds a geometry-and-actual-energy gate to the frozen endpoint preparation contract. If P_upper≤eta²/4 and F_upper≤B/2, with B=N eta⁴/1600 and the shared error budget, ambient Hamiltonian flow stays within eta. The geometry gate has no prior local-chart assumption. Energy means the total actual Hamiltonian minus its value on the frozen reference orbit, including norm/coefficient errors. It is not the nominal energy alone. A rank-one zero-Gauss diamond circulation is accepted at exactly 2.5 times the older sufficient initial radius.

Actual conserved norms n_q,n_w are individually normalized to unit coordinate vectors, retaining their actual symplectic weights. They create a centered curvature allowance beta_norm=20(|n_q−N|+|n_w−N|), which shares the existing budget with other errors. This admits uncertainty in positive constant norm scales; it does not cover non-Hamiltonian norm leakage.

The confinement proof holds on the ambient manifold at nonzero Gauss levels. Their residual is conserved and obeys an explicit distance envelope. This does not make such states solutions of the zero-source constrained action. The exact summed trace is n_w−n_q, so unequal norms exclude zero Gauss on this closed carrier. Equal norms alone do not solve the matrix constraints. In the frozen residual cone, distance to neutrality is t/sqrt(2) for an explicit family with residual norm t²: a linear correction-distance estimate fails there. No quantitative nonlinear full-state projection is supplied.

## Replay and inputs

- `python3 verify_energy_admission.py`: Python standard library; regenerates 49 exact finite/rational checks, eight budget fixtures, invalid-input controls and rational matrix Gauss fixtures. Analytic geodesic, Noether and cone proofs remain in the paper.
- `OPENBLAS_NUM_THREADS=1 python3 check_norm_gauss.py`: NumPy/SciPy floating diagnostics; 32 geodesic Hessian fixtures, four centering and four Gauss-envelope/covariance controls at ranks 1,2,3,5. No trajectories, empirical data or interval certification.
- `python3 energy_admission.py INPUT.json`: rational upper-bound calculator. Example inputs and full results are in ENERGY_ADMISSION_CERTIFICATE_v0.1.json; save a fixture's `input` object as INPUT.json. Empty input is an assumed ideal example, not a measurement. Optional keys are a,N,eta,nq,nw,score_upper,energy_upper,nu,beta_other,variation. Norm intervals contain two positive ordered strings; other coefficients/upper bounds are rational strings. Norms differing from N must be supplied explicitly when N differs from the unit default. Every returned gate is conditional on certified coverage and model identification.
- The copied `preparation_certificate.py` computes P_upper from the earlier 27 raw invariant intervals. Use its result with target_squared=eta²/4, then pass its score_upper to the new energy calculator. The full sufficient scalar contract adds two norm readings and one actual relative-energy reading (30 total); this is not a minimality or physical acquisition-cost claim.

At a=N=1, eta=1/829538022, the geometry score cap is about 3.63e-19, the actual relative-energy cap 6.60e-40 and the norm-error-only sum cap 5.68e-24. The geometric ceiling ratio (~6.88e21) is conditional on the extra energy test, not an overall measurement improvement or basin-volume gain. No necessary physical precision is derived.

Unchanged copied calculators and certificates are hash-bound. Frozen ERT/PET/GPC/RGC inputs retain their conditional scopes. Next: a typed external-source or defect-work contract, then physical realization/data availability work. No empirical GUT conclusion is asserted. Other workstream observer/sketch and floating-estimator results are unchanged.
