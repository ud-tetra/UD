# Saved emitted phases, exact transition spectrum, and separate circuit component contract

Development — no registry entry; external non-constructor review PENDING; Physical Promotion=0.

All four saved PR240 outputs (directional amplitudes0,1,2,4) pass finite emitted-phase qualification. Each209-angle list is bijective to the unchanged two-step model targets. Across836 angles the certified maximum circular error is **<2.821e-14 radians per two-step sample**. All unchanged saved inverse/eigenpair/argument gates and exact ties-even encodings pass. No estimator, SVD, inverse or alignment proposal is rerun. Prior strict-frame0/1PASS and2/4FAIL verdicts remain unchanged. Thus these finite frame failures do not imply inaccurate emitted phases; no uniform noise-ball success is inferred.

A separate, disclosed post-known-outcome algebraic extension encloses the eigenphases of each exact saved dyadic transition T, rather than only its emitted list. Verified inverse and eigenpair residuals imply V^-1 T V=Lambda+F with ||F||<=e*h/(1-rho). Exact pairwise center separation proves one simple eigenvalue per disjoint disk. The disk modulus margin gives the angular bound asin(R/m). Adding the independently certified center-to-emission and emission-to-source errors proves **<9.413e-12 radians per two-step sample** for all four exact T spectra, with the same unique209-target assignments. This is a finite exact-saved-matrix result; it does not certify ideal SVDs, an arbitrary floating solver, full old eight-gate admission, unaliased primitive frequencies or physical clocks. See EXACT_T_THEOREM.md and exact_T_results/EXACT_T_CERTIFICATE.json.

## Separate published-circuit contract

The ten-channel Riechert acquisition is addressed only through its own frozen descriptive contract. No raw waveform was downloaded, parsed, fitted or scored in this turn. The contract binds the existing30,941,478-byte author-deposited file by SHA256, fixes metadata grouping and60/20/20 held-out label-group partitions, and fixes DC/AC RMS, rectangular spectra with Hann sensitivity, dominant bins and centroids. Training-only median and piecewise-linear comparators remain descriptive; no calibrated gauge-model/null comparison is claimed.

The original serialization failure and original code/freeze remain. Append-onlyv0.2 preserves the scientific recipe and adds disclosed serialization, exclusive-output and finite-reduction safeguards. Its31 small controls and byte-identical replay pass. A separate same-team reviewer passed15 additional small/static categories. These are engineering checks, not experimental accuracy or hardware qualification. SPECTRAL_ERROR_LEMMA.md gives conditional deterministic voltage-to-feature bounds; actual calibration, timing and validated computation debits are missing. Native62-channel apparatus admission, Gauss/phase extraction and physical correspondence remain HOLD.

## Replay

Use a new external output directory and the full UD repository containing the immutable PR240 dependencies. The phase replay resolves repository paths directly and copies no raw trajectories or large factors:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python phase/replay.py --repo /absolute/UD --out /absolute/new-phase-replay
PYTHONDONTWRITEBYTECODE=1 python exact_t.py --phase-dir /absolute/this-capture/phase --repo /absolute/UD --out /absolute/new-exact-T-replay
PYTHONDONTWRITEBYTECODE=1 python component/replay_v2.py --output /absolute/new-component-controls.json
```

The first replays four finite phase certificates, ten fixed controls and an isolated hash-negative custody check. The second checks the four finite exact-T implications and six boundary controls; it consumes the independently checked phase residual premises. The third runs synthetic contract controls only. Primary author notes are paraphrases with immutable source hashes; no acquisition code, credentials or session configuration is captured. Imported code was read as data and not executed.

## Scope and review

The phase producer's freeze preceded phase scoring but followed the earlier saved estimator outcomes. The exact-T extension was written after finite-phase outcomes were known and frozen before its own predicate evaluation. The component contract was selected with inherited published-data audit summaries known. These are not blinded external preregistrations. Separate same-team audits are retained with source bindings; external review remains PENDING. Original reviewer endpoint-serialization and component serialization failures and their additive corrections are preserved. Old captures are unchanged. The unavailable Gap2_FINAL_Finite_Genesis.png was unused. No public-site deployment or outside outreach occurred.
