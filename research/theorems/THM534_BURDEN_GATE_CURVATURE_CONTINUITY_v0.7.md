# THM-534 — Native Burden-Gate Curvature and Continuity Audit v0.7

**Date:** 2026-10-21  
**Scope:** fixed filled tetrahedron K=Δ³; discrete normalized relaxational vertex-burden lane, unsigned hard gates, oriented simplicial currents.  
**Status:** EXACT CONDITIONAL / NO-GO / OPEN_GATED. Development / no registry promotion. Physical promotion = **0**.  
**Provenance:** `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, Q153 (source/sink accounting), Q155 (internal redistribution), Q156 (hard gate `h_e`), Q158 (residual source receipt), Q162 (normalized relaxational mixing edge current), Q169–173 (separate skew/Hasse support continuity). Companion: THM534_COVARIANT_SOURCE_CONTINUITY_v0.6.md and THM534_QUADRATURE_FLUX_TYPING_AMENDMENT_v0.6.1.md. Original THM-534 Markov weights remain SOURCE-BLOCKED.

## 1. Typed objects and rule

K is the **complete filled oriented tetrahedron** on vertices 0,1,2,3 with oriented edges 01,02,03,12,13,23 and oriented triangular faces 012,013,023,123. Signed boundary maps are `B1:C1→C0`, `B2:C2→C1`, `B3:C3→C2`, with `B1B2=B2B3=0`, under unit simplex-chain inner products. The edge-to-vertex graph is the full K4 independent of gate settings.

- `ρ ∈ (ℝ_{≥0})⁴` is dimensionless **vertex burden stock** in the normalized relaxational model, **not** physical mass-energy, the complex 15D amplitude vector ψ, or its squared norm.
- `h_e=C_cl,e^hard T_int,e^hard∈{0,1}` are hard edge conductance/admissibility bits from legacy Q156. **Their governing state-to-gate map remains OPEN**; a displayed pattern does not prove an admitted UD closure configuration.
- `H=diag(h_e):C1→C1` is an unsigned gate operator. Under edge-orientation changes, the signed edge-basis coordinates are updated covariantly while H remains diagonal.
- `j_B=−(1/4) H B1ᵀρ ∈C1` is the previously admitted **Q162 normalized relaxational current**, with the dimensionless coefficient 1/4 applicable to this declared model only. It is not the separate Q163 mixing normalization or a physical velocity/time law.
- Choose the **new conditional discrete one-attempt update** `ρ'=ρ+B1 j_B`. The continuous-time analogue is `dρ/ds=B1 j_B` with s an uncalibrated mathematical event parameter; identifying an exact finite physical duration is not authorized.
- `F_face=B2ᵀ j_B∈C²` is a signed oriented **face-circulation two-cochain**, not the v0.6 operator defects `F_down=B1N∈Hom(C2,C0)` and `F_up=NB3∈Hom(C3,C1)`.

This new candidate is **not** a recovered physical seam action. The complete burden stock (sum of vertex ρ) is conserved under the closed model because the single current is internal. No physical radiation/vacuum/latent reservoirs are silently inserted.

## S18 — Total burden continuity, positivity and event-time contraction (EXACT CONDITIONAL)

For any gate mask `0≤h_e≤1` and any nonnegative ρ, set `L_H=B1 H B1ᵀ` and `P_H=I₄−L_H/4`. Then `ρ'=P_Hρ` is nonnegative and conserves total burden:

`1ᵀρ'=1ᵀρ`, `P_H≥0` entrywise, `P_H1=1`, `1ᵀP_H=1ᵀ`.

**Proof.** Every off-diagonal entry is `(P_H)_{uv}=h_{uv}/4≥0`; the diagonal is `1−deg_H(u)/4≥1/4` because K4 has degree 3 and `h≤1`. All row/column sums are one because `1ᵀB1=0`, and P is symmetric. Moreover `0≤L_H≤L_K4=4I−J` in the Loewner order, so the eigenvalues of P lie in [0,1]. Hence `||ρ'−ρ̄1||₂≤||ρ−ρ̄1||₂`, where `ρ̄=(Σ_vρ_v)/4`. These statements hold on every step with possibly state/history-dependent H so long as it satisfies the same bounds. QED.

**Scope:** symmetric stochastic preservation of dimensionless vertex burden is an *internal mathematical continuity theorem*, not mass-energy conservation or a source/sink law for open packet environments. No physical time or calibrated rate follows.

## S19 — Exact face circulation, discrete closure, and the Hodge current split (EXACT)

For any edge current `j∈C1`, define node redistribution `δρ=B1j` and face circulation `F=B2ᵀj`. Then

`1ᵀδρ=0`, `B3ᵀ F=0`, and `4 ||j||² = ||δρ||²+||F||²`.

**Proof.** The first is `1ᵀB1=0`; the second is `(B2B3)ᵀj=0`. The last follows from the fixed filled-tetrahedron identity `B1ᵀB1+B2B2ᵀ=4I₆` by taking the quadratic form against j. QED.

