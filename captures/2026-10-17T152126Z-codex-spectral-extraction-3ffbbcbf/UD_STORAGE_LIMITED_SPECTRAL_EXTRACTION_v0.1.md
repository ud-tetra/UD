# UD spectral extraction without the dense Hankel matrix v0.1

RESULT / STATUS: **DERIVED method, constructor verified**. Exact arithmetic and direct spectral enclosures replace dense Hankel storage. Thirteen checks and three frozen-dimension constructed spectral controls are supplied. No nominal600-cell full-history run or apparatus dataset was supplied or certified. Independent review pending; physical promotion **0**. Development — no registry entry.

## Disposition of the parallel appendix

The appendix reproduces the acquisition arithmetic correctly, with its original conditions. Its additional leakage-sieve interpretation is not supported by the frozen source chain.

| Submitted claim | Review result |
|---|---|
| M4096;8191 timestamps;37 preparations;18790154 readings | Retain |
| delta2^-20 per62-vector; scalar2^-23 sufficient | Retain as bounded-error contracts |
| 1893 retained signals; condition<2029 | Retain conditionally; requires numeric and acquisition evidence |
| 62 auxiliary diagnostic ports | Correct:62 original history channels;189 diagnostic outputs; four extra six-ratio ports |
| One port per frequency block | Reject: a coordinate readout generally mixes frequencies |
| Every port residual<2^-49 | Not implied by the frozen budget; would require a new experiment contract |
| Borel-shear norm<=2^-38 | Undefined new proposal;2^-38 belongs to a particular source shape statistic |
| 1146-dimensional invariant plane | No such certificate in this chain |
| Finite-field leakage, real norms and physical currents share one provenance | No transfer supplied |
| Monitoring detects phases confined to the747 hidden directions | No-go for the nominal invariant hidden sector |
| ACTIVE_MONITOR and causal diagnosis of failure | Unsupported; no hardware run or causal isolation supplied |

Two exact counterexamples make the distinction concrete. Port0 is coordinate33. The source operator has A[33,120]=−1, so the initial state e120 gives y0(0)=0 and y0'(0)=−1. That port is not stationary-only. A scalar instrument error2^-24 is allowed by the frozen allocation and exceeds the proposed2^-49 residual gate by2^25; the strict gate cannot be inferred from the existing contract.

Let N=intersection over k>=0 of ker(RA^k), the nominal747-dimensional dynamical unobservable space. A preservesN, and skewness makes N-perpendicular invariant too. If J is any skew operator supported entirely insideN, then

\[
R e^{t(A+J)}x=R e^{tA}x\quad\text{for every }x,t.
\]

There are747×746/2=278631 such skew degrees of freedom. No history processing of this observer can diagnose them without a separately specified coupling that makes them observable. The dimension747 is tied to the frozenA,R; it is not a universal claim about every altered plant. The replacement `CORRECTED_MONITORING_APPENDIX.md` preserves the valid finite-observer scope. The full claim audit is `PARALLEL_APPENDIX_REVIEW.json`.

## Exact Hankel action and total energy

Write the encoded numeric history as Y[a,k,c]/q with p=37 preparations, c=62 channels, M=4096 and q=2^48. The exact data matrix is

Here q is only the encoding denominator, not the parent common-rate multiplier. The candidate V below is an input-history basis, distinct from the parent's105-column temporal frame.

\[
H[(i,c),(j,a)]=Y[a,i+j,c]/(Mq).
\]

For an integer candidate vector v, define P_ac(z)=sum_k Y[a,k,c]z^k and W_a(z)=sum_j v[j,a]z^(M−1−j). Then

\[
(Mq)(Hv)[i,c]=\sum_a[z^{i+M-1}]P_{ac}(z)W_a(z).
\]

The transpose action exchanges the preparation/channel summation. Python-FLINT integer polynomial multiplication computes both exactly; there is no floating FFT error in the verifier. The separate numerical proposer uses FFTs only to suggest a basis. It has no authority to certify rank or convergence.

