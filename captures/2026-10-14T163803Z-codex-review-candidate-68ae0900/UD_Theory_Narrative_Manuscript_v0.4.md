---
title: "Unified Dynamics: Distinction, Interaction and Persistence"
subtitle: "A theoretical account of tetrahedral carriers, information access and finite records"
author: "Benjamin Walker Mayes"
date: "14 October 2026 — Review candidate 0.4"
lang: en-US
---

## Abstract

Finite coherent dynamics can preserve a state difference while a restricted observation loses access to it. This manuscript develops that distinction on oriented tetrahedral chain carriers and connects it to the separate requirements of reconstruction and finite record retention. We give exact incidence spectra for selected glued carriers, decompose the five-cell core-star oscillator, and exhibit two preparations whose cell snapshots coincide although their full states remain separated. A declared Gaussian readout makes the resulting error quantitative. An orthogonal interface retains seven otherwise discarded coordinates but does not intertwine the inherited flow with the native glued generator. These calculations are integrated with conditional reconstruction, prepared capture and renewal results from four companion papers. Standard Hodge, synchronization and engineered transfer methods are identified as prior ingredients. The contribution is a finite theoretical synthesis and explicit carrier calculations, with reproducible certificates and stated resource assumptions. Native configuration selection, autonomous preparation and physically calibrated geometry remain open. No universal entropy-area density or gravitational field equation is derived.

**Keywords:** tetrahedral complexes; incidence dynamics; persistence; projective reconstruction; finite memory; capture; renewal.

**Source and scope.** The technical baseline is the recovered four-paper M5 release dated 4 October 2026: Papers I–III review drafts 1.1.1 and Paper IV development draft 0.1 [1–4]. This is a separate synthesis manuscript. The four source papers retain their identities and theorem numbering. The first closure package reconciles the four paper bytes against repository commit `4b9c1f7ba03f76324b792f389517161d2bc47e05` and integrates selected later source/interface results. It is not a complete audit of every subsequent development. All results retain their stated assumptions. Review candidate; no independent review or registry promotion is claimed. Physical promotion: 0.

# 1. The problem: how does change produce things that last?

The world changes, yet it contains things we can recognize again. Signals travel, structures survive encounters, and interactions leave traces. A theoretical account should explain how these processes connect: how a structure is generated, how it preserves identifiable properties, and how its behaviour becomes available to another process.

These are related questions with different mathematical requirements. Existence in a state space is not a formation mechanism. Conservation of a full-state quantity is not guaranteed access through a restricted readout. A successful transfer is not permanent memory. The purpose of this manuscript is to make those distinctions part of one explanatory argument.

The organizing question is:

> Can constrained interactions explain the formation of persistent structures and readable records within a common dynamical framework?

UD investigates tetrahedral packet complexes as a candidate architecture for that framework. The word *packet* denotes a declared carrier and its state; it does not independently establish a particle, a material substance or an isolated unit of physical energy. The theory must earn each of those interpretations through a further map to observables.

The approach begins with a finite setting because its relationships and consequences can be inspected exactly. A small carrier permits an explicit boundary matrix, an exact spectrum, a complete observation map and a finite apparatus state. Larger claims should remain accountable to these constructions.

Our narrative progresses through five questions. What can differ? What can interact? What survives that interaction? What can a readout recover? What mechanism preserves the recovered difference as a record? Formation and the physical bridge then become precise obligations rather than unexplained transitions between equations.

## 1.1 Object, representation and observation

UD distinguishes the system being described from the mathematical model, numerical encoding, and observation used to describe it. An exact expression and a finite approximation may refer to the same intended quantity while carrying different information. Likewise, a complete state and a restricted readout can support different conclusions about distinguishability.

The programme therefore asks which relationships survive changes of representation, which distinctions remain accessible after coarse-graining, and what mechanisms make that access persistent. Numerical convenience is a methodological choice whose consequences must be accounted for. Continuity, discreteness, dimensionality, and scale invariance remain properties to be established within a justified physical description.

This is the philosophical role of distinction in the present account: it makes access and persistence explicit without equating the description with its physical referent. The methodological governance addition [10] operationalizes this separation through exact specifications, transported observables, and declared approximation errors.