This is a strict *orthogonal Hodge norm decomposition*, not an exchange of physical energy from redistribution into curvature and not the chain-amplitude current of v0.6.

## S20 — Nonuniform hard-gating criterion and universal flat-mask no-go (EXACT / NO-GO)

With Q162 current, `F_face=−(1/4)B2ᵀ H B1ᵀρ`. For any oriented face `(a,b,c)` with `a<b<c`,

`F_{abc}=−(1/4)[(h_ac−h_ab)ρ_a+(h_ab−h_bc)ρ_b+(h_bc−h_ac)ρ_c]`.

It follows that **`F_face=0` for every vertex burden ρ if and only if all six edge gate weights are equal.**

**Proof.** The formula follows from the oriented face boundary `∂[abc]=[bc]−[ac]+[ab]`. Vanishing for *every* independent ρ_a,ρ_b,ρ_c forces `h_ab=h_ac=h_bc` on each face. The four triangles of K4 overlap in edges, so the equalities propagate to all six edges. Conversely `H=hI` gives `F=−h B2ᵀ B1ᵀρ/4=0` by `B1B2=0`. QED.

For binary gates there are only **two** masks flat as operators: all-off and all-on. Any nonuniform mask admits **some** initial burden generating nonzero face circulation; it need not do so for every particular ρ. The result is restricted to this gradient-current law. A different source law might yield circulation under uniform gates.

## S21 — Explicit nonzero sourced-curvature and conservation witness (EXACT CONDITIONAL)

Use `ρ=(1,0,0,0)ᵀ`, with `h_01=0` and all other edge gates one. In edge order `01,02,03,12,13,23` and face order `012,013,023,123`, the exact current and receipts are

`j_B=(0,1/4,1/4,0,0,0)ᵀ`,

`ρ'=(1/2,0,1/4,1/4)ᵀ`,

`F_face=(−1/4,−1/4,0,0)ᵀ`.

Consequently `Σρ'=Σρ=1`, `B3ᵀF_face=0` and

`4||j_B||²=1/2=3/8+1/8=||B1j_B||²+||F_face||²`.

All coordinates are nonnegative and the source/circulation are nonzero. These are exact fraction calculations. **The mask itself is a conditional Q156-compatible binary pattern, not an independently demonstrated outcome of the still-OPEN gate-selection dynamics.** A refused transport edge does not delete that edge from the underlying simplicial chain complex.

## S22 — Burden conservation does not uniquely determine physical seam phase (EXACT / NO-GO)

The rules for `ρ'` and `F_face` do not supply a map `C²→U(1)` with a selected angular normalization or a physical current/charge unit. For any real scale κ, one can define the **candidate** edge phase `u_e(κ)=exp(iκ j_e)`, yielding face holonomy `W_f(κ)=exp(iκ F_f)`, with the same exact burden-conservation receipts for all κ. In the S21 example, κ=0 gives trivial holonomy and κ=1 gives `exp(−i/4)` on the two nonzero faces. Thus mass/burden continuity and source-free cochain closure alone cannot select unique non-flat **U(1)** holonomy or recover historical THM-534 transition probabilities. QED.

If κ is given physical dimensions, a native burden/time/action conversion is separately required. The face cochain `F_face` is exact and obeys `B3ᵀF=0`, so the product of oriented face holonomies around the tetrahedral boundary is one for every κ: there is no magnetic-monopole or non-Abelian curvature claim here.

## 2. Exhaustive exact verification and claim states

`verify_thm534_burden_gate_curvature_v0_7.py` (Python + SymPy) checks: full chain identities, Hodge split, 64 binary gate masks × four unit-burden inputs, positivity and double stochasticity, spectral contraction, discrete face closure, six edge-orientation gauge flips, flat masks, and the S21 witness. Constructor execution PASS. Rank distribution for `B2ᵀHB1ᵀ`: rank 0—2 masks, rank 1—12, rank 2—38, rank 3—12. Numeric fitting is absent.

- **EXACT CONDITIONAL:** S18 and S21 for Q162 and the separately declared one-attempt update, with fixed topological carrier.
- **EXACT:** S19 algebraic identities; S20 gate-uniformity criterion; S22 normalization underdetermination.
- **OPEN_GATED:** derive hard gate mask from `(ρ,θ,χ,σ,b)` and packet boundary/contact state; validate Q162 beyond the normalized relaxational lane; derive U(1) phase conversion, physical action/time, explicit reservoirs if open, and a stochastic/Born edge readout.
- **NO PROMOTION:** do not substitute `F_face` for the v0.6 covariant operator defect or for physical stress-energy curvature. Do not identify Q162 with distinct Q163 clock/normalization. Physical promotion remains **0**.

**Exposure:** historical THM-534 target was known; this is target-exposed exploration, not blind confirmation. Independently verifiable mathematics is not independent *review*: non-constructor review PENDING. The originating `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39` is a historical provenance source, not proof of a unique current physical constitutive law.