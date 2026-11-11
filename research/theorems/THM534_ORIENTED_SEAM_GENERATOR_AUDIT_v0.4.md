# THM-534 oriented-seam generator audit v0.4 — flat-gauge no-go and curvature candidate

**Date:** 2026-10-21 · **Status:** EXACT/NO-GO + EXACT CONDITIONAL + CANDIDATE source law · **Lane:** Development / no registry promotion · **Physical promotion:** 0.  
**Parent:** [v0.3 incidence programme](THM534_FORWARD_INCIDENCE_EVENT_PROGRAMME_v0.3.md); [v0.2 S4 classification](THM534_MICRO_SOURCE_RECOVERY_AND_NO_GO_v0.2.md); [PR #346](https://github.com/ud-tetra/UD/pull/346); [issue #347](https://github.com/ud-tetra/UD/issues/347).  
**Source inputs:** filled oriented tetrahedron's chain complexes and unit-metric Hodge–Dirac construction; `THM-561_Weak_Color_Mass_Split_v1.0.md` §1.4 as **citation only** for historical THM-534 probabilities; `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39` typed metric/holonomy governance. The supplied `seam_phase_transport.md` is a reconstruction placeholder, **not** an independently derived phase rule.

## Types, carrier and execution semantics

Let `K=Δ³` be the complete **filled** simplex with ordered vertices 0,1,2,3 and usual oriented real cochain/chain bases. `C₀=R⁴`, `C₁=R⁶`, `C₂=R⁴`, `C₃=R`; unit simplex basis inner products, complexified where needed. Let signed boundary matrices `B₁:C₁→C₀`, `B₂:C₂→C₁`, `B₃:C₃→C₂` satisfy `B₁B₂=B₂B₃=0`. These are *not* the nonnegative edge Markov readout `T:R⁶→R⁶`. No physical time, Born readout, probability normalization or Standard Model correspondence is presumed.

Define on `H=C₀⊕C₁⊕C₂⊕C₃` the **skew-adjoint** generator
```text
                [ 0     B1       0     0 ]
A =             [ -B1*  0        B2    0 ]
                [ 0    -B2*      0     B3]
                [ 0     0       -B3*   0 ]
```
where * denotes conjugate transpose and `P₁` orthogonal projection onto `C₁`. The group `e^{sA}` is norm-preserving for dimensionless evolution parameter s; it is a mathematical evolution, not a native physical clock.

## THM-534-S1 — Flat seam-gauge no-mixing theorem [EXACT / NO-GO]
**Claim.** On this carrier with unit metric,
```text
B1* B1 + B2 B2* = 4 I6,
P1 e^(s A) P1 = cos(2s) I6        (all real s).
```
For arbitrary degreewise diagonal unitary `G_k:C_k→C_k`, set `B'_k=G_{k−1} B_k G_k*` and `A'=G A G*` with `G=⊕_k G_k`. Then
```text
B'_{k−1}B'_k=0;
P1 e^(s A')P1=cos(2s)I6.
```
**Proof.** The simplex's signed incidence gives the unit edge Hodge Laplacian `L₁=4I₆` (v0.3 N7). Moreover the off-degree terms in `A²` vanish by the chain law `B₁B₂=B₂B₃=0`. Thus `(A^{2m})|_{C₁}=(-4)^mI` and odd powers have zero edge block. The exponential series yields the cosine. Degreewise unitary conjugation preserves both nilpotency and edge block, because `G₁ I G₁*=I`. QED.

**NO-GO scope:** flat local seam gauge phases cannot produce distinct-edge *amplitude* transfer in this exact unit-incidence model. At `cos(2s)=0` an edge-only conditional probability is undefined (zero edge-sector norm). It does not exclude changing the metric, selecting a new nonflat connection, adding degrees, nonlinear/open-system evolution or recording non-edge channels.

## THM-534-S2 — Unequal lower/upper sector-weight theorem [EXACT CONDITIONAL]
Define `X=B₁*B₁`, `Y=B₂B₂*`. These obey `XY=YX=0`, `X²=4X`, `Y²=4Y`, `X+Y=4I₆`, `rank(X)=rank(Y)=3`. Thus `P_X=X/4`, `P_Y=Y/4` are orthogonal complementary rank-three projectors.

If **independently assigned** positive weights `a,b` multiply lower and upper incidence contributions, then
```text
K(a,b)=a X + b Y = 4a P_X + 4b P_Y,
spec(K(a,b)) = {4a (×3),4b (×3)}.
```
For a skew generator with `B₁→√a B₁`, `B₂→√b B₂` (and compatible unchanged degree-3 chain), the exact edge block is
```text
P1 e^(s A(a,b)) P1 =
   cos(2√a s) P_X + cos(2√b s) P_Y.
```
Unless the two cosine factors agree, cross-edge amplitudes can arise. **No relative weight selection rule is derived here**. Choosing `a/b` to recreate THM-534 is disallowed inverse fitting. `a=b=1` returns S1.

## THM-534-S3 — One-incidence U(1) curvature-spectrum identity [EXACT CONDITIONAL]
Select one oriented face f and one of its three incident edges e. Let its signed incidence coefficient be `q=(B₂)_{ef}=±1`, and choose `z∈U(1)`. Define the *covariant candidate incidence*
```text
N_z = B2 + (z−1)q |e><f|.
```
Keep the original topological boundary B₂ unchanged in the chain complex. `N_z` is a **separate candidate connection operator**, not a replacement simplicial boundary.

Then
```text
F_z = B1 N_z = (z−1)q (B1 |e>)<f|,
||F_z||_F² = 2 |z−1|²;
K_z = B1* B1 + N_z N_z*;
spec(K_z) = {4±√2|z−1|,4 (×4)}
          = {4±2√2 |sin(φ/2)|,4 (×4)} if z=e^(iφ).
```
**Proof.** `B₁B₂=0` proves the curvature composition. The incidence vector `B₁|e>` has squared norm 2. Relative to `4I`, `K_z` has two nonzero off-diagonal couplings between the modified edge and the other two edges in f, each of modulus `|z−1|`; its Hermitian rank-two perturbation has eigenvalues `±√2|z−1|`. QED.

**Chain obstruction.** `F_z=0` iff `z=1`. Also `N_z B₃≠0` for `z≠1`. Thus a *single-entry twist* cannot preserve the original chain differential identities unless trivial. It must be admitted, if ever, as separate nonflat/covariant transport with its own curvature and receipt law.

## THM-534-S4 — Localized Z2 seam produces cross-edge amplitudes [EXACT CONDITIONAL / NUMERICAL]
Fix the smallest nontrivial phase `z=−1` as a **declared exploratory choice**, not source-selected physical phase. Then
```text
rank(F_z)=1;  ||F_z||_F²=8;
spec(K_z)={4+2√2, 4−2√2, 4,4,4,4}.
```
Let `A_z` be the skew-adjoint 15×15 block generator with `B₂` replaced by `N_z` in off-diagonal transport blocks, while retaining the original topological `B₂` separately. It obeys `A_z*=-A_z`, hence conserves the total chain-state norm. For distinct edges e and e' with `(K_z)_{e'e}≠0`,
```text
(P1 e^(s A_z)P1)_{e'e} = -s² (K_z)_{e'e}/2 + O(s⁴).
```
Thus cross-edge amplitude is genuinely nonzero for sufficiently small nonzero s. For the declared sign-flip and orientation, a direct double-precision full exponential gave maximum edge off-diagonal amplitude 0.0048840129 at s=0.07 and 0.0352389967 at s=0.19, while `||e^(sA_z)*e^(sA_z)-I||_max < 10^(-12)`. All 12 possible face-edge incidence locations have the same exact spectrum.

**Limits:** single defects break a specific realization's tetrahedral symmetry; the orbit of 12 positions is symmetric but does not supply a physical ensemble. Amplitude readout is not a stochastic kernel; no Born mapping, conditional edge probability, physical generator, physical phase selection, event schedule, or historical THM-534 hop probabilities follows. Note `N_zB₃≠0`: the naive formula `cos(s√K_z)` is **not** an exact edge block of the *full* 15D evolution here, since other odd-degree sectors couple through the covariant curvature. Only the displayed short-s expansion is claimed.

## Decision ledger
- **AUTO_LOCK scoped:** S1–S3 exact algebra, S4 exact leading transfer and unitary-norm conservation.
- **NUMERICAL:** two nonzero-time amplitude witnesses on the single exploratory Z2 seam.
- **AUTO_FREEZE:** interpreting the nonflat seam as a lawful replacement for `B₂` in an ordinary nilpotent chain complex; claiming THM-534 recovered; asserting an amplitude-to-probability rule; identifying s as physical time; treating flat phase gauge changes as dynamics; importing physical gauge/boson meanings.
- **OPEN_GATED:** original THM-534 microscopic transport source, phase/defect source law, coupling coefficients and carrier metric selection, admissibility/curvature Bianchi analogue, packet receipt and renewal rules, edge outcome readout, and a fresh held-out test.

**Exposure:** historical THM-534 matrix was visible prior to selecting this model. New results are explicitly *exploratory*, not prospectively target-blind or independently reviewed.

## Reproduction
`verify_thm534_oriented_seam_v0_4.py` checks signed boundaries, both Hodge projectors and symbolic weighted spectra, a nontrivial flat U(1) gauge conjugacy, U(1) phase tests z∈{1,−1,i,−i}, the 12 defects, and two full 15D real skew-exponential tests. Constructor execution PASS 2026-10-21. Requires SymPy, NumPy and SciPy. Review CRL-2a/development only; no physical promotion.
