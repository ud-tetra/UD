# Prospective six-case source and execution review

Same-team, read-only source review before any new campaign records or fitted outputs. This is not an independent non-constructor audit and contains no observed outcome claims.

The six paired cases implement the adopted design: signed reverse/stationary; signed shuffle219237/channel cycle; signed shuffle219238/block1024 seed219301; R1/period2; R1R0/period4; transpose(R1R0)/directed spatial seed219302. Block noise draws37x8 channels before37x8 signs; spatial noise draws37 channels before37 signs. The denominator25 compositions are exact integer matrix products followed by one rounding, not two rounded passes.

The preparation transforms are orthogonal over the rationals and preserve preparation parity, hence the original two rate/jitter clock families before encoding. Their different origins are absorbed into modal coefficients. This preserves the unsketched source temporal span and total aggregate preparation energy before quantization; it does not prove fixed-sketch excitation, an individual preparation norm, or any learned-order result.

For maximum numerator row L1 L and denominator d, the scalar nominal source error is bounded by (L/d)*d0 + floor(d/2)/d * 2^-48. The per62-vector squared source error after a single unit coordinate perturbation is bounded by62*dnom^2+2*dnom*2^-48+2^-96. The implementation uses these exact fractions. Every new vector differs from its own frozen nominal by exactly one signed raw quantum. The fresh nominal is not asserted to lie in the old baseline ball.

The strengthened49*mx+25<2^63 guard covers weighted sums and the extra denominator-remainder excursion in signed floor arithmetic. Projection independently checks integer partial-sum range and exact float representability. Invalid numerical execution is an explicit retained HOLD. In the current driver, a previously failed projection is not repeated: the saved projectionNone causes N,p=(None,None), and verify_one exits on the execution HOLD before inspecting N.

All six raw hashes and complete scalar difference receipts are generated before DATA_FREEZE and before the first new fit. Each fit requires exact equality of its regenerated receipt to the frozen row. A second raw regeneration supplies saved-output verification. Full replay checks saved witnesses and regenerates raw/projection receipts without a new estimator call. Transient raw deletion is restricted to reproducible temporary files, and outcomes are neither selected nor retried.

The measured source-frame route retains old Gram, normal, raw-frame and shift caps. The learned cutoff is2^-24, with209 not forced. Exact sketch cutoff, measured frame/shift, saved phase witness and finite emitted-list matching are separate gates. A learned209 count is not a full321-factor SVD certificate or a native1893 Hankel rank certificate. Any eventual pass is scoped to saved finite outputs; there is no uniform future floating convergence, SI timing, physical-data or physical-promotion claim.

Two findings were resolved before this receipt: the int64 remainder headroom above, and replay of a failed projection above. No remaining material defect was found in the source-domain, record recipe, frozen regeneration or HOLD retention paths inspected. Deep phase/cutoff proof review is a separate review responsibility.

The execution launcher must retain OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1 before Python starts, as prescribed: driver imports records/NumPy before estimator sets these variables. The estimator-local assignment alone would not ensure pre-import thread configuration. This is a runtime reproducibility condition, not an inferred mathematical certificate.

No new raw records, transforms, controls or estimators were executed for this review. Python source syntax was parsed without module import. Exact reviewed bytes are recorded in FINAL_CODE_REVIEW.json.
