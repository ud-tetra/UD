# PB5 post-merge review intake for v0.87-preview

**Physical Promotion = 0.** The verified v0.85 baseline has 723 rows, Git blob 93e2ca31eba625989087275a71c4857848e321c6, and SHA-256 8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec. Its baseline revision is cef84ca5c996ec21b67247c74ee85c2c6c5dd995.

## Attribution and verification

The maintainer supplied a sign-off statement attributed to Devin Ramos with AI assistance, declaring INDEPENDENT_SIGNOFF_APPROVED / SCOPE_LOCKED for #583–#586 and #590. This capture preserves the attribution and reported disposition as supplied. The submission provides no direct reviewer confirmation or separately attributable GitHub approval. GitHub contains COMMENTED entries from ud-tetra, so independent approval has not been corroborated. The two records retain separate provenance.

| PR | Pinned implementation head | Merge commit |
| --- | --- | --- |
| [#583 radial projector](https://github.com/ud-tetra/UD/pull/583) | bf78e3737e5da0ad8a07ce5ef4d51db8b494972f | 8a7724ba7f5bf57c78698bdcf138ac0cee9ed386 |
| [#584 shear retention](https://github.com/ud-tetra/UD/pull/584) | 6addbc4c92947cca7cb88c749e477c7c64ff334b | fdcafc3841a733fd89716dcaa6c9ba482874ab96 |
| [#585 rim twist](https://github.com/ud-tetra/UD/pull/585) | 8343f85f714aa222fc2f63414c29a81349abbb97 | 57b926540e6284a34fbd550adf5f2c8c2f2b6a8b |
| [#586 relative holonomy](https://github.com/ud-tetra/UD/pull/586) | 22ebe538835a8e3efcc82a8def21fc35b82907c3 | a61e2b2b7bfff2b10be51079d517b1e8e4d347f3 |
| [#590 exterior settling](https://github.com/ud-tetra/UD/pull/590) | 02b957bbc6cb69c81868d18c77d2c39f04ee3bc0 | 729e84cc0c356487ca7184827b1827b6cd1d22f7 |

The Git tree for #590's merge is 71eb36a1380a4ec4a3237b8e9b7a1563a275807a. The supplied shorthand 729e84c refers to the merge commit.

## Scope corrections against the merged records

- **#583.** \(MM^+\) is the rank-11 orthogonal projector onto the radial edge-trace image. Duplication of flags preserves this projector. \(MM^\mathsf T\) can share its image and kernel while changing weights. The specified PB5 sink yields 21 invariant lossless and 22 damped dimensions on the 43-dimensional carrier. The separate B-complex result is 17/10 for its specified coordinate sink. Neither decomposition supplies a physical Lindblad model.
- **#584.** The declared equivariant signed-edge preparation retains two planar directions. The directional preparation with a supplied cyclic orientation retains three. Native shear encoding remains open.
- **#585.** The rim sign alone cannot select cyclic orientation because it equals its inverse. The result permits mirror-symmetric negative-flux configurations and makes no blanket claim about admissibility of parity transformations or full curvature assignments.
- **#586.** Every \(Q_8\) element is conjugate to its inverse, so single-loop character data cannot select an orientation. A shared-basepoint, gauge-invariant mixed-loop witness gives \(-1/2\) and \(+1/2\) on the declared mirror pair. These are exhibited values. A universal bound and endogenous coupling were outside the demonstrated scope.
- **#590.** With each channel normalized by its own initial magnitude, the specified exterior sink, and a one-period settling horizon \(T=2\pi/\sqrt{32/7}\), the minimum coupling is \(2.071267496\ldots\) in carrier time units. The binding even-channel peak reaches the stipulated \(1/62\) tolerance. The coherence-observable mapping and a quantitative Markov approximation remain open.

## Release status

The release candidate note #587, coarse-graining architecture #588, and two-cell memory result #589 are also merged. They were outside the submitted sign-off scope. This intake updates the earlier dashboard-copy status and leaves the release gate pending independently attributable review evidence. No v0.87-preview tag was observed at intake.

The previously logged constructor or maintainer records remain available on [#583](https://github.com/ud-tetra/UD/pull/583#pullrequestreview-6007398883), [#584](https://github.com/ud-tetra/UD/pull/584#pullrequestreview-6007451253), [#585](https://github.com/ud-tetra/UD/pull/585#pullrequestreview-6007451386), and [#586](https://github.com/ud-tetra/UD/pull/586#pullrequestreview-6007451093).
