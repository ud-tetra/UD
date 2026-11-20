# v0.3.3 completion of original result bytes

The exact original v0.3 `results.json` has now been transferred to GitHub **without changing its bytes**.

- Local SHA-256: `46c149dcd8a006437a551b203e9d5c0c35439480a4080c624ff725ac5efb434a`
- Git blob: `8b77e418a49a68dbef5bcf9df0901acf234881ea`
- Size: 5338 bytes
- Executed provenance: local `verify.py` run, with `run.log` and independently checked `replay.log`; original source SHA-256 and Git blob IDs are documented in v0.3.2.

All consequential run source and output files (REPORT.md, verify.py, replay_stdlib.py, results.json, run.log, replay.log) are now independently readable in this GitHub PR. Historical input copies reside in the cross-linked UD-Physics PR and local ZIP.

The original local `MANIFEST.json` and ZIP binary have **not** been transferred; this append-only capture has sufficient file provenance to regenerate results from `verify.py`. Reproduction in a fresh GitHub checkout and non-constructor review remain pending, and no physical correspondence has been promoted.
