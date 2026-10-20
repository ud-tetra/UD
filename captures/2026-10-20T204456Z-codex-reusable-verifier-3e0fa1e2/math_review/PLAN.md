# Frozen independent intake/fixture test plan

Development — no registry entry. Physical Promotion = 0. External promotion review PENDING.

The reviewer will inspect the new package and its manifest schema without importing any prior archived constructor, estimator or model. Schema adapters may be added after the package is available; expected fixture mathematics and negative-test categories are frozen here before exercising it. No fit will run.

Expected exact positive fixtures:

1. m=n=2, N=diag(2,0), bZ=0, singular=[2,0], right_transpose=I2, U=e1 supplied in exact once-only row chunks. At default cutoff q=1. Every norm is zero; full error bound0, exact cutoff count1 and leading1 condition1.
2. m=n=3, N=diag(4,2,0), bZ=0, singular=[4,2,0], right_transpose=I3, U=[e1,e2]. At default cutoff q=2. Every norm is zero; full error bound0, exact cutoff count2 and leading2 condition2.
3. If the declared generic int64 input contract allows its entire range, m=n=2, N=diag(-2^63,0), singular=[2^63,0], right_transpose=I2 and U=-e1. The dyadic factors are exact and every residual/Gram norm is zero. This fixture detects INT64_MIN absolute-value overflow; narrower explicit input policy would make a refusal a resource/completeness restriction rather than a false accepted certificate.

Expected negative intake categories, using only reviewer-controlled files:

- Incorrect manifest byte identity; duplicate or invalid file declarations.
- Wrong N dtype/shape; object/complex/nonfloat64 factor; NaN/Inf; malformed required array keys.
- Unsorted or negative singular list; exact cutoff equality; q=0 or q=n.
- Wrong full right-factor shape; retained U wrong column count or bad chunk row coverage (gap, overlap, incorrect declared extent).
- Relative path escape, absolute path if forbidden, symlink file or ancestor, and input/output overlap.
- Existing output path; attempted overwrite must leave existing sentinel bytes unchanged.
- Manifest/resource dimensions outside declared caps; oversized/truncated array header, handled under a bounded subprocess if needed.

Expected negative mathematical fixtures:

- Proposals/factors for a nonzero spectrum with zero projected N must not be certified.
- A deliberately wrong right or U factor must not produce an accepted certificate merely because its singular list is sorted.
- A bad discarded Gram factor or large tail must retain HOLD, without tuning accuracy, retrying precision or swapping norm routes.

Observed malformed-input rejection, clean program exception, explicit HOLD and process failure will be recorded distinctly. A crash or exception is not an accepted-output counterexample, and it is not a successful structured rejection unless the API contract defines it as such. Any material or minor finding will name the exact trigger, expected behavior, actual behavior and scientific impact. Parent-owned source files will not be edited by this reviewer.