## 1.2 Exact representation and controlled approximation

The number $\sqrt{10}$ is exactly defined by $x^2=10$ and $x>0$. It is irrational: if $x=a/b$ in lowest terms, $a^2=10b^2$ gives an even exponent of the prime 2 on the left and an odd exponent on the right, a contradiction. Its nonterminating, non-eventually-periodic expansion occurs in every integer positional base. A finite expansion is rational, as is an eventually periodic expansion by a geometric-series sum. Thus changing numeral base cannot make this irrational quantity a finite fraction.

An exact expression, including $1/3=0.\overline3$, need not discard information. A finite truncation is a different object. The reduced rational $a/b$ terminates in base $B$ precisely when $b$ divides $B^n$ for some $n$, equivalently when all denominator primes divide $B$. This is an arithmetic property of encoding. It establishes no physical fractality or fundamental discreteness.

For an invertible coordinate change $y=Tx$, equivalent dynamics and observations obey

\[
A_y=T A_xT^{-1},\qquad O_y(y)=O_x(T^{-1}y).
\]

If squared norm is $x^TH_xx$, its metric transforms as

\[
H_y=(T^{-1})^TH_xT^{-1}.
\]

Transporting the state while keeping an incompatible generator, metric or noise model changes the calculation. An information-losing projection is another operation: it needs a closure criterion and an account of the distinctions it forgets.

This discipline has a direct application to recurrence. The exact frequencies $\sqrt3$ and $\sqrt5$ have no positive common period. If operative frequencies are instead replaced by the finite decimals

\[
1.732=\frac{433}{250},\qquad 2.236=\frac{559}{250},
\]

the rounded-frequency model has a common period $500\pi$, since its phase advances are $2\pi\cdot433$ and $2\pi\cdot559$. Display rounding alone creates no such change when the exact quantities are retained internally. The artefact arises when the approximations are promoted into the dynamics.

The example does not prohibit numerical modelling. It requires the numerical model's error and intended domain to accompany its predictions. Exact algebra also remains conditional on the chosen model; it cannot establish the physical interpretation of that model by itself.


## 1.3 Scope, contribution and relation to prior work

The paper studies finite models of distinction, access and retention. Its reviewable claim is that these are separate mathematical obligations, illustrated by concrete tetrahedral calculations. It does not establish that tetrahedra are the unique architecture of nature. The narrative motivates the models; the declared assumptions determine their consequences.

Combinatorial Laplacians on simplicial complexes are established objects [11]. Discrete Dirac constructions likewise predate this manuscript [12]. Our real skew incidence operator is specified explicitly; these references supply context rather than an assertion that every convention is identical. Norm conservation is a standard consequence of skew-adjointness.

Phase recovery from relative offsets belongs to the established synchronization problem [13]. The noiseless support-tree receipt in §9 gives a sufficient reconstruction under supplied nonzero-support data and component references. It is not a new general synchronization algorithm. The clock in §10 uses engineered perfect state transfer [14]; prefix dressing adds a supplied gate word, not a new origin for the clock.

The specific calculations emphasized here are the selected glued spectra, the five-cell comparison, the two-cell observation obstruction and its declared noise model, and the retained interface with its exact generator defects. Results inherited from Papers I-IV are cited as such. The present synthesis explains how their assumptions connect and where they do not. We make no priority claim that these finite examples are absent from all prior literature; a comprehensive novelty assessment remains a submission task.

## 1.4 Assumptions and mathematical domains

| Domain | Declared premises | Limit on interpretation |
|:--|:--|:--|
| Real carrier | Finite downward-closed complex; one coordinate per nonempty simplex; increasing orientation; Euclidean simplex metric | Coordinate stocks are model quantities |
| Fixed flow | Constant real skew generator; no supplied switching during the interval | Full-state conservation does not imply attraction or retention |
| Observation | Named map, preparation alternatives, known time; noise only where stipulated | A readout is not automatically an apparatus or record |
| Complex receipts | Nonzero-support forest and one supplied root phase per component | Relative phases require references and acquisition |
| Quantum apparatus | Separate finite complex Hilbert spaces; declared joint inputs, Hamiltonians and comparator | No derivation of quantum theory from the real carrier |
| Resources | Count supplied donors, references, clocks, switching and exhaustion on the same domain | A subsystem energy or marginal error is not total cost |
| Physical bridge | No calibrated length, laboratory time, action scale or geometric metric is supplied | Physical entropy-area normalization remains open |

