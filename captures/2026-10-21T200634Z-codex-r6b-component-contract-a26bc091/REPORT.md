# R6b modular baseline and component-aware diagnostic contract

RESULT — The existing R6b implementation is frozen as a modular baseline, with N/64 disconnected 64-site modules per channel. Its source docstring states a globally connected intent; that intent is not achieved for L>3. A globally connected completion remains a separate source-law obligation. No links or weights were added. Physical promotion: 0. Development only; not CRL-2b registration.

Pinned repository source: c6b66d68a25b655627d6eb6f1bf6f96a13e2121b. Source hashes, domain, metric, diagnostics, controls, exposure and future execution requirements are in CONTRACT.json. FREEZE_RECEIPT.json binds its bytes before the new exact calibration output was generated. This construction does not revise the separately frozen six-channel particle operators or identify simulation sites with particle channels.

## 1. Baseline disposition

For L>=3, N=4^L, the source's cousin and second-cousin edges preserve the first L-3 base4 address digits. The Theta graph has C=N/64 connected components, each64 sites. Rho sibling edges, on-site cross coupling and diagonal disorder preserve that same partition, giving C independent128-coordinate components in the coupled two-channel matrix.

This is the mathematical reading of the implementation, not a claim that the original author intended a collection of isolated modules. The source explicitly intended connection; the audit records that intended-versus-implemented gap. Selecting a globally connected hierarchy requires a forward rule for additional incidences and their weights. The candidate formula eta^(2d) at larger d is not silently extrapolated here.

## 2. Frozen localization diagnostics

For one channel v, first report its support W=sum_i |v_i|^2. When W>0 set q_i=|v_i|^2/W. Let w_c=sum_(i in c) q_i. For m=64 define

\[
F_{\rm global}=N\sum_i q_i^2,\qquad
I_{\rm comp}=\sum_c w_c^2,\qquad
C_{\rm eff}=1/I_{\rm comp},
\]
\[
F_c=\frac{64\sum_{i\in c}q_i^2}{w_c^2}\quad(w_c>0),\qquad
\overline F_{\rm within}=\frac{\sum_c w_c^2 F_c}{\sum_c w_c^2}
=\frac{F_{\rm global}}{(N/64)I_{\rm comp}}.
\]

EXACT identity: F_global=(N/64) sum_c w_c^2 F_c. It separates within-component concentration from concentration across components. Both F_c and the weighted within-component score lie in[1,64]. A score of1 means uniform probability within occupied components; it does not require global occupation. These are mathematical diagnostics, not experimentally calibrated material-localization thresholds.

W=0 makes normalized localization undefined. There is no arbitrary denominator floor that turns an empty channel into a measured mode. For small nonzero W, report W and numerical sensitivity alongside the normalized diagnostic; a tiny channel's large normalized IPR is not large physical stock.

At L=4 (N=256, C=4), the frozen controls return:

| Preparation probability | Global F | Component IPR | Conditioned within-component F |
|---|---:|---:|---:|
| Uniform over all sites | 1 | 1/4 | 1 |
| Uniform over one component | 4 | 1 | 1 |
| Uniform over two components | 2 | 1/2 | 1 |
| One occupied site | 256 | 1 | 64 |

All four controls pass exact rational checks, including the factorization identity. They certify definitions and implementation on declared inputs, not empirical localization.

## 3. Complete exact spectrum of one Theta module

Set a=eta^4, b=eta^6 with eta=185/192. Let E4,E16,E64 average within aligned groups of4,16,64 sites. These nested orthogonal averaging projectors satisfy E4 E16=E16, E16 E64=E64. Thus

\[
P_0=E_{64},\quad P_3=E_{16}-E_{64},\quad
P_{12}=E_4-E_{16},\quad P_{48}=I-E_4
\]

are mutually orthogonal projectors summing to identity, with ranks1,3,12,48. The source-defined weighted Laplacian satisfies

\[
H_\Theta=64bP_3+(16a+48b)P_{12}+(12a+48b)P_{48}.
\]

| Eigenvalue | Multiplicity in one64-site module |
|---|---:|
| 0 | 1 |
| 64 eta^6 | 3 |
| 16 eta^4+48 eta^6 | 12 |
| 12 eta^4+48 eta^6 | 48 |

The new verifier constructs the projectors as integer matrices divided by64. It verifies all sixteen projector products, ranks, completeness and entrywise equality with the independently assembled source-rule Laplacian using exact fractions. These constitute a full finite spectral certificate for H_Theta. This does not diagonalize H_full or prove persistence under its cross coupling and disorder.

## 4. Why a returned eigenvector is insufficient

The global Theta zero space has dimension C. Component-uniform zero modes each have global F=C. An orthogonal Hadamard rotation at C=4 gives equally valid zero modes with global F=1. Both orthonormal bases have the same spectral projector; all these component-uniform or Hadamard-mixed states have conditioned within-component F=1.

For the complete rank-C projector P onto the Theta zero space, normalized projector density q_i=P_ii/C=1/N gives density F=1. This is basis independent. It summarizes the complete subspace and does not say that every preparation in that space is globally uniform or has F=1. State preparation and subspace density remain different objects.

The Hadamard coefficient matrix is checked exactly orthogonal after division by2. The two bases therefore give the same projector despite the factor4 difference in their individual global IPR scores. Probe dependence in such a degenerate space can reflect basis selection; compare spectral projectors and component-aware quantities before interpreting an individual-vector discrepancy as a physical anomaly.

## 5. Execution boundary and next task

No archived script or fresh numerical eigensolver was run. The only new execution was the explicitly constructed exact matrix/calibration verifier. The contract was frozen before its result. Historical R6b outputs and probes are already exposed; these controls do not create a blind holdout or an independent-review receipt.

A future bounded run should use L=4 (Theta256, coupled512 coordinates), preserving the source's two exposed probes0.00133 and1e-8 for comparison while recording their roles. Before execution, its actual implementation must freeze numerical tolerances and eigenspace separation rules and capture source/input/matrix hashes, metric, runtime versions, initial vector or RNG state, all solver failures, complete returned eigenpairs, residuals, per-probe labels and projector ranks. Six-decimal rounding is not a valid sole eigenspace/deduplication rule.

Priority100 next: implement that bounded component-aware numerical replay against the exact Theta spectrum and then the unchanged coupled model. Measure whether apparent localization survives component conditioning and subspace comparison. Keep native global connectivity as a separate unresolved source programme rather than altering the operator to obtain a desired result.

Generated: immutable contract, freeze receipt, exact verifier and results. Checked: source hashes, projector algebra, complete module spectral reconstruction and four calibration controls. Constructor verification only; independent review pending; no registry or physical promotion. Gap2_FINAL_Finite_Genesis.png remained unavailable and was not used; retry the upload if it is intended as evidence.
