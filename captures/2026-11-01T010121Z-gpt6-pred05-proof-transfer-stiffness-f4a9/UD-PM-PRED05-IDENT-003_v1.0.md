# UD-PM-PRED05-IDENT-003 v1.0 — Static geometry does not determine action amplitude

**Kind:** NO_GO (exact and scoped).  
**Proof status:** VERIFIED_SCOPED / EXACT_CONDITIONAL.  
**Review:** DEFERRED. **Physical promotion:** 0.  
**Sources:** UD PR #479 action model §4, source-bound stiffness analysis PRED05-SCALE-002, supplied UD coefficient provenance ledger v0.39 (G05, Q13, O03) dated 2026-08-22.

## Statement and hypotheses

Consider a connected finite punctured complex \(K\) with a fixed unweighted cochain metric and fixed integral winding generator. Let \(h\) be the unique real harmonic cochain with period 1. Suppose only the following are supplied: simplicial incidences, cohomology and the *static minimizer* within each period sector of a model family
\[
\mathcal A_{\lambda,\rho}(a)=\frac\lambda2\|a\|^2+\frac{\rho\lambda}{2}\|da\|^2,
\quad \lambda>0,\quad\rho\ge0\text{ fixed}.
\]
No independently normalized action measurement, time generator or micro-to-cochain coupling is assumed.

**NO-GO:** These data do not determine \(\lambda\). In fact an entire positive continuum of distinct action amplitudes is compatible with exactly the same incidences, homology, harmonic representatives and static minimizers.

## Proof

For each \(c>0\), replacing \(\lambda\) by \(c\lambda\) multiplies the full action by \(c\), without changing the argmin of the action in any fixed class. Its vanishing-gradient equation and stationary configuration set are unchanged; the topology and the unit-period harmonic representative are properties of the fixed complex and metric, not of \(\lambda\). Yet the retained gap \(\Delta=\frac52\lambda\|h\|^2\) for \(n=2\to3\) changes to \(c\Delta\). Hence the listed geometric/static observations cannot identify \(\lambda\). QED.

## Limits

This no-go does **not** claim that native UD dynamics can never determine an action scale. A physical clock and rate law, microscopic amplitude, source current, calibrated energy measurement, or an independently normalized action map could break the amplitude freedom. The proof does not cover a kinetic generator with independently specified physical time and measured relaxation rates: multiplying its action could then change experimentally observable rates. It proves only that topology and equilibrium representatives alone cannot recover the stiffness coefficient.

In the source ledger, numerical equality of distinct \(\lambda\)-named objects does not supply the required map. Selecting \(\lambda_N=2/(5\|h_N\|^2)\) is an inverse problem, not an independent derivation. Together with PRED05-SCALE-002 this pins down what a true micro-to-action bridge must provide: an absolute dimensioned coupling and its resolution law, not merely a normalized stable winding configuration.

**Disposition:** EXACT_CONDITIONAL NO_GO within the stated static data class; physical promotion 0; non-constructor review deferred.
