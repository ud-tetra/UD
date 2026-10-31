# UD Tetrahedral Spacetime: Four-to-Three Folding, Time, Twist, and Conservative Remeshing

**Artifact:** `UD_TETRAHEDRAL_SPACETIME_4_OVER_3_FOLD_AND_ENERGY_AUDIT_v0.5`  
**Date:** 2026-10-31  
**Status:** DEVELOPMENT — NO REGISTRY ENTRY. Theorems tagged EXACT apply only under explicitly stated mathematical assumptions.  
**Physical promotion:** **0**. Not a native UD spacetime derivation, a physical energy law, or a GR recovery.  
**Task:** Continue native apex-creation/twist Workload 1, incorporate the user's tetrahedral 3+1 spacetime folding proposal, and produce a counterexample-safe, exactly conservative cubical-to-simplicial construction.

## 0. Source strata, precedence and objects

Controlling sources:

- `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (2026-08-22), rows **F01–F05**: dimensional frame ratios and locked `R_3^(tet-face)=4/3` under its own dyad definition; **P01–P09**: K4 packet structure; **G05**: master loop-action coefficient OPEN; **Q153–Q154**: burden incidence and typed source/sink bookkeeping (constitutive laws OPEN); **Q165–Q179**: exact support conservation on a *fixed* `C0 ⊕ C1 ⊕ C2 ⊕ C3` carrier and global gluing, with open-system/source semantics OPEN. `R_3^(tet-face)=4/3` is *not* silently identified with physical dimensionality or the independently constructed tight frame below.
- `UD_K4_K5_NATIVE_BIRTH_J34_CURVED_METRIC_AUDIT_v0.3.md` (2026-10-31), §§1–2: fixed-carrier no-go, shell/fill versus 3D stellar subdivision, curved apex transport controls, variable-length Gram gate.
- `UD_K4_K5_OMEGA_APEX_TWIST_VERIFY_v0.4.py` (2026-10-31), verified afresh: 94 exact assertions, shell/stellar/fill branch split, finite orientation transport/twist controls. The first two modes are mathematical models rather than source-derived omega_0 dynamics.
- UD repository `ud-tetra/UD` README and AGENTS.md (retrieved 2026-10-31); designated portal https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/ (retrieved 2026-10-31, Papers I–III 1.1.1 / IV 0.1, physical promotion 0, independent review pending).
- External **comparison only**: Einstein Toolkit 3+1 documentation `https://www.einsteintoolkit.org/arrangementguide/EinsteinExact/documentation.html`; NIST FiPy finite-volume conservation `https://pages.nist.gov/fipy/en/latest/numerical/discret.html`; Cambridge GR lecture on local/global energy conservation `https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html`. These are not imported UD primitives.

**Typed objects:** `K4` = complete graph on four vertices; `Δ³` = *filled* 3-simplex (tetrahedral cell); `Σ³` = three-dimensional spatial simplicial complex; `M⁴` = 3+1 spacetime complex or smooth manifold; `Δ⁴` = 4-simplex **not** automatically Lorentzian; `z∈R⁴` = four-channel **amplitude vector** (not necessarily four spacetime coordinates); `x∈R³` = spatial channel readout; `q∈R` = orthogonal singlet channel (not physical clock or energy); `ε` = test energy density on spatial geometry; `S_mu` = UD support stock (distinct from `E`); `B` = native burden (distinct from energy); `U_e` = orientation/transport group element (distinct from metric).

## 1. EXACT: 4/3 tetrahedral tight-frame theorem and lossless full folding

Let four tetrahedral unit vectors be

\[
 n_1=\frac{(1,1,1)}{\sqrt3},\quad n_2=\frac{(1,-1,-1)}{\sqrt3},\quad
 n_3=\frac{(-1,1,-1)}{\sqrt3},\quad n_4=\frac{(-1,-1,1)}{\sqrt3}.
\]

For `N=[n_1\;n_2\;n_3\;n_4]∈R^{3×4}`, direct multiplication gives

\[
 \sum_{a=1}^4n_a=0,\qquad NN^{\mathsf T}=\frac43I_3.
\]

Therefore for all `x∈R³`,

\[
 \boxed{ x=\frac34\sum_{a=1}^4n_a(n_a\cdot x),\qquad
 \|x\|_2^2=\frac34\sum_{a=1}^4(n_a\cdot x)^2.}
\]

