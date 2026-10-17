---
title: "Unified Dynamics: Distinction, Interaction and Persistence"
subtitle: "A theoretical account of tetrahedral carriers, information access and finite records"
author: "Benjamin Walker Mayes"
date: "14 October 2026 — Development draft 0.1"
lang: en-US
---

## Abstract

Unified Dynamics investigates whether the formation of structures, their persistence through interaction, and the production of readable records can be connected within a common dynamical account. This manuscript develops that question through a narrative synthesis of four source papers. It begins with declared distinctions and tetrahedral chain carriers, derives coherent incidence exchange and its symmetry restrictions, and shows why preserved full-state distinctions need not remain accessible to restricted observations. It then treats projective reconstruction as an information-access problem and finite capture and renewal as explicit apparatus constructions. Geometry determines possible relationships; dynamics determines their consequences; reconstruction identifies the information a readout must supply; and record formation requires an additional retention mechanism. Exact finite results are separated from supplied coefficients, prepared resources, configuration changes and physical interpretation. The resulting account provides a coherent theoretical foundation and identifies the mechanisms still needed for native formation, complete autonomous renewal and a calibrated spacetime description. It does not derive a physical metric, a universal entropy-area normalization, or a gravitational field equation.

**Keywords:** tetrahedral complexes; incidence dynamics; persistence; projective reconstruction; finite memory; capture; renewal.

**Source and scope.** The technical baseline is the recovered four-paper M5 release dated 4 October 2026: Papers I–III review drafts 1.1.1 and Paper IV development draft 0.1 [1–4]. This is a separate synthesis manuscript. The four source papers retain their identities and theorem numbering. The present draft does not certify that this release includes every subsequent portal or repository amendment. All results retain their stated assumptions. Development — no registry entry. Physical promotion: 0.

# 1. The problem: how does change produce things that last?

The world changes, yet it contains things we can recognize again. Signals travel, structures survive encounters, and interactions leave traces. A theoretical account should explain how these processes connect: how a structure is generated, how it preserves identifiable properties, and how its behaviour becomes available to another process.

These are related questions with different mathematical requirements. Existence in a state space is not a formation mechanism. Conservation of a full-state quantity is not guaranteed access through a restricted readout. A successful transfer is not permanent memory. The purpose of this manuscript is to make those distinctions part of one explanatory argument.

The organizing question is:

> Can constrained interactions explain the formation of persistent structures and readable records within a common dynamical framework?

UD investigates tetrahedral packet complexes as a candidate architecture for that framework. The word *packet* denotes a declared carrier and its state; it does not independently establish a particle, a material substance or an isolated unit of physical energy. The theory must earn each of those interpretations through a further map to observables.

The approach begins with a finite setting because its relationships and consequences can be inspected exactly. A small carrier permits an explicit boundary matrix, an exact spectrum, a complete observation map and a finite apparatus state. Larger claims should remain accountable to these constructions.

Our narrative progresses through five questions. What can differ? What can interact? What survives that interaction? What can a readout recover? What mechanism preserves the recovered difference as a record? Formation and the physical bridge then become precise obligations rather than unexplained transitions between equations.

# 2. Distinction: specify the alternatives before explaining their evolution

## 2.1 State, observation and resolvability

Let a declared state space be $\mathcal X$ and an observation map be $O:\mathcal X\to\mathcal Y$. Two states $x,y$ are distinguishable under this exact observation when $O(x)\ne O(y)$. Under a noisy or finite-resolution observation, distinguishability additionally depends on the output distributions, permitted decisions and error criterion.

This operational definition makes the model's alternatives explicit. It does not imply that physical existence depends on observation, nor that every state difference is already an irreversible record. Distinction under a readout is relative to a specified map.

For real chain states, the observation might retain signed coordinates or only their squares. For complex states, it might retain amplitudes, phases or bilinear receipts. These alternatives preserve different information. A narrative that calls them all “information” without naming the map would conceal the central problem.

## 2.2 A finite binary label register

On four vertices, the tetrahedral edge graph has three opposite-edge matchings:

