# Corrected particle specification freeze and simulation provenance audit

RESULT — Corrected six-channel operators and reference metric frozen as a reproducible development specification. Recovered simulations audited at source/output level. A new exact graph obstruction invalidates the R6b scripts' global-connectedness claim. No historical source was edited. Physical promotion remains 0; no particle preregistration or independent review is asserted.

Repository source: `ud-tetra/UD`, main commit `c6b66d68a25b655627d6eb6f1bf6f96a13e2121b`. Both case-distinct source directories are retained: 170 files in `docs/` and 51 in `Docs/`. SOURCE_INVENTORY.json pins all 221 files by SHA-256. NEW_DOCS_RELEVANCE.json records targeted text locators for the new archive. File-level ingestion is complete; this does not certify every historical theorem or diagram. No archived scripts, boot instructions or HTML code were executed.

## 1. What is frozen

`FROZEN_OPERATORS.json` is the normative finite mathematical specification; `FREEZE_RECEIPT.json` binds its bytes. Status: **FROZEN_DEVELOPMENT_SPECIFICATION__NOT_PREREGISTERED**. This is an explicit convention lock for subsequent calculations, not a claim that the microscopic source selects these objects or their physical interpretation.

| Object | Frozen definition | Scope |
|---|---|---|
| Coordinates | Unsigned edge channels (01,23,02,13,03,12) | Distinct from oriented simplicial-chain coordinates |
| Metric | G=I6, dimensionless positive reference form | Mathematical state metric; no physical Hilbert/energy identification |
| Kernel T | Self 1/2; opposite 1/6; each other edge 1/12 | Declared source matrix; counting/renewal derivation remains missing |
| Swap S | Exchanges the two members of each opposite pair | S squared is I |
| Star | Signed swap with pair signs (+1,-1,+1) | Declared channel involution; not a proved physical chirality operator |
| Spectral projectors | J6/6; (I+S)/2-J6/6; (I-S)/2 | T eigenvalues 1,1/2,1/3; ranks1,2,3 |
| Joint projectors | (I+sS)(I+h star)/4 | Ranks2,1,1,2; not generally T-invariant |
| H diagnostic | I-T | No time law or SI energy coefficient inferred |
| Coupling | H_j=u w_j^T+w_j u^T in orthonormal Pplus coordinates | Candidate finite operator, not a Higgs VEV or fermion mass law |

Use p_j=(e_(2j)+e_(2j+1))/sqrt2. In this orthonormal three-coordinate basis, u=(1,1,1)/sqrt3, w1=(1,-1,0)/sqrt2, w2=(1,1,-2)/sqrt6; L1=p0,L2=p2,R=p1. The explicit coupling is

\[
Y=\begin{pmatrix}0&2/\sqrt{18}\\-1/\sqrt6&-1/\sqrt{18}\end{pmatrix},\qquad
YY^T=\frac19\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]

EXACT: squared singular values1/3 and1/9. The invariant ratio sqrt3 survives; universal entrywise nonzero does not. Orthogonal rotations of the real Higgs basis preserve the singular values and absolute determinant. Orientation reversal changes the determinant sign. The frozen entry Y11=0 is the admissible counterexample to THM-565a's stronger wording.

Metric rule: if x_new=U x and T_new=U T U^-1, then G_new=(U^-1)^dagger G U^-1. Fixed-metric invariance is restricted to unitary changes (orthogonal in the real register). Exact checks show fidelity covariance under this transformation and failure when the metric is incorrectly held fixed. This repairs THM-LS1(iii).

The T/star commutator is nonzero; joint eigenspace dimensions do not imply conserved dynamical chirality. T commutes with all24 unsigned vertex-induced edge permutations, but only2 canonical signed edge actions. Replacing one representation by the other is prohibited without an explicit intertwiner and metric contract.

No species labels, mass scale, action unit, VEV, target dataset or fit enters this freeze. It fixes mathematical inputs for the development lane. It does not satisfy the non-constructor review or pre-exposure requirements of a particle bridge registration.

## 2. Simulation code-to-output map

Twelve recovered Python files were parsed as AST data. Eight shell/Hmulti code-output associations cover39 output records; a ninth OCPF family covers39 table points. Matching schema, profile, parameters and model descriptions support **candidate producer associations**, not authenticated execution. No family has a recovered code-hash/matrix-hash/environment execution receipt in the audited output. Historical actor names and timestamps remain declarations.

| Candidate code | Recovered output | Provenance finding |
|---|---|---|
| shell1_sim.py | B_rho_raw.json | Exponential profile with supplied xi; not a dynamically obtained localized eigenstate |
| shell1_4x10.py | B_rho_raw_4x10.json | Same profile family; sigma2 xi is imposed as8 times the supplied xi |
| shell1_eigensolve.py | B_rho_raw_eigensolve.json | Sparse Hamiltonian, shift-invert and overlap selector; source-compatible schema, execution hash absent |
| shell1_sector_resolved.py | B_rho_raw_sector.json | Changed sector selector; must remain a distinct analysis version |
| shell1_hmulti_va.py | B_rho_raw_hmulti_va.json | Clean3N operator; fallback labels a rho candidate even when no candidate passes the stated rho-weight cut |
| hmulti_version_a.py | Hmulti_A_raw.json | Clean2N operator; two supplied cross-coupling ansatze; not independent disorder trials |
| hmulti_r6b.py | Hmulti_R6b.json | Source-compatible schema and operators; 'connected' graph claim false globally |
| r6b_version_b.py | R6b_VersionB.json | Adds rho disorder to disconnected R6b graph; preserves the same finite component partition |
| ocpf_v3_sweep.py / ocpf_v3_efficient.py | OCPF JSON/CSV | Possible upstream generators; saved numbers exactly match the literal dataset in ocpf_v3_analyze.py, not a recovered hash-bound generator run |

