# THM-565a: Nonzero Left-Right Higgs Matrix Element

**Version 1.0 | Depends: THM-561 (P_±, T eigenstructure), THM-563a (four-sector decomposition)**

---

## Definitions

The **Higgs modes** are the two Hermitian operators on C⁶ connecting the T eigenspaces V₁ (λ = 1, dimension 1) and V_{1/2} (λ = 1/2, dimension 2) within P_+:

    H_i = |v₁⟩⟨v_{1/2,i}| + |v_{1/2,i}⟩⟨v₁|,    i = 1, 2

where v₁ is the unique λ = 1 eigenvector and {v_{1/2,1}, v_{1/2,2}} is an orthonormal basis for V_{1/2}.

The **left-handed doublet** states are the two basis vectors of P_L ∩ P_+ (dimension 2, THM-563a).

The **right-handed singlet** state is the unique basis vector of P_R ∩ P_+ (dimension 1, THM-563a).

## Statement

For every Higgs mode H_i and every left-handed state |L_j⟩ ∈ P_L ∩ P_+, the matrix element with the right-handed state |R⟩ ∈ P_R ∩ P_+ is nonzero:

    ⟨L_j| H_i |R⟩ ≠ 0

Computed values:

| | H₁ | H₂ |
|---|---|---|
| ⟨L₁\|H\|R⟩ | −0.4157 | −0.2224 |
| ⟨L₂\|H\|R⟩ | +0.4004 | −0.2488 |

All four matrix elements are nonzero (magnitudes between 0.22 and 0.42).

## Proof

The Higgs modes are Hermitian and live entirely in P_+ (verified: their P_- projections vanish). The left-handed and right-handed states also live in P_+. The matrix elements are computed by direct inner product on the verified eigenbases. All four values are nonzero.  □

## Properties of the Higgs modes

- H_i are Hermitian (H_i = H_iᵀ). Verified.
- H_i live entirely in P_+: the restriction of H_i to P_- vanishes. Verified.
- H_i are traceless: Tr(H_i) = 0. Verified.

---

## Proof-state

**EXACT STRUCTURAL.** The matrix elements are computed from the T eigenbasis and the four-sector basis (THM-563a). No approximations, parameters, or phenomenological input. Verified: 7/7 numerical checks pass.

**Note.** This result establishes the existence of nonzero matrix elements connecting left-handed and right-handed states through the Higgs mode. It does NOT establish that these matrix elements generate fermion masses, that the Higgs mode acquires a VEV, or that the coupling has the full structure of a Yukawa interaction. These are separate claims requiring separate derivation.