The exact squared Frobenius norm is one pass over the time record:

\[
E=\|H\|_F^2=\frac1{M^2q^2}\sum_{k=0}^{2M-2}m_k\sum_{a,c}Y[a,k,c]^2,
\quad m_k=\min(k+1,M,2M-1-k).
\]

The multiplicities are essential. Counting each raw value once, ignoring duplicated Hankel antidiagonals, would understate the energy and invalidate completeness checks.

## Projection-tail certificate

Let V be any proposed real right signal basis with r=1893 columns. It need not be exactly orthonormal. The proof recomputes

\[
G_V=V^TV,\qquad C=HV,\qquad G_C=C^TC
\]

from the numeric input and candidate, using integer numerators and common denominators. Suppose the exact calculation gives an outward bound

\[
\|G_V-I\|_2\le\|G_V-I\|_F\le\eta<1.
\]

The exact orthogonal projection onto the candidate space is P=V G_V^-1 V^T. Its full discarded energy obeys

\[
\begin{aligned}
\|H(I-P)\|_F^2
&=E-\operatorname{tr}(G_V^{-1}G_C)\\
&\le E-\frac{\operatorname{tr}G_C}{1+\eta}
=:\rho^2.
\end{aligned}
\]

The trace inequality follows from G_V^-1 >= I/(1+eta) and G_C positive semidefinite. The code never clamps a negative inconsistent energy to zero; inconsistent cores are rejected. A candidate with eta>=1 returnsHOLD.

This section's rho is the projection-tail bound. It is distinct from the readout-operator error tolerance denoted rho in the parent acquisition model.

For each ordered eigenvalue of G_C, suppose an exact/validated bound is ell_i <= lambda_i(G_C) <= u_i. Define

\[
L_i=\max(0,\ell_i)/(1+\eta),\qquad
U_i=u_i/(1-\eta)+\rho^2.
\]

Then direct enclosures of the exact data spectrum are

\[
\boxed{\sqrt{L_i}\le\sigma_i(H)\le\sqrt{U_i}\ (i\le r),
\qquad \sigma_{r+1}(H)\le\rho.}
\]

Proof: the nonzero spectrum of HP equals that of C G_V^-1/2. Singular-product inequalities give its ordered squared bounds ell_i/(1+eta),u_i/(1−eta). Also

\[
HH^T=(HP)(HP)^T+H(I-P)(H(I-P))^T.
\]

The second summand is positive semidefinite with norm at most rho². Min-max therefore gives the displayed lower/upper bounds, and the rank-r approximation HP bounds the entire remaining tail. This is a completeness certificate, not only a residual check for a few computed singular triplets.

The frozen target is certified when

\[
L_r>T^2,\qquad \rho^2<T^2,\qquad U_1<2029^2L_r,
\quad T=2B
\]

using the exact unchanged threshold from the parent contract. The output includes enclosures for all1893 retained singular values. A failure isHOLD: a poor candidate or a conservative bound can fail even when the underlying record has a valid signature. The code never lowers the target or moves the threshold to force acceptance.

These are direct enclosures for the exact encodedH. No approximate matrix Htilde is substituted, so the matrix-perturbation error entry is0. Scalar interval rounding is already included in the outward endpoints. This uses the frozen contract's explicit alternative of directly verified singular-value enclosures; it does not spend or silently enlarge its B/4096 allowance for an approximate-matrix solver.

## Verified small-core eigenvalue bounds

The inexpensive first bound uses d_i, the sorted diagonal entries of G_C, and nu=max_i sum_(j!=i)|G_C[i,j]|. Symmetry implies ||G_C−diag(G_C)||_2<=nu, hence each eigenvalue lies in [d_i−nu,d_i+nu].

