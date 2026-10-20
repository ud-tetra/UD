# Grade-rate invariance and local motion of the hidden subspace

Development — no registry entry. DERIVED conditional mathematics, with exact source arithmetic checks. External promotion review PENDING. Physical Promotion=0.

## 1. Fixed chain complex, observer and inherited premises

Use the existing unit-chain600-cell generator A=A1+A2+A3. Ai acts only between grades i-1 and i, with upper block -Bi and lower block Bi^T. The actual source has B1B2=B2B3=0, Ai^T=-Ai and AiAj=0 for i≠j. R observes every simplex of the vertex-link subcomplex L through grade2:12vertices,30edges,20faces. Write Rk for each grade restriction and BL,k for the link boundary. Downward closure gives the exact cochain restriction identities

\[
R_1B_1^T=B_{L,1}^TR_0,\qquad
R_2B_2^T=B_{L,2}^TR_1.
\]

The old continuous-history rank1893, dynamical kernel N of dimension747, harmonic decomposition and isolated character ranks are inherited source premises, not newly recomputed ranks. Time and amplitudes remain internal model coordinates. No apparatus or physical rate/metric law is supplied.

## 2. Grade-uniform rates cannot reveal the nominal hidden states

Let Ei=imAi and H=kerA. Pair annihilation and skewness imply the orthogonal decomposition

\[
X=H\oplus E_1\oplus E_2\oplus E_3.
\]

Indeed the images are mutually orthogonal, their common orthogonal complement is the common kernel, and A restricts to Ai on Ei. Each Ai is invertible on Ei, so its real oscillatory trajectories have no zero-frequency term. Define Ni as the unobservable subspace of the single-channel flow exp(tAi) restricted to Ei, with the same R. Let Hd=H∩kerR.

**Theorem GR1.** For every constant rate triple with a1a2a3≠0,

\[
N\!\left(\sum_i a_iA_i,R\right)
=H_d\oplus N_1\oplus N_2\oplus N_3=N.
\]

Consequently the continuous-history rank remains1893 and kernel dimension747. No separation of the weighted frequencies is assumed: the statement includes coincident frequencies across channels. All isolated C10character kernels/ranks also remain the same, since the generator still commutes with the declared signed action and its full dynamical kernel is unchanged. This does not make isolated ranks additive.

Proof: decompose an invisible trajectory into its stationary part and its three image-channel parts. In grade0 only H and E1 contribute. Separating the constant term from the nonzero-frequency part gives zero R0 output for E1. Its grade1 output obeys

\[
\frac{d}{dt}R_1x_1(t)=a_1B_{L,1}^TR_0x_1(t)=0.
\]

It is thus constant; because the entire E1 trajectory has no DC term, that output is zero. Remove E1's output. In grade1 the only remaining nonstationary contribution is E2's lower component, which must vanish after separating the stationary term. The second restriction identity then makes its upper grade2 output constant and hence zero. Remove E2. In grade2 the remaining E3 lower output must vanish; its upper grade3 is not observed. Finally the stationary output is zero. Thus each channel is separately invisible. Conversely separate invisibility implies zero total output. A nonzero constant ai merely reparametrizes that channel's time, so Ni is independent of ai. The same proof applies to the nominal ai=1 and proves the equality. Commutation alone would not have proved this; downward-closed, grade-resolved observation is essential.

**Corollary GR2.** N is invariant under each Ai. Therefore for arbitrary real locally integrable rates ai(t), the original N remains invisible. One may write the propagator as exp(sum_i Ai integral_0^t ai(s)ds), because the Ai commute. This is an inclusion statement; time-varying or zero rates need not retain the full nominal observable quotient. For constant rates with zeros, no old hidden mode is exposed and the kernel contains N. At all three rates zero it is simply kerR of dimension2578. No finite-sample conditioning, alias exclusion, unknown-rate identification or calibration guarantee is transferred from GR1.

## 3. Local weights change which states are hidden

Let h0 be the consistently oriented fundamental3-cycle,600coefficients±1, and h=h0/√600. Choose either J={0}, the tetrahedron τ=(0,33,34,41), or its10element rightC10orbit

\[
J=\{0,9,227,432,447,582,538,347,332,141\}.
\]

For -1<ε and ε≠0 set D=I+εP_J on C3. Keep B1,B2 and replace the top boundary by B3D; assemble K_D with upper block -B3D and lower block DB3^T. This is a declared weighted-boundary, unit-Euclidean-metric model in fixed x coordinates.

It preserves boundary support, adjacent-grade locality, skewness, odd chain-parity anticommutation and B2(B3D)=0. Because D is invertible the chain complex is isomorphic to the original and has the same homology. Its coefficients are weighted boundary coefficients, not unchanged signed integer incidences. No native selection of those weights or physical realization is derived. The orbit choice commutes with the actual signed C10action; the single-tetrahedron choice does not.

New exact checks show the selected boundary columns have Gram4I in both cases. Therefore

\[
\|K_D-A\|=2|\epsilon|.
\]