\[
M_1=\{01,23\},\quad M_2=\{02,13\},\quad M_3=\{03,12\}.
\]

Assigning one bit to each defines $\Theta=\mathbb F_2^3$. Its eight labels separate into Hamming-weight sectors of dimensions $1,3,3,1$. Vertex permutations induce an onto action $S_4\to S_3$ on the matchings, with Klein-four kernel [1, §3].

The labeled product set $S_4\times\Theta$ has $24\cdot8=192$ elements. Under the specified reference-edge projection, its six edge fibers each have 32 elements. These are exact counts of declared objects. They do not establish a physical coupling, a 32-stage history or a clock period. On the same fiber one can supply an identity update, a transposition or a 32-cycle.

The binary register and the amplitude carrier below therefore have different roles. The first organizes labels; the second supports continuous state evolution. A source law relating them must be supplied or derived. Counting their coordinates does not provide that law.

# 3. Why tetrahedral structure enters

## 3.1 Relationships before metric

A state list does not determine which parts interact. A simplicial complex makes those relationships explicit through containment and shared boundaries. A filled tetrahedron includes vertices, edges, faces and a cell. Its chain dimensions are

\[
f(\Delta^3)=(4,6,4,1),\qquad \dim\mathcal C(\Delta^3)=15.
\]

It is the smallest three-dimensional simplex. This supplies a compact architecture with a closed two-dimensional boundary and several incidence levels. It provides a tractable setting for exchange within a cell and coupling between cells.

This explains why it is useful to investigate tetrahedra. It does not prove uniqueness among candidate architectures or derive the dimension of physical space. A topological cell dimension, a chain-register dimension and an apparatus Hilbert-space dimension are distinct objects.

## 3.2 Chain conventions

Let $K$ be a finite oriented tetrahedral simplicial complex, downward closed under faces. Each nonempty simplex occurs once. Increasing vertex order fixes the basis orientation. Set

\[
\mathcal C(K)=\bigoplus_{k=0}^3C_k(K;\mathbb R).
\]

For an oriented simplex,

\[
\partial_k[v_0\ldots v_k]
=\sum_{j=0}^k(-1)^j[v_0\ldots\widehat v_j\ldots v_k].
\]

Write $B_k$ for its matrix. Every codimension-two face appears twice with opposite signs, giving $B_{k-1}B_k=0$. The simplex basis is orthonormal in the present model. This is a declared Euclidean inner product on coordinates, not a derived physical spacetime metric.

The filled tetrahedron, its boundary sphere and its edge graph are different carriers. Replacing one by another changes the chain spaces, homology and operators. Their shared visual vocabulary cannot make their equations interchangeable.

# 4. Interaction: what the architecture actually does

## 4.1 The declared coherent flow

On the direct-sum chain space define [1, §4]

\[
\mathcal A_K=
\begin{pmatrix}
0&-B_1&0&0\\
B_1^T&0&-B_2&0\\
0&B_2^T&0&-B_3\\
0&0&B_3^T&0
\end{pmatrix},\qquad
\frac{dc}{ds}=\mathcal A_Kc.
\]

The parameter $s$ has no laboratory unit assigned. The operator is skew, so

\[
\frac{d}{ds}(c^Tc)=0,\qquad e^{s\mathcal A_K}\in O(\mathcal C(K)).
\]

More strongly, every pair of solutions preserves its Euclidean separation:

\[
\|c(s)-\widetilde c(s)\|=\|c(0)-\widetilde c(0)\|.
\]

This tells us what the model protects: full-state norm and distance. It does not yet tell us what a particular readout retains or how disturbances affect the model.

The chain identity also gives

\[
-\mathcal A_K^2=L_K,\qquad
(L_K)_k=B_k^TB_k+B_{k+1}B_{k+1}^T,
\]

with missing endpoint terms zero. Thus the flow's frequencies follow from the declared combinatorial Laplacian. These are conventional incidence/adjoint constructions; the theoretical work lies in their specified carriers and consequences, not in presenting skew norm conservation as a new principle.

## 4.2 A local account of exchange

For adjacent simplices $\sigma\subset\tau$, define

\[
J_{\sigma\tau}=2B_{\sigma\tau}c_\sigma c_\tau.
\]

The incidence contributes $-J_{\sigma\tau}$ to the lower coordinate's stock derivative and $+J_{\sigma\tau}$ to the upper coordinate's. For any coordinate set $R$,

\[
\frac{d}{ds}\sum_{\sigma\in R}c_\sigma^2
=J_{\mathrm{in}}(R)-J_{\mathrm{out}}(R).
\]

Internal contributions cancel. A change in the selected stock is therefore accounted for by crossing incidences. This makes “exchange” a defined balance statement. Identifying this bilinear quantity with an electrical current or physical energy flux needs an independent observation map.

## 4.3 Single-cell recurrence

For the filled tetrahedron, let $P_0$ project onto the uniform vertex mode and vanish on higher degrees. Direct boundary multiplication gives

\[
\mathcal A^2=-4(I-P_0),\quad
\det(\lambda I-\mathcal A)=\lambda(\lambda^2+4)^7,
\]

\[
e^{s\mathcal A}=P_0+\cos(2s)(I-P_0)
+\tfrac12\sin(2s)\mathcal A.
\]

The single-cell operator has period $\pi$. This is a property of the chosen flow, not the identification of a universal tick of nature.

# 5. Symmetry: organize interactions without inventing coefficients

The natural signed $S_4$ action decomposes the chain carrier as [3, §2]

\[
\begin{aligned}
C_0&=A_1\oplus T_2,&C_1&=T_2\oplus T_1,\\
C_2&=T_1\oplus A_2,&C_3&=A_2.
\end{aligned}
\]

Consequently,

\[
\mathcal C=A_1\oplus2A_2\oplus2T_1\oplus2T_2.
\]

Equivariance permits adjacent exchange only between common irreducible types: $T_2$ between vertices and edges, $T_1$ between edges and faces, and $A_2$ between faces and cell. The harmonic $A_1$ mode is isolated.

The real commutant has dimension $1+4+4+4=13$. Its skew-adjoint part has dimension three. In orthonormal multiplicity bases an equivariant skew family consists of three blocks

\[
\begin{pmatrix}0&-\omega_r\\\omega_r&0\end{pmatrix}\otimes I_{d_r},
\qquad (d_r)=(1,3,3),
\]

plus zero on $A_1$. This restates the source symmetry result: three scalar channels are available. The canonical unit-weight incidence generator selects their magnitudes to be 2. Symmetry and norm conservation alone do not force that selection.

The quadratic carrier also matters. For the standard three-dimensional representation,

\[
\operatorname{Sym}^2_0(T_2)=E\oplus T_2,
\qquad\operatorname{Hom}_{S_4}(E,T_2)=0.
\]

The two sectors share a quadratic parent but admit no nonzero equivariant linear identification. A context permitting $R\otimes E\to T_2$ needs $R=T_1$ or $T_2$ among irreducible contexts; its minimum dimension is three [3, §10]. The source constructs a compatible tensor basis, while its scalar strength remains a separate choice.

Symmetry therefore answers which interactions are possible and which are excluded. A constitutive rule must answer how strongly the permitted interactions occur. A finite symmetry group is not, by itself, a derived physical gauge group.

# 6. Shapes change function; topology changes require another rule

## 6.1 Glued spectra

Use the downward-closed complexes

\[
K_A=\langle0123,0124\rangle,
\quad K_B=\langle0123,0124,0134\rangle,
\quad K_C=\langle0134,0234,1234\rangle.
\]

Their chain dimensions are 23, 27 and 27. Exact incidence certificates give [1, §6]

\[
\chi_A(\lambda)=\lambda(\lambda^2+3)^4(\lambda^2+5)^7,
\]

\[
\chi_B(\lambda)=\chi_C(\lambda)
=\lambda(\lambda^2+2)^2(\lambda^2+5)^{11}.
\]

The arrangement changes the available frequencies. Since $\sqrt{5/3}$ and $\sqrt{5/2}$ are irrational, none of these complete flows has a positive full-operator period. Selected single-frequency states remain periodic and approximate returns remain possible. Lack of a common exact period is not dissipation or irreversible history production.

## 6.2 Shared interfaces and ownership

In a unique-simplex complex a shared face is one coordinate, not one copy per cell. For a pure tetrahedral complex, attributing $1/n_3(\sigma)$ of each stock to each containing cell gives

\[
S_\tau^{\mathrm{eq}}=\sum_{\sigma\subseteq\tau}
\frac{c_\sigma^2}{n_3(\sigma)},\qquad
\sum_\tau S_\tau^{\mathrm{eq}}=\|c\|^2.
\]

The equality is accounting, not a physical constitutive law. Independent copies of cells have separate coordinates and require an explicit identification map before this formula describes their assembly.

## 6.3 Equal exterior boundary is insufficient for dynamical equivalence

The oriented 2-to-3 move has equal exterior boundary because its difference is the boundary of $[01234]$. Its two sides nevertheless have different carrier dimensions and spectra. A norm-preserving coordinate inclusion need not intertwine their continuous flows.

The source also gives a concise incompatibility witness. Boundary fixation and chain compatibility force a top chain of squared norm 2 to map to a filling of squared norm 3. An isometry cannot implement that forced image [1, §6.5]. Thus boundary preservation, chain compatibility and Euclidean isometry cannot all be imposed under that linear contract.

Geometry creation needs its own state-transfer law. Equality of boundary chains does not select it.

# 7. Persistence and formation

## 7.1 State preservation does not imply attraction

Under the fixed skew flow, different initial states keep their separation. In particular, a state cannot converge to a different fixed point: its distance from that point remains constant. Distance to an invariant linear subspace is also preserved, because orthogonal evolution preserves both the subspace and its orthogonal complement.

This permits persistent modes and recurrence. It excludes attracting convergence to those targets in that particular full-state model. A projected observable can show apparent concentration without establishing full-state attraction. Open or nonlinear dynamics requires a separate analysis.

## 7.2 An explicit prepared growth construction

The source contains a useful assembly rule [3, §11.2]: begin with one tetrahedron and attach each new cell to a boundary face using a fresh vertex. Each step adds one vertex, three edges, three faces and one cell. It removes one boundary face and creates three. Therefore after $m$ cells,

\[
f=(m+3,3m+3,3m+1,m),\qquad f_{2,\partial}=2m+2.
\]

Its dual graph is a tree. Chain and star arrangements both satisfy the rule, so it supplies assembly grammar without a unique shape selector.

The earlier five-cell configuration—a core tetrahedron with one cell attached to each of its four faces—is a member of this class when all four attachments use distinct fresh vertices. It has

\[
f=(8,18,16,5),\quad\dim\mathcal C=47,\quad f_{2,\partial}=12.
\]

These counts describe a prepared abstract complex. They do not select a physical embedding, a frequency spectrum, a formation probability or a stability advantage.

## 7.3 What a preference claim must specify

A structure may form rarely and survive well, or form frequently and fail quickly. Its occurrence depends on both processes. Comparing candidates requires a common initial ensemble, configuration-changing rules, state transfers, disturbances and resources.

A persistence criterion should name the retained property, tolerance and duration. Possible properties include bounded leakage, retained distinguishability or valid receipt consistency. These are different criteria. Coherent agreement explains selection only when a stated interaction makes that agreement alter formation or survival.

The source's four-coordinate averaging law provides a warning [3, §12.1]:

\[
T(s)=P_0+e^{-4s/3}(I-P_0).
\]

It preserves the uniform component but suppresses contrast. Retaining total stock through averaging does not establish a localized bound structure. Formation, localization and information retention must remain separately tested.

# 8. A distinction can survive while a readout loses access

Consider $K_A$, with two cell amplitudes $q=(q_1,q_2)^T$. Boundary cancellation gives

\[
q''=-B_3^TB_3q
=-\begin{pmatrix}4&1\\1&4\end{pmatrix}q.
\]

