# Dual-Tetrahedral Contact, Signed-Duality and Source-Coupling Audit — v0.1

**Date:** 2026-11-22 (America/Chicago; capture 2026-11-23 UTC)  
**Result:** `EXACT_CONDITIONAL` / `NO-GO_SCOPED` / `OPEN_CONSTITUTIVE_SOURCE`; **Physical Promotion = 0**.  
**Scope:** Authenticated two-tetrahedral Euclidean contact geometry as a *comparison*, edge-contact orbit classification by an exact test, orientation-signed relation to prior UD signed complement, source-native cross-Hasse-current admission, and an illustrative norm-preserving spectral control. This is **not** a physical resonance discovery or the generation of a contact force from UD.

## 1. Sources and source boundaries

1. **External hypothesis:** Dan **Echegoyen**, *Structure of Existence Video 3.1 narrated*, YouTube, 2020-04-03, https://www.youtube.com/watch?v=UDGeXvDRwgU (segment **Tetrahedral dynamics** begins at 18:16). The supplied transcript and quotation claim that six inter-tetrahedral edge pairs always touch regardless of relative orientation. That **universal** geometric claim is directly tested and falsified below. The philosophical dual objective/subjective action semantics are not adopted as UD amplitudes.
2. **UD scope:** `ud-tetra/UD` main SHA `6a1fa6aa14624190bae4ed86a8a5db081ecb27e2`, `docs/governance/UD-SCOPE-001-observable-domain-falsifiability.md` §Locked scope rules and `AGENTS.md`. Mathematical minimality is not physical uniqueness. Physical promotion 0.
3. **Prior exact math (not promoted):** UD PR [#578](https://github.com/ud-tetra/UD/pull/578), `captures/2026-11-20T031100Z-chatgpt-sphere-inversion-6b72/REPORT.md` §3, signed complement `D1`; UD PR [#579](https://github.com/ud-tetra/UD/pull/579), `captures/2026-11-20T042200Z-chatgpt-whitney-s4-c4e7/REPORT.md` §§3–6, Whitney `S4` sign-orbit theorem and source-sign gate. Both are draft research records at source-inspection time.
4. **Source Hodge transport:** `TETRAHEDRAL_PACKET_COMPLEXES_JOP_LEAN_MANUSCRIPT_v2.5_POC1_LAB_IMPLEMENTATION_READY.md` §§2.2, 3.1–3.3, 4.5 (user-provided Library source). Typed native `A` is the 15-dimensional skew simplicial generator; Hasse currents are `J_{ση}=2 B_{ση} c_σ c_η` for incident simplex pairs; no untyped intercell spatial contact law is included in that definition. POC-1 §4.5 is a constitutive **candidate**, not a proof.
5. **Source direction:** `EDGE_STRAIN_TO_SUPPORT_AMPLITUDE_CONSTITUTIVE_SOURCE_AUDIT_v0.1.md` §§2–4,8–9 (user-provided source), which does not supply the reverse strain/contact-to-support generator or its normalization.
6. **Discovery governance:** `ud-tetra/UD-Physics` main SHA `0c9c35871d93922f081054dcc4a7a00040c9d7e3`, `BOOTLOADER.md` v1.1, `instructions/UD_DISCOVERY_v1.2.md`, `docs/UD_MATHEMATICAL_METHOD_v1.0.md`, `docs/CONCURRENCY.md` v2.0. Merged Discovery geometric controls: [#13](https://github.com/ud-tetra/UD-Physics/pull/13) (primal/dual topological typing) and [#241](https://github.com/ud-tetra/UD-Physics/pull/241) (orientation-sensitive geometry-selection control).

The present calculations use no empirical target or fitted physical constants; **the canonical dual preparation and unit illustrative cross-coupling are specified choices motivated by the lecture, not source-selected UD outcomes.**

## 2. Mathematical objects, conventions and question

Use four **labelled** regular tetrahedral vertices in a supplied, dimensionless Euclidean chart, ordered

\[
v_0=(1,1,1),\;v_1=(1,-1,-1),\;v_2=(-1,1,-1),\;v_3=(-1,-1,1).
\]

Let `E={(01),(02),(03),(12),(13),(23)}` in lexicographic order, with directed edge tangent `u_{ij}=v_j-v_i`. The other tetrahedron has vertices `w_i(Q)=-Qv_i`, with `Q∈SO(3)` and directed tangent `v_{kl}(Q)=w_l-w_k`. Each edge is a **closed line segment**; the filled 3-simplices are *distinct, disjoint labelled abstract complexes* until an explicit gluing/identification is declared. Geometric intersections of their Euclidean realizations do not by themselves establish common simplex identities.

**Typed operators:** `C(Q):R^6_B→R^6_A` is the unsigned geometric **contact incidence** (not a UD transport generator); `C_s(Q)` is orientation-signed on *transverse interior* contacts by a supplied ambient orientation; `A_0:C_*(Δ³;R)→C_*(Δ³;R)` is the single-packet skew Hodge generator, 15×15. `κ` is an externally introduced, **dimensionless comparison** parameter, not a derived native coefficient. The model evolution variable `s` is dimensionless, not physical time. `S=||c||²` is chain support, not physical energy.

For one edge pair `e=(i,j), f=(k,l)`, put `p=v_i`, `u=v_j-v_i`, `r=w_k`, `v=w_l-w_k` and `d=r-p`. Define

\[
n=u\times v,\qquad h_{ef}(Q)=d\cdot n.
\]

When `n≠0`, **EXACT** segment contact holds iff

\[
h_{ef}=0,\quad
0\le t=\frac{(d\times v)\cdot n}{n\cdot n}\le1,\quad
0\le z=\frac{(d\times u)\cdot n}{n\cdot n}\le1.
\]

A *transverse interior* contact requires `0<t,z<1`; parallel/collinear cases are treated separately by interval overlap. This is a complete **exact decision algorithm** for each of 36 pairs and any given exact rotation. It is not an enumeration of every geometrically possible contact count in all of `SO(3)`.

At an interior contact point `x=p+tu`, define the *supplied* radial orientation sign `σ_{ef}=sgn[x·(u×v)]` when nonzero. Under a reflection it changes sign. This metric/embedding/handedness-dependent pseudoscalar is **not** an endogenous seam phase.

## 3. Exact dual contact, counterexamples and orientation strata

**EXACT — canonical inverted dual `Q=I`:** exactly **six** proper interior contacts, all at parameter `t=z=1/2`, with six distinct points

\[
(\pm1,0,0),\quad(0,\pm1,0),\quad(0,0,\pm1).
\]

Their edge index pairs are `(01,23),(02,13),(03,12),(12,03),(13,02),(23,01)`; all other 30 cross-edge pairs have no actual segment intersection. The six are an **octahedral** crossing-point set in this externally supplied coordinate realization.

**EXACT — rational proper rotation counterexample:**

\[
Q_* =\frac1{87}\begin{pmatrix}-61&-22&58\\62&-19&58\\-2&82&29\end{pmatrix},
\quad Q_*^TQ_*=I,\quad\det Q_*=1.
\]

At `Q_*`, `h_{ef}(Q_*)≠0` for **each of the 36 pairs**: no two supporting lines are coplanar, so no segments intersect. Thus the claim that all six dual crossings are maintained regardless of relative orientation is **false** under independent rigid rotation. A common rigid rotation of the *whole compound* is a distinct operation and trivially preserves all contacts.

**EXACT — special quarter-turn:** `Q_90` rotates by 90° about the z-axis and produces coincident tetrahedral vertex sets. There are **30 touching edge pairs**, but their types are **six overlaps plus 24 endpoint pairs**, and **zero proper interior transverse crossings**. Total contact-pair count cannot substitute for node type or actual dynamical contact.

**EXACT — A4 stability:** each of the 12 proper tetrahedral rotational symmetries individually relabels the canonical dual tetrahedron and retains six proper interior contacts.

**NO-GO_SCOPED — generic exact-contact instability:** Each contact requires `h_{ef}(Q)=0`. Each `h_{ef}` is a real-analytic (indeed polynomial-in-matrix-entries) function on the connected 3D Lie group `SO(3)` and is nonidentically zero, as proved by the **same** exact `Q_*` satisfying `h_{ef}(Q_*)≠0` for every pair. Each zero set is therefore measure zero and has empty interior. Their finite union is measure zero and nowhere dense. Hence **almost every independently chosen rotation has zero exact edge contact**. This does *not* exclude finite-distance interaction, deformable contact, constrained alignment, or wave overlap; all require separately specified laws.

## 4. Signed contact identity, representation and geometry null

At `Q=I`, the unsigned 6×6 contact matrix is the **opposite-edge matching** involution

\[
O=(01\;23)(02\;13)(03\;12),\quad O^2=I_6,\quad\operatorname{spec}(O)=\{+1^{\times3},-1^{\times3}\}.
\]

The radial crossing signs in the ordered edge basis are `+` for the `01↔23` pair, `−` for `02↔13`, and `+` for `03↔12`. **EXACT:**

\[
\boxed{C_s(I)=D_1,\quad D_1^2=I_6,}
\]

where `D1` is *exactly the signed complementary edge map* already proved in **UD PR #578 §3** and used in **UD PR #579 §4**. Its full combinatorial symmetry is orientation-twisted:

\[
D_1T_1(g)=\operatorname{sgn}(g)\,T_1(g)D_1\qquad(g\in S_4).
\]

The radial triple-product sign is a pseudoscalar under improper Euclidean isometry, consistent with this required parity twist. However, the equality `C_s=D1` is a mathematical **conventional null**, not an independently discovered UD force law: it follows from chosen vertex coordinates, coincident dual centers, directed edges, and an oriented embedding. Neither `O` nor `D1` is automatically a dynamically active coupling.

## 5. Source-admission obstruction (no invented seam coupling)

For the **disjoint simplicial union** of two packet carriers, the native boundary matrices are block diagonal. The current skew Hodge generator is therefore

\[
A_{\mathrm{disjoint}}=\operatorname{diag}(A_0,A_0),\quad
A_0^T=-A_0,
\]

and its Hasse current `J_{ση}=2B_{ση}c_σc_η` exists only on **declared incidences**. A geometric crossing point of two straight-line drawings is not automatically a shared abstract simplex, nor an interpacket current channel. The available opposite-edge parity `Θ`, POC-1 positive latent support `ω^{lat}`, and local seam/holonomy notation do not provide:

1. an authenticated source rule creating six interpacket junctions or updating shared simplex incidence;
2. an orientation-/phase-sensitive **intertwiner** `C_s→U_{AB}` (a link transport map with specified gauge action);
3. a nonzero strength `κ`, units or work/boundary receipt; or
4. a forward event/clock selecting the mutually oriented six-contact configuration rather than generic zero contact.

**NO-GO_SCOPED:** Under unchanged, disjoint source incidences, source Hasse dynamics cannot transfer support across geometric crossings. **OPEN:** A newly declared gluing or transport action might do so after providing its state space, generator, source, normalization and controls. Prescribing the desired six crossings, setting `κ=1`, or importing a contact threshold would constitute a new candidate assumption, not a native derivation.

## 6. Conditional coupled-mode dynamics and ordinary-resonator null

To expose which observations *would* be available if a cross-edge coupling were supplied, define an **illustrative** 15×15 matrix `K_κ` supported only on degree-1 coordinates (`4:10`) with `K_κ|_{C1}=κC`. Set

\[
\mathcal A_κ=\begin{pmatrix}A_0&K_κ\\-K_κ^T&A_0\end{pmatrix},\quad\mathcal A_κ^T=-\mathcal A_κ.
\]

Then exact chain support continuity holds for all real κ:

\[
\frac{d}{ds}(\|c_A\|^2+\|c_B\|^2)=0,\quad
\frac{dS_A}{ds}=2c_A^TK_κc_B=-\frac{dS_B}{ds}.
\]

**EXACT / CONDITIONAL:** For `C=O`, or `C=D1`, or `C=I6` (all orthogonal edge intertwiners), the characteristic polynomial is **identical**:

\[
\boxed{\chi_{\mathcal A_κ}(z)
=z^2(z^2+4)^2\bigl[z^4+(8+κ^2)z^2+16\bigr]^6.}
\]

At κ=0 the original disjoint baseline is `z²(z²+4)^14`. At κ=1 the quartic is `z⁴+9z²+16`. For real κ the two split positive internal frequencies can be written

\[
\omega_\pm=\tfrac12\left(\sqrt{κ^2+16}\pm κ\right),\qquad \omega_+\omega_-=4.
\]

**NO-GO_SCOPED — spectral identifiability:** Under this symmetric unit-metric model, **global modal frequencies alone cannot identify the contact pairing nor whether an oriented `D1` sign was used**. Ordinary resonators with an arbitrary orthogonal contact matrix give the same spectrum. A discriminating readout must be address-/phase-/orientation-resolved and must control the source preparation, rather than fitting a spectral split with κ.

For the all-positive edge seed and *illustratively* κ=1, the unsigned pairing gives `dS_A/ds=+12`, `dS_B/ds=-12` at the initial instant. The signed pairing gives `+4` and `−4`, respectively. Those are mathematical consequences of the **assumed** cross-current map, not measurements or native UD source receipts. No physical units are assigned.

## 7. Falsification, checks and decision

**Independent verification:** `python3 verify.py` builds the oriented 15-chain Hodge generator, exact segment geometry, 6/0/30 contacts, 12 proper tetrahedral rotations, signed `D1`, generic no-contact proof witness and symbolic 30×30 coupled generator spectrum. `python3 replay_stdlib.py` independently implements rational segment tests and the Faddeev–LeVerrier 30×30 characteristic polynomial using standard-library `fractions.Fraction` only. Both were run by the **same constructor**; this is algorithmic cross-check, not non-constructor review. Source artifacts contain logs and exact outputs.

**Claim decisions:**
- **EXACT_CONDITIONAL / math verified:** canonical six interior edge crossings and `C_s=D1` under the declared geometric orientation; 12 proper symmetry controls; generic measure-zero contact theorem; conditional action/support and isospectrality theorem.
- **NO-GO_SCOPED:** universal orientation-independent six-contact claim; direct creation of interpacket Hasse exchange from disjoint incidence; recoverability of signed pairing from aggregate frequency splitting in this unit-metric model.
- **OPEN_GATED:** source-authenticated inter-tetra junction rule, pre-event orientation selector, phase/seam interface, nonarbitrary transfer strength, geometrically robust coupling, external observable bridge and independent replication.
- **Physical Promotion = 0**. No metric or physical force emerges solely from this computation.

**Next discriminant:** Search current UD sourced gluing and pre-event seam/Hasse current receipts for a pair-addressed *junction constructor* with a source-defined finite-range or shared-simplex topological rule. Require a fixed observable **before** evaluating any desired resonance splitting. If absent, stop rather than manufacture κ from the six geometric crossings.

**Reopening:** a versioned source rule with a typed interpacket state space, locality, gauge covariance, conservation/work receipt, selector, and independent signed-vs-unsigned/zero-contact discriminant; subsequent physical bridge must specify units, uncertainty, null controls, and preregistered acceptance rule.
