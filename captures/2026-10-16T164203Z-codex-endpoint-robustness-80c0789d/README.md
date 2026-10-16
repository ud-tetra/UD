# Robust trapping at the quartic endpoint — ERT v0.1

Development, no registry entry. DERIVED CONDITIONAL under the frozen nominal action and an explicit symmetry-preserving uncertainty class. Independent review pending; physical promotion 0.

For epsilon=0 at each finite rank, use the PET radius R_p, choose 0<eta<=R_p, c=N/1600, J=max(a,25N), B=c eta^4, delta=eta^2 sqrt(c/J) and nu_star=c eta^3/8. Split V=V_g+V_c into a generic error with gradient<=nu and a centered error with zero gradient on the nominal orbit and Hessian norm<=beta. The sufficient mixed condition is

    nu + eta*beta <= N eta^3/12800.

Initial data in the delta ball remain within eta for all real time under a static H+V. On zero Gauss there is a nonempty compact invariant minimizing set, stable as a set, within the largest nonnegative root of c r^3-beta r/2-nu=0. That root is <=eta/2; for purely centered errors it is sqrt(beta/(2c))<=eta/4. No unique perturbed stationary orbit, attraction or unchanged nominal stability is asserted.

Time-varying errors require the same uniform amplitude cap AND cumulative spatial-gradient variation integral<=nu_star through the requested horizon. Instantaneous smallness alone does not give a general all-time guarantee; an exact resonant oscillator within the abstract quartic-coercivity class demonstrates the gap.

## Typed coefficient and observation requirements

Let A=max|Delta a_e|, K=max|Delta kappa_d|/(rN), H_c=|xi_0| for a chosen real common hopping component, G_r=max|xi_e-xi_0|, and D_s the scalar site-detuning half-range. It suffices that

    14N*G_r + 3N*D_s + eta*(A + 12N*K + 24N*H_c) <= N*eta^3/12800.

Kinetic, diamond and common real hopping errors are centered at the critical orbit. Uniform site/mass shifts are free constants on the norm surface. Use the same formula on coefficient derivatives to bound the cumulative variation integrand; do not differentiate a reported bound envelope. The coefficient limits share one budget.

A positive uniform magnetic shift 0<t<=eta^2/153600 passes this contract while placing the exact nominal orbit above its frozen sharp stability boundary. Finite-radius trapping and stability of the nominal equilibrium are different conclusions. The full minimizing set is still within eta/4 in this example.

All 18 nominal complex loop readouts equal 1. State motion contributes <21eta per channel; adding instrument error sigma gives total<=21eta+sigma. Choose eta<=min(R_p,tau/42), sigma<=tau/2 for a complex readout target tau. Loop proximity alone does not certify full initial orbit distance or electric/matter preparation. No 26-branch endpoint classifier is supplied.

At a=N=1, eta=1/829538022≈1.20549e-9: nu_star≈1.36861e-31, pure centered Hessian cap≈1.13532e-22, pure K cap≈9.46098e-24. These conservative mathematical values are not measured physical tolerances.

## Replay

- Python 3 + SymPy: `python3 verify_endpoint_robustness.py` checks 24 exact algebraic conditions and five rational budget examples. The eight-page manuscript supplies the analytic transfer, set localization and coefficient proof.
- Standard-library calculator: `python3 endpoint_robustness_budget.py --a 1 --N 1`. Optional `--eta`, `--A`, `--K`, `--common-hopping`, `--residual-hopping`, `--detuning`, `--variation` are exact rational inputs. It returns exact energy quantities, initial-radius and cubic-root enclosures, and sufficient-budget status. Zero defaults are assumptions, not measurements. Out of budget is inconclusive.
- NumPy + SciPy + python-flint 0.9.0: `python3 check_endpoint_gradients.py` checks four NUMERICAL full-matrix synthetic fixtures at ranks 1,2,3,5, including the centered/generic gradient split and readouts. Gauss is not imposed because bounds hold on the larger fixed-norm surface. No empirical samples or trajectories are used.

Three copied frozen inputs are hash-bound in PROVENANCE_v0.1.json. The PET certificate and sharp boundary remain conditional dependencies, not new interval evidence or independent review. The nominal action and coefficient ledger are unchanged. Experimental use needs a source-selected realization and calibrated state/energy/time/detector maps. No sharp basin, infinite-rank flow, physical GUT proof or laboratory calibration is established.
