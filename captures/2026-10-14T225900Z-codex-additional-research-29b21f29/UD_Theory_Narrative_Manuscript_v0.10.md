---
title: "Unified Dynamics: Distinction, Interaction and Persistence"
subtitle: "A theoretical account of tetrahedral carriers, information access and finite records"
author: "Benjamin Walker Mayes"
date: "14 October 2026 — Review candidate 0.10"
lang: en-US
---

## Abstract

Finite coherent dynamics can preserve a state difference while a restricted observation loses access to it. We study this distinction on oriented tetrahedral chain carriers and separate reconstruction from finite record retention. A family-level gluing theorem shows that t tetrahedra formed by fresh-vertex face attachment have a 15t-dimensional copied state and an (8t+7)-dimensional normalized unique-simplex view. Under separate skew incidence dynamics with nonzero exchange weights in each cell, snapshot and derivative together distinguish every copied state. Any exact autonomous linear realization of the complete visible trajectory for arbitrary initial states therefore needs 7(t-1) extra state coordinates. This requirement differs from lossless residual storage for general gluings. We also derive conditioning and noise bounds, including sharp two-cell and core-star gains, a fixed-norm ill-conditioning family, and an exact sampled-readout contract. Exact spectra, observation examples and a closed-gluing control support the argument, which is integrated with conditional reconstruction, capture and renewal contracts. Standard Hodge, observability, projection-memory, synchronization and transfer methods are credited. The result concerns declared finite models: it derives neither native configuration selection nor a calibrated physical metric, universal entropy-area density or gravitational equation.

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

The two-tetrahedron model in §6.1 has a squared frequency 3, hence the exact frequency $\sqrt3$, defined by $x^2=3$ and $x>0$. This is a model-derived example, not a universal physical constant. It is irrational: if $x=a/b$ in lowest terms, $a^2=3b^2$ gives an even exponent of the prime 3 on the left and an odd exponent on the right, a contradiction. Its nonterminating, non-eventually-periodic expansion occurs in every integer positional base. A finite expansion is rational, as is an eventually periodic expansion by a geometric-series sum. Thus changing numeral base cannot make this irrational quantity a finite fraction.

A radical must also retain its declared meaning. For example, $\sqrt{4/3}=2/\sqrt3$ is distinct from $\sqrt2$; taking the square root of a supplied ratio does not derive a carrier frequency or physical law. A numerical match between quantities with different definitions requires an explicit correspondence. An exact expression, including $1/3=0.\overline3$, need not discard information. A finite truncation is a different object. The reduced rational $a/b$ terminates in base $B$ precisely when $b$ divides $B^n$ for some $n$, equivalently when all denominator primes divide $B$. This is an arithmetic property of encoding. It establishes no physical fractality or fundamental discreteness.

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

Combinatorial Laplacians on simplicial complexes are established objects [11]. Discrete Dirac constructions likewise predate this manuscript [12]. Knill gives the complete-graph Dirac spectrum, including the filled tetrahedron [18, §9.3]. The phase equivalence in Appendix D.7 identifies its spectrum with ours. The single-cell spectrum is established background. Weighted simplicial Dirac constructions also predate this manuscript [19]. Norm conservation is a standard consequence of skew-adjointness.

Phase recovery from relative offsets belongs to the established synchronization problem [13]. The noiseless support-tree receipt in §9 gives a sufficient reconstruction under supplied nonzero-support data and component references. It is not a new general synchronization algorithm. The clock in §10 uses engineered perfect state transfer [14]; prefix dressing adds a supplied gate word, not a new origin for the clock.

The main added result is the stacked-family memory theorem in §6.5, supported by a structural rank proof. The selected glued spectra, five-cell comparison, two-cell observation obstruction and retained interface provide concrete examples. General observability and projection-memory principles are established background [20,21]. Results inherited from Papers I-IV are cited as such. The present synthesis explains how their assumptions connect and where they do not. We make no priority claim that these finite examples are absent from all prior literature; a comprehensive novelty assessment remains a submission task.

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

## 2.3 Comparing event labels and composing a history

A receipt alphabet can distinguish event types without specifying which events can follow each other. The additional working notes [24] motivate a conditional 44-label alphabet: eight fixed-weight labels, eighteen onset labels and eighteen extinction labels, including address and parity. It has 946 unordered comparisons of distinct labels. Only 400 pairs have even one ordering with compatible incoming and outgoing Hamming weights. Full bit, frame and transport rules may reduce this set further. These counts organize possible comparisons; an admissible event graph and its update kernel remain separate obligations.

The onset/extinction block illustrates why numerical matches need typed provenance. Both its same-address subset and its reverse-weight-step subset have 108 pairs, yet their intersection contains only 36. They are different subsets. Neither their count ratio nor an assigned address cost determines a winding increment. Appendix D.12 derives the counts and shows that a winding or cost is recoverable from a receipt precisely when it is constant on each receipt fiber.

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

We use the full vertex-permutation group $S_4$, including odd permutations, with orientation signs on simplex chains. The standard representation $T_2$ is the sum-zero subspace of the four-vertex permutation representation; $A_2$ is the sign representation and $T_1=T_2\otimes A_2$. These definitions remove label ambiguity. Finite-group reduction uses standard character theory [17]. This is the signed chain action, distinct from the unsigned permutation action on six edge labels.

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

## 5.1 Symbolic strengths and invariant exchange sectors

Let $G_k$ contain only the degree-$k-1$/$k$ exchange blocks of §4.1. On the filled tetrahedron,

\[
A(a,b,c)=aG_1+bG_2+cG_3,\qquad a,b,c\in\mathbb R,
\]

\[
\det(zI-A(a,b,c))
=z(z^2+4a^2)^3(z^2+4b^2)^3(z^2+4c^2).
\]

The mutually orthogonal invariant sector projectors are $\Pi_k=-G_k^2/4$, of ranks 6, 6 and 2. Together with the harmonic rank-one projector they sum to identity. For nonzero weights the active frequencies are $2|a|,2|b|,2|c|$, with positive-frequency multiplicities 3, 3 and 1; a zero weight makes that entire sector stationary. Coefficient signs select the sense of rotation in an oriented channel, while the spectrum alone retains only their magnitudes. Equal frequency does not mix inequivalent irreducible channels.

The projectors follow from the incidence matrices and $B_{k-1}B_k=0$. They organize exchange within the declared carrier; the free strengths are constitutive choices, not derived constants. The canonical unit-weight case is $a=b=c=1$. This weighted boundary construction is standard in kind [19]; the exact convention and calculation are supplied here for review. Appendix D.7 proves the sector and character statements.

The dimensions above require full $S_4$. Restricting to proper tetrahedral rotations $A_4$ identifies the two three-dimensional types and trivializes the sign type. The full carrier becomes $3\mathbf1\oplus4\mathbf3$, so its real commutant dimension is 25 and its skew dimension is 9. One cannot replace $S_4$ by $A_4$ while retaining the 13/3 counts. The coefficient field is also part of the model. Auxiliary finite-field modules require a declared action and an observable bridge before they can describe the real carrier. For example, the additional notes correctly exclude a surjection from the order-26 group $D_{13}$ onto $S_3$; an extension by the order-four Klein group has order 104 and still cannot supply that quotient. Valid arithmetic on a chosen group or field does not select it as the native frame symmetry [24].

## 5.2 Quadratic context and its limits

The quadratic carrier also matters. For the standard three-dimensional representation,

\[
\operatorname{Sym}^2_0(T_2)=E\oplus T_2,
\qquad\operatorname{Hom}_{S_4}(E,T_2)=0.
\]

The two sectors share a quadratic parent but admit no nonzero equivariant linear identification. A context permitting $R\otimes E\to T_2$ needs $R=T_1$ or $T_2$ among irreducible contexts; its minimum dimension is three [3, §10]. Each permitted irreducible context has a one-dimensional intertwiner space. A three-dimensional carrier of type $A_1\oplus E$ fails this criterion despite having the minimum numerical dimension. The representation type, not dimension alone, makes the channel available. The source constructs a compatible tensor basis, while its scalar strength remains a separate choice.

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

The arrangement changes the available frequencies. Since $\sqrt{5/3}$ and $\sqrt{5/2}$ are irrational, none of these complete flows has a positive full-operator period. Selected single-frequency states remain periodic. More generally, every finite skew flow has uniformly close operator returns; Appendix D.10.1 gives a quantitative bound. Lack of a common exact period is not dissipation or irreversible history production.

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

