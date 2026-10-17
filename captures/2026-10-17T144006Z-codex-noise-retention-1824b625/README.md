# Noise versus retained-signal certificate

Read `UD_NOISE_RETENTION_FRONTIER_v0.1.md` first. The result is conditional on inherited real modal bounds and declared acquisition/model error contracts. Physical promotion 0; independent review pending; no measured data.

`NOISE_RETENTION_CERTIFICATE.json` records all exact outward dyadic inputs, 512-bit scalar boundary enclosures and 207 grid evaluations. `NOISE_RETENTION_CURVE.csv` is the compact data table. `ACQUISITION_CHOICES.json` supplies five proposed 4096-axis-sample contracts with exact vector and sufficient scalar error ceilings. PNG and PDF show the conservative sampled lower-bound curves. `PROVENANCE.json` hashes every inherited input.

Reproduce with Python 3.12 and `requirements.txt`:

```sh
python certify_noise.py
python -m unittest -v test_noise.py
python validate_noise.py
python plot_noise.py
```

The isolated replay checks this derivation; it does not repeat the parent's full 600-cell modal diagonalization or execute a physical experiment. Use the source-bound status stated in the report. Repository capture is append-only and local; no public publication is included.