The symbol $\mathcal X$ in §2.1 denotes a general state space; the binary register $\Theta$ in §2.2 is a separate label space. Model parameter $s$ and apparatus time $t$ are not identified. Entropies use natural logarithms and are dimensionless unless a physical conversion is separately declared.

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

with missing endpoint terms zero. Thus the flow's frequencies follow from the declared combinatorial Laplacian. These are conventional incidence/adjoint constructions [11,12]; the theoretical work lies in their specified carriers and consequences, not in presenting skew norm conservation as a new principle.

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

## 6.4 A transfer contract that retains the interface residual

The following finite contract and checks are developed in the first closure package [9].

Two independent tetrahedron carriers have 30 coordinates. The unique-simplex face-glued carrier has 23; the shared face contributes seven duplicate coordinates (three vertices, three edges, one face). For every consistently oriented pair of shared coordinates x,y, define

\[
z=(x+y)/\sqrt2,\qquad r=(x-y)/\sqrt2.
\]

Carry unshared coordinates unchanged. This defines $Q:\mathbb R^{30}\to\mathbb R^{23}$ and $R:\mathbb R^{30}\to\mathbb R^7$ with orthogonal completion $U=(Q;R)$, so

\[
\|Qv\|^2+\|Rv\|^2=\|v\|^2.
\]

The transfer is invertible when residuals are retained. Agreement $x=y$ sets $r=0$ but gives $z=\sqrt2x$. A decoder $z/\sqrt2$ restores the shared amplitude convention. Simply calling z the old amplitude silently changes calibration.

This is a conditional linear interface/state-transfer contract. It does not claim chain-map compatibility or native move admission. For the direct-sum old generator, $G=U(\mathcal A_{\Delta^3}\oplus\mathcal A_{\Delta^3})U^T$, exact arithmetic gives visible/residual coupling rank 7. The visible block differs from the native glued generator with rank 14; $Q\mathcal A_{\rm old}-\mathcal A_{\rm glued}Q$ has rank 21. Keeping residuals closes the transformed old dynamics; discarding them does not create the native glued flow.

Choosing post-event generator $\mathcal A_{\rm glued}\oplus\mathcal A_{\rm residual}$ is an additional intervention, even though it preserves total norm when both blocks are skew. Its source, locality and physical cost are unclosed. This exposes the event-local generator obligation rather than hiding it inside geometric identification.

The existing subdivision results give a second contract: $T=S/\sqrt{24}$ is a bounded chain map with residual $(I-T^TT)^{1/2}$, but attenuates vertex readout and fails unweighted flow intertwining. The stricter requirement of contraction, unit singleton vertex coefficient and unweighted intertwining is already excluded by the exact 7-versus-3 incidence norm witness. These are different contracts; neither selects native geometry change.

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

## 7.4 What the five-cell calculation adds

The exact incidence certificates and comparison protocol accompany this revision [9].

The core-star has $f=(8,18,16,5)$, chain dimension 47 and 12 exposed faces. Exact signed incidence construction, boundary cancellation and characteristic-polynomial factorization give

\[
\begin{aligned}
\chi_{\star}(x)={}&x(x^2+2)(x^2+3)^2(x^2+4)^3(x^2+5)^3(x^2+6)^2\\
&\times(x^4+9x^2+16)^3(x^4+10x^2+20)^3.
\end{aligned}
\]

The positive squared frequencies and each sign's multiplicities are

| Squared frequency | Multiplicity of each ±i frequency |
|:--|--:|
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5 | 3 |
| 6 | 2 |
| $\frac{9-\sqrt{17}}2$, $\frac{9+\sqrt{17}}2$ | 3 each |
| $5-\sqrt5$, $5+\sqrt5$ | 3 each |

There is one zero mode. The exact norm is $\sqrt{5+\sqrt5}$. The squared-frequency multiplicities sum to 23, accounting for 46 active dimensions plus the zero mode.

