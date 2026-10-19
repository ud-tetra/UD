# Uniform excitation guarantee and apparatus-validation freeze

This capture derives a uniform exact-sketch cutoff guarantee for a declared neighborhood of six previously certified preparations, and freezes a prospective apparatus-intake/model-mismatch protocol. Development — no registry entry; external review PENDING; Physical Promotion=0.

The preparation radius is2^-20 in operator norm and the encoded-noise radius is1127*2^-48≈4.0039083160082e-12 per62-vector. The guarantee preserves exactly209 singular values above2^-24 for every member of this specified family. It does not promise universal floating solver/frame/phase success. Its larger input noise allowance applies only to this cutoff theorem, not the prior measured-frame/phase gates, and is not a sharp actual tolerance limit.

APPARATUS_CONTRACT.json separates the current temporal lane, the old native1893 history contract, and the six-ratio calibration lane. It requires independent calibration, clock/alias, preparation, raw coverage and heldout lineage evidence. Actual apparatus submissions remain HOLD; the32 synthetic fixtures test logic and fail-closed behavior, not hardware. The toy cap1/16 is local to those controls; the real mismatch cap is OPEN and must freeze before data. No physical noise tolerance is certified.

THEOREMS.md contains the proof and units. inputs/ANCHORS.json is an extraction from PR231 with original-source hashes in INPUT_PROVENANCE.json; the parent certificates are not re-fit. inputs/SOURCE_BOUNDS.json is an independently recomputed source-norm receipt. Source scripts in reviews/ are review evidence, not executed by replay. The original waveform rank/error proof and saved-anchor lower bounds remain explicit inherited premises. Family inputs have exact orthogonality and encoded perturbations; arbitrary preparation-specific clocks and approximate orthogonality are not admitted implicitly.

With python-flint and NumPy installed, run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python replay.py --out /absolute/path/to/new-replay-directory
```

Add `--repo /absolute/path/to/UD` to verify original-source extraction hashes and fields. For a read-only full recomputation of the baseline exact norm, also pass `--raw /absolute/path/to/ramp_clock_stress.i64le`. The pinned original synthetic baseline is150,321,232 bytes; its hash is in INPUT_PROVENANCE.json. Replay checks the prospective freeze, recomputes directed family bounds and small protocol controls, and writes only to a NEW external output directory. No estimators, new large records, physical acquisitions or dense287-GiB Hankel arrays are created. Omitting--raw explicitly uses the frozen source-norm receipt rather than claiming raw scalar replay.

The prospective freeze is a local engineering freeze after the anchor/source outcomes were known, before evaluation of these newly declared controls. It is not blinded data or external preregistration. Same-team design/code reviews remain scoped separately. External review and custodian qualification remain OPEN. Public site unchanged; no new external outreach. The unavailable Gap2_FINAL_Finite_Genesis.png was not used.
