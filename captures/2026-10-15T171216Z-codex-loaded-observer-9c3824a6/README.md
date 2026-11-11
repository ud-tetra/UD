# Loaded observer and finite write/read budget

Read `UD_Loaded_Observer_and_Write_Read_Budget_v0.1.md` for the derivation. The figure shows the declared pulse and subsequent source-free read, with six voltage samples marked.

Run from this directory:

```sh
OPENBLAS_NUM_THREADS=1 python verify_loaded_observer.py
```

Requires Python, NumPy and SciPy. Expected: 46 exact and 10 numerical checks pass. Rational certificates use `fractions.Fraction`; they do not depend on numerical exponentials/singular values. The replay regenerates `LOADED_OBSERVER_DATA.json` and `LOADED_OBSERVER_CHECKS.json` without network access or executing archived/imported scripts. A clean-directory replay matches both JSON files byte for byte on the recorded environment.

For the optional figure, run `python make_figure.py` with Matplotlib installed. The figure uses numerical trajectories and is not itself a proof certificate. All plotted parameters and pulse coefficients are read from the data JSON.

The eight-parameter box preserves matching and opposite mutuals. It is not arbitrary per-component mismatch. Waveform accuracy, zero initial state, static-offset preparation and sample timing/gain calibration are explicit assumptions. Electrical source-port work includes all declared passive losses; digitizer, actuator electronics, durable records, bath renewal and reset remain outside the model. No hardware result, entropy law, boundary-area law or fundamental UD unit calibration is claimed.

Pre-release implementation repair: integer zero entries initially produced floating polynomial energy coefficients. The exact net-work assertion caught this; all model matrix entries, including zeros, are now normalized to Fractions. This changed no mathematical source equation and supersedes no published artifact. See `CORRECTIONS.json`.

Development lane; physical promotion 0; independent review pending. PR121 is a preserved dependency, not silently replaced. SHA256SUMS.json inventories all package files except itself; the repository capture separately inventories the ZIP.
