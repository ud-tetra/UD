---
title: "Projective Reconstruction from Simplex Stocks and Incidence Currents"
subtitle: "Paper II · Review edition 1.0"
author: "Benjamin Walker Mayes"
date: "16 September 2026"
---

**Independent researcher**  
ORCID: [0009-0002-5813-0724](https://orcid.org/0009-0002-5813-0724)

## Abstract

Let a nonzero real vector be indexed by the simplices of a finite oriented complex. Squared coefficients and adjacent-degree bilinear incidence currents do not generally determine its positive ray: parity-degree rescaling preserves every current and can preserve total squared norm while changing the ray. We construct a sufficient finite reconstruction statistic consisting of normalized squared coefficients, relative signs on a spanning forest of nonzero support, and one reference sign per component. The statistic reconstructs the normalized signed vector, independently of forest choice. For the fully supported filled tetrahedron, the 28 incidence channels split into a frozen 14-edge spanning tree and 14 complementary checks. An integer alternating-path matrix maps training log-current magnitudes to held-out log-current magnitudes, yielding exact covariance pushforward without an independence assumption. The covariance describes predicted log magnitudes; it supplies neither a coverage probability nor the uncertainty of an independently measured residual without further assumptions. We state exact consistency tests, interval feasibility conditions, and the limits of the reconstruction claim. No experimental optical result is reported.

# 1. Problem and related work

The problem is deterministic reconstruction from finite data. A state \(c\in\mathbb R^N\setminus\{0\}\) is indexed by oriented simplices. We wish to determine its positive ray
\[
[c]_+=\{\lambda c:\lambda>0\}.
\]
Unlike a real projective line, this convention distinguishes \(c\) from \(-c\). The distinction is why one absolute sign per connected support component is required.

Squared coefficients determine magnitudes but lose signs. Adjacent bilinear products constrain relative signs but can leave magnitude ambiguities. A recording of measurements is useful only if the reconstruction map and its assumptions are stated. We call the resulting finite data a *projective support receipt* (PSR). “Sufficient statistic” here means sufficient for this deterministic reconstruction problem. No Fisher–Neyman statistical sufficiency claim is made without an additional sampling model.

Graph-based recovery from relative observations has a substantial literature. Singer [1, arXiv version p. 1] explicitly describes noiseless phase recovery along a spanning tree, up to a root reference, and explains why noisy tree integration can accumulate error. Our sign propagation is the elementary two-element-group case, not a new general synchronization method. Its role here is to make the required sign data and zero-support cases explicit.

The simplex-incidence graph and its operators are standard in combinatorial Hodge and Dirac constructions [2, pp. 1–2; 3, arXiv pp. 4–6]. We use the filled tetrahedron's bipartite degree structure to expose a second ambiguity: opposite rescaling on even and odd degrees. That multiplicative ambiguity is distinct from the component sign ambiguity. Normalization by the total squared norm does not generally remove both.

The contribution is the explicit reconstruction data structure on this carrier, a scoped identifiability counterexample, and a frozen-tree formulation that keeps full-state reconstruction separate from held-out magnitude prediction. Linear covariance pushforward is standard. Its useful specialization here is the exact integer matrix determined by the declared tree, together with a clear boundary between covariance and coverage. We make no priority claim for graph sign synchronization or covariance propagation in general.

The companion finite-carrier paper establishes the chain conventions and exact A/B/C operators. This paper is independently readable: only the incidence signs, support graph and Euclidean norm are needed for its principal reconstruction theorem.

> **What this paper does not claim.** Algebraic consistency does not authenticate the origin of data or identify a mathematical state with a physical field. The receipt is sufficient under stated assumptions; it is not claimed globally minimal among every possible measurement design. A spanning tree is not claimed statistically optimal. Fourteen held-out channels are not fourteen independent confirmations. No device session or experimental success is reported.

# 2. The parity-degree identifiability obstruction

## 2.1 Observables and domain

Let \(K\) be a finite oriented simplicial complex. For each simplex \(\sigma\), let \(c_\sigma\) be a real coefficient and define
\[
q_\sigma=c_\sigma^2,\qquad S=\sum_\sigma q_\sigma>0.
\]
For an adjacent-degree incidence \(\sigma\subset\tau\), the boundary entry is \(B_{\sigma\tau}\in\{-1,1\}\), and the recorded bilinear current is
\[
J_{\sigma\tau}=2B_{\sigma\tau}c_\sigma c_\tau.
\]
These are algebraic observations. The word “current” does not assert an electrical or optical interpretation.

Partition the coordinates into even and odd simplex degrees. Put
\[
A=\sum_{\dim\sigma\text{ even}}c_\sigma^2,\qquad
B=\sum_{\dim\sigma\text{ odd}}c_\sigma^2.
\]
For \(\lambda>0\), define
\[
(G_\lambda c)_\sigma=\begin{cases}
\lambda c_\sigma,&\dim\sigma\text{ even},\\
\lambda^{-1}c_\sigma,&\dim\sigma\text{ odd}.
\end{cases}
\]
Every adjacent incidence crosses the parity partition.

**No-go NG2.1 (currents and total norm are not generally sufficient).** All incidence currents are invariant under \(G_\lambda\). If \(A,B>0\) and \(A\ne B\), there is a nonidentity \(G_\lambda\) that also preserves \(S\) and changes \([c]_+\).

*Proof.* Each adjacent product gains the factor \(\lambda\lambda^{-1}=1\). The transformed norm is \(A\lambda^2+B\lambda^{-2}\). Setting \(y=\lambda^2\), equality with \(A+B\) gives
\[
Ay^2-(A+B)y+B=(y-1)(Ay-B)=0.
\]
Besides \(y=1\), there is \(y=B/A\ne1\). Since both parity sectors are nonzero, positive-ray equality would require \(\lambda=\lambda^{-1}\), hence \(\lambda=1\), a contradiction. \(\square\)

A rational witness is supported on vertex \(0\) and edge \(01\). Set \((c_0,c_{01})=(2,1)\), all other coefficients zero. The vector \((1,2)\) has the same total norm 5 and the same products, but a different positive ray. With the canonical boundary sign, the nonzero current is \(-4\) in both cases.

Even where \(A=B\), stocks and currents cannot distinguish simultaneous sign reversal on a connected support component. The theorem establishes noninjectivity of the observation map; it does not say every state has the same ambiguity. Additional metadata cannot repair it unless that metadata is specified to constrain the ambiguous state coordinates. Labels describing an event or route, by themselves, are not such a constraint.

## 2.2 A second ambiguity: component signs

Form a graph whose vertices are simplex coordinates with \(q_\sigma>0\), and whose edges are their adjacent-degree incidences. Multiplying all coefficients in one connected component by minus one leaves all stocks and currents unchanged. Edges to zero coordinates still have zero current.

There is therefore one undetermined common sign per connected support component. Fixing one global sign suffices only when that graph is connected. A zero coordinate can split the graph and increase the number of required reference signs. An isolated nonzero coordinate is a component and needs its own reference.

# 3. A sufficient recorded statistic

## 3.1 Definition

Choose a deterministic spanning forest \(F\) of the nonzero support graph, with one declared root in each component. Record
\[
\rho_\sigma=\frac{q_\sigma}{S},\quad
\chi_{\sigma\tau}=\operatorname{sgn}(c_\sigma c_\tau)\quad((\sigma,\tau)\in F),
\]
and the root sign \(\epsilon_C\in\{-1,1\}\) for each component \(C\). The normalized stocks include explicit zeros. Their sum is one.

**Definition D3.1 (PSR).** The recorded statistic is
\[
\operatorname{PSR}(c)=\bigl((\rho_\sigma)_\sigma,(\chi_e)_{e\in F},(\epsilon_C)_C\bigr),
\]
together with the declared simplex ordering, support graph, forest and roots. When these conventions are fixed globally, they need not be repeated as independent state data.

For measured stocks and forest currents, the relative sign is
\[
\chi_{\sigma\tau}=\operatorname{sgn}(B_{\sigma\tau}J_{\sigma\tau}).
\]
This requires nonzero forest endpoints. A reported zero or sign-uncertain current cannot be assigned a relative sign by an arbitrary convention.

## 3.2 Reconstruction and proof

Start at each root with \(s_r=\epsilon_C\). Traverse its tree and set
\[
s_v=s_u\chi_{uv}
\]
when first reaching a child \(v\) from its parent \(u\). Set
\[
\widehat c_\sigma=\begin{cases}s_\sigma\sqrt{\rho_\sigma},&\rho_\sigma>0,\\0,&\rho_\sigma=0.\end{cases}
\]

**Theorem T3.2 (positive-ray reconstruction).** For every nonzero real chain state,
\[
\mathcal R(\operatorname{PSR}(c))=\frac{c}{\sqrt S}.
\]

*Proof.* At a component root, the propagated sign agrees with the coefficient sign by definition. Suppose it agrees at \(u\). Since \(\chi_{uv}=\operatorname{sgn}(c_uc_v)\), multiplication gives \(s_v=\operatorname{sgn}(c_v)\). Induction along the unique root-to-vertex path covers each tree. Multiplying by \(\sqrt{c_\sigma^2/S}\) yields \(c_\sigma/\sqrt S\). Zero coordinates are reconstructed as zero. \(\square\)

This proof has two separate inputs: normalized stocks fix the magnitudes; the forest and roots fix signs. It does not reconstruct the unknown absolute scale \(S\). If \(S\) is also supplied, multiplying by \(\sqrt S\) recovers \(c\).

**Proposition P3.3 (exact current consistency).** Every exact receipt satisfies
\[
J_{\sigma\tau}^2=4q_\sigma q_\tau.
\]
On a connected nonzero graph, compatible relative signs have product one around every cycle. Conversely, positive stocks, compatible edge signs and root signs define a state realizing the corresponding signed products.

*Proof.* The squared-current identity follows from \(B_{\sigma\tau}^2=1\). A cycle product of coefficient-pair signs contains every coefficient sign twice, giving one. For the converse, propagate from a root along a tree. Cycle compatibility makes the result consistent with every non-tree edge. Multiply the assigned signs by the square roots of the stocks. \(\square\)

An exact packet violating the squared-current identity is rejected. Approximate measurements require the interval or probabilistic specification of Section 7; they cannot be repaired by silently relaxing this exact equation after viewing the target.

## 3.3 A reference-sign measurement model

One possible ideal reference uses a separately calibrated real probe \(\alpha\ne0\) at a root coordinate:
\[
q_r^+=(c_r+\alpha)^2,\qquad q_r^-=(c_r-\alpha)^2.
\]
Then
\[
q_r^+-q_r^-=4\alpha c_r.
\]
The sign of the difference relative to the known sign of \(\alpha\) identifies the root sign. These equations describe a measurement model, not evidence that a device has implemented it. They require the same underlying state for the two probe conditions, or a validated equivalent preparation, and separate treatment of probe uncertainty.

# 4. Forest choice and event maps

**Proposition T4.1 (forest independence).** Any spanning forest and root choices with data derived from the same state reconstruct the same normalized signed vector.

*Proof.* Theorem T3.2 holds for each forest separately, with the same right-hand side. Equivalently, cycle-consistent pair signs make each path product agree with the endpoint coefficient signs. \(\square\)

Forest choice is therefore a serialization convention for exact data. It is sometimes called a gauge in the broader project, but it is not a physical gauge field. With noisy data, different trees can have different conditioning and uncertainty. Exact equivalence is not a claim of equal statistical performance.

Let \(T\) be the canonical zero-extension from the A complex to B, and \(P\) the signed B-to-C isomorphism defined in Paper I. Both preserve the Euclidean norm on their source domains.

**Proposition P4.2 (event-level reconstruction covariance).**
\[
\mathcal R_B(\operatorname{PSR}(Tc))=T\mathcal R_A(\operatorname{PSR}(c)),
\]
\[
\mathcal R_C(\operatorname{PSR}(Pc))=P\mathcal R_B(\operatorname{PSR}(c)).
\]

*Proof.* Apply T3.2 to the transformed vector and use \(\|Tc\|=\|c\|\), or \(\|Pc\|=\|c\|\), respectively. \(\square\)

The statistic on the transformed state may use a newly computed forest. Its edge list need not be the image of the previous list. These are event-level reconstruction identities. They do not assert that the dimension-changing A-to-B inclusion intertwines the continuous flows; Paper I gives an explicit nonzero residual for that claim.

# 5. The filled tetrahedron and the frozen 14/14 split

## 5.1 The incidence graph

The filled tetrahedron has 15 nonempty simplices: four vertices, six edges, four faces and one cell. Its graph of adjacent-degree containments has
\[
12+12+4=28
\]
incidences. It is connected and bipartite by simplex-degree parity. On full nonzero support, a spanning tree uses 14 incidences, leaving 14 chords. Thus
\[
28=14_{\rm tree}+14_{\rm held\ out}.
\]
This is a channel partition. It does not mean a PSR consists only of fourteen current readings: normalized stocks and root references remain necessary for its full reconstruction theorem.

The supplement supplies the ordered 28-channel list and one specific frozen tree. Channel identities, not a path-length histogram, define the split. A tree must be chosen before examining held-out measurements if they are to remain held out.

## 5.2 Signless incidence and the parity gauge

For nonzero currents, define
\[
x_\sigma=\log|c_\sigma|,\qquad z_e=\log(|J_e|/2).
\]
Then \(z_{uv}=x_u+x_v\). Equivalently, using log stocks would insert a factor of one half; the convention here is log amplitude.

Let \(S\in\mathbb Z^{14\times15}\) have a one in each of the two endpoint columns of a training incidence, and zeros elsewhere. Let \(H\) be the analogous matrix for held-out chords.

**Theorem T5.1 (tree rank and its unresolved direction).** The connected tree matrix \(S\) has rank 14. Its nullspace is spanned by the parity vector \(p_\sigma=(-1)^{\dim\sigma}\). Every held-out row annihilates \(p\).

*Proof.* The equation \(Sx=0\) forces \(x_v=-x_u\) along each tree edge. Connectivity determines every coordinate from one root value, with sign alternating by parity. Thus the kernel is one-dimensional. Every adjacent-degree chord also has opposite-parity endpoints, so its row has zero dot product with \(p\). \(\square\)

The gauge is \(x\mapsto x+tp\), not uniform translation. Exponentiating gives opposite multiplicative scales on the two parity classes. A known root log amplitude fixes it. A total norm can admit the two values exhibited in NG2.1 and is not a generally unique substitute.

## 5.3 Alternating-path synthesis

**Theorem T5.2 (held-out magnitudes from tree data).** There is a unique matrix \(C\in\mathbb Z^{14\times14}\) satisfying
\[
H=CS,\qquad z_H=Cz_T.
\]
For a chord's unique tree path, its row has alternating entries \(+1,-1,+1,\ldots,+1\) on the path edges, and zero elsewhere.

*Proof.* The endpoints of a chord have opposite parity, so their tree path has odd length. In the alternating sum of endpoint-sum rows along this path, each interior vertex cancels and the two endpoints have coefficient one. This is the chord row. Uniqueness follows from independence of the 14 training rows. \(\square\)

For the declared split, eight paths have length 3, five have length 5 and one has length 7. The mean is exactly 4. The held-out row matrix has rank 10, checked over the rationals in the supplement. Accordingly, four of the fourteen log relations are linearly redundant. They are still useful consistency checks, but not independent evidence.

The sign of a held-out coefficient product is also determined by multiplying the recorded pair signs along its path. The incidence orientation sign then determines the signed current. Root signs cancel from pair products. Full signed-vector reconstruction and signed-current prediction therefore have different reference requirements.

# 6. Exact covariance transport and what it does not imply

Let a random training log-current estimate have a finite covariance matrix \(\Sigma_T\). Define its predicted held-out log vector by the fixed linear map \(\widehat z_H=C\widehat z_T\).

**Proposition T6.1 (covariance pushforward).**
\[
\Sigma_H^{\rm pred}=C\Sigma_TC^T.
\]
For rows \(c_h,c_k\) of \(C\),
\[
\operatorname{Var}(\widehat z_h)=c_h\Sigma_Tc_h^T,\qquad
\operatorname{Cov}(\widehat z_h,\widehat z_k)=c_h\Sigma_Tc_k^T.
\]

*Proof.* Center the training vector about its expectation, multiply by \(C\), and take the expectation of the resulting outer product. Linearity and finite second moments give the formula. \(\square\)

No independence or Gaussian assumption is required. If, additionally, \(\Sigma_T=\sigma^2I\), each predicted variance equals its path length times \(\sigma^2\). This specialization is exact for that log-space covariance model. It is not an assumption about untransformed detector readings.

If the input consists of signed nonzero currents with covariance \(\Sigma_J\), differentiating \(z_e=\log(|J_e|/2)\) gives \(D=\operatorname{diag}(1/J_e)\) and the first-order approximation
\[
\Sigma_T\approx D\Sigma_JD^T.
\]
The first-order map must not be relabeled exact. When possible, covariance estimated directly from declared transformed replicates avoids this extra approximation, although its own estimation uncertainty still remains.

**No-go NG6.2 (covariance is not a coverage certificate).** Covariance alone does not imply that a chosen interval \(\widehat z_h\pm k u_h\) has a specified coverage probability for an unknown data-generating law.

*Proof.* Different distributions can have the same variance and different tail probabilities. For instance, a mean-zero variable taking \(\pm1\) equally often and one taking 0 with probability \(3/4\), \(\pm2\) with probability \(1/8\) each, both have variance one but different probabilities outside \([-3/2,3/2]\). \(\square\)

Distribution-free inequalities can provide conservative bounds under their own assumptions, but do not turn an arbitrary multiplier into an exact 95-percent interval. A coordinate condition number also supplies no such probability. It measures sensitivity of a specified inversion in specified norms. Neither \(\kappa(S)\) nor \(\kappa(C)\) is a substitute for a simultaneous coverage rule.

Prediction covariance also differs from measurement-residual covariance. If \(r=\widetilde z_H-C\widehat z_T\), then
\[
\operatorname{Cov}(r)=\Sigma_{HH}+C\Sigma_{TT}C^T
-\Sigma_{HT}C^T-C\Sigma_{TH}.
\]
The cross terms vanish only under an appropriate uncorrelatedness assumption. Comparing predicted intervals to independently noisy held-out readings must account for that additional measurement uncertainty.

# 7. Exact consistency, uncertainty and prospective tests

## 7.1 Feasible sets

For an exact receipt, the reconstruction theorem and squared-current constraints can be checked directly. For measurements with certified strictly positive magnitude intervals, write \(x_\sigma=\log|c_\sigma|\). Stock intervals give
\[
\tfrac12\log q_\sigma^{\min}\le x_\sigma\le\tfrac12\log q_\sigma^{\max},
\]
and current-magnitude intervals give
\[
\log(|J_e|^{\min}/2)\le x_u+x_v\le\log(|J_e|^{\max}/2).
\]
Together these define a linear feasible set in log amplitudes, subject to separately compatible signs. If sign or support cannot be qualified because an interval crosses zero, this log construction is unavailable and the declared procedure returns an indeterminate result; it must not invent a sign or an epsilon cutoff after inspection.

For a frozen feasible set \(\mathcal F\), the predicted range of a held-out signed current is
\[
I_h^{\rm pred}=\{2B_hc_uc_v:c\in\mathcal F\}.
\]
Optimizing the linear log-magnitude functional over the feasible set gives its endpoints before exponentiation, with the sign convention then applied. Marginal ranges alone need not guarantee a single jointly compatible state. A protocol claiming joint compatibility must use the joint feasible-set test.

## 7.2 A small operational decision rule

> **Internal falsifiers.** An exact receipt with \(J_e^2\ne4q_uq_v\) is inconsistent. Incompatible products of relative signs around a cycle are inconsistent. A claimed reconstruction differing from the normalized input state refutes T3.2's implementation. A nonzero \(H-CS\) refutes the supplied tree map. Once the training feasible set and held-out measurement model are fixed, an observed held-out vector incompatible with that set fails the declared protocol.

Acceptance of the finite model on a data set is conditional on the acquisition and uncertainty assumptions. Device authentication, same-state preparation and independent scoring are external procedures. They cannot be inferred from an algebraically valid receipt, and are kept out of the mathematical sufficiency claim.

A numerical noise sweep may check an implementation or illustrate a stipulated stochastic model. It is not needed for the exact map \(H=CS\) or the covariance theorem. The earlier 1,500-trial sweep is therefore omitted from this paper's evidence for the exact claims. Any future protocol report using it should label it as a numerical check under the specified noise distribution.

# 8. Limits and claim table

The reconstruction theorem assumes real coefficients, a correct support graph, normalized stocks and valid reference signs. Complex coefficients require phase data and a different specification. Sparse support changes both the forest and the number of references. Exact tree prediction can be sensitive to noise; the chosen tree is not claimed optimal. No redundancy count is a count of independent replications. No uncertainty model or acquisition calibration has been derived from the finite algebra.

The main result is best understood as an explicit complete invariant for positive rays under a chosen observation scheme. It solves an identifiability problem after sufficient data have been supplied. It does not provide an endogenous source of those data or establish that a physical apparatus measures the intended coefficients.

| ID | Statement | Status | Proof / artifact | Depends on |
|:--|:--|:--|:--|:--|
| NG2.1 | Currents and total norm can leave two rays | No-go | Quadratic equation; rational witness | Both parity sectors nonzero |
| T3.2 | PSR reconstructs \(c/\sqrt S\) | Theorem | Forest induction; fixtures | D3.1 |
| P3.3 | Current square and cycle consistency | Proposition | Products and sign cancellation | Incidence signs |
| T4.1 | Exact forest choice is immaterial | Proposition | T3.2 in two forests | Valid root data |
| P4.2 | Reconstruction commutes with isometries | Proposition | Norm identity | Event isometry |
| T5.1 | Tree rank 14; parity kernel | Theorem | Tree propagation; exact rank | Full support |
| T5.2 | \(H=CS\), integer path map | Theorem | Alternating path cancellation | Frozen tree |
| T6.1 | \(\Sigma_H=C\Sigma_TC^T\) | Standard proposition | Centered outer products | Finite covariance |
| NG6.2 | Covariance alone is not coverage | No-go | Equal-variance distributions | No fixed distribution law |

# 9. Reproduction

The shared supplement includes the canonical ordered incidence list, frozen training and held-out identities, all 196 entries of \(C\), \(S\), \(H\), an exact finite-distribution covariance example, and signed-state fixtures with full, sparse and disconnected support. Run `python verify.py` with Python 3.10 or later; no third-party package is required.

The checks regenerate the artifacts rather than reading a stored PASS flag. Rational arithmetic verifies matrix identities and squared amplitudes. The general square-root reconstruction follows the written proof; fixtures check its signs and normalized squared coefficients without floating-point approximation. The same package contains Paper I's exact matrices. A package README maps each check family to its paper and states the measured runtime.

# Appendix A. The declared training tree

Here \(v\), \(e\), \(f\), and \(t\) label a vertex, edge, face and tetrahedron, respectively. The fourteen tree incidences, in their frozen order, are

| Index | Training incidence | Index | Training incidence |
|--:|:--|--:|:--|
| 1 | v0–e01 | 8 | v1–e13 |
| 2 | v1–e01 | 9 | v2–e23 |
| 3 | v0–e02 | 10 | e01–f012 |
| 4 | v2–e02 | 11 | e01–f013 |
| 5 | v0–e03 | 12 | e02–f023 |
| 6 | v3–e03 | 13 | e12–f123 |
| 7 | v1–e12 | 14 | f012–t0123 |

The complementary chord list is e12–v2, e13–v3, e23–v3, e02–f012, e12–f012, e03–f013, e13–f013, e03–f023, e23–f023, e13–f123, e23–f123, f013–t0123, f023–t0123, f123–t0123. Reversing the written order of endpoints here does not change a signless row; the boundary orientation used for signed currents remains fixed by the simplex bases.

For example, the chord v2–e12 follows the path v2–e02–v0–e01–v1–e12. Its prediction is
\[
z_{v2,e12}=z_{v2,e02}-z_{v0,e02}+z_{v0,e01}-z_{v1,e01}+z_{v1,e12}.
\]
Every interior log amplitude cancels. This illustrates why a coordinate-gauge uncertainty can remain while this chord magnitude is fixed.

# References

[1] A. Singer, “Angular synchronization by eigenvectors and semidefinite programming,” *Applied and Computational Harmonic Analysis* **30**, 20–36 (2011). [doi:10.1016/j.acha.2010.02.001](https://doi.org/10.1016/j.acha.2010.02.001). Exact tree recovery and root ambiguity: [arXiv:0905.3174v2](https://arxiv.org/pdf/0905.3174), p. 1.

[2] O. Knill, “The Dirac operator of a graph” (2013), [arXiv:1306.2166](https://arxiv.org/pdf/1306.2166), pp. 1–2.

[3] D. Horak and J. Jost, “Spectra of combinatorial Laplace operators on simplicial complexes,” *Advances in Mathematics* **244**, 303–336 (2013). [doi:10.1016/j.aim.2013.05.007](https://doi.org/10.1016/j.aim.2013.05.007); [arXiv:1105.2712](https://arxiv.org/pdf/1105.2712), pp. 4–6.

[4] B. W. Mayes, *Finite Tetrahedral Complexes and Skew Hodge–Dirac Support Flow*, review edition 1.0, 16 September 2026. Companion manuscript, supplied with this reproduction package; not represented as a peer-reviewed publication.