A related inclusion has a useful positive result. The coordinate inclusion of the subcomplex $K_A$ into $K_B$ preserves precisely the 15-dimensional full-trajectory sector consisting of the harmonic mode and the $\sqrt5$ sector. The other eight dimensions are vulnerable even though the instantaneous generator defect has rank four. This is a stipulated subcomplex insertion, distinct from the boundary-fixing replacement above. Appendix D.10.2 gives the projectors, exact ranks and spectral-projection weights [23].

Subdivision also shows why the metric class belongs in a no-go statement. For the boundary-fixing 1-to-4 stellar map, unit-metric isometry fails and no positive diagonal simplex metric gives adjoint intertwining. A general non-diagonal positive metric can do so: Appendix D.10.3 constructs one exactly. Its weighted generator is an added model, not the native unit-metric flow. Thus an unrestricted positive-metric obstruction would be false.

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

## 6.5 A family law for gluing and dynamic memory

The interface problem extends beyond two cells. Keep one complete local register per tetrahedron before identifying shared simplex labels. For $t$ cells the copied state has $n=15t$ coordinates. Let the union have $m$ unique simplex coordinates. For each simplex $\sigma$ appearing in $\nu_\sigma$ copies, define

\[
(Qx)_\sigma=\frac1{\sqrt{\nu_\sigma}}\sum_{j:\sigma\subset\tau_j}x_{j,\sigma},
\qquad QQ^T=I_m,
\]

with orientation signs aligned first. An orthogonal completion adds $n-m$ residual coordinates, giving exact norm balance. These coordinates retain copied distinctions discarded by the normalized view; they are not physical memory bits or an energy estimate.

Predictive memory has a sharper definition. Let $A$ be the copied generator and

\[
d=\operatorname{rank}(Q;QA;\ldots;QA^{n-1}).
\]

Under exact autonomous linear evolution, linear initial encoding, arbitrary copied initial states and retention of $Qx$ as the visible coordinates, the minimum additional state dimension is $d-m$. The observability criterion is standard [20]; Appendix D.8 gives the precise skew realization and lower bound.

**Theorem 6.5 (stacked-family memory).** Start from one tetrahedron and repeatedly attach a tetrahedron along one boundary face using a fresh vertex. Give each copied cell its own constant, nonzero real weights for all three adjacent-degree exchange channels. Then

\[
m=8t+7,\qquad\operatorname{rank}(Q;QA)=15t,
\qquad h_{\min}=7(t-1).
\]

**Proof idea.** The newest cell has eight private coordinates containing its fresh vertex. Zero visible state and zero visible derivative force these coordinates and their derivatives to vanish. The seven attachment-face coordinates feed them through an injective block when all three weights are nonzero. The newest copy is therefore zero. Repeating backwards eliminates every copy. Appendix D.8 supplies the full argument and its limits.

For both five-cell star and chain, this yields 75 copied coordinates, 47 visible coordinates and 28 necessary hidden state coordinates. This is inherited independent-copy dynamics, distinct from the native 47-dimensional incidence law in §7.4. Snapshot/derivative injectivity explains why the apparently redundant copied information can matter to future observations. It supplies no free derivative sensor or uniform noise robustness.

The five-cell boundary of a 4-simplex is a different gluing. Under canonical copied dynamics it has $n=75$, $m=30$, $d=55$: 45 coordinates retain all copied information, but only 25 extra coordinates are needed for its visible dynamics. Twenty directions remain unobservable. Thus the stacked theorem's attachment condition is substantive.

Eliminating hidden coordinates instead of retaining them gives a history-dependent visible equation with an initial-residual term. This linear projection mechanism is standard in kind [21]. Neither reduced dynamics nor a memory kernel establishes irreversible record formation. The mathematical reduction identifies the information that must be retained, encoded in a history or restricted by preparation.

## 6.6 Exact access and reliable readout are different requirements

The rank theorem establishes uniqueness in exact arithmetic. Noise sensitivity depends on the declared observation metric. With scale $\tau>0$, write $M_\tau=(Q;\tau QA)$ and $H_\tau=M_\tau^TM_\tau$. If $\gamma_\tau=\sqrt{\lambda_{\min}(H_\tau)}>0$, least-squares reconstruction gives the sharp combined-error bound

\[
\|\widehat x-x\|\le\|e\|/\gamma_\tau.
\]

For canonical copies and $\tau=1/2$, the two-cell gain is exactly $1+\sqrt3$, the five-cell star gain is $\sqrt2(\sqrt5+\sqrt3)$, and the five-cell chain gain is approximately $6.43292$, with an exact rational eigenvalue certificate. These compare the same declared copied dynamics and coordinate-noise convention, not measured physical expenditure.

If a derivative is acquired from endpoint samples separated by $2h$, endpoint errors at most $\epsilon$ give derivative error at most $\epsilon/h+\|A\|^3Rh^2/6$ for state norm at most $R$. Shrinking $h$ removes Taylor bias while amplifying noise. For canonical copies the exact sampled matrix instead uses $\sin(2h)/(2h)\,QA$, removing approximation bias. Sampling at its zeros destroys this two-block readout's active information.

Known correlated Gaussian noise is handled by $I=M^T\Sigma^{-1}M$, not by treating repeated observations as independent. Its inverse is the exact reconstruction covariance under the stated linear Gaussian model. Rescaling the observation and covariance consistently leaves $I$ unchanged. Exact recovery can therefore coexist with poor operational performance, and changing a numerical normalization cannot manufacture information.

Appendix D.9 supplies complete proofs, uncertainty and confidence bounds, exact spectral certificates, the sampled acquisition contract and a fixed-norm counterexample to uniform robustness. Standard least-squares background is credited [22]. None supplies a physical noise law or the energy cost of sensors, references and storage.

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

uses the engineered transfer chain of [14]. Explicitly, supply $n\ge1$, $\kappa>0$, work generators $H_W,\bar H_W$, and unitary gates satisfying $[U_j,\bar H_W]=0$. With prefixes $P_0=I$, $P_j=U_j\cdots U_1$, let

\[
\mathcal W=\sum_{j=0}^n|j\rangle\langle j|\otimes P_j,
\quad H_p=\mathcal W(H_C\otimes I)\mathcal W^\dagger.
\]

Actual and comparison generators are $I_C\otimes H_W+H_p$ and $I_C\otimes\bar H_W+H_p$, with $\|H_W-\bar H_W\|\le d$ on the full admitted domain. Prepare address 0 independently of the work/spectator state. At the endpoint the comparator applies $P_n$ up to a common phase and the retained free evolution $e^{-it\bar H_W}$. Its clock norm is $\kappa n$. This specifies the comparison contract of [4, Theorem IV.4]. Its endpoint probability is $\sin^{2n}(\kappa t)$, transfer occurs at $T=\pi/(2\kappa)$, and the address returns at $2T$. The prefixes and preparation are supplied; the gate-dependent address edges do not prove locality on the work registers.

If actual and comparison generators differ by at most $d$, Duhamel's identity gives propagator difference at most $td$ and full-joint trace distance at most $\min\{1,td\}$. This includes the entire interval; a successful endpoint does not erase propagation error.

## 10.2 Timed protection and static retention differ

Timed capture supplies a terminal exchange, a fresh flag, an off-switch and a factorized guarded background. Under those premises the output is protected after pulse-off, with its stated free evolution retained [4, §5].

For timed capture, output protection follows from the factorization $H_{\rm bg}=H_O+H_{\rm rest}$, with no background interaction on output $O$ or record $M$, after the supplied contacts are off. It holds for correlated actual inputs, including failures. It preserves whatever output was captured; it does not turn an incorrect capture into a correct one [4, Theorems IV.6-IV.7].

A separate static post-launch construction provides a finite window [4, Theorem IV.10]. Supply matched source/output energies, blank flag and records $L,M,E$, and terminal production projector $P_n$. Define the involution

\[
J_*=P_n\otimes\mathrm{SWAP}_{SO}\otimes X_LX_MX_E
+(I-P_n)\otimes I.
\]

The body free generator $H_f$ satisfies $[J_*,H_f]=0$. A fresh independent clock $Q$ starts at address 0, has $N+1$ addresses ($N\ge1$) and rate $\lambda>0$. Dress its first edge with $J_*$ and later edges with identity: $W_0=I$, $W_j=J_*$ for $j\ge1$, $\mathcal V=\sum_j|j\rangle\langle j|\otimes W_j$ and $H_d=\mathcal V(H_Q\otimes I)\mathcal V^\dagger$. Actual and comparison generators are $I_Q\otimes(H_f+V_p)+H_d$ and $I_Q\otimes H_f+H_d$, with $\|V_p\|\le h_p$. The complete target is the evolving clock state tensor the freely evolved body $J_*\rho J_*$, including its retained spectator. Distance to this target need not mean successful capture if the incoming production state is nonterminal.

