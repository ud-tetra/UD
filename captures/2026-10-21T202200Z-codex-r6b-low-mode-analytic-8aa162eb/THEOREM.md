# Exact low-mode reduction of the three depth-1 R6b modules

RESULT — EXACT CONDITIONAL. Each of the three constant-depth-1 modules of clean level-4 R6b has an exactly invariant two-coordinate sector containing its unique negative eigenvalue. Both channel profiles have exactly uniform squared magnitude within the module. Every nonzero state in the resulting three-module negative branch has component-conditioned localization score1. This replaces the floating-point observation by a source-bound theorem on these three modules.

Development; no registry entry. Constructor proof and exact verification only; independent review pending. Physical promotion0. The real symmetric source matrix is not identified with physical energy, particle mass or a temporal instability law.

## 1. Source and domain

Source main:8be4e90d68528325f081126d27c61ac61cad951e, `docs/hmulti_r6b.py`. The source code and AGENTS.md are unchanged from the preceding replay base. L=4 gives four disconnected64-site modules per channel. In the modules whose first base4 digit is1,2 or3, the source depth is h=1 at every site. The first-digit-zero module has varying depth and is excluded from the exact profile theorem below.

Set

\[
\eta=185/192,\quad\delta=1-\eta=7/192,\quad
v=\delta^2,\quad c=\eta^3\delta^3,\quad r=4\eta^2+v.
\]

These expressions follow directly from the source rho potential delta(1-eta^h) and cross coefficient eta^2 delta(1-eta^h)(eta^h-eta^(2h)) at h=1. No value is chosen using the previous numerical eigenvalues.

On one64-site module let L_sib be the disjoint union of sixteen K4 graph Laplacians, let D be the diagonal source parity matrix, and let L_Theta be the source cousin/second-cousin weighted Laplacian. The coupled source block is

\[
H=\begin{pmatrix}\eta^2 L_{\rm sib}+vI&cD\\cD&L_\Theta\end{pmatrix}.
\]

All metrics here are the frozen identity metrics in the source site coordinates. These are rho/Theta simulation channels, not the separate six-edge particle-candidate algebra.

## 2. Exact invariant two-coordinate sector

Define u=(1,...,1)/8 and p=D u. Both have norm1. The parity alternates twice positive/twice negative inside every sibling group of4, so L_sib p=4p. Since the Theta module is connected and conservative, L_Theta u=0. Also Dp=u and Du=p.

For e_rho=(p,0), e_Theta=(0,u), direct multiplication gives

\[
H e_\rho=r e_\rho+c e_\Theta,\qquad
H e_\Theta=c e_\rho.
\]

The embedding Q=(e_rho,e_Theta) is orthonormal and satisfies

\[
HQ=QK,\qquad K=\begin{pmatrix}r&c\\c&0\end{pmatrix}.
\]

The exact verifier avoids radicals in Q by checking the integer-column embedding B=8Q: B^T B=64I2 and HB=BK. It constructs and verifies all three parity-distinct source modules separately using rational arithmetic.

The eigenvalues are

\[
\lambda_\pm=\frac{r\pm\sqrt{r^2+4c^2}}2,\qquad
\lambda_-=-\frac{2c^2}{r+\sqrt{r^2+4c^2}}<0<\lambda_+.
\]

The second form avoids numerical cancellation. A corresponding normalized negative-branch vector is

\[
z_- = \frac{((\lambda_-/c)p,\ u)}{\sqrt{1+(\lambda_-/c)^2}}.
\]

Thus

\[
W_\rho=\frac{(\lambda_-/c)^2}{1+(\lambda_-/c)^2},\qquad
W_\Theta=\frac1{1+(\lambda_-/c)^2}.
\]

These are normalized channel weights in the declared finite model, not fitted physical probabilities.

## 3. It is the module's unique negative branch

For completeness, let E4,E16,E64 average within aligned groups of4,16,64 sites. Their nested ranges give the orthogonal decomposition

\[
L_\Theta=(12a+48b)(I-E_4)+(16a+48b)(E_4-E_{16})
+64b(E_{16}-E_{64}),\quad a=\eta^4,\ b=\eta^6.
\]

The three displayed projectors have ranks48,12,3; the remaining projector E64 has rank1 and eigenvalue zero. Entrywise equality with the constructed source Laplacian is checked for each module. This gives the smallest positive eigenvalue

\[
g=12\eta^4+48\eta^6.
\]

