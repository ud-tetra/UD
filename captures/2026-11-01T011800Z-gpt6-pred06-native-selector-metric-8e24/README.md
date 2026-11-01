# UD PRED06 proof-first native selector and action audit — v1.0

**Date:** 2026-10-31. **Status:** D0 mathematical research; six scoped proof milestones, external review DEFERRED, physical promotion 0.

The source-bound audit does **not** claim that a unique native defect source, absolute action normalization, integer winding lift or physical apparatus has been derived. It records what is mathematically implied and what is independent additional structure.

## Primary materials

- `UD_PRED06_SOURCE_BOUNDARY_AND_ACTION_AUDIT_v1.0.md` — consolidated conclusions, source/claim typing and next proof obligations.
- `UD-PM-PRED06-SEL-001_v1.0.md` — permutation-symmetric native selector NO-GO and diffusion-only nonselection.
- `UD-PM-PRED06-SEL-002_v1.0.md` — exact conditional local burden/flux comparator lemma.
- `UD-PM-PRED06-PAR-003_v1.0.md` — finite parity cannot additively yield unrestricted integer winding.
- `UD-PM-PRED06-FIX-004_v1.0.md` — fixed incidence cannot alter carrier homology.
- `UD-PM-PRED06-ACT-005_v1.0.md` — curvature/Hodge-only action cannot split flat winding sectors.
- `UD-PM-PRED06-MET-006_v1.0.md` — uniformly elliptic metric logarithmic obstruction; stiffness/metric scale ambiguity.
- `independent_proof_checks.py`, `test_proof_checks.py`, `EXACT_AUDIT.json`, `EXACT_AUDIT_LOG.txt`, `TEST_LOG.txt` — exact symbolic and enumerative verification.
- `ledger/` — append-only typed proof status JSON entries; `CLAIM_LEDGER.json` and `SOURCE_REGISTER.json` retain source boundary.
- `MANIFEST.json`, `RECEIPT.json` — SHA-256 records (manifest excludes itself and the separately versioned GitHub event).

## Reproduce

```bash
python3 -m pip install 'sympy==1.14.0'
python3 independent_proof_checks.py
python3 -m unittest discover -s . -p test_proof_checks.py -v
```

No web, simulated measurement or physical clock is used. Hardware performance, scientific truth of candidate assumptions, and any actual physical bridge are **not** verified by these tests. This package complements open UD PR #487 and preserves its original hypotheses and content.
