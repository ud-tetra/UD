# Additional research audit and manuscript integration

14 October 2026. Development - no registry entry. Constructor verification only. Physical promotion: 0.

The three new working-note documents contain valid finite counting and representation-theory results alongside unsupported transport and winding-cost claims. Their most useful contribution to the manuscript is a sharper distinction between comparing event labels and composing actual histories. Independent enumeration reduces 946 possible unordered label comparisons to 400 pairs with at least one weight-compatible ordering. The source also contains two distinct 108-pair subsets that overlap in only 36 pairs. This gives a concrete example of why equal numbers do not identify equal objects.

The auxiliary Wilson-Dirac slab is a mathematically inspectable model, but no derivation from the tetrahedral UD generators is supplied. Its proposed universal reflectionless transport is false even for the continuum surface Hamiltonian: an explicit scalar-potential step has reflection probability 1/25. Finite-group calculations survive with qualifications, but do not supply a native framing group, physical metric or action scale. Only the repaired event-history and cost-inference results are integrated into the manuscript body and Appendix D.12. The group and transport analyses remain in this companion audit so the narrative does not acquire unrelated candidate physics.

## Inputs and provenance

| Source | Original name | Bytes | SHA-256 |
|:--|:--|--:|:--|
| S5 | `1, 2, and 3(5).docx` | 28,359 | `371648db493e44e36c30dd55880ed0be9dd5229c9e3e10f41f00c6a816165e09` |
| S7 | `1, 2, and 3(7).docx` | 3,024,616 | `e9f9990b00e82d2132bc0e7932137d25aa34fbbf7760b73409439043c366568a` |
| S8 | `1, 2, and 3(8).docx` | 3,025,213 | `cc0826472de371ac70b5e1fc09c345d6f471c2dd39a7ee538a4d12dff98ff29e` |

Each source is preserved byte-for-byte, with paragraph extracts and Office Math XML. Anchors S5:P111, for example, mean zero-based paragraph 111 of source S5, including empty body/table paragraphs in the index. The sources have 240, 151 and 171 paragraphs and 146, 136 and 113 Office Math objects, respectively. Plain extracts can flatten mathematical notation; the original DOCX and equation XML retain the source representation. Claimed code outputs are source data, not verified executions. No imported code was executed. The supplied files are not independently reviewed papers.

The comparison also uses the supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, dated 22 August 2026, and `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`. These inputs are preserved unchanged. The August ledger does not supersede later manuscript source reconciliations merely because it is attached again. It explicitly keeps physical promotion at 0, the master action normalization G05 source-open, action calibration G06 source-unrecovered and the legacy 13-pi-squared electromagnetic expression B03 at consistency-check/rebase status. Its 4/3 coframe identity F03 likewise does not authorize a dynamical interpretation without a bridge.

The supplied governance is marked a proposal and separates development from registry promotion. This audit uses its provenance, anti-erosion and non-constructor-review distinctions without claiming a custodian ruling or a confidence promotion. Missing source IDs Q393 and Q420 cited for WBQ1 in S8 are not entries in the supplied v0.39 ledger. That is a source-recovery gap, not proof that the IDs never occur in other project versions.

The current manuscript baseline is review candidate 0.9. Its Library identity and version were read before editing; earlier evidence remains available in its preserved release and GitHub capture commit `9cc94626e0e525a4460e04304a1c705c56137ba5` (PR 90). The unavailable `Gap2_FINAL_Finite_Genesis.png` was not read or used. Other historical attachments are not treated as fresh validation of these claims.

## Findings and dispositions

### Event labels and admissible history

**S5:P113-176: counts verified, dynamical language narrowed.** For the explicitly declared coarse alphabet there are eight fixed-weight labels F, eighteen onset labels O and eighteen extinction labels E. The six unordered comparison blocks FF, OO, EE, FO, FE, OE have cardinalities (28,153,153,144,144,324), summing to 946. The one-pair comparison subsets with the same address and different addresses have counts 198 and 432. These are exact counts conditional on the alphabet. They do not establish six invariant sectors of an unspecified event algebra or show that every pair is a transition.

For a history consisting of label 1 followed by label 2, a necessary condition is that the first outgoing weight equals the second incoming weight. Applying this condition to at least one ordering reduces the six blocks to (4,72,72,72,72,108), totaling 400. Only four of the 28 FF pairs are even weight-compatible; the other 24 involve fixed labels at different weights. Full bit, frame, gate and address conditions can impose additional restrictions, so 400 is not a claim that 400 native UD transitions have been admitted. The number of ordered, weight-compatible pairs, including repetition, is 520.

