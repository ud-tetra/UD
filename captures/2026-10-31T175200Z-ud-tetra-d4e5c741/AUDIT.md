# UD 3+1 simplex-slab / redshift / prism-observer bridge audit v0.1

**Date**: 2026-10-31. **Claim:** EXACT small-complex chain identities, CONDITIONAL standard-cosmology redshift and mode mixing, NUMERICAL toy stencil, OPEN native photon/metric/instrument bridge. **Physical promotion**: 0. **Status**: DEVELOPMENT_NO_REGISTRY_PROMOTION, external reviewer pending.

## EXACT simplex and 3+1 history construction
A filled d-simplex has f_k=binomial(d+1,k+1) and total 2^(d+1)-1 simplices. Exact signed incidence checks for d=0..4:
- d0: (1), chain dim1, skew characteristic lambda.
- d1: (2,1), chain dim3, lambda(lambda²+2).
- d2: (3,3,1), chain dim7, lambda(lambda²+3)^3.
- d3: (4,6,4,1), chain dim15, lambda(lambda²+4)^7.
- d4: (5,10,10,5,1), chain dim31, lambda(lambda²+5)^15.
All tested boundary compositions vanish; these frequencies belong to the unit simplicial **internal** generator, not physical Hz.

A *single* 4-simplex has five tetrahedral facets but no intrinsic future time. To record persistence of a spatial tetrahedron across one indexed interval, triangulate Delta3×[0,1] using past vertices vi and next-slice wi:
 sigma0=[v0,w0,w1,w2,w3]
 sigma1=[v0,v1,w1,w2,w3]
 sigma2=[v0,v1,v2,w2,w3]
 sigma3=[v0,v1,v2,v3,w3].
The oriented chain S4=sigma0-sigma1+sigma2-sigma3 contains FOUR pentachora on eight vertices. EXACT: three interior tetrahedral facets cancel, fourteen tetrahedral facets remain on the boundary (one past, one future, twelve lateral), ∂3∂4S4=0. Two independent algorithms checked the boundary. Boundary-of-boundary cancellation does not prove material/burden conservation; a source-current update law and a clock still must be supplied.

## REDSHIFT as a conditional temporal/causal test
External FLRW assumptions (NOT derived from a 4-simplex): comoving photons in an isotropically scaled spatial metric, local rest wavelengths constant. Then 1+z=a_obs/a_em, ν_obs/ν_em=a_em/a_obs; log shifts telescope exactly: Δlnν=-Δlna. A discrete a_n can reproduce this **given** a_n, but computing a_n from native UD dynamics, physical duration, the Lorentzian metric and photon transport remains OPEN.

Observer-time redshift drift, for comoving source and standard FLRW:
 dz/dt_obs = (1+z)H0 - H(z).
This is a stronger temporal discriminator than one spectral-line ratio. Redshift z, primordial spectral tilt n_s, dimensionless alpha_EM, and laboratory mass ratios are distinct observable types.

## PRISM and chromatic null
Stationary prism/dielectric interfaces preserve optical frequency; n(ν) determines wavelength, phase velocity and Snell deflection. Pure standard cosmological redshift is achromatic:
 D_ij=[λ_i(obs)/λ_i(rest)]/[λ_j(obs)/λ_j(rest)]-1=0 for correctly paired lines under the declared null.
A nonzero D_ij could be a source-line change, chromatic native propagation, or instrument offset; a prism does NOT imply cosmological redshift.

Exact synthetic example only: λ_rest in {400,500,600} nm; a_obs/a_em=7/4; add fictitious detector wavelength offset 1/20 nm. Then inferred z values are 0.750125, 0.750100, 0.75008333, and z400-z600=1/24000; true cosmological z=3/4 for all. Hence a reporting discrepancy can be produced by the instrument map without new cosmology. This says NOTHING about actual CODATA alpha or any laboratory instrument.

## SMALL CORRECTIONS and scope no-go
For a declared two-mode symmetric H=[[0,g],[g,Delta]], Delta>0, the lower eigenvalue is (Delta-sqrt(Delta²+4g²))/2 = -g²/Delta + O(g^4/Delta^3). Second-order small response is lawful if g, Delta and readout are source-derived, not selected from target.

A centered 1D wave spatial stencil (continuous time), N cells per wavelength, has ω_h/ω=sin(π/N)/(π/N)=1-π²/(6N²)+O(N^-4). Numeric example: N32=-0.1605607%, N64=-0.0401547%, N128=-0.0100396%. This vanishes under numerical refinement and MUST NOT be promoted as a physical lattice prediction.

Current UD history-comparison v0.14 (2026-10-14) proves no spontaneous detail from a purely coarse state when the full generator reduces both subspaces. Under exact inheritance with no forcing, a dimensional lift produces ZERO dynamical new-mode excitation. Current metric selection v0.12 and refinement tower v0.13 prove exact conditional readout/normalization nonuniqueness: the same retained state can yield normalized coarse fractions 1/3 and 1/5 under different detail-calibration contracts while absolute coarse stock is unchanged. These are mathematical observations, NOT measurement biases.

## NEXT GATED experiment
Specify state space, 3D slices, four-pentachoron slab, spacetime causal metric, transport generator, detail excitation/coupling, initial/boundary conditions, conserved source and lateral receipts, detector transfer and uncertainty covariance; derive scale factors and line-response kernel without target exposure. Null: g=0, exact achromatic redshift and D_ij=0. Controls: mesh refinement independent from physical length, reversed orientation, alternative triangulations, known detector offsets and source-line changes. Predict redshift drift and chromatic double ratios, then score independent measured lines/epochs/instruments against preregistered limits. Physical promotion is blocked until independent evidence.

## Source links
- Public UD Math (Paper I), 2026: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/mathematics/
- UD Metric Selection v0.12 §2–6: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/metric-selection-v0.1/UD_METRIC_OBSERVABLE_SELECTION_GATE_v0.1.md
- UD Refinement Tower v0.13 §2–5: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/refinement-tower-v0.1/UD_REFINEMENT_TOWER_COHERENCE_v0.1.md
- UD History Comparison v0.14 §3–6: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/history-comparison-v0.1/UD_REFINEMENT_HISTORY_AND_DETAIL_SOURCE_v0.1.md
- Uploaded coefficient ledger v0.39 (2026-08-22): F01–F05, C02/C06.
- NASA cosmological redshift: https://science.nasa.gov/mission/hubble/science/science-behind-the-discoveries/hubble-cosmological-redshift/
- Prism dispersion: https://openstax.org/books/college-physics/pages/25-5-dispersion-the-rainbow-and-prisms
- DESI DR2: https://data.desi.lbl.gov/doc/papers/dr2/
- NIST astrocomb: https://www.nist.gov/programs-projects/frequency-comb-calibration-astronomical-spectrographs
- DESI pilot calibration warning: https://www.iaa.es/publications/constraints-spacetime-variation-fine-structure-constant-using-desi-emission-line
- Full LOCAL downloadable package UD_4D_REDSHIFT_TRANSPORT_AUDIT_v0.1.zip SHA256 18bc04dd0ec50e55244092fa367d73a0e3b69380706cc71776ee3794ebdcef6e. This GitHub text capture does NOT mirror entire local ZIP and cannot imply missing binary files were published.

CONCLUSION: Four pentachora exactly represent a tetrahedral event slab. Redshift and prism impose contrasting observational constraints. An additional native transport/metric/source and instrument correspondence is required before any small physical correction claim. No physical promotion, no new dynamics adopted.