With the stated cell ordering, the top-cell Gram matrix is

\[
H_3=\begin{pmatrix}
4&1&-1&1&-1\\1&4&0&0&0\\-1&0&4&0&0\\1&0&0&4&0\\-1&0&0&0&4
\end{pmatrix}.
\]

Let $b=(1,-1,1,-1)$ in the four leaf coordinates. Every leaf vector orthogonal to b has eigenvalue 4; this is a three-dimensional cell sector. On the core and normalized collective leaf $b/2$, the matrix is $\begin{pmatrix}4&2\\2&4\end{pmatrix}$, giving eigenvalues 2 and 6. Thus cell motion splits into three frequency-2 modes and two collective modes of frequencies $\sqrt2$, $\sqrt6$. This is an invariant top-cell oscillator decomposition, not a complete claim that all full-chain modes live on cells.

The chain's top-cell squared frequencies are $4-\sqrt3,3,4,5,4+\sqrt3$. Its full characteristic polynomial is recorded exactly in `results.json`; it differs from the core-star despite identical f-vectors. The full norm is approximately 2.69936488629, compared with approximately 2.68999404786 for the star before common scaling.

No complete exact period exists for the core-star because it includes frequencies $\sqrt2$ and $\sqrt3$ with irrational ratio. The frequency-2 cell sector can be periodic. Lack of a global period is not dissipation, stability or formation preference.

The numerical C2 comparison is illustrative only. A distance grid can be supplemented by the analytic Lipschitz estimate: since the generator ceiling is 1 and the initial difference norm is $\sqrt2$, the cell distance changes at most $\sqrt2$ per unit time. A nearest-grid cover gives a whole-interval error envelope from the sampled minimum. Floating evaluations have not been interval-certified, so the recorded envelope is not an exact numerical certificate. It cannot establish universal shape preference.

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

## 8.1 Readout error under a declared noise law

For two Gaussian output laws with known means mu_L, mu_R, common positive-definite covariance $\Sigma$ and equal priors, let $\delta=\mu_L-\mu_R$. The likelihood-ratio statistic is linear, and its exact Bayes error is

\[
P_e=\Phi\!\left(-\tfrac12\sqrt{\delta^T\Sigma^{-1}\delta}\right).
\]

Proof: center at $(\mu_L+\mu_R)/2$ and project with $\Sigma^{-1}\delta$. The score has means $\pm\delta^T\Sigma^{-1}\delta/2$ and variance $\delta^T\Sigma^{-1}\delta$; threshold zero gives the expression. At delta=0 the outputs coincide and error is 1/2. Singular covariance requires a different support-sensitive statement.

For C1 cell-only observation,

\[
\delta_q=\cos(\sqrt3s)(1,-1),\qquad
P_e(s)=\Phi\!\left(-\frac{|\cos(\sqrt3s)|}{\sqrt2\sigma}\right).
\]

For the augmented observation, $\delta_{q\prime/\sqrt3}=-\sin(\sqrt3s)(1,-1)$. Consequently its separation squared is exactly 2 for every s, and

\[
P_e^{\mathrm{aug}}=\Phi(-1/(\sqrt2\sigma)).
\]

At sigma=1/4 this is approximately 0.00233886749, while the cell-only error is 1/2 at its blind instants. The augmented receiver observes four channels rather than two, and this gain cannot be called free. No physical derivative-acquisition or retained-memory cost is closed here.

The symmetric optimal hard decision defines a binary channel with $I(Z:\widehat Z)=\ln2-h(P_e)$. This is decision information, not the full continuous-output mutual information, irreversible record entropy or information already stored in a memory. Data processing bounds it above by the full analog information.

For correlated multiple observations, stack the entire mean difference and use the complete $\Sigma$. An exact stipulated witness $\delta=(1,1)$, $\Sigma=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}$ gives squared Mahalanobis distance 4/3 rather than the incorrect independent value 2. Repeated observations with shared noise are not independent confirmations.

For m declared Gaussian residual coordinates with known marginal deviations sigma_i, Bonferroni gives simultaneous residual coverage at least $1-\alpha$ using thresholds $\sigma_i\Phi^{-1}(1-\alpha/(2m))$, without independence. This is coverage under the declared Gaussian law, not coverage inferred from covariance alone. Unknown covariance estimation needs its own uncertainty contract. Uncertain measurement time can mix the output laws and invalidate the known-time formula; no jitter law is assumed here.

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

