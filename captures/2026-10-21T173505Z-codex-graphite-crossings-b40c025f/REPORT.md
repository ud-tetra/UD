# Graphite cutoff-crossing attribution v0.1

RESULT: NUMERICAL diagnosis passes for all six previously failed stencils. Original qualification remains HOLD; physical promotion remains 0.

The fixed-normal KCz implementation shifts the attractive energy at the cutoff but leaves a nonzero limiting force immediately inside it. A pair entering or leaving the cutoff can therefore contaminate a finite derivative stencil. No parameters, original tolerances, coordinates, or saved matrices were changed.

| Failed check | Cutoff Å | Crossing pairs, x/y | Maximum observed discrepancy | Residual after attribution |
| --- | ---: | --- | ---: | ---: |
| Local g, 21 dir10024 | 20 | 36 / 36 | 3.45581661e-4 | 5.33537353e-9 |
| Local g, 21 dir0 | 24 | 144 / 288 | 1.60749438e-4 | 4.46856091e-9 |
| Local g, 21 dir10024 | 24 | 36 / 0 | 8.05905832e-5 | 5.33622563e-9 |
| Energy mixed, 21 dir10024, x | 16 | 36 total | 7.82149592e-5 | -3.93516865e-7 |
| Energy mixed, 31 dir10084, y | 16 | 25 total | 4.75389589e-5 | -6.64569694e-8 |
| Energy mixed, 31 dir10134, y | 16 | 25 total | 4.89240372e-5 | 1.26882242e-6 |

All discrepancy and residual values have units eV/Å². Local residuals are maxima over the complete retained g array; energy residuals are signed. Pair counts include periodic images and count each unlike-layer pair once. Counts for x/y can overlap and must not be added as unique counts.

The local diagnostic residuals meet the inherited 1e-7 threshold. Energy attribution residuals meet the predeclared diagnostic 5e-6 threshold and are below the original energy tolerance. This subtraction explains the failures; it is not a replacement derivative or a retroactive PASS for the original run.

## Method and provenance

For each failed stencil, enumerate all unlike-layer pairs within 0.005 Å of its cutoff, using exact lateral supercell vectors and integer image bounds obtained from inverse-lattice norms plus coordinate extrema. Bounds are [-2,2] in both lateral directions for these inputs. No z image can enter because the box height is 100 Å and the layer separation is about 3.4 Å. Stencil displacement is smaller than the shell width, so a pair omitted from the shell cannot cross. Use r² < cutoff² at each corner. PAIRS.npz records 1-based atom IDs, image integers, base displacements and memberships.

Evaluate the shifted KCz pair energy and vertical force independently in NumPy. For local g, aggregate crossing forces into the same normalized primitive-periodic groups and calculate fine-minus-coarse derivatives. For the energy test, subtract the crossing-pair force mixed derivative at h=5e-5 Å from its four-corner energy mixed derivative at h=0.001 Å. Compare with the original recorded discrepancy.

Source reference: LAMMPS src/INTERLAYER/pair_kolmogorov_crespi_z.cpp at commit 111817ce3255b756025a0c57389908a2b719cd6b, the latest returned file revision before 2025-07-23. This is not proof of the wheel's source byte identity. Nine isolated-pair checks against installed runtime 20250722, spanning near contact and both sides of 16/20/24 Å cutoffs, agree in energy and vertical force to 1e-12 in metal units. The numerical bridge supports the formula used here. Runtime installation is required to repeat runtime_check.py.

The diagnostic FREEZE was written after the original failures and before these attribution outcomes. It is an explicitly post-failure investigation. Verification checks saved hashes, membership and aggregation; it is constructor verification, not independent review. Latest main observed: 62cb6e62d9ec4f170c5dbe5e859af9dea92282f4; governance unchanged.

## Interpretation

DERIVED: the unsmoothed cutoff permits force discontinuities. NUMERICAL: their enumerated contributions account for all six observed failures within the declared diagnostic limits. OPEN: remaining small residuals are not uniquely separated into smooth truncation and total-energy cancellation. CANDIDATE: a UD-specific dissipative protection hypothesis still lacks an independent constraint. No physical bath, friction prediction, full-supercell stability proof or empirical UD bridge follows.

Next: freeze a separately versioned smooth-cutoff model and repeat derivative/energy controls before considering bath inference. Treat any smoothing as a model change, with fresh results and comparison to the unchanged legacy baseline.
