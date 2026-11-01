# UD Native Quadratic Observer Gate v0.1

**Date:** 2026-11-01  
**Status:** `EXACT_SCOPED_SOURCE_STOCK_AND_CURRENT` / `DERIVED_CONDITIONAL_TWO_CHANNEL_PACKAGING` / `NO_GO_EVEN_CARDIOID_AND_O09_ABSOLUTE_REFERENCE` / `PHYSICAL_PROMOTION_0`.

## Main result

The recovered UD v0.85 ledger Q165/Q166/Q169/Q170 specifies a native quadratic stock observable and signed support currents. For a filled tetrahedron, unit simplex basis, and any nonzero edge-only preparation `x`:

- Native flow: `X(s)=exp(s A) x`, `A=B.T-B`, native angular frequency 2.
- Exact native edge-degree stock: `S1=q*cos(2s)^2=q*(1+cos(4s))/2` where `q=||x||^2`.
- Exact normalized stock-plus-flux circle: `W=(2 S1/q - 1)+i*(J12-J01)/(2 q)=exp(4 i s)`.
- `W(s+pi/2)=W(s)`, while `X(s+pi/2)=-X(s)`; even quadratic channels cannot generate the first harmonic needed for `2u-u^2`.
- Recovered O09 stores modal phase increments and amplitudes, not a selected absolute phase reference or instrument. **It does not select the cardioid observer.**

This is **mathematical nonlinear observation already available from the source rules**, not a physical detector or proof of measured spectral anomalies. The complex packaging is a declared diagnostic convention; its normalization is algebraic, not experimentally tuned.

## Reproduce

```bash
python3 exact_source_observer.py
python3 independent_numeric.py
python3 coherence_kernel_audit.py
python3 verify_release.py
```

Requirements: Python 3, SymPy, NumPy. The scripts write/verify JSON receipts adjacent to themselves. `verify_release.py` verifies the frozen byte manifest. The full 2-page A4 typeset `PROOF.pdf` is included; LaTeX source is `PROOF.tex`.

## Sources / limits

- [UD mathematical results, Paper I §4.3](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/mathematics/)
- [Recovered coefficient ledger v0.85](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/evidence/ledger-recovery/) (inherited scientific revision v0.43), Q165, Q166, Q169, Q170, Q76–Q79, Q84 and O09.
- Historical ledger v0.39 and source bounds retained separately.
- Previous candidate cardioid observer: [GitHub PR #498](https://github.com/ud-tetra/UD/pull/498).

**Missing for physical promotion:** source-selected phase reference, optical apparatus/readout, physical clock, detector transfer/covariance, held-out empirical test and independent non-constructor review. No laboratory correction or redshift law is claimed. **Physical promotion = 0.**
