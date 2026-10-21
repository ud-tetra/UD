# C30 independent action-certificate review plan

Freeze before actual2640-state action measurements/results. Review source construction and a fixed-point degree40 Taylor half-step, then complete4096-sample forward/adjoint actions. The full8192-step decoder and physical/input admission are out of scope.

1. Bind the intended signed weighted K, readout R, dimensions and inherited normK<5. Check H=2K so the half-step generator is H/4.
2. Derive exact rational Taylor tail and a uniform bound on every term-rounding error, including term recurrence and exact integer accumulation.
3. Propagate errors with the true skew propagator norm1 or polynomial norm<=1+tau; avoid a naive exp(time*normK) growth bound.
4. Treat input/output encoding,1/64 normalization, and adjoint injection rounding explicitly. Derive an adjoint norm bound using the complete data RMS/Euclidean norm, not an unsupported uniform per-time cap.
5. Distinguish exact source-bound all-input arithmetic bounds from finite runs/tests. Require independent audit of actual outputs and source hashes; no archived code execution or repo edits.
6. Actual full-decoder runtime, physical preparation/error inputs and acquisition remain HOLD. Development—no registry entry; external review PENDING; Physical Promotion=0.