Prepare either $L$ with $q(0)=(1,0)$ or $R$ with $q(0)=(0,1)$; set all other coordinates initially to zero, so $q'(0)=0$. Write $c_5=\cos(\sqrt5s)$ and $c_3=\cos(\sqrt3s)$. Then

\[
q_L(s)=\tfrac12(c_5+c_3,c_5-c_3),\qquad
q_R(s)=\tfrac12(c_5-c_3,c_5+c_3).
\]

The cell-only separation is $\sqrt2|c_3|$. At $s_* =\pi/(2\sqrt3)$ the snapshots coincide. An observer receiving only those exact cell coordinates cannot recover the initial alternative; with equal priors its best error is $1/2$.

The complete state separation remains $\sqrt2$, and

\[
q'_L(s_*)-q'_R(s_*)=-\sqrt3(1,-1).
\]

Retaining the derivatives restores this distinction. The apparent loss belongs to the observation restriction, not to closed-state erasure.

Away from the zeros, exact noiseless cell coordinates separate these preparations perfectly. Shrinking separation becomes a gradual information-loss curve only after noise or finite resolution is specified. This example extends the source carrier calculation as an explicitly derived illustration; it does not introduce a new physical measurement claim.

More generally, a linear visible law $PA=FP$ exists exactly when $\ker P$ is invariant under $A$ [2, Theorem II.M1]. If hidden states with equal visible outputs have different visible derivatives, no autonomous visible law can describe both. Memory of the omitted coordinates or a larger state description is needed.

# 9. Reconstruction: what must a receipt contain?

## 9.1 Why stocks and currents may be insufficient

Squared coefficients lose signs. On the bipartite incidence graph, adjacent products also allow opposite rescaling of even and odd degrees. If their initial norm contributions are $a,b>0$, rescaling by $\lambda$ and $\lambda^{-1}$ preserves currents and changes total norm to

\[
a\lambda^2+b\lambda^{-2}.
\]

When $a\ne b$, the same original norm is obtained at both $\lambda^2=1$ and $\lambda^2=b/a$. The states $(2,1)$ and $(1,2)$ on one incident vertex-edge pair provide a rational witness [2, §2]. Thus all adjacent products plus total norm do not generally recover the signed state.

## 9.2 A sufficient real receipt

Let $S=\sum c_\sigma^2>0$ and $\rho_\sigma=c_\sigma^2/S$. On each connected component of nonzero support choose a root and spanning tree. Supply the root sign and relative signs $\chi_{uv}=\operatorname{sgn}(c_uc_v)$ on tree edges. Propagate signs by $s_v=s_u\chi_{uv}$. Then

\[
\widehat c_\sigma=s_\sigma\sqrt{\rho_\sigma}
=c_\sigma/\sqrt S.
\]

This reconstructs the positive ray, with explicit zeros, independently of forest choice. Root signs remain necessary because simultaneous sign reversal of a support component leaves its stocks and pair products unchanged. The receipt's sufficiency is deterministic identifiability under the supplied data, not an authentication or acquisition theorem.

## 9.3 Complex phase receipts

For complex coefficients define [2, §6]

\[
\mathcal J_{\sigma\tau}=2B_{\sigma\tau}\overline c_\sigma c_\tau,
\qquad u_{\sigma\tau}
=\frac{B_{\sigma\tau}\mathcal J_{\sigma\tau}}{|\mathcal J_{\sigma\tau}|}.
\]

On nonzero support, $u_{\sigma\tau}=\overline z_\sigma z_\tau$, where $z_\sigma=c_\sigma/|c_\sigma|$. Supply one root phase per component and propagate forward by $z_\tau=z_\sigma u_{\sigma\tau}$, using the conjugate ratio backward. Together with normalized stocks this recovers $c/\sqrt S$.

The oriented cycle products must equal one. Real-part currents alone do not recover these phases: conjugation preserves stocks and real parts while generally changing the declared positive ray. References are part of the receipt's required resources.

## 9.4 Prediction and uncertainty

