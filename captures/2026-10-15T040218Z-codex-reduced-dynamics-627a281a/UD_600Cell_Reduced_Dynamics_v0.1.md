# UD 600-cell reduced dynamics: spectra, interaction mixing and fibration selection

Version 0.1 | 15 October 2026 UTC | Development; no registry entry | Physical promotion 0

## Outcomes and limits

All ten 264-by-264 reduced generators have been constructed with three symbolic degree-exchange coefficients a,b,c. Exact sparse entries are supplied over Q(zeta10), and the squared-singular-value characteristic polynomials are factored over Q(sqrt(5)). Six representative sectors suffice for the spectral tables: sectors 6,7,8,9 are the conjugates of 4,3,2,1. Explicit matrices are supplied for all ten.

The spectrum is the union of three exchange families, rather than a mixed cubic equation in a,b,c. This follows from the boundary-square identities. The finite spectral verification comprises 110 exact checks (including finite-field determinant checks) and 24 separately labelled numerical corroborations. Ten symbolic generators also pass coefficient-wise skew-Hermitian checks. Exact interaction tests distinguish orbit-complete gates, a single-face gate, alternating contrasts and orthogonal quaternion controls. These controls are separately declared candidates; they are not automatically native UD interactions.

A state-dependent fibration selector is formulated with a declared least-squares objective, covariance, tie handling and an error margin. Geometry alone cannot choose uniquely among the six symmetry-related right-quaternion fibrations. Moreover all six proposed coherence scores are conserved by the symmetric free dynamics. The selector therefore reads an existing asymmetry; that flow does not generate one. Native selection remains open and has not been hidden in a coordinate choice.

The baseline assessment and exact 600-cell data are preserved by hash and prior capture commit. The current repository base is pinned in SOURCE_REGISTER.json. The two historical user-supplied documents retain their original status and bytes. Their master action, coefficient normalization and seam-source gaps are not closed by this calculation. Constructor checks do not constitute independent review.

## 1. Exact construction of the ten generators

Use the preceding declared regular 600-cell boundary K, its sorted oriented simplex basis and unit simplex metric. The dimensions of C0,C1,C2,C3 are 120,720,1200,600. The signed right action T induced by a unit quaternion g of order ten has free length-ten simplex orbits. Counts by degree are 12,72,120,60.

For each degree choose the least indexed simplex r_alpha in an orbit, and write

\[
T^l e_{r_\alpha}=s_{\alpha,l}e_{j_{\alpha,l}},\qquad
u_{\alpha,m}=\frac1{\sqrt{10}}\sum_{l=0}^9
\zeta^{-ml}s_{\alpha,l}e_{j_{\alpha,l}},\quad \zeta=e^{2\pi i/10}.
\]

This is a reproducible basis convention, not a physical axis selector. T u_alpha,m=zeta^m u_alpha,m. Let Q_k,m collect these columns. The restricted boundary is B_k,m=Q_(k−1),m* B_k Q_k,m.

There is an integer polynomial representation that avoids storing approximate phases. For a representative k-simplex r_beta, every oriented boundary face f lies at position l of a (k−1)-orbit alpha. If its boundary sign is epsilon and the orbit transport sign at f is s_alpha,l, then add epsilon s_alpha,l z^l to B_k(z)[alpha,beta]. Thus

\[
B_{k,m}=B_k(\zeta^m),\qquad B_k(z)\in
\operatorname{Mat}\bigl(\mathbb Z[z]/(z^{10}-1)\bigr).
\]

The positive exponent is fixed by the negative exponent in the basis definition above. All representative indices, signed orbits and polynomial entries are in REDUCED_GENERATORS.json. The group-ring identities B1(z)B2(z)=0 and B2(z)B3(z)=0 are checked exactly modulo z^10−1. These certify the reduced chain identities simultaneously for every m.

The actual symbolic reduced generator is

\[
A_m(a,b,c)=
\begin{pmatrix}
0&-aB_{1,m}&0&0\\
aB_{1,m}^{\dagger}&0&-bB_{2,m}&0\\
0&bB_{2,m}^{\dagger}&0&-cB_{3,m}\\
0&0&cB_{3,m}^{\dagger}&0
\end{pmatrix},\quad (a,b,c)\in\mathbb R^3.
\]