On nonzero support, $u_{\sigma\tau}=\overline z_\sigma z_\tau$, where $z_\sigma=c_\sigma/|c_\sigma|$. As in noiseless synchronization [13], supply one root phase per component and propagate forward by $z_\tau=z_\sigma u_{\sigma\tau}$, using the conjugate ratio backward. Together with normalized stocks this recovers $c/\sqrt S$.

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

uses the engineered transfer chain of [14] and implements the word under the comparison contract. Its endpoint probability is $\sin^{2n}(\kappa t)$, transfer occurs at $T=\pi/(2\kappa)$, and the address returns at $2T$. The prefixes and preparation are supplied; the gate-dependent address edges do not prove locality on the work registers.

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

A zero signed mean switching work under one convention does not establish a free record. Thermal erasure bounds require additional reservoir and initial-state premises; finite-reservoir corrections are treated in [15]. A fresh-donor SWAP by itself supplies no thermal bath model. Nor does a matched swap establish an autonomous router. A static machine interval conserves its total energy; subsystem bare energies can change against the interaction term.

These distinctions explain why a theory of records needs the apparatus's joint state and full resource account. Without them, information-per-cost comparisons can omit the very mechanism producing the information.

# 12. Entropy, area and the physical bridge

Entropy must follow from a declared state and coarse-graining. In an illustrative symmetric binary retention channel, a uniform source bit flipped with probability $p$ leaves a uniform memory marginal. Its marginal entropy stays $\ln2$, while retained source information is

\[
I(Z:M)=\ln2-h(p),\quad
h(p)=-p\ln p-(1-p)\ln(1-p).
\]

This elementary example is an additional operational illustration, not a thermodynamic entropy-production theorem. It shows why memory entropy alone is an inadequate record-quality measure.

A boundary-face count is a combinatorial quantity. Physical boundary area requires a geometric map and units. To derive retained information per area, a capacity or scaling mechanism must link the declared records to that boundary under complete resource constraints. None of the preceding conservation or reconstruction results supplies this automatically.

Likewise, the four-paper baseline does not derive a universal gravitational entropy density, Newton's constant or Einstein's equations. The narrative identifies what such a bridge would have to connect: finite state and records, controlled coarse-graining, physical geometry, thermodynamic quantities and independently normalized couplings. Supplying the target normalization would not constitute deriving it. Jacobson's local-horizon construction [16] assumes an entropy-area relation and a Clausius condition; citing it does not derive those inputs from the UD carrier. No Bochner-flat Kähler reduction is used or established here.

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

## 13.1 Reconciled native event-source boundary

Later source audits qualify the positive interfaces and their limitations [6–8].

Later sources already provide

\[
\Theta^+=P_g\Theta^-\oplus\xi
\]

and an exact closure/hard-mask pushforward when the receipt xi and relevant local transport gates are supplied. The package rechecks 24,576 fixed-gate cases. This closes a conditional map, not the source of xi, gate updates or event occurrence.

At identical native pre-state, formal receipt completions xi=000 and xi=111 give different endpoints. Both identity and complementation commute with pair permutations. Hence symmetry and the fixed pre-event chain trajectory do not uniquely select the endpoint under that interface. The positive repair must make the set of admitted next outputs a singleton, or specify a complete normalized stochastic kernel with receipt availability, null windows and timing separately typed.

The balance observable $E_3-E_2$ supplies a pre-event signal; treating its crossing as a subdivision command is a candidate constitutive rule. The historical action/Metropolis acceptance likewise fails to select proposal frequency or admissible moves. The later polarity audit shows that universal signed-flux/index agreement and simultaneous nontrivial burden selection under binding saturation fail on stated counterexamples.

Therefore G05/G06/G09 remain source-open. The next positive task is an explicit joint state $(K,c,\Theta,\mathrm{transport},\mathrm{source},\mathrm{reservoir})$ with lawful pre-event generator, move eligibility, transfer, generator change and resource update. Supplying one such rule establishes a candidate model; a uniqueness or native-source theorem needs additional justified restrictions. There is no derivation of that rule from the reconciled fixed-flow equations alone.

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

