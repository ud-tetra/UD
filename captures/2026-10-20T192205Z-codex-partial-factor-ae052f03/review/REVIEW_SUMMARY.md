# Independent review of the retained partial-factor route

**PASS, conditional on the inherited norm and source premises.** The lower-bound proof, prefix extension, restricted conditioning bound, and active V3 implementation agree with an independent exact Fraction calculation. No mathematical error was found in the proposed formulas.

| Existing computational case | Actual sigma209 lower | All321 ordered proposal overstatement upper | Restricted condition upper |
|---|---:|---:|---:|
| boundary_pair_block | 0.00288043008098632 | 3.5295369483695666e-13 | 1887.2373658773165 |
| boundary_pair_rotating | 0.0028804300809872345 | 3.3836663193498766e-13 | 1887.2373658767126 |

The exact rational bounds are in CERTIFICATE.json and PREFIX_CERTIFICATE.json; table values are readable approximations. Both all321 overstatement bounds are below 2^-41. The qth-only overstatement bounds are respectively 4.738689459687481e-14 and 4.673960424661997e-14. The source tail upper, inherited with the original noise radius, is 1.0656170268898675e-10. It is strictly below cutoff2^-24, which is strictly below each new sigma209 lower. This conditionally certifies exactly209 actual singular values above the cutoff; it does not certify algebraic rank209.

The proof uses only saved thin-factor Gram and singular-equation premises. It does not need a complete reconstruction residual. The all321 extension uses prefix minmax for indices1..209 and nonnegativity for indices210..321; its discarded term is the saved s210 proposal. It needs no actual-tail premise for that one-sided inequality.

These are **one-sided overstatement** bounds. Underestimation and absolute indexed singular-value errors remain uncontrolled. The condition bound concerns Z restricted to the saved right-factor span; ambient leading-spectrum conditioning is not certified. Exact rational countermodels demonstrate both limitations, including a family whose restricted condition stays2 while ambient leading condition grows without bound, despite correct actual rank and zero residual.

The review passed49 primary arithmetic controls,19 additional countermodel controls,16 prefix controls, and58 active V3 identity/comparison checks. All10 original derived-bound pairs and6 added prefix pairs match exactly. Root V3's21 logical controls pass, and its certificate and controls are byte-identical to replay. Existing large norm certificates are inherited; their square-wrapper consistency is checked, but this is not a fresh raw-record or matrix-factor audit. Hashes bind provenance rather than establish inequalities.

No fits, raw records, or vector-factor copies were created. No actual floating-backend bug, two-sided B1 closure, all-history backend guarantee, registry promotion, or physical result is claimed.

Development — no registry entry. Same-team independent review. External promotion review PENDING. Physical Promotion = 0.
