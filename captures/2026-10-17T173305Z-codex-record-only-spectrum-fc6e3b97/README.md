# Record-only spectral extraction — PASS

**Development — no registry entry. Constructor checked; independent review pending; physical promotion 0.**

The verifier now certifies the frozen record using learned phases and a complete finite-record residual, without loading the nominal operator or its modal data. The exact gate is `9093197064441289377 / 604462909807314587353088`; exact outward dyadic bounds are in `RESULT.json` and `certified/CERTIFICATE.json`.

| Result | Verified bound or measurement |
|---|---:|
| Readings checked | 18,790,154 |
| Temporal components learned | 105 |
| Singular values above frozen threshold | 1,893 |
| Retained condition | <706.570 |
| Complete projection tail, Frobenius | <1.132×10^-12 |
| Record-only proposal time | 1.13 seconds |
| Verification time | 112.87 seconds |
| Verification peak RSS | 2,088,816 KiB (1.99206 GiB) |
| Dense Hankel allocation | none; 286.75 GiB avoided |

The bounded one-reading edit `u=2^-20` preserves the numeric signature. The strong edit `u=1` provably forces at least **2203** values above threshold and is rejected. These controls scan complete modified records; they do not rerun the learner. Conditional on the frozen total operator-error ceiling, the retained condition remains **<754.162**; acquisition receipts are still required to apply that premise.

The lossy-model distinction is explicit: the replay codec stores every integer deviation from its learned dictionary. Restoring all 150,321,232 input bytes reproduces SHA-256 `812ede167804a754f1e7343cc370cdc72a231d3f255a8656080e5cc7a2753ff7`.

## Reproduce

Install `requirements.txt`, then run `python replay.py NEW_DIRECTORY --controls`. The directory must not exist. This restores the lossless input, runs a fresh record-only proposal, certifies the complete record, computes conditional robustness, runs regression checks and optionally builds both full-size controls. For your own complete frozen-format record, use `--record PATH`. The tool can HOLD; it does not adapt the acceptance threshold or target rank.

No independent blind execution, apparatus validation or continuous-generator identification is claimed. The numerical proposer may HOLD on valid noisy records; successful proposal generation throughout the acquisition family remains open. The original generic dense-candidate adapter is a separate, unbenchmarked path.

See [theorems and scope](RECORD_ONLY_THEOREMS.md), [provenance](PROVENANCE.json), [guard correction](RETRACTIONS.json) and [test results](TEST_RESULTS.json).
