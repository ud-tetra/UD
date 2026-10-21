# Source-bound forward and adjoint actions for the weighted600-cell map

Development — no registry entry. DERIVED numerical-method certificate plus executed mathematical reference controls. External promotion review PENDING; Physical Promotion=0. No physical acquisition, calibrated input or full8192-step decoder run is claimed.

## 1. Object and source binding

Keep the PR307/PR313 map unchanged:

\[
F=\frac1{64}\operatorname{stack}_{j=0}^{4095}R\exp(jK/2),\quad
F^Ty=\frac1{64}\sum_{j=0}^{4095}\exp(-jK/2)R^Ty_j.
\]

The state dimension is2640 and data dimension253952=62*4096. R is the ordered62-coordinate vertex-link restriction at source vertex0. The generator has upper adjacent blocks minus oriented simplicial boundary matrices and lower positive transposes; only the ten frozen tetrahedron columns J carry weight3/2. Put H=2K. Its14880 nonzero entries are integers±2 or±3. The source checker reconstructs all entries and observer indices from pinned JSON members; no archived executable is run. The exact generated OPERATOR.txt SHA256 is cca3ed7e671b8397c3940921d9845399425fd2558cc62708941c00fc4b899950. The theorem admits those exact bytes, not arbitrary matrices satisfying a row bound. The adapter enforces that hash before every executable call. It also requires an expected executable SHA256 from a trusted source/build receipt, checks that hash before every call, and rejects mismatches. The integration receipt binds the actual binary, build receipt and adapter source. The receipt establishes file identity; correctness of the compiler, GMP runtime and trusted build provenance remains an explicit premise, not a trusted-computing attestation.

Exact boundary-square checks and weighted top-column scaling give the adjacent chain annihilations. Maximum absolute boundary row/column products give squared norm caps24,15,15. On each grade the adjacent exact/coexact ranges are orthogonal, so the square of the skew generator has norm at most24. Consequently ||K||<=sqrt24<5, and ||H/4||=||K/2||<5/2. The separate check max absolute row sum(H)=24 is useful for implementation auditing; it alone is not the spectral norm proof.

The rank1999/kernel641 and conditioning premises of PR307 are unchanged and inherited. These action proofs do not recompute them or reconstruct any hidden state.

## 2. A finite rounded half-step

Both action inputs and delivered outputs use exact integer coordinates times2^-96, matching the PR313 decoder. Internally use integers times2^-128. For Q=H/4=K/2 and sign sgn=±1, the half-step routine evaluates

\[
t_0=x,\quad t_k=\operatorname{trunc}_{128}(\mathrm{sgn}\,H t_{k-1}/(4k)),\quad
\widetilde E_{\mathrm{sgn}}x=\sum_{k=0}^{40}t_k.
\]

Every matrix product and sum is exact integer arithmetic. Each division truncates toward zero, with absolute coordinate defect less than2^-128. The polynomial truncation obeys

\[
\left\|e^{\mathrm{sgn}Q}-\sum_{k=0}^{40}(\mathrm{sgn}Q)^k/k!\right\|
\le\tau=\frac{(5/2)^{41}}{41!}\frac1{1-5/84}<2^{-109}.
\]

Let u=52*2^-128, since sqrt2640<52. Relative to the exact Taylor terms, the rounded term errors obey e1<=u, e2<=9u/4, e3<=23u/8 and e_k<3u for every k>=4: their recurrence is e_k<=(5/(2k))e_(k-1)+u. Summing40 term defects gives a whole-half-step arithmetic error less than r=120u=6240*2^-128. This is an aggregate vector error, not a per-primitive floating tolerance. Therefore for every supplied internal dyadic state v,

\[
\|\widetilde E_{\pm}v-e^{\pm K/2}v\|\le\tau\|v\|+r.
\]

This statement covers all state directions, including nominally hidden ones. It does not assume errors stay in the observable subspace.

## 3. Forward action and normalization

The input v has norm<=2048. Shift its integer coordinates left32 bits to the internal grid, exactly. Emit the62 selected coordinates at j=0; for subsequent j apply the positive half-step above. To normalize by64 and deliver on grid96, divide each selected internal integer by2^38 and truncate toward zero.

The corresponding exact trajectory has norm<=2048 at every time because K is skew. Freeze an intentionally loose internal state cap C=2^18 and put

\[
e=\tau C+r,\qquad E=4096e.
\]

At any computed step inside that cap, comparison with exact exp(K/2) on the computed input adds at most e. Exact exponential isometry then gives an error at index j at most je. There is no need to multiply by an exp(5/2) bound at every time. Exact rational arithmetic verifies E<2^-77<1. Induction keeps every computed state below2048+1<C, closing the cap used in the proof.

