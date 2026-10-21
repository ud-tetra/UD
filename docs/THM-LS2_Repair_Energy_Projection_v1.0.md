# THM-LS2: Repair Burden via Energy Projection

**Version 1.0 | Depends: THM-534 (transport matrix T), THM-LS4 (spectral projector P_λ)**

---

## Statement

Let H = I − T be the transport Hamiltonian on C⁶. For a state ψ in the T eigenspace V_λ and a perturbation δψ, the **repair burden** is:

    B_repair(ψ, δψ) = |⟨P_λ(ψ + δψ) | H | P_λ(ψ + δψ)⟩ − ⟨ψ + δψ | H | ψ + δψ⟩|

This is the absolute energy difference between the perturbed state and its projection back onto the eigenspace V_λ.

## Explicit form

Decompose δψ = δψ_∥ + δψ_⊥ where δψ_∥ ∈ V_λ and δψ_⊥ ∈ V_λ^⊥.

Then P_λ(ψ + δψ) = ψ + δψ_∥ (the in-eigenspace part), and:

    B_repair = |⟨ψ + δψ_∥ | H | ψ + δψ_∥⟩ − ⟨ψ + δψ | H | ψ + δψ⟩|
             = |⟨δψ_⊥ | H | δψ_⊥⟩ + 2 Re⟨ψ + δψ_∥ | H | δψ_⊥⟩|

Since H|_{V_λ} = (1−λ)I and (ψ + δψ_∥) ∈ V_λ while δψ_⊥ ∈ V_λ^⊥, the cross term vanishes (H is block-diagonal in the T eigenbasis). Therefore:

    B_repair = ⟨δψ_⊥ | H | δψ_⊥⟩ = Σ_{μ≠λ} (1−μ) ‖P_μ δψ‖²

The repair burden equals the energy content of the out-of-eigenspace component of the perturbation.

## Retired formulation

The state-distance definition B_old = ‖P_λ(ψ+δψ) − ψ‖²/‖ψ‖² is **retired**. It is nonzero for within-eigenspace perturbations and does not measure energy cost. Only the energy-projection form above is canonical.

---

## Proof-state

**EXACT STRUCTURAL.** Follows from the spectral decomposition of T and the block-diagonal structure of H in the T eigenbasis. No approximations, parameters, or conventions.
