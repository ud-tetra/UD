# Four-coordinate physical module and two-channel readout

Read `UD_Four_Coordinate_Physical_Realization_and_Two_Channel_Readout_v0.1.md` for the derivation and `Four_Coordinate_Circuit.png` for the schematic. The SVG and its generator are included.

The four-coordinate normalized module has a passive two-loop LC analogue, with exact inherited energy, complementary voltage outputs, a deterministic sample-noise bound and an explicit finite-load apparatus energy balance. This is a development construction, not empirical evidence for fundamental UD. Physical promotion 0; independent review pending.

## Replay

Requires Python 3, NumPy and SciPy. From this directory:

```sh
OPENBLAS_NUM_THREADS=1 python verify_physical_module.py
```

Expected: 27 exact and 9 numerical checks pass. It regenerates `PHYSICAL_MODULE_DATA.json` and `PHYSICAL_MODULE_CHECKS.json`. Replaying does not require network access, the original image, or executing imported source artifacts. Rational algebra is exact; floating trajectories, roots, integration and decoder examples are numerical corroboration. `ENVIRONMENT.json` records the constructor environment, not a universal dependency pin.

To recreate the schematic, run `python make_schematic.py`, then render the SVG with Inkscape. This rendering step is not needed for the algebra replay. The SVG is a conceptual network diagram; dashed sensing connections are not additional circuit wires.

`SOURCE_REGISTER.json` distinguishes primary circuit ingredients from UD source equations. `CLAIM_REGISTER.json` declares claim types and open issues. Source copies in `sources/` are preserved data. No imported script is executed.

## Validation note

The first coarse fixed-step dissipation integral did not resolve a fast secondary transient accurately enough. Adaptive quadrature now verifies the same energy-loss tolerance and additionally checks its estimated error. No source equations or analytic bounds were altered. A clean-directory replay matches both output JSON files byte for byte on the recorded environment.

This package is separate from frozen manuscripts and does not supersede PR120. Every code/data/output file is listed in `SHA256SUMS.json` (the inventory excludes itself). The outer ZIP contains this inventory. GitHub capture records the ZIP hash separately.