The normalized stack has error at most the maximum state error, since sqrt4096/64=1. Its final coordinate delivery adds less than sqrt253952*2^-96<504*2^-96. Thus the implemented reference forward action obeys

\[
\|\widetilde Fv-Fv\|\le E+504\,2^{-96}<2^{-68},\qquad\|v\|\le2048.
\]

The exact upper fraction is retained in ACTION_CONSTANTS.json. It is about7.1214e-25, substantially below the required gate. Neither independence nor cancellation of rounding errors is assumed.

## 4. Adjoint action and exact injections

For input data ||y||<=2049 on grid96, initialize z=0. Traverse j=4095 down to0: inject R^Ty_j/64, then apply the negative half-step if j>0. This gives the intended order of the exact sum above. The injection is exact on grid128: each input integer is shifted left26 bits (128−96−6). The final state is delivered on grid96 by truncating32 bits.

Every exact partial adjoint sum has norm at most

\[
\frac1{64}\sum_j\|y_j\|
\le\frac{\sqrt{4096}}{64}\|y\|\le2049.
\]

The same comparison with the exact isometric negative propagator gives at most E state error, and every computed state remains below2049+1<C. Injections add no rounding error. Final delivery contributes less than52*2^-96, hence

\[
\|\widetilde F^Ty-F^Ty\|\le E+52\,2^{-96}<2^{-68},\qquad\|y\|\le2049.
\]

This is a uniform absolute-domain bound; it is not inferred from a few unit vectors or a small duality residual. A forward result for state norm<=2048 has norm<2049, so the factored normal action has error<=2^-67. The constructed reference actions therefore supply the explicit oracle slots left open by PR313, for this precise model and arithmetic implementation.

## 5. Executable scope and checks

The C++ implementation uses arbitrary-precision GMP integer operations. The current build supplies minimal Linux64 GMP ABI declarations because development headers are absent; it is explicitly platform-bound. The runtime receipt records the GMP version and word size. No internal limbs are accessed. The source proof assumes the specified integer operations are correctly implemented; independent Python-bigint evaluation of40 reference terms and comparison of all final half-step output coordinates for both signs checks the actual backend path. This is not a claim of a portable, formally verified compiler or GMP implementation.

Two full4096 forward actions and one full4096 adjoint action exercise the actual2640-state source operator, not a rational proxy. An ordinary preparation and a scale128 near-domain preparation are used; the dense adjoint input approaches its declared domain. Their exact dyadic input/output hashes are retained. Full-size duality and scale consistency are checked against the proven error budgets; the delivered rounded actions are not claimed to be exactly linear or exactly transposes of one another.

Source-hash changes and out-of-domain inputs are rejected. Whole-half-step independent integer controls evaluate211200 reference term coordinates and compare all5280 compiled half-step output coordinates; the binary does not export intermediate terms. Separate same-team review independently reconstructs the source and bounds and exercises its own backend controls. Timed full-action replay hashes must match the original runs; timings and peak memory are empirical receipts, not universal bounds.

A separate two-step execution connects these real source actions to the unchanged PR313 Arb/dyadic decoder, using a normalized253952-coordinate input. It checks5280 whole-update coordinates at the full2640-state size. It is an integration test at N=2, not an N=8192 convergence test or an achieved accuracy gate.

The reference stores state vectors and one data vector; no full matrix F, F^TF or287-GiB Hankel is allocated. Standalone action runtimes do not certify a practical full-decoder runtime. The8192-step decoder requires16383 such forward/adjoint actions; the present reference method makes performance optimization a material next task.

## 6. What closes and what remains open

Closed in the mathematical reference scope: source-bound finite forward and adjoint implementations with absolute errors<2^-68 on the required domains; composed normal error<=2^-67; full-size action and two-step decoder integration checks. The PR313 full-space arithmetic theorem then applies to an eventual8192-step execution if its per-update Arb checks continue to pass.

Open: actual full8192-step decoder execution and performance, any separate optimized or floating implementation, and every physical/input premise of PR309. The illustrative X<=1,D<2^-50 observable-chain error implication remains conditional on those input premises. No six-ratio calibration, old Hankel-family bound, physical noise gate, fresh timing record or experimental correspondence is transferred.641 hidden components remain unrecovered.

Ledger v0.39/CRL-2; Development—no registry entry. O03 tolerances, Taylor degree and dyadic grids are protocol controls, not theory constants. External promotion review PENDING; Physical Promotion=0. Zero new frozen mathematical retractions; full-session ratio NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png unavailable/unused—please re-upload if needed. Notes/ASTER available unused.
