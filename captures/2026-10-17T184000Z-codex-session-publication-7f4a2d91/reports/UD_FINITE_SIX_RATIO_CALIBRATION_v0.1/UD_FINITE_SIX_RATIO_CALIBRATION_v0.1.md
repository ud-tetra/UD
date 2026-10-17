# UD finite six-ratio calibration v0.1

**RESULT / STATUS — DERIVED CONDITIONAL; constructor verification PASS.**
Twelve scalar readings from three specified preparations suffice to estimate
the six effective directed ratios with

\[
\|\widehat q-q\|_2<6.189\times10^{-13}
 <2^{-40}<2^{-39}.
\]

The decimal is rounded upward; the exact interval expression below is the
certificate. The result is uniform on the declared ratio and gain box and
uses a finite interval, not a derivative oracle. Four auxiliary diagnostic
ports are required beyond the original 62-channel vertex-link observer.
This is a proposed protocol with sufficient deterministic input bounds;
apparatus performance has not been measured. Development lane; no registry
entry. Physical promotion = 0. Independent review pending.

## 1. Model and what is identified

Use the frozen real 2640-coordinate chain carrier with grade sizes
(120,720,1200,600) and skew incidence channels A1,A2,A3. In logger time,
let K scale the lower-grade rows of Ak by Dk and upper-grade rows by Uk,
retaining all signs of the frozen A. Equivalently, for the grade-scalar family,

\[
 D_k=\alpha w_k/h_{k-1},\qquad U_k=\alpha w_k/h_k,\qquad
 q=(D_1,U_1,D_2,U_2,D_3,U_3).
\]

Both true ratios and six positive sensor gains are assumed to lie in
\(\Omega=[15/16,17/16]^6\). Ratios, gains and the affine logger scale
are constant across the calibration runs. Sensor outputs are the declared
coordinate times its gain, plus bounded error. Offsets, cross-talk,
off-diagonal metric terms and extra generator terms are excluded by this
candidate family unless their selected-output effects are already bounded
within the stated error receipts. The twelve readings do not verify these
model restrictions.

The effective ratios absorb the constant clock scale. No independent alpha
or h0 reference is needed for their estimation or relative metric/rate shape.
Separating alpha from native rates, or determining an absolute metric scale,
remains unidentified by this protocol. Logger units do not identify physical
seconds. All coordinates below are zero-based and all preparations use real
chain coefficients; no finite-field SVD or exponential is invoked.

## 2. Finite acquisition: three preparations, twelve readings

Let e_j be the jth chain-coordinate vector and set h=1/32 in logger units.
Use a separately prepared initial state for each run:

1. Gain run: pG=e1+e133+e486+e878+e1680+e2040. At the preparation event,
   read these six coordinates. Clip each reading to [15/16,17/16] to obtain
   its gain estimate. The gain preparation has squared norm 6.
2. Run A: pA=e1+e1680, squared norm 2. At h, read 133,486,2040.
3. Run B: pB=e133+e2040, squared norm 2. At h, read 1,878,1680.

Each dynamic output is zero in its prepared initial state. Apply the sign in
the table and divide its reading by h times the corresponding gain estimate.
The resulting vector is z, in the ratio order below.

| Ratio feature | Run | Output | Sign | Oriented simplex | In original shell |
|---|---|---:|---:|---|---|
| D1 | B | 1 | + | vertex (1) | No |
| U1 | A | 133 | − | edge (1,11) | No |
| D2 | A | 486 | − | edge (33,34) | Yes |
| U2 | B | 878 | + | face (1,11,87) | No |
| D3 | B | 1680 | − | face (33,34,41) | Yes |
| U3 | A | 2040 | + | tetrahedron (0,33,34,41) | No |

Thus four auxiliary ports are **1,133,878,2040**. All six are available in the
previous 189-coordinate diagnostic layout, but the original 62-coordinate
shell alone does not implement this calibration. The scalar count is
6+3+3=12. It excludes the work needed to certify preparation amplitudes,
addressing, timing and error bounds. In particular, pG contains six known
amplitudes, rather than one unknown amplitude inferred from the same data.
Its error is bounded at its actual readout event, covering any initial
timing uncertainty affecting those prepared coefficients.

## 3. Uniform finite-map theorem

