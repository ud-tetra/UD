# THM-LS4: Spectral Restore Projector

**Version 1.0 | Depends: THM-534 (transport matrix T)**

---

## Statement

For each distinct eigenvalue λ of T, define the **spectral restore projector**:

    P_λ = Σ_{v ∈ ONB(V_λ)} |v⟩⟨v|

where the sum is over any orthonormal basis of the eigenspace V_λ.

P_λ is the unique orthogonal projector onto V_λ.

## Properties

(i) P_λ is uniquely determined by T and the eigenvalue λ. It does not depend on the choice of orthonormal basis for V_λ.

(ii) P_λ² = P_λ (idempotent).

(iii) P_λ† = P_λ (Hermitian / self-adjoint).

(iv) Σ_λ P_λ = I (completeness).

(v) P_λ P_μ = 0 for λ ≠ μ (orthogonality).

(vi) T = Σ_λ λ P_λ (spectral decomposition).

## Proof

Standard spectral theorem for real symmetric (Hermitian) matrices. T is real and symmetric (THM-534: T is doubly stochastic and symmetric). The spectral theorem guarantees the existence and uniqueness of the projectors {P_λ}. Properties (i)–(vi) are standard consequences.  □

## Application

For the tetrahedral transport matrix T with spectrum {1(×1), 1/2(×2), 1/3(×3)}:

    P₁:    rank 1 projector onto the vacuum mode
    P_{1/2}: rank 2 projector onto the weak sector
    P_{1/3}: rank 3 projector onto the color sector = P_- (THM-561)

## Non-claims

This definition does NOT assign physical interpretation to the eigenspaces. The identification of V_{1/3} with "color" or V_{1/2} with "weak" is a separate bridge claim.

---

## Proof-state

**EXACT STRUCTURAL.** The spectral theorem is standard linear algebra. P_λ is uniquely defined by T. No approximations, conventions, or interpretive content.