TEN_SYMBOLIC_GENERATORS.json explicitly records all ten matrices, with 14616 nonzero entries in total. Each entry has row, column, coefficient-channel and four integer field coefficients. The field relation is zeta^4−zeta^3+zeta^2−zeta+1=0. ALL_REDUCED_BLOCKS.json separately records the three restricted boundary matrices per sector. These are executable specifications of the matrices, not only a statement that they exist.

## 2. Complete symbolic spectrum

Define the three Hermitian positive semidefinite matrices

\[
G_{1,m}=B_{1,m}B_{1,m}^{\dagger}\ (12\times12),\quad
G_{2,m}=B_{2,m}B_{2,m}^{\dagger}\ (72\times72),\quad
G_{3,m}=B_{3,m}^{\dagger}B_{3,m}\ (60\times60).
\]

Their nonzero eigenvalues are the squared singular values mu of the corresponding boundaries. Because successive boundaries compose to zero, im(B_k*) and im(B_(k+1)) are orthogonal. On every singular-vector pair the full generator is a 2-by-2 skew exchange with eigenvalues plus/minus i a_k sqrt(mu), where (a1,a2,a3)=(a,b,c). No simultaneous mixing of a,b,c is needed on these orthogonal Hodge subspaces.

If F_k,m(u) is the monic polynomial containing the positive eigenvalues of G_k,m with multiplicity, and r_k,m its degree, then

\[
\boxed{\chi_{A_m}(\lambda)=\lambda^{h_m}
\prod_{k=1}^3(-a_k^2)^{r_{k,m}}
F_{k,m}(-\lambda^2/a_k^2).}
\]

This is a polynomial identity, extended to a_k=0 by its polynomial limit. For nonzero coefficients h0=2, h_m=0 otherwise. The nonzero singular ranks are (11,61,59) in m=0 and (12,60,60) in every other sector. Turning off channel k adds 2 r_k,m zero modes. Zeros in the individual rectangular Gram matrices must not be counted again as harmonic zeros of A_m.

EXACT_SPECTRA.json contains the full characteristic coefficients and factorizations for every G_k,m, including their Gram zeros. Appendix A below gives the positive-root factors F_k,m. A factor f(u)^e means that every root mu of f contributes multiplicity e to each of the two generator eigenvalues plus/minus i a_k sqrt(mu). All these mu are positive, since the exact Gram characteristic polynomials account for the eigenvalues of a positive semidefinite matrix and their zero factors have been removed.

For example, the complete m=5 characteristic polynomial is particularly compact:

\[
\begin{aligned}
\chi_{A_5}(\lambda)={}&(\lambda^2+14a^2)^{12}
(\lambda^2+4b^2)^{12}(\lambda^2+7b^2)^{24}\\
&\times(\lambda^4+14b^2\lambda^2+44b^4)^4
(\lambda^4+11b^2\lambda^2+23b^4)^8\\
&\times(\lambda^4+7c^2\lambda^2+11c^4)^4
(\lambda^4+10c^2\lambda^2+23c^4)^8\\
&\times(\lambda^6+11c^2\lambda^4+33c^4\lambda^2+28c^6)^{12}.
\end{aligned}
\]

Its degree is 264. The a-channel contributes 12 oscillator pairs, and the b- and c-channels contribute 60 each. The displayed polynomial also shows explicitly how coefficient-zero limits behave.

There is no nonzero exact global recurrence period on the entire 2640-dimensional carrier for any (a,b,c) other than (0,0,0). If a is nonzero, its spectrum includes |a|sqrt(12) and |a|sqrt(15), with irrational ratio sqrt(5)/2. If a=0 and b is nonzero, the b-channel includes 2|b| and sqrt(7)|b|. If only c is nonzero, the c-channel includes sqrt(3)|c| and 2|c|. A common return would require rational frequency ratios. State-restricted periodicity and approximate finite-dimensional recurrence remain possible. The model clock is still uncalibrated physical time.

