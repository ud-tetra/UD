# C06 Whitney unsigned direct port v0.10

**Status.** EXACT / CONDITIONAL for the declared cooriented face field and unit regular cell. NO-GO for an exact shared half-stock time under the unaugmented Whitney metric. CANDIDATE (agile) for a separate rotational energy. Physical Promotion = 0.

**Source boundary.** [UD-Physics #404](https://github.com/ud-tetra/UD-Physics/pull/404) supplies the regular unit-triangle area-averaged Whitney tangential metric on signed incidence flags. [UD-Physics #405](https://github.com/ud-tetra/UD-Physics/pull/405) and the integrated Regular Simplex Whitney Spectrum note (§5.3, in the pinned Discovery base) develop the centered rotational energy. [UD #537](https://github.com/ud-tetra/UD/pull/537) and [Discovery #413](https://github.com/ud-tetra/UD-Physics/pull/413) supply the unordered shear direct port. Applying Whitney face energy to that port uses the explicit coorientation map below. The established globally signed cut/cycle pullback is distinct and retains its own spectrum.

## Count correction

Each edge belongs to two faces. For a pair of distinct adjacent edges, their union determines one triangle, not two. Thus the outer-product sum is 2I+A_adj. With block metric (u−v)I+v11^T, the flag pullback is 2uI+vA_adj. Its sector spectrum from v0.9 stands.

## Whitney transfer test

Take a length-one regular tetrahedron with Euclidean source metric. Let b_f have the three boundary incidence signs in the increasing-edge basis. For each face, define the tangential interpolation of three **unordered** flag amplitudes as the sum of their Whitney edge fields weighted by b_f. Under global edge reorientation the two signs cancel. Reversing a face orientation multiplies the entire interpolated field by −1 and preserves its energy. The resulting map is face-local and its metric is tetrahedrally equivariant. This is a declared identification of the unordered input with oriented face records.

The signed Whitney face block is (6I−b_fb_f^T)/9. Conjugating by diag(b_f) gives the ordinary flag block (6I−11^T)/9. Thus (u,v)=(5/9,−1/9). With copied flags and the closed skew exchange x' = −F*y, y' = Fx, the source is initially x0 with zero flag stock. Source plus flag squared norm is conserved. The squared phase rates are

```math
(\omega_E^2,\omega_{T_2}^2)=(4/3,10/9),\qquad
\omega_E/\omega_{T_2}=\sqrt{6/5}.
```

The rates are dimensionless in the stated unit convention. Any simultaneous half transfer at positive time would require both phases to be odd multiples of π/4, making the rate ratio a ratio of odd integers. The ratio √(6/5) is irrational by prime valuations. Thus preparations with both sectors have no exact common half-stock time for this constant unaugmented port, including late times. This rules out the shared half-transfer requirement for that port and does not rule out other schedules or approximate coincidences.

## Candidate rotational completion

The regular-triangle centered rotational mass is b_fb_f^T/9 in signed coordinates. Equivalently, its factor is 1/48 times the area-averaged exterior-derivative energy matrix, whose coefficient on b_fb_f^T is 16/3. This is the resident rotational contribution, not an independently required extra term in the physical energy. If the interaction adds λ copies of it to the Whitney face energy, the cooriented flag block becomes (6I+(λ−1)11^T)/9. Consequently

```math
v=(\lambda-1)/9,\qquad (\omega_E^2,\omega_{T_2}^2)=(4/3,\,2(5+\lambda)/9).
```

With λ≥0, one additional copy (λ=1) gives a common first half-stock time π√3/8. The choice is fixed by requiring equal rates in this family. An independent constitutive law must still supply that extra energy and justify the port. Stage-two depletion, deficit allocation, and observable calibration remain separately open.

## Verification

The exact replay integrates the three triangle Whitney products from the area-average barycentric second moments, checks the centered rotational coefficient and directly replays the ordinary five-mode spectra. The target equal rate was known before this audit. No empirical fit enters.
