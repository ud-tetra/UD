# THM-566: Yukawa Singular Value Ratio √3

**Version 1.0 | Depends: THM-561 (P_± decomposition), THM-563a (four-sector chirality), THM-565a (nonzero Higgs element), THM-LS9 (S₄ irreps), THM-LS12 (eigenvalues)**

---

## Statement

The 2×2 Yukawa matrix Y(θ) = ⟨L_i|H_j(θ)|R⟩, where L₁, L₂ span P_L∩P_+, R spans P_R∩P_+, and H_j(θ) are the two Higgs modes connecting V₁ to an arbitrary ONB of V_{1/2}, satisfies:

(i) det(Y) = 1/(3√3), independent of θ.

(ii) tr(YᵀY) = 4/9, independent of θ.

(iii) The singular values are σ₁ = 1/√3 and σ₂ = 1/3.

(iv) The singular value ratio is σ₁/σ₂ = √3.

## Proof

Work in the P_+ dimension basis {|+,1⟩, |+,2⟩, |+,3⟩} where the Hodge star acts as diag(+1,−1,+1). Then P_L∩P_+ = span{|+,1⟩, |+,3⟩} and P_R∩P_+ = span{|+,2⟩}. The vacuum V₁ = (1,1,1)/√3. Any ONB of V_{1/2} (trace-zero in P_+) is parameterized by angle θ using the standard basis {(1,−1,0)/√2, (1,1,−2)/√6}.

The Yukawa matrix factors as Y = (1/√3)M(θ) where M(θ) has:

- tr(MᵀM) = 4/3 (the row-pair norms each equal 2/3; cross-terms cancel by trigonometric identity)
- |det(M)| = 1/√3 (the sc terms cancel leaving 2/(√6·√2) = 1/√3)

Both quantities are θ-independent. The singular values of M satisfy σ² − (4/3)σ² + 1/3 = 0, giving σ₁² = 1, σ₂² = 1/3. Therefore σ₁/σ₂ = √3.  □

## Non-claims

This result establishes the singular value ratio of the Higgs coupling matrix. It does NOT claim that this ratio equals any specific quark mass ratio — the identification of singular values with physical masses is a separate bridge step.

---

## Proof-state

**EXACT STRUCTURAL.** Follows from the inner product geometry of P_+ under the (*, T, S) algebra. All quantities are θ-independent and verified by direct computation (1000-point scan confirms invariance). No parameters, conventions, or physical identifications.