A correct candidate span can have a core that is not diagonally dominant. The verifier then proposes a small-core numerical eigensystem Q,D and recomputes its orthogonality defect and eigen-residual **exactly**. Let eta_Q bound ||Q^TQ−I||_2, R_Q=G_C Q−QD, and S=(Q^TQ)^1/2. With U=Q S^-1 orthogonal,

\[
\begin{aligned}
\|G_C-U D U^T\|_2\le{}&\|G_C\|_2\eta_Q
+\|R_Q\|_F\sqrt{1+\eta_Q}\\
&+\|D\|_2\frac{\eta_Q}{1+\sqrt{1-\eta_Q}}
(1+\sqrt{1+\eta_Q}).
\end{aligned}
\]

To check the formula, first use G_C−QDQ^T=G_C(I−QQ^T)+R_QQ^T, then bound QDQ^T−UDU^T with ||Q−U||<=eta_Q/(1+sqrt(1−eta_Q)). The resulting outward dyadic radius certifies every ordered eigenvalue against the sorted entries ofD. The original floating eigenvalues/vectors are proposals only. The verifier refuses an inadequately orthogonal proposal rather than trusting its convergence flag.

## What is extracted

For any input-history vector x, the candidate coordinates are z=G_V^-1 V^Tx and its projected representative is Vz. The left image is Cz. The coordinate system is stable because the candidate singular values lie in [sqrt(1−eta),sqrt(1+eta)]. It is a basis for the retained history signal space, not a reconstruction of the2640-dimensional chain state.

If W contains the true leading-r right singular vectors, then

\[
\|(I-P)W\|_2
\le\frac{\|H(I-P)\|_2}{\sigma_r(H)}
\le\frac\rho{\sqrt{L_r}}.
\]

Indeed W=H^TU_r Sigma_r^-1. This gives a certified right-subspace leakage/angle bound for the numeric matrix. It does not identify microscopic hidden phases or label C10 sectors. Temporal eigenfrequencies and physical mode coordinates require their own operator mappings.

## Implementation and storage

The method also has a quantitative sufficient precision contract for the native family, recorded in `NATIVE_PRECISION_CONTRACT.json`. Let H0 be the matched nominal matrix for the run, with the parent singular bounds s0,S0 and the parent's Frobenius perturbation bound ||H−H0||_F<=B. The script reproduces that Frobenius bound directly from the weighted response-error formula. Suppose:

- candidate Gram defect eta<=2^-40;
- missed nominal mass ||H0(I−P)||_F<=zeta=B/4096;
- the total slack of the verified core eigenvalue bounds is at most xi=2^-41; a validated eigen-radius at most2^-42 suffices.

These are **new sufficient computational targets**, not experimental receipts. In particular, zeta and the parent's approximate-matrix solver allowance happen to use the same fraction B/4096; one does not prove the other. Their objects and proof obligations remain distinct.

Set Emax=(sqrt(r)S0+B)^2. The exact projector residual is at most(B+zeta)^2. The conservative trace replacement adds at most2eta Emax/(1−eta), so the verifier's rho² is bounded by their sum. Its smallest retained squared bound is at least

\[
\frac{(1-\eta)(s_0-B-\zeta)^2-\xi}{1+\eta},
\]

and its largest bound is at most

\[
\frac{(1+\eta)(S_0+B)^2+\xi}{1-\eta}+\rho^2.
\]

Outward interval evaluation verifies a retained condition bound below**2028.403** and a tail bound below**0.689T**, preserving the frozen2029 andT gates. This proves that finite positive candidate/core tolerances suffice for the native family. It does not assert that a generated candidate or an actual run meets those tolerances; that remains a data-dependent verification requirement.

`propose_basis.py` uses an FFT operator and fixed-seed block power proposals, storing the basis on disk. Its output is an **untrusted numerical proposal**. `run_certificate.py` binds the exact frozen protocol hash, recomputes exact cores from the encoded data and candidate, and produces `SPECTRAL_PROOF.json`. On success it also writes `FROZEN_SIGNATURE_ENCLOSURES.json` in the prior receipt auditor's interval layout. Input hashes are checked before and after verification. Evidence and physical provenance are still separate.