## 3. Which interactions preserve the sectors?

For an added linear operator E the exact test is P_m E P_n=0 for all m≠n, equivalently [E,T]=0. For a sum of candidates E=sum gamma_j E_j, the corresponding off-diagonal blocks must cancel; preservation of one summand cannot be inferred from preservation of the total. This is a linear constraint on the supplied coefficients.

### 3.1 Face gates and contrast profiles

The ledger's Q173 motivates a declared face-contact response with B3 replaced in the upper contact by F B3 and in the lower contact by B3* F, where F=diag(h_f) is real. The resulting full generator stays skew. It preserves the ten sectors if and only if h_f is constant along every chosen ten-face T-orbit. For necessity, [T2,F]B3 has in each row a scalar orbit-weight difference times a nonzero permuted boundary row; no such row can vanish unless the difference is zero. Sufficiency follows from [T2,F]=0 and boundary equivariance. This statement concerns the full operator and all admitted states, rather than an accidental state with zero leakage.

Write an orbit contrast as

\[
\delta h_l=\sum_{s=0}^9\widehat h_s\zeta^{-sl},\qquad
\widehat h_s=\frac1{10}\sum_l\delta h_l\zeta^{sl}.
\]

Its Fourier component s sends sector n into sector m=n+s modulo ten. Real contrasts have conjugate opposite shifts. Thus a desired selective mixing pattern can be specified without claiming that its profile is natively generated. Constant profiles preserve m; alternating profiles shift by five; a single-face impulse contains all ten shifts.

### 3.2 Exact finite interaction results

The following numbers count nonzero blocks in the 10-by-10 array E_mn. They are computed with exact cyclotomic arithmetic, including the 1/10 basis normalization. Frobenius squares are stored as rational coefficients of 1 and phi in INTERACTION_AND_SELECTION_CHECKS.json.

| Declared operator/control | Nonzero sector blocks | Result |
| --- | ---: | --- |
| Each uniform degree exchange G1,G2,G3 | 10 | Preserves every m |
| Change contacts on one complete ten-face orbit | 10 | Preserves every m |
| Change contacts on one face | 100 | Every m,n is coupled |
| Alternating signed contrast on one ten-face orbit | 10 | Only m=n+5 |
| Change every other face on that orbit, as a hard-gate perturbation | 20 | Only m=n or m=n+5 |
| Supplied left-quaternion geometric control | 10 | Preserves every m |
| Supplied right normalizer control reversing g to g^(-1) | 10 | Permutes n into −n; preserves the paired real sectors |
| Tested right-quaternion control outside the normalizer | 50 | Couples exactly the same-parity pairs for this explicit control |

The left/right controls are orthogonal signed chain automorphisms, not skew infinitesimal generators by themselves. Their sector transfer describes a supplied finite control operation. A generator realizing such a control requires its own interaction/time/resource specification. The generic example must not be read as a theorem that every element outside the normalizer has identical nonzero block entries. The central antipodal action commutes with all left/right quaternion rotations, which explains the even/odd restriction. Right-multiplication normalizer and centralizer orders are exactly 20 and 10 in the tested binary group.

The quaternion controls commute with the free incidence generator even when they mix the chosen character sectors. Degenerate frequency spaces allow that mixing. Thus changing a character label is not by itself an energy transfer or new force. All such controls preserve the central antipodal even/odd split, whose two real dimensions are 1320 and 1320; this coarser decomposition does not require a Hopf-axis choice.

For the single-face contact perturbation, every block has exactly

\[
\|E_{mn}\|_F^2=1/25.
\]

The full perturbation has operator norm sqrt(2): it is the skew exchange between the face vector and its signed two-cell incidence vector. Multiplication by a supplied amplitude gamma scales these squares by gamma^2 and the operator norm by |gamma|. The previous Duhamel argument consequently bounds leakage from any original sector by min(1,sqrt(2)|gamma| |t|). This is a worst-case comparison, not a transition probability or a measured damping rate.

