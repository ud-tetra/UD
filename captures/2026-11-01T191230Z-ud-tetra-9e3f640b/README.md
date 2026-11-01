# UD Signed Reference Observer Gate v0.1

**Date:** 2026-11-01 · **Physical promotion: 0** · **Independent review: pending**.

Target: the user's authorized Option 1, to test Q81-Q84/O09 for a source-selected sign-sensitive first-harmonic reference that could complete the K4 quadratic stock observer and explain whether a cardioid can be selected without fitted gain.

## Result

- **EXACT / CONDITIONAL:** Any prepared nonzero initial K4 edge state `r` plus its Hodge quadrature `Ar/2` gives a sign-sensitive reference phase `u_r(s)=exp(2is)`; the accepted Q165/Q166 quadratic stock/current observer yields `W(s)=u_r(s)^2=exp(4is)`.
- **EXACT:** The reference is compatible with all 24 signed S4 relabelings *only when it co-transforms with the state*.
- **EXACT / CONDITIONAL:** Q81 supplies a relative context phasor; Q84 its signed cosine. Its link to `u_r` and the apparatus source remain open.
- **NO-GO / SCOPED:** One signed cosine plus even W fails global injectivity at `theta=pi/2,3pi/2`; Q83 half-angle modulo pi has an independent Z2 lift gate; Q82 orientation sign does not supply a quadrature.
- **NO-GO / SCOPED:** Neither Q81-Q84 nor O09 fixes the observer gain that makes the cardioid cusp: `Z_lambda=lambda u-u^2` has a stationary point iff `lambda=2>0`.
- **EXACT / DISTINCT CANDIDATE:** No S4-invariant *linear* edge scalar exists, but source-free *cubic* odd invariant polynomials exist mathematically and generate first+third harmonics. Such cubic observations are not source-selected by Q165/Q166.

## Reproduce

`python exact_reference_gate.py` — exact rational/symbolic source math and representation tests.

`python independent_reference_replay.py` — independently assembled 15D skew Hodge evolution, 8192 time samples, reference covariance, monomial-action invariant count, cusp checks.

`TECHNICAL_NOTE.md` — complete definitions, proofs, source register, no-go and reopened gates.

`PROOF.pdf` — A4 typeset mathematical summary.

`MANIFEST.json` — SHA-256 hashes, validation and provenance. `CLAIM_DEPENDENCY_LEDGER.csv` — status for each consequential claim.

This package does not identify real photons, laboratory apparatus, physical time, or a measured numerical dressing correction. Physical promotion remains zero.
