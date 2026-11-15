# UD pre-event authorization and two-tetrahedron multimode gate v0.2

**Date:** 2026-11-15. **Research lane:** DEVELOPMENT — NO REGISTRY ENTRY. **Claim status:** EXACT_CONDITIONAL / CANDIDATE / NO-GO_SCOPED / OPEN_GATED. **Physical promotion:** **0**. **Historical target exposure:** March 2026 cosmology targets were previously known; this finite test uses no physical target values or fitting. **Successor to:** `UD_TWO_TETRA_NATIVE_SOURCE_GATE_v0.1` and `UD_NATIVE_MODE_PRODUCTION_COHERENCE_GATE_v0.1`; earlier files preserved.

## 1. Source boundary and problem

Historical recovered March files supply (i) face-admission `A_[ijk]=1−δ_{b_i b_j}δ_{b_j b_k}` (`triangular_transport_symbol_alphabet.md`, §3); (ii) seam transport `U_ij` and abelian reduction `U=e^{iqφ}` (`seam_phase_transport.md`, §§1,4); (iii) packet variables `(ρ,θ,χ)`, routing memory and a generic (not source-selected) update with coefficients (`packet_modulation_layer.md`, §§1–3); and (iv) a coarse field equation ansatz (`packet_field_equation.md`, §§1–4). These are **source strata**, not proof of a particular Markov transition law. The current `UD-Physics/state/CURRENT.md` and `experiments/g0506-packet-hodge-sourcegate/README.md` (2026-11-05) explicitly leave packet-to-Hodge map, absolute preparation, temporal connection, the G05 source map and G06 action units open. Nothing below changes their frozen scope.

**Question 1:** What can the finite carrier uniquely *authorize before an event* from admissibility, closure, local topology, stock positivity and seam phase? **Question 2:** Does the smallest conservative extension excite at least two distinct structural face modes with source-budget conservation and null controls?

## 2. Typed carrier, phase and clocks

Let `K = [0123] ∪ [0124]` be the filled oriented face-glued tetrahedral complex. Vertex set `V={0,1,2,3,4}`; edge set `E` has 9 elements; triangular-face set `F` has 7; two 3-simplices. Face ordering:

```
F = (012,013,014,023,024,123,124)
      c  L1  R1  L2  R2  L3  R3
```

The two exclusive three-face groups are `L=(013,023,123)` and `R=(014,024,124)`; shared face `c=012` is its own single slot. The binary distinction assignment is `b∈{0,1}^5`. Define `χ_L(b)=∏_{f⊂[0123]}A_f` and `χ_R(b)=∏_{f⊂[0124]}A_f`; this *all-face-closure indicator* is an explicit model definition, **not** a proof that historical branch `χ` has no additional components.

Introduce a nonnegative **face-stock** vector `x∈ℕ_0^7` with `∑_f x_f=M`. The stock is a dimensionless integer count, not physical mass, energy, or the raw gate `A_f`. The relative seam state is `d=θ_R−θ_L+a_LR (mod 4)`, represented by `U_d=i^d`. Under the local rephasing `θ_t→θ_t+ε_t`, `a_LR→a_LR+ε_L−ε_R`, `d` is invariant. This finite Z4 phase submodel is a **CANDIDATE choice** from the historical U(1)-like family. Native event-count parameter `s` has no calibrated unit.

## 3. Exact pre-event admissibility result and its limit

**EXACT:** Exactly six of 32 vertex strings satisfy `χ_L=χ_R=1`:

```
00111, 01011, 01100, 10011, 10100, 11000
```

A single-vertex flip from any of these six fails full face admissibility. The smallest possible nonidentity admissible Hamming move changes **two** vertex bits. The six Hamming-2 edges form two disjoint triangles (three-state complete graphs). The complement branches do not connect by these minimal moves. This follows by exact enumeration and also from the shared triangle's 2+1 distribution: the two apex bits must both equal the singleton shared-triangle bit. The minimum-move convention is an **added kinematic premise**; the historical source does not require choosing Hamming-2 moves over admissible Hamming-3/5 jumps or a simultaneous phase/burden update.

**SOURCE-BOUND AUTHORIZATION PREDICATE (not a rate):** For a proposed local face-stock move `f→g`, a necessary positive-stock, topology and closure gate is

`Adm_base(b,x;f,g) = χ_L(b)χ_R(b) · 1[x_f≥1] · 1[|f∩g|=2]`.

For a proposed minimal bit move `b→b'`, under the declared minimum-Hamming convention:

`Adm_bit(b→b') = 1[χ_L(b)=χ_R(b)=χ_L(b')=χ_R(b')=1]·1[Hamming(b,b')=2]`.

These predicates are evaluated on the **pre-event state plus a candidate destination**, not retrospectively fitted from an observed outcome. They determine which of the declared moves is *permitted*, **not** which occurs or at what rate. No original March equation selects unique probabilities, rates, a physical time unit, or even this minimum-move principle.