Under these premises, the complete joint bound is

\[
\epsilon(t)\le\min\{1,th_p+2|\cos(\lambda t)|^N\}.
\]

For $\pi/(4\lambda)\le t\le3\pi/(4\lambda)$,

\[
\epsilon(t)\le\min\{1,3\pi h_p/(4\lambda)+2\,2^{-N/2}\}.
\]

Writing $r=|\cos(\lambda t)|^{2N}$, the comparison reduced-body distance is at most $r$. For incoming nonterminal probability $p$ and fresh records, its NO_CAPTURE probability is $p+(1-p)r$. The smaller reduced-body tail cannot replace the full joint term when clock correlations remain relevant. Appendix D.6 gives a tighter joint bound under explicitly stated fresh-record conditions. The comparator transfers exactly halfway through its cycle and undoes the transfer at a full cycle. These are pointwise bounds, not continuously monitored survival probabilities.

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

Independence means the exact product input written above, including the whole history; equal donor marginals are insufficient. For static renewal the active module includes its capture clock. The identity is kinematic; an implemented exchange requires a generator and a comparison against running contacts [4, §8.1]. The active module is refreshed; all old correlations are exported to donor and history. They are not destroyed. Repetition consumes fresh donor and output slots, and failures consume resources too.

On matching full joint domains, admitted bank error $\epsilon_F$ and operation comparisons $\epsilon_j$ compose unconditionally as

\[
\epsilon_{\mathrm{total}}
\le\min\{1,\epsilon_F+\sum_j\epsilon_j\}.
\]

This requires uniform operation bounds on the admitted joint states. Isolated-input results do not automatically meet that requirement. The bank error is charged once; diagnostics already covered by it are not charged again as independent errors.

## 11.2 Coherent supply is a resource

The source constructs a uniform reference packet of length $L=2^q$ from a seed and supplied coherent binary fuel [4, Theorem IV.2]. Here $\Delta>0$, fuel qubit $j$ has Hamiltonian $\Delta2^j|1\rangle\langle1|$ and state $|+\rangle$, and the independent reference begins at seed $|n_0\rangle$ on a sufficiently long finite ladder. The seed energy $n_0\Delta$ is additional to fuel energy. Matched disjoint exchanges transfer the supplied coherence into the reference. Ideal independent fuel has

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

## 11.4 What a prepared stationary ratio does and does not explain

A supplied dissipative channel can have a stable population ratio while retaining coherence much longer than a population readout suggests. Appendix D.11 examines a two-state channel motivated by the partner working notes [23]. Its stationary state is $\operatorname{diag}(4/7,3/7)$, but its sharp trace-distance contraction per application is $(1+\sqrt2)/\sqrt6\simeq0.985599$, rather than the proposed $5/7$. Population polarization instead relaxes at magnitude $1/6$. The whole state must accompany a retained-distinguishability claim.

The ratio $4/3$ is reverse-rate divided by forward-rate for the chosen rates $2/3$ and $1/2$. An explicit third-state branch changes it to $(4/3)\alpha$. This is a conditional formation mechanism, not a derivation of a coframe ratio from incidence geometry. A channel can be dilated using a supplied environment, but its mathematical operators specify neither the environment's Hamiltonian nor renewal and switching costs. Those resources remain required before making an information-per-cost comparison.

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

The additional receipt audit sharpens this requirement. A collection of labels with zero individual Hamming change is not itself a composable history, and the zero change does not determine an unobserved winding. To assign a winding-dependent cost, specify the fine-history domain, its admissible composition, the winding functional and what the receipt retains. Appendix D.12 gives a counterexample to inferring winding from fixed-weight labels alone. This is a source-law gap, not an argument against possible laws that supply the missing information.

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

The version-0.9 partner ingestion preserves the complete supplied working-note file and audits selected material claim families. It does not certify every imported formula or image. Important corrections include a general-metric counterexample to an overbroad subdivision obstruction and the sharp two-state contraction factor. Reference [23] identifies the source and independent replay. Constructor checks are not independent review.

The version-0.10 ingestion audits three additional partner working-note documents against the supplied v0.39 coefficient ledger and CRL-2 governance proposal. It integrates the receipt/history and cost-inference repairs, while preserving disconnected finite-group results and transport counterexamples in the companion audit [24]. Imported status labels do not constitute promotion receipts.

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

## D.6 Refined static joint error under an explicit input contract

**Proposition D6 (conditional refinement).** Use the §10.2 static comparator and a fresh independent clock at address 0. Put $r=\cos^{2N}(\lambda t)$ and $x=\operatorname{Tr}(\rho J_*)\in[-1,1]$. Its complete body/clock/spectator trace distance from the fully transferred product target is at most

\[
\sqrt{1-(1-r+rx)^2}.
\]

For an arbitrary admitted body input a uniform bound is

\[
g(r)=\begin{cases}2\sqrt{r(1-r)},&0\le r\le1/2,\\1,&1/2\le r\le1.\end{cases}
\]

If $L,M,E$ are exactly blank and independent of the incoming body/history, then $x=p$, the incoming production nonterminal probability. In particular, a wholly terminal input ($p=0$) gives joint error at most $\sqrt{2r-r^2}$. Actual evolution adds at most $th_p$ to each applicable bound, capped at one. Input preparation error is a separate additive distance, not an amplitude-square term.

**Proof.** Purify the body and its spectator as $|\psi\rangle$. The comparator vector uses $|\psi\rangle$ at clock address 0 and $J_*|\psi\rangle$ at every other address, with common free evolution. The target uses $J_*|\psi\rangle$ at every address. Their inner product is $1-r+rx$, since the address-0 probability is $r$ and $J_*$ is Hermitian. Pure-state trace distance gives the first expression; discarding a purification register contracts distance. Minimizing $|1-r+rx|$ over $x\in[-1,1]$ gives $g$. With fresh records the terminal summand flips their blank state to an orthogonal state, while the nonterminal summand is identity, so $x=p$. Lemma IV.1 supplies the actual/comparator debit.

For a pure terminal input with fresh records the joint value $\sqrt{2r-r^2}$ is exact, whereas the reduced-body distance is exactly $r$ because the two branches have orthogonal record states. Thus the joint/marginal distinction persists even after tightening. A small distance to a target constructed from nonterminal inputs does not certify that a record was written. These bounds are an additional finite derivation in this manuscript, not an amendment to the preserved Paper IV theorem or an independent-review receipt.

## D.7 Signed characters, channel completeness and the standard Dirac relation

**Proposition D7.** Under the signed full-$S_4$ action and unit simplex metric, the decomposition and commutant counts in §5 follow from the character table below. The three generator channels span the full equivariant skew family.

Conjugacy classes are ordered as identity, transposition, double transposition, 3-cycle and 4-cycle, with sizes $(1,6,3,8,6)$.

| Character | Identity | $(12)$ | $(12)(34)$ | $(123)$ | $(1234)$ |
|:--|--:|--:|--:|--:|--:|
| $A_1$ | 1 | 1 | 1 | 1 | 1 |
| $A_2$ | 1 | -1 | 1 | 1 | -1 |
| $E$ | 2 | 0 | 2 | -1 | 0 |
| $T_1$ | 3 | -1 | -1 | 0 | 1 |
| $T_2$ | 3 | 1 | -1 | 0 | -1 |
| $C_0$ | 4 | 2 | 0 | 1 | 0 |
| $C_1$ | 6 | 0 | -2 | 0 | 0 |
| $C_2$ | 4 | -2 | 0 | 1 | 0 |
| $C_3$ | 1 | -1 | 1 | 1 | -1 |

**Proof.** Signed oriented $k$-chains are $\Lambda^{k+1}P$, with $P$ the four-vertex permutation representation. Traces of these exterior-power actions give the four chain rows. Taking the weighted character inner product $\langle\chi,\psi\rangle=\frac1{24}\sum_jn_j\chi_j\psi_j$ gives the §5 multiplicities. The five real irreducibles have irreducible complexifications, so their real endomorphism algebra is scalar. Multiplicities $(1,2,2,2)$ therefore give full, self-adjoint and skew-adjoint commutant dimensions $13,10,3$.

