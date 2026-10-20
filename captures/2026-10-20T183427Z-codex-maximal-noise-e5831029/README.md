# Largest admissible encoded noise: actual estimator validation

Capture `2026-10-20T183427Z-codex-maximal-noise-e5831029` extends PR #269 from base `0e4d6f6e6d3c0403241a551265439657d5a5b151`.

Both frozen cases passed the original 14 numerical gates after one unchanged estimator call each. There were two calls, zero retries and zero replacements. The independent output audit also passed its prospectively strengthened error-enclosure checks. A separate zero-fit replay reproduced both certificates and exact matrix witnesses byte for byte.

## Exact input theorem

For integer noise e=qk with q=2^-48, the unchanged radius δ0=3*2^-49 is (3/2)q. Membership is equivalent to ∑k_j²≤9/4. Since the sum is integer, it is at most 2. Thus every active coordinate is ±1 and at most two coordinates are active. The complete pointwise alphabet contains

`1 + 2·62 + 4·binom(62,2) = 7,689`

vectors. Its maximum encoded norm is √2q, with squared-radius ratio 8/9. This lies strictly inside the continuous ball; the lattice does not attain the radius itself. A single 2q coordinate or three unit coordinates is excluded. An independent sparse enumeration and a separate root generating-function count agree. The full proof is in `input_review/LATTICE_THEOREM.md`.

The two records attain this largest encoded amplitude in every observation vector, with different block and rotating-channel structures. They are two deterministic histories, not an enumeration of the `7689^303067` possible pointwise assignments. The input theorem does not establish universal estimator or backend success.

## Actual outputs

| Case | Independently recounted rank | Lag operator upper | LS distance upper | Finite phase-error upper |
|---|---:|---:|---:|---:|
| boundary_pair_block | 209 | 3.794759617E-11 | 3.018852023E-14 | 2.918469639E-14 |
| boundary_pair_rotating | 209 | 4.284849322E-11 | 3.007994298E-14 | 1.959605171E-14 |

The displayed bounds are rounded upward from their exact rational certificates; DISPLAY_BOUNDS.json retains the comparison. Phase errors are radians per TWOstep, modulo 2π. The lag cap remains 2^-34. The LS column is a posterior upper bound, with no new LS acceptance cutoff. Conditional source-theorem envelopes are separately reported in RESULT.json and are distinct from the direct finite phase-match errors.

Recipes, order, code, caps, sole Gram-Frobenius lag route, and independent audit code were frozen before fitting. Both complete input audits and record hashes were bound before the first fit release. The unchanged producer estimator learned its order; the exact verifier independently counted all 321 saved singular values against 2^-24 and excludes equality. Acceptance uses the original source ball, with no retrospective tightening to the actual encoded amplitude.

Independent input checks covered 37,580,308 scalar differences, 606,134 vector norms, and 5,258,622 projection entries. The separated nominal-plus-perturbation projection matched the producer’s direct raw projection. The independent output audit checked 262,086 exact matrix entries and 418 phase matches and encodings, alongside the retained equation, Gram defects, lag and LS bounds, complex residuals, original conditional theorem and phase disks.

The new audit checks were frozen before fitting: advertised inverse and eigenpair residual metrics must enclose the independently computed exact squared residuals; the inverse norm must enclose the independent bound; all 418 actual circular argument errors must satisfy validated comparison against their advertised bounds, without rounding tolerance or fallback. Underreporting and indeterminate comparisons are rejected. The producer caps and earlier campaign verdicts are unchanged.

## Recovery and repeat verification

Workspace maintenance had removed the nominal raw. `baseline_recovery/` contains the reviewed standalone PR195 formula recovery, source pins, a fresh recovery receipt and independent full scalar-range/hash postcheck. Only the reference NPZ was read as archive data; archived Python was not executed. The recovered baseline has SHA-256 `25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59` and 150,321,232 bytes.

Under the frozen omission protocol, the two temporary raw files were removed only after all audits and replay. Their hashes and deterministic recovery route remain in `root/RAW_DISPOSITION.json`. Complete actual factors and proof matrices are retained once per case. The recovered baseline was unchanged. No full 287-GiB Hankel matrix was allocated; component timings do not constitute a native end-to-end Hankel benchmark.

To repeat saved-output verification, restore the exact baseline in a new external workspace. Set UD_REPO to the immutable repository. With the relevant case directory first on sys.path, import its records.py and call records.make(baseline,new_external_raw). Require the DATA_FREEZE.json hash or remain HOLD. Then run:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python <case>/certify.py --repo /absolute/UD --raw /absolute/recovered_raw --out /absolute/new_output
```

Compare CERTIFICATE.json and EXACT_MATRIX_WITNESS.json.gz to the primary bytes. Do not rerun the captured fit drivers or reuse intent files. Root wrappers preserve historical invocation paths; the explicit-path case verifier is the repeat-check entry point. Versions are in `root/ENVIRONMENT.json`; cross-version identity is not assumed.

## Correction and limits

One pre-fit aggregate-review parser initially refused the control-receipt schema. The corrected parser read both original frozen control lists and required all 27 checks to pass. Both source versions and its correction receipt are retained. No formula, input, numerical cap, estimator run, or scientific rule changed.

These are source-aware computational perturbations of the same exposed model, preparations and phase targets. Source H, full-factor, frame and target proofs remain inherited and hash-bound. No blinded or independent physical acquisition, new held-out preparations, whole-trajectory/backend guarantee, exact spectrum(T), unaliased primitive frequency, SI or physical six-ratio 2^-39 gate, or native 1893/747 recovery follows. New-case full reconstruction and sigma210 lower bound are NOT_EVALUATED. Older HOLD/NO-GO results remain unchanged. The previous 128-path unresolved/UNSENT status is an inherited snapshot; no new evidence-return search or outreach occurred.

Unavailable and unused: Gap2_FINAL_Finite_Genesis.png; Notes Backup 17-04-2026 07-13.txt; ASTER_Project_Folder_Instruction_Block_v1.md. Supplied ledger v0.39 and CRL-2 subdivision bytes are retained. Development — no registry entry. Tolerances and recipe integers are O03 protocol controls. Same-team independent implementation review does not substitute for external promotion review. External promotion review PENDING; Physical Promotion=0.

Publication, CI, merge and tracking receipts are reported only after they complete. This capture makes no advance assertion that a merge, public-site or Project-board update succeeded.
