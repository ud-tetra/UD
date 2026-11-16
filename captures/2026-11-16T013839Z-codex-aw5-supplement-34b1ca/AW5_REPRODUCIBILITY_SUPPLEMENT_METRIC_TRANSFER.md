# Revised Manuscript Reproducibility Supplement — AW5 chapter, metric and readout transfer

**EXACT_INTERNAL / CONDITIONAL. Physical Promotion = 0.** This companion section extends the [AW5 chapter](../2026-11-16T011802Z-codex-aw5-refine-1dd290/REVISED_MANUSCRIPT_REPRODUCIBILITY_SUPPLEMENT_AW5.md) and packages the [transfer and Whitney derivation](../2026-11-16T013033Z-codex-aw5-metric-6e34cd/AW5_METRIC_AND_READOUT_TRANSFER.md). Constructor review. Independent review open.

## Chain splitting

For each interior stellar refinement let s be the oriented subdivision injection and r a collapse chain map, with rs=I. Define Q=I−sr. The split C_f = im s ⊕ ker r is into subcomplexes because r and s commute with boundary. Choose any positive definite grade-wise complement metric W and keep the original coarse metric M_c. On the fine carrier use M_f=rᵀM_c r+QᵀWQ. Since x=s(rx)+Qx, both summands are orthogonal and M_f is positive definite. Also sᵀM_f=M_c r, so s is isometric and its adjoint is r.

Boundary and its metric adjoint preserve the orthogonal summands. Taking their skew difference gives A_f s=s A_c. These statements also hold for compositions of finitely many subdivision and collapse maps. For a coarse input q, the matched fine pair comprises drive sq and covector rᵀM_cq. For all t≥0 its response is qᵀM_c r exp(tA_f)sq=qᵀM_c exp(tA_c)q. The unrefined AW5 harmonic residue 1/4 is therefore preserved, together with the oscillatory response. This transfer statement remains valid for damped generators if the fine loss operator obeys D_f s=sD_c. A fine coordinate mask requires a separate loss check.

## Scope and replay sequence

| Result | Established scope |
| --- | --- |
| Face heat trace plateau | b₂=1 is invariant through the declared hollow refinements. |
| Unweighted exterior amplitude | The fixed drive drops to 19/80 for one leaf and 1/5 for all four leaves. |
| Matched metric amplitude | Exact 1/4 for the lifted drive and its fine metric dual. |
| Raw exterior readout | A normalized raw covector gives 3/13 in the split-metric one-leaf example. Euclidean Whitney weighting preserves the fixed-load residue 27/64 in the tested construction, with normalized residue 1/6 → 43/273. |

Run the three replays in sequence: [heat-trace and bistellar control](../2026-11-16T004932Z-codex-aw5-heat-729e4b/heat_trace_aw5.py), [stellar refinement sweep](../2026-11-16T011802Z-codex-aw5-refine-1dd290/refine_aw5.py), and [metric transfer and Whitney assembly](../2026-11-16T013033Z-codex-aw5-metric-6e34cd/metric_transfer_aw5.py). The metric family depends on the selected chain retraction and complement metric. The raw exterior and Whitney comparisons provide separate controls for normalization and observability.

The [Discovery one-leaf acquisition certificate](https://github.com/ud-tetra/UD-Physics/blob/c26feb7e1c93b3eb54d3d055df7a1fab3d6243cf/candidates/aw5-hollow-star-intake/REFINED_WINDOW_CERTIFICATE.md) uses the unweighted 60-coordinate carrier and fixed exterior probes. It provides a conditional finite-window contrast bound of 978548309/16095641600 against both controls, above the existing 3/64 threshold. This certificate is separate from the matched-transfer theorem and has no measured bench evidence.
