# Exact PSD Gram bounds for the actual floating-estimator certificate

Development lane; physical promotion 0; independent review pending.

For a real residual R=N/2^b with exact integer N, let G=N^T N. Then

\[
 \|R\|_2^2=\lambda_{max}(G)/2^{2b}
 \le\frac{\min\{\operatorname{tr}G,\max_i\sum_j|G_{ij}|\}}{2^{2b}}.
\]

Proof: G is positive semidefinite, so its largest eigenvalue is bounded by its
trace. Every eigenvalue is bounded in modulus by the induced infinity norm,
which is the maximum absolute row sum. Taking the minimum preserves both upper
bounds. Trace is exactly the squared Frobenius norm, hence this refinement is
never worse. It is an upper bound on the operator norm, not an exact evaluation
of the largest eigenvalue. Integer Grams have only 161-by-161 entries here.

For Z minus the reference sketch, phase values are enclosed by the same 512-bit
validated arithmetic as PR186. The integer residual uses the same 2^-60 phase
approximants and 2^-127 total scale. The exact Gram upper bound is supplemented
by the identical, validated phase-approximation allowance. No floating phase
value is treated as exact transcendental arithmetic.

For Z-U B, the actual captured binary64 U and B are encoded exactly as integers
at a common dyadic scale. Its Gram uses the exact residual integer matrix;
there is no additional approximation of the saved floats.

Substitute these two upper bounds for e>=||Z-M||_2 and p>=||Z-UB||_2 in the
unchanged PR186 residual-to-phase theorem, reproduced in
PARENT_FLOATING_THEOREM.md. Every other bound and gate is unchanged, including
orthogonality/polar correction, shift residual, eigenvector inverse, actual
returned-eigenvalue residual, captured angle rounding, and strict separation.
The proof uses only upper bounds, so the substitution is valid. The verifier
records both the old Frobenius decision and the refined operator-bound decision
on exactly the same output arrays; a HOLD is not an estimator failure theorem.

Each accepted record has a conditional a posteriori certificate relative to the
pinned fitted reference. The discovery-order check is separately recorded.
Neither finite tests nor this refinement establish matching over the whole
2^-20 error ball, physical frequencies, independent review, acquisition
admission, hidden-state recovery, or convergence of the estimator on all inputs.
The 747-dimensional nominal dynamical kernel remains unchanged. The full
253952-by-151552 Hankel matrix is never allocated. Raw-to-sketch verification
and portable saved-sketch replay have distinct provenance.
