# Graphite derivative-step diagnosis and periodic-image correction v0.1

RESULT / STATUS: DIAGNOSTIC_COMPLETE. Both remaining derivative failures are isolated to different numerical regimes. All20 tested observables have local stable three-step windows, but no single three-step window is common to all20 on the frozen ladder. Previous stationary-stiffness qualification remains2/4; this diagnostic does not retrospectively replace failed tests. A substantive earlier periodic-image error in the geometric axial maps was corrected and all36 maps/72 closure tests replayed. Physical promotion0. Development — no registry entry. Constructor verification only; non-constructor review pending.

## Derivative diagnosis

The stationary positions, force model, basis and previous matrices are unchanged and hash-checked. A prewritten adaptive diagnostic evaluates all three original directional vectors and the two largest-discrepancy coordinate columns in each of four configurations, using seven steps from5e-5 to7.8125e-7 Angstrom. Both previously passing cases are controls. Positive/negative projected forces, repeated baselines, actual displacement rounding and effective tangent directions are retained. All original tolerances remain unchanged.

A stable local window requires three consecutive ladder values with both adjacent max changes below1e-6 eV/Angstrom^2. All20 observables have at least one such window. Their intersection is empty. This is a finite diagnostic on exposed observables, not a proof that no other common step could exist or that selected columns qualify every matrix entry.

| Remaining failure | Evidence from this audit | Disposition |
|---|---|---|
|21_dir_0, direction1 | Error relative to the stored refined Hessian is8.32e-8 at h5e-5,2.69e-7 at6.25e-6,1.0406e-6 at1.5625e-6 and1.5747e-6 at7.8125e-7 | The smaller step worsens the check; a local directional plateau exists at larger steps |
|31_dir_10084, columns13/63 | Full-column changes remain above1e-6 across6.25e-6/3.125e-6; they fall below the limit at the next smaller pair | Those columns require a smaller local stencil than the previously selected full-matrix pair |

Repeated baseline forces are bit-identical, and fresh baseline reproduction differs from the stationary archive by at most7.90e-17 eV/Angstrom. This excludes observed baseline history drift in these runs; it does not eliminate deterministic floating-point conditioning.

Actual Cartesian displacements differ from their nominal values by a few e-15 Angstrom. Dividing those representation differences by an increasingly small h enlarges effective direction error. For the failing21_dir_0 direction at1.5625e-6, using the projected actual direction in the exposed approximate Hessian lowers the discrepancy from1.0406e-6 to6.77e-7. This is evidence that input representation contributes, not an independent corrected derivative or a bound on all force-evaluation error. Orthogonal rounding components remain outside that tangent correction. The original failed check is preserved.

## REBO force-channel and angular-spline diagnostic

A separately frozen31_dir_10084 control retains only the two same-layer REBO interactions and explicitly disables cross-layer pairs. Subtracting its derivative from the stored full derivative isolates the fixed-normal KCz contribution up to floating summation error. At the6.25e-6/3.125e-6 pair, column13 changes by9.5253262e-6 in the full model and9.5253477e-6 in REBO alone; the KCz residual change is5.74e-10 eV/Angstrom^2. Column63 gives the same separation. Thus the large step-sensitive component is localized to REBO, rather than the smooth interlayer tail in this control.

The actual CH.rebo parameter file has a carbon angular knot at cos(theta)=-1/2. Exact Decimal evaluation of its neighboring gC1 polynomial pieces gives equal value, first derivative and second derivative at the join, but a third-derivative mismatch24.334074. This is a C2 join, not a discontinuity of the angular function or its first two derivatives. A central force derivative that spans a Hessian-slope change need not display the usual smooth-region quadratic convergence.

The corrected periodic geometry shows25 angle triples crossing this knot for each of the two31_dir_10084 coordinate probes at steps through3.125e-6. The crossings disappear at1.5625e-6 and below, where the selected-column changes settle. Those angles are only4.65e-7 away from the knot at the reference. This supports the angular-branch interpretation of the REBO-localized effect. It does not instrument the runtime to prove that this one term uniquely accounts for every residual.