Sector preservation is distinct from nilpotence. The tested complete-orbit gate has ||B2 D B3||_F^2=60; a single-face gate gives 6, with D its selected-face projector. Thus both generally break the original boundary composition when interpreted as B3→D B3 while B2 is held fixed. Such gates are response interactions on the existing carrier. They cannot simultaneously be treated as unchanged ordinary chain boundaries when importing the free Hodge spectral formula. Their perturbed spectra are not given by the free-channel factors above.

### 3.3 Seam and additional interaction boundary

The supplied seam_phase_transport.md, master_action.md and coherence_equation.md are placeholders. No source-complete seam matrix on the 600-cell is supplied by them. The historical ledger's w_ij, Xi_ij and action normalization entries remain open. Consequently no specific seam spectrum or physical coupling is invented here.

For a proposed block C_k between adjacent degrees, the needed condition is T_(k−1) C_k=C_k T_k. For a transported internal fibre the action and transport must be lifted and their covariance checked on that enlarged space. This is a precise admission test for the missing source, not a substitute for its definition.

## 4. Fibration selection: an obstruction and a conditional rule

Fix the declared right-quaternion family. Conjugation of C10 inside 2I gives six distinct cyclic subgroups H. They are transitively related, with normalizer order 20 and index 120/20=6. Geometry invariant under that action cannot have a unique deterministic equivariant output in this six-element set: an invariant input would require an output fixed by every symmetry, and none exists. The choice of a right rather than left family itself also needs an orientation/chirality convention if the full reflection group is admitted.

The symmetric generator has the same sector spectra after conjugating the fibration, up to generator/character relabeling. Its spectrum therefore cannot distinguish those equivalent axes. A lexicographic quaternion choice is a computational convention, not a source rule.

Here is an explicit state-conditioned candidate with a declared operational objective. Let

\[
\Pi_H=\frac1{10}\sum_{h\in H}\rho(h),\quad
s_H(x)=\|\Pi_H x\|^2,\quad
\mathcal H_*(x)=\operatorname*{arg\,max}_H s_H(x).
\]

Pi_H is the orthogonal projector onto the H-invariant chain states. The rule minimizes the squared projection residual ||x−Pi_H x||^2, equivalently maximizing the retained zero-character coherent weight. That least-squares objective is newly declared; it is not a derivation that nature must optimize it. A unique maximizer returns one fibration. A tie returns the tied set and an unresolved-selection receipt. Resolving the tie requires additional state/history/asymmetry or an explicitly normalized stochastic rule.

This selector is equivariant: rho(q) Pi_H rho(q)^(-1)=Pi_(qHq^(-1)) implies the score vector and its argmax transform covariantly. For state uncertainty ||delta x||≤delta and ||x||≤R,

\[
|s_H(x+\delta x)-s_H(x)|\le2R\delta+\delta^2.
\]

If the best-to-second score gap Delta exceeds 4R delta+2 delta^2, the selected fibration is unchanged. This is a sufficient deterministic robustness margin; it does not guarantee uniqueness when the gap vanishes.

Exact examples on unit-norm vertex states are:

| Input state | Six scores | Selection |
| --- | --- | --- |
| Uniform vertex state | All 1 | Six-way tie |
| One vertex basis state | All 1/10 | Six-way tie |
| Equal positive amplitudes on the ends of one edge through the identity | One 1/5 and five 1/10 | Unique; gap 1/10 |
| Equal amplitudes on the ten vertices of one subgroup fibre | One 1 and five 1/5 | Unique; gap 4/5 |

The last example is not a source-generation theorem: the input already contains the fibre asymmetry. The edge example shows that an entire fibre need not be supplied, but its coherent edge preparation is still a premise. Relative signs/phases matter because the objective retains the zero-character component; a population-only input would be a different state/readout contract.

There is an additional dynamical no-go for this candidate objective. Every H acts by chain automorphisms, so [A,Pi_H]=0 and

\[
\frac{d}{dt}s_H(e^{tA}x)=0.
\]

