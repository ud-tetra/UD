# UD conditioning review candidate 0.8

Read the manuscript 0.8 and `UD_Conditioning_And_Noise_Bounds_v0.1.md`. The manuscript integrates the derivation in §6.6 and Appendix D.9. The standalone report provides a shorter path to the bounds.

Run `python3 verify_conditioning.py` with SymPy, NumPy and SciPy. It uses the exact source matrices in `baseline/` and regenerates Gram, LDL and polynomial certificates plus `CONDITIONING_CHECKS.json`. The script checks exact two-cell/star factorization conclusions, a chain Sturm bracket and rational LDL lower bounds. Floating fixtures separately test sharp noise directions, generator mismatch, covariance transport, the GLS covariance identity, exact centered sampling and the fixed-norm degenerating family. Floating tolerances do not certify the theorem; the written arguments and exact arithmetic supply the stated mathematical certificates.

The preserved version-0.7 package is included unchanged. It contains prior source papers and replays, which have not all been rerun in this turn. Its checksum inventory was verified before using the matrices. This release adds a conditioning analysis; it does not change the copied generator into the native union generator.

`SOURCE_HASHES.json`, `ENVIRONMENT.json` and `SHA256SUMS.json` record provenance, constructor dependency versions and the new release inventory. No empirical covariance, physical sensing/energy cost, independent review, fresh-environment replay or novelty certification is claimed. Physical promotion: 0.

For operational use, freeze an acquisition protocol with joint temporal covariance, timing error, detector scale and admitted generator uncertainty. The quarter-period result applies only to the retained statistic and fixed independent snapshot-noise contract; it is not a universal sensor optimum.
