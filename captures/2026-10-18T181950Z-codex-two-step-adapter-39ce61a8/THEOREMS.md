# Two-step source-precision adapter and actual-output certificate

Development — no registry entry. Physical promotion 0; independent review pending.
All results concern two known synthetic PR195 records and their pinned learned
modal source. They do not establish physical-frequency truth.

## 1. A different audit rule, preserving prior outcomes

The original instrument-noise diagnostic retains its common/scaled cutoff
counts205/204 on the wider stress sketch and its original proposer HOLD.
This return defines a separate encoding-precision audit with frozen cutoff
tau=2^-24. It does not change that older noise contract.

The record-only adapter uses the same nested321-column sketch as PR196, but
learns its order by its own SVD count above tau. It receives no source phases,
rates, jitter or coefficients. Source hashes are checked for lineage only.
Expected source orders105 and209 are used by the verifier as applicability
conditions, never forced onto a different learned order.

## 2. Source-aware order and excitation

Let X be the encoded time-by-coordinate record, quantum2^-48, and S=A/128 the
dyadic sketch. Its mathematical value is Z=X_integer A/2^55. Integer products
are guarded against overflow before execution, then FLINT forms exact G=Z^T Z
at scale2^-110. All18,790,154 readings per record are projected and raw hashes
checked before/after. Exact Grams and untrusted sorted dyadic eigenproposals
are retained. STRUCTURAL_AUDIT.json checks symmetry, shapes and descending
eigenproposal order for the actual hash-bound witnesses.

As in PR196, exact orthogonality/eigenpair residuals and a polar/Weyl bound
enclose each ordered eigenvalue of G. Let l_q be the qth lower enclosure.
The declared source comparison has rank at most q, where q=105 for zero
clocks and q=209 for the two-rate stress model.

PR195's generator error is independently re-evaluated from the pinned
coefficient numerators:

\[
 d_{\rm eval}=L\,2^{-120}+2^{-49},\qquad
 L=\max_c\sum_{r>0}|B_{{\rm integer},rc}|.
\]

Hence

\[
 \|Z-Z_{\rm model}\|_2
 \le\sqrt{8191\cdot2294}\,d_{\rm eval}\|S\|_F
 =:\epsilon<1.034\,10^{-10}.
\]

If l_q>tau^2 and epsilon<tau, then exactly q singular values of encoded Z
exceed tau: the qth is bounded below by sqrt(l_q), and Weyl bounds the
(q+1)th above by epsilon. This is NOT a statement that encoded algebraic
rank equals q; rounding may add smaller directions.

The actual lower bounds are sigma105>0.3585086 for the baseline and
sigma209>0.0028804 for stress. Both exceed tau, while the next value is below
epsilon. The floating counts105/209 agree with these source-aware exact
encoded-sketch certificates. The source comparison itself therefore has
exact rank105/209, because its qth singular value is still positive after
subtracting epsilon.

The exact-sketch count is not silently a certificate of every intermediate
floating BLAS entry. The output proof below uses saved actual arrays directly
and does not assume SVD or BLAS accuracy to transport phases.

## 3. Two-step closure and aliasing

For stress, s=+1 or-1 labels the preparation rate class and

\[
 g_{js}(k)=e^{i(1+s\mu)\theta_j k}
          e^{is\theta_jj_0(-1)^k},\quad
 \mu=2^{-20},\ j_0=1/16.
\]

Preparation origins rotate coefficients without adding temporal functions.
Since parity is unchanged by two steps,

\[
 g_{js}(k+2)=e^{2i(1+s\mu)\theta_j}g_{js}(k).
\]

The real comparison frame P has columns1,cos,sin for each j and rate class.
It obeys P[2:]=P[:-2]J, where J is block diagonal with stationary block1 and
orthogonal blocks

\[
 J_{js}=\begin{pmatrix}\cos(2\omega_{js})&\sin(2\omega_{js})\\
 -\sin(2\omega_{js})&\cos(2\omega_{js})\end{pmatrix},
 \quad\omega_{js}=(1+s\mu)\theta_j.
\]

Thus J is normal. Its complete target list is1 and exp(plus/minus2i*omega_js).
Every pairwise unit-circle chord is recomputed with validated arithmetic;
the minimum is bounded below by7.285423493e-7 for stress. This checks folded
cross-pair collisions as well as same-pair rate-class splitting.

