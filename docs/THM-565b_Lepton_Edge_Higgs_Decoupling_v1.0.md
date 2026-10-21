# THM-565b: Lepton–Edge-Higgs Decoupling

**Version 1.0 | Depends: THM-562 (C⁸ = C⁶ ⊕ C²)**

---

## Statement

The Higgs modes H₁, H₂ (operators on C⁶ connecting V₁ to V_{1/2} within P_+) have identically zero matrix elements with any state in the lepton sector C²:

    ⟨ψ_lepton| H_i |φ_lepton⟩ = 0    for all ψ, φ ∈ C², i = 1, 2.

More generally, for any operator A on C⁶ and any states in C²:

    ⟨ψ_lepton| A |φ_lepton⟩ = 0.

## Proof

The lepton sector C² = span{|Σ,+⟩, |Σ,−⟩} lives in the face-singlet extension space (THM-562). The edge space C⁶ and the face-singlet space C² are orthogonal summands of C⁸:

    C⁸ = C⁶ ⊕ C²,    C⁶ ⊥ C².

The Higgs modes H_i are operators on C⁶. When extended to C⁸ by zero on C², they act as H_i ⊕ 0 on C⁶ ⊕ C². Therefore, for any ψ, φ ∈ C²:

    ⟨ψ| (H_i ⊕ 0) |φ⟩ = ⟨ψ|0|φ⟩ = 0.  □

## Scope

This result applies specifically to the edge-space Higgs modes (operators on C⁶). It does NOT preclude the existence of a separate scalar mode within the face sector C² or within the full C⁸ that could couple to the lepton states. The existence or nonexistence of such a face-sector scalar mode is an open question.

---

## Proof-state

**EXACT STRUCTURAL.** Follows from the orthogonal direct sum C⁸ = C⁶ ⊕ C² (THM-562) and the fact that the Higgs modes are operators on C⁶. No approximations, parameters, or phenomenological input.
