# THM-LS11: Repair Burden Cross-Eigenspace Additivity

**Version 1.0 | Depends: THM-LS2 (repair burden)**

---

## Statement

Let ψ ∈ V_λ, and let δψ₁, δψ₂ be perturbations such that their out-of-eigenspace components target **distinct** eigenspaces: there exist μ₁ ≠ μ₂ (both ≠ λ) with P_{μ₁} δψ₁ = δψ₁ and P_{μ₂} δψ₂ = δψ₂. Then:

    B_repair(ψ, δψ₁ + δψ₂) = B_repair(ψ, δψ₁) + B_repair(ψ, δψ₂)

The repair burden is additive for perturbations targeting distinct eigenspaces.

## Proof

From THM-LS2: B = Σ_{μ≠λ} (1−μ) ‖P_μ(δψ₁ + δψ₂)‖².

Since δψ₁ ∈ V_{μ₁} and δψ₂ ∈ V_{μ₂} with μ₁ ≠ μ₂:

For μ = μ₁: P_μ(δψ₁ + δψ₂) = δψ₁ + P_{μ₁} δψ₂ = δψ₁ (since δψ₂ ∈ V_{μ₂}, P_{μ₁} δψ₂ = 0).
For μ = μ₂: P_μ(δψ₁ + δψ₂) = P_{μ₂} δψ₁ + δψ₂ = δψ₂.
For other μ: P_μ(δψ₁ + δψ₂) = 0.

Therefore B = (1−μ₁)‖δψ₁‖² + (1−μ₂)‖δψ₂‖² = B(δψ₁) + B(δψ₂).  □

## Scope limitation

If δψ₁ and δψ₂ both have components in the **same** out-of-eigenspace V_μ, the cross term 2Re⟨P_μ δψ₁|P_μ δψ₂⟩ is generally nonzero and additivity fails. The distinct-target condition is essential.

## Verified

Cross-eigenspace case (V_{1/2} and V₁ targets): additivity confirmed to machine precision. Same-eigenspace case: additivity holds in the tested instance but by coincidence of orthogonality, not by the theorem.

## Non-claims

This result does NOT claim general additivity of B_repair. It applies only under the explicit distinct-target condition.

---

## Proof-state

**EXACT STRUCTURAL.** Follows from the orthogonality of eigenspace projectors (P_{μ₁} P_{μ₂} = 0 for μ₁ ≠ μ₂). No approximations or conventions.
