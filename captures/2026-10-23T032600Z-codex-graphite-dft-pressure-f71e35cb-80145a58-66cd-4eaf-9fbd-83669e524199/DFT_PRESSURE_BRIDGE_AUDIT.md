# Public vdW-DF3 separation scan: conditional pressure bridge

**23 October 2026. Status: NUMERICAL replay of a published conventional material calculation; DERIVED conditional static response; OPEN kinetic friction and UD residual.**

## Source and method

Lebedeva *et al.*, arXiv:2511.01338, data availability statement, links the original Quantum ESPRESSO data to [Zenodo record 16318186](https://zenodo.org/records/16318186), DOI [10.5281/zenodo.16318186](https://doi.org/10.5281/zenodo.16318186). Download only these four public files to a source directory (they are not checked into the UD repository): `qe-21-vdw-df3-aa.tar.gz`, `qe-21-vdw-df3-ab.tar.gz`, `qe-21-vdw-df3-sp.tar.gz`, `qe-21-vdw-df3-opt-dist.tar.gz`. The included `replay_dft_pressure.py` SHA-256 checks each archive, reads `struct.in`, a `JOB DONE` marker in `struct.out`, and XML `total_energy/etot`. It **never runs scripts from the archives**. The 31 AA, AB and saddle configurations span 3.20–3.80 Å in 0.02 Å steps. The separate fine AB normal-energy scan has 21 complete points at 3.401–3.403 Å in 0.0001 Å steps; overlapping coarse scans in the same archive are deliberately ignored. Each rigid 30 Å vacuum cell has 28 atoms, 14 per layer. XML total energies are in Hartree; conversion to energy **per upper atom** divides by 14. A paired AB input at 3.40 Å and the normal scan input agree geometrically; their energy difference is below 0.0001 μeV per upper atom. Inputs specify vdW-DF3-opt1, 14×14×1 k grid and 400 Ry wavefunction cutoff.

Command: `python replay_dft_pressure.py --source-dir DIRECTORY --output-dir OUTPUT`. It writes `DFT_PRESSURE_RESULTS.json` and `DFT_REGISTRY_SCAN.csv`; the results bundled in this capture come from the SHA-checked source archives. Published Table 2 gives a corrugation of approximately 0.347 μeV per atom at its optimized rigid spacing 3.4022 Å, consistent with the local fit below. This is numerical reuse of those authors' calculations, not an independent DFT study.

## Separation derivative and normal response

Let (d) be the rigid layer separation, (e_{
m AB}(d)) the energy per upper atom, and (Delta(d)=e_{
m AA}-e_{
m AB}). For the type-II first-harmonic branch, (U_1=(2/9)Delta>0); ideal static shear strength (	au\propto U_1), while rigid relative shear frequency (	ilde\nu\propto\sqrt{U_1}) at fixed in-plane lattice constant. Five-point quadratic fitting over (d=3.36,3.38,3.40,3.42,3.44) Å, evaluated at (d_0=3.4022) Å, yields

\[
 \Delta(d_0)=0.34351\;\mu\mathrm{eV/atom},\quad
 \Delta'(d_0)=-4.74370\;\mu\mathrm{eV/(atom\,\mathring A)},\quad
 \partial_d\ln U_1=-13.8094\;\mathring A^{-1}.
\]

The 17-point quadratic fit to the *fine* AB energy within ±0.0008 Å gives (k_z=e''_{\rm AB}(d_0)=146.15\) meV per upper atom per Å². Different local fitting windows and degrees in the accompanying JSON yield 140.25–150.19 in the selected sensitivity set; the differential corrugation log derivative ranges from −13.46 to −14.29 Å⁻¹. These spreads are **fit sensitivity**, not a statistical or DFT functional error bar. Strong cancellation of total DFT energies makes extrapolation outside this small neighborhood unsafe. The registry scan also gives Δ(3.54 Å)=+0.00653 and Δ(3.56 Å)=−0.01963 μeV per atom, signaling a registry inversion near 3.5 Å; the first-harmonic type-II log formula does not extend through that crossing.

For compression-positive external uniform pressure (P), ideal in-plane atomic area (A_a=\sqrt3a^2/4=2.63322\) Å² at (a=2.4660\) Å and per-atom enthalpy (h=e_{\rm AB}(d)+PA_ad), stationarity gives (e'_{\rm AB}(d)+PA_a=0). Hence

\[
 {dd\over dP}=-{A_a\over k_z}
 =-1.12457\times10^{-4}\;\mathring A/\mathrm{MPa},\quad
 {d\ln\tau\over dP}={\Delta'\over\Delta}{dd\over dP}
 =+1.55297\times10^{-3}\;\mathrm{MPa}^{-1},\quad
 {d\ln\tilde\nu\over dP}=+7.76487\times10^{-4}\;\mathrm{MPa}^{-1}.
\]

The pressure conversion is (A_a(1\;\mathrm{MPa})=0.01643525\) meV Å⁻¹ per upper atom. Cross-combining the listed fit choices gives an approximate **1.47–1.68×10⁻³ MPa⁻¹** sensitivity interval for the first slope. Around the published theoretical τ≈1.39×10⁴ Pa, its nominal derivative is about +22 Pa per MPa *inside the same ideal rigid model*. It is not a claim about the 2026 sliding-force experiment, a resolved contact pressure, or a larger pressure excursion. In-plane strain, vertical relaxation, higher PES harmonics, finite size, domain walls, thermal effects and changes to the sampled registry each require a new calculation. This finite positive local slope is compatible with a sliding force that appears nearly load independent, since these are different observables.

## UD identifiability boundary

The two harmonic translation coordinates are an invertible encoding of two ordinary lateral coordinates. A scalar measured low-frequency dissipative tensor alone cannot identify this encoding as a new force law. In fact any symmetric positive semidefinite target \(\Gamma\) can be represented by an ordinary passive internal bath in equation (5): take (K=D=I) and (C=\Gamma^{1/2}), so (CK^{-1}DK^{-1}C^T=\Gamma). A seven-orbit source contrast is therefore a **candidate selection rule** only after its source weights and normalization are defined independently and frozen, with a distinct signed force residual tested on held-out paired-angle data. A flexible conventional bath can otherwise reproduce the same port response. The present DFT data constrain static separation and corrugation; they provide neither damping (D), kinetic contact force, nor a UD-specific coefficient. No physical promotion follows.
