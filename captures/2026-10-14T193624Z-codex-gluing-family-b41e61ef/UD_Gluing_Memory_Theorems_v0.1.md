# Boundary gluing, retained residuals and exact dynamic memory

14 October 2026. Development lane; no registry entry. Constructor-derived mathematics; physical promotion: 0.

## Declared model

Let $t$ finite oriented tetrahedra be separate copies of their full chain registers. Their direct sum $V$ has dimension $n=15t$. The union $K$ has one coordinate per distinct nonempty simplex and dimension $m$. Each local simplex orientation is aligned with the increasing global vertex order. The copied generator $A$ is block diagonal, with each cell using its own constant real skew incidence weights. It is not the native incidence generator of the union.

For a simplex $\sigma$, let $\nu_\sigma$ be its copy multiplicity. The normalized visible coordinate is the sum of its aligned copied coordinates divided by $\sqrt{\nu_\sigma}$. Denote the corresponding matrix by $Q$. It has $m$ independent orthonormal rows.

## Theorem G1: lossless normalized gluing

There is an orthogonal completion $U=(Q;R)$, with $n-m$ residual rows, such that

\[
\|x\|^2=\|Qx\|^2+\|Rx\|^2.
\]

Among linear lossless encodings retaining these m visible coordinates, at least n-m additional real coordinates are required. This is a state-dimension theorem, not a physical bit or energy cost.

**Proof.** Different visible rows have disjoint copied-simplex supports, and each row has squared norm $\nu_\sigma/\nu_\sigma=1$. Complete the rows by an orthonormal basis of $\ker Q$. Orthogonality proves the identity. An injective linear encoding of an n-dimensional state has rank n, so m+r output coordinates require $r\ge n-m$. If the copies all equal $c_\sigma$ on a simplex, $Qx=\sqrt{\nu_\sigma}c_\sigma$; recovering the native coordinate requires division by $\sqrt{\nu_\sigma}$. Native and copied norm conventions differ.

## Theorem G2: minimal autonomous linear memory

For any real skew $A$ on $\mathbb R^n$ and $Q$ with $m$ orthonormal rows, define

\[
\mathcal O=(Q;QA;\ldots;QA^{n-1}),\qquad d=\operatorname{rank}\mathcal O.
\]

To reproduce $Qe^{sA}x_0$ exactly for every $x_0$ and $s\ge0$ using a time-independent autonomous linear state model, initialized by a linear encoding of $x_0$ and retaining $Qx$ as its first $m$ coordinates, the minimum number of additional state coordinates is $d-m$.

**Proof.** The observable subspace $W=\operatorname{im}\mathcal O^T$ is $A$-invariant by Cayley-Hamilton and skewness. Its orthogonal complement is also invariant. The subspace $W$ contains $\operatorname{im}Q^T$. Choose an orthonormal basis for W starting with the rows of Q and extend them by d-m rows H in W intersect $\ker Q$. With $T=(Q;H)$, $F=TAT^T$ is skew and $TA=FT$, so the d-dimensional model reproduces the visible trajectory exactly. Conversely, any linear initial encoding C supporting exact future outputs has $\ker C\subseteq\ker\mathcal O$: a state encoded as zero must have every visible derivative zero. Hence $\operatorname{rank}C\ge d$ and at least d-m extra coordinates are required. This lower bound concerns exact finite autonomous linear realizations for arbitrary initial states; it is not a bound for one fixed preparation, a nonlinear encoding or an apparatus with external stored history.

The underlying observability construction is established control theory. The skew case permits an orthogonal reducing realization. The gluing-specific contribution is the concrete observation, its dimension and the structural rank argument below. No priority claim is made for the general observability principle.

## Theorem G3: fresh-vertex stacked tetrahedra require all residuals

Start with one tetrahedron and attach each later tetrahedron along one boundary face using a new vertex. In each copied cell let all three adjacent-degree weights $a_j,b_j,c_j$ be nonzero real constants; they need not agree between cells.

Then

\[
n=15t,\qquad m=8t+7,\qquad
\operatorname{rank}(Q;QA)=15t.
\]

Consequently $d=n$, and exactly $7(t-1)$ additional coordinates are required by Theorem G2. The visible/residual derivative coupling has rank $7(t-1)$. For $t=1$ this count is zero.

**Proof.** Attachment adds 1 vertex, 3 edges, 3 faces and 1 cell, so the unique register grows by 8 from its initial 15 coordinates. Consider the last attached tetrahedron, with fresh vertex v. Its eight simplex coordinates containing v occur in no earlier cell. If $Qx=0$ they vanish in this last copy. If $QAx=0$ their local derivatives also vanish, because the copied generator is block diagonal.

The remaining seven coordinates belong to the attachment face. The map from these face coordinates to derivatives of the eight private coordinates has Gram matrix

\[
C^TC=\operatorname{diag}(a_j^2,a_j^2,a_j^2,
b_j^2,b_j^2,b_j^2,c_j^2).
\]

