# Direct returned-basis witness and scalar quality budget: design review

Same-team mathematical design PASS with the conditions below. No new numerical constants/case outcomes were evaluated in this review. Development — no registry entry; physical promotion0; external review remains PENDING.

## 1. Arbitrary alignment witness suffices

Let U0 and U1 have q209 columns, with validated full rank. Let P0 project onto span(U0), G1=U1^T U1, Q1=U1*G1^-1/2 and Q0 an orthonormal frame for span(U0). Propose ANY finite dyadic X and certify the exact Frobenius residual R=U1-U0X. No inverse or least-squares property of X is required. Since(I-P0)U0=0,

(I-P0)Q1=(I-P0)R*G1^-1/2.

For eta1>=||G1-I||2, eta1<1, a residual upper rF gives

||sinTheta||F <= sF=rF/sqrt(1-eta1).

A separate residual operator upper r2 gives s2=r2/sqrt(1-eta1); without one, s2=sF is safe. Require s2<1. The common principal-angle Procrustes alignment satisfies

dF<=c(s2)*sF, d2<=c(s2)*s2,
c(v)=sqrt(2/[1+sqrt(1-v^2)]).

There is no full321-column polar triangle here: Q1 is defined directly from the actual retained209-column basis. Adding2p(etaFull) is unnecessary. Conversely one must actually validate the retained Gram and not assume its normalization is exact.

Exact integer direct differences or exact cross-Gram cancellation can certify rF squared:

||U1-U0X||F^2=tr(G1)-2tr(X^T U0^T U1)+tr(X^T G0 X).

Reject inconsistent negative exact numerators rather than clipping. A floating LU alignment only proposes X; no floating equation is trusted. Zero X must fail the s2<1 guard under eta1<1 because its normalized Frobenius upper is at least sqrt(q).

## 2. Source comparison and actual shift

Choose O so Q1 is aligned to Q0 O and write U1=Q1 S1. The comparator S1^-1 O^T Tbar0 O S1 has raw Frobenius residual at most

J=sqrt(1+eta1)*[sigma0F+(1+M0)*dF].

The unchanged baseline deleted-row margin gives

amin=sqrt(1-eta1)*(beta-d2)>0.

For the SAME saved U1,T, an exact normal-residual upper nu>=||Uminus^T(Uplus-UminusT)||F gives

actual_shift_F<=sqrt(J^2+(nu/amin)^2).

This follows from the already proved least-squares Pythagoras identity. Use actual validated nu, not an illustrative ceiling smaller than that record's measured normal residual. Source baseline residual sigma0F remains Frobenius-derived; neither saved baseline nor actual T is assumed exact least squares.

This certificate is record-wise. R measures returned-subspace displacement from baseline, including input perturbation/geometric change and numerical effects. It is not a bound on floating roundoff alone, nor does it establish raw eligibility. Raw noise, full-factor/order, source, inverse/eigenpair and emission obligations remain separate when claiming complete phase admission.

## 3. A source-calculated off-span allowance

If only s2=sF=v is used, put d=f(v)=sqrt(2-2sqrt(1-v^2)). On0<=d<beta,

H(d)=sqrt((1+eta1)*[sigma0F+(1+M0)d]^2
           +nu^2/[(1-eta1)(beta-d)^2])

is increasing. A validated passing d threshold for H(d)<the published strict shift allowance yields a sufficient normalized off-span threshold

vcrit=dcrit*sqrt(1-dcrit^2/4),

provided0<=dcrit<=sqrt2. Multiply by sqrt(1-eta1) for a sufficient raw witness-residual threshold. One may instead evaluate H at the directly certified measured distance, without claiming a maximal threshold. Preserve strict comparisons; equality/unresolved intervals are HOLD.

## 4. Blanket scalar Frobenius error budget

In the source-weighted graph lane, hold the encoded radius, Gram maxima and normal-residual ceiling fixed. For epsilon2=epsilonF=epsilon>=0, the scalar forcing and Riccati coefficients e,ef,w,z,a,b are nondecreasing in epsilon. A single graph-radius witness x certified at a passing upper epsilon therefore also works for every smaller epsilon: self-map/contraction improve, and the leading Rayleigh separation improves while alpha>2e remains valid. The same x bounds shift sufficiency throughout that interval.

Store a validated passing rational epsilon_safe. A higher failing point is only a limitation of this sufficient proof, not a necessary floating-error boundary or a demonstrated failure. An additional source-calculated quality requirement below the old full-SVD gate must be reported as a separate sufficient condition; it does not modify that old gate. Source-only calculation and known-outcome development disclosure remain explicit.

These scalar-budget results remain conditional on an actual Frobenius approximation certificate and the declared normal residual; they do not prove every library run satisfies either. Preserve separate abstract operator-only treatment. No new estimator fit, raw acquisition, uniform solver success or external review is created by proposing alignment witnesses or evaluating these bounds.
