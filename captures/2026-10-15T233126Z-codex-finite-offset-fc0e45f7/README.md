# Finite-offset branch certification v0.1

DERIVED CONDITIONAL / COMPUTER-ASSISTED CONSTRUCTOR CERTIFICATE. Development lane, no registry entry. Independent review PENDING; physical promotion 0.

Read the theorem PDF/TeX and FINITE_OFFSET_CERTIFICATE_v0.1.json. The normalized sufficient interval is 0 < epsilon <= 1/100000, epsilon=kappa/(r*N)-k_star. This is not a maximal interval. All 26 labeled scalar branches continue over it. Stationary embeddings and readout bounds apply at each finite rank. Scalar stability and Morse indices are certified; full-rank finite-offset stability of the minima remains open. The finite soft-mode brackets fix a=N=r=1.

## Replay

Install Python, python-flint==0.9.0, NumPy, SciPy and SymPy. Run `python3 certify_finite_offset.py` in a copy of this release. Typical constructor replay was about 195 seconds. The 44-dimensional regularized equations, analytic Jacobian, parameter derivative, entire-function remainders and scaled Schur tests are supplied. CERTIFICATE_INPUTS contains rational centers. SECTOR_BASES contains exact rational symmetry projectors' bases; `python3 sector_basis.py` regenerates and checks them.

The three global interval boxes prove existence, uniqueness within their tubes and analytic continuation including the rescaled zero endpoint. All 1536 child boxes are contained in their global boxes. Configuration inertia is checked on every cell; 2048 spectral cut tests certify the stable radial and angular sectors. Directed rounding is carried by Arb; float eigenvectors only propose congruences that must pass strict interval Gershgorin tests. No floating residual is accepted as proof. The software arithmetic and implementation are trusted components, not a machine-formal proof or an independent implementation.

The rescaling uses X=sqrt(epsilon)*(Z*b+epsilon*Y*c), f=v+epsilon*s, lambda=-rho+epsilon*ell. Its intermediate b is different from the physical critical readout. All reported amplitude and noise bounds use h=b+epsilon*Gamma^-1*(CZ)^T*C*Y*c, with physical amplitude sqrt(epsilon)*h.

Geometry and critical basis are reconstructed from the frozen tetrahedral model. The action, coefficient ledger and governance are unchanged. The inherited quartic directed-integer certificate is replayed. The center inputs are roots proposed numerically and subsequently enclosed; proposals carry no authority before the strict interval tests pass.

No experimental data are analyzed. A physical action/readout dictionary, actual instrument calibration, sourced preparation and independent review remain required. Real-only data cannot recover overall phase sign. The unavailable source image Gap2_FINAL_Finite_Genesis.png was not used. Earlier captures are immutable; replay results should not be committed over them.
