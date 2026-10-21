# Native104 action arithmetic review

The admitted model is the identical pinned C30 sparse H=2K, so H/4=K/2, with operator header128 retained as a source-format field. Computation uses104 fractional bits and external data96 bits. The source channel proof gives ||K||<5; max row24 alone does not prove this skew spectral bound.

Let r0=52*2^-104. Dividing a vector of integer accumulators by4k toward zero introduces norm error<r0. With alpha=5/2 the first three Taylor-term error bounds are r0,9r0/4,23r0/8. For k>=4 the multiplier alpha/k<=5/8 preserves the upper bound3r0. Thus the sum of40 term errors<120r0=6240*2^-104. The exact term coefficient maximum is25/8<4, and the positive coefficient sum through40 is<13.

For any halfstep input norm<=4096, each computed term norm<4*4096+3r0. Each partial sparse row sum is bounded by the total absolute row sum24 times the maximum term coordinate. At integer scale104 this is<2^123. Each partial accumulated polynomial sum is bounded by13*4096+120r0, hence integer magnitude<2^121. Both are far inside signed128.

The implementation provides additional runtime guards: every current and divided-next term coordinate has absolute value<2^119. For syntactically admitted row-max24 sources, even before invoking the sharper source proof, each row accumulator is<24*2^119<2^124. At most41 guarded terms yield partial output sums<41*2^119<2^125. Guards therefore do not themselves need a possibly-overflowing intermediate computation. The admitted exact model never reaches their thresholds.

The split row loop is exact: z is the signed sum of one copy of each selected term, extra the signed sum for coefficient magnitude3, and2z+extra equals the original signed coefficient2/3 row product. Negative shifts are avoided: multiplication by a positive power of two implements upscaling; signed division by a positive power implements downscaling toward zero. External integers are parsed in an unsigned accumulator capped at2^112; exact GMP norm validation precedes scaling. The admitted2048/2049 domains are much smaller. Decimal formatting also avoids negating the signed minimum.

Let tau=((5/2)^41/41!)/(1-5/84). A halfstep has error<=tau*4096+120r0. The exact exp(+-K/2) is an isometry, so4096 steps accumulate at most E=4096*(tau*4096+120r0). Exact forward states have norm<=2048, normalized adjoint prefixes<=2049; E<1 closes the4096 state-cap bootstrap. Each round error is compared at its actual computed input, so no repeated exp(5/2) amplification is introduced.

The exact scaling exponents are8 for input96->104,14 for normalized forward104->96,2 for normalized adjoint96->104 injections and8 for final adjoint104->96. Thus whole forward error<=E+504*2^-96 and adjoint error<=E+52*2^-96. Both are<2^-79, and therefore meet2^-68. The normal composition meets2^-67 using true ||F^T||<=1 and the adjoint2049 data domain.

These are sufficient bounds for the source-pinned algorithm under exact native-integer semantics, the stated platform/compiler/GMP ABI trust, correct build bindings and stable intended files. They do not establish universal malformed-input safety, race-free snapshots, exact linearity of rounded actions, hidden-state recovery, full8192 execution or physical correspondence. The raw operator reader is not the authority for source admissibility; source/executable binding is essential.