Let L extract the six signed coordinates from the direct-sum states of runs
A and B. Define the ideal finite map

\[
\Phi(q)=h^{-1}L\big(e^{hK(q)}p_A\oplus e^{hK(q)}p_B\big).
\]

The exact incidence jet is I6. K flips grade parity and the selected outputs
have opposite parity to their preparations. Every even Taylor power vanishes
in those outputs, so Phi=q plus odd terms beginning at order 3.

The frozen incidence channels satisfy Ai Aj=0 for i≠j, with orthogonal active
spaces. The inherited spectral certificate gives ||A||<4 and hence every
channel boundary block has norm <4. On each active pair, the directed block
norm is at most 4 max(Dk,Uk). Consequently, throughout Omega,

\[
\|K(q)\|\le\omega=17/4,\qquad
\|\partial K/\partial q_i\|\le4.
\]

For n≥1, differentiating K^n gives n product terms. The combined nominal
preparation norm is 2 and ||L||=1. Summing odd terms n≥3 and then taking the
Frobenius bound over six Jacobian columns gives

\[
\|D\Phi-I\|\le8\sqrt6[\cosh(17/128)-1]
 <0.173082<1/5.
\]

Integrating along segments in the convex box yields

\[
\tfrac45\|q-q'\|_2\le\|\Phi(q)-\Phi(q')\|_2
 \le\tfrac65\|q-q'\|_2.
\]

The finite map is globally injective on this box and its normalized Jacobian
condition number is <3/2. This is a condition number for normalized features,
not for arbitrary raw voltage scales. Finite-time normalization amplifies raw
errors and is explicitly included next. Unlike the older alpha-anchored
protocol, alpha is already absorbed in q, so the bound needs no separate
alpha error term.

## 4. Candidate deterministic precision contract

Let l=15/16 and u=17/16. These are sufficient design requirements, not measured
performance or theory constants. No stochastic averaging assumption is used.

| Error source | Exact ceiling | Norm and scope |
|---|---:|---|
| Gain preparation coefficients at readout | 2^-49 | Infinity norm over six ports |
| Gain-run additive raw noise | 2^-49 | Infinity norm over six readings |
| Dynamic preparation errors | 2^-49 | Combined two-run Euclidean state norm |
| Dynamic additive raw noise | 2^-49 | Euclidean norm of all six readings |
| Dynamic interval error | 2^-55 | Absolute logger-time error for each run |
| Computation of normalized data | 2^-60 | Six-vector Euclidean error |
| Numerical update error | 2^-60 | Euclidean error per projected iteration |
| Accepted projected fixed-point defect | 2^-44 | Six-vector Euclidean norm |

A sufficient per-reading dynamic noise ceiling is 2^-51, since
sqrt(6) times 2^-51 <2^-49. Individual preparation errors must respect the
combined two-run bound; giving each the full combined ceiling would not
suffice. Gain estimation by clipping cannot increase distance to a true gain
in the assumed box. Writing xiG=nuG=xi=nu=2^-49 and j=2^-55 gives

\[
 \epsilon_g=u\xi_G+\nu_G=33/2^{53},\qquad
 E=\exp[\omega(h+j)].
\]

The combined ideal dynamic state norm is at most 2E. Gain normalization error
contributes at most 2E epsilon_g/l. Preparation error contributes at most
u E xi/l. The variation of the exponential over the two interval errors is
at most 2 omega E j before the gain factor u/l. Raw additive noise contributes
at most nu/l, which is conservatively bounded by E nu/l. Therefore

\[
\|z-\Phi(q)\|_2\le B:=
\frac{E(\nu+2\epsilon_g+u\xi+2u\omega j)}{hl}+2^{-60}.
\]

256-bit Arb arithmetic encloses B below 4.382260 times 10^-13. This includes
both readout gain and finite-time normalization. A known constant clock-scale
offset is part of q; j measures error relative to the specified logger
interval. Arbitrary time variation of that scale is outside this model.

## 5. Finite inverse, including noisy data outside the image

Starting at q0=(1,...,1), perform **20 iterations**:

\[
 q_{n+1}=\Pi_\Omega[q_n+z-\Phi(q_n)].
\]