**S8:P72-114: count ratio verified; metric and WBQ1 identification rejected.** Same-address OE pairs number 108 and cross-address pairs 216. Independently, reverse-weight-step OE pairs number 108. These predicates are different: their intersection has 36 pairs. The address count therefore cannot be silently substituted for the history-composition count.

The assigned cross-block cost `1 + 2 * indicator[different addresses]` has values 1 and 3 because its coefficient 2 was chosen. Replacing 2 by another nonnegative number preserves every count. The formula, if extended unchanged to a whole-set metric, would also fail the zero-diagonal axiom; as a cost on two disjoint label classes it is well defined. With a separately supplied uniform probability on OE pairs its mean is 7/3, distinct from the count ratio 3. Neither object derives a winding increment or physical energy.

**S7:P67-99: proposed zero-winding inference is incomplete.** Each F label describes an event with zero Hamming-weight change. An arbitrary pair of such labels is not thereby a composable history. More fundamentally, an unobserved winding can change while this receipt is fixed. On an auxiliary lifted state `(w, parity, n)`, the two candidate updates `n -> n` and `n -> n+1` have the same projected fixed-weight receipt. Their winding increments differ. Thus the receipt definitions alone do not determine winding. This is a nonidentifiability witness, not a claim that either lift has been derived as native UD dynamics.

The general repair is exact: a fine-history functional descends to a receipt if and only if it is constant on every receipt fiber. For the stipulated quadratic burden B(n)=kappa*n^2, an independently supplied winding increment nu gives `Delta B = kappa*(2*n*nu + nu^2)`. Zero nu implies zero burden change. Zero Hamming change alone does not supply nu. The step ratio 3 follows from choosing initial winding 1 for the second unit increment, compared with initial winding 0 for the first. It is independent of the address-pair cardinality ratio. A signed burden-stock change is also distinct from complete write, readout, control and renewal cost.

These corrected results are integrated into manuscript sections 2.3, 13.1 and Appendix D.12. They sharpen the source-law obligation rather than closing it by numerical coincidence.

### The stipulated slab and its transport

**S5:P79-112: a finite slab result survives, with reversed stated chirality signs.** Adopt exactly the source's five Clifford matrices, hopping T=-(Gamma5+i*Gamma4)/2, mass 3 and 20 layers. At zero surface momentum its 80-dimensional Hermitian matrix satisfies H^3=H, rank H=76 and trace H=0. Its exact eigenvalue multiplicities are (-1:38, 0:4, +1:38). Two zero modes lie on each boundary. Thus the Gamma-point compact localization can be shown exactly; numerical thresholds such as 1e-16 are not the proof.

For the stated coordinate and Clifford convention, the left boundary's first-order Hamiltonian can be written `kx*sigma_x + ky*sigma_y + kz*sigma_z` and the right boundary's as `kx*sigma_x + ky*sigma_y - kz*sigma_z`. Their velocity determinants have signs +1 and -1. A basis rotation can express the left velocities as (-1,+1,-1), as in the source, but that determinant is still +1. The source explicitly evaluates (-1)*(+1)*(-1) as -1 and (+1)*(-1)*(+1) as +1; both arithmetic signs are reversed. Relabeling boundary orientation can change a chirality convention, but cannot repair those products under the convention actually written.

The Gamma-point result and linear projection do not prove exact compact localization at every momentum, or vanishing finite-slab coupling globally. The mass relation `m_eff=4-2g` is stipulated; no source-complete pushforward from the tetrahedral product carrier derives it. A full occupied-band second Chern calculation, with its sign convention, is not supplied by the Gamma-point check. The slab remains a separate candidate model rather than an admitted UD Hamiltonian.

**S7:P35-66: universal zero reflection and conductance e^2/h rejected.** A three-dimensional Weyl cone has energy E=|k| and longitudinal group velocity kx/|k| in the positive band. Both signs of velocity occur on the same surface. Chirality is not one-way propagation along each coordinate. Even scalar scattering at oblique incidence can reflect within that cone.

