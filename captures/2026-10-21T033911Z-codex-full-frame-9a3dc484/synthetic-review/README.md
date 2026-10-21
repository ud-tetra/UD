# Synthetic actual-CLI solver review

The unchanged `c33_solve.py` passed one explicitly synthetic 1999-by-2640 diagonal-frame test and four input-rejection tests. This is a finite record residual and lift check, with no admission of an actual UD source frame, no physical accuracy claim, and no external promotion authority.

The test plan and independent test source were frozen before generating fixture rows or invoking the CLI. The required source-frame status literal inside the fixture is a CLI schema requirement; the fixture is separately marked `synthetic_source_excluded` and never represents authenticated UD geometry.

The diagonal entries are exact powers of two from 1 through 2^-12 after the dyadic96 scale. The alternating signed right-hand sides use integer `floor(D_i^2/3)`. Iteration zero failed the frozen residual gate at approximately 2.371557733541425e-16. One refinement passed at approximately 1.316479000002771e-32. Neither the source nor the gates were modified.

Independent Python-integer arithmetic reproduced every final normal-equation residual, coefficient-to-lift truncation coordinate, and both reported exact squared errors. An exact rational diagonal-solution oracle gave a total lift error of approximately 2.9728975600477977e-28; the separately reported finite truncation error is approximately 2.972905026425522e-28. These are distinct errors. The rational oracle was also checked against a conservative squared triangle bound.

The missing mandatory trusted hash, wrong trusted hash, missing final row coverage, and corrupt first packed row all exited nonzero without emitting `FULL_SOLVE.json`. Their complete stdout, stderr, process status and output directories remain saved. Two one-unit mutations were detected by the independent exact oracle checks.

Application-data reads are limited to the unchanged solver and the synthetic fixture in this directory. The source interpreter and its ordinary installed dependencies are inherited runtime inputs. No actual UD frame was read or solved. CPU affinity was restricted to two cores; the solver's internal threadpool setting remained unchanged. Before/after hashes support the exclusive stable-input test premise, not a universal concurrent snapshot guarantee.

`FREEZE.json` binds the plan, test source, and solver. `REVIEW_RECEIPT.json` contains exact fractions and invocation records. `REVIEW_MANIFEST.json` is the execution-time artifact inventory; `FINAL_MANIFEST.json` additionally binds this report and that inventory. Physical promotion remains zero; external promotion review remains pending.