## 4. Explicit local transition candidate (not uniquely native)

The face adjacency graph joins two distinct faces exactly when they share an edge in `K`. There are six within-left/right edges (two K3 triangles) and nine *interface* edges (three matched L↔R, six c↔exclusive). For `f≠g`, set symmetric weights

```
w_fg(d)= 1       if f,g are exclusive faces of the same tetrahedron
         p(d)   if the adjacency touches the glued interface
         0       otherwise
p(d) = |1+U_d|²/4 = (1+Re U_d)/2 ∈ {1, 1/2, 0, 1/2}.
```

This first-harmonic interference gate is **CANDIDATE**, motivated by the squared norm of two equal-amplitude channels. Equality of those channels and the choice of intensity readout are *additional assumptions*. They are not forced by seam transport or closure. For an admitted `b`, define the face-stock part of a Markov generator on observables `f(x,b,d)`:

`(Q_stock f)(b,d,x)= ∑_(f~g, ordered) x_f w_fg(d)[f(b,d,x−e_f+e_g)−f(b,d,x)]`.

Add the assumed bit-sector generator `(Q_b f)(b,d,x)= ∑_(b':Hamming(b,b')=2, admitted)[f(b',d,x)−f(b,d,x)]` and phase diffusion `Q_d f= 1/2[f(d+1)+f(d−1)−2f(d)]` on `Z4`. The demonstration coefficients one and one-half set a **native example event-clock convention**, not energy/time normalization. The full candidate is `Q=Q_stock+Q_b+Q_d`. It acts on the `6×4×C(M+6,6)` finite state space. For `M=2`, there are **672 states**.

**EXACT under this specified generator:** Each event preserves `M`, and every rate is nonnegative. An occupied source loses exactly one stock while its destination gains one; bit and phase events leave stock unchanged. The normalized equilibrium measure is uniform across the 6 admitted `b`, uniform in 4 phases, and multinomial over face stocks `π(x)=(M!/∏x_f!)·7^(−M)`. Every transition satisfies detailed balance. The two b-components remain disconnected: no full phase-space irreducibility is claimed.

**NO-GO_SCOPED — native selection:** The phase-independent choice `p(d)=1`, first-harmonic `p(d)=(1+Re U_d)/2`, and strict-matching `p(d)=1[d=0]` are distinct nonnegative, gauge-covariant, closure-compatible conservative generators. The source also permits different positive donor laws and overall clock rates. All pass the stated structural gates. Thus neither the March rules nor the closed two-K4 geometry uniquely derive `Q` or its phase gate. An additional source action, constitutive principle, balance condition, or experimentally discriminating law is indispensable. This is *not* a claim that all possible enriched UD source laws are nonunique.

## 5. Exact multimode spatial spectrum from common source and readout

Let `H∈{0,1}^{7×9}` be the **unsigned** face–edge incidence matrix. The previous raw-independent-bit reference covariance is `C_raw=HHᵀ/16`. This matrix is a combinatorial reference, **not** automatically the covariance of the new stock field. Let `L(p)` be the weighted seven-face graph Laplacian from `w_fg`. Direct exact diagonalization gives

`spec L(p) = {0:1, 3p:1, 7p:1, (3+p):2, (3+3p):2}`.

The full matrices `C_raw` and `L(p)` do **not commute** for generic `p`; therefore no global one-to-one identification between their eigenspaces is asserted. Nevertheless, three explicit orthogonal, zero-sum vectors are simultaneous eigenmodes on the same seven-face basis:

| mode | vector (c,L1,R1,L2,R2,L3,R3) | `C_raw` eigenvalue | `L(p)` eigenvalue |
|---|---|---|---|
| `v` | `(0,1,-1,1,-1,1,-1)` | `1/4` | `3p` |
| `w` | `(0,1,-1,-1,1,0,0)` | `1/16` | `3+3p` |
| `u` | `(0,1,1,-1,-1,0,0)` | `3/16` | `3+p` |

For stock modes `Z_e(x)=e·x`, at the displayed stationary measure,

`E Z_e =0`, `Var Z_e = (M/7)||e||² >0`, and `Cov(Z_e,Z_e')=0` when `e⊥e'`.

**EXACT_CONDITIONAL:** Thus **at least two independently populated spatial face-stock modes** (`v` and `w`) exhibit distinct decay rates under the declared local candidate, and they align with two distinct `C_raw` structural eigenspaces. This advances beyond the previous rank-one seven-face readout by adding independent face-stock occupancy degrees of freedom. It does **not** derive those added degrees of freedom from historical UD nor establish physical mode production.

### Frozen phase d=1

At `U=i`, `p=1/2` and `Q_d` switched off, the normalized stationary autocorrelations are

