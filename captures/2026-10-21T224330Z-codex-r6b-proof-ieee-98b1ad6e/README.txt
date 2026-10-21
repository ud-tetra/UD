R6b exact spectral proof: independent-review submission
Benjamin W. Mayes, October 21, 2026. Prepared with AI assistance.

The PDF is the mathematical manuscript. It uses the official IEEEtran journal class, two columns, 10-point body text, and A4 paper. IEEEtran.cls is redistributed unchanged with its embedded license. This is a manuscript for review, not a statement of IEEE publication or peer-review acceptance.

FILES
R6b_Exact_Spectral_Proof.pdf: seven-page proof manuscript.
R6b_Exact_Spectral_Proof.tex: editable LaTeX source.
IEEEtran.cls: unchanged IEEEtran 1.8b class from the CTAN MIT mirror.
verify_exact.py: exact rational source-model verification, no third-party dependencies.
EXACT_CERTIFICATE.json: rational root/profile/weight intervals and exact embedding checks.
verify_stored.py: exact stored-byte eigenvalue and solver-error audit; requires NumPy.
NUMERICAL_PAYLOAD.npz: immutable original matrix/eigenpair payload, loaded without pickle.
STORED_MATRIX_CERTIFICATE.json: module-wise Rayleigh/Temple intervals and solver-return bounds.
SHA256SUMS.txt: file-byte checksums for the distribution.

VERIFY
Use Python 3. Both programs are supplied in readable source and may be inspected before running.
  python3 verify_exact.py
  python3 verify_stored.py
The second program checks the fixed payload SHA-256 before reading its arrays. It requires NumPy; the checked environment used CPython 3.12.14 and NumPy 2.3.5. No Git, network access, SciPy or SymPy is needed for these two verifiers. Programs regenerate their corresponding certificate JSON in the same directory.

BUILD
Use a LaTeX installation providing amsmath, amssymb, amsthm, bm, booktabs, array, xurl, balance and hyperref.
  pdflatex -interaction=nonstopmode -halt-on-error R6b_Exact_Spectral_Proof.tex
  pdflatex -interaction=nonstopmode -halt-on-error R6b_Exact_Spectral_Proof.tex
The bundled IEEEtran.cls is sufficient for the document class. PDF creation timestamps may change on rebuilding.

REVIEW FOCUS
1. Check the address and coefficient assumptions against the explicitly stated model.
2. Check the component partition and orthogonal Theta projector decomposition.
3. Check the codimension-one lower bound and the negative Rayleigh trial.
4. Check the two-coordinate and weighted six-coordinate intertwiners.
5. Check negative-root isolation and outward interval propagation, including all denominators.
6. Check the weighted pairwise-variance formula and strict nonuniformity proof.
7. Check that each Temple bound uses the second eigenvalue of its own component.
8. Check the separation between source error, stored-matrix error and solver reporting error.

The constants, edge law and site metric are hypotheses. No particle identification or physical unit map is inferred. The manuscript and this supplement contain mathematical and reproducibility material only.
