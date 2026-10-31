# UD Prediction Development v0.2 - formal assumptions, not physical proof

**Lane:** D0 DEVELOPMENT / NO REGISTRY PROMOTION. **Physical promotion:** 0.
**Source strata:** UD preregistration packet v1.0 Part A/B with mandatory v1.1 errata E.1-E.3, UD external review brief. Non-constructor review intentionally deferred.

Files in this immutable research capture:
- PRED01 theorem and leakage addendum (exact conditional recurrence, parameter singularity and four-event necessary invariant).
- PRED02 formal class occupancy audit (iid expectation and deliberate 54-state sufficient schedule).
- pred01_pred02_replay.py (stdlib numerical/exact reproducibility; assumed formal carriers, no physical n=3 carrier).
- RESULTS_SUMMARY.json (source-bound examples plus 10,000 synthetic Monte Carlo draws with seed 20261031).
- MANIFEST.json and RECEIPT.json (SHA-256 and verification scope).

Run from this capture directory:
    python3 pred01_pred02_replay.py --out local_replay.json --draws 10000 --seed 20261031

Full local development package containing two full scripts, 15 unit tests and both full numerical JSON outputs was generated separately in this session. Its archive SHA-256 is 63124de8c21e68d1f6a059c6b849033b0875e3324c25b54260a71214aeb07bb4; it is not represented as checked-in GitHub bytes.

These mathematical tests do not establish physical event carriers, instrument behavior, energy units, nor independent review. Physical promotion remains 0.
