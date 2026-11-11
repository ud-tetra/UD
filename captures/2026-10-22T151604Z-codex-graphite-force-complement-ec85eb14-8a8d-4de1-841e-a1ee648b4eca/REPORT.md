# Matched-geometry REBO force complement and one-ULP control

22 October 2026. **Development — no registry entry.** Extends draft PR #394 (direct carbon-angle source trace) and draft PR #396 (archive-to-replay pointwise transfer audit). Full 81-coordinate Hessian **HOLD**, independent review pending, physical promotion **0**.

## Partition and controls

At every offset of the two frozen graphite probes, `matched_complement.py` reads the unchanged instrumented REBO source-copy plugin from PR #394, collects its 3,024 direct `gSpline` angular force records, and assembles a Cartesian vector `F_angle`. It defines `F_complement = F_full - F_angle` at **that same coordinate array**, then projects each vector and applies the side stencil to the complement directly. The complement contains all other REBO forces together, including pair radial and other bond-order paths. The pointwise identity `F_full=F_angle+F_complement` is true by construction; its exact binary64 closure is an accounting check, **not independent validation** of a source-term formula.

Seven h values from 8e-5 to 1.25e-6 Å use 17 unique coordinates per preparation, with the same probe 34/component 8 and probe 30/component 4 as PR #394. The original plugin SHA-256 is `80b511dd88cfa6db9d15705709f36d6b37a40892a6d703248a3b86ab098402bf`; the original potential `CH.rebo` SHA-256 is `70b77656397c0468631af41883d3b781f30432189f749eb0c3d724141055cbd4`.

Two mathematically equivalent coordinate construction orders (extended precision then cast versus binary64 multiply/add) produce identical stored coordinates and complement stencils in this tested setup. A third control moves **every** binary64 coordinate by exactly one representable step, toward +∞ or -∞ according to fixed `(atom index + Cartesian index)` parity. That pattern is independent of sampled force, case, offset sign, and result. Its largest coordinate displacement is 7.10543e-15 Å. This is an intentional conditioning probe, not an estimate of experimental positional uncertainty.

## Signed complement side stencil

All responses in eV/Å²; the table gives the unperturbed complement, followed by its fixed one-ULP counterpart:

| h (Å) | `21_dir_0` base | `21_dir_0` one ULP | `21_dir_10024` base | `21_dir_10024` one ULP |
| ---: | ---: | ---: | ---: | ---: |
| 8e-5 | -8.10e-10 | +1.24e-9 | -2.691e-8 | -3.816e-8 |
| 4e-5 | +3.675e-8 | -7.648e-9 | -4.537e-8 | -9.541e-9 |
| 2e-5 | +1.224881e-7 | +5.100382e-8 | -7.370771e-8 | -1.107027e-7 |
| 1e-5 | +1.056585e-7 | +1.128622e-7 | +1.093691e-8 | +4.040344e-8 |
| 5e-6 | +2.994e-9 | -2.879367e-7 | -2.639534e-7 | -1.566455e-7 |

The captured JSON also retains h=2.5e-6 and 1.25e-6, every point's three projected force values, and each per-point force-vector closure check. Maximum vector closure is exactly 0 in the recorded binary64 arithmetic; projected point identity is within 3.30e-17 eV/Å. The force-level complement agrees with PR #394's `full minus direct-angle` middle-step result to 1.16e-12 and 5.54e-11 eV/Å², respectively. Over the full ladder the largest difference from that earlier subtraction order is 4.69e-10 and 6.43e-10 eV/Å².

At h=2e-5 Å, the one-ULP shifts are -7.14843e-8 and -3.69950e-8 eV/Å², substantial fractions of the respective base complement values. No stable step plateau is observed in either case. This control does not establish a universal uncertainty bound or show that the complement is physically zero. It shows sensitivity of this selected finite stencil to a fully specified representational perturbation. There is still no experimental dissipation, velocity or load-series data and no UD source coefficient.

## Decision

Direct force-level subtraction removes one avoidable ordering question but leaves the same numerical resolution gate. **NO-GO for a quantitative remaining friction or load response from these static stencils.** The conventional carbon-angle attribution for the dominant side discrepancy still stands. A future trace should log the remaining REBO bond-order contributions independently at a single pinned geometry, check additivity against the built-in force, and then require a convergent residual with a calibrated error envelope. Only after that should a load- and velocity-controlled two-angle friction protocol be evaluated against the honeycomb/moiré baseline. Neither the 60° pairing nor this complement supplies a dissipation law.

To replay the captured JSON checks, run `python3 verify_matched_complement.py` with the files together. A fresh LAMMPS run also needs the pinned source/plugin/runtime from PR #394, the frozen `CH.rebo`, and the two copied structure inputs placed at the paths in `matched_complement.py`. Constructor checks only. `Gap2_FINAL_Finite_Genesis.png` was unavailable and was not used.