# Appendix B. Comparison contracts

**C1 — noisy two-cell observation.** Carrier is `0123,0124`, with increasing-order simplex orientations and unit-metric skew incidence flow. Source label Z is equiprobable L/R, prepared in the two unit cell states with every other coordinate zero. Observe either the two cell amplitudes, or the four coordinates $(q,q\prime/\sqrt3)$. Measurement time is known. Add independent Gaussian noise of covariance `sigma² I` in the declared observation coordinates. This is a mathematical readout model, not measured/native noise. Units are model amplitude units; derivative normalization fixes an observation scale, not a free physical sensor.

**C2 — five-cell architecture comparison.** Compare the core-star cells `0123,1234,0235,0136,0127` with the chain `0123,1234,2345,3456,4567`. Both have 47 coordinates and 12 boundary faces. Use the same scale $\mathcal A/\sqrt8$, admitted operator-norm ceiling 1, initial norm 1, equal-prior alternatives in the first and last listed cells, cell-only readout, sigma=1/4, and horizon `[0,pi]` in the scaled model parameter. Exact rational LDL proves $8I-L$ positive definite for both, so both satisfy the ceiling. Their actual norms differ; the comparison matches a resource ceiling, not identical expenditure. Their preparation sites have different structural roles, so this single preparation does not establish architecture-wide superiority.

The reported 129-point comparison is NUMERICAL under C2. The finite horizon, noise and scale are protocol choices, not theory constants. A general worst-time or preference theorem needs additional certification or preparation averaging.

# Appendix C. Provenance and review boundaries

The recovered release contains corrected editable papers, PDFs, source records and replay receipts. Its M5 corrections supersede identified passages in the preserved prior editions. This draft uses those corrected sources rather than the older reconstructed Markdown placeholders.

The four-paper release was retrieved as `UD_FOUR_PAPER_M5_v1.0_RELEASE.zip`. Its internal README dates it 4 October 2026 and states the source versions used here. A targeted first-package reconciliation checked all four source paper blobs and selected October 9–13 interface, event-source and record-entropy captures against the current repository. Uninspected developments remain outside this reconciliation. Release hashes and the selected source hashes are recorded in the companion source register.

Constructor replay is not independent review. General statements depend on their written assumptions and proofs, not on fixture counts. This draft performs editorial integration and exact checks of the two-cell and five-cell constructions, the orthogonal interface and its generator defects, and 24,576 conditional closure cases; it does not claim to rerun every historical audit.

The unavailable `Gap2_FINAL_Finite_Genesis.png` was not read or used. Historical genesis fits and domain-only references are not used to substantiate physical formation, cosmological or gravitational claims. Physical promotion remains 0.

# Appendix D. Proofs and exact certificate conventions

## D.1 Skew flow and the harmonic obstruction

**Proposition D1.** Under §3.2, $\mathcal A^T=-\mathcal A$ and $-\mathcal A^2=L$ with the degree blocks in §4.1. Consequently the flow preserves distances and admits no attracting fixed state with a basin containing two distinct initial states.

**Proof.** Transposition reverses the two adjacent blocks. Squaring leaves diagonal blocks $-(B_k^TB_k+B_{k+1}B_{k+1}^T)$; nonadjacent blocks vanish by $B_kB_{k+1}=0$. For a difference $d$ of solutions, $(d^Td)'=d^T(\mathcal A^T+\mathcal A)d=0$. If two distinct trajectories converged to the same fixed state, their distance would tend to zero, contradicting its positive constant value. This concerns fixed closed flow, not switched or open dynamics.

## D.2 Visible closure and the retained interface

**Proposition D2.** Let $P:V\to W$ be a surjective linear observation and $A:V\to V$. A linear $F:W\to W$ satisfying $PA=FP$ exists if and only if $A(\ker P)\subseteq\ker P$.

**Proof.** Necessity follows by applying $PA=FP$ to a vector in the kernel. Conversely define $F(Px)=PAx$. If $Px=Py$, kernel invariance gives $PA(x-y)=0$, so this definition is independent of the representative. Surjectivity makes it a linear operator on all of $W$. For a nonsurjective observation the same construction is on its image, with an arbitrary extension outside that image.