Each $G_k$ is nonzero, skew and equivariant; their adjacent blocks have disjoint positions, so they are independent and span the three-dimensional skew family. Boundary multiplication gives $G_iG_j=0$ for $i\ne j$, and $G_k^2=-4\Pi_k$ with symmetric idempotent projectors of ranks $(6,6,2)$. The rank-one remainder is the uniform vertex mode. On each image, $G_k/2$ squares to minus identity; hence the weighted characteristic polynomial in §5.1 follows. This proves sector completeness even at zero or coincident weights.

The symmetric-square character $(\chi(g)^2+\chi(g^2))/2$ reduces to $A_1+E+T_2$. Likewise the multiplicity of $T_2$ in $E\otimes R$ is zero for $R=A_1,A_2,E$ and one for $R=T_1,T_2$. Complete reducibility extends the minimum-dimension conclusion to reducible contexts: a contributing three-dimensional irreducible summand is required.

Finally, let $B$ be the block upper-triangular boundary operator, $D=B+B^T$ and $U=\bigoplus_{k=0}^3 i^k I_{C_k}$. Then

\[
U D U^\dagger=i(B^T-B)=i\mathcal A.
\]

This complex unitary phase change identifies the Hermitian spectrum with the standard simplicial Dirac spectrum. It is a mathematical comparison, not a physical identification of the real carrier with a quantum state. For a filled tetrahedron it recovers the established single-cell spectrum [18].

The replay constructs all 24 signed actions, checks 576 group compositions and 72 boundary equivariance identities, and verifies the weighted polynomial and projectors exactly. It also reconstructs the Paper III §10.1 compatible context tensor and checks 72 covariance identities. These are constructor certificates for the written argument; they do not establish novelty or physical coupling strength.

## D.8 General gluing and minimal dynamic memory

### D.8.1 lossless normalized gluing

There is an orthogonal completion $U=(Q;R)$, with $n-m$ residual rows, such that

\[
\|x\|^2=\|Qx\|^2+\|Rx\|^2.
\]

Among linear lossless encodings retaining these m visible coordinates, at least n-m additional real coordinates are required. This is a state-dimension theorem, not a physical bit or energy cost.

**Proof.** Different visible rows have disjoint copied-simplex supports, and each row has squared norm $\nu_\sigma/\nu_\sigma=1$. Complete the rows by an orthonormal basis of $\ker Q$. Orthogonality proves the identity. An injective linear encoding of an n-dimensional state has rank n, so m+r output coordinates require $r\ge n-m$. If the copies all equal $c_\sigma$ on a simplex, $Qx=\sqrt{\nu_\sigma}c_\sigma$; recovering the native coordinate requires division by $\sqrt{\nu_\sigma}$. Native and copied norm conventions differ.

### D.8.2 minimal autonomous linear memory

For any real skew $A$ on $\mathbb R^n$ and $Q$ with $m$ orthonormal rows, define

\[
\mathcal O=(Q;QA;\ldots;QA^{n-1}),\qquad d=\operatorname{rank}\mathcal O.
\]

To reproduce $Qe^{sA}x_0$ exactly for every $x_0$ and $s\ge0$ using a time-independent autonomous linear state model, initialized by a linear encoding of $x_0$ and retaining $Qx$ as its first $m$ coordinates, the minimum number of additional state coordinates is $d-m$.

**Proof.** The observable subspace $W=\operatorname{im}\mathcal O^T$ is $A$-invariant by Cayley-Hamilton and skewness. Its orthogonal complement is also invariant. The subspace $W$ contains $\operatorname{im}Q^T$. Choose an orthonormal basis for W starting with the rows of Q and extend them by d-m rows H in W intersect $\ker Q$. With $T=(Q;H)$, $F=TAT^T$ is skew and $TA=FT$, so the d-dimensional model reproduces the visible trajectory exactly. Conversely, any linear initial encoding C supporting exact future outputs has $\ker C\subseteq\ker\mathcal O$: a state encoded as zero must have every visible derivative zero. Hence $\operatorname{rank}C\ge d$ and at least d-m extra coordinates are required. This lower bound concerns exact finite autonomous linear realizations for arbitrary initial states; it is not a bound for one fixed preparation, a nonlinear encoding or an apparatus with external stored history.

The underlying observability construction is established control theory. The skew case permits an orthogonal reducing realization. The gluing-specific contribution is the concrete observation, its dimension and the structural rank argument below. No priority claim is made for the general observability principle.

### D.8.3 fresh-vertex stacked tetrahedra require all residuals

Start with one tetrahedron and attach each later tetrahedron along one boundary face using a new vertex. In each copied cell let all three adjacent-degree weights $a_j,b_j,c_j$ be nonzero real constants; they need not agree between cells.

Then

\[
n=15t,\qquad m=8t+7,\qquad
\operatorname{rank}(Q;QA)=15t.
\]

Consequently $d=n$, and exactly $7(t-1)$ additional coordinates are required by §D.8.2. The visible/residual derivative coupling has rank $7(t-1)$. For $t=1$ this count is zero.

**Proof.** Attachment adds 1 vertex, 3 edges, 3 faces and 1 cell, so the unique register grows by 8 from its initial 15 coordinates. Consider the last attached tetrahedron, with fresh vertex v. Its eight simplex coordinates containing v occur in no earlier cell. If $Qx=0$ they vanish in this last copy. If $QAx=0$ their local derivatives also vanish, because the copied generator is block diagonal.

The remaining seven coordinates belong to the attachment face. The map from these face coordinates to derivatives of the eight private coordinates has Gram matrix

\[
C^TC=\operatorname{diag}(a_j^2,a_j^2,a_j^2,
b_j^2,b_j^2,b_j^2,c_j^2).
\]

Indeed each face vertex contributes through its new edge to v, each face edge through its new face containing v, and the attachment face through the new cell; orientation signs disappear in the Gram matrix. Nonzero weights make this map injective. Thus the last copied cell is zero. Remove it and repeat backwards: contributions of already-zero later copies vanish in both $Qx$ and $QAx$, and every remaining row normalization is nonzero. Finally the original copy is zero. Therefore $\ker Q\cap\ker(QA)=\{0\}$, proving the rank claim. On $\ker Q$, $QA$ is injective, so its rank is $n-m$, which is the visible/residual coupling rank under any orthogonal residual basis.

This proves a family result, not just a rank observation on the two-cell fixture. It also identifies the hypotheses: fresh-vertex attachment, separate copied generators, nonzero exchange weights, and unrestricted copied initial states. Cyclic gluing or a zero channel need not satisfy the conclusion.

### D.8.4 Exact projected dynamics

In orthogonal visible/residual coordinates, write $UAU^T$ as blocks $G_{vv},G_{vr},G_{rv},G_{rr}$. Eliminating the residual gives

\[
z'(s)=G_{vv}z(s)+G_{vr}e^{sG_{rr}}r_0
+\int_0^sG_{vr}e^{(s-u)G_{rr}}G_{rv}z(u)\,du.
\]

This follows directly from variation of constants in $r\prime=G_{rv}z+G_{rr}r$. The initial residual term cannot be discarded for arbitrary preparation. The kernel is a deterministic memory term; it is not automatically physical noise or dissipation. Skewness gives $G_{rv}=-G_{vr}^T$, so its instantaneous value is $-G_{vr}G_{vr}^T$, but its time dependence and initial term retain the underlying reversible dynamics. This is the linear projection/memory mechanism familiar from Mori-Zwanzig reduction, not a new irreversible entropy law.


## D.9 Conditioning, noise and sampled acquisition

### D.9.1 Declared readout and its conditioning

Use the copied-state generator $A^T=-A$ and normalized gluing observation $Q$, with $QQ^T=I_m$, from the stacked-family theorem. The copied state has $n$ real coordinates. Declare an observation scale $\tau>0$ and

\[
y=M_\tau x+e,\qquad M_\tau=\begin{pmatrix}Q\\\tau QA\end{pmatrix},
\quad e=\begin{pmatrix}e_0\\\tau e_1\end{pmatrix}.
\]

Here $e_1$ is raw derivative error; its acquisition is not assumed free. The scale makes the two blocks commensurate in the chosen model units. It is not a new dynamical coefficient or a physical clock calibration. Assume full column rank when reconstructing the complete state.

Define

\[
H_\tau=M_\tau^TM_\tau=P+\tau^2A^TPA,
\quad P=Q^TQ,
\quad\gamma_\tau=\sqrt{\lambda_{\min}(H_\tau)}>0.
\]

The absolute noise gain is $1/\gamma_\tau$. The relative matrix condition number is $\kappa_2(M_\tau)=\sigma_{\max}(M_\tau)/\gamma_\tau$. These are different quantities.

**Theorem C1 (sharp deterministic error).** The least-squares reconstruction $\widehat x=M_\tau^\dagger y$ satisfies

