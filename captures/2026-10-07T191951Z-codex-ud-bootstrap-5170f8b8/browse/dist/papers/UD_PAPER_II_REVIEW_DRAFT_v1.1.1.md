---
title: "Projective Reconstruction, Complex Phase Receipts and Frozen-Tree Validation"
subtitle: "Paper II - Consolidated review draft 1.1.1"
author: "Benjamin Walker Mayes"
date: "4 October 2026"
---

**Independent researcher**  
ORCID: [0009-0002-5813-0724](https://orcid.org/0009-0002-5813-0724)

**Edition status.** Integration draft for independent review. Source baseline: portal version 161, commit `62a7c594e0c7ab02f1c87702d0586a39352170d5`. Mathematical assertions retain the premises of their declared carriers and maps. Source-audited calculations are distinguished from new derivations. Physical promotion: zero. Independent human review: pending.

**Edition 1.1.1 release note (4 October 2026).** This review draft supersedes the reading edition 1.1 for the corrected passages; the original 1.1 source, PDFs and review receipts remain preserved. M3 published the consolidated portal at version 162 on 4 October 2026. Publication is distribution, not independent proof review or physical validation. M4-01 through M4-09 are recorded in the accompanying correction register. This edition supplies text repairs and scope clarifications; it makes no registry or physical promotion. Paper IV draft 0.1 supplies a dedicated treatment of prepared controllers, capture and renewal. Section numbering and PT identifiers in this paper remain stable.

## Abstract

We give sufficient recorded statistics for reconstruction of real and complex chain states up to positive real scale. The real parity-degree and component-sign obstructions, exact forest reconstruction, frozen filled-tetrahedron 14/14 prediction split and covariance pushforward are retained. A separate twelve-incidence sign code detects single errors without unique correction. A new general complex forest proof uses normalized stocks, full complex incidence receipts and one supplied root phase per nonzero component; real-part currents alone remain insufficient. Exact tree-count arithmetic is separated from an unavailable alternative-tree optimization certificate. Correlated residual covariance, joint feasible-state tests, detector references, backaction and finite reuse remain explicitly qualified. A linear invariant-kernel criterion explains why unsigned interface memory need not close visible dynamics. The result is mathematical identifiability after sufficient data are supplied, with acquisition, units, physical carrier identification and original-release provenance maintained as separate obligations.

# 1. Problem and related work

The problem is deterministic reconstruction from finite data. A state \(c\in\mathbb R^N\setminus\{0\}\) is indexed by oriented simplices. We wish to determine its positive ray
\[
[c]_+=\{\lambda c:\lambda>0\}.
\]
Unlike a real projective line, this convention distinguishes \(c\) from \(-c\). The distinction is why one absolute sign per connected support component is required.

Squared coefficients determine magnitudes but lose signs. Adjacent bilinear products constrain relative signs but can leave magnitude ambiguities. A recording of measurements is useful only if the reconstruction map and its assumptions are stated. We call the resulting finite data a *projective support receipt* (PSR). “Sufficient statistic” here means sufficient for this deterministic reconstruction problem. No Fisher-Neyman statistical sufficiency claim is made without an additional sampling model.

Graph-based recovery from relative observations has a substantial literature. Singer [1, arXiv version p. 1] explicitly describes noiseless phase recovery along a spanning tree, up to a root reference, and explains why noisy tree integration can accumulate error. Our sign propagation is the elementary two-element-group case, not a new general synchronization method. Its role here is to make the required sign data and zero-support cases explicit.

The simplex-incidence graph and its operators are standard in combinatorial Hodge and Dirac constructions [2, pp. 1-2; 3, arXiv pp. 4-6]. We use the filled tetrahedron's bipartite degree structure to expose a second ambiguity: opposite rescaling on even and odd degrees. That multiplicative ambiguity is distinct from the component sign ambiguity. Normalization by the total squared norm does not generally remove both.

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

## 4.1 The separate vertex-edge sign code

The \(C_0+C_1\) incidence graph of \(K_4\) has ten nodes and twelve incidences. It is not the fifteen-node, twenty-eight-incidence graph of the filled tetrahedron used in Section 5. With nonzero stocks and a supplied root sign, a nine-edge tree leaves three chord parity checks. In the declared coordinate order the check matrix is
\[
H_{\rm code}=\left(\begin{array}{rrrrrrrrr|rrr}
1&1&1&0&1&1&0&0&0&1&0&0\\
0&1&1&1&0&0&0&1&1&0&1&0\\
0&0&0&0&1&1&1&1&1&0&0&1
\end{array}\right)
\]
over \(\mathbb F_2\). It has rank three and defines a \([12,9,2]\) code with 512 words.

**Proposition II.S1 (detection without unique correction).** A single incidence-sign error is detected, but cannot always be uniquely located. Error positions \((1,10),(2,3),(4,11),(5,6),(7,12),(8,9)\) have equal syndromes.

*Proof.* Every column is nonzero, so every weight-one error has nonzero syndrome. The listed pairs have identical columns, giving weight-two kernel words and ambiguous single-error syndromes. No weight-one kernel word exists, so the minimum distance is two. Rank gives dimension nine. \(\square\)

Stocks, support mistakes and root-reference errors are outside this incidence-sign code. Its redundancy is an algebraic consistency check, not independent replication or apparatus calibration.


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

# 6. Complex coefficients and component phase references

This section supplies a fresh general derivation. It does not claim recovery of the named historical complex-audit release. Let \(c\in\mathbb C^n\setminus\{0\}\), \(S=\sum|c_\sigma|^2\), \(\rho_\sigma=|c_\sigma|^2/S\). On a nonzero adjacent-degree incidence define the complex receipt
\[
\mathcal J_{\sigma\tau}=2B_{\sigma\tau}\overline{c_\sigma}c_\tau,
\qquad
u_{\sigma\tau}=B_{\sigma\tau}\mathcal J_{\sigma\tau}/|\mathcal J_{\sigma\tau}|.
\]
Here \(B_{\sigma\tau}\in\{\pm1\}\). The raw stock remains \(q_\sigma=|c_\sigma|^2\); normalized stock is \(\rho_\sigma=q_\sigma/S\). Thus \(|\mathcal J_{\sigma\tau}|^2=4q_\sigma q_\tau\), while \(|\mathcal J_{\sigma\tau}/S|^2=4\rho_\sigma\rho_\tau\). Normalizing receipts by positive \(S\) leaves the phase ratio unchanged. Traverse a spanning forest of the graph induced by nonzero support and supply one unit root phase per component. Write \(z_\sigma=c_\sigma/|c_\sigma|\). Forward traversal assigns \(z_\tau=z_\sigma u_{\sigma\tau}\), and reverse traversal uses \(\overline u_{\sigma\tau}\).

**Theorem II.C1 (complex positive-ray reconstruction).** Valid normalized stocks, these phase ratios and the supplied root phases reconstruct exactly \(c/\sqrt S\), independently of forest choice. Without component references they determine only the independent component \(U(1)\) phase class.

*Proof.* Substitution gives \(u_{\sigma\tau}=\overline z_\sigma z_\tau\). Induction along each rooted tree therefore reproduces every phase. Multiplication by \(\sqrt{\rho_\sigma}\) gives the stated vector; zero coefficients are assigned zero without a phase division. Any forest carrying valid data gives the same reconstructed vector. Multiplying all coefficients in a component by an arbitrary unit phase preserves every stock and every within-component receipt. Hence those phases cannot be recovered without the references. An isolated nonzero node is a component and also needs a reference. \(\square\)

**Proposition II.C2 (cycle consistency).** For unit edge ratios on a connected nonzero support graph, phases exist exactly when the oriented product around every cycle is one.

*Proof.* Existence makes cycle products telescope. Conversely, propagate phases along a spanning tree. A non-tree edge agrees with the propagated phases exactly when its fundamental cycle product is one. Every cycle is generated by these fundamental cycles. \(\square\)

The references are acquisition resources. This result is a complete invariant under positive real rescaling after they are supplied; a complex global phase has not silently been quotiented out. Real signed PSR in T3.2 remains a separate specification.

## 6.1 Current convention and nonidentifiability

Under Paper I's real skew generator, continued complex-linearly, a lower coordinate has stock derivative \(-\operatorname{Re}\mathcal J\) from its incidence with an upper coordinate, and the upper derivative is \(+\operatorname{Re}\mathcal J\). This follows from differentiating \(|c|^2\). The imaginary part is not that stock current under this convention. Full complex receipts contain phase information that real-part currents alone do not: conjugating all coefficients preserves stocks and real-part receipts but generally changes the positive ray. An imaginary-current Hamiltonian convention requires its own definition and cannot be substituted without changing the map.

## 6.2 Tree arithmetic and unresolved historical provenance

For the filled-tetrahedron incidence graph, the exact tree count is
\[
\tau=2^8\,3\,17^3=3\,773\,184.
\]
The number 28 counts incidences. The supplementary verifier recomputes the tree count by an exact Laplacian cofactor. The reported alternative-tree path spectrum \(10\times3+4\times5\) has sum 50, squared sum 190 and mean \(25/7\). The equality \(384=16\times24\) is arithmetic, not proof of optimality, group freeness or sixteen orbit classes. The original exhaustive certificate for the reported tuple \((5,50,190)\) has not been recovered; these optimization assertions remain source-blocked. They do not replace the frozen tree in Section 5, whose path spectrum is \(8\times3+5\times5+1\times7\), mean 4.

The named historical release is:

`UD_THEORY_MATH_AUDIT_AND_CLOSURES_2026-09-20_v0.1_RELEASE.zip`.

Its reported SHA-256 is:

`bccb1b26e1623f8fc425307acdcfef8086b6d10e65b0b62345a95564b8215f79`.

Its original bytes, disputed passage and exhaustive enumeration were unavailable in the source and retrieval inventory. This is a provenance limitation, not evidence that the release never existed. II.C1--II.C2 and the new replay are separately identified repairs; no historical implementation or claimed review is inferred from them.

# 7. Exact covariance transport and what it does not imply

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

## 7.1 Correlated receipts and noise reconciliation

The frozen map \(H=CS\) stays fixed across covariance amendments. Correlated noise changes \(\Sigma_T\), not the algebraic map. The residual formula above must retain cross-covariances whenever train and held-out measurements share preparation, calibration or reference noise. A dual-split identity or noise floor correction must state its common-state and dependence assumptions. Per-chord variances, simultaneous coverage, joint feasible-state compatibility and successful physical acquisition are distinct claims. Selecting a better-looking tree after inspecting held-out data would change the prospective protocol.

# 8. Exact consistency, uncertainty and prospective tests

## 8.1 Feasible sets

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

## 8.2 A small operational decision rule

> **Internal falsifiers.** An exact receipt with \(J_e^2\ne4q_uq_v\) is inconsistent. Incompatible products of relative signs around a cycle are inconsistent. A claimed reconstruction differing from the normalized input state refutes T3.2's implementation. A nonzero \(H-CS\) refutes the supplied tree map. Once the training feasible set and held-out measurement model are fixed, an observed held-out vector incompatible with that set fails the declared protocol.

Acceptance of the finite model on a data set is conditional on the acquisition and uncertainty assumptions. Device authentication, same-state preparation and independent scoring are external procedures. They cannot be inferred from an algebraically valid receipt, and are kept out of the mathematical sufficiency claim.

A numerical noise sweep may check an implementation or illustrate a stipulated stochastic model. It is not needed for the exact map \(H=CS\) or the covariance theorem. The earlier 1,500-trial sweep is therefore omitted from this paper's evidence for the exact claims. Any future protocol report using it should label it as a numerical check under the specified noise distribution.

## 8.3 Encodings, detector effects and interface memory

Real/complex state-cone encodings, complete \(S_4\) quadratic carriers, harmonic references and six-quadrature composites describe declared interfaces. Positivity of a quadratic statistic does not derive a Born law; an operator encoding does not identify a physical carrier. The positive-channel and reference obstructions in the source addenda are retained beside their candidates. Paper III supplies the exact symmetry typing and one explicit compatible context basis, with its scalar coupling still open.

Source-selected paired complex effects require a prepared phase reference and a specified detector coupling. Posterior accuracy must be reported with success probability and all failure branches. Backaction, reference preparation, correlated reuse and reset are resource obligations. Reusing a reference does not create independent trials. Marginal fidelity is insufficient for a claim about the complete joint output; Paper III Section 13 gives an exact three-slot counterexample and the finite capture budgets.

**Theorem II.M1 (autonomous visible dynamics criterion).** For a linear generator \(A\) and observation \(P\), a linear autonomous visible law \(PA=FP\) exists exactly when \(\ker P\) is \(A\)-invariant.

*Proof.* The identity makes \(PAv=0\) whenever \(Pv=0\). Conversely define \(F(Pv)=PAv\) on the image of \(P\). Invariance makes this well-defined; extend it linearly to the chosen visible codomain if necessary. \(\square\)

The source's ambient 30-to-23 interface needs seven signed memory coordinates, with coupling rank seven. Unsigned memory does not close the visible law: its equal-stock witness has total stock \(7/2\), visible stock \(3\) and memory stock \(1/2\) under the orthogonal sum/difference interface coordinates, because \((3/2)^2+(1/2)^2+1=7/2=3+1/2\), while the sum-channel contribution is \(2^2/2+1=3\). The two prepared witnesses have visible derivatives differing by \(-1\) on edge 03 and \(+1\) on edge 04. This observation restriction is different from complete signed PSR, which reconstructs the entire supplied state. The four-face same-history lift likewise assumes complete shared-face observations and a supplied history; incomplete observations do not inherit its conclusion.

# 9. Acquisition, units and evidence limits

The mathematical input must be acquired with correct support, normalization, sign or phase references, common-state provenance and a frozen uncertainty model. Zero-crossing intervals require an indeterminate branch. Optical/QuiX proposals retain frozen training, held-out identities and correlated-noise controls. LC Stage 0 remains UNSCORED with threshold \(3/200\); calorimetry and engineering comparisons retain independently calibrated energy, flux, latency and readout units. Event counts and internal action normalization do not determine seconds or an empirical action scale.

The QTP, InTaSet, CMU, Google QEC, Lehigh/Cordoba and other collaboration/corpus records are dated, dataset-scoped or prospective. No unverified contact, synthetic fixture or external-domain result promotes the physical same-carrier bridge. A measured device response must first be shown to observe the declared coefficients. Acquisition calibration is neither a consequence of identifiability nor of covariance transport.

Complex reconstruction is now proved for the separately specified receipt. Original complex-release recovery and exhaustive alternative-tree optimization remain open. Native detector interaction, reference preparation, complete reusable reset and physical identification remain supplied or unresolved. Physical promotion is zero, and independent human review is pending.
# 10. Claims and reproduction

The shared supplement includes the canonical ordered incidence list, frozen training and held-out identities, all 196 entries of \(C\), \(S\), \(H\), an exact finite-distribution covariance example, and signed-state fixtures with full, sparse and disconnected support. Run `python replay/baseline/verify.py` with Python 3.10 or later; no third-party package is required.

The checks regenerate the artifacts rather than reading a stored PASS flag. Rational arithmetic verifies matrix identities and squared amplitudes. The general square-root reconstruction follows the written proof; fixtures check its signs and normalized squared coefficients without floating-point approximation. The same package contains Paper I's exact matrices. A package README maps each check family to its paper and states the measured runtime.


The complex/current/cofactor/code/interface replay is `python replay/repairs/verify_m2.py` and requires SymPy. Its bounded fixtures and deliberate-error controls accompany the written general proofs. The unprovided original complex archive and alternative-tree optimization certificate are not dependencies of II.C1. Legacy T6.1 and NG6.2 now occur in Section 7.

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
| II.S1 | [12,9,2] sign detection; ambiguous correction | Exact column/rank proof | Section 4.1 | Nonzero stock and root |
| II.C1 | Complex positive-ray reconstruction | General forest proof; exact fixtures | Section 6 | Component phase references |
| II.C2 | Unit-ratio cycle consistency | Fundamental-cycle proof | Section 6 | Nonzero support |
| II.M1 | Visible autonomous law iff invariant kernel | Linear quotient proof | Section 8.3 | Declared observation P |

# Appendix A. The declared training tree

Here \(v\), \(e\), \(f\), and \(t\) label a vertex, edge, face and tetrahedron, respectively. The fourteen tree incidences, in their frozen order, are

| Index | Training incidence | Index | Training incidence |
|--:|:--|--:|:--|
| 1 | v0-e01 | 8 | v1-e13 |
| 2 | v1-e01 | 9 | v2-e23 |
| 3 | v0-e02 | 10 | e01-f012 |
| 4 | v2-e02 | 11 | e01-f013 |
| 5 | v0-e03 | 12 | e02-f023 |
| 6 | v3-e03 | 13 | e12-f123 |
| 7 | v1-e12 | 14 | f012-t0123 |

The complementary chord list is e12-v2, e13-v3, e23-v3, e02-f012, e12-f012, e03-f013, e13-f013, e03-f023, e23-f023, e13-f123, e23-f123, f013-t0123, f023-t0123, f123-t0123. Reversing the written order of endpoints here does not change a signless row; the boundary orientation used for signed currents remains fixed by the simplex bases.

For example, the chord v2-e12 follows the path v2-e02-v0-e01-v1-e12. Its prediction is
\[
z_{v2,e12}=z_{v2,e02}-z_{v0,e02}+z_{v0,e01}-z_{v1,e01}+z_{v1,e12}.
\]
Every interior log amplitude cancels. This illustrates why a coordinate-gauge uncertainty can remain while this chord magnitude is fixed.


# Appendix B. Source integration and evidence authority

This edition consolidates the 26 thematic source families from the M1 inventory. The companion `INTEGRATION_DISPOSITIONS.json` and filterable register contain all 984 routed records (955 registered items and 29 additional addendum paths), with original paths, hashes, disposition and this edition's body/digest anchors. The addendum inventory contains 166 paths and 145 distinct hashes; repeated snapshots are cross-references, not additional evidence. Inventory coverage and editorial integration are not independent certification of every underlying proof. Detailed historical apparatus reports remain linked source evidence rather than new physical claims.

Legacy proposition IDs from Papers I and II edition 1.0 are retained even where a section moved. New IDs carry the paper prefix. Paper III uses the consecutive statement numbers 1-16 of its retained core, followed by the explicitly prefixed new statements. Section numbers and claim-table IDs therefore need not coincide.

A CRL label is a dated governance assertion. The supplied CRL2 subdivision proposal distinguishes proposal, preregistration/review, blinded execution and independent replication; it is not evidence that the last stages occurred. Citation depth does not deepen evidence, and a changed assumption demotes dependent conclusions until reviewed. Candidate amendments remain development-lane proposals. The coefficient ledger v0.39 supplied with older packages is an August baseline, not the ceiling for later amendments.

Original unavailable artifacts are named as provenance gaps. Reconstructed proofs and certificates have their own identity and never stand in for recovered historical bytes. Historical M2 note (3 October 2026): full portal publication and presentation reconciliation were a subsequent release task. The dated 1.1.1 release note records the later M3 publication; this historical note is retained for provenance.

Archive authority is determined by bytes and embedded edition together: the v2.33-named checkpoint embeds v2.32, and the v2.40-named checkpoint embeds older v2.36 text. Both names are retained as lineage, without silently treating their filenames as current scientific assertions. The journal core v0.3.2 supersedes the earlier v0.3.1 event-time account for the present digest.

## F08. Real PSR, sign code and observability {#F08}

**Body location:** 3-4.1. **Evidence class:** EXACT / NO-GO. **Source records:** 7.

Retain real positive-ray sufficiency; add sparse/disconnected support, one root reference per component and the C0+C1 [12,9,2] sign code. Distinguish the 12-incidence graph from the 15-node/28-incidence filled-tet graph.

**Remaining limit:** Measured stocks, support and references are supplied; apparatus validity is external.

- Source record `eventAdmission`: Shared-event discriminator and signed interface memory. Original path and SHA-256 are retained in the companion register.
- Source record `s29PSR`: PSR incidence-sign certificate. Original path and SHA-256 are retained in the companion register.
- Source record `s29PSRResults`: PSR incidence-sign certificate - exact results. Original path and SHA-256 are retained in the companion register.

## F09. Complex PSR and tree arithmetic {#F09}

**Body location:** 6. **Evidence class:** EXACT formula / OPEN provenance. **Source records:** 3.

Introduce a separately defined phase receipt J=2B conjugate(c_sigma)c_tau and root phase per nonzero component. Preserve frozen tree; record tau=2^8*3*17^3=3773184, with 28 reserved for incidence count.

**Remaining limit:** Complex forest theorem independently derived in II.C1-C2; original release bytes and alternative-tree optimum certificate remain unavailable.

- Source record `s30TreeAudit`: Tree-count factor: 2^8 versus 28. Original path and SHA-256 are retained in the companion register.
- Source record `s30TreeVerifier`: Hasse tree count - integer replay. Original path and SHA-256 are retained in the companion register.
- Source record `s30TreeResults`: Hasse tree count - exact matrix and results. Original path and SHA-256 are retained in the companion register.

## F10. Frozen held-out map, covariance and noise {#F10}

**Body location:** 5; 7. **Evidence class:** EXACT / CONDITIONAL / NO-GO. **Source records:** 22.

Consolidate H=CS and C Sigma C^T, per-chord formulas, correlated covariance, dual-split identity corrections and noise reconciliation. Retain path spectrum 8x3+5x5+1x7 for the original frozen tree.

**Remaining limit:** No substitution by a proposed optimized tree; covariance alone is not coverage or acquisition calibration.

- Source record `nonautonomousCovariance`: Source-History Covariance and Segmentation. Original path and SHA-256 are retained in the companion register.
- Source record `sigma7Segmentation`: Finite-Torus Covariance and Watershed Segmentation. Original path and SHA-256 are retained in the companion register.
- Source record `nrf1Refinement`: NRF-1 Quadratic Refinement: Ordering-Dependent Channel Flow. Original path and SHA-256 are retained in the companion register.

## F11. State cone, quadratic maps and quantum representations {#F11}

**Body location:** 8.3. **Evidence class:** CONDITIONAL / CANDIDATE / NO-GO. **Source records:** 38.

Summarize real/complex encoding, complete S4 quadratic carriers, positivity/channel obstructions, harmonic references and six-quadrature composites as declared interfaces. Preserve candidate-source labels and failed alternatives.

**Remaining limit:** No native Born law, phase donor or physical quantum carrier is derived merely from an encoding.

- Source record `AD093`: SOURCE ADDENDUM K4 RETURN COVARIANT SQUARE POSITIVE INTERFACE v0.1. Original path and SHA-256 are retained in the companion register.
- Source record `AD144`: SOURCE ADDENDUM K4 RETURN COVARIANT SQUARE POSITIVE INTERFACE v0.1. Original path and SHA-256 are retained in the companion register.
- Source record `AD145`: SOURCE ADDENDUM QUADRATIC ACTIVE MODE STATE INTERFACE v0.1. Original path and SHA-256 are retained in the companion register.

## F12. Readout, detector backaction and finite phase references {#F12}

**Body location:** 8.3; 9. **Evidence class:** CONDITIONAL / CANDIDATE / OPEN. **Source records:** 44.

Add source-selected complex paired effects, gauges, failure branches, detector disturbance, reference preparation, correlated reuse and reset-resource ledgers. Include success probability when quoting posterior accuracy.

**Remaining limit:** Physical detector coupling and native preparation remain supplied or open; marginal accuracy cannot replace complete-joint reuse bounds.

- Source record `AD052`: SOURCE ADDENDUM SIX QUADRATURE QUANTUM COMPLETION AND COMPOSITE v0.1. Original path and SHA-256 are retained in the companion register.
- Source record `AD062`: SOURCE ADDENDUM COMPLEX PAIRED DETECTOR AND FAILURE LAW v0.1. Original path and SHA-256 are retained in the companion register.
- Source record `AD109`: SOURCE ADDENDUM S4 QUADRATIC FULL CARRIER READOUT CONTRACT v0.1. Original path and SHA-256 are retained in the companion register.

## F22. Energy/control comparison and engineering contracts {#F22}

**Body location:** 9; III 13-14. **Evidence class:** CONDITIONAL / CANDIDATE / OPEN. **Source records:** 28.

Summarize reciprocal controller energy, matching activation, damping, sensing, latency, force/readout budgets and robust finite windows. Keep calibrated independent units and model comparisons explicit.

**Remaining limit:** These are stipulated mechanism/engineering contracts, not acquired hardware evidence or a native primitive.

- Source record `AD058`: UD BARE ROLE ADMISSIBILITY SOURCE ADDENDUM CANDIDATE v0.1. Original path and SHA-256 are retained in the companion register.
- Source record `AD059`: UD SOURCE ADDENDUM PARITY PARENT v0.1. Original path and SHA-256 are retained in the companion register.
- Source record `AD064`: UD SOURCE ADDENDUM CONTROLLER CELL CANDIDATE v0.1. Original path and SHA-256 are retained in the companion register.

## F24. Empirical protocols, corpus audits and collaboration records {#F24}

**Body location:** 9. **Evidence class:** PROTOCOL / DATASET-SCOPED / OPEN. **Source records:** 98.

Preserve optical/QuiX, LC Stage 0, calorimetry, QTP, InTaSet, CMU, Google QEC, Lehigh/Cordoba and lab records with dated acquisition/evidence labels. Carry only mathematically relevant identifiability, covariance and admissibility limits into the body.

**Remaining limit:** Stage 0 remains UNSCORED (threshold 3/200); no unverified contact, synthetic fixture or external-domain dataset promotes the physical same-carrier bridge.

- Source record `AD010`: UD JOP PSR OPTICAL HISTORICAL INSTANCE MINING ADDENDUM v0.1. Original path and SHA-256 are retained in the companion register.

# References

[1] A. Singer, “Angular synchronization by eigenvectors and semidefinite programming,” *Applied and Computational Harmonic Analysis* **30**, 20-36 (2011). [doi:10.1016/j.acha.2010.02.001](https://doi.org/10.1016/j.acha.2010.02.001). Exact tree recovery and root ambiguity: [arXiv:0905.3174v2](https://arxiv.org/pdf/0905.3174), p. 1.

[2] O. Knill, “The Dirac operator of a graph” (2013), [arXiv:1306.2166](https://arxiv.org/pdf/1306.2166), pp. 1-2.

[3] D. Horak and J. Jost, “Spectra of combinatorial Laplace operators on simplicial complexes,” *Advances in Mathematics* **244**, 303-336 (2013). [doi:10.1016/j.aim.2013.05.007](https://doi.org/10.1016/j.aim.2013.05.007); [arXiv:1105.2712](https://arxiv.org/pdf/1105.2712), pp. 4-6.

[4] B. W. Mayes, *Finite Tetrahedral Complexes and Skew Hodge-Dirac Support Flow*, consolidated review draft 1.1.1, 4 October 2026. Companion manuscript, supplied with this reproduction package; not represented as a peer-reviewed publication.
