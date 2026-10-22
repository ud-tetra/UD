# Graphite direct carbon angular force trace

22 October 2026. **Development — no registry entry; physical promotion 0.** This append-only result extends [draft PR #389](https://github.com/ud-tetra/UD/pull/389), which reproduced the two frozen source geometries and matched PR #381's unmodified force samples. Its input `candidate.npz` arrays are copied here with exact hashes. No earlier capture bytes are changed.

## Traced source equation and scope

LAMMPS `stable_22Jul2025_update4` `PairAIREBO::bondorder` calls `gSpline` and, in its bond-order force loops, adds the direct angular term with `tmp=-p_ij³/2`, `tmp2=VA*tmp*dgdc/2` and per-atom force `-tmp2*∇cos(theta)`. `PairREBO::spline_init` sets `PCCf[2][0]=0`. The verified `CH.rebo` has identical `gC1/gC2` polynomials over the three relevant angle intervals. For the recovered sheet geometry, 1,512 unique C–C bonds yield 6,048 ordered angular calls per sample. `trace_gspline_forces.py` computes each call's atom IDs, cosine, selected polynomial segment and projected force contribution from these source equations at the unchanged probe positions. Periodic images are reconstructed from the source triclinic cell; all sampled bonds stay within the full-weight cutoff.

This is an **independent Python evaluation of one force term specified by the source**, not a log emitted by the unmodified C++ runtime. Its per-call contributions sum to the projected direct angular force, with side-stencil closure better than 4e-11 eV/Å² at the middle step. Original first-layer REBO force vectors were separately matched against the archived PR #381 arrays in PR #389. The archived full REBO side difference is subtracted from this direct-term result to expose a remainder; that subtraction does not isolate every remaining bond-order term.

## Middle-step result

For the signed stiffness side difference `S=Qplus−Qminus`, `Q=-dF/dx`, at `h=2e-5 Å`:

| Case, probe/component | Archived first-layer S | Direct angular S | Full minus direct | Calls changing segment in five-point stencil |
| --- | ---: | ---: | ---: | ---: |
| `21_dir_0`, 34/8 | -7.264999548e-5 | -7.265588010e-5 | +5.884616e-9 | 504 |
| `21_dir_10024`, 30/4 | -7.780658083e-5 | -7.776180188e-5 | -4.477895e-8 | 360 |

Units for all three force-response columns are eV/Å². The direct angular term accounts for the first discrepancy within 0.0081% and the second within 0.0576% in magnitude. Summing only calls that change segment within the stencil gives -7.266071202e-5 and -7.776070699e-5 eV/Å²; calls staying in one segment contribute +4.79e-9 and -1.12e-9 eV/Å². Each trace contains its top individual atom triples and all seven h values. At the smallest h, force subtraction and coordinate-rounding error are comparable to the measured side difference; no physical interpretation is assigned to that limit.

The branch counts are from the reconstructed source equation, not original runtime instrumentation. In the first case they differ by a few near-boundary calls from the original PR #381 geometry count, consistent with sensitivity to reconstructed coordinates and floating-point comparison at the knot. The aggregate side response is the discriminating quantity here.

## Deliberate scope correction

During construction a provisional reconstruction of **all** REBO forces failed a baseline fingerprint check by approximately 0.14–0.18 eV/Å. Source inspection showed the omitted torsional bond-order path: at carbon coordination `(2,2,9)`, `TijSpline` is nonzero (`-0.0040480`), even for REBO. That provisional full-force calculation is rejected and is not included as an authority in this capture. The direct `gSpline` angle-gradient term above is computed independently from the specified source lines and compared only through its own projected side response. This check prevents labeling the small middle-step remainder as a uniquely isolated torsional or UD response.

## Consequence and next gate

The measured plateau in PR #381's first-layer REBO side stencils is almost entirely explained by the original carbon angular join's **direct force contribution** in the frozen numerical model. This strengthens the source-model attribution beyond the changed-potential control in PR #389. It does **not** establish a UD physical effect, source a dissipation constant, clear the original 81-coordinate Hessian gate, or predict friction under load. A patched C++ trace of `gSpline` call IDs and complete force-component additivity, followed by independent review, remains the appropriate term-level replication. The full original Hessian remains **HOLD** and physical promotion remains **0**.
