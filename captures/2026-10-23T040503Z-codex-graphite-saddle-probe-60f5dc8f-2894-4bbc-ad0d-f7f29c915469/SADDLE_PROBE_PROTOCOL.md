# Source-matched off-line saddle probe

**Status: PROPOSED DFT, NOT RUN. Development only; no registry entry or physical promotion.** This probe tests the static two-dimensional PES used in the conventional friction baseline. It does not measure damping, kinetic sliding friction, or a UD residual.

## Geometry and calculation

The five `*.in` files reproduce the published 3.4022 Å, 30 Å vacuum, 28-carbon $(2,1)$ rigid bilayer input at line index 30 (14 lower and 14 upper atoms), with all original settings retained: Quantum ESPRESSO 7.3 source archive, vdW-DF3-opt1, ecutwfc/ecutrho 400/2000 Ry, Gaussian smearing 0.001 Ry, 14×14×1 k points, SCF threshold 1e-11 Ry. `center.in` is byte-identical to the archive member. Only upper-atom x/y coordinates change in the four other files. The scan tangent inferred from archive indices 29–31 is $(\sqrt3/2,1/2)$; the perpendicular unit vector is $n=(1/2,-\sqrt3/2)$. At $h=0.04,0.08$ Å, displace every upper atom by $\pm hn$ with z=8.4022 Å and all lower atoms fixed at z=5.0 Å. No relaxation or changes in cell, pseudopotential, k sampling or electronic settings are requested.

Source: [Lebedeva et al., arXiv:2511.01338](https://arxiv.org/abs/2511.01338), original [Zenodo 10.5281/zenodo.16318186](https://doi.org/10.5281/zenodo.16318186), `qe-21-vdw-df3-3.4022A-h30A.tar.gz`, SHA-256 `05e5e995d70ad83a98f8b534addb3dcff51ff3422c8f24dcba25453c3e76e228`; member `dir_30/struct.in` SHA-256 `ece677e20daaa3d7ca84143fa03c622c8ee949498350aefead6f359834517aba`. Each run needs its own copy of archive `dir_30/C.upf`, SHA-256 `a5b0fe8d6b63f703745b99d47e2dd47ed18efdb35a01ff410bc8e8d0af4e247f`, in its run directory because `pseudo_dir='.'`. The pseudopotential is referenced by digest, not repackaged in this capture. Run each input in an isolated fresh QE working directory to avoid shared `pwscf.save` state. Preserve output `pwscf.save/data-file-schema.xml` for the analysis. The old `struct.out` prints only eight decimals in Ry; that rounded value is insufficient for this small contrast.

## Frozen model forecast and interpretation

Set $U_1=0.0793396654$ μeV per upper atom from the earlier 37-point first-shell fit; $a=2.4660$ Å and $k_y=2\pi\sqrt7/(\sqrt3 a)=3.892021124$ Å⁻¹. For energies per upper atom, define $D(h)=E(+h)+E(-h)-2E(0)$ and $\beta=\sqrt3 k_yh$. On this normal through the index-30 saddle, $D_0=8U_1\sin^2(\beta/2)$ for the first shell $f=2\cos v\cos u+\cos2v$. The line-invisible symmetry term $F=(1-\cos(u-3v))(1-\cos(u+3v))(1-\cos2u)$ adds $2\varepsilon(1-\cos2\beta)(1+\cos\beta)^2$ to $D$. $\varepsilon=-0.2U_1$ is an illustrative counterexample, not a fitted material coefficient.

| h (Å) | First-shell $D_0$ (μeV/upper atom) | Illustrative $D_{-.2U_1}$ (μeV/upper atom) |
| ---: | ---: | ---: |
| 0.04 | +0.01146777 | −0.00590399 |
| 0.08 | +0.04504230 | −0.01274570 |

The infinitesimal first-shell transverse curvature is $6U_1k_y^2=+7.21094$ μeV Å⁻² per upper atom; this example gives $(6-9.6)U_1k_y^2=-4.32657$ μeV Å⁻². A measured negative $D$ at h=0.08 Å would directly show a lower off-line state at that displacement. Approximate the local curvature from $D(h)/h^2$ at both steps and extrapolate linearly against $h^2$, checking smaller h if needed. A positive $D$ at these finite steps does not mathematically establish positive infinitesimal curvature under arbitrary higher harmonics. Fitting an illustrative $\varepsilon$ from a single $D$ assumes precisely this one-term ansatz; do not label it a UD coefficient.

## Analysis and precision gate

Pass the **five new** XML outputs to `analyze_saddle_probe.py`:

```bash
python analyze_saddle_probe.py \
  --center center/pwscf.save/data-file-schema.xml \
  --minus-04 minus_0.04A/pwscf.save/data-file-schema.xml \
  --plus-04 plus_0.04A/pwscf.save/data-file-schema.xml \
  --minus-08 minus_0.08A/pwscf.save/data-file-schema.xml \
  --plus-08 plus_0.08A/pwscf.save/data-file-schema.xml
```

The parser checks the XML SCF convergence flag and reads Hartree `total_energy/etot`, converts a 28-atom cell energy difference to μeV per **14 upper atoms**, reports each symmetric contrast, a model-conditional epsilon fit and two-step curvature extrapolation. No output XML is present in this capture. If independent per-run standard uncertainty $\sigma_E$ is established, optional `--sigma-microev-atom` gives $\sigma_D=\sqrt6\sigma_E$; shared numerical errors require covariance analysis instead. At $\sigma_E=0.001$ μeV per upper atom, the $h=0.08$ example's negative contrast is 5.20σ from zero, while $h=0.04$ is only 2.41σ. These are *conditional detectability calculations*, not established DFT uncertainty. Check total-energy differences against tighter SCF, k mesh, cutoff and vacuum, plus independent repeats. Freeze a precision criterion before using outputs to alter the conventional PES. The two-step Hessian extrapolation reuses the center energy and has correlated statistical errors, even if individual calculations are independent.

The original archive is data only; `prepare_saddle_probe.py` reads and hashes it without executing its scripts. The exact line-invisible term and grid example in the previous capture remain a no-go on unique 2D inference from the single line. This off-line protocol can constrain that ambiguity; neither outcome alone identifies kinetic dissipation or a UD-specific force.
