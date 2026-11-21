# Ledger v0.85 dependencies for UD-Physics PR #456

**Status:** staged dependency addendum. Activation requires an independent reviewer to confirm the exact B-complex carrier and sink tuple on the reviewed head and an integration receipt identifying the verified merge commit. **Physical Promotion = 0.**

The 723-object baseline is captures/2026-10-21T151000Z-codex-exit03-recovery-98dc7b12/library_LEDGER_v0.85.json, at UD revision cef84ca5c996ec21b67247c74ee85c2c6c5dd995. Ledger SHA-256 8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec. This append-only capture records dependencies by existing ID and leaves the historical snapshot available for byte verification.

| Claim | Scoped dependency |
|---|---|
| C05, d_seat = 5, EXACT_INTERNAL | Appendix F.3 uses the tetrahedral S4 action. The two-dimensional trace-free diagonal sector E and three-dimensional off-diagonal sector T2 are different representations. The separate PB5 signed-edge theorem uses pentagonal ring symmetry with pole exchange and gives rank at most two. |
| C06, 7/960, DERIVED_STRUCTURAL with existing physical freeze | Under the proposed normalization only 2w2 + 3w3 = 7/192 follows. Equal per-coordinate weights and the physical coupling interpretation remain open. PB5 retention and stock accounting supply no deficit-to-shear allocation law. |
| B-complex sink calculation | PR #456 head 93d60b42553435979f24d7118441559c6a5950d4 uses cells 0134, 0234 and 1234, with sinks 34, 034, 134 and 0134. The lossless and damped dimensions are 17 and 10. The relay observation depends on a separate transfer map. |
| PB5 additive radial sink | The 43-dimensional carrier gives 21 lossless and 22 damped dimensions. A bare same-clock intertwiner has no PB5 target for the relay's rotating sqrt(5) branch. |
| Paired witness stock | Relay-minus-PB5 phase is atan2(det(v,u), dot(u,v)) in the standard orientation. The equal-effective-weight bounded-disk model gives 2c csc²(E/2); 7/6 is a parameter-specific asymmetric fixture. Emission, transport, verification work, and any physical unit map remain OPEN_CONSTITUTIVE_SOURCE. |

[PR #456](https://github.com/ud-tetra/UD-Physics/pull/456) · [Manuscript v0.16, Appendix F.3](https://chatgpt.com/library?file_id=libfile_950249aa77248191bb59f8460d92e53b&account_id=personal) · [Paired-witness derivation](https://chatgpt.com/library?file_id=libfile_fde3_f-9ee85d2534e08191859269e502f7b0b6_6894c086e37481918ca587ea44a8b0bc&account_id=personal)