Source code was retrieved from the official LAMMPS tag stable_22Jul2025_update4: src/MANYBODY/pair_rebo.cpp, pair_airebo.cpp and pair_airebo.h. The tag family matches the installed runtime version, but exact binary-to-tag build identity was not independently verified. Source, parameter bytes and license are preserved with hashes in SOURCE_REGISTER.json. The reference code selects angular polynomial pieces in gSpline; the polynomial derivative calculation uses the actual retained parameter decimals. Sources: https://github.com/lammps/lammps/tree/stable_22Jul2025_update4/src/MANYBODY . Current develop documentation was not substituted for this versioned source.

## Correction to earlier geometric axial maps

A bond-length guard in the angular audit exposed a separate earlier construction error. The source graph used periodic image shifts computed at raw input coordinates. Three cases had atom-specific integer cell wrapping in the saved LAMMPS references. Reusing the old edge shifts without converting that image gauge produced spurious bond lengths up to40.45 or45.72 Angstrom, instead of about1.42 Angstrom.21_dir_0 has no such image change. This error affects geometric axial directions, norms and cycle fractions in27 earlier rows and their saved acceleration witnesses. It does not affect the source graph incidence or the LAMMPS force/Hessian calculations.

For saved-versus-raw image offsets t_i, the corrected edge shift is

    s_corrected(i,j)=s_raw(i,j)-t_j+t_i.

Every offset is checked to be an integer lattice vector within1e-10 Angstrom, and every corrected intralayer bond is below1.7 Angstrom. A separate nearest-image enumeration agrees exactly with all corrected normals in all36 configurations. The initial guard failure and script are retained under development_failure; it aborted before exporting angular results.

IMAGE_GAUGE_CORRECTION.json names the affected capture/cases and superseded fields. The earlier quantitative axial geometry for the three affected cases is superseded, with immutable originals retained. The corrected cycle-projection squared-norm fraction spans0.0951764–0.2219354; it is a fraction within the selected geometric observable, not physical protected energy or friction.

All72 corrected axial and cycle-axial closure tests again have rank n-1, hidden relative-layer breathing and resolved nonclosure. The normalized closure residual range remains0.00108978–0.00146917 because the rowspace is again b-perp; its invariant-subspace coupling depends on that rowspace, not on a particular redundant encoding. Corrected acceleration witnesses are retained. The conditional minimal full-quotient augmentation corollary is re-established with these corrected numerical hypotheses. The exact gradient-cycle obstruction, frozen H/b breathing-memory algebra, force derivatives and stationary preparations are unaffected. No native600-cell/material identification is gained.

This is a recorded constructor correction, not an independent review. Earlier constructor verification failed to check the image-gauge premise; agreement between implementations using the same wrong shifts did not catch it.

## Verification and next gate

The verifier independently recomputes all20 force ladders, actual-direction residuals and complete window intersections from raw arrays, checks source hashes and baseline repeatability, and confirms36 corrected bond maps by direct periodic-image enumeration. The corrected geometric replay preserves all72 closure records and witnesses. A failed REBO-only setup omitted the explicit cross-pair none setting; its script/log are preserved, and it failed before any force arrays were produced. The corrected setup is fully declared in component.py.

The useful next gate is a branch-aware, direction-aware derivative contract: bound each stencil against angular branch distance, use a documented local step plateau, and control Cartesian input representation before testing the full matrix and independent directions again. The numerical diagnosis does not authorize loosening thresholds or promoting the earlier2/4 result. A source-selected physical/native bath and physical friction remain OPEN/HOLD.

A — NUMERICAL:20 step observables diagnosed; no common frozen-ladder window.
B — CORRECTED:36 geometric maps and72 closure tests replayed; old quantitative geometry superseded for three cases.
C — HOLD: stationary stiffness remains2/4 qualified; independent review and physical/native bath open.
D — Physical promotion0; Development — no registry entry.

1. Next: freeze a branch-aware per-column derivative rule and independent directional plateau checks, then run full qualification with the same tolerances. Priority97/100.