The dense candidate is int64 at denominator2^60. Exact H actions are stored as signed128-bit integer numerators with a common denominator, in column order. The frozen amplitude and candidate bounds imply a numerator magnitude below2^127; overflow raises an error, with no clipping. Gram products use arbitrary-precision FLINT integers and row blocks. Linux mapped pages are released between blocks; no denseH is allocated.

| Object | Storage |
|---|---:|
| Avoided denseH in binary64 | 307895468032 bytes =286.75GiB |
| Encoded history record | 150321232 bytes |
| Dense candidate,151552×1893 int64 | 2295103488 bytes |
| Exact C,253952×1893 signed128 | 7691698176 bytes |
| Each core | 1893×1893 arbitrary-precision integers |

Provision disk space for the candidate,exactC,small cores and proposer scratch, rather than287GiB forH. Exact Gram accumulation can be expensive. A full dense1893-vector nominal/measured verification has not been benchmarked; this version certifies correctness and storage structure, not an experimental processing deadline.

## Verification evidence

Thirteen tests compare exact actions, transpose duality, duplicated energy and streamed cores with independently constructed **tiny** dense matrices. They also cover missing candidate modes, orthogonality defects, inconsistent energy, noninteger input rejection, a non-diagonal core, floating proposals followed by exact verification, and individual spectral intervals.

The full frozen dimensions are tested separately with constructed records:

| Constructed record | Algebraic rank | Signals aboveT | Certificate |
|---|---:|---:|---|
| Clean impulse control |1893|1893|Certified numeric signature |
| Additional weak rank-one component |1894|1893|Certified numeric signature |
| Additional strong rank-one component |1894|1894|HOLD |

The impulse control has36 preparation/channel blocks of rank51 and one of rank57:36×51+57=1893. Its nonzero singular value is2^-12. The extra constant channel has amplitude2^-19 or2^-14. Its additional singular value follows from an independent2×2 eigenvalue formula, which verifies the expected threshold counts. These records deliberately are not600-cell trajectories: they demonstrate the certifier and also demonstrate that the spectral signature alone does not identify the UD generator.

A dense separable record additionally exercises all37×62 preparation/channel polynomial products at M4096. Both exact action and exact transpose are checked against closed-form integer sums. No dense Hankel matrix is formed. `CONTROL_PERFORMANCE.json` records the observed runtime and RSS for these constructed controls only; those figures must not be extrapolated to a dense1893-vector certificate.

Fresh-directory replay reproduces the mathematical control and appendix-review artifacts. Runtime/RSS logs are kept separate because they are operational observations, not exact mathematics. The inherited modal/diagnostic proofs are not independently rerun, and no new experiment or physical correspondence is certified.

## Use and remaining work

```sh
python review_parallel.py
OPENBLAS_NUM_THREADS=1 python -m unittest -v test_spectral.py
python full_size_controls.py
python native_precision_contract.py
python validate_spectral.py
python propose_basis.py normalized_history.i64le candidate.npy
python run_certificate.py normalized_history.i64le candidate.npy NEW_PROOF_DIRECTORY
```

The last two commands require an actual complete encoded history record. None was supplied, so they were not executed at full dense1893-vector scale. Their end-to-end path is tested on a small independent record, and their full-size exact action kernels are tested as above. Basis proposal can fail or yieldHOLD; it is not guaranteed to converge for every admitted record. A valid proof, rather than a favorable numerical rank printout, controls the result.

Next recommended step — priority **98/100**: benchmark the complete candidate/core pipeline on a frozen nominal trajectory or independently supplied record, then obtain non-constructor review. Preserve the frozen threshold,all raw records and rejected/inconclusive results. Physical promotion remains0; the nominal747-dimensional hidden subspace remains unreconstructed.
