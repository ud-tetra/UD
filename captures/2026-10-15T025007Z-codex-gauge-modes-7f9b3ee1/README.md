# UD Gauge-reduced modes theorem v0.1

This is a conditional mathematics release for the candidate action in the preceding joint Hamiltonian v0.1. It does not select that action or a physical gauge group. Physical promotion 0; independent review pending.

Read the ten-page PDF. It provides the stationary family, explicit regular Abelian reduction, exact mode polynomial, all-positive-stiffness Jordan obstruction, higher-rank symplectic slice with residual stabilizer, and a separate nonlinear vacuum stability theorem.

Replay: `python3 verify_reduced_modes.py` with Python 3, SymPy, NumPy and SciPy. The code uses `mode_model.py`. Exact results, a rational constrained Jordan witness, and a numerical diagnostic are separate JSON receipts. A finite fixture check is not independent review.

PDF build: run `pdflatex -interaction=nonstopmode -halt-on-error UD_GAUGE_REDUCED_MODES_THEOREM_v0.1.tex` twice.

The reported unbounded tangent flow does not by itself prove nonlinear instability of the nonzero family. At rank greater than one, the slice still requires residual U(r-1) reduction. Curved/excited stationary branches are outside this classification.

Historical coefficient and governance attachments are provenance, not hidden sources of action coefficients. The missing image Gap2_FINAL_Finite_Genesis.png was not used. No experimental data were used.
