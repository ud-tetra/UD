# UD symmetry review candidate 0.6

The top-level narrative manuscript 0.6 supersedes 0.5 for development. The symmetry/contribution audit explains the repaired conventions and priority limits. The preserved 0.5 package is nested unchanged and contains the four source papers, apparatus audit and replay, and earlier carrier package.

Run `python3 verify_symmetry.py` with SymPy. It regenerates `SYMMETRY_CHECKS.json` and `EXACT_SYMMETRY_MATRICES.json`. The replay checks finite signed actions, characters, boundary equivariance, symbolic channel spectra, projectors and context covariance. The written proof supplies general conditional statements; this is not independent review.

`SOURCE_HASHES.json` records inspected local baselines. `SHA256SUMS.json` inventories the package except itself. `ENVIRONMENT.json` records the constructor environment. No earlier source paper is edited. Physical promotion remains 0.