\[
\boxed{\|\widehat x-x\|\le
\frac{\sqrt{\epsilon_0^2+\tau^2\epsilon_1^2}}{\gamma_\tau}}
\quad\text{if }\|e_0\|\le\epsilon_0,\ \|e_1\|\le\epsilon_1.
\]

As a bound in the combined error norm $\|e\|$, the factor $1/\gamma_\tau$ is attained by error along a least singular left vector. Separate block budgets need not attain this combined bound simultaneously.

**Proof.** Full rank gives $M_\tau^\dagger M_\tau=I$. Hence $\widehat x-x=M_\tau^\dagger e$, and the pseudoinverse norm is $1/\gamma_\tau$. A singular-vector error attains the norm. This is standard SVD-based least-squares conditioning, specialized to the declared observation.

If $M_\tau$ is rank deficient, no finite bound recovers arbitrary full states even at zero noise. The pseudoinverse recovers only the projection onto its row space. That space need not equal the full time-observable subspace when higher derivatives are required.

### D.9.2 Generator uncertainty and usable certificates

Let $\bar A$ be the reconstruction model, $\|A-\bar A\|\le\delta$, with the same exact $Q$. Set $\bar M_\tau=(Q;\tau Q\bar A)$ and $\bar\gamma_\tau=\sigma_{\min}(\bar M_\tau)$. For $\|x\|\le R$,

\[
\boxed{\|\bar M_\tau^\dagger y-x\|\le
\frac{\sqrt{\epsilon_0^2+\tau^2\epsilon_1^2}+\tau\delta R}
{\bar\gamma_\tau}.}
\]

This assumes $\bar\gamma_\tau>0$. It owns model mismatch separately from measurement noise. Since $\|M_\tau-\bar M_\tau\|\le\tau\delta$, minimization over unit vectors gives

\[
|\gamma_\tau-\bar\gamma_\tau|\le\tau\delta.
\]

Thus a certified true lower bound $\gamma_\tau\ge\Gamma$ guarantees reconstruction-model injectivity when $\tau\delta<\Gamma$, with denominator at least $\Gamma-\tau\delta$.

**Proof.** Write $y=\bar M_\tau x+e+(M_\tau-\bar M_\tau)x$ and apply C1. The singular-value inequality follows from $\|\bar Mv\|\ge\|Mv\|-\|(\bar M-M)v\|$ for unit $v$, and then interchange the matrices. No small-error expansion is used.

For exact rational $H_\tau$, a rational LDL factorization of $H_\tau-qI$ with positive pivots certifies $\gamma_\tau>\sqrt q$. Floating eigenvalues may suggest $q$ but do not certify it. A general, usually conservative, bound is

\[
\gamma_\tau\ge
\frac{\sqrt{\det H_\tau}}{(1+\tau^2\|A\|^2)^{(n-1)/2}},
\]

because every Gram eigenvalue is at most $1+\tau^2\|A\|^2$. Positivity of the determinant is available only after full rank is established. Unknown errors in $Q$ require an additional observation-model term and are not included in $\delta$.

### D.9.3 Gaussian noise, correlations and representation invariance

Assume the complete error $e$ is zero-mean Gaussian with known positive-definite covariance $\Sigma$, independent of the unknown fixed state. The generalized least-squares estimate and information matrix are

\[
\widehat x=I_\Sigma^{-1}M_\tau^T\Sigma^{-1}y,
\qquad I_\Sigma=M_\tau^T\Sigma^{-1}M_\tau.
\]

**Theorem C2 (exact covariance and confidence region).** Under full column rank and the exact measurement model,

\[
\operatorname{Cov}(\widehat x-x)=I_\Sigma^{-1},\qquad
\mathbb E\|\widehat x-x\|^2=\operatorname{tr}(I_\Sigma^{-1}),
\]

\[
\Pr\!\left[(\widehat x-x)^TI_\Sigma(\widehat x-x)
\le\chi^2_{n,1-\alpha}\right]=1-\alpha.
\]

In particular, a Euclidean confidence radius is

\[
\|\widehat x-x\|\le
\sqrt{\chi^2_{n,1-\alpha}/\lambda_{\min}(I_\Sigma)}.
\]

**Proof.** The estimator error is the displayed linear map applied to $e$. Multiplying its covariance gives $I_\Sigma^{-1}$. Whiten this $n$-dimensional Gaussian error to obtain the chi-square statement. The radius follows from the smallest information eigenvalue. Gaussianity is needed for this exact coverage, not for the covariance identity. Bias, covariance estimation and non-Gaussian tails need separate bounds.

For equal-prior alternatives separated by $\Delta x$ under the same covariance, the exact optimal decision error is

\[
P_e=\Phi\!\left(-\tfrac12\sqrt{\Delta x^TI_\Sigma\Delta x}\right)
\le\Phi\!\left(-\tfrac12\sqrt{\lambda_{\min}(I_\Sigma)}\|\Delta x\|\right).
\]

This follows by the likelihood-ratio projection onto $\Sigma^{-1}M_\tau\Delta x$. It is distinguishability of the readout distributions, not information already written into a retained physical memory.

For an invertible output rescaling $S$, transport all three objects:

\[
y\mapsto Sy,\quad M\mapsto SM,\quad
\Sigma\mapsto S\Sigma S^T.
\]

Then $I_\Sigma$ is unchanged. Increasing $\tau$ on paper cannot improve statistical information while leaving the raw noise physics fixed. An unweighted singular value can change under this rescaling; a consistent whitened calculation cannot. Correlated observations require the full covariance, including cross-block terms.

### D.9.4 Derivative acquisition from three snapshots

Observe $y_-,y_0,y_+$ at $s_0-h,s_0,s_0+h$, with $h>0$ and $s_0\ge h$. Prepare the state and retain its history under the same constant generator throughout. Define

\[
D_h=\frac{y_+-y_-}{2h}.
\]

If each endpoint has norm error at most $\epsilon$, $\|A\|\le L$ and $\|x(s_0)\|\le R$, then

\[
\boxed{\|D_h-QAx(s_0)\|
\le\frac\epsilon h+\frac{L^3Rh^2}{6}.}
\]

**Proof.** Endpoint errors contribute at most $2\epsilon/(2h)$. The third derivative of $Qx$ is $QA^3x$, whose norm is at most $L^3R$ by skew-flow norm preservation. The centered Taylor remainder gives the second term. No noiseless derivative is assumed.

Finite precision and timing fit the same budget. Suppose each $m$-coordinate snapshot has additional detector error at most $\epsilon_{\rm det}$, componentwise rounding to nearest with step $q$ and no saturation, and timestamp error at most $j$. Its total deterministic error is at most

\[
\epsilon_{\rm eff}=\epsilon_{\rm det}+\frac{\sqrt m\,q}{2}+LRj.
\]

The rounding vector has at most $q/2$ in each component, and integrating $\|Qx'\|\le LR$ over the timing offset gives the last term. Use the appropriate effective budget for each center/endpoint in C1 and the difference formula. Correlated or stochastic timing errors are not thereby independent Gaussian noise.

Substitute this derivative error into C1. For this conservative derivative-approximation bound alone, the unconstrained minimizing step is

\[
h_*=(3\epsilon/(L^3R))^{1/3},
\]

when $L,R,\epsilon>0$. Actual latency or admissible-time restrictions may exclude it. This is a minimum of the bound, not a universal sampling optimum.

For independent endpoint Gaussian errors with covariance $\sigma^2I_m$, derivative-noise covariance is $\sigma^2I_m/(2h^2)$. With an independent center snapshot of the same noise, the cross covariance with $y_0$ is zero. The derivative mean-square error obeys

\[
\mathbb E\|D_h-QAx\|^2\le
\frac{m\sigma^2}{2h^2}+\frac{L^6R^2h^4}{36}.
\]

Its unconstrained bound-minimizing step satisfies $h_*^6=9m\sigma^2/(L^6R^2)$. Shared temporal noise changes these formulas. A three-snapshot acquisition uses $3m$ scalar readout channels over a span $2h$, plus clock alignment, bandwidth and storage resources; this is not a complete energy cost.

### D.9.5 Exact canonical sampling avoids truncation bias

For the canonical independent-copy generator, $A^3=-4A$. Consequently

\[
\frac{e^{hA}-e^{-hA}}{2h}
=f(h)A,\qquad f(h)=\frac{\sin(2h)}{2h}.
\]

This can be used as the exact measurement matrix rather than approximating the derivative. The retained statistic $(y_0,D_h)$ has

