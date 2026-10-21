# A minimal sufficient history compression with finite solve certificates

Development — no registry entry. DERIVED source-bound linear-algebra/algorithm results; actual construction and solve evidence is restricted to16 rows. External promotion review PENDING; Physical Promotion=0.

## 1. Fixed source and inherited bounds

F is the unchanged253952×2640 weighted600-cell observation map. Its rank is r=1999 and its nominal kernel dimension641. In the unit Euclidean metrics,

\[
\|F\|\le1,\qquad\sigma_{\min,+}(F)>s=61/27648.
\]

Retain the exact dyadic trial Q and skew trial J from PR307. Define the true real trial trajectory

\[
Y=4096^{-1/2}\operatorname{stack}_{j=0}^{4095}RQe^{jJ/2}.
\]

Pinned parent certificates give ||Q||<9/8, sigma_min(Y)>m=1/384 and ||FQ−Y||<eps=1/8192. Therefore ||Y||<9/8+eps<2. These are inherited validated mathematical bounds, not new measured data. No exact membership of Q in the observable state space is assumed.

Let V=(kerF)-perpendicular in state space, H=rangeF in data space, and P the orthogonal state projection onto V. Distinguish all three spaces from the trial-column space. The source weights, observer, clocks and model are unchanged.

## 2. Minimal sufficient linear statistic

Here sufficient means deterministic recovery of P_Vx from ideal nominal records Fx by a real linear map; no statistical distribution or statistical sufficiency claim is made.

Define

\[
C=Y^TF,\qquad W=C^T=F^TY,\qquad z=Y^Ty.
\]

Since FQ lies in H, ||P_Hperp Y||<=eps. For every trial-coordinate vector u,

\[
\|P_HYu\|^2\ge(m^2-\mathrm{eps}^2)\|u\|^2.
\]

The nonzero singular values of F^T on H exceed s. Hence

\[
\sigma_{\min}(C)>s\sqrt{m^2-\mathrm{eps}^2}
>s(m-\mathrm{eps})=:h=3721/679477248.
\]

C has all1999 rows independent. Because C factors through F, kerF is contained in kerC; equal rank makes these kernels equal. Thus z is a sufficient linear statistic for the1999-dimensional observable quotient, and

\[
B_0=C^+Y^T,\qquad B_0F=C^+C=P.
\]

No linear statistic with fewer than1999 coordinates can have this same kernel: rank(LF)<=number of statistic coordinates. This is a minimal state-reconstruction statistic for this map, not a count of physical readings, independent preparations, frequency sectors or calibrated parameters.

This construction resolves the earlier arbitrary-Q right-inverse problem by lifting through F^TY. It does not declare Q an exact observable basis. For the exact fixture F=[1,0] and Q=(3/5,4/5)^T, the trial right inverse outputs hidden component4/3 on a noiseless unit state; C^+Y^T instead equals(1,0)^T. The old counterexample remains valid.

## 3. The decoder gain is small despite the compression matrix floor

Let U=Y(Y^TY)^(-1/2), an orthonormal data frame. Then

\[
\|P_Hperp U\|<\mathrm{eps}/m=3/64,
\quad\sigma_{\min}(U^T|_H)>\sqrt{4087}/64.
\]

The dimension of H is r, so U^T|_H is bijective. Invertible left-coordinate scaling of a full-row-rank matrix cancels in C^+Y^T, giving

\[
B_0=(U^TF)^+U^T,\qquad
\|B_0\|<\frac{64}{s\sqrt{4087}}<454.
\]

The final comparison is checked by exact rational squares. A generic ||Y||/h bound is valid but unnecessarily large. The small floor h of C alone is not the reconstruction gain of the complete composed decoder.

## 4. Approximate precomputed rows and the full-state projection error

Suppose ALL1999 stored rows G approximate C with ||G−C||<=delta<h. Let P_G be the orthogonal projection onto row(G). Then G has full row rank and sigma_min(G)>=h−delta. The rowspace gap obeys ||P_G−P||<=delta/h: for vectors in kerG, Cv=(C−G)v and the positive singular floor of C controls their V component; equal rank identifies the largest principal-angle gap.

The exact solve decoder based on the stored rows is B_G=G^+Y^T. Since Y^TF=C,

\[
B_GF-P=(P_G-P)+G^+(C-G),
\]
\[
\|B_GF-P\|\le\frac\delta h+\frac\delta{h-\delta}=:a_G.
\]

Both terms matter; a single perturbation debit is not generally sufficient. For gain, CB_0=Y^T and

\[
B_G=G^+CB_0,\qquad
\|B_G\|\le\frac h{h-\delta}\|B_0\|.
\]

This is a full2640-state conformance bound. G's own numerical kernel is not asserted identical to the true nominal kernel; the angle/defect bound quantifies that approximation. Nominal hidden input states remain invisible to the exact F and are not reconstructed.

## 5. A concrete source-bound frame construction

Each column of Y has the form (a cos−b sin)/64 or(a sin+b cos)/64, with a,b from the frozen ordered readout of dyadic Q. Their norms are each below9/8. Trial phases use the exact dyadic frequency and time j/2. Arb192 enclosures produce grid128 phase integers with absolute scalar error<2^-127. The encoded Y columns are then delivered on grid96. Their complete column error is bounded by

\[
e_Y=3\,2^{-127}+504\,2^{-96}.
\]

The1/64 and sqrt4096 factors cancel in the phase-error stack; the second term covers all253952 delivered coordinate roundings. The zero-frequency column is encoded exactly but may use the same conservative envelope.

