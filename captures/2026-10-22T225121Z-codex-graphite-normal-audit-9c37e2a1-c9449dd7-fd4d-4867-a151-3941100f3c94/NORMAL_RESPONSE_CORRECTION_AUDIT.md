# KC normal-response scope correction

Status: EXACT derivative identity for an explicitly chosen normal field; NUMERICAL cutoff-convention sensitivity; OPEN full material Hessian, bath damping and friction residual. Physical promotion 0.

The v16 atom-height reconstruction used the flat-layer SI potential with transverse squared distance equal to lateral squared distance even after *individual* upper-atom height displacements. That freezes the local normals. The original KC potential instead defines transverse distance from the local atomic normal. At a flat configuration, differentiation with respect to upper height gives the additional term in manuscript Eq. (24c). Thus v16’s 97.5921% squared-norm projection, 15.5176% norm residual and seven coefficient products apply only to the frozen-normal continuation. No numerical full-KC projection is asserted.

The exact representation count (eight C3-equivariant real maps from 14 scalar heights to the lateral plane; six in the seven-orbit family) is unchanged. The full Hessian could have a different projection. A full-normal test needs a declared local or semilocal normal formula, periodic neighbor heights, intralayer stiffness and validated lateral/height derivatives. Static cross-Hessian alone cannot identify a dynamic damping kernel or measured friction.

The cutoff check adds A(z0/Rc)^6 to every retained pair in the prior 16 Å pair enumeration. The grid’s raw energy origin is not established. The constant pair shift reduces the mean difference from -0.500845 to -0.252897 meV/atom but *increases* the centered RMS from 1.29210 to 1.38895 μeV/atom. Thus a matching mean alone would be inconclusive and this variant does not reproduce the spatial archive PES. Replay: `python3 audit_cutoff_shift.py /path/to/SHA-checked-public-archive.zip`.

Source scope: Kolmogorov and Crespi PRB 71, 235415 (2005), DOI 10.1103/PhysRevB.71.235415; LAMMPS official `kolmogorov/crespi/z` and `kolmogorov/crespi/full` manuals; Minkin et al. PRB 108, 085411 (2023) SI Eq S1/Table S1; 2023 public PES archive DOI 10.17632/svnpzbjc3t.1. No 2026 experiment curve or independent material damping supplied.