This is a mathematically exact 4-channel representation of three spatial components. `4/3` is its frame bound and `3/4` the exact reconstruction coefficient. The numerical equality to ledger F03 suggests a **typed comparison**, not an identification of the operators without recovering the frozen dyad's normalization/domain.

For an invertible split of **all** four amplitude channels, let

\[
T=\frac12\begin{pmatrix}
1&1&1\\1&-1&-1\\-1&1&-1\\-1&-1&1
\end{pmatrix},\qquad
u=\frac12(1,1,1,1)^{\mathsf T}.
\]

Then `T^T T=I3`, `T^T u=0`, `TT^T+uu^T=I4`. The matrix `Q=[T\;u]` is orthogonal. For **every** `z∈R⁴`, define `x=T^T z` and `q=u^T z`. Then

\[
\boxed{z=Tx+uq,\qquad \|z\|_2^2=\|x\|_2^2+q^2.}
\]

The spatial readout alone loses the `q²` contribution unless `q=0`. The **complete** (3+1) typed readout `(x,q)` is invertible and quadratic-stock conserving.

**Symmetry:** For every `P∈S₄` permuting the four channels, `Pu=u` and `PT=TR_P`, where `R_P=T^TPT∈O(3)`. Exactly 12 `P` induce `det(R_P)=+1` and 12 induce `det(R_P)=-1`. All 24 were verified exactly. The singlet `q` is invariant under *relabeling*, but this does **not** establish persistence under the native update law.

**Full energy tensor caution:** For `E_M(z)=z^T M z/2` with arbitrary positive-definite channel metric/mass matrix `M`, energy is preserved **only if** one transforms the full tensor:

\[
E_M(z)=\tfrac12(x,q)^{\mathsf T}\,Q^{\mathsf T}M Q\,(x,q).
\]

The mixed `x–q` terms generally do not vanish. `M=diag(1,2,3,5)` is a verified counterexample to blindly using scalar `||x||²+q²` for a nonuniform energy form. No UD energy interpretation of the quadratic stock has been derived.

## 2. CANDIDATE: a Lorentzian sign without pretending it was derived

The channel-space tensor

\[
 \eta_{\rm cand}:=TT^{\mathsf T}-uu^{\mathsf T}=I_4-2uu^{\mathsf T}
\]

has the exact eigenvalues `{-1,1,1,1}` and is invariant under the four-channel `S₄` permutations. It creates the formal interval

\[
 ds^2_{\rm candidate}=\|dx\|^2-dq^2.
\]