`R_v(s)=exp(−3s/2)`, `R_w(s)=exp(−9s/2)`, `R_u(s)=exp(−7s/2)`.

The distinct rates are structural consequences of the **candidate** graph generator and **not** physical relaxation times.

### Dynamical seam phase

With `d` performing the declared symmetric nearest-neighbor Z4 walk, let `L_d` be its 4×4 phase Laplacian (diagonal `−1`, nearest neighbors `1/2`), and `p_d=(1,1/2,0,1/2)`. Each shared mode has an exact 4-phase Feynman–Kac block `B_e = L_d−diag(λ_e(p_d))`. In particular

`B_w=B_v−3I` **EXACT**, so for every `s≥0`:

`R_w(s)=e^(−3s) R_v(s)`.

This identity holds for the assumed phase diffusion rate and also for a general common phase generator, provided the two mode eigenvalue functions differ by exactly 3. With the normalized initial phase-uniform stationary distribution,

`R'_v(0)=−3/2`, `R''_v(0)=27/8`;
`R'_w(0)=−9/2`, `R''_w(0)=171/8`.

**NUMERICAL (matrix exponential, native s=1):** `R_v(1)=0.3299920370849191`, `R_w(1)=0.016429336111197713`, ratio `e^(−3)=0.04978706836786441`. The entire exact identity, stationary covariance, local flux and derivatives were independently checked by a stdlib-only Fraction replay.

## 6. Negative controls, attempted falsification and interpretation limits

- **Admissibility:** all 672 constructed states retain full face admission; 6-state minimal-bit graph has six Hamming-2 edges and *zero* admissible single-bit edges. Alternate Hamming-3/5 move rules remain possible and unselected.
- **Conservation:** exact positive rates and `∑x_f=M` on every stock transition; stationary detailed balance checked over **all 672 states** and their 6972 directed transitions. An excluded source cannot contribute positive transfer.
- **Phase-gauge compensation:** exhaustively checked every `θ_L, θ_R, a_LR, ε_L, ε_R ∈ Z4`; `d` and `p(d)` invariant.
- **Seam off, p=0:** cross-interface transfers vanish. `v` becomes conserved (`R_v=1`), while intra-cell `w` still decays (`R_w=e^(−3s)`). A no-transfer seam is not an empty local graph.
- **Phase-blind p=1:** `R_v=e^(−3s)` and `R_w=e^(−6s)`, proving **mode splitting by itself does not demonstrate phase dependence**; only a phase sweep with controls can show that.
- **Quenched d=1:** distinct conditional rates above. It cannot be interpreted as a derived clock.
- **Closure sham:** artificially set the right-cell closure flag to 0, then all transition edges incident on the R-exclusive group are forbidden while left-exclusive K3 transfer remains. This is an *external sham control*, not a real member of the admitted six-bit state space.
- **Empty stock, M=0:** all stock rates vanish; phase and bit transitions may still occur. No spontaneous birth exists in this closed conservative model.
- **Isolated vertex:** adding a detached vertex changes a uniform-per-vertex tick count (and its `1−4/N` response) but does not change this face graph or its mode rates, exposing the danger of equating event count with a physical time scale.
- **Raw covariance is not dynamical covariance:** shared basis and common eigenvectors do not identify their probability laws. Only the new multinomial stock covariance was used to calculate dynamic mode amplitudes.

**Discriminating physical bridge still OPEN:** choose a *native* pre-event transition rule selecting the internal face-stock registers, bond weights, phase reference, active spectrum and rate; prove its conservation/selection and persistence. Then specify a physical wave-number/readout and clock/units with uncertainty, freeze predictions before unseen data, and pass nonconstructor/independent tests. The current two-cell model has no k continuum, calibrated metric, photon energy or primordial tensor observable; its relaxation spectrum cannot establish cosmological `n_s` or electromagnetic `α`.

## 7. Reproduction / governance

- `python verify.py` performs SymPy exact incidence/spectral checks, 672-state exhaustive Fraction reversibility/conservation tests, and a SciPy matrix exponential. Results: `results.json`.
- `python replay_stdlib.py` independently verifies raw 5-bit covariance, shared eigenvectors, phase-specific rates, stock detailed balance and short-time moments in Python standard-library Fraction arithmetic only. These are two implementations in the same authoring context, not nonconstructor review.
- All generated outputs are synthetic/exact conditional. No experimental observations or held-out samples were consumed.
- This is a new **development branch**. It does not supersede frozen G05/G06 or any earlier NO-GO theorem, nor does it claim an actually source-selected native event law. Original March files and v0.1 reports remain intact.

**Status:** EXACT_CONDITIONAL multimode result; NO-GO_SCOPED native-source uniqueness; OPEN_GATED source selection, physical bridge and review. **Physical promotion = 0**.
