# Registry-dependent graphite potential audit v0.1

2026-10-21. Development — no registry entry. Constructor source/data checks; independent review pending. Physical promotion0. Extends PR334; no old result overwritten.

## Decision

CONDITIONAL BASELINE ADMITTED FOR IMPLEMENTATION, not validated for target friction. Use the full local-normal KC family plus a separately frozen intralayer model. Reproduce author-deposited commensurate PES results first. Do not treat scalar PES recovery as a full Hessian or as evidence of an extra UD dissipative nullspace.

## Implementation custody

LAMMPS documentation https://docs.lammps.org/stable/pair_kolmogorov_crespi_full.html identifies source commit8de817dd79bfe4525d5d39246a212d833e6dee07. Retrieved its potentials/CH_taper.KC and src/INTERLAYER/pair_kolmogorov_crespi_full.cpp through the GitHub connector; original text bytes saved. Source hashes and sizes in RESULTS.json. A concurrent direct stable-URL retrieval was replaced with pinned connector bytes before final verification; the final custody is the pinned commit. No imported executable ran. No LAMMPS simulation was performed.

Static source audit confirms conversion of energy coefficients by 1e-3*S into eV, local-normal derivatives in forces, and taper derivatives. C-C row has z0=3.416084Angstrom, delta=0.8447122Angstrom, lambda=2.9360584/Angstrom, S=1, and normal-neighbor cutoff2Angstrom. This cutoff is distinct from the global interaction cutoff. A16Angstrom tapered run is only a documented starting configuration, not a converged derivative certificate. Layer identity, intralayer separation and neighbor topology must remain explicit. Documentation requires an intralayer contribution; KC alone is not a full mechanical Hessian. Derivatives of normals must not be frozen for deformable modes. Current CH_taper parameters are a distinct sensitivity branch, not silently substituted into the older author's calculations.

Official taper header at the same commit defines T(s)=1-35s^4+84s^5-70s^6+20s^7 for0<=s<1, zero outside. Exact rational evaluation verifies derivatives1,2,3 vanish at both endpoints, along with T(0)=1,T(1)=0. This protects cutoff smoothness through third order for a fixed regular local-normal topology; neighbor changes/degenerate normals are separate gates. Source-code pattern checks are not a proof of the whole force implementation.

## Same-angle author data recovered

Minkin et al., Zenodo v1 DOI10.5281/zenodo.14283098, https://zenodo.org/records/14283098: KC plus second-generation Brenner calculations with two constraint families; includes exact target-angle archives. Retrieved data.zip and lammps_relax_bond.tar.gz, matching published MD5 values ea3fd75cd88e4c405c14b6cc89ce473c and04ef40c563d2d13c47d90e3afbbef747. Did not retrieve the519.4MB and724.9MB target archives, so their actual interlayer scripts/parameter bytes remain uninspected. The small bond archive contains202 REBO inputs and no active interlayer interaction in those inputs; commented KC commands are not evidence of active target setup. Do not infer the author's precise KC variant from the bond archive.

Parsed both PES tables without executing Mathematica. Each has22801 unique coordinate pairs. Author plotting source labels energies microeV/atom; coordinates Angstrom. Model grid ranges are exactly94.55074222microeV/atom for(2,1) and20.35016251microeV/atom for(3,1), in the precision of deposited decimal strings. These are sampled classical model energy ranges, not independently calculated continuum extrema, DFT energies, measured friction or a new blind test. Both static target PESs have now been exposed and cannot later be called held-out evidence. The whole source grid is insufficient to recover internal displacement eigenvectors or g.

Prior DFT source arXiv:2511.01338v1 remains a distinct model/constraint stratum. No direct numerical accuracy ratio is asserted without matching geometry, relaxation and conventions.

## Derivative contract — DERIVED under declared mechanics

Freeze E_theta(R,x) from a versioned intralayer+interlayer model in eV and Angstrom, exact supercell, periodic image sum, cutoff/taper, layer IDs, constraints, and normal-load or fixed-separation condition. Let internal Cartesian coordinates q be a fixed constrained basis excluding imposed collective sliding and rigid zero modes. Calculate K=E_qq and g=E_qx from forces, with central finite differences at multiple step sizes. Require symmetry, rigid translation controls, force-versus-energy consistency, normal-rotation covariance, cutoff convergence and positive constrained stiffness before K inverse. No numerical tolerance is invented here; it must be frozen from required downstream uncertainty before target scoring.

When separation z is minimized at fixed external load, include the load term in the appropriate potential and eliminate z consistently. For positive E_zz, the effective Hessian is the Schur complement E_ab-E_az E_zz^(-1)E_zb for a,b in(q,x). A fixed-z Hessian cannot be relabeled a constant-load Hessian. With eV/Angstrom^2 derivatives, multiply by16.02176634 to obtain N/m (exact from SI eV and Angstrom definitions). Full conservative K,g supply no damping Gamma. Only a separately sourced bath response can complete the dissipative test.

## UD disposition and next gate

This is conventional material-model qualification. It supplies no native UD map or extra symmetry constraint on loss. The next useful workload is to retrieve and inspect the two original target setup archives, freeze their historical implementation and constraints, and reproduce a small declared subset of already-exposed PES values before computing Hessians. Reproduction is a numerical qualification, not confirmatory friction scoring. A later CH_taper branch must remain a separately versioned model. Missing Gap2_FINAL_Finite_Genesis.png unused; historical v0.39 ledger and CRL-2 proposal do not set graphite parameters.

## Reproduction and preservation

Run python3 verify.py with the four source files named in RESULTS.json alongside it. Source URLs/hashes permit reacquisition; do not execute archived scripts. The checks cover archive custody, all grid rows, parameter conversion, source features and exact taper endpoints. No force/Hessian convergence, bath derivation, physical experiment or independent review is claimed. The compact repository capture stores source URLs, sizes and hashes, plus reacquisition code; third-party source files and archives remain local and are not mirrored in this capture. Reacquisition must match recorded hashes before replay. No modified LAMMPS implementation is distributed.