**Important:** The minus sign is a **chosen** Lorentzian signature, not a result of the Euclidean `4/3` frame identity or the UD action. A regular Euclidean pentachoron and a Lorentzian spacetime simplex cannot be related through a real coordinate change alone (Sylvester's law of inertia). Physical time requires independent causal propagation, chronology, clock/unit calibration and dynamical laws. The `q` channel might be *proposed* as an order/phase/persistence slot, but no physical meaning is established.

## 3. EXACT: tetrahedral spatial slices and 4-simplex spacetime slabs

Take a three-dimensional tetrahedral spatial cell `τ=Δ³` with volume `V_3`. Its prism over a single event interval `I=[n,n+1]` is topologically `τ×I` and is a four-dimensional combinatorial manifold with boundary. It admits a standard triangulation into exactly four 4-simplices:

\[
S_k=\operatorname{conv}((v_0,0),\ldots,(v_k,0),(v_k,1),\ldots,(v_3,1)),\qquad k=0,1,2,3.
\]

For a unit coordinate interval, each has 4-hypervolume `V_3/4`. Thus `Σ_{k=0}³ Vol4(S_k)=V_3`. For the reference unit tetrahedron, each is `1/24` and total `1/6`; independently checked exact determinants. This is a **discrete evolution slab**, not spontaneous generation of a four-dimensional spatial universe. Event `n` is an ordering index, **not** measured seconds.

For comparison, the unit spatial cube admits six tetrahedra, each volume `1/6`. The four-dimensional coordinate hypercube admits 24 4-simplices, each hypervolume `1/24`. These are explicit coordinate-order/Freudenthal triangulations; they are not statements that standard physics regards spacetime as a cube.

A physically meaningful smooth spacetime is described on a 3+1 foliation by

\[
 ds^2=-N^2dt^2+h_{ij}(dx^i+\beta^i dt)(dx^j+\beta^jdt),
\]

where `h` is a 3-metric, `N>0` lapse, and `β` spatial shift. Even knowing `h` at one slice cannot reconstruct the full metric `g` without `N,β`, nor determine gravitational evolution without relevant extrinsic-curvature/matter data. In the exact test: `h=diag(4,9,25)`, `N=7`, `β=(1/2,1/3,1/5)`, yielding `det(g)=-44100` and unit timelike normal. Different lapse/shift values yield **the same spatial h** but different `g`: an explicit no-go for metric-only reversible folding.

## 4. EXACT: no-energy-loss conversion of cubical spatial geometry

For any integrable scalar energy-density observable `ε` on the unit cube `C³`, its exact six-tetrahedron partition `T_i` satisfies

\[
 \boxed{ E(C^3)=\int_{C^3}\epsilon(x)\,d^3x
 =\sum_{i=1}^{6}\int_{T_i}\epsilon(x)\,d^3x. }
\]

This is measure additivity, not a new conservation law. A change of variables to a single deformed tetrahedron would instead require the full Jacobian factor, not a claim of Euclidean isometry. There is **no theorem** that a cube and regular tetrahedron are globally Euclidean-isometric.

For the declared exact **test density** `ε=1+x+2y+3z` on `C³=[0,1]³`, direct cubical integration and separate simplex barycentric quadrature both give

\[
E=4,\quad (E_1,\ldots,E_6)=\left(\frac7{12},\frac58,\frac58,\frac{17}{24},\frac{17}{24},\frac34\right).
\]

Sum is exactly `4`. This demonstration's number `4` is a **test result**, not a source-derived `G_1`, a dimensional constant, or evidence for the 4/3 coframe hypothesis.

**Source-free 3D apex birth:** Add an internal barycentric vertex to one tetrahedron, replacing one tetrahedral 3-cell by four tetrahedra. If the old cell is the coordinate unit tetrahedron, every child has one-quarter the parent volume. The same affine density yields parent energy `5/12` and child energies `(23/192, 7/64, 19/192, 17/192)`, summing exactly to `5/12`. The original three-dimensional region is unchanged. This is a **mathematically executable topology-changing spatial remesh** but not an energy-driven native UD growth event.

A nontrivial conservative transfer rule on the six-cell mesh is

\[
 E_i^{(n+1)}=E_i^{(n)}+\alpha\sum_{j\sim i}\big(E_j^{(n)}-E_i^{(n)}\big).
\]

Every internal face contributes equal and opposite exchange to the two cells, so `Σ_i E_i` is invariant in a closed domain. The test sets `α=1/12` **strictly as a protocol control**. All twelve exact updates preserved `E_total=4` and positive cell energies. This proves **designed model conservation**, not the UD native constitutive law.

**Dimensional-typing warning:** Integrating an energy density across `d^3x dt` yields energy×time (up to lapse/units), not a conserved spatial-slice energy. The four-dimensional test integral of `1+x+2y+3z+t` is `9/2`; it is *not* the energy on a time slice.

## 5. EXACT/NO-GO: twists can hide transport information, not automatically a geometric coordinate

Define a bundle-valued transport around a noncontractible spatial loop with local 3-frame holonomy

\[
R=\operatorname{diag}(-1,1,1),\qquad R^{\mathsf T}I_3R=I_3,\qquad\det R=-1.
\]

Scalar metric measurements cannot distinguish `R` from the identity at the base point; an oriented or parallel-transported observable can. An `SU(2)` double-cover comparator likewise has a `2π` spinor lift of `-I₂` and `4π` lift of `+I₂`, while the corresponding 3-vector direction returns after `2π`.

**Critical distinction:** A holonomy twist is additional orientation/phase information in the connection or internal frame. It does **not prove** an additional geometric dimension. A nontrivial globally flat Z₂ twist on the *simply connected* fully triangulated pentachoron shell is obstructed. Previous v0.4 exhaustive enumeration checked all `2^10` binary edge assignments; all 16 flat assignments were pure gauge. Protected global twist requires different topology, whereas curved transports may contain local mismatch.

The user's 'persistence' should be modelled provisionally as a **history/state readout**, e.g. `P(n0,n1)=∏_{n=n0}^{n1-1}Adm(X_n)`, not automatically a second time coordinate. Otherwise `three spatial + time + independent smooth persistence` is **five** mathematical coordinates, not four. Distinguish packet update count, clock calibration, and retained state.

## 6. NO-GO: generic GR does not have a globally conserved scalar energy

A physical promotion must not demand that every arbitrary, dynamical, curved 3+1 spacetime has an observer-independent global scalar energy. Standard GR has local covariant conservation

\[
\nabla_\mu T^{\mu\nu}=0,
\]

but a globally conserved energy current `J^μ=-T^{μν} ξ_ν` follows, with suitable boundary conditions, when `ξ` is a timelike Killing symmetry; then `∇_μJ^μ=0`. In an arbitrary time-dependent spacetime, such a symmetry need not exist, so scalar global energy conservation is not generally guaranteed. The valid initial target for UD is **exact local/signed flux accounting on the discrete cells** and, in a stationary closed limit, an actual conserved energy observable after units/metric/source correspondence are established.

## 7. Highest-value source-backed Omega_0 birth target

Proposed typed state:

\[
 \mathsf X_n=(\Sigma_n^3,\,\psi_n,\,E_n,\,U_n,\,h_n,\,\text{receipts}_n,\,n),
\]

where `E_n` is **test** cell energy, `U_n` the oriented transport/holonomy, `h_n` the spatial metric, and `n` the discrete event index. A legitimate *candidate* refinement operator must produce a new simplicial complex, recalculate exact cell integrals/Jacobians, and preserve signed boundary/source receipts. An evolution slab uses `Σ_n³×[n,n+1]` triangulated by four-simplices per tetrahedral prism. The degree-four spacetime cells are **history/transport cells** in the 3+1 interpretation, not independent fourth spatial cells.

The three source-dependent decision gates are still OPEN:

1. **Native birth trigger:** show that an admitted `Ω₀` rule, not a human-chosen remeshing schedule, selects the apex event or causal subdivision.
2. **Energy/stock bridge:** derive a typed physical energy observable and source/sink constitutive dynamics from UD `B`, `S_μ`, and `J` before identifying any preserved quadratic count with joules.
3. **Temporal/metric/holonomy bridge:** choose and derive Lorentzian sign, normal, lapse/shift, causal order and orientation-transport readout rather than deriving them from `4/3` alone.

**Controls to preregister:** same-energy/no-birth, geometrically invalid Gram, orientation-reflected (same metric), curved-holonomy, nonuniform density, source/sink open boundary, arbitrary mass matrix with x–q cross terms, lapse/shift-changed (same h), no-Killing curved background. Predictions and thresholds require independent non-constructor review before any registry promotion.

## 8. Exact computational verification

Run:

```bash
python3 UD_TETRAHEDRAL_3PLUS1_ENERGY_FOLD_VERIFY_v0.5.py
python3 UD_K4_K5_OMEGA_APEX_TWIST_VERIFY_v0.4.py
```

- **v0.5:** 126 exact assertion groups passed: 3-cube six-tetrahedron / 4-cube 24-four-simplex determinants, linear test-density integration, four-simplex time slabs, barycentric 1→4 refinement with nonuniform energy, twelve conservative exchange steps, `4/3` tight frame and inverse, 24 S4 equivariance and parity checks, full positive quadratic form preservation, Lorentz-sign gate, ADM counterexample, O(3) and spinor-twist controls.
- **v0.4:** 94 exact assertion groups passed: `K4→K5` structural alternatives, cycle/homology, `2^10` Z₂ twists, exact hidden-normal Gram and finite twisted graph Laplacian comparisons.
- **Total:** 220 executed assertion groups across these two scripts. Two scripts test different mathematical questions; the count is not 220 independent experimental validations.

**Decision:** AUTO_LOCK only the explicitly proved statements under the declared mathematical objects; keep **all** native dynamics, 4/3 physical identification, energy calibration, hidden-dimension, causal and temporal bridges as `OPEN_GATED` / `CANDIDATE`. Do not change frozen ledger F03, Q169, G05, and source/sink statuses. Neither upload to GitHub nor public site update is implied by a local artifact.
