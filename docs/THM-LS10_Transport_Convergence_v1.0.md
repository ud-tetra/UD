# THM-LS10: Transport Convergence Rate

**Version 1.0 | Depends: THM-534 (transport matrix T), THM-561 (T spectrum), THM-LS4 (spectral projector)**

---

## Statement

Let P₁ be the rank-1 orthogonal projector onto the eigenspace V₁ (λ = 1). Then:

    ‖T^n − P₁‖₂ = (1/2)^n

where ‖·‖₂ is the operator (spectral) norm.

## Proof

T = P₁ + (1/2)P_{1/2} + (1/3)P_{1/3} (spectral decomposition). Therefore:

T^n − P₁ = (1/2)^n P_{1/2} + (1/3)^n P_{1/3}.

The operator norm of a sum of orthogonal projectors scaled by distinct coefficients is the maximum coefficient:

‖T^n − P₁‖₂ = max((1/2)^n, (1/3)^n) = (1/2)^n.  □

## Corollary

Every initial state ψ converges under iterated transport to its projection onto V₁:

    ‖T^n ψ − P₁ ψ‖ ≤ (1/2)^n ‖ψ‖

The convergence rate is set by the second-largest eigenvalue λ₂ = 1/2, independent of the initial state.

## Verified

Operator norm ‖T^n − P₁‖₂ matches (1/2)^n to machine precision for n = 1, 5, 10, 20.

## Non-claims

This result does NOT interpret convergence as "decoherence" or "thermalization." It states only the rate at which T^n approaches a rank-1 operator.

---

## Proof-state

**EXACT STRUCTURAL.** Spectral decomposition and operator norm computation. No approximations or conventions.
