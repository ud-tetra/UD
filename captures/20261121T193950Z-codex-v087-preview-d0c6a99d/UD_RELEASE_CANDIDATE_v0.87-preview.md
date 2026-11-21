# Unified Dynamics v0.87-preview release candidate

**Status** · Proposed documentation. **Physical Promotion = 0.**

This candidate documents the PB5 radial sink on main and records the shear and holonomy results awaiting independent review. The scope is the specified finite PB5 simplicial carrier, its skew Hodge–Dirac generator, and the declared reciprocal link connections.

## Included on main

[UD #583](https://github.com/ud-tetra/UD/pull/583) is on main at [8a7724ba](https://github.com/ud-tetra/UD/commit/8a7724ba7f5bf57c78698bdcf138ac0cee9ed386). Reviewed-code target bf78e3737e5da0ad8a07ce5ef4d51db8b494972f has the same repository tree as the two-parent merge. Its recorded review is [COMMENTED](https://github.com/ud-tetra/UD/pull/583#pullrequestreview-6007398883). Independent scope-locked approval is still unverified.

Let \(S\) collect the edge traces of the five internal radial faces. The orthogonal projector \(MM^+\) for \(M=S^\mathsf T\) has rank 11 and the same kernel as the positive additive Whitney sink. For the unit skew Hodge–Dirac generator \(A\), the observation ranks of \(S\), \([S;SA]\) and \([S;SA;SA^2]\) are \(11,22,22\). The 43-dimensional carrier therefore has a 21-dimensional invariant lossless sector and a 22-dimensional damped complement in the specified sink model. The face-sum control instead has 33 invariant lossless dimensions. The radial trace specification concerns the five shared interior faces. It supplies no exterior-boundary condition or physical damping rate.

[Canonical operator and replay on main](https://github.com/ud-tetra/UD/blob/8a7724ba7f5bf57c78698bdcf138ac0cee9ed386/captures/20261121T173219Z-codex-pb5-projector-c1ac5024/UD_PB5_PSEUDOINVERSE_REPLAY.md)

## Pending independent review

| PR and head | Candidate scope | Constructor evidence |
| --- | --- | --- |
| [#584 · 6addbc4c](https://github.com/ud-tetra/UD/pull/584) | The tested equivariant signed-edge encoding retains two planar directions. A supplied cyclic orientation allows the directional encoding to retain one additional axial direction. | [CI](https://github.com/ud-tetra/UD/actions/runs/44931130035) · [Scope comment](https://github.com/ud-tetra/UD/pull/584#pullrequestreview-6007451253) |
| [#585 · 8343f85f](https://github.com/ud-tetra/UD/pull/585) | A single \(\mathbb Z_2\) rim sign is invariant under reversal. The replay checks 1,024 gauge-fixed filled PB5 connections and identifies mirror-symmetric negative-flux examples. | [CI](https://github.com/ud-tetra/UD/actions/runs/44932812320) · [Scope comment](https://github.com/ud-tetra/UD/pull/585#pullrequestreview-6007451386) |
| [#586 · 22ebe538](https://github.com/ud-tetra/UD/pull/586) | Single-loop \(Q_8\) class functions are invariant under inversion. A relative rim-and-triangle trace yields an exact gauge-invariant witness of \(\pm1/2\) on the supplied mirror pair. | [CI](https://github.com/ud-tetra/UD/actions/runs/44933530575) · [Scope comment](https://github.com/ud-tetra/UD/pull/586#pullrequestreview-6007451093) |

The relative witness is invariant under equatorial rotations and pole exchange and changes sign under a vertical mirror. These results leave native shear encoding, autonomous selection of a handed connection, the axial coupling coefficient, and physical interpretation open.

## Before cutting a release

Record each actual independent disposition against the head reviewed, including the outstanding governance record for #583. For #584–#586, compare the final integrated files against the reviewed payloads and rerun the integrity checks on the final heads. Move a candidate result into the included scope only after its merge and verification. This note does not assign a tag target or publish a release.
