# Two-shell local load response: calculation receipt

Status: NUMERICAL_CONDITIONAL_CONVENTIONAL_EQUILIBRIUM. Physical promotion 0.

The replay implements SI Eq. S1/Table S1 from Minkin et al., PRB 108, 085411 (2023), arXiv:2308.06302, on 14 atoms in the exact seven-cell top layer and a finite lower patch. The 2023 Mendeley archive DOI 10.17632/svnpzbjc3t.1 supplies read-only X/Y/Z grids for regression positions and mismatch checks. Source tar SHA-256 adea7468f311c648a0d25abf4f5eecacd8eebe1b6fc7761ffcea7d073b2f460b; data ZIP SHA-256 b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875. No imported code executed.

The code fits E, E_z, E_zz independently at 3.46 Å to first and norm-three reciprocal shells. It solves three local saddle branches and one minimum in x,y,z, with a quadratic vertical Taylor model. The chosen reference load yields z_min=3.46 Å. This requires a tensile baseline of -10.74 MPa at 16 Å; the differential pressure response is thus not a claim at zero lab load. Finite pressure differences at +/-5 MPa verify the stationary-branch envelope slope.

At 16 Å, the three enthalpy barriers are 75.16–75.21 μeV/atom, vertical gaps 0.0020324–0.0020325 Å, and pressure slopes 0.033228–0.033229 μeV/atom/MPa. For cutoffs 14/18 Å, local slopes are 0.033215–0.033216. The earlier leading first-shell slope 0.03472 is about 4.3% higher. Pair-sum grid mismatch at 16 Å persists: 1.292 μeV/atom centered RMS and -0.501 meV/atom mean energy offset on the sampled grid; reconstructed barrier differs from the deposited-grid two-shell fixed-height value of about 78.2 μeV/atom. Do not equate the small slope variation across cutoffs with general model or experiment uncertainty.

Source Table I specifies 18x18 simulation cells at (2,1), yet ZIP folder says 10x10; exact run identity remains unresolved. The calculation is rigid, local, and conservative; it supplies no kinetic friction estimator, damping, UD material coefficient, or measured 2026 load curve. Existing v12/v13 symmetry and harmonic-sector results remain conditional, with no independently tested UD-specific residual.
