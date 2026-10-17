# Fixed-sketch blind-record audit

Development — no registry entry. Constructor verification only. Independent
review not established; physical promotion 0. This work advances issue #178
without claiming independent data, full acquisition qualification or convergence
for every bounded perturbation.

The frozen 160-column sketch has an exact 2134-dimensional nullspace in its
2294-dimensional preparation/channel input. A concrete integer witness defines
record perturbations whose exact sketches vanish. The new bounded impulse
record nevertheless has **algebraic Hankel rank at least 30,875**. Its full
verifier still certifies **exactly 1893 singular values above the frozen
threshold**. This makes the rank/threshold distinction concrete on a much
larger exact lower bound than the earlier scalar impulse example.

See `THEOREMS.md` for the proof and `EXACT_BLIND_FAMILY_CERTIFICATE.json` for
the integer witness checks, exact minors and rational gap. The rank lower bound
uses a pinned inherited baseline approximation certificate; it does not claim
the baseline's exact rank is 1893 or prove the noisy exact rank increased.

## Execution contract

Three constructed cases were fixed before generation on an already known
synthetic baseline: bounded impulse, bounded alternating clock and an oversized
alternating control. Their additions are exactly invisible to the mathematical
sketch. The original proposer and full verifier are unchanged and hash-frozen.
Each case gets one proposal and one full certificate attempt; HOLDs are kept.
Floating sketches need not agree bit-for-bit despite exact cancellation.

The first two cases satisfy both the sufficient scalar additive ceiling2^-23
and global62-vector ceiling2^-20. This is not the complete acquisition contract.
The third deliberately violates both. All three discover105 temporal components;
discovery order alone is therefore inadequate for certifying the full record.

`CAMPAIGN_RESULTS.json` preserves final pass/HOLD decisions and exact certificates
are in `results/certificate-*`. A HOLD refuses the proposed certificate; it is
not alone proof that the true record's signature fails or that a physical
mechanism caused a failure. The sketch nullspace is unrelated to the nominal
observer's747-dimensional dynamical kernel, which remains unobserved.

## Reproduction

Use Python3.12 and the pinned requirements. Supply the exact clean baseline raw
record with SHA256812ede167804a754f1e7343cc370cdc72a231d3f255a8656080e5cc7a2753ff7
at the generator's documented baseline path. It can be recovered through the
lossless finite-history codec in the source record-only capture. The full
baseline source is
`captures/2026-10-17T173305Z-codex-record-only-spectrum-fc6e3b97` in
https://github.com/ud-tetra/UD/tree/4b4e78f796132c2843444aa024d0471af38c7054 .

1. `python certify_blind_family.py` checks the exact witness and inherited-tail
   implication without requiring the raw record or running the spectral solver.
2. `python test_exact_witness.py` runs a clean isolated replay and three hostile
   input cases, including an altered vector with a renewed hash.
3. In a fresh copy without `records` or previous `results`, run
   `python make_records.py` then `OPENBLAS_NUM_THREADS=1 python run_campaign.py`.
4. `python validate_campaign.py` compares every encoded reading to its exact
   recipe, binds all record/proposal/contract hashes, checks unchanged code and
   verifies pass/HOLD scope without modifying the frozen threshold.

The raw450,963,696 bytes and regenerable large factor-Gram arrays are omitted
from the compact package. Their sizes/hashes are recorded in `OMITTED_DATA.json`.
Proposals, compact factor arrays, certificates, logs, witness, recipes and source
bindings are retained. Fresh full replays recreate the arrays; saved execution
receipts are not a substitute for an independent replay or endorsement.

## Remaining work

Independent records and attributable review remain open, as do broader fitting
convergence, calibrated timing/preparation/disturbance, native observer
selection and physical interpretation. This finite campaign does not close
issue #178, #144, #136, #130 or the review HOLD in #177.

## Fresh execution results

| Constructed record | Discovery order | Full decision | Retained condition upper | Complete tail upper |
|---|---:|---|---:|---:|
| bounded_null_impulse | 105 | CERTIFIED_NUMERIC_RECORD_SIGNATURE | 706.634521 | 1.094415131e-08 |
| bounded_null_alternating | 105 | CERTIFIED_NUMERIC_RECORD_SIGNATURE | 710.509243 | 6.608411417e-07 |
| strong_null_alternating | 105 | HOLD | not certified | 2.165444770e-02 |

The two accepted records each certify1893 values above the unchanged threshold. The strong control is out of budget; its HOLD does not decide the true spectral count. All56,370,462 scalar readings were checked in the three fresh proof attempts. Sequential proposal-plus-proof wall time: 338.62 seconds; maximum worker RSS 2091424 KiB. Dense Hankel storage was not allocated. These are machine/schedule-specific measurements.