\[
M_h=\begin{pmatrix}Q\\f(h)QA\end{pmatrix},\qquad
\Sigma_h=\sigma^2\operatorname{diag}(I_m,I_m/(2h^2))
\]

under the independent equal-noise three-snapshot contract. Its information matrix is exactly

\[
\boxed{I_h=\sigma^{-2}
\left[P+\frac{\sin^2(2h)}2A^TPA\right].}
\]

Thus $h=\pi/4$ maximizes this information matrix in Loewner order over $0<h<\pi/2$. It is a model-unit optimum for this retained statistic under fixed snapshot noise; it is not an optimum over every sensor, time budget or the full three-snapshot record. The symmetric endpoint sum has been discarded. At $h=k\pi/2$, $k\ne0$, the derivative statistic loses its active signal, so this two-block readout is rank deficient for a nontrivial stack.

**Proof.** On harmonic modes both sides of the first identity vanish; on every active mode $A$ has frequency 2, giving the sine factor. The covariance inverse contributes $2h^2/\sigma^2$, which cancels the factor $1/(4h^2)$ in $f(h)^2$. The remaining coefficient is maximized when $\sin^2(2h)=1$. At its zeros, only the snapshot remains. Calibrating the exact matrix removes Taylor bias, not noise amplification or acquisition cost.

### D.9.6 Exact two-cell and five-cell conditioning

The following values concern independent copied dynamics and the normalized union observation, with $\tau=1/2$ and canonical weights. They are not the native union-generator frequencies. All copied generators have norm 2.

| Configuration | $n$ | $m$ | Minimum Gram eigenvalue | Absolute error gain $1/\gamma$ |
|:--|--:|--:|:--|:--|
| Two cells, shared face | 30 | 23 | $1-\sqrt3/2$ | $1+\sqrt3\approx2.73205$ |
| Five-cell core-star | 75 | 47 | $1-\sqrt{15}/4$ | $\sqrt2(\sqrt5+\sqrt3)\approx5.61177$ |
| Five-cell chain | 75 | 47 | Smallest root of $64z^4-256z^3+280z^2-48z+1$ | Approximately 6.43292 |

For the chain, exact LDL and Sturm checks place the minimum Gram eigenvalue in $(241/10000,243/10000)$. Hence an entirely rational certificate gives error gain below $100/\sqrt{241}$. The decimal estimate is more precise but is not itself the certificate. All three maximum Gram eigenvalues are 2, so their relative condition numbers are $\sqrt2$ times the listed absolute gains.

**Proof for two cells.** The exact Gram polynomial factors as

\[
\frac{(z-2)^{14}(z-1)(4z-7)(4z^2-8z+1)^7}{2^{16}}.
\]

Its smallest root is $1-\sqrt3/2=((\sqrt3-1)/2)^2$. Inverting its square root gives $1+\sqrt3$. The star's exact factorization, stored in the certificate, has its smallest root in $16z^2-32z+1$. All its other factor roots are at least this value. For the chain, the full characteristic polynomial's square-free part has exactly one root in the certified interval and none between zero and its lower endpoint; that root belongs to the displayed quartic. These statements are checked in exact arithmetic.

For the same combined output error budget 0.01, worst-case state errors are at most approximately 0.02732, 0.05612 and 0.06433 respectively. These are worst-direction readout comparisons. They do not establish universal architecture superiority or equal physical expenditure.

### D.9.7 Exact recoverability has no uniform robustness guarantee

Even keeping the copied-generator norm equal to 2 does not give a positive uniform $\gamma$ over all nonzero weights. In the two-cell example set $a=b=1$, $c=\varepsilon>0$ in each cell. Let $v$ be the unit difference of their shared-face coordinates. Then

\[
Qv=0,\qquad\|QAv\|=\varepsilon,
\qquad\gamma_\tau\le\tau\varepsilon.
\]

Therefore the snapshot/derivative noise gain is at least $1/(\tau\varepsilon)$ and diverges as $\varepsilon\downarrow0$, although exact rank remains full for every positive $\varepsilon$. The other channels keep $\|A\|=2$. At $c=0$ a higher derivative can restore time observability, so this is specifically a failure of uniform robustness of the declared two-block readout, not a theorem that all possible observation histories fail.

For full-state reconstruction on the closed five-cell boundary, the two-block matrix has a 20-dimensional kernel even before noise. Restricting to its certified observable subspace permits positive singular-value bounds there; adding a finite noise budget cannot identify the discarded directions.

### D.9.8 Scope, verification and references

The pseudoinverse, whitening and Gaussian arguments are standard statistical linear algebra. The specialized results here are their application to the declared gluing observation, its exact spectra, the fixed-norm degenerating family and the exact canonical sampling contract. Constructor replay supplies exact characteristic-polynomial/LDL/Sturm certificates plus separately labelled floating fixtures. It does not estimate a physical noise covariance, establish independent review, certify measured bandwidth or prove a physical entropy-area relation.

Primary background: LAPACK *Users' Guide*, [Linear Least Squares Problems](https://www.netlib.org/lapack/lug/node27.html), and [How to Measure Errors](https://www.netlib.org/lapack/lug/node75.html). General perturbation literature includes G. W. Stewart, [On the Perturbation of Pseudo-Inverses, Projections and Linear Least Squares Problems](https://doi.org/10.1137/1019104); only its abstract/metadata were inspected, so no specific theorem from its paywalled text is invoked here. The displayed bounds have self-contained proofs.

Next requirements for operational use are calibrated joint covariance, acquisition and clock-error models, admissible sampling windows, generator uncertainty and a complete resource ledger. The derivation closes a mathematical conditioning gap while leaving those physical inputs explicit.


## D.10 Recurrence and transfer under explicit metric contracts

### D.10.1 Incommensurability permits uniformly close returns

Let $A$ be a finite real skew matrix with $r\ge1$ distinct positive frequencies $\omega_1,\ldots,\omega_r$. For every integer $N\ge1$ there is $1\le q\le N^{r-1}$ such that, at $s=2\pi q/\omega_1$,

\[
\|e^{sA}-I\|_2\le\frac{2\pi}{N}.
\]

For $r>1$, partition the $(r-1)$-torus into $N^{r-1}$ cubes of side $1/N$. Among the $N^{r-1}+1$ points with coordinates $\{j\omega_k/\omega_1\}$, $j=0,\ldots,N^{r-1}$ and $k=2,\ldots,r$, two share a cube. Their index difference is the required $q$, with each phase within $2\pi/N$ of an integer multiple of $2\pi$. Orthogonal block diagonalization of $A$ reduces the operator error to the largest rotation-block error, bounded by the phase error. Zero modes contribute zero error. For $r=1$, choose $q=1$ and the return is exact. If $r=0$, the flow is the identity.

Consequently, irrational frequency ratios exclude an exact common period but do not exclude approximate recurrence. If there is no exact period, the approximating times have an unbounded subsequence; otherwise a bounded subsequence would yield an exact return as $N\to\infty$. In the periodic case, arbitrarily late exact returns exist. This is a finite-flow statement; no thermodynamic limit, mixing, dissipation or record formation follows from it.

### D.10.2 A protected sector for a specified inclusion

Use the complexes $K_A,K_B$ of §6.1 and the coordinate inclusion $T:\mathbb R^{23}\to\mathbb R^{27}$ that fixes every simplex of $K_A$. This is an inclusion of subcomplexes, not a boundary-fixing 2-to-3 replacement. Write $A=\mathcal A_{K_A}$, $B=\mathcal A_{K_B}$ and $L=-A^2$. With unit metrics,

\[
T^TT=I,\quad d_BT=Td_A,\quad R=BT-TA,
\]

where $d$ is the total boundary. Exact signed incidence gives

\[
\operatorname{rank}R=4,\quad RR^TR=2R,\quad
\operatorname{rank}\begin{pmatrix}R\\RA\end{pmatrix}=8.
\]

Thus the four nonzero singular values of $R$ are $\sqrt2$. The polynomial projectors are

\[
P_0=\frac{(L-3I)(L-5I)}{15},\quad
P_3=\frac{L(5I-L)}6,\quad P_5=\frac{L(L-3I)}{10}.
\]

They are mutually orthogonal and sum to $I$. Direct incidence identities give $R(P_0+P_5)=0$ and $\operatorname{rank}(P_0+P_5)=15$. Since this projector commutes with $A$, its image lies in the kernel of every $RA^j$. The displayed rank-eight two-block matrix shows that no larger protected space exists. Therefore

\[
\bigcap_{j\ge0}\ker(RA^j)=\operatorname{im}(P_0+P_5),\qquad
e^{sB}Tx=Te^{sA}x
\]