**Corollary D2a.** For the §6.4 interface, the exact rank-seven block $G_{vr}$ obstructs closure of the retained visible coordinates for arbitrary residual states.

**Proof.** In transformed coordinates the projection is $(z,r)\mapsto z$. Its kernel consists of $(0,r)$, while $G(0,r)$ has visible part $G_{vr}r$. Kernel invariance is therefore equivalent to $G_{vr}=0$. The exact rank certificate rules this out. Retaining $r$ closes the inherited 30-dimensional description; it does not change it into the native 23-dimensional glued dynamics.

## D.3 Orientation and reproducible spectra

**Proposition D3.** Reversing any subset of simplex basis orientations leaves the spectrum of the unit-metric incidence generator unchanged.

**Proof.** Write the degree-wise sign matrices as $S_k$ and their direct sum as $S$. Boundary matrices transform as $B_k'=S_{k-1}B_kS_k$. Hence $\mathcal A'=S\mathcal AS$, with $S^{-1}=S$. Characteristic polynomials and Euclidean norms are unchanged. Observations and prepared coordinates must also be transported when comparing state-dependent predictions.

The reproducible certificates use sorted simplex tuples grouped by degree and the alternating boundary formula of §3.2. Constructing the integer boundaries fixes the entire operator. Symbolic characteristic polynomials certify finite spectra; multiplicity and degree checks account for every coordinate. The star top-cell decomposition follows by splitting leaf space into $b^\perp$ and $\operatorname{span}(b)$ as in §7.4. The full-chain spectrum is independently obtained from its characteristic polynomial, not inferred from the top-cell block alone. The package stores both exact polynomials and matrices. Floating norms and the 129-point comparison remain numerical outputs.

## D.4 Reconstruction and static-storage qualifications

**Proposition D4.** The stock and rooted-tree receipt of §9 reconstructs the normalized state on its declared support.

**Proof.** Each nonzero stock fixes the positive magnitude. The supplied root fixes a sign or unit phase. The unique tree path fixes every remaining sign or phase by multiplication of edge ratios, with conjugation for reversed complex edges. For receipts generated by one state, every cycle product is one, so all admissible paths agree. Without a root, multiplying a component by a common sign or phase leaves all relative receipts unchanged. This is a sufficiency result, not an optimal acquisition-cost theorem.

**Proposition D5.** A finite-dimensional time-independent Hermitian generator cannot produce exact permanent first-entry into an invariant subspace from its orthogonal complement.

**Proof.** If $W$ is invariant, Hermiticity gives $\langle Hw,v\rangle=\langle w,Hv\rangle=0$ for $w\in W^\perp$ and $v\in W$, so $W^\perp$ is invariant too. The projector onto $W$ commutes with the propagator, and its population is constant. More generally, a fixed-observable expectation is a finite sum of exponential functions of time. Constancy on an open interval forces constancy everywhere by analyticity. Approximate finite-window capture, supplied time dependence and open dynamics have different premises.

# Appendix E. Data, code and development declarations

The accompanying `UD_REVIEW_CANDIDATE_v0.4_PACKAGE.zip` contains this manuscript, four editable companion papers, exact carrier/interface matrices, the finite replay, recorded results, additional exact review assertions, an environment record and SHA-256 inventory. Run the replay in a disposable extracted copy because it regenerates result files. Python, SymPy, NumPy and SciPy versions used for this candidate are recorded in `ENVIRONMENT.json`. `README.md` states the scope of replay and the distinction between exact assertions and floating diagnostics.

Source recovery is pinned to repository base commit `4b9c1f7ba03f76324b792f389517161d2bc47e05` and first-package commit `f274108856caecd2504f28a6729a91ce93846893`; the source register records the inspected bytes. These identifiers establish provenance rather than review acceptance. Package verification does not replay every proof or apparatus theorem in Papers I-IV; inherited results must be reviewed in those sources.

ChatGPT/Codex assisted with synthesis, source checking, symbolic/numerical calculations and preparation of this review candidate. This is a development disclosure. The named author must verify the final text, accept responsibility for it, and complete the target venue's authorship, funding, competing-interest and assistance declarations before submission. No declaration of funding or competing interests is inferred from missing source information.