All six scores and their gaps are conserved under the symmetric free flow, for arbitrary uniform symbolic a,b,c. It cannot break a tie or produce a new preferred fibration according to this rule. A source interaction, symmetry-breaking preparation, update/attachment or open process must change the scores if actual preference formation is intended. An externally chosen gate can provide that asymmetry, but specifying its orbit has already supplied information about the fibration and must not be counted as its derivation.

## 5. What is closed and what remains

Closed on the declared finite carrier: all ten reduced matrices; complete algebraic free spectra for symbolic a,b,c, including coefficient-zero limits; exact mixing tests for the listed operators; Fourier selection rules for orbit profiles; the geometry-only selection obstruction; and a conditional state-based selector with exact examples and an uncertainty margin.

Open: a native source of the symmetry-breaking state or interaction, the operational reason for optimizing the chosen score, a complete seam/internal gauge model, spectra after arbitrary sector-mixing perturbations, physical action/clock calibration, and the current manuscript's preparation/blank-production mechanisms. These computations do not identify Standard Model charges or running couplings.

A unique fibration is unnecessary for using symmetry as a computational basis: conjugate choices yield equivalent calculations. A native selector becomes necessary if UD assigns a preferred fibration physical meaning.

The highest-value next closure is a declared source interaction that changes the six scores, with a full joint state, resources and stability analysis. The exact gates and mixing arrays now provide a test harness for that proposal. The finite nonlinear/open law must be supplied or derived before reporting a selected axis as a physical outcome.

## Reproducibility and provenance

The construction uses the preceding exact finite complex as data; it executes no imported partner or archived source code. Standard orthogonal projection, Fourier and Hodge singular-value methods are being applied, not claimed as new methods. The original 600-cell quaternion coordinates and symmetry context are credited in the preserved baseline note to Koca et al., arXiv:0906.2109v2, §3, and Dechant, arXiv:1602.05985, §§5-6. The present orbit-representative matrices, polynomials, mixing arrays and source-rule tests are independently constructed development results.

Run the new scripts in this order: `build_reduced.py`, `exact_spectra.py`, `export_generators.py`, `verify_reduced_spectra.py`, `test_interactions.py`. Required packages are Python, NumPy, SciPy, SymPy and python-flint. Exact spectral characteristic polynomials use integer matrix arithmetic in the basis (1,zeta,zeta^2,zeta^3) and Newton identities; m=0 and m=5 use direct integer characteristic polynomials. Independent checks reconstruct all factors, annihilate each Gram matrix with the squarefree factor product, test coprimality, and compare direct characteristic polynomials over two finite fields. Numerical eigensolver checks are separately labelled. Their tolerances do not establish the exact claims.

All exact matrices and spectral multiplicities are in the evidence package. The prior complex generator/check script is preserved with its own status, but the full prior manuscript/research replays are not all rerun. The narrative manuscript is not revised by this separate technical package. The unavailable `Gap2_FINAL_Finite_Genesis.png` is excluded.

# Appendix A. Complete positive squared-singular-value factors

The following factors define F_k,m(u); zero Gram factors are omitted. Sector m and 10−m have identical polynomials. The exponent is the multiplicity of each root, not its decimal approximation. Factors are over Q(sqrt(5)).

## A.1 Exchange channel 1

\[
\begin{aligned}
F_{1,0}(u)={}&\left(u - 10 - 2 \sqrt{5}\right)^{3} \left(u - 10 + 2 \sqrt{5}\right)^{3} \left(u - 12\right)^{5}
\end{aligned}
\]

\[
\begin{aligned}
F_{1,1}(u)={}&\left(u - 9 + 3 \sqrt{5}\right)^{2} \left(u - 9\right)^{4} \left(u - 14\right)^{6}
\end{aligned}
\]

\[
\begin{aligned}
F_{1,2}(u)={}&\left(u - 10 + 2 \sqrt{5}\right)^{3} \left(u - 15\right)^{4} \left(u - 12\right)^{5}
\end{aligned}
\]

\[
\begin{aligned}
F_{1,3}(u)={}&\left(u - 9 - 3 \sqrt{5}\right)^{2} \left(u - 9\right)^{4} \left(u - 14\right)^{6}
\end{aligned}
\]