On the full-support filled tetrahedron, the incidence graph has 15 nodes and 28 edges. A frozen tree uses 14 edges and leaves 14 chords. For log amplitudes, tree observations are endpoint sums. Alternating path sums give an exact integer matrix $C$ satisfying $H=CS$ and $z_H=Cz_T$ [2, §5].

Prediction covariance follows as $\Sigma_H=C\Sigma_TC^T$. The identity does not certify coverage without a probability model, and shared measurement noise requires residual cross-covariances. Algebraic consistency, statistical uncertainty and physical acquisition are separate claims.

# 10. From readable state to finite record apparatus

Reconstruction tells us what information is sufficient if supplied. Record formation asks what interaction produces and retains it. Paper IV makes this apparatus question explicit in finite complex Hilbert spaces [4]. This changes the mathematical description; it is not a derivation of quantum theory from real chain amplitudes.

For a declared quantum encoding and equal-prior alternatives, optimal readout error can be expressed through trace distance. Every apparatus claim must name that encoding, its joint state and its readout. We use

\[
D_{\mathrm{tr}}(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1
\]

for state comparisons, and operator norm for generator mismatch. No physical unit follows from the convention $\hbar=1$.

The apparatus includes work registers, reference, fuel, production clock, output, capture flag, records, renewal donor and retained spectators. A complete comparison includes their correlations. Good marginals cannot certify a good joint state: equal weights on $110,101,011$ give each bit success probability $2/3$ and zero probability of all three succeeding.

## 10.1 Prepared history propagation

For a supplied gate word $U_1,\ldots,U_n$, prefix dressing of the clock

\[
H_C=\kappa\sum_{j=0}^{n-1}\sqrt{(j+1)(n-j)}
(|j+1\rangle\langle j|+|j\rangle\langle j+1|)
\]

implements the word under the comparison contract. Its endpoint probability is $\sin^{2n}(\kappa t)$, transfer occurs at $T=\pi/(2\kappa)$, and the address returns at $2T$. The prefixes and preparation are supplied; the gate-dependent address edges do not prove locality on the work registers.

If actual and comparison generators differ by at most $d$, Duhamel's identity gives propagator difference at most $td$ and full-joint trace distance at most $\min\{1,td\}$. This includes the entire interval; a successful endpoint does not erase propagation error.

## 10.2 Timed protection and static retention differ

Timed capture supplies a terminal exchange, a fresh flag, an off-switch and a factorized guarded background. Under those premises the output is protected after pulse-off, with its stated free evolution retained [4, §5].

A separate static post-launch construction provides a finite window. With an additional clock of $N+1$ addresses and rate $\lambda$, and mismatch at most $h_p$, its complete joint bound is

\[
\epsilon(t)\le\min\{1,th_p+2|\cos(\lambda t)|^N\}.
\]

For $\pi/(4\lambda)\le t\le3\pi/(4\lambda)$,

\[
\epsilon(t)\le\min\{1,3\pi h_p/(4\lambda)+2\,2^{-N/2}\}.
\]

The smaller reduced-body tail cannot replace the full joint term when clock correlations remain relevant. The comparator transfers exactly halfway through its cycle and undoes the transfer at a full cycle. These are pointwise bounds, not continuously monitored survival probabilities.

## 10.3 Why permanent capture needs another mechanism

For finite time-independent Hermitian $H$, an invariant subspace is reducing. Its projector commutes with $H$, so population cannot first enter it from its orthogonal complement. Fixed-observable expectations are finite sums of exponentials; if exactly constant on an open interval, analyticity makes them constant for all time [4, Theorem IV.9].

This excludes exact permanent first-entry storage under that closed static contract. It permits finite-window approximation, supplied switching and open-system mechanisms with their own resources. The theorem explains why protection cannot simply be inferred from successful coherent transfer.

# 11. Renewal, preparation and complete resource cost

## 11.1 Renewal moves correlations

Supply a donor $D$ independent of the old active module $A$ and its history $Y$, with matched carrier and bare energy operators. Then [4, Theorem IV.12]

\[
\mathrm{SWAP}_{AD}(\rho_{AY}\otimes\sigma_D)
\mathrm{SWAP}_{AD}=\sigma_A\otimes\rho_{DY}.
\]

The active module is refreshed; all old correlations are exported to donor and history. They are not destroyed. Repetition consumes fresh donor and output slots, and failures consume resources too.

On matching full joint domains, admitted bank error $\epsilon_F$ and operation comparisons $\epsilon_j$ compose unconditionally as

\[
\epsilon_{\mathrm{total}}
\le\min\{1,\epsilon_F+\sum_j\epsilon_j\}.
\]

This requires uniform operation bounds on the admitted joint states. Isolated-input results do not automatically meet that requirement. The bank error is charged once; diagnostics already covered by it are not charged again as independent errors.

## 11.2 Coherent supply is a resource

The source constructs a uniform reference packet of length $L=2^q$ from a seed and supplied coherent binary fuel [4, Theorem IV.2]. Ideal independent fuel has

\[
\langle H_F\rangle=\Delta(L-1)/2,
\qquad\operatorname{Var}H_F=\Delta^2(L^2-1)/12.
\]

The exchanges conserve the declared sum of bare energies while transferring the supplied coherence. They do not create that coherence from an unspecified reservoir.

For a complete stationary input processed covariantly under the declared additive free-energy generators, the reference remains stationary. With nondegenerate packet energies, its distance from the pure uniform packet is at least $1-1/L$ [4, Theorem IV.3]. Nonstationary supply can evade that particular obstruction, but must enter the ledger.

## 11.3 What a complete cost comparison includes

Cost requires declared energy operators, initial states, interaction and switching conventions, clock preparation, write and readout, retention, renewal, and finite exhaustion. Mean energy, variance, signed switching work, peak demands, time and consumed blank capacity are different quantities.

A zero signed mean switching work under one convention does not establish a free record. Nor does a matched swap establish an autonomous router. A static machine interval conserves its total energy; subsystem bare energies can change against the interaction term.

These distinctions explain why a theory of records needs the apparatus's joint state and full resource account. Without them, information-per-cost comparisons can omit the very mechanism producing the information.

# 12. Entropy, area and the physical bridge

Entropy must follow from a declared state and coarse-graining. In an illustrative symmetric binary retention channel, a uniform source bit flipped with probability $p$ leaves a uniform memory marginal. Its marginal entropy stays $\ln2$, while retained source information is

\[
I(Z:M)=\ln2-h(p),\quad
h(p)=-p\ln p-(1-p)\ln(1-p).
\]

This elementary example is an additional operational illustration, not a thermodynamic entropy-production theorem. It shows why memory entropy alone is an inadequate record-quality measure.

A boundary-face count is a combinatorial quantity. Physical boundary area requires a geometric map and units. To derive retained information per area, a capacity or scaling mechanism must link the declared records to that boundary under complete resource constraints. None of the preceding conservation or reconstruction results supplies this automatically.

Likewise, the four-paper baseline does not derive a universal gravitational entropy density, Newton's constant or Einstein's equations. The narrative identifies what such a bridge would have to connect: finite state and records, controlled coarse-graining, physical geometry, thermodynamic quantities and independently normalized couplings. Supplying the target normalization would not constitute deriving it.

Counting events can order histories and track resources. It does not calibrate proper time. A metric, an action scale and a clock map remain additional physical obligations. This manuscript makes no claim that all these bridges are already closed.

# 13. What the theory currently explains, and what it must explain next

The finite account already gives a coherent explanatory sequence. Incidence specifies possible exchange. A generator calculates its consequences. Symmetry organizes channels while exposing free choices. A restricted readout can conceal a preserved distinction. Sufficient receipts restore identifiability when acquired. Prepared capture and renewal specify finite record mechanisms and their limits.

Formation remains partly supplied: boundary attachment is an explicit grammar, but the source must still determine which attachment occurs and how its state and resources transfer. A stability or occurrence preference needs the same preparation and disturbance conditions across candidates.

The next theoretical targets therefore have a dependency order:

1. Specify a native configuration-changing rule and complete state transfer.
2. Connect compatibility to formation or survival through that rule.
3. Derive a complete production-to-capture trigger and finite router on one joint domain.
4. Include reference and clock preparation, failure histories and exhaustion.
5. Establish calibrated observable and coarse-graining maps before physical identification.

Each step answers a question opened by the previous one. That is the manuscript's organizing logic: every equation earns its place by explaining a mechanism or delimiting what the mechanism can do.

# Appendix A. Source crosswalk

| Manuscript topic | Four-paper source | Treatment here |
|:--|:--|:--|
| Binary labels and cardinalities | I §3 | Selected definitions and counting boundary |
| Chains, skew flow, local balance | I §§4–5 | Definitions and explanatory derivations |
| Glued spectra and jump limits | I §6 | Exact source results with assumptions |
| Signed contact and admission | I §§7–8 | Retained as formation-source obligations; detailed contact family deferred |
| Real and complex reconstruction | II §§2–6 | Main identifiability argument |
| Covariance and visible closure | II §§7–8 | Selected results and scope |
| Symmetry and commutant | III §2 | Interaction typing and scalar freedom |
| Confining radial refinement | III §§3–8 | Outside the main argument; source retained for a later spectral chapter |
| Quadratic context | III §§9–10 | Symmetry obstruction and minimum context |
| Prepared growth and retention | III §§11–12 | Formation grammar and persistence distinction |
| Controllers and preparation | IV §§2–4 | Joint-state and supply requirements |
| Capture and obstruction | IV §§5–7 | Timed/static distinction and finite limits |
| Renewal and resources | IV §§8–9 | Correlation export and accounting |
| Two-cell observation example | I §6 plus direct derivation | New expository calculation, not physical promotion |
| Binary retention entropy | Declared illustrative channel | Additional operational example, not a sourced UD entropy law |

This is a selective theoretical synthesis, not a concatenation or exhaustive replacement of the four papers. The radial and full contact results remain available in their source locations. No omitted source result is withdrawn by this manuscript.

# Appendix B. Provenance and review boundaries

The recovered release contains corrected editable papers, PDFs, source records and replay receipts. Its M5 corrections supersede identified passages in the preserved prior editions. This draft uses those corrected sources rather than the older reconstructed Markdown placeholders.

The four-paper release was retrieved as `UD_FOUR_PAPER_M5_v1.0_RELEASE.zip`. Its internal README dates it 4 October 2026 and states the source versions used here. No fresh audit of subsequent live portal or GitHub amendments was performed for this draft. Release hashes and the selected source hashes are recorded in the companion source register.

Constructor replay is not independent review. General statements depend on their written assumptions and proofs, not on fixture counts. This draft performs editorial integration and a targeted exact check of the two-cell and five-cell constructions; it does not claim to rerun every historical audit.

The unavailable `Gap2_FINAL_Finite_Genesis.png` was not read or used. Historical genesis fits and domain-only references are not used to substantiate physical formation, cosmological or gravitational claims. Physical promotion remains 0.

# References

1. Mayes, Benjamin Walker. *Finite Tetrahedral Complexes, Skew Support Flow and Contact Readiness*. Paper I, consolidated review draft 1.1.1, 4 October 2026. M5 release, `source/paper-1.md`.
2. Mayes, Benjamin Walker. *Projective Reconstruction, Complex Phase Receipts and Frozen-Tree Validation*. Paper II, consolidated review draft 1.1.1, 4 October 2026. M5 release, `source/paper-2.md`.
3. Mayes, Benjamin Walker. *Tetrahedral Symmetry, Radial Spectra and Finite Collective Mechanisms*. Paper III, consolidated review draft 1.1.1, 4 October 2026. M5 release, `source/paper-3.md`.
4. Mayes, Benjamin Walker. *Finite Prepared Quantum Controllers, Capture Windows and Correlation-Preserving Renewal*. Paper IV, development draft 0.1, 4 October 2026. M5 release, `source/paper-4.md`.
5. *Governance Amendment — CRL-2 Subdivision and Anti-Erosion Rules*, supplied `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`. Development and registry lanes remain distinct.