Apply the audited native adjoint action from PR318 to each encoded column. Its proved absolute error a_native on data ball2049 is approximately1.271842e-24. Encoded columns have norm<3 and lie inside that domain. Each stored W column, equivalently each G row, therefore has error at most a_native+e_Y. Since sqrt1999<45,

\[
\delta=45(a_{\rm native}+e_Y)\approx5.75192\,10^{-23}.
\]

Exact fraction checks give

\[
a_G<2^{-55},\qquad\|B_G\|<455.
\]

These full-frame conclusions require all1999 rows to be constructed and validated. Sixteen rows do not establish them. The actual16-row construction, including native input/output and phase hashes, is recorded separately. The trusted trial-slice hash, sourceoperator hash and expected executable build hash are explicit admission inputs; selfreported metadata alone is not source verification.

## 6. Finite compression, solve and lift need residual certificates

For a data record y, the exact intended RHS is z=Y^Ty. A finite implementation computes zhat, coefficient vector a and state xhat. Require independently certified bounds

\[
\|\widehat z-z\|\le e_z,\quad
\|GG^Ta-\widehat z\|\le e_r,\quad
\|\widehat x-G^Ta\|\le e_{\rm lift}.
\]

Then, using G^+=G^T(GG^T)^(-1),

\[
\|\widehat x-B_Gy\|
\le\frac{e_z+e_r}{h-\delta}+e_{\rm lift}.
\]

There is no unnecessary square of the inverse singular floor in this state-error bound. The residuals can be checked with exact saved dyadic products or validated intervals; an ordinary floating residual is not itself a proof. A reusable factorization may propose the coefficients, while these residual gates decide acceptance for each record.

Encoded Y must not be silently substituted for exact Y. Its operator error is at most eta=45e_Y. For ||y||<=2, if computing the encoded RHS introduces at most zeta=2^-65 additional vector arithmetic error, then

\[
e_z\le2\eta+\zeta<2^{-64}.
\]

With e_r<=2^-64 and e_lift<=2^-44, exact arithmetic verifies an implementation envelope<2^-43. This is an explicit future full-solve contract, not an executed1999-row factorization or full-record accuracy result.

For y=Fx+e, ||x||<=X and ||e||<=D, the complete state envelope is

\[
\|\widehat x-Px\|\le a_GX+455D+
\frac{e_z+e_r}{h-\delta}+e_{\rm lift}.
\]

The earlier illustrative X<=1,D<2^-50 profile then implies observable-chain error<2^-40, IF the full construction/solve and all input premises are supplied. Those physical/input premises remain UNSUPPLIED/HOLD. This is not the old six-ratio q or Hankel accuracy gate.

## 7. Actual partial construction and exact solve control

Sixteen distributed stationary/u/v trial columns were encoded, phase-enclosure checked and passed through the actual2640-state native adjoint. The packed grid96 rows are saved. An authenticated-source replay reproduces all16 rows and its scientific receipt byte-for-byte. All122880 nonzero-column phase scalar enclosures are checked. Independent review regenerates the encoded input/RHS hashes at higher precision and validates source/build bindings.

Their16×16 Gram matrix is computed exactly from the saved row integers. Sixteen positive rational elimination pivots certify rank16; the chosen encoded RHS is solved exactly, with normal-equation residual0. A finite grid96 lift checks all2640 output coordinates against its exact rational value. These are actual source-derived partial construction/solve controls, not synthetic diagonal Gram placeholders.

For the selected true C_I, the exact decoder projects onto row(C_I), a16-dimensional subspace of V. The partial row-error factor is sqrt16=4, giving a separate partial projection defect<2^-58 under the same source bounds. This is not fullP. Any rank<=16 decoder satisfies

\[
\|B_{16}F-P\|\ge1,
\]

because at least1983 directions of the1999-dimensional V remain in its nullspace. Successful partial solves therefore cannot certify full observable extraction. The actual finite output is certified against the16-row solve, with no claim that its unknown coordinates equal named character/frequency sectors.

## 8. Compression is not an arbitrarily accurate replacement for F

The rank-preserving statistic allows state reconstruction without constructing the entire raw data map. A different approximation, Y(Y^TY)^(-1)C=P_rangeY F, has only the general full-operator residual bound

\[
\|(I-P_{\rm rangeY})F\|\le(\mathrm{eps}/m)\|F\|<3/64.
\]

Its small residual on Q is not a full-state1/8192 action certificate. The exact rational fixture in CONTROLS.json shows the distinction. Such an approximation cannot be substituted into the old recurrence's2^-68 action slots. The compressed inverse above is a separately derived algorithm with its own conformance/residual gates.

## 9. Storage, provenance and remaining gate

The prospective full stored G has1999×2640 entries and a1999×1999 Gram/factorization, reused across records. Exact RHS compression can be generated/streamed from the trial basis; no full time×trial Y or287-GiB Hankel is required. This statement does not claim a completed full frame, reusable factorization or measured full-pipeline throughput. Native precomputation of all1999 rows and its verified solve implementation remain OPEN/HOLD.

The new algebra provides a candidate route around8192 repeated normal actions; it is not an unexecuted8192 test pass. Existing source, conditioning, action and native results remain unchanged. Full physical correspondence, preparation/timing/noise/encoding evidence and any separate floating estimator remain HOLD.641 nominal hidden components remain unrecovered.

Ledger v0.39/CRL-2; Development—no registry entry. All tolerances, precisions and solve budgets are O03 controls, not theory constants. External promotion review PENDING; Physical Promotion=0. Zero new frozen mathematical retractions; sessionratio NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png unavailable/unused—please re-upload if needed. Notes/ASTER unused.
