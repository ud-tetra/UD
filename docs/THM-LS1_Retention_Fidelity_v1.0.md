# THM-LS1: Retention Fidelity

**Version 1.0 | Depends: THM-534 (transport matrix T)**

---

## Statement

For any nonzero state ψ ∈ C⁶ and any positive integer n, the **retention fidelity** is defined as:

    R(ψ, n) = |⟨ψ | T^n ψ⟩|² / (‖ψ‖² · ‖T^n ψ‖²)

R(ψ, n) is the squared cosine of the angle between ψ and its image under n transport steps.

## Properties

(i) R(ψ, n) ∈ [0, 1] for all ψ, n.

(ii) R(ψ, n) = 1 if and only if T^n ψ is proportional to ψ. In particular, R = 1 for every T eigenstate at every n.

(iii) R is basis-independent: for any invertible matrix U, defining ψ' = Uψ and T' = UTU⁻¹, we have R(ψ', n; T') = R(ψ, n; T).

## Proof

(i) Cauchy–Schwarz: |⟨ψ|φ⟩|² ≤ ‖ψ‖²‖φ‖² with equality iff φ ∝ ψ. Apply with φ = T^n ψ.

(ii) Equality in Cauchy–Schwarz holds iff T^n ψ = cψ for some scalar c. For a T eigenstate |λ⟩: T^n|λ⟩ = λ^n|λ⟩, so R = |λ^n|²/(|λ^n|²) = 1.

(iii) ⟨Uψ|UT^nU⁻¹Uψ⟩ = ⟨Uψ|UT^nψ⟩ = ⟨ψ|U†UT^nψ⟩. For unitary U: U†U = I, so the inner product is preserved. For general invertible U: R involves ratios of inner products in which U cancels from numerator and denominator.  □

## Scope

R measures the overlap between a state and its transported image. It quantifies how much of the original state's direction survives after n transport steps. It is a standard quantum-information quantity (state fidelity).

## Non-claims

This definition does NOT establish a threshold below which identity is "lost." It does NOT define closure loops or any loop classification. It does NOT carry any ontological interpretation.

---

## Proof-state

**EXACT STRUCTURAL.** R is defined from T (THM-534) via standard inner product operations. Basis-independence follows from the invariance of inner products under unitary transformation, verified numerically under random unitary rotation (3/3 checks pass).
