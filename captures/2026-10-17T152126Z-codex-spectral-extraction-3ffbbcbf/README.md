# Exact Hankel spectral verification without dense storage

Read `UD_STORAGE_LIMITED_SPECTRAL_EXTRACTION_v0.1.md` for the theorem, input assumptions and limits. `PARALLEL_APPENDIX_REVIEW.json` audits the supplied parallel work; `CORRECTED_MONITORING_APPENDIX.md` is its proposed replacement.

The certifier derives exact/validated singular-value enclosures from total Hankel energy and two small Gram matrices. It verifies the entire discarded tail. The FFT basis proposer is untrusted; its output must pass the separate exact verifier. No dense253952×151552 matrix is formed.

```sh
python review_parallel.py
OPENBLAS_NUM_THREADS=1 python -m unittest -v test_spectral.py
python full_size_controls.py
python native_precision_contract.py
python validate_spectral.py
```

For a real numeric record, follow the two proposal/certification commands in the main report. A complete normalized history record and large dense candidate were not supplied for full-scale verification. The supplied full-dimension controls are constructed numeric examples, not UD trajectories or hardware data. Their RSS/runtime log is not a benchmark for the general dense proof path.

Status: derived method,constructor verified;13 tests and3 full-dimension spectral controls. Independent review pending. Physical promotion0. The method certifies numeric history spectra, not hidden-state reconstruction,model membership orphysical-law identification.