For an exact counterexample using the source's continuum Hamiltonian `h=-kx*sigma_x+ky*sigma_y-kz*sigma_z`, set kz=0, ky=1, E=5/3 and introduce the scalar potential step V0=5/12. The incident, reflected and transmitted longitudinal momenta are 4/3, -4/3 and 3/4. The normalized positive-band spinors are `(1,z)/sqrt(2)`, where

\[
z_i=(-4+3i)/5,\quad z_r=(4+3i)/5,\quad z_t=(-3+4i)/5.
\]

Continuity `u_i+r*u_r=t*u_t` gives

\[
r=\frac{z_t-z_i}{z_r-z_t}=\frac{3+4i}{25},\quad
\mathcal R=\frac1{25},\quad
\mathcal T=\frac{v_t}{v_i}|1+r|^2=\frac{24}{25}.
\]

Flux is conserved. Both the incident and reflected states belong to the same cone/surface. This refutes the claim that chirality alone forces all reflection blocks to vanish. It does not predict scattering for an otherwise unspecified UD interface. Nor is a small exponential overlap exactly zero. Leads, widths, transverse channel count, occupations, contact matching and allowed disorder remain necessary for a Landauer conductance calculation.

**S8:P30-71: velocity derivatives are valid; universal Hall response is not derived.** The stated continuum derivatives are J=(-sigma_x,+sigma_y,-sigma_z), in model units. They are velocity matrices; physical electric current additionally needs charge, hbar and a momentum convention. Their anticommutation relations define a Clifford relation, not by themselves a full identification with an SU(2) current theory.

A constant term proportional to sigma_z shifts the Weyl node in kz; it does not gap the three-dimensional two-component cone. Indeed no nonzero 2-by-2 Hermitian matrix anticommutes with all three Pauli matrices. For a fixed nonzero slice parameter M, the source's stated Berry-curvature convention gives the plane integral `C_plane=sgn(M)/2`. This is a noncompact continuum calculation, not an integer Chern number of an already specified compact lattice bundle. An ultraviolet completion and occupied-state prescription are required. The jump between slices is distinct from integrating a three-dimensional conductivity over kz; the latter includes a momentum measure and corresponding length units. Thus the claimed universal `sigma_xy=-1/(2*pi)` is not proved, and its sign cannot be fixed by the source's erroneous chirality products. No conductance or Hall constant is added to the manuscript.

For context, Qi, Hughes and Zhang's standard dimensional-reduction construction is an established four-plus-one-dimensional topological model, not a derivation of a UD generator. Bai, Yang and Chang explicitly calculate angle- and structure-dependent Weyl tunneling. The independently derived counterexample above is sufficient for the present rejection; it does not depend on transferring a numerical result from those papers.

### Finite-group and finite-field calculations

**S5:P178-213 and S7:P100-124: the algebraic core is valid under the declared group and field.** Declare D13 of order 26, generated by r^13=s^2=1 and s*r*s=r^-1, over F7. Since 7 does not divide 26, the group algebra is semisimple. The order of 7 modulo 13 is 12, with 7^6=-1 modulo 13. A primitive thirteenth root lies in L=F_(7^12); its trace u=zeta+zeta^-1 generates K=F_(7^6). The trace has irreducible polynomial

\[
p(x)=x^6+x^5+2x^4+3x^3-x^2+3x-1\quad\text{over }\mathbb F_7.
\]

In the nontrivial cyclic component reflection acts as Frobenius^6. Multiplications by L together with that involution generate End_K(L), giving

\[
\mathbb F_7[D_{13}]\simeq\mathbb F_7\oplus\mathbb F_7\oplus M_2(K).
\]

The simple dimensions over F7 are 1,1,12; the regular multiplicities are 1,1,2. On the 12-dimensional simple, r+r^-1 has characteristic polynomial p(x)^2. Calling this central element a Casimir is terminology; it does not give a physical energy or confinement mechanism.

The field K already splits the dihedral group algebra, although it does not contain zeta itself. For each trace root u the matrices

