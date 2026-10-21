# C29 independent review plan

Freeze before decoder numerical budget evaluation. Review the fixed PR307 finite map, with norm<=1, positive singular lower s=61/27648, rank1999/kernel641. No actual matrix-free F/F-transpose oracle is yet validated.

1. Derive the residual Chebyshev polynomial and the stated three-term iterate recurrence, checking initialization, signs and degree/iteration indexing.
2. Separate ideal decoder conformance from perturbed recurrence. The ideal B_NF acts as zero on kerF and approximately identity on its orthogonal complement. Additive computational errors can contain hidden components and need a full-space stability proof.
3. Derive the exact forced-recurrence Green coefficient for every error insertion index, including the initial x1 and final update. Check any uniform bound at lambda0 as well as over the positive spectrum.
4. Verify the proposed N8192 ideal bias and gain using exact rational inequalities, without relying on a floating logarithm. Bound action and arithmetic errors only under explicitly supplied norm contracts and coefficient-accuracy conditions.
5. Provide exact small controls for wrong indices, omitted initialization/input errors, hidden accumulation, and decoder-vs-oracle distinction. Do not infer implementation conformance, acquisition admission or physical accuracy from an ideal polynomial theorem.
6. Keep supplied error magnitudes conditional; actual weighted F/F-transpose actions, coefficient implementation and input-domain evidence remain HOLD. No source/repo modification, estimator fit, full Hankel or physical promotion.
