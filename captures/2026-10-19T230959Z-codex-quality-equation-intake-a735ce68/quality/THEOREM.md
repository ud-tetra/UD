# Retained rank-209 quality cannot hold uniformly on the encoded q-ball

Development — no registry entry. Physical Promotion=0. External nonconstructor review PENDING. This is a deterministic computational obstruction, not a physical model failure or a phase-extraction counterexample.

## Fixed domain and provenance

The baseline is the original encoded synthetic `ramp_clock_stress.i64le`, SHA-256 `25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59`, shaped preparation × sample × channel = 37 × 8191 × 62. The scalar quantum is q=2^-48. The unfolded spatial index is j=37c+a. The unchanged fixed integer sketch is A with S=A/128; exact projected data are Z=Y S. Prior exact cross-Gram H=Uintᵀ(X0 A), where X0 is the unfolded integer baseline and U=Uint/2^77, is an explicitly inherited premise pinned by archive, member and source replay receipts. It is not a new constructor-independent derivation of that source cross-Gram. Current proof independently recomputes U's exact Gram, regenerates the fixed sketch and checks its exact Gram, reads every baseline scalar, and computes the alternating baseline projection with Python/FLINT exact integers. No floating GEMM is assumed exact.

## Two prospectively frozen records

Let v be the fixed 320-coordinate nullvector padded to2294, the special middle column of A. For each preparation a and count d∈{1,2}, select distinct channels ordered by decreasing |v[37c+a]| with ascending c as tie-breaker. Set w[37c+a]=sign(v[37c+a]) at those d channels and0 elsewhere; sign(0)=+1. Define u_t=(-1)^t and the integer perturbation K_ac(t)=u_t w[37c+a]. Both recipes and their code were frozen before their own raw/projection evaluation; neither was selected by the resulting success. All outcomes retained. No estimator was run.

Every complete62-vector has squared encoded perturbation norm d q². The d=1 record lies in the CLOSED q-ball; d=2 lies in the CLOSED sqrt2 q-ball and hence the3q/2 ball. Exact modified-byte hashes are retained. The recipes are adversarial arithmetic noise about one synthetic nominal; they are not proposed physical noise laws.

## Compression certificate

Take L=[U,u/128] (8191×210). Propose210 real right test columns R by the frozen NumPy QR of [C0ᵀ,b], where C0 is the pinned prior209×321 coefficient proposal and bᵀ=wᵀA/128. QR is only a dyadic witness proposal: its orthogonality and success are NOT presumed. Actual exact right Gram RᵀR is evaluated from decoded dyadics.

Define D=Lᵀ Z R. The exact top209 rows before multiplication by R have integer numerator

H+(Uintᵀu)(wᵀA)

over2^132. The final row has numerator

[uᵀ(X0 A)+8191(wᵀA)] 2^70

over the same2^132. Thus the saved210×210 D is the exact compression of the actual encoded perturbed data, rather than of a low-rank approximation. The large global low-rank source residual is not discarded or subtracted. The left and right frame Gram absolute row sums certify ||L||2 and ||R||2. At512-bit Arb arithmetic, invert D and bound ||D^-1||F outward. Since singular values obey

σ210(D) ≤ ||L||2 ||R||2 σ210(Z),
σ210(D) ≥ 1/||D^-1||F,

we get the retained exact rational lower bounds in CERTIFICATE.json:

- d=1: σ210(Z)>6.7313944404399×10^-13.
- d=2: σ210(Z)>1.0800978363112×10^-12.

Both exceed εcap=2^-41≈4.547473508864641×10^-13. The displayed decimals are shortened safely below the actual certificate rational lower bounds.

By the rank approximation inequality, EVERY real matrix B of rank at most209 satisfies ||Z−B||2≥σ210(Z)>2^-41. In particular, no proposed polar retained product polar(Uret) diag(sret) polar(Vtret) can meet the PR252 retained εcap on either record. Any Frobenius residual upper bound would also have to exceed this necessary operator lower bound. Consequently universal success of that QUALITY PREMISE on the entire encoded q-ball is impossible, independently of any numerical solver, precision, library convergence or initialization. The conclusion is stronger than a floating-library failure: the requested approximation is mathematically infeasible.

## Scope exclusions

This does not falsify the conditional phase-only theorem, which explicitly requires the quality premises. Nor does it show that the emitted phases or exact saved transition phases fail: no new fit/eigenvalue/phase evaluation occurred. It does not revoke finite PR250 passes, identify an optimal tolerance, imply a physical leakage mechanism, or certify/falsify six-ratio2^-39 calibration. u_{t+2}=u_t, so the extra temporal component itself has TWO-step multiplier+1; rank infeasibility and phase identity are separate objects. The source209 cutoff count can remain209 while the discarded210th singular value is too large for the stricter εcap.

The proof uses only a210×210 compression and small source/test factors, with baseline read in place. No full287-GiB Hankel matrix or persistent new150-MB raw copy is allocated.