The old h is no longer stationary or invisible. At the global face port1680, simplex (33,34,41),

\[
(RK_Dh)_{1680}=-\epsilon/\sqrt{600}.
\]

The orbit choice also has the same derivative at port1689; its other selected boundary faces lie outside R. Thus arbitrarily small positive orbit weights can move the hidden subspace while preserving C10, adjacent grades and the chain identity.

However z=D^-1h remains a stationary invisible vector: K_Dz=0 and Rz=0. Moreover RA z is nonzero at the same face, with value ε/[(1+ε)√600]. Hence both differences are witnessed:

\[
h\in N_A\setminus N_{K_D},\qquad z\in N_{K_D}\setminus N_A.
\]

This proves that the hidden subspace moves. It proves neither a decrease of its dimension nor rank1894. The PR300 nonlocal harmonic rank calculation does not transfer to this weighted model. Its full history rank and conditioning are NOT_COMPUTED here.

For m=|J| the angle θ between the old and new stationary dark lines obeys exactly

\[
\sin^2\theta=
\frac{m(600-m)\epsilon^2}
{600[(600-m)(1+\epsilon)^2+m]}.
\]

This follows from r=(1+ε)^-1, ||D^-1h||²=(600-m+mr²)/600 and <h,D^-1h>=(600-m+mr)/600. It is a geometric line angle in the stated metric, not a physical curvature or leakage measurement.

## 4. A finite scalar response, without inferring kernel shrinkage

For either choice of J, assume0<|ε|≤1/2 and prepare exactly the old h in fixed x coordinates. Let y_f(t) be the noiseless output at port1680. Exact source row sums give ||A||≤12; the skew perturbation bound gives ||K_D||≤13. Also

\[
\|K_Dh\|=\sqrt{4m}|\epsilon|/\sqrt{600}
\le\sqrt{40}|\epsilon|/\sqrt{600}<7|\epsilon|/\sqrt{600}.
\]

K_D is odd under chain parity. The C2face output of a C3initial state therefore contains only odd powers. Its linear term is -εt/√600. The third-order integral remainder of the odd part (exp(tK)-exp(-tK))/2 is at most |t|³||K³h||/6: its third derivative is K³cosh(tK)h and ||cosh(tK)||≤1 for real skew K. Thus

\[
|y_f(t)+\epsilon t/\sqrt{600}|
\le |t|^3\,13^2\|K_Dh\|/6.
\]

At the declared internal time t=1/64 the relative remainder is less than

\[
\frac{7\cdot169}{6\cdot4096}=\frac{1183}{24576}<\frac1{16}.
\]

Consequently the sign is -sgnε and

\[
\boxed{\frac{15|\epsilon|}{1024\sqrt{600}}
<|y_f(1/64)|<
\frac{17|\epsilon|}{1024\sqrt{600}}.}
\]

This is a certified finite mathematical response, not an acquisition gate. If both nominal and alternative scalar readings have independently justified total error at mostν, their admissible reading intervals are disjoint whenever ν is below half the lower bound. Preparation, time, gain, encoding and model errors must all be covered in those same scalar coordinates; none was measured here. Exact lower/upper rational enclosures and example angle values are in RESULT.json. At ε=2^-40 the certified response lies between5.4389e-16and6.1642e-16, in internal readout units. No SI, six-ratio or prior residual-gate claim follows.

## 5. Coordinate and metric provenance

With F=diag(I,I,I,D), y=Fx gives

\[
K_y=F K_D F^{-1}=H^{-1}A,\qquad
H=\operatorname{diag}(I,I,I,D^{-2}).
\]

The transformed generator is skew in H and R y=R x. But preparations transform too: x0=h corresponds to y0=Fh, not y0=h. The same numeric h remains stationary for H^-1A because Ah=0; fixed y0=h corresponds to the new dark state x0=D^-1h. Thus this basis/metric relation cannot be used to claim that a fixed-coordinate H^-1A perturbation exposes its old fundamental harmonic. The equality ker(H^-1A)=kerA concerns the stationary generator kernel, not an assertion about the complete dynamical observer kernel. Equal numeric vectors in these two coordinate conventions are not automatically the same prepared state.

## 6. Verification and open scope

The new checker reads3JSON members from the immutable observer archive without executing archived scripts. It checks1800boundary-product columns,15840cross-channel product columns,60+60cochain restriction entries, the harmonic cycle, the actual signed action/orbit, selected boundary Gram4I, the row bound12,19200metric-transform triplets and rational angle/response enclosures. Three scientific outputs replay byte-identically. Nominal1893/747and sector ranks remain inherited premises.

Separate same-team source/proof/arithmetic review is not external promotion authority. No raw acquisition, estimator/SVD, physical preparation or calibrated uncertainty record was produced. All prior nominal results and HOLD/NO-GO decisions remain unchanged. The next mathematical question is the complete history rank and conditioning for an explicitly fixed weighted model; the physical question separately requires a source-supported constitutive law and independently justified preparation/readout/time/error receipts. Ledger v0.39 / CRL-2; Development—no registry entry; Physical Promotion=0.