Projection is nonexpansive, and the map inside projection has derivative
I−D Phi of norm <1/5. The iteration is thus a contraction even if noisy z
is outside Phi(Omega). Its fixed point exists uniquely. If the computed
estimate has projected defect r, comparison with the true q gives

\[
\boxed{\|\widehat q-q\|_2\le\tfrac54(B+r).}
\]

For numerical updates with error at most epsilon_step=2^-60, the box diameter
D=sqrt(6)/8 gives the finite defect bound

\[
 r\le\tfrac65[(1/5)^{20}D+\tfrac54\epsilon_{step}]
 <3.855\times10^{-15}<2^{-44}.
\]

The implementation evaluates the exponential map by an **exact rational
degree-32 Taylor polynomial**. Exact incidence channel powers construct the
integer coefficients; all odd terms through degree 31 are retained. The
uniform vector remainder is at most

\[
 T=\frac{2e^{17/128}(17/128)^{33}}{33!h}
 <2^{-170}.
\]

Rounding each updated coordinate to the nearest 2^-64 costs at most
sqrt(6) times 2^-65. T plus this rounding error is <2^-60, so the specified
finite implementation meets the update contract. Exact rational division
followed by the same rounding also meets the normalized-data computation
contract. h and the box endpoints are exactly dyadic.

With the conservative accepted r=2^-44, the interval-certified final bound is

\[
 \tfrac54(B+2^{-44})
 \in (6.18836,6.18837)\times10^{-13}
 <1/2^{40}<1/2^{39}.
\]

In particular every individual ratio meets the requested absolute 2^-39
accuracy gate. The stopping rule uses the **projected fixed-point defect**,
rather than requiring an arbitrarily small raw forward residual. An explicit
boundary example in the replay adds −2^-43 to all six normalized features at
q=(l,...,l). Projection retains the boundary point with zero exact defect,
while the raw forward residual exceeds 2^-44. This distinction prevents an
unnecessary failure on valid noisy data.

## 6. Connection to the fitted-generator shape certificate

The new protocol supplies the previously missing bounded-estimate hypothesis
of `PARENT_SHAPE_GATE.json`, conditional on the family and precision receipts.
It does not supply measured estimates. Retaining the parent's declared
delta=2^-39 cap, define

\[
 \widehat q_0^{\rm frame}=1,\qquad
 (\widehat q_k^{\rm frame})^2=\prod_{j\le k}\widehat D_j/\widehat U_j,
 \quad \widehat s_k=\sqrt{\widehat D_k\widehat U_k},\quad
 \widehat c=(\widehat s_1\widehat s_2\widehat s_3)^{1/3}.
\]

If actual estimates also pass
|shat_k/chat−1|≤2^-38 and the separate common-scale gate 1±1/1024, the parent
propagation bounds imply metric and native-rate shape errors <2^-35. The
protocol alone does not force data to pass those acceptance gates. A measured
shape-gate evaluation must include its own interval arithmetic.

The bound on an additional skew J, full-domain acquisition readout error,
preparation receipts for the 37 history runs, acquisition timing, and stability
throughout the acquisition batch remain separate requirements. Calibrating six
diagonal gains does not certify all 62 or 189 sensor channels. The original
747-dimensional nominal kernel and 1893 historical signal rank are not altered
by this calibration theorem.

## 7. Verification and provenance

Constructor replay verifies identical frozen shell/calibration generators;
14880 sparse entries; all cross-channel directed products; orthogonal channel
identities; the exact I6 jet; parity; polynomial equality against full-carrier
rational powers at four parameter points; four synthetic inverse cases,
including imperfect gain readings and nonzero raw noise; and the noisy
out-of-image boundary case. Uniform interval comparisons establish the global
theorem; point tests alone would not establish it. An isolated fresh-directory
replay checks source hashes and identical certificate fields.

The coefficient ledger O03 treats every precision here as protocol control.
Q139's physical-clock gap remains open; Q165/Q169 supply the scoped real
support/generator framework. The CRL2 attachment is a governance proposal,
not silently adopted. No attachment is modified or republished. No independent
review or apparatus run is claimed. Local capture is separate from public
publication; no push, PR or merge is performed.

Recommended next gate: specify held-out checks for the assumed readout and
generator family at an error level compatible with this six-ratio budget,
and prove the detectable alternatives and blind directions before execution.
