# THM-LS7: Repair Cost Ordering

**Version 1.0 | Depends: THM-LS2 (repair burden), THM-LS3 (degenerate zero cost), THM-561 (T spectrum)**

---

## Statement

Define the repair cost matrix C on the three T eigenspaces {V₁, V_{1/2}, V_{1/3}} by:

    C(λ → μ) = (1 − μ)    for μ ≠ λ
    C(λ → λ) = 0

Then:

**(i)** C depends only on the target eigenspace μ, not the source λ.

**(ii)** The diagonal vanishes: C(λ → λ) = 0 for all λ. (THM-LS3.)

**(iii)** The off-diagonal costs are strictly ordered:

    0 = C(→V₁) < C(→V_{1/2}) = 1/2 < C(→V_{1/3}) = 2/3

**(iv)** The repair cost rank ρ(V_μ) = 1 − μ equals the Hamiltonian eigenvalue of H = I − T restricted to V_μ.

## Proof

(i) From THM-LS2: B_repair = Σ_{μ≠λ} (1−μ) ‖P_μ δψ‖². For a unit perturbation entirely in V_μ (i.e., P_μ δψ = δψ with ‖δψ‖ = 1), only the μ-term survives: B = (1−μ). This is independent of the source eigenspace λ.

(ii) THM-LS3: within-eigenspace perturbations have B = 0.

(iii) The eigenvalues satisfy 1 > 1/2 > 1/3 > 0. Applying 1 − (·): 0 < 1/2 < 2/3.

(iv) H|_{V_μ} = (I−T)|_{V_μ} = (1−μ)I_{dim V_μ}. For any unit ψ ∈ V_μ: ⟨ψ|H|ψ⟩ = 1−μ = ρ(V_μ).  □

## Explicit cost matrix

|  | → V₁ | → V_{1/2} | → V_{1/3} |
|---|---|---|---|
| V₁ | 0 | 1/2 | 2/3 |
| V_{1/2} | 0 | 0 | 2/3 |
| V_{1/3} | 0 | 1/2 | 0 |

Each column is constant (except the diagonal zero). The target determines the cost.

## Structural consequence

The three eigenspaces carry a total order by repair cost rank:

    V₁ (ρ = 0) < V_{1/2} (ρ = 1/2) < V_{1/3} (ρ = 2/3)

This order is identical to the energy ordering under H = I − T. The repair cost rank and the Hamiltonian eigenvalue are the same quantity.

## Non-claims

This result does NOT identify V₁ as "vacuum," V_{1/2} as "weak," or V_{1/3} as "color." It does NOT claim the ordering constitutes an ontological hierarchy. It does NOT assign any threshold or classification. The connection between repair cost ordering and physical stability is a separate bridge claim.

---

## Proof-state

**EXACT STRUCTURAL.** Follows from T eigenvalues {1, 1/2, 1/3} (THM-561), the repair burden formula (THM-LS2), and arithmetic. Verified computationally: all matrix entries match, column constancy confirmed, Hamiltonian eigenvalue agreement confirmed (3/3 checks pass). No approximations, conventions, or parameters.