# References

1. Mayes, Benjamin Walker. *Finite Tetrahedral Complexes, Skew Support Flow and Contact Readiness*. Paper I, consolidated review draft 1.1.1, 4 October 2026. M5 release, `source/paper-1.md`.
2. Mayes, Benjamin Walker. *Projective Reconstruction, Complex Phase Receipts and Frozen-Tree Validation*. Paper II, consolidated review draft 1.1.1, 4 October 2026. M5 release, `source/paper-2.md`.
3. Mayes, Benjamin Walker. *Tetrahedral Symmetry, Radial Spectra and Finite Collective Mechanisms*. Paper III, consolidated review draft 1.1.1, 4 October 2026. M5 release, `source/paper-3.md`.
4. Mayes, Benjamin Walker. *Finite Prepared Quantum Controllers, Capture Windows and Correlation-Preserving Renewal*. Paper IV, development draft 0.1, 4 October 2026. M5 release, `source/paper-4.md`.
5. *Governance Amendment — CRL-2 Subdivision and Anti-Erosion Rules*, supplied `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`. Development and registry lanes remain distinct.

6. Mayes UD research record. *Native pre-event projection obstruction*, 12 October 2026, `captures/2026-10-12T014919Z-codex-native-source-97c0393f/THEOREM.md`.
7. Mayes UD research record. *Direct-Theta event to typed closure and hard-mask pushforward*, 10 October 2026, `captures/2026-10-10T170752Z-codex-theta-closure-245626d6/REPORT.md`.
8. Mayes UD research record. *Bounded subdivision two-event gate* and *Vertex interface and cross-event generator gate*, 13 October 2026, repository captures identified by the companion source register; reports are included in the replay sources.
9. *UD first closure package*, 14 October 2026. `UD_FIRST_CLOSURE_PACKAGE_v0.1.md`, accompanying source hashes, exact incidence certificates and replay.
10. *UD core methodological governance: representation and approximation*, version 1.0, 14 October 2026. User-authorized methodological addition; no theorem-confidence or physical-promotion receipt. `UD_Representation_And_Approximation_Governance_v1.0.md`.

11. Horak, Danijela, and Jürgen Jost. *Spectra of combinatorial Laplace operators on simplicial complexes*. Advances in Mathematics 244 (2013), 303-336. DOI: [10.1016/j.aim.2013.05.007](https://doi.org/10.1016/j.aim.2013.05.007). [arXiv:1105.2712](https://arxiv.org/abs/1105.2712).
12. Knill, Oliver. *The Dirac operator of a graph*. 2013. [arXiv:1306.2166](https://arxiv.org/abs/1306.2166).
13. Singer, Amit. *Angular Synchronization by Eigenvectors and Semidefinite Programming*. Applied and Computational Harmonic Analysis 30 (2011), 20-36. DOI: [10.1016/j.acha.2010.02.001](https://doi.org/10.1016/j.acha.2010.02.001). [arXiv:0905.3174](https://arxiv.org/abs/0905.3174).
14. Christandl, Matthias, Nilanjana Datta, Artur Ekert, and Andrew J. Landahl. *Perfect State Transfer in Quantum Spin Networks*. Physical Review Letters 92 (2004), 187902. DOI: [10.1103/PhysRevLett.92.187902](https://doi.org/10.1103/PhysRevLett.92.187902). [arXiv:quant-ph/0309131](https://arxiv.org/abs/quant-ph/0309131).
15. Reeb, David, and Michael M. Wolf. *An improved Landauer Principle with finite-size corrections*. New Journal of Physics 16 (2014), 103011. DOI: [10.1088/1367-2630/16/10/103011](https://doi.org/10.1088/1367-2630/16/10/103011). [arXiv:1306.4352](https://arxiv.org/abs/1306.4352).
16. Jacobson, Ted. *Thermodynamics of Spacetime: The Einstein Equation of State*. Physical Review Letters 75 (1995), 1260-1263. DOI: [10.1103/PhysRevLett.75.1260](https://doi.org/10.1103/PhysRevLett.75.1260). [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004).