For this eta it is less than both64 eta^6 and16 eta^4+48 eta^6, as exact fractions verify. The complement of Q is invariant because H is symmetric. For (x,y) in that complement, x is orthogonal to p and y to u. Therefore

\[
\langle(x,y),H(x,y)\rangle
\ge v\|x\|^2-2c\|x\|\|y\|+g\|y\|^2
\ge\frac v2\|x\|^2+
\left(g-\frac{2c^2}{v}\right)\|y\|^2.
\]

The exact inequality g-2c^2/v>v/2 holds. Hence all eigenvalues on Q-perp are at least v/2; lambda_plus>r>v/2 also. The two-coordinate sector contains the only negative eigenvalue of the128-coordinate module. Negative matrix eigenvalue is not by itself a dynamical-instability theorem: the physical evolution law and energy identification remain separate.

A forward rational enclosure is

\[
-\frac{c^2}{r}<\lambda_-<
-\frac{c^2}{r+c^2/r}<0.
\]

It follows from r<sqrt(r^2+4c^2)<r+2c^2/r. The saved100-digit evaluation falls strictly inside this exact interval. Numeric values are corroboration of the algebraic expression, not its definition.

## 4. Exact component-conditioned score

Since |u_i|^2=|p_i|^2=1/64, normalizing either nonzero channel of z_minus gives uniform probability within that module. Consequently IPR_channel=1/64 and F_within=64 IPR_channel=1 exactly. The rho channel is very small but its conditional profile is still mathematically uniform; the actual W_rho must remain visible in any measurement interpretation.

Let z_minus,j be the normalized branch vector in each of the three modules. These vectors have disjoint support and equal eigenvalue. Every vector in their branch is

\[
z=\sum_{j=1}^3\alpha_j z_{-,j},\qquad\sum_j|\alpha_j|^2=1.
\]

In either separately normalized channel its module weights are w_j=|alpha_j|^2 and its within-module probabilities are uniform. Thus for the full256-site register

\[
F_{\rm global}=4\sum_j w_j^2\in[4/3,4],\qquad
I_{\rm comp}=\sum_j w_j^2,\qquad
\boxed{\overline F_{\rm within}=1.}
\]

Changing the orthonormal basis inside this branch changes individual global scores but never creates within-module localization. The rank3 branch projector's normalized Theta density is uniform over the192 sites of these three modules, yielding global F=4/3. This statement concerns the branch supported on these modules and does not assert an unproved global multiplicity or profile for the excluded fourth module.

## 5. Relation to the numerical replay

The branch formula gives lambda_minus approximately -5.05879939585e-10 and Theta weight approximately0.999999999863827. REPLAY_COMPARISON.json records a100-digit forward evaluation, the numerical dense-cluster interval and the corresponding three sparse-probe values from PR352. The original replay result/payload hashes are preserved so these observations cannot become inputs to the algebra.

The numerical cluster's small spread is consistent with its finite-precision residuals and the exact same source eigenvalue on the three modules. The prior sparse values near -5.05840557449e-10 differ from the rational-source root by about3.94e-14. The stored floating matrix has a nonzero Theta uniform-vector Rayleigh shift of about4.40e-14, where the rational source has exactly zero. An exact audit of the stored IEEE entries records its two-column Rayleigh compression and its nonzero embedding leakage separately from solver error. The compressed root is not asserted to be an exact eigenvalue of those floating bytes.

Small globally scaled residuals do not certify all relative digits of a5e-10 eigenvalue or remove source-to-floating-matrix error. These differences remain within the prior absolute residual scale; the earlier finite replay passes its declared tolerance, while the analytic source root is the appropriate value for the exact theorem. No source coefficient or old tolerance was changed.

The present proof closes the conditional profile conclusion for this branch; it does not authenticate the historical simulation outputs, fix native global connectivity or identify matter species.

## 6. Remaining scope and next task

The varying-depth first-digit-zero module has different local potentials and coupling strengths. Its low profile is not proved exactly uniform by this theorem. Numerical score1 at floating precision must remain a numerical statement there. Disorder also breaks the constant-potential invariant sector in general and requires its own analysis.

Priority100 next: derive the equitable sibling-group reduction for that fourth module, retaining16 Theta group amplitudes and16 parity-weighted rho amplitudes. Then bound its departure from a uniform Theta profile. This uses the existing source operator and requires no added links or fitted source law.

Original source files are preserved. New exact verifier and certificate support the proof; same-constructor review only. Physical promotion0, registration unchanged. Gap2_FINAL_Finite_Genesis.png was unavailable and unused.
