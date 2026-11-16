# AW5 reproducibility supplement — recursive refinement

**EXACT_INTERNAL** stationary law and grade-aware Schur recursion. **NUMERICAL / CONDITIONAL** phase-averaged acquisition bounds with certified error allowances. **Physical Promotion = 0.** Constructor verification. Independent review and the measured hardware gate remain open.

## Exact stationary boundary residue

Take the hollow AW5 and stellarly subdivide every tetrahedron of each selected original leaf once per level. Keep each original leaf boundary fixed and apply the unit simplex metric at each level. The degree-2 homology rank is one at every finite depth, so the unnormalized face heat trace tends to one. Harmonic boundary projection is an additional metric-dependent quantity.

Use concordant top-cell orientations within a leaf. Minimizing the squared norm of the cavity shell minus a top boundary turns into a unit-resistor dual network. Each interior shared face contributes (x_i−x_j)² for the two incident top-cell coefficients and each exposed face contributes (z_f−x_i)². The terminal currents give the four boundary coefficients of the harmonic representative. Symmetry requires the four-port response to have the form α_d(4I−J), or a star with arm resistance r_d=1/(4α_d). The base case is one cell with four unit terminal arms and r₀=1.

In the next level, strip the unit terminal edges from each of four child networks. Each child’s equivalent internal arm has resistance r_d−1. An original external terminal connects to one child center with resistance r_d after restoring its unit terminal edge. The four centers form a complete graph. Across each shared face the edge resistance is (r_d−1)+1+(r_d−1)=2r_d−1. Its differential conductance on the zero-sum center modes is 4/(2r_d−1). Adding that internal differential resistance yields

    r_(d+1) = r_d + (2r_d−1)/4,
    r_d = [1+(3/2)^d]/2.

For the unit signed shell load, one leaf’s cavity coefficient has magnitude 3α_d and each exterior coefficient has magnitude α_d. The harmonic norm squared is 3 times the sum of the four coefficients α_(d_i), since the representative is an orthogonal projection of the unit shell. The original twelve-face signed unit probe therefore has squared normalized overlap [Σ_i α_(d_i)]/4. At common depth d the stationary residue is

$$R_d=\frac{1}{2[1+(3/2)^d]}.$$

This quantity approaches zero with fixed b₂=1. The ideal stationary gate 3/64 is first missed at depth six, where R₆=32/793. The matched split metric from the preceding AW5 supplement carries a different metric and readout declaration. The result above concerns the unit simplex metric along the stated refinement sequence.

## Pinned finite-window receipts

The declared test retains the original 256 midpoint observations over a 32-native-unit window and compares a fixed exterior signed probe against the filled carrier and a fixed two-face reference. The acquisition assumptions and independent centered noise allowance are specified in the Discovery receipts. Each table entry is a downward-rounded lower bound against both controls combined.

| Carrier scope | Minimum conditional contrast | Verification |
| --- | ---: | --- |
| All 16 subsets of first-level leaf replacement | 0.075435 | Exact rational enclosure and nuisance budget |
| Uniform depth 2 | 0.055678 | Exact rational enclosure and nuisance budget |
| Uniform depth 3 | 0.054310 | Direct damped enclosure, with independently varying arm damping |
| Uniform depth 4 | 0.052667 | Recursive boundary resolvent, Fourier and numerical allowance |
| Uniform depth 5 | 0.109238 | Recursive boundary resolvent, Fourier and numerical allowance |
| Uniform depth 6 | 0.047115 | Recursive boundary resolvent; headroom 0.000240 |

- The [exact static replay](https://github.com/ud-tetra/UD-Physics/blob/359989a70d2fd604c3b213b2f3245574a867fb2c/candidates/aw5-hollow-star-intake/RECURSIVE_LEAF_RESIDUE.md) verifies the dual-network formula at depths zero through three. The [depth 1–3 receipt and controlled window](https://github.com/ud-tetra/UD-Physics/blob/359989a70d2fd604c3b213b2f3245574a867fb2c/candidates/aw5-hollow-star-intake/refinement_depth_receipt.json) pin the exact arithmetic, protocols and captures.
- The [depth 4–6 derivation and replay](https://github.com/ud-tetra/UD-Physics/blob/107d9c9feed6416b7eb59b6b215158bf5bd0ddfd/candidates/aw5-hollow-star-intake/RECURSIVE_FREQUENCY_RESPONSE.md) retain 14 boundary coordinates per leaf while gluing, then reduce to a 16-face AW5 resolvent. They use the same fixed 3/64 threshold. The shallow full-matrix cross-check and local residual accounting are constructor checks.

The finite-window depth-six result clears the gate despite the lower stationary residue. The published headroom depends on the stated carrier, readout, nuisance tolerances, numerical allowances and noise model.
