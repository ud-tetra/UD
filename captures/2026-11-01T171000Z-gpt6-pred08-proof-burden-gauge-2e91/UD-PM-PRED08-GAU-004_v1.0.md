# UD-PM-PRED08-GAU-004 v1.0 — Compact-link lift ambiguity and a conditional relative-winding construction

**Kind:** NO-GO + exact conditional construction. **Proof status:** EXACT_CONDITIONAL / VERIFIED_SCOPED. **Review:** DEFERRED. **Physical promotion:** 0. **Date:** 2026-11-01.

## Source, carrier, and gauge convention

Prior source: PRED07-ACT-003 in open UD PR #491 (source commit b56f892b5fe9fbc9059ebd0f83a9113f6f4867a0), which constructs a period-squared term under **single-valued real exact shifts** and explicitly warns it is not invariant under compact-link large-lift identifications. PRED06-PAR-003 proves no additive map `Z_2^3 -> Z` supplies the integer register. Ledger v0.39's G05 absolute master action weight remains open.

Let `K` be a connected oriented finite complex with `H_1(K;Z) = Z`, and let `Gamma` be a chosen primitive 1-cycle. Let `a in Z^1(K;R)` be a closed real 1-cochain, measured in *turns* (dimensionless), with lifted integer period `n=<a,Gamma> in Z`. A compact **link-only** readout is the family `U_e = exp(2 pi i a_e)`; no branch data, continuity interpolation, external reference or unwrapped measurement channel is supplied.

## Theorem A — compact link-only sectors do not determine the integer lift

For any integral closed 1-cochain `z in Z^1(K;Z)` with period `<z,Gamma>=1`, the shift `a -> a+k z`, `k in Z`, leaves **every** compact link `U_e` unchanged, but changes the lifted period `n -> n+k`. Therefore no function of the compact links alone can assign different values to two such lifts. In particular, `A_per(a)=tau*n^2/2`, `tau != 0`, cannot be a well-defined compact-link-only action on this equivalence class.

**Proof.** Each `z_e` is an integer, hence `exp(2 pi i(a_e+k z_e))=exp(2 pi i a_e)`. Period pairing is additive, giving `<a+kz,Gamma>=n+k`. For `k=1`, the proposed squared values for `n=0` and `n=1` differ by `tau/2`; the same compact link data cannot map to both. QED.

**Scope precision:** The ambiguity is of *edge-link lifts*. It does not rule out genuine topological winding of a separately given continuous order-parameter field or other global data: those would be an enlarged state with its own continuity and gauge convention. The theorem does not claim every integer edge-lift change is a vertex-gauge transformation; many are not. It proves a non-identifiability of a lift from the specified compact-link observables.

### Exact witness

On an unfilled oriented triangle `K` with cycle `Gamma=(1,1,1)`, `a=(0,0,0)` and `a'=(1,0,0)` have distinct integer periods 0 and 1 but exactly the same three compact links `(1,1,1)`. The unfilled qualification is essential: a filled triangle has trivial `H_1`.

## Theorem B — relative winding is invariant under an enlarged diagonal large-lift gauge group

Add a **new typed noncompact reference cochain** `r in Z^1(K;R)` and restrict the declared enlarged gauge action to simultaneous shifts
`(a,r) -> (a+d phi+z, r+d psi+z)`, where `phi,psi` are real vertex cochains and `z` is an integer closed 1-cochain. Define
`q=<a-r,Gamma>`.
Then `q` is gauge invariant under this **diagonal**, separately declared action, and `A_rel= tau q^2/2` is a well-defined sector-sensitive action on this enlarged state space. For integer relative sectors `q=2,3`, the exact gap is `5 tau/2`.

**Proof.** For any cycle `Gamma`, exact cochain integrals vanish: `<d phi,Gamma>=<phi,partial Gamma>=0`. The common `z` cancels identically in `a-r`. Hence `q` is invariant. The quadratic sector values follow by substitution. QED.

**Critical limit:** If the two fields permit *independent* large integer-lift shifts, then `q` changes and this action is again not invariant. Merely supplying the two compact link families `exp(2pi i a_e)` and `exp(2pi i r_e)` does not determine the unwrapped difference; the correlated reference lift and restriction of the gauge group are **additional physical/structural input**. This is a mathematical construction, not evidence such a reference exists in UD.

## Coefficient no-go and source boundary

Both `tau>0` and `2tau>0` obey all the above stated gauge and topological conditions but predict different gaps. No unique `tau` can be derived from these conditions alone; G05 and a calibrated native action map remain open. A forced equality to a separate quadratic harmonic-norm action determines only an *inverse matching* `kappa_N=tau/P_N(G)`, not an independent physical stiffness. Non-constructor review and experimental correspondence are OPEN_GATED. Physical promotion 0.
