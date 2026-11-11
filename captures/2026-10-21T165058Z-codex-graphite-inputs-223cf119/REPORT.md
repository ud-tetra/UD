# Graphite independent-input audit v0.1

2026-10-21. Development — no registry entry. Physical promotion 0. Constructor source audit and numerical arithmetic only; independent review pending. Extends PR334's registry calculation without altering prior evidence.

## Result

PARTIAL INPUT RECOVERY. Published work supplies an independently parameterized approximate substrate damping route. It does not yet supply the complete angle-specific mixed Hessian, mode eigenvectors and bath response for aligned,(2,1),(3,1) contacts. No quantitative target friction or UD protected-sector prediction is claimed. Search was focused, not an exhaustive claim of dataset absence.

## Source register and applicability

1. Wang, Ma and Tosatti, arXiv:2306.00205v2 (15 December 2023), https://arxiv.org/html/2306.00205v2; Journal of the Mechanics and Physics of Solids 180,105396, DOI10.1016/j.jmps.2023.105396. Full HTML including SI inspected. Sections4,6.2 and SI II-III give a graphite bath estimate from force constants and Debye response; approximately 0.05 ps^-1 is analytically estimated, about0.02 ps^-1 from its anisotropic alternative. The reference simulation comparison suggests about0.1 ps^-1 for their example. These are distinct model estimates, not uncertainty endpoints. Section2 Eq1 is qualified for relatively small twists; the6degree prototype is not an established exact21.8degree or32.2degree commensurate calculation. High-temperature thermal fluctuation coefficient c2 is extracted from simulation (SI IV); a wholesale parameter-free characterization would omit this calibration and the stated approximation error. The paper is a conventional baseline, not evidence for UD novelty.

2. Lu et al., arXiv:2207.04965v3 (10 May2023), https://arxiv.org/abs/2207.04965v3; DOI10.1103/PhysRevB.106.144305. Abstract/version record inspected, not complete implementation or IFC arrays. Configuration-space DFT force-constant method targets small twists; v3 appends an erratum. Applicability to our large-angle small commensurate cells remains unverified. It supplies a possible method, not recovered target matrices.

3. Wu et al., Nature Communications5,5309(2014), DOI10.1038/ncomms6309, https://www.nature.com/articles/ncomms6309. Publisher abstract and figure index inspected; full article paywalled on retrieval. Twisted multilayer shear spectra constrain interlayer coupling. No full same-geometry registry-dependent Hessian or damping matrix recovered from inspected content.

4. Cong and Yu, Nature Communications5,4709(2014), DOI10.1038/ncomms5709, https://www.nature.com/articles/ncomms5709. Publisher abstract/figure index inspected. Polarization/temperature Raman study addresses shear symmetry and electron-phonon effects. No transferable full damping matrix acquired.

5. Dai et al., Science Advances11,eadu2880(28 May2025), DOI10.1126/sciadv.adu2880, https://pmc.ncbi.nlm.nih.gov/articles/PMC12118635/. Main article retrieved through Firecrawl after direct web retrieval encountered a browser challenge; supplementary PDF linked but not inspected. AFM and time-resolved CARS relate layer-dependent friction to breathing-related LOZO-prime dynamics. This probe-on-layer geometry and combination-mode decay do not identify the target twisted homointerface bath. Numerical figure lifetimes were not digitized or imported. No raw matrices acquired.

Prior source arXiv:2511.01338v1 section2 remains the exact geometric/PES baseline; it does not supply the dissipative response required by the proposed test. Supplied UD ledger v0.39 and CRL-2 proposal remain context, not graphite force constants. Unavailable Gap2_FINAL_Finite_Genesis.png unused.

## Independent damping arithmetic — NUMERICAL

Source Eq24 is r_alpha approximately (3pi/(2 omega_D^3)) |Phi12^(alpha alpha)|^2/m^2. Taking its Phi_zz=2.7N/m and omega_D=1.2e14rad/s and a declared carbon12 mass convention gives r_z approximately0.0501ps^-1 (exact output in RESULTS.json). This reproduces the published order without using friction targets. It is not a precision bound, measured lifetime, target-angle result or friction prediction.

Dimensional control: this expression has units s^-1. In our Cartesian equation M qddot+Gamma qdot+Kq=f, Gamma has units kg/s. For a per-atom scalar bath Gamma=m r, not r. The source's displayed Eq15 omits an explicit mass factor while its numerical damping is quoted in inverse time; our import uses the dimensional rate interpretation and preserves the source convention issue rather than equating the two objects. A full implementation must check its thermostat convention.

For qddot+r qdot+omega0^2q=0 in the weakly damped limit, amplitude decays at r/2 and energy envelope at r. A Raman coherence time T2, population lifetime T1 and phenomenological energy-loss time cannot be interchanged; pure dephasing and optical selection can matter. Even a correctly identified scalar rate determines neither off-diagonal damping nor coupling to Raman-dark modes. No conversion of the cited CARS data into Gamma was performed.

## Gate decision and revised hypothesis

The idea that low friction follows from weak overlap with lossy phonons is already part of conventional dynamics. The UD candidate can contribute only if its source law independently restricts the interface coupling or bath operator and predicts additional outcomes. No such graphite constraint is currently derived.

Recovered: exact crystallographic filtering (prior capture); approximate bulk substrate force constant and analytic bath route; relevant measurement methods. Missing: same-geometry relaxed U(x,q,z), mixed derivative g=U_qx and constrained K=U_qq along sliding; mode/bath spectral matrices; boundary/contact/load/temperature contract; and an independent UD map selecting an extra constraint. A few phonon frequencies determine eigenvalues only, not eigenvectors or g.

Recommended next work: implement a frozen conventional atomistic energy and a surface-response bath for the two exact commensurate supercells, then derive the proposed UD constraint before friction-target access. Use one material parameter source across angles; benchmark forces and Hessians independently. Do not use a fitted damping per angle. A mode-resolved spectral bath may be necessary if the Markov approximation fails. This conventional calculation is a baseline qualification, not a confirmation of UD. If no distinct constraint is available, end the extra-protection claim and retain only the conventional explanation.

## Verification

verify.py uses standard-library Fraction for decimal inputs and binary64 pi for the numerical source formula. It checks the reported rate's order and explicit factor2 comparison; no false exact-material status. No DFT or MD executed. Capture-only repository verification is recorded in PR discussion; full historical repository remains outside the sparse checkout. Source content is summarized rather than redistributed.
