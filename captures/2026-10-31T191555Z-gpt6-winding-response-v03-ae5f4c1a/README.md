# UD PRED-01 + PRED-02 constructive development package v0.3

**Evidence:** EXACT_CONDITIONAL and NUMERICAL, development lane. **Physical promotion 0. Non-constructor review deferred.**

This package advances two authorized tasks: construct explicit finite `n=2` and `n=3` winding-sector **proxies** with a defined update/source receipt; and formalize the 27-state response preparation schedule, including minimal discriminants and full coverage.

## Contents

- `UD_PRED01_CONDITIONAL_K4_DECORATED_CARRIERS_v0.3.md` — formal object, exact cochain and homology calculation, three-edge source, update, gross/retained readout split, boundary and continuum no-go.
- `UD_PRED02_RESPONSE_PREPARATION_AND_MODEL_DESIGN_v0.3.md` — 27-class design, exact four/12/20/54 observation schedules, S3 quotient and typed measurement contract.
- `carrier_and_preparation.py` — source-code reproducible exact matrices and output enumerator.
- `test_carrier_and_preparation.py` — 35 unit checks, plus exact incidence and numeric relaxation checks.
- `RESULTS.json` — m=8 complete output (64 vertices, 128 edges, 80 faces, 16 tetrahedra), full ordered 54-class and 12-class schedules.
- `REFINEMENT_SWEEP.json` — m=4,6,8,12 comparison.
- `requirements.txt` — pinned SymPy and NumPy versions.
- `TEST_LOG.txt`, `MANIFEST.json` — verification results and SHA-256 provenance.

## Reproduction

```bash
python3 -m pip install -r requirements.txt
python3 carrier_and_preparation.py --m 8 --exact-ranks --seed 20261031 --out RESULTS_replay.json
python3 -m unittest discover -v
```

`RESULTS_replay.json` must be hash-identical to `RESULTS.json` under the pinned code and dependencies only if the formatter and invocation are unchanged. No random draws occur in the six-state or 54-state proofs beyond the deterministic shuffle seeded with `20261031`.

## Interpretive boundary

**This is not yet a UD-native n=3 carrier.** It uses an **assumed annular hole**, a unit-edge action and an imposed integer-valued lifted phase. The primitive origin of the annulus, a physical readout identifying retained versus gross action, a calibrated time unit, native phase-slip dynamics and full carrier persistence remain OPEN_GATED. All 27 response classes are formal (not necessarily physically preparable). None of the branch-local mathematical successes imply physical promotion.

The prior exact source is `UD_PREREGISTRATION_PACKET_v1.0.md`, read with `UD_PACKET_v1.1_ERRATA.md` and the external-review brief; this package does not overwrite those records. Governance v1.0 is separately proposed via UD PR #473, and review is deferred but not waived. The prior model-development PR is UD #475.
