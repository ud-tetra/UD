# UD PRED-01/PRED-02 Native-Selection Development v0.4

**Status:** D0 DEVELOPMENT / EXACT_CONDITIONAL + NUMERICAL. **Physical promotion:** 0. **Non-constructor review:** deliberately deferred, not waived. **Date:** 2026-10-31.

**Goal:** Replace v0.3's *pre-inserted annulus* with a model in which a local defect-excision rule changes K4 packet topology, and lift PRED-02's 27 abstract classes to explicit raw edge-control states with separately typed readouts.

## Principal results

- **PRED-01:** Initial space is a tetrahedralized three-ball (\(H_1=0\)). A boundary-seeded, conserved local marker propagates along two vertical edges; an explicitly assumed star-excision/pruning rule makes \(H_1\cong\mathbb Z\). Exact topology is verified over \(\mathbb Z\) by annulus-times-interval deformation retraction, and over \(\mathbb F_2\) by finite incidence ranks at three refinements. No K4-native asymmetry or physical defect-trigger has yet been derived.
- **PRED-01:** An integer cohomology cocycle and harmonic lift support formal \(n=2\) and \(n=3\) sector minima. A vertex-neighbor local diffusion solver converges numerically to the harmonic representative. With *chosen* size-dependent energy normalization, distributed one-edge-at-a-time injection and temporary curvature, total positive action input obeys \(W^+\le 41/5\) uniformly in grid size under the stated bounded-incidence assumptions. This opens a different source branch; it does not refute the prior fixed-three-edge no-go. Algorithmic event count rises with resolution; not a physical duration.
- **PRED-02:** A proposed 12-bit raw interface defines two edge-integrity/support flags per pair. Exactly 9, 4 and 3 of the 16 pair configurations map respectively to (0,0), (0,1) and (1,1). The three-pair interface has 4,096 raw configurations mapping onto all 27 formal classes.
- **PRED-02:** Under iid uniform raw-bit sampling the expected number of class-pair replays among 24 observations is \(10272513/524288\approx19.59\); a shell-2 miss still has approximately 11.65% probability. A fully generated three-pass 81-event Boolean schedule separates exact-raw replay from within-class microstate challenges. A class replay mismatch cannot by itself establish temporal memory.

## Files and reproduction

- `UD_PRED01_LOCAL_DEFECT_SELECTION_AND_BOUNDED_SOURCE_v0.4.md` — definitions, proofs, source receipts, no-go scope, numerical table and open gates.
- `UD_PRED02_RAW_STATE_REALIZATION_AND_DUAL_CONTROL_v0.4.md` — Boolean source-compatible lift, sensor distinctions, 81-event protocol and error controls.
- `native_defect_and_readout.py` — deterministic construction, GF(2) chain audit, integer seam, local solver, local source receipts and full 81-event schedule.
- `test_native_defect_and_readout.py` — **25** tests.
- `independent_audit.py` — separate planar Euler and 4-bit raw-enumeration implementation.
- `RESULTS.json`, `INDEPENDENT_AUDIT.json`, `TEST_LOG.txt` — reproducible finite outputs.
- `QUALIFICATION_MATRIX.json`, `BRIDGE_CONTRACT.json`, `CLAIM_LEDGER.json`, `MANIFEST.json` — typed audit and proof/physical boundaries.

Run in Python 3.11+ after installing `requirements.txt`:

```bash
python native_defect_and_readout.py --out RESULTS.json
python independent_audit.py
python -m unittest discover -v
```

The output is a mathematical candidate and digital emulation interface only. The unique positive-burden/parity seed, distinguished transport port, dynamic K4-pruning rule, persistent defect, phase lift, physical action units, laboratory apparatus, leakage custody and independent experiment remain **OPEN_GATED**. The integer winding is not observable from its U(1) Wilson loop alone.

## Source/version governance

This package adds new development results and does not overwrite UD v2.40 derived statements, packet preregistration v1.0, mandatory packet errata v1.1, or the accepted v0.3 independent research package. Read those exact sources and status scopes before any claim transfer. Program-wide predictive governance is in UD PR #473 (proposed), and v0.3 carrier/preparation construction is in UD PR #477 (proposed). **No physics promotion.**
