# THM-567: Intra-Generation Coupling Angle Bound [60°, 120°]

**Version 1.0 | Depends: THM-566 (Yukawa singular values √3)**

---

## Statement

The angle between the two column vectors of the Yukawa matrix Y(θ) is bounded:

    angle(y₁, y₂) ∈ [60°, 120°]

for all V_{1/2} basis rotations θ. The bounds are attained.

## Proof

From THM-566: Y(θ) has singular values σ₁ = 1/√3, σ₂ = 1/3 (or equivalently, M(θ) has σ₁ = 1, σ₂ = 1/√3).

For any 2×2 matrix M = UΣVᵀ with column vectors m₁, m₂, write V = [[cos φ, −sin φ], [sin φ, cos φ]]. Then:

    m₁·m₂ = −(σ₁²−σ₂²) sin(2φ)/2
    |m₁|² = σ₁²cos²φ + σ₂²sin²φ
    |m₂|² = σ₁²sin²φ + σ₂²cos²φ

The extremum of |cos(angle)| occurs at φ = π/4 where |m₁| = |m₂| = √((σ₁²+σ₂²)/2):

    |cos(angle)|_max = (σ₁²−σ₂²)/(σ₁²+σ₂²)

With σ₁² = 1, σ₂² = 1/3:

    |cos(angle)|_max = (1−1/3)/(1+1/3) = (2/3)/(4/3) = 1/2

Therefore angle_min = arccos(1/2) = 60° and angle_max = 180° − 60° = 120°.  □

## Corollary

The 60° floor is the tetrahedral angle arccos(1/2). It is forced by the singular value ratio √3, which is forced by the (*, T, S) geometry on the tetrahedron. No V_{1/2} basis rotation can produce a coupling angle below 60°.

## Non-claims

This bound constrains the INTRA-GENERATION coupling geometry only. It does NOT constrain the CKM matrix, which is an INTER-GENERATION quantity controlled by the IFS shell deformation parameters ε(n). The Cabibbo angle (13°) is not in conflict with this bound because it measures a different geometric quantity.

---

## Proof-state

**EXACT STRUCTURAL.** SVD identity applied to the θ-independent singular values from THM-566. Verified: 1000-point scan confirms all angles in [60°, 120°].
