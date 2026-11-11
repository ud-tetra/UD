# THM-534 v1.0 Constructor Execution / Falsification Receipt

**Date:** 2026-10-21 | **Review:** constructor only; non-constructor PENDING | **Lane:** development | **Physical promotion:** 0.

**Main manuscript:** [THM534_SUPPORT_READINESS_GATE_v1.0.md](THM534_SUPPORT_READINESS_GATE_v1.0.md).  **Claim delta:** [v1.0 ledger](THM534_SUPPORT_GATE_CLAIM_LEDGER_DELTA_v1.0.md).

## Exact executed source
- `verify_thm534_support_gate_v1_0.py` — SymPy exact 4×4 Schur-Cayley solve with unit signed incidence and Q167/Candidate gate. PASS: all 64 hard masks, 24 signed S4 relabelings, 8 exact state-selected updates, Q167 visible/latent support switch accounting, Q162 + passive vertex/reservoir stock accounting, oriented face-closure, all-off absorption. Source SHA-256 recorded in release manifest.
- `verify_thm534_support_gate_fraction_v1_0.py` — independently coded standard-library Fraction Gaussian elimination, no SymPy; PASS: same exact eight masks, support squared norm 55, burden-plus-reservoir sum 4, all-off obstruction and nonzero redistribution. Same constructor, **NOT** non-constructor review.

## Complete actual eight-mask witness
Edge order: 01,02,03,12,13,23. Initial support x0=(-3,-4,-1,-2), y0=(-3,1,-2,-1,-3,1). Initial rho0=(1,0,0,0), r0=(1,1,1,0). Fixed dimensionless update ε=1/4. Prospective readiness q_e=(B1.T x)_e y_e; **candidate** gate h_e=1[q_e>0]. Mask sequence:

```
n=0  110000  q02>0
n=1  110000  q02>0
n=2  110000  q02>0
n=3  101000  q02<0   (closed)
n=4  001000  q02<0
n=5  011000  q02>0   (reopened)
n=6  011000  q02>0
n=7  001000  q02<0   (closed again)
```

Every event conserved **two typed invariants** separately: ||x||²+||y||²=55 and sum(rho+r)=4. All 8 finite events had nonzero burden face-circulation readout but this does **not** bypass the exact v0.9 dissipative no-persistence theorem. The hard gate's sign selection and tie remain candidate constitutive rules; no χ_geom or β reset was derived.

## Recorded constructor corrections
1. Initial attempt used `int(sympy BooleanTrue)`, which Python rejects; changed to `int(bool(...))`. Same as historical v0.9 code conversion issue; no model parameter change.
2. All-off absorbing control initially used ascending vertex values while the sign rule demands descending values for unit-positive y. Repaired test fixture from (0,1,2,3) to (3,2,1,0); mathematical theorem unchanged, source diagnostic recorded.
3. Independent second Fraction solver and every proof control passed afterward. No prior mathematical result was overwritten, and no non-constructor reviewer has yet checked the amended source code.

## Objective status
**PASS_SCOPED:** autonomous *transport-integrity* gate opening, closing and reopening with exact support/stock receipts under a named candidate rule. **NO-GO:** all-off recovery without a prospective/neighbor/memory source; masked-only Q167 flux cannot reopen; passive reservoir circulation decays. **OPEN_GATED:** native geometric closure χ and boundary b transition, transport integrity selection, action normalization, mode coupling, physical time/energy, genuine persistent phase holonomy and historical THM-534 stochastic probabilities.

## Reproducibility
Local package `THM534_SUPPORT_GATE_v1.0_RELEASE.zip` includes the **executed** SymPy/stdlib files, exact result JSON, main theorem, claim delta, this receipt, manifest with SHA-256, and runtime versions. GitHub published code must be explicitly checked for byte identity before describing it as an executed replica; source read-back alone is not a computational replay. Independent review required before CRL promotion.