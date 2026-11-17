# C06 unweighted boundary action coefficient v0.11

**Status.** EXACT / CONDITIONAL for the declared regular Euclidean Whitney boundary action. NO-GO for exact simultaneous half stock under its unweighted unit-cell direct port. Native relative weighting, the latch, and deficit allocation remain OPEN. Physical Promotion = 0.

**Source basis.** [Discovery #404](https://github.com/ud-tetra/UD-Physics/pull/404) supplies the Whitney trace mass. [Discovery #405](https://github.com/ud-tetra/UD-Physics/pull/405), the Hodge-energy and gyration notes, supplies the curl Gram and separates a kinematic rotational energy from a second constitutive copy. [UD #538](https://github.com/ud-tetra/UD/pull/538) and [Discovery #414](https://github.com/ud-tetra/UD-Physics/pull/414) supply the cooriented Whitney port and its half-stock criterion. The new calculation applies the literal proposed boundary action to that port. It does not identify signed cut/cycle sectors with ordinary shear sectors.

## Defined action and independent term evaluation

On each face of a regular tetrahedron of side length ℓ, use real Whitney one-forms normalized to unit circulation on each basis edge. The faces have ordinary Euclidean duality. Let b be the three-entry boundary sign column in the oriented edge basis, and A=√3 ℓ²/4. Let c be the factor on the derivative term, the same on every face. Compare squared mass and squared curl by taking their sum of face averages. The raw surface integral multiplies the assembled metric by A, since all areas agree, and has the same sector-rate ratio. A dimensional version needs c with units of length squared. Below, the literal coefficient-one comparison uses the prescribed nondimensionalization.

The already sourced Whitney mass on one face is M_f=(6I−bb^T)/(9ℓ²). The curl of a Whitney combination w with coefficients q is constant on the flat face. Stokes' theorem and basis edge circulation give curl(w)=(b^Tq)/A. Thus the area-average Gram of the derivative term is

```math
Q_f=A^{-2}bb^\mathsf{T}=\frac{16}{3\ell^4}bb^\mathsf{T}.
```

In the oriented face coordinates, the combined form is M_f+cQ_f. Passing to ordinary flag inputs by diag(b) sends bb^T to 11^T, so the diagonal and off-diagonal scalars are

```math
u=\frac{5+48c/\ell^2}{9\ell^2},
\qquad v=\frac{48c/\ell^2-1}{9\ell^2}.
```

Equivalently, the required action coefficient is c=ℓ²/48. It matches the coefficient of the resident centered rotational mass, already present in M_f. The equality only identifies which coefficient would supply another copy. It is not a derivation of that second copy from the unweighted action.

## Consequence for the direct-port dynamics

Use the fixed v0.10 skew exchange between the mean-zero ordinary six-edge source and its twelve face flags. Source metric is Euclidean, flag metric is the action block above, flag stock is initially zero, and total squared metric stock is conserved. With per-face area averages the squared rates are

```math
\omega_E^2=\frac4{3\ell^2},\qquad
\omega_{T_2}^2=\frac{2(5+48c/\ell^2)}{9\ell^2}.
```

At ℓ=1 and c=1 the curl term contributes 16/3 on bb^T, which is 48 times the required 1/9. Thus v=47/9 and the squared rates are (4/3,106/9). The rate ratio √(6/53) is irrational by prime valuations. The two sectors cannot each have phase an odd multiple of π/4 at the same positive time. This rules out exact shared half stock for constant-rate exchange with this unweighted unit-cell flag metric. It does not rule out separately latching the sectors or other action/port choices.

On the nondimensional coefficient-one family, cancellation at ℓ²=48 would be a choice of relative scale. It cannot establish cancellation on the regular unit cell or scale-independent automatic equalization. Changing common area averaging rescales both terms together and does not change the necessary relative coefficient. No microscopic length, physical clock, or empirical target was used.

## Exact replay

The Python replay constructs the mass by elementary barycentric second moments, computes the curl Gram independently by the Euclidean wedge inner product, compares its coefficient with Stokes, and applies the combined flag metric to five exact mode vectors for zero augmentation, the equalizing coefficient, and literal unit weighting. The equal-rate target was known. The comparison used no fitted empirical coefficient.