for precisely these initial states. A zero instantaneous residual alone would give a larger, insufficient kernel.

The remaining eight-dimensional sector admits a more detailed description. Put $L_B=-B^2$ and $P^B_2=L_B(5I-L_B)/6$. The positive compression

\[
W=P_3T^TP^B_2TP_3
\]

has rank four and satisfies $W^2=(2/3)W$. On $\operatorname{im}P_3$ its eigenvalues are $2/3$ and $0$, each fourfold. Corresponding normalized states have squared spectral-projection weights $(2/3,1/3)$ or $(0,1)$ in the $L_B=2,5$ sectors. These are instantaneous spectral weights after a stipulated inclusion, not transmission probabilities of a derived scattering experiment. Their exact matrices and ranks are replayed in [23].

### D.10.3 Stellar subdivision: diagonal obstruction and a general-metric counterexample

Subdivide $[0123]$ using interior vertex 4 into $0124,0134,0234,1234$. Let $d_c,d_f$ be the coarse and fine total boundaries. The map $S$ fixes the old boundary and sends the oriented top cell to

\[
S[0123]=[0124]-[0134]+[0234]-[1234].
\]

Then $d_fS=Sd_c$ and $S^TS=I_{14}\oplus[4]$. Boundary fixation and the unique filling force this image: the fine $d_3$ is injective. Hence this map cannot be an isometry for unit simplex metrics.

For a positive *diagonal* fine metric $H$, the adjoint is $d_f^{\dagger_H}=H^{-1}d_f^TH$. Adjoint intertwining on the old four boundary faces would require a matrix with four separate nonzero face-to-cell entries to equal the rank-one matrix $S_3d_{c,3}^T$. Positive diagonal weights cannot change these ranks. Thus diagonal weighting alone cannot provide this stronger intertwining contract.

That argument does not exclude all positive metrics. Define the simplicial chain retraction $\Pi$ by sending vertex 4 to 0 and fixing 0,1,2,3; a simplex with repeated image vertices maps to zero, and other images carry their permutation sign. It obeys

\[
\Pi S=I,\qquad \Pi d_f=d_c\Pi.
\]

Put $N=I-S\Pi$ and choose the degree-preserving, generally non-diagonal metric

\[
H=\Pi^T\Pi+N^TN.
\]

For any $v$, $v^THv=\|\Pi v\|^2+\|Nv\|^2>0$ unless $v=0$, since $v=S\Pi v+Nv$. Also $S^THS=I$. The decomposition $\operatorname{im}S\oplus\ker\Pi$ is $H$-orthogonal and each summand is $d_f$-invariant. Therefore the weighted adjoint preserves the same summands and restricts on $\operatorname{im}S$ to the coarse Euclidean adjoint. It follows that

\[
A_H=H^{-1}d_f^TH-d_f,\qquad
A_HS=S(d_c^T-d_c),\qquad A_H^TH+HA_H=0.
\]

This explicitly refutes an unrestricted positive-metric no-go. It does not supply unit-metric intertwining or a native choice of $H$. The weighted generator is an added model, with correlated simplex coordinates; its locality and physical admissibility require a separate contract. The supplied certificate verifies all identities exactly and gives positive rational LDL pivots [23].

## D.11 A prepared channel: retained coherence, fixed ratios and branching

The following operators are declared mathematical channels, motivated by the partner working notes [23]. They are not derived from a UD carrier-to-bath interaction. For a two-state Hilbert space, take

\[
K_0=\begin{pmatrix}1/\sqrt2&0\\0&1/\sqrt3\end{pmatrix},\qquad
K_1=\begin{pmatrix}0&\sqrt{2/3}\\1/\sqrt2&0\end{pmatrix},\qquad
\mathcal E(\rho)=\sum_{j=0}^1K_j\rho K_j^\dagger.
\]

Completeness is $\sum_jK_j^\dagger K_j=I$. In Bloch coordinates $\rho=(I+r_x\sigma_x+r_y\sigma_y+r_z\sigma_z)/2$, direct multiplication gives

\[
r_x'=a_xr_x,\quad r_y'=a_yr_y,\quad
r_z'=-r_z/6+1/6,
\qquad a_x=\frac{1+\sqrt2}{\sqrt6},\quad
a_y=\frac{1-\sqrt2}{\sqrt6}.
\]

All linear eigenvalues have modulus less than one, so the unique fixed point is $\rho_*=\operatorname{diag}(4/7,3/7)$. The repeated channel has $r_x(k)=a_x^kr_x(0)$, $r_y(k)=a_y^kr_y(0)$ and $r_z(k)-1/7=(-1/6)^k(r_z(0)-1/7)$. Coherences decay asymptotically; they are not erased in one step.

For qubit states, trace distance is half the Euclidean distance of their Bloch vectors. The sharp one-step contraction coefficient, and its $k$-step counterpart, are consequently

\[
\eta(\mathcal E)=a_x\simeq0.985599,\qquad
\eta(\mathcal E^k)=a_x^k.
\]

Opposite $\sigma_x$ eigenstates attain the bound. The same sharp factor applies to distance from $\rho_*$ by taking sufficiently small $x$-axis perturbations around that full-rank state. Thus $(5/7)^k$ is not a valid universal bound for this channel. An additional projection could change a contracted readout, but requires its own defined action and comparison domain.

The population transition rates are $u=1/2$ from state 1 to 2 and $v=2/3$ from 2 to 1. For arbitrary $0<u,v<1$, the same construction with $K_0=\operatorname{diag}(\sqrt{1-u},\sqrt{1-v})$ and off-diagonal $K_1$ yields stationary populations $(v,u)/(u+v)$. Therefore $p_1^*/p_2^*=v/u$. The value $4/3$ follows from the chosen rates; its numerical agreement with a separately stated geometric ratio does not derive those rates or identify the populations with that geometry. At some other rates the population fixed point need not be the unique full-state fixed point; uniqueness above was proved for the displayed channel.

A three-state extension makes the dependence explicit. For $0\le\alpha\le1$, let

\[
K_0=\operatorname{diag}(1/\sqrt2,1/\sqrt3,1/\sqrt7),
\]
\[
K_1=\begin{pmatrix}0&\sqrt{2\alpha/3}&0\\1/\sqrt2&0&0\\0&0&0\end{pmatrix},\qquad
K_2=\begin{pmatrix}0&0&0\\0&0&\sqrt{6/7}\\0&\sqrt{2(1-\alpha)/3}&0\end{pmatrix}.
\]

Their products sum to $I_3$ and diagonal states remain diagonal. Their stationary population vector is

\[
p_* =\frac{(12\alpha,9,7(1-\alpha))}{16+5\alpha},\qquad
\frac{p_1^*}{p_2^*}=\frac43\alpha.
\]

At $\alpha=7/9$, it is $(84,81,14)/179$, not $(28,27,6)/61$; the latter is not stationary for the declared channel. At $\alpha=1$, state 3 receives no input from state 2 but can still decay into it: this is absence of incoming branching, not full dynamical decoupling of state 3. No general full-state convergence theorem for this three-state family is asserted here.

Finally, a channel alone fixes no energy cost. An explicit Stinespring isometry $V|\psi\rangle=\sum_jK_j|\psi\rangle\otimes|j\rangle_E$ shows that its implementation requires a supplied environment input and that discarded correlations reside in the environment. It does not fix Hamiltonians, switching work, bath renewal, clock cost or temperature. Those are additional entries in §11's resource account; no entropy-area or gravitational normalization follows from these fixed populations.


## D.12 Event comparisons, composable histories and winding observability

### D.12.1 A declared receipt alphabet does not specify its transition graph

The additional working notes [24] motivate the following conditional alphabet. A label contains incoming and outgoing Hamming weights $w,w'\in\{0,1,2,3\}$ and parity $\epsilon\in\{0,1\}$. Fixed-weight labels have $w'=w$ and no address, giving $|F|=8$. One-step labels have $w'-w=+1$ or $-1$, three possible adjacent weight steps in each direction and address $a\in\{0,1,2\}$. Thus $|O|=|E|=3\cdot3\cdot2=18$. These are coarse labels, not a count of underlying microstates or independently generated events. Their parity/address interpretation remains conditional on a supplied receipt map.

There are $\binom{44}{2}=946$ unordered pairs of distinct labels. Pair comparison differs from history composition: the ordered history $\ell_1$ then $\ell_2$ requires at least $w'_1=w_2$. Applying that necessary weight condition yields:

| Comparison block | All distinct unordered pairs | At least one weight-compatible ordering |
|:--|--:|--:|
| $F,F$ | 28 | 4 |
| $O,O$ | 153 | 72 |
| $E,E$ | 153 | 72 |
| $F,O$ | 144 | 72 |
| $F,E$ | 144 | 72 |
| $O,E$ | 324 | 108 |
| Total | 946 | 400 |

For $F,F$, weights must agree; only the two opposite-parity labels at each of four weights can form such a distinct pair. For $O,O$, the first weight step must end where the second starts: two successive step positions, each with $6\cdot6$ address/parity choices, give 72. Extinctions give the same count. Each onset or extinction label can compose with the two fixed labels at either endpoint, giving 72 in each mixed fixed block. For $O,E$, the two weight steps must be reverses: three step positions with $6\cdot6$ choices give 108. There are 520 ordered weight-compatible pairs when repetition is included. This last number is also $8^2+14^2+14^2+8^2$, from the incoming/outgoing label counts at each weight.

These are combinatorial compatibility results. Full bit patterns, address histories, transport gates, null events and frame consistency may impose further constraints. Neither the 946 comparisons nor all 400 weight-compatible pairs constitute a derived native transition graph. A partition by label type also need not be an invariant sector of an unspecified evolution operator.

The $O,E$ block demonstrates a useful collision of equal counts. Its same-address subset has $3\cdot6^2=108$ pairs. Its reverse-weight-step subset also has $3\cdot6^2=108$ pairs, but the intersection contains only $3\cdot3\cdot2^2=36$. The address and weight-step predicates are independent restrictions in this declared product alphabet. Equality of their cardinalities does not identify the subsets, their admissibility or their dynamics.

### D.12.2 When a receipt determines a winding or cost

Let $\mathcal H$ be a declared set of fine histories, $q:\mathcal H\to\mathcal R$ a receipt, and $W:\mathcal H\to\mathbb Z$ a winding increment. There exists a receipt-level function $\bar W$ on $q(\mathcal H)$ with $W=\bar W\circ q$ if and only if $W$ is constant on each fiber of $q$. Necessity follows by evaluating $\bar W$ on equal receipts. For sufficiency, define $\bar W(r)$ using any history in that fiber; the assumption makes the definition independent of the representative. The same criterion applies to any proposed cost functional.

A fixed-weight receipt alone does not satisfy this criterion for an unspecified winding. For a counterexample to the inference, extend the state to $(w,\epsilon,n)$, $n\in\mathbb Z$, and consider two candidate lifts that fix $w,\epsilon$ but update $n$ to $n$ or $n+1$. Both project to the same fixed-weight receipt; their winding increments differ. This proves underdetermination from the label premises alone. It does not declare either lift admissible under a future complete UD source law.

Even when a winding increment $\nu$ is independently known, a quadratic burden $B(n)=\kappa n^2$ gives

\[
\Delta B=\kappa(2n\nu+\nu^2).
\]

The first and second positive unit steps cost $\kappa$ and $3\kappa$ because their initial windings are 0 and 1. A cardinality ratio $324/108=3$ does not supply either winding, $\nu$, $\kappa$, a probability law or an address-to-winding map. If $\nu=0$ is separately established, then $\Delta B=0$; a zero Hamming change alone does not establish that premise. A zero change of this burden stock also does not establish zero complete apparatus cost.

For example, the notes propose the cross-block cost $c(\ell_O,\ell_E)=1+2\mathbf1_{a_O\ne a_E}$. This is an assigned pair cost, not a consequence of the pair counts. Replacing 2 by any nonnegative constant preserves the alphabet and all its counts. If the expression is asserted to be a metric on the whole label set, its nonzero diagonal first requires correction; the given formula is defined here only on the disjoint $O,E$ block. Under an additional uniform distribution on those 324 pairs, the proposed mean is

\[
\frac{108\cdot1+216\cdot3}{324}=\frac73,
\]

which is a different object from the count ratio 3. Thus label counting, history eligibility, winding inference, signed burden change and complete resource cost require separate maps. The new exact replay enumerates the declared alphabet and checks these counts [24]; the fiber criterion and counterexample supply the general logical boundary.


# Appendix E. Data, code and development declarations

The preserved `UD_CONDITIONING_REVIEW_v0.8_PACKAGE.zip` contains the prior manuscript, the conditioning report, exact Gram/LDL/Sturm certificates, current replay and the preserved version-0.7 gluing package. Run `verify_conditioning.py` with SymPy, NumPy and SciPy; its required source certificates are in `baseline/`. It regenerates the conditioning certificates and `CONDITIONING_CHECKS.json`. Prior source and replay scopes remain unchanged. `ENVIRONMENT.json` records the constructor environment.

The preserved `UD_PARTNER_REVIEW_v0.9_PACKAGE.zip` adds the prior revised manuscript, the partner-work audit, the original partner DOCX and its paragraph/Office Math extracts, an explicit claim-disposition register, `verify_partner_findings.py`, `PARTNER_CHECKS.json` and the positive-metric certificate. Run the new replay with SymPy; it executes no imported partner code. The archive preserves the full version-0.8 conditioning package. The imported working notes are unreviewed claim data; only independently rederived material is integrated. Their unattested physical, modular-filter and holonomy interpretations are not promoted. Approximate recurrence and metric-class qualifications also have written proofs in D.10.

The current version-0.10 additional-research package contains this manuscript, its companion audit, the independently authored `verify_additional_research.py`, exact check output, source register, claim dispositions and the five new input documents. Original DOCX and governance/ledger bytes are preserved inside the source archive with their hashes. The version-0.9 manuscript is preserved as a baseline; its complete earlier evidence package remains pinned by the source register and prior capture commit. The new replay checks event counts/composability, selected auxiliary finite-group facts and counterexamples to imported transport claims. It does not repeat every earlier replay. Auxiliary group/transport calculations are retained in the companion audit rather than admitted as UD physical correspondences. All additions remain development, with no registry promotion or independent review.

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

17. Serre, Jean-Pierre. *Linear Representations of Finite Groups*. Graduate Texts in Mathematics 42, Springer, 1977. DOI: [10.1007/978-1-4684-9458-7](https://doi.org/10.1007/978-1-4684-9458-7).
18. Knill, Oliver. *The McKean-Singer Formula in Graph Theory*. 2013, §9.3 and complete-graph example. [arXiv:1301.1408](https://arxiv.org/abs/1301.1408).
19. Wee, Junjie, Ginestra Bianconi, and Kelin Xia. *Persistent Dirac for molecular representation*. Scientific Reports 13, 11183 (2023). DOI: [10.1038/s41598-023-37853-z](https://doi.org/10.1038/s41598-023-37853-z).

20. Åström, Karl Johan, and Richard M. Murray. *Feedback Systems: An Introduction for Scientists and Engineers*. Author draft v2.4a, 16 September 2006, §7.1, Theorem 7.1. [Inspected draft](https://people.duke.edu/~hpgavin/SystemID/References/Astrom-Feedback-2006.pdf). Background reference for the observability rank criterion; draft numbering is version-specific.
21. Gouasmi, Ayoub, Eric Parish, and Karthik Duraisamy. *A priori estimation of memory effects in coarse-grained nonlinear systems using the Mori-Zwanzig formalism*. [arXiv:1611.06277v2](https://arxiv.org/abs/1611.06277v2), 2017. DOI: [10.1098/rspa.2017.0385](https://doi.org/10.1098/rspa.2017.0385). Background reference for projected memory equations.

22. LAPACK authors. *LAPACK Users' Guide*, “Linear Least Squares Problems” and “How to Measure Errors.” Official documentation: [least squares](https://www.netlib.org/lapack/lug/node27.html), [error measures](https://www.netlib.org/lapack/lug/node75.html). Background for standard least-squares and norm-based conditioning; the specialized bounds here are proved explicitly.

23. Supplied partner-LLM working notes, *Calculating the Square Root of 4/3*, DOCX upload ingested 14 October 2026. Unreviewed source data; no public-paper or model-identity claim. Original SHA-256, paragraph anchors, dispositions and independent replay are documented in the companion partner-work audit and version-0.9 package. This reference identifies provenance, not authority for the corrected results.

24. Additional supplied partner working notes, `1, 2, and 3(5).docx`, `1, 2, and 3(7).docx` and `1, 2, and 3(8).docx`, ingested 14 October 2026. Exact hashes, paragraph anchors, source/dependency dispositions and independent checks are in the companion additional-research audit and version-0.10 package. Unreviewed source data; this reference records provenance rather than authority for their conclusions.
