# Frozen C10-orbit weighted model: exact rank and finite sampling

Development—no registry entry. DERIVED conditional mathematics, external promotion review PENDING, Physical Promotion=0. No physical weight law, acquisition or estimator fit is supplied.

## 1. Definitions and inherited premises

Use the oriented 600-cell boundary complex, unit Euclidean chain coordinates and the unchanged downward-closed62-channel vertex-link restriction R from the source archive pinned in SOURCE_BINDINGS.json. Nominal A is the skew adjacent-grade boundary generator. Its full history rank1893/kernel747 and observed signed frequency count105 are inherited from the prior observer certificate. PR303 establishes the grade-channel separation proof for this downward-closed observer; it is not replaced by commutation alone. Readout does not see grade3 directly. No archived executable is run.

Freeze J=[0,9,227,432,447,582,538,347,332,141], the signed rightC10 orbit from PR303, and epsilon=1/2. Let P select these ten tetrahedron coordinates, D=I+P/2, and replace only B3 by B3D, with the negative transpose in the opposite block, obtaining K_D. B1,B2 and R are unchanged. Weighted chain-square zero and skewness persist, while the incidences have declared weights. The construction retains the C10 action; character-resolved ranks for the weighted model are NOT_COMPUTED here. These are internal model units and fixed preparations in unit coordinates.

Let B=B3, G=B^T B, C0=R2 B. For integer arithmetic put D2=2D, M=D2 G D2, C=C0D2. Scaling by4 and2 does not change the relevant continuous cyclic row spaces. Define r0=rank_Q span(C0 G^j) and rD=rank_Q span(C M^j). The unchanged lower channel ranks cancel in the comparison. Downward-closed channel separation gives

    rank_history(K_D,R)=1893+2(rD−r0).

Each observed nonzero top singular mode contributes both first-order partners; the top stationary mode is unseen. The separation holds even if frequencies of different channels coincide.

## 2. Exact finite certificates

The checker reconstructs B from sorted oriented tetrahedra, G and C0 from JSON data. Three explicit nonzero minors over the prime1009 certify lower bounds390,443,444 for the nominal, weighted and augmented cyclic spaces. Selected time/channel row indices and coordinate columns are retained; their determinants are respectively103,66,1005 modulo1009. These are characteristic-zero lower bounds, not deficient-rank upper bounds.

For the upper bounds set U=stack(C0; e_j^T for j in J) and W=span(U G^k). The source polynomial q of degree53 annihilates U exactly:18000 integer entries of Uq(G) are zero. Its30 monic squarefree factors are pairwise coprime (435 gcd checks), with productq. For each factor f of degree d_f form

    V_f=stack_{0<=j<d_f} U G^j (q/f)(G).

Polynomial Chinese remaindering decomposes the cyclic row space as the sum of these factor row spaces. For each nominal and augmented V_f the stored primitive integer rows B_f, pivot columns I_f and positive row denominators d_i satisfy B_f[:,I_f]=diag(d_i), and

    V_f[:,I_f] diag(1/d_i) B_f = V_f.

The checker clears denominators and verifies the identities with arbitrary-precision integers. Thus the retained rows explicitly span all input factor rows, independently of a numerical tolerance or an asserted RREF rank. Summing upper dimensions gives390 nominal and444 augmented. Together with the nonzero minors, r0=390 and dimW=444 exactly. Compact row normalization changes only the witness encoding; no mathematical residual is discarded.

W is invariant under G. Because it contains all selected coordinate rows, P maps W into W; hence D2 and M preserve W, and C has its rows in W. The signed dual graph is connected and sign-gauges G to its connected graph Laplacian. Thus kerG=span(h), where h is the oriented fundamental cycle with ±1 entries. The zero spectral projection of any selected coordinate has nonzero harmonic component, so h belongs to W. Also D2^-1=I/2−P/6, hence z=D2^-1h belongs to W. It is nonzero and Mz=Cz=0. Therefore the weighted cyclic row space has dimension at most444−1=443. The weighted modular minor saturates this upper bound, proving rD=443.

Consequently the exact full history rank is1999, its kernel dimension641, and the net rank gain over nominal is106. This uses the inherited nominal1893 proof and channel separation plus the newly certified top-channel delta; it is not represented as a new dense2640-dimensional rank computation.

## 3. The two kernels are not nested

Let F=W^perp, dimF=156. It is G-invariant, P annihilates it, and it is orthogonal to h. The weighted C3-coordinate dark space is exactly F direct-sum span(D^-1h), by the saturated rank. Its oscillatory first-order partners are F in grade3 and BF in grade2:312 shared dark dimensions, because D acts asI onF. These also lie in the nominal kernel. The nominal top dark dimension is1+2(599−390)=419, leaving328 unchanged lower dark dimensions.

