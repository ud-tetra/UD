# THM-LS8: Retention Decay Rate

**Version 1.0 | Depends: THM-LS1 (retention fidelity R), THM-561 (T spectrum)**

---

## Statement

Let ψ = c₁|λ₁⟩ + c₂|λ₂⟩ be a superposition of two T eigenstates with eigenvalues λ₁ > λ₂ > 0 and |c₁|, |c₂| > 0. Then:

(i) R(ψ, n) → |c₁|² / ‖ψ‖² as n → ∞.

(ii) |R(ψ, n) − R(∞)| is O((λ₂/λ₁)^n) as n → ∞.

The retention fidelity converges to the weight of the dominant eigencomponent, with deviation decaying exponentially at rate γ = ln(λ₁/λ₂).

## Proof

T^n ψ = c₁ λ₁^n |λ₁⟩ + c₂ λ₂^n |λ₂⟩. Set q = λ₂/λ₁ < 1 and r² = |c₂|²/|c₁|².

⟨ψ|T^n ψ⟩ = |c₁|² λ₁^n + |c₂|² λ₂^n = |c₁|² λ₁^n (1 + r² q^n).

‖T^n ψ‖² = |c₁|² λ₁^{2n} + |c₂|² λ₂^{2n} = |c₁|² λ₁^{2n} (1 + r² q^{2n}).

R = (1 + r² q^n)² / ((1 + r²)(1 + r² q^{2n})).

As n → ∞: q^n → 0, so R → 1/(1 + r²) = |c₁|²/‖ψ‖². The leading correction is O(q^n).  □

## Verified

Equal-weight superposition (V₁ + V_{1/2}): deviation matches (1/2)^n to 6 significant figures at n = 20.

## Non-claims

This result does NOT define a threshold for "identity loss." It does NOT classify states by retention rate.

---

## Proof-state

**EXACT STRUCTURAL.** Eigenvalue arithmetic on the T spectrum. No conventions or parameters.
