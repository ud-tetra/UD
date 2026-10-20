# Three noise cases: actual floating estimator validation

Capture `2026-10-20T133845Z-codex-three-noise-f72a62fa` extends PR #267 from base `0dc7dd79f565063ff198f3cade3e0548b8577c52`.

All three fixed cases passed the 14 frozen numerical gates after one unchanged estimator call each. The independent implementation audit agreed, and a separate zero-fit replay reproduced each certificate and exact matrix witness byte for byte. There were three estimator calls, zero retries, and zero replacement cases.

| Case | Saved rank | Lag operator upper | LS distance upper | Maximum finite phase error |
|---|---:|---:|---:|---:|
| block257_port17 | 209 | 3.723157435e-11 | 3.117947341e-14 | 6.879591539e-15 |
| affine62_qr13 | 209 | 4.000914921e-11 | 3.222029945e-14 | 5.052130079e-15 |
| prep_port_period7 | 209 | 4.364451973e-11 | 3.095727658e-14 | 1.121386749e-14 |

Phase errors are radians per two-step transition, modulo 2π. The lag cap is 2^-34. The LS column is a certified posterior upper bound, with no additional LS acceptance cutoff. Conditional source-theorem phase envelopes are reported separately in RESULT.json; they are not the much smaller direct finite phase-match errors.

Each case changes exactly one scalar by one 2^-48 quantum in every 62-channel vector. Each record contains 18,790,154 readings and 303,067 changed scalars. The squared noise-radius ratio is 4/9 of the fixed ball with radius 3*2^-49. The three formulas use different channel and temporal structures. Their integers and tolerances are O03 protocol controls.

The case list, formulas, order, source hashes, original caps, sole Gram-Frobenius lag route, and independent audit code were frozen before fitting. All three input audits and record digests were bound before the first fit release. The unchanged estimator learned its order; the exact verifier independently counted all 321 saved singular values against 2^-24 and excludes equality. The complete actual output tuple is retained once per case.

The input audit checked 56,370,462 scalar differences, 909,201 vector norms and 7,887,933 projection entries. Its separate nominal-plus-perturbation projection agreed with the producer’s direct raw projection. The independent output audit compared 393,129 exact matrix entries and checked 627 phase matches and encodings. Original source premises, the measured singular floor, both Gram defects, retained equation, lag bound, finite LS bound, complex inverse and eigenpair residuals, argument bounds, and phase disks remain explicit.

## Saved evidence and recovery

The scratch runtime had reset. `baseline_recovery/` contains a reviewed standalone reconstruction of the PR195 formulas, source pins, a static scope review, formula byte-identity checks, and the recovery receipt. Only the reference NPZ member was read from its archive as data; archived code was not executed. The recovered baseline exactly matches SHA-256 `25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59` and size 150,321,232 bytes.

Under the frozen omission protocol, the three temporary raw files were removed only after all input and output audits and root replay. `root/RAW_DISPOSITION.json` records their exact hashes and recovery method. The recovered baseline was unchanged. The actual floating factors, complete lossless matrix witnesses, certificates, independent audits, source freezes, invocation receipts, and separate resource measurements are retained. No full 287-GiB Hankel matrix was allocated. These component timings do not constitute a native full-pipeline Hankel benchmark.

For repeat verification in a new external workspace: check the recovery freeze, reconstruct the baseline with `baseline_recovery/recover_baseline.py`, and require the exact baseline hash. Set `UD_REPO` to the immutable repository. With the relevant case directory first on `sys.path`, import its `records.py` and call `records.make(baseline, new_external_raw)`. Require the raw hash in that case’s DATA_FREEZE.json. Then run:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python <case>/certify.py --repo /absolute/UD --raw /absolute/recovered_raw --out /absolute/new_output
```

The certificate and exact matrix witness must match the saved primary bytes. A mismatch remains HOLD. Do not rerun the captured fit drivers or reuse their intent files. Root wrappers preserve historical absolute invocation paths; the explicit-path case verifier is the repeat-check entry point. Versions are recorded in `root/ENVIRONMENT.json`. Cross-version numerical identity is not assumed.

## Scope and corrections

These are deterministic computational perturbations of the same exposed model, preparations, and phase targets. They do not establish blinded validation, new held-out preparations, independent physical acquisition, a stochastic population result, universal backend or whole-ball success, exact spectrum(T), unaliased primitive frequencies, SI calibration, the physical six-ratio 2^-39 gate, or native 1893/747-dimensional recovery. New-case full reconstruction and a sigma210 lower bound are NOT_EVALUATED. Source H, full-factor, frame, and target proofs remain inherited and hash-bound. Older HOLD and NO-GO results are unchanged.

One boundary-control setup initially refused because an expected script path was absent. The identical already-frozen script was copied to that path before any raw generation or fit, and all boundary controls then passed. The custody note retains this correction. An independent hand-expected period-7 control sign was corrected before its freeze without changing the formula. Neither correction retried a fit or changed a scientific gate.

The earlier 128-path unresolved/UNSENT evidence status is an inherited snapshot. This campaign performed no new evidence-return search or outreach. Gap2_FINAL_Finite_Genesis.png remained unavailable and was unused.

Development — no registry entry. Supplied coefficient ledger v0.39 and CRL-2 subdivision bytes are retained. Same-team independent implementation review does not substitute for external promotion review. External promotion review is PENDING; Physical Promotion=0.

Publication, CI, merge, and tracking receipts are reported after they occur. This immutable capture makes no advance assertion that a future merge or site update succeeded.
