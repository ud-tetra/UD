# Three-neighbor KC local-normal coupling audit

Status: EXACT_CONDITIONAL linear normal response; NUMERICAL_CONVENTIONAL 2x14 mixed Hessian; development, no registry entry; physical promotion 0.

At every upper honeycomb atom, define a local normal by averaging cyclic normalized cross products of the three nearest-neighbor bond vectors (1.42 Å), then normalize the average. Upper displacements share the periodic 14-atom coincidence cell; the lower sheet stays rigid. This selects one original-KC local-normal rule. It does not include semilocal normals, intralayer elasticity, any normal bath stiffness, dissipative rate or kinetic friction.

The first-order normal tilt is -2/(3b²) times the neighbor displacement-weighted bond-vector sum. Its central-atom height contribution cancels. Each of all 42 site-neighbor normal finite differences agrees with this expression within 1.1e-11 inverse Å. An independent nonlinear energy construction reproduces all 14 height derivatives at two lateral positions within 1.5e-9 meV/Å per mean upper atom and the mixed 2x14 energy derivative within 2.94e-7 meV/Å² per mean upper atom.

At the 16 Å pair cutoff and 1e-4 Å lateral step, frozen-normal matrix Frobenius norm 15.88102 meV/Å² per atom, seven-orbit norm residual 0.1551756, explained squared norm 97.59205%. Three-neighbor local-normal matrix norm 20.90902, residual 0.2738055, explained squared norm 92.50305%. The normal-rotation difference has norm 6.40387, or 40.324% of frozen matrix norm. Symmetry selects the same offset 2: C3 defect 0.001471 versus >1.5269 at six alternate cyclic offsets. Normal terms are not a small correction to the source projection.

The seven-orbit map span has rank six; the exact C3-allowed map space has dimension eight, independent of this constitutive choice. Local three-neighbor normal rules in the full KC setting should not be conflated with the archived source run: the flat-layer SI formula does not identify its off-plane normal implementation. Nor is the finite 14-upper-atom plus truncated lower-patch reconstruction an exact reproduction of the deposited PES; its frozen-normal centered RMS mismatch was previously 1.292 μeV/atom. The 14/16/18 Å and 1e-3/1e-4/1e-5 Å sensitivities test this implementation, not a physical error bar. Other normal prescriptions and force fields could change the result.

Replay `python3 derive_three_neighbor_kc_projection.py /path/to/minkin_svn.zip`; SHA-256 b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875 enforced by trusted prior repo derivation. No archive code is executed.

Next material gate: specify an intralayer height stiffness matrix and compute the relaxed Schur complement; only then source a frequency-dependent dissipative kernel or measured drag and compare both paired-angle force-versus-load curves to the conventional baseline.
