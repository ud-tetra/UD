# Robust nonlinear trapping — RHT v0.1

Development, no registry entry. DERIVED CONDITIONAL under the unchanged UD action and explicit symmetry-preserving error class. Independent review pending; physical promotion 0.

For every finite rank, a,N>0 and 0<epsilon<=10^-5, use the inherited m=min(a,N*epsilon)/2, J=max(a,25*N), R0=3*m/(62*N). Select any target 0<eta<=R0. Define B_eta=m*eta^2/2, delta_eta=eta*sqrt(m/(2*J)), nu_star=m*eta/16.

Static gauge/species-phase invariant Hamiltonian errors with gradient norm <=nu_star on the eta tube preserve all-time trapping from the delta_eta initial ball. On zero Gauss there is a nonempty compact invariant minimizing set within eta/8 of the nominal orbit, stable as a set. The old orbit itself need not be invariant; neither unique shifted equilibrium nor retained degeneracy is proved.

For time-dependent errors, additionally require integral_0^T sup_tube ||grad partial_t V_t|| <=nu_star and a uniform amplitude-gradient bound <=nu_star. This traps through T. Arbitrarily small bounded resonant drive need not permit an all-time guarantee without a cumulative work/variation condition. The exact oscillator counterexample is scoped to that generic inference, not a classification of forced UD dynamics.

## Coefficient and readout requirements

Admit kinetic errors A=max|Delta a_e|, normalized diamond errors K=max|Delta kappa_d|/(r*N), relative hopping errors G=max|xi_e|, and scalar site-detuning half-range D=(max v_i-min v_i)/2. It suffices that

    A*eta + N*((1+12*eta)*K + 14*G + 3*D) <= m*eta/16.

The corresponding derivative-coefficient formula bounds the time-variation integrand. Uniform detuning/mass shifts are constant on the norm surface and spend no relative-energy budget. The carrier, equal norms and Gauss law are preserved.

Complex loop-readout errors are below 21*eta per channel. Oriented phase errors have L2 norm below 180*eta. For six real channels choose eta<=min(R0,epsilon/1680) and instrument error per channel<=epsilon/80; model motion and instrument together then fit the inherited epsilon/40 classifier budget. Real channels discriminate three families, not overall sign. Oriented phases retain the prior 26-label discrimination with instrument phase L2 error <=(5/2)*sqrt(epsilon).

All distances use the declared product metric: unnormalized Frobenius links/electric fields and real round unit spheres on psi/sqrt(N),bar(chi)/sqrt(N). No componentwise or physical-unit interpretation follows without a separate map.

## Reproduction

- Python 3 + SymPy: run python3 verify_robustness.py for 30 exact rational/integer/symbolic checks.
- NumPy, SciPy, python-flint 0.9.0: run python3 check_robust_gradients.py for six NUMERICAL synthetic matrix-gradient/readout fixtures (no empirical data; Gauss not enforced because bounds hold on the larger norm surface).
- Standard-library exact calculator: python3 robustness_budget.py --a 1 --N 1 --epsilon 1/100000 . Add --real-readout for the stricter target. Optional --A, --K, --G, --D and --gradient-variation enter mathematical upper bounds.

Zero default errors are illustrative assumptions, not measurements. For time variation the coefficient caps must hold over the whole interval. Out of a sufficient budget is not proof of instability. The forcing-only cumulative-displacement budget is a separate contract; it does not combine automatically with Hamiltonian-error budgets.

Seven inherited files are copied unchanged, with hashes and source capture in PROVENANCE_v0.1.json. The prior NEB 211-check interval certificate remains a dependency; no new interval cells are counted here. The eight-page manuscript provides the analytic transfer proofs.

## Remaining obligations

No epsilon=0 quantitative modulus, sharp basin, unique perturbed branch, nonlinear attraction, infinite-rank flow or physical realization is established. The requirements contract is mathematical: laboratory state, energy, clock and detector maps remain open. Independent review is separate from constructor replay. The action and coefficient ledger are unchanged.