\[
R=\begin{pmatrix}0&-1\\1&u\end{pmatrix},\qquad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

realize an absolutely irreducible two-dimensional module over K. Their invariant symmetric Gram matrix can be chosen as

\[
G=\begin{pmatrix}2&u\\u&2\end{pmatrix},\qquad \det G=4-u^2\ne0.
\]

The replay verifies the group and Gram identities by arithmetic modulo p(u). This also shows why a full cyclotomic root field need not be the minimal splitting field of the nonabelian group.

**S7:P106-114: quotient correction retained and strengthened.** No surjection D13 onto S3 exists because 6 does not divide 26. Homomorphisms do exist with trivial or order-two image; writing “no map D13 -> S3” without “surjective” is too broad. The matching quotient of the tetrahedral frame group is S4 onto S3 with Klein-four kernel. These are different groups. The suggested future repair `V4 semidirect D13` has order 104, also not divisible by 3, so it cannot surject onto S3 either. Any action of D13 on V4 has image of order at most two in Aut(V4)=S3. This proposal cannot restore the desired quotient by changing the action.

**S8:P115-144: orthogonal-type result valid, metric uniqueness overstated.** The group square map has 14 preimages of the identity and one of every nonidentity rotation. Both one-dimensional characters have indicator (14+12)/26=1; every two-dimensional splitting character has (28-2)/26=1. The explicit G above verifies nondegenerate invariant symmetric forms over K. Such forms on each absolutely irreducible component are unique up to a nonzero scalar, not absolutely unique. A finite field has no compatible ordering that would turn these forms into positive Euclidean metrics. No characteristic-preserving field embedding F7 into R exists. A separate representation and observable bridge is necessary before any physical metric interpretation.

These finite-group results are preserved in the audit and replay. They are standard conditional mathematics on an auxiliary chosen group/field. Neither the number of nonreference Boolean labels nor the legacy 13-pi-squared expression selects a physical F7 or D13 action. Without a supplied action on the native carrier and intertwiners to its real S4 representation, they do not close a UD formation, holonomy, metric or time-reversal claim. The manuscript adds only the relevant group/field typing qualification.

## Publication decisions and next dependency

The manuscript v0.10 integrates the receipt-counting repair, the weight-composition table, the two 108-count subsets with intersection 36, and the general criterion for a cost to descend to a receipt. These findings directly strengthen its narrative about distinction, accessible history and the source of dynamics. A short symmetry qualification keeps group, field and representation changes explicit.

The isolated standard modular algebra and independently stipulated Wilson-Dirac model remain in the companion research record. Their inclusion as established UD physics would lengthen the manuscript while introducing unclosed correspondence assumptions. The original source documents and ledger are preserved, not rewritten or automatically promoted.

The most valuable next theoretical task is to specify the admissible fine-history space, composable event graph and complete next-event kernel, together with the winding/record functional on that history. Then test whether the proposed functional is constant on each available receipt fiber. This makes a winding-cost claim falsifiable and tells us what additional receipt coordinates are needed. It precedes further numerical matching, Hall-response claims or adding framing groups.

## Verification and references

Run `python3 verify_additional_research.py` with Python 3 and SymPy. The independent replay checks all label counts and intersections, finite-field irreducibility and Frobenius relations, explicit group/Gram identities, order obstructions, indicators, exact Gamma-point slab identities, corrected projected chiralities and the scalar-step reflection witness. The code does not execute imported snippets. It does not compute a full occupied-band Chern number or a native UD transport conductance, and does not repeat every historical manuscript replay.

The functional-factorization criterion, winding lift counterexample and group-order obstruction are mathematical arguments with written assumptions. The finite checks support their applications; they do not supply independent review. The accompanying register records each source, dependency, disposition and review lane. The paper remains a review candidate; no registry or physical promotion is asserted.

1. Supplied sources S5, S7, S8, identified by exact hashes above. Source labels “EXACT” are claims to be checked, not review receipts.
2. Supplied coefficient ledger v0.39, 22 August 2026; supplied CRL-2 governance amendment, status proposal. Exact input hashes are in `SOURCE_REGISTER.json`.
3. Qi, Xiao-Liang, Taylor Hughes and Shou-Cheng Zhang. *Topological Field Theory of Time-Reversal Invariant Insulators*. Physical Review B 78, 195424 (2008). [arXiv:0802.3537](https://arxiv.org/abs/0802.3537), [DOI](https://doi.org/10.1103/PhysRevB.78.195424). Background provenance for a standard topological model, not a UD bridge.
4. Bai, Chunxu, Yanling Yang and Kai Chang. *Chiral tunneling in gated inversion symmetric Weyl semimetal*. Scientific Reports 6, 21283 (2016). [DOI](https://doi.org/10.1038/srep21283). Primary context for angle-dependent tunneling; the exact scalar-step counterexample here is independently derived.