\[
\begin{aligned}
F_{1,4}(u)={}&\left(u - 10 - 2 \sqrt{5}\right)^{3} \left(u - 15\right)^{4} \left(u - 12\right)^{5}
\end{aligned}
\]

\[
\begin{aligned}
F_{1,5}(u)={}&\left(u - 14\right)^{12}
\end{aligned}
\]

## A.2 Exchange channel 2

\[
\begin{aligned}
F_{2,0}(u)={}&\left(u - 5 - 2 \sqrt{5}\right)^{4} \left(u - \frac{15}{2} - \frac{\sqrt{5}}{2}\right)^{4} \left(u - \frac{15}{2} + \frac{\sqrt{5}}{2}\right)^{4}\\
&\times \left(u - 5 + 2 \sqrt{5}\right)^{4} \left(u - 8\right)^{5} \left(u^{2} - 11 u + 27\right)^{4}\\
&\times \left(u^{2} - 11 u - 2 \sqrt{5} + 22\right)^{8} \left(u^{2} - 11 u + 2 \sqrt{5} + 22\right)^{8}
\end{aligned}
\]

\[
\begin{aligned}
F_{2,1}(u)={}&\left(u - \frac{9}{2} - \frac{3 \sqrt{5}}{2}\right)^{2} \left(u - 7 + \sqrt{5}\right)^{2} \left(u - 9\right)^{4}\\
&\times \left(u - 4\right)^{6} \left(u - \frac{9}{2} + \frac{3 \sqrt{5}}{2}\right)^{6} \left(u - 7 - \sqrt{5}\right)^{8}\\
&\times \left(u - 7\right)^{12} \left(u^{2} - 11 u + 23\right)^{10}
\end{aligned}
\]

\[
\begin{aligned}
F_{2,2}(u)={}&\left(u - 5 + 2 \sqrt{5}\right) \left(u - \frac{15}{2} + \frac{\sqrt{5}}{2}\right)^{3} \left(u - 5\right)^{4}\\
&\times \left(u - 8\right)^{5} \left(u - \frac{15}{2} - \frac{\sqrt{5}}{2}\right)^{7} \left(u^{2} - 11 u + 2 \sqrt{5} + 22\right)^{3}\\
&\times \left(u^{2} - 11 u - 2 \sqrt{5} + 22\right)^{8} \left(u^{2} - 11 u + 27\right)^{9}
\end{aligned}
\]

\[
\begin{aligned}
F_{2,3}(u)={}&\left(u - 7 - \sqrt{5}\right)^{2} \left(u - \frac{9}{2} + \frac{3 \sqrt{5}}{2}\right)^{2} \left(u - 9\right)^{4}\\
&\times \left(u - 4\right)^{6} \left(u - \frac{9}{2} - \frac{3 \sqrt{5}}{2}\right)^{6} \left(u - 7 + \sqrt{5}\right)^{8}\\
&\times \left(u - 7\right)^{12} \left(u^{2} - 11 u + 23\right)^{10}
\end{aligned}
\]

\[
\begin{aligned}
F_{2,4}(u)={}&\left(u - 5 - 2 \sqrt{5}\right) \left(u - \frac{15}{2} - \frac{\sqrt{5}}{2}\right)^{3} \left(u - 5\right)^{4}\\
&\times \left(u - 8\right)^{5} \left(u - \frac{15}{2} + \frac{\sqrt{5}}{2}\right)^{7} \left(u^{2} - 11 u - 2 \sqrt{5} + 22\right)^{3}\\
&\times \left(u^{2} - 11 u + 2 \sqrt{5} + 22\right)^{8} \left(u^{2} - 11 u + 27\right)^{9}
\end{aligned}
\]

\[
\begin{aligned}
F_{2,5}(u)={}&\left(u - 7 - \sqrt{5}\right)^{4} \left(u - 7 + \sqrt{5}\right)^{4} \left(u - 4\right)^{12}\\
&\times \left(u - 7\right)^{24} \left(u^{2} - 11 u + 23\right)^{8}
\end{aligned}
\]

## A.3 Exchange channel 3