Indeed each face vertex contributes through its new edge to v, each face edge through its new face containing v, and the attachment face through the new cell; orientation signs disappear in the Gram matrix. Nonzero weights make this map injective. Thus the last copied cell is zero. Remove it and repeat backwards: contributions of already-zero later copies vanish in both $Qx$ and $QAx$, and every remaining row normalization is nonzero. Finally the original copy is zero. Therefore $\ker Q\cap\ker(QA)=\{0\}$, proving the rank claim. On $\ker Q$, $QA$ is injective, so its rank is $n-m$, which is the visible/residual coupling rank under any orthogonal residual basis.

This proves a family result, not just a rank observation on the two-cell fixture. It also identifies the hypotheses: fresh-vertex attachment, separate copied generators, nonzero exchange weights, and unrestricted copied initial states. Cyclic gluing or a zero channel need not satisfy the conclusion.

## Exact projection equation and the meaning of memory

In orthogonal visible/residual coordinates, write $UAU^T$ as blocks $G_{vv},G_{vr},G_{rv},G_{rr}$. Eliminating the residual gives

\[
z'(s)=G_{vv}z(s)+G_{vr}e^{sG_{rr}}r_0
+\int_0^sG_{vr}e^{(s-u)G_{rr}}G_{rv}z(u)\,du.
\]

This follows directly from variation of constants in $r\prime=G_{rv}z+G_{rr}r$. The initial residual term cannot be discarded for arbitrary preparation. The kernel is a deterministic memory term; it is not automatically physical noise or dissipation. Skewness gives $G_{rv}=-G_{vr}^T$, so its instantaneous value is $-G_{vr}G_{vr}^T$, but its time dependence and initial term retain the underlying reversible dynamics. This is the linear projection/memory mechanism familiar from Mori-Zwanzig reduction, not a new irreversible entropy law.

## Verified examples and excluded controls

| Carrier | Copied n | Unique m | Lossless residual n-m | Observable d | Minimal dynamic memory d-m |
|:--|--:|--:|--:|--:|--:|
| Single tetrahedron | 15 | 15 | 0 | 15 | 0 |
| Two cells sharing a face | 30 | 23 | 7 | 30 | 7 |
| Five-cell core-star | 75 | 47 | 28 | 75 | 28 |
| Five-cell chain | 75 | 47 | 28 | 75 | 28 |
| Five-cell boundary of a 4-simplex | 75 | 30 | 45 | 55 | 25 |

The last row uses canonical unit-weight copied cells. Its 20 unobservable directions have an exactly certified invariant basis. Copy generators satisfy A³=-4A, so the three-block observability matrix suffices. The certificate gives rank 55 already for (Q;QA), with no later increase. This carrier's unique dimension 30 does not identify its 75-dimensional copied register with the separate 30-dimensional Pachner comparison.

Setting both cell-exchange weights c to zero in the two-cell example reduces the snapshot/derivative rank to 29; a shared-face difference is then invisible to that instantaneous snapshot/derivative readout. The next derivative restores full observability in this fixture, so its minimal dynamic memory is still seven. An all-zero copied generator instead needs no dynamic memory. This is an excluded hypothesis, not a counterexample to G3. An independent hidden oscillator supplies another control: it needs lossless residual storage but no dynamic memory for a decoupled visible oscillator. Therefore residual count and minimal predictive memory are distinct in general.

## Publication and physical boundary

The family theorem extends the previously reviewed two-cell interface, with an induction proof and exact fixtures under heterogeneous nonzero weights. The general observability and projection-memory machinery is standard and must be credited. A limited literature search did not establish an identical stacked-family statement; this absence is not a novelty proof.

Keeping residual coordinates closes inherited copied dynamics. It does not replace that generator by the native unique-simplex incidence law. That replacement requires a separate constitutive intervention or a justified admitted-state restriction. Neither the coordinate count nor mathematical derivative access establishes free acquisition, physical retained information, energy cost, entropy-area scaling or a gravitational equation.

Next publication work: independently challenge the induction and realization contract, assess the specialized theorem against related gluing/model-reduction work, and certify practical conditioning if derivative access is proposed. Small nonzero weights satisfy exact injectivity but may produce arbitrarily poor noise sensitivity; the theorem supplies no uniform reconstruction-error bound.

## Literature and source comparison

The rank criterion is standard observability theory: Åström and Murray, *Feedback Systems*, inspected author draft v2.4a (16 September 2006), §7.1, Theorem 7.1: https://people.duke.edu/~hpgavin/SystemID/References/Astrom-Feedback-2006.pdf. The autonomous linear minimal-memory proof here states its own exact initialization and output contract.

Projection memory is established background: Gouasmi, Parish and Duraisamy, *A priori estimation of memory effects in coarse-grained nonlinear systems using the Mori-Zwanzig formalism*, arXiv:1611.06277v2 (2017), §1.1 linear example: https://arxiv.org/abs/1611.06277v2. The equation here follows independently by variation of constants and includes arbitrary initial residuals.

Targeted searches for stacked-tetrahedron observability and simplicial gluing/Dirac observability did not identify an exact specialized match. This limited search does not certify originality. The general mathematics must be credited; the stacked-family induction and copied/unique coordinate accounting are the specific result to assess.