The replacement stationary line D^-1h is not nominally unobservable: the named face1680 of C0D^-1h is nonzero (−1/(3sqrt600) when h is normalized). Thus

    dim(N_old intersection N_new)=328+312=640;
    rank(new history map restricted to N_old)=747−640=107.

The old kernel has dimension747 and the new641. The rank gain106 does not mean simple setwise removal of106 old hidden directions. Both kernel set differences remain nonempty. This is a declared mathematical model change, not recovery by a right inverse of a fixed boundary projection.

## 4. Frozen finite-sample map

Define F4096=4096^-1/2 stack_{j=0}^{4095} R exp(j K_D/2). The step1/2 and normalization1/64 are fixed in the model plan; this is not a physical clock calibration. The source row/column sum bounds give ||B1||²<=24, ||B2||²<=15 and ||B3D||²<=15. Pairwise channel annihilation implies ||K_D||<=sqrt24<5. Half-step phases lie in an interval of diameter<5<2pi, so distinct continuous eigenvalues have distinct sampled nodes.

K_D is real skew and normal, with at most2640 distinct eigenvalues. The first d distinct-node Vandermonde time rows, d<=2640<4096, separate its modal output vectors. Therefore the frozen sample kernel equals the continuous-history kernel: sample rank1999/kernel641. No dense full-history, time-Hankel or SVD array is required for this argument.

## 5. Formal conditioning bound, and its limit

The full2640-domain condition number is infinite because the kernel is641-dimensional. The following bound concerns only N_new^perp with the declared Euclidean norms. It is deliberately conservative and does not certify useful inversion precision.

Set S=2K_D, an integer normal skew matrix with ||S||<10. On its rational observable quotient the minimal polynomial p is a monic rational divisor of the integer characteristic polynomial, hence belongs to Z[x] by Gauss's lemma. Normality makes p squarefree. Its degree d is at most D=105+2*443=991: the unchanged lower observed frequencies are a subset of the old105, and the new top channel has at most443 positive frequencies. The nonzero integer discriminant implies

    product_{i<j}|lambda_i−lambda_j|>=1.

For sampled nodes z_i=exp(lambda_i/4), |Im(lambda_i−lambda_j)|<20. Concavity of sine on[0,5/2] and its degree7 alternating Taylor lower bound75935/129024>1/2 show sinx>=x/5 there. Hence |z_i−z_j|>=|lambda_i−lambda_j|/20. With N=d(d−1)/2, the d-by-d Vandermonde determinant has modulus at least20^-N. Its norm is at most its Frobenius normd, giving

    sigma_min(V_d)>=20^-N/d^(d−1)>2^(-2452725−9900).

The integer jet O_D=stack_{j=0}^{D−1} R S^j has rank1999 and the same kernel. The product of its positive squared singular values is a nonzero integer coefficient of its integer Gram characteristic polynomial, hence at least1. The bound ||O_D||<=sqrt(62D)10^(D−1)<2^3968 gives

    sigma_min,+(O_D)>2^(-3968*1998)=2^-7928064.

Writing modal outputs z=(R P_lambda x)_lambda, the jet modal Vandermonde has norm<=D10^(D−1)<2^3970. Thus ||z||>2^(-7928064−3970)||x|| on N_new^perp. Apply the temporal Vandermonde to these vector-valued modal outputs, retain the firstd sample blocks and the normalization1/64. Since ||F4096||<=1,

    sigma_min,+(F4096)>2^-10394665,
    kappa_+(F4096)<2^10394665.

This is a finite full-quotient analytic bound, not a numerical singular-value enclosure. It is far too weak to certify practical conditioning, the previous nominal2029 bound, any2^-39 calibration/2^-38 shape gate, estimator accuracy or noise tolerance. Those transfers remain HOLD. Cross-channel finite-sample Gram terms cannot be replaced by a maximum of isolated channel condition numbers. A tighter whole-observable-quotient Gram enclosure is the next computational question.

## 6. Provenance and reproduction

Run compute.py with --repo pointing at a complete UD checkout, --evidence at this capture directory, and --out at a NEW directory. It reads3 pinned JSON members, the compact witness archive and nonzero-minor records; dependencies are numpy, scipy and python-flint. Output3scientific JSON files must replay byte-identically. The witness constructor and freeze are retained separately from the verifier. Separate same-team review independently built the signed dual adjacency, exact factor dimensions, graph/norm facts and analytic constants; it is not external promotion review.

No measured source, acquisition, physical constitutive correspondence, raw timing record, floating estimator, full Hankel array or new gate has been supplied. Earlier nominal conclusions and failures remain intact. The declared model study does not remove the native acquisition/provenance HOLD. Ledger0.39/CRL-2 apply; O03 controls are not theory constants. Full-session retraction ratio NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png unavailable/unused; please re-upload if needed. Notes/ASTER available but unused.