\[
\begin{aligned}
F_{3,0}(u)={}&\left(u - \frac{3}{2} - \frac{\sqrt{5}}{2}\right)^{3} \left(u - \frac{3}{2} + \frac{\sqrt{5}}{2}\right)^{3} \left(u - 5\right)^{4}\\
&\times \left(u - 3\right)^{4} \left(u - 4 - \sqrt{5}\right)^{4} \left(u - 4 + \sqrt{5}\right)^{4}\\
&\times \left(u - 4\right)^{6} \left(u - \frac{11}{2} - \frac{\sqrt{5}}{2}\right)^{8} \left(u - \frac{11}{2} + \frac{\sqrt{5}}{2}\right)^{8}\\
&\times \left(u^{3} - 11 u^{2} + 33 u - 24\right)^{5}
\end{aligned}
\]

\[
\begin{aligned}
F_{3,1}(u)={}&\left(u - 6\right)^{2} \left(u - \frac{7}{2} + \frac{\sqrt{5}}{2}\right)^{2} \left(u - \frac{7}{2} + \frac{3 \sqrt{5}}{2}\right)^{2}\\
&\times \left(u - \frac{7}{2} - \frac{\sqrt{5}}{2}\right)^{8} \left(u^{2} - 5 u + 3\right)^{4} \left(u^{2} - 10 u + 23\right)^{10}\\
&\times \left(u^{3} - 11 u^{2} + 33 u - 28\right)^{6}
\end{aligned}
\]

\[
\begin{aligned}
F_{3,2}(u)={}&\left(u - 5\right) \left(u - 4\right)^{3} \left(u - \frac{11}{2} - \frac{\sqrt{5}}{2}\right)^{3}\\
&\times \left(u - \frac{3}{2} + \frac{\sqrt{5}}{2}\right)^{3} \left(u - 4 + \sqrt{5}\right)^{3} \left(u - 4 - \sqrt{5}\right)^{7}\\
&\times \left(u - \frac{11}{2} + \frac{\sqrt{5}}{2}\right)^{8} \left(u - 3\right)^{9} \left(u^{2} - 9 u + 15\right)^{4}\\
&\times \left(u^{3} - 11 u^{2} + 33 u - 24\right)^{5}
\end{aligned}
\]

\[
\begin{aligned}
F_{3,3}(u)={}&\left(u - 6\right)^{2} \left(u - \frac{7}{2} - \frac{3 \sqrt{5}}{2}\right)^{2} \left(u - \frac{7}{2} - \frac{\sqrt{5}}{2}\right)^{2}\\
&\times \left(u - \frac{7}{2} + \frac{\sqrt{5}}{2}\right)^{8} \left(u^{2} - 5 u + 3\right)^{4} \left(u^{2} - 10 u + 23\right)^{10}\\
&\times \left(u^{3} - 11 u^{2} + 33 u - 28\right)^{6}
\end{aligned}
\]

\[
\begin{aligned}
F_{3,4}(u)={}&\left(u - 5\right) \left(u - 4\right)^{3} \left(u - 4 - \sqrt{5}\right)^{3}\\
&\times \left(u - \frac{3}{2} - \frac{\sqrt{5}}{2}\right)^{3} \left(u - \frac{11}{2} + \frac{\sqrt{5}}{2}\right)^{3} \left(u - 4 + \sqrt{5}\right)^{7}\\
&\times \left(u - \frac{11}{2} - \frac{\sqrt{5}}{2}\right)^{8} \left(u - 3\right)^{9} \left(u^{2} - 9 u + 15\right)^{4}\\
&\times \left(u^{3} - 11 u^{2} + 33 u - 24\right)^{5}
\end{aligned}
\]

\[
\begin{aligned}
F_{3,5}(u)={}&\left(u - \frac{7}{2} - \frac{\sqrt{5}}{2}\right)^{4} \left(u - \frac{7}{2} + \frac{\sqrt{5}}{2}\right)^{4} \left(u^{2} - 10 u + 23\right)^{8}\\
&\times \left(u^{3} - 11 u^{2} + 33 u - 28\right)^{12}
\end{aligned}
\]

