# Graphite omitted-mode coupling audit v0.1

RESULT / STATUS: PASS numerical qualification across 36 frozen configurations. Source-selected physical/native bath remains HOLD. Physical promotion0. Development — no registry entry. Constructor verification only; independent review pending.

## What was tested

The earlier material response held lateral coordinates fixed and retained primitive-periodic vertical displacements with global vertical translation removed. This audit keeps all36 previously relaxed geometries and potential choices, observes the full Cartesian force, and differentiates with respect to the same normalized vertical inputs. Lateral line-force filtering is omitted only in these force observations. No geometry was re-relaxed and no dynamic trajectory was integrated. The extension in which the lateral constraints are released is therefore explicit; the earlier constrained response is preserved.

The inputs span four source configurations, cutoff radii16/20/24 Angstrom and imposed smooth-tail widths1/2/3 Angstrom in the previously qualified REBO plus fixed-normal KCz family. This is not the legacy hard-cutoff model, a fully relaxed3D graphite calculation, an infinite-range result, a complete phonon dispersion or a new experiment. Equal atom masses preserve the Euclidean subspace split up to a common scalar mass.

## Coupling result

The table gives ||output component||F/||full force derivative on retained inputs||F. These are tangent operator norm ratios, not energy fractions or friction rates.

| Omitted output block | Minimum | Maximum | Classification |
|---|---:|---:|---|
| Primitive-periodic in-plane x/y | 0.00701323655 | 0.00873500755 | {'RESOLVED_NONZERO': 36} |
| Nonprimitive vertical | 4.43394304e-12 | 4.64615065e-10 | {'BELOW_THRESHOLD': 36} |
| Nonprimitive in-plane x/y | 3.56812702e-10 | 1.20235805e-08 | {'BELOW_THRESHOLD': 36} |

The full-force derivative resolves a coupling from retained vertical motion into primitive-periodic lateral coordinates. In contrast, nonprimitive outputs lie below the frozen numerical threshold. This distinguishes omitted Cartesian polarizations within the same periodic sector from omitted spatial wavevector sectors. A broad statement that all omitted phonons are automatically a reservoir would miss this distinction.

DERIVATION.md proves the conditional symmetry result: if the full Hessian commutes with primitive translations at a periodic reference, it commutes with the group-average projector onto primitive-periodic coordinates, so the complementary wavevector sectors have zero linear harmonic cross block. Translation symmetry does not prohibit in-plane/vertical mixing at the same wavevector. Small numerical residuals corroborate this premise-based obstruction; they do not prove exact zero at the saved floating-point positions or in a defective, bounded or anharmonic specimen.

## The reference is not a free3D equilibrium

The maximum per-coordinate lateral residual force across the36 geometries ranges from 0.0229320708 to 0.025151649 eV/Angstrom. Thus releasing the lateral constraints also releases a nonzero reference force. The free linearization is affine, F=F0-Hu+..., and the reference is not a free3D equilibrium.

The detected cross block is a valid force derivative at a constrained equilibrium. It is not a full3D normal-mode spectrum or a stable bath. Before using the omitted lateral coordinates dynamically, a new preparation must specify how registry and load are maintained and either balance the residual forces or re-equilibrate under the declared constraints. The positive prior vertical block cannot certify positivity of the full3D Hessian.

## Verification and reproducibility

All36 source matrix hashes were checked. Central differences use1e-4 and5e-5 Angstrom. Maximum full-column coarse/fine relative discrepancy is 5.5664e-10; maximum absolute reciprocity discrepancy in the declared in-plane controls is 4.87052e-07 eV/Angstrom^2. Reciprocity compares separate in-plane input force evaluations with the transpose of the vertical-input cross block. The full retained block matches the earlier constrained block to relative 6.57295e-15.

A second constructor script independently projects full-force columns by group averaging rather than the isometry matrix used in construction, checks exact preservation of input geometry/group labels, and verifies all full vertical derivative columns against the earlier saved raw arrays. Maximum full-z column discrepancy is 3.29344e-14. Neither script is non-constructor review. Finite-step diagnostics are not rigorous force-model uncertainty bounds.

The first four jobs saved their full arrays but could not export NumPy Boolean values to JSON. Their script, arrays and error logs are retained under development_failure. The exporter was corrected; the raw columns were reused, only reciprocal controls were reevaluated, and all36 preserved arrays across those four jobs are exactly equal. No scientific threshold was changed. EXECUTION.json records those initial process failures separately from EXPORT_RECOVERY.json and the final scientific verdict.

The package includes all full Cartesian column arrays at both steps, source geometry and labels, reference forces, prior K/g, frozen protocol, source hashes, mathematical derivation and verification. It preserves the smooth plugin source and potential bytes used, with a reproduction note. The derivative audit requires a compatible LAMMPS runtime; archived scientific source files are not executed on ingestion.

## Meaning for the UD hypothesis

The original protected-port proposal still requires an independently sourced material map, port and drain. This audit supplies neither a native dictionary nor a damping coefficient. Its constructive result is a candidate material coupling route within the same periodic sector, accompanied by the prerequisite equilibrium/preparation problem. Its scoped obstruction is that symmetry-separated harmonic modes are not automatically an export channel.

Even after a suitable stationary full-coordinate preparation is supplied, a finite conservative omitted block gives reversible memory. A physical reservoir claim needs its spectrum, preparation, boundary or continuum limit, coupling and export/noise bookkeeping. Nonzero coupling is a necessary admission test, not a friction prediction or a new UD explanation.

A — DERIVED: full-force subspace criterion and conditional symmetry obstruction.
B — NUMERICAL:36 retained configurations qualified; constructor only.
C — OPEN/HOLD: stationary released-coordinate preparation, omitted spectrum, physical/native bath and independent review.
D — Physical promotion0; Development — no registry entry.

1. Next: construct a stationary preparation allowing internal in-plane relaxation while explicitly maintaining layer registry/load, then test the retained/omitted coupling and full constrained stability there. This is a new declared material preparation and must preserve the current evidence. Priority94/100.