Two-step eigenvalues identify omega only modulo pi. Primary results are
circular two-step phase errors. Dividing by2 is only a conditional lift about
the named source target; each target's lift integer is retained. No
unrestricted continuous generator or SI frequency is identified.

## 4. Actual floating adapter and saved arrays

For the learned order q, the actual adapter forms
T=lstsq(U[:-2],U[2:]), calls the floating eigensolver, captures its arguments,
and rounds all signed phase arguments onto the2^-60 grid. The original and
instrumented variants share all proposal arithmetic; instrumentation runs
only after proposal emission. Their proposal bytes match on both records.

Saved witnesses include the actual U,T,eigenvalues,eigenvectors,inverse,
angle outputs and emitted phase integers. The large U is split into two row
archives without changing bytes. A verifier-only untrusted reduction
D=U^T P_tilde and inverse witness K are proposed after the record-only fit.
The source frame is generated with the validated96-bit recurrence from PR195;
each nonstationary component is within2^-60 of its exact value.

The basis orthogonality, two-step shift residual and source-frame span
residual are checked and retained. The direct similarity proof does not
require a guessed deleted-row or reference conditioning bound.

## 5. Direct similarity certificate

Let T be the actual shift matrix, D an arbitrary square reduction witness,
and K an inverse witness. Verify exact binary64 encodings and bounds

\[
 \rho_D\ge\|DK-I\|_2<1,\quad
 h_D=\|K\|_{2,\rm upper}/(1-\rho_D),\quad
 d\ge\|D\|_2,\quad L_J\ge\|TD-DJ\|_2.
\]

All residual products use exact integers. J is evaluated as a validated
dyadic block rotation; its component errors below2^-60 contribute an operator
error at most2^-59, so d*2^-59 is charged to L_J.

For the actual returned diagonal Lambda and an eigenvector/inverse witness
V,H, verify

\[
 \rho_V\ge\|VH-I\|_2<1,\qquad
 \delta_\lambda=
 \|TV-V\Lambda\|_{2,\rm upper}
 \frac{\|H\|_{2,\rm upper}}{1-\rho_V}.
\]

Then A=V Lambda V^-1 has exactly the returned eigenvalues and
||A-T||<=delta_lambda. Both V and D are certified invertible by their
Neumann residual bounds. Consequently

\[
 \|D^{-1}AD-J\|_2
 \le h_D\bigl(L_J+d\,\delta_\lambda\bigr)=:R.
\]

Because J is normal, every eigenvalue lies in a radius-R disk about its
unit-circle spectrum. Along the homotopy from J to D^-1 A D, all spectra
stay inside these disks. If2R<s_min, disjoint disks retain one eigenvalue
each, counting multiplicity. The checker also explicitly verifies a unique
assignment of every actual eigenvalue to every labeled target.

Exact real residuals use PSD Gram trace/absolute-row-sum upper bounds.
For complex matrices, the Hermitian Gram's absolute row sums are bounded
using |Re|+|Im|; the minimum with its trace remains an operator-norm upper
bound. Frobenius bounds are used where stated. Square roots and target
exponentials use512-bit interval arithmetic; reported dyadic bounds round
outward. No floating SVD/eigenvalue/inverse accuracy is assumed.

## 6. Actual angle emission

For every captured angle bit pattern, the checker recomputes exact
ties-to-even2^-60 rounding using integer ratios. It then bounds the circular
difference between the validated complex argument of the actual returned
eigenvalue and the emitted phase. Let this maximum be epsilon_arg.
For R<1, the circular emitted-phase error is at most

\[
 \arcsin R+\epsilon_{\rm arg}.
\]

Both2R<s_min and the conservative2*phase_error<s_min gates must pass.
The baseline error is<1.373e-13 and stress error<8.961e-10 radians per two-step
sample. Stress's209-way matching is certified only under this source-precision
audit; prior noise-cutoff outcomes are unchanged.

Two frozen corruption controls on isolated copies refuse a zero source inverse
and a changed emitted phase integer. Original witnesses remain unchanged.
All source-order and actual-output proofs replay from saved arrays.

## 7. Scope

These are finite synthetic constructor fixtures. The source phases, rate and
jitter are declared model parameters used by the verifier, not physical
measurements or independently identified laws. No claim of blinded execution,
general optimizer convergence, uniform whole-noise-ball recovery, independent
review, original-contract admission, full-Hankel certification, native physical
observer/metric selection or SI calibration follows. The nominal747-dimensional
dynamical observer kernel is unchanged. O03 cutoffs remain protocol controls.
