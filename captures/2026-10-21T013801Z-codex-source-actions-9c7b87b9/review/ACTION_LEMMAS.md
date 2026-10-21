# Independent full-domain fixed-point action derivation

Let the admitted source operator have H=2K, with K real skew, normK<5, n2640, M4096, and the ordered unique62-coordinate restriction R. The independently reconstructed source file has14880 entries and exactly the frozen hash in SOURCE_BOUND_CHECKS.json. An arbitrary row-bounded input matrix is not admitted by this theorem.

Each half-step approximates exp(plus-or-minus K/2). The exact Taylor tail after degree40 has norm at most

    tau=(5/2)^41/(41!*(1-5/84)).

The first omitted term is degree41; every subsequent term ratio is at most5/84. Independent Fraction arithmetic proves tau<2^-110 (the producer's weaker2^-109 comparison also holds).

Internal inputs are exact grid128 integers. Each signed matrix multiply is exact and division by4k truncates toward zero. Its coordinate error is strictly below2^-128; the vector bound r0=52*2^-128 follows from sqrt2640<52. Term errors relative to the exact Taylor terms obey e1<=r0,e2<=9r0/4,e3<=23r0/8. For k>=4, the recurrence e_k<=(5/(2k))*e_previous+r0 keeps e_k<3r0. Summing40 errors gives half-step rounding below120r0=6240*2^-128. Exact integer accumulation adds no rounding.

For every internal dyadic v the complete step therefore differs from the exact skew exponential by at most tau*norm(v)+r. Freeze cap2^18 and e=tau*2^18+r. Compare each computed step with exact exp on that computed input: exact propagation of the prior error has norm unchanged, and the new local error is at most e. Thus after at most4096 calls, accumulated error is at most4096e. This avoids multiplying a loose exp(5/2) growth factor at each time.

The cap is closed by induction. Exact forward states have norm at most2048. Exact adjoint partial sums have norm at most(1/64)*sum_j norm(y_j)<=sqrt4096*norm(y)/64<=2049. Their computed counterparts differ by at most4096e<1, so every internal input remains below2^18. The adjoint estimate applies before or after an exact injection and uses the norm of the complete supplied data, not a fictional per-time uniform amplitude assumption.

External inputs and outputs use grid96. Forward input shift32 is exact; selecting R and dividing by64 then delivering on grid96 means truncating38 bits. The normalized stacked trajectory error is at most the maximum state error because sqrt4096/64=1. Delivery contributes at most504*2^-96. Therefore forward error on state ball2048 is at most4096e+504*2^-96.

Reverse Horner adjoint processing injects y_j/64 exactly via shift26 on grid128, then applies the negative half-step except at j0. It yields the exact intended ordering sum exp(-jK/2)R-transpose y_j/64. There is no injection rounding. Final output shift32 contributes at most52*2^-96, so adjoint error on data ball2049 is at most4096e+52*2^-96.

The independent exact fractions give about7.121319393e-25 forward and7.064268972e-25 adjoint; both are below2^-79, hence well below2^-68. The nonlinear rounded actions need not be exactly linear or exact transposes. The pointwise absolute-domain bounds suffice for C29's normal-action composition: normF<=1 and forward output norm<2049 imply normal error at most2^-67. They do not supply physical/input premises or a completed8192-step decoder run.

The C++ implementation's mathematical guarantee assumes correct GMP exact-integer semantics and the recorded Linux64 ABI. Independent actual-binary tests check finite large signed cases, including input-domain boundary, against Python integers; they do not formally verify a compiler or every ABI input. The actual adapter additionally requires a trusted expected executable hash and the frozen operator hash before every call. Build provenance, stable intended files/runtime, and library correctness remain explicit premises; hash identity is not trusted-computing attestation or concurrent-mutation prevention.

Development — no registry entry. Same-team mathematical/software review; external review PENDING; Physical Promotion=0. Actual full8192 decoder execution and physical/input admission remain HOLD.