The analysis script's literal OCPF dataset, JSON and CSV agree on all39 points. This proves transcription consistency. It does not establish how the original numbers were calculated. The canonical generator requests N5–13, the efficient variant N5–10 and partial eigenspaces for larger dimensions; the saved table covers only N5–7. No extrapolation to unreturned levels is admitted.

`hmulti_repaired_v11.py` emits schema Hmulti_A_repaired_v1.1, but no matching recovered output JSON was located in docs/Docs. The requested per_probe_sigma2 payload was likewise not located in output JSON. The request document and schema sketch are not execution results.

Numerical-source issues needing a new controlled replay include unspecified eigsh starting vectors, changing shift/fallback strategies, eigenvalue rounding to six decimals during deduplication, omitted per-probe labels and missing residual/eigenvector payloads. Rounding can discard distinct close eigenvalues as well as degenerate directions. Clean-operator repeated runs are not automatically independent disorder realizations. Normalized channel IPR must be read with its channel weight: a tiny-weight channel can have large normalized IPR without carrying significant support.

## 3. New exact finding: R6b is not globally connected

Both R6b scripts group sites by their base4 address. Sibling edges share a prefix of length L-1; cousin edges L-2; second-cousin edges L-3. Therefore every edge preserves the first L-3 digits. Within each64-site group, the second-cousin edges join its four16-site groups and cousin edges join distinct4-site groups. Positive weights make that64-site graph connected, but no edge leaves it.

For L>=3 and N=4^L:

\[
\#\text{components}=4^{L-3}=N/64,\qquad\dim\ker H_\Theta=N/64.
\]

The rho sibling edges, diagonal disorder and pointwise rho/Theta coupling also preserve that prefix. The full2N graph therefore retains N/64 disconnected components of128 coordinates. Adding same-site disorder does not supply the missing long-range hierarchy.

| Level | Sites N | Components | One-component-uniform F=N/64 | Reported Version B mean F_Theta |
|---|---:|---:|---:|---:|
| 5 | 1024 | 16 | 16 | 16.0 |
| 6 | 4096 | 64 | 64 | 63.999999999990564 |
| 7 | 16384 | 256 | 256 | 255.99999999997368 |
| 8 | 65536 | 1024 | 1024 | 1023.9999999998679 |

The exact theta Laplacian has both a globally uniform zero mode with F=1 and component-uniform zero modes with F=N/64. Orthogonal basis choices in this degenerate zero space change the IPR. The table's agreement within1e-6 with component-uniform values is an observed arithmetic property of the stored outputs. It is **not** a proof that these exact zero vectors are eigenvectors of the coupled H_full: coupling and disorder change that eigenproblem.

What is falsified is global connectedness and the use of these F values alone to establish intrinsic localization independent of finite component structure. No conclusion about fundamental physical localization follows. A spectral-projector/subspace diagnostic, component-aware normalization and genuine intended connectivity contract are required before interpreting a probe-bias replay.

The new verifier enumerates the source-defined adjacency independently at levels3,4,5, checks all component sizes and counts, and uses the prefix proof for general L. This is fresh finite mathematical verification. No recovered solver was imported or run.

## 4. What the additional Docs archive changes

The51 new files mainly add conservative contact, crossing, metric and propagation audits. They name missing native selection/clock/physical-map premises; importing them does not close those premises. Some augmented representations use induced half-weights after sum/difference transforms. Those are transported metrics for their own registers, not a reason to silently change G=I6 in this separate channel contract.

The energy-clock-support theorem adds a particularly relevant obstruction: measured same-carrier energy and signed state period determine A0*a, where a is native support, rather than A0 alone. Rescaling x by c and the injection map by1/c preserves apparatus trajectories while changing a by c^2 and A0 by1/c^2. Independent absolute support calibration is required. Quadratic readouts can also report half the signed state period. These are declared conditional results from the recovered manuscript, not new empirical anchors admitted here.

The monomial action theorem remains consistent: independently calibrated native unit energy and time identify action, while unknown total-state support is an additional unknown. The current operator freeze supplies no absolute amplitude injection map, state-clock certificate or universal action quantum. Physical promotion and particle registration remain unchanged.

## 5. Disposition and next action

Generated: immutable operator/metric specification, freeze receipt, code/output candidate map,221-file inventory, new-Docs relevance index and graph obstruction. Checked: exact operator identities, metric covariance, selected coupling invariants, source hashes,39 OCPF transcription rows and finite graph witnesses. Constructor only; independent review pending. Originals and historical outputs are preserved.

Priority100 next: freeze whether the intended R6b carrier is a disconnected collection of64-site modules or a globally connected hierarchy. If global connectivity is intended, derive the missing links/weights forward from a declared source rule. Do not add them merely to obtain a desired F result. Then run a bounded per-component/subspace and per-probe diagnostic under a new hash-bound execution contract with code/input/matrix hashes, solver settings, initial vectors, library versions, residuals and complete failure reporting.

Gap2_FINAL_Finite_Genesis.png was unavailable and not used. Re-upload it if it supplies needed source evidence.
