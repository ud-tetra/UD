# Unified Dynamics: O09 phase-current source gate and cubic tetrahedral selection theorem

**Artifact:** `UD_O09_CUBIC_CURRENT_GATE_v0.1`  
**Date:** 2026-10-31  
**Status:** `EXACT_SCOPED` (K4 symmetry, cubic selection, gauge/continuity and conditional variational identities) / `CANDIDATE` (periodic burden-phase coupling and illustrative evolution) / `NO-GO` (unsourced identification) / `OPEN_GATED` (O09-to-link intertwiner and physical bridge).  
**Physical promotion:** **0**. Scientific review is constructor-team only; non-constructor review pending. No target measurements were used.

## 1. Source hierarchy and precise question

The current *recovered* coefficient ledger v0.85 (see Sources, filename `library_LEDGER_v0.85.json`, inherited scientific revision v0.43) assigns:

- **O09 — `I_loop->Hodge`:** `I_lift = (1/2) sum_(omega>0) a_omega Delta phi_tilde_omega`, and on a closed history `I = pi sum_(omega>0) n_omega a_omega`. This is a **typed lifted loop-history action map**, temporally additive and Hodge-intertwiner covariant. Its next gate is open/contractive action defects, potential sufficiency of Q136, and downstream physical action units via G06. It does **not** specify an edge-link phase, a local Hamiltonian, or a burden-to-phase current.
- **G05:** the historical universal scalar loop coefficient is **RETIRED / AUTO_FREEZE** in mainline; a scalar endpoint-defect shortcut is not permissible. This supersedes the weaker status of G05 in the supplied ledger v0.39. The archived v0.39 numerical formulas remain separate objects.
- **Q140:** `delta_U(U)=1-ReTr(U)/d = ||I-U||_F^2/(2d)` is exact mathematical geometry, not an automatically selected action coefficient or face stiffness. There is no published equivalence `O09 = historical local Wilson action`.

**Question addressed:** Can a conserved oriented phase current be *derived* from O09 and the native K4 geometry, with no arbitrary data-facing coefficient? The answer separates (i) variation of O09, (ii) source-shape selection from K4 symmetry and scalar vertex burden, and (iii) an optional, newly declared constitutive coupling. These are different results.

## 2. Typed state spaces and fixed assumptions

- Filled oriented tetrahedron `T=Delta^3`, vertex set `{0,1,2,3}` and unit oriented-simplex chain bases.
- `C0(T;R)=R^4`, `C1=R^6`, `C2=R^4`, `C3=R`. Boundary operators `B1:C1->C0`, `B2:C2->C1`, `B3:C3->C2`, with `B1 B2=B2 B3=0`.
- Edge cycles `Z=ker B1=im B2` (dimension 3), equipped with the inherited Euclidean metric. The projector is `P_Z=I6-B1^T B1/4`, and `B2 B2^T=4P_Z`.
- **Candidate input carrier:** one *dimensionless scalar vertex-burden value* `b_i` per vertex; `b in C0`. This typing is assumed for the theorem and is **not** a proof that every current UD burden stock lives at vertices or is dimensionless.
- `S4` acts by vertex permutation on `b`, and by the orientation-signed induced action on edges/faces. A candidate polynomial source must be `S4`-equivariant. The source has **no fixed spatial direction chosen externally**.
- **Separate carrier:** O09 records modal Hodge-history variables `(a_omega,phi_tilde_omega)`. These are **not** declared identical with K4 link phases `alpha in C1(T;R/2pi Z)` or with scalar vertex stock `b`.

All conclusions are finite-algebraic. The indexed 3+1 four-pentachoron slab, metric/lapse, laboratory units, physical photons and measured spectra remain outside this domain.

## 3. Theorem O09-V — O09 does not determine an edge source

O09 specifies an action *history value*, not a complete Hamiltonian system with a local derivative map. Its formal first variation is

`delta I_lift = (1/2) sum_omega [delta a_omega Delta phi_tilde_omega + a_omega delta(Delta phi_tilde_omega)]`.

There are no source-specified derivatives `D_alpha a_omega`, `D_alpha phi_tilde_omega`, or an intertwiner from the Hodge modal carrier to the oriented edge carrier. Therefore `delta I_lift / delta alpha_e` and `J_edge` **cannot be uniquely computed from O09 as supplied**. This is a **source-identifiability obstruction**, not a claim that all future UD couplings must vanish.

For an expressly **added** indexed first-order variational interpretation with independent amplitude and phase variables,

`S_hist = (1/2) sum_(n=0..N-1, omega) a_(n,omega) [phi_(n+1,omega)-phi_(n,omega)]`,

the exact interior equations under free variation are

`partial S_hist / partial phi_(n,omega) = (a_(n-1,omega)-a_(n,omega))/2`,  
`partial S_hist / partial a_(n,omega) = [phi_(n+1,omega)-phi_(n,omega)]/2`.

Without a separately defined Hamiltonian/constraint these impose no nontrivial deterministic transport evolution (for fully free variations they give constant `a` and phase increments zero). If amplitudes are prescribed rather than varied, the phase increments are not selected by O09. For the extension `S_hist - h sum_n H_n(a_n,phi_n,b_n)`, its Euler equations instead include

`a_n-a_(n-1)=-2h partial_(phi_n) H_n`, and `phi_(n+1)-phi_n=2h partial_(a_n) H_n`.

**These equations are exact under the added discretization; H is still missing.** Restoring retired G05 as a universal scalar does not supply H or the required carrier map.

## 4. Theorem K4-C — The first equivariant vertex-scalar-to-cycle current is cubic

Let `P_k` be the space of **homogeneous polynomial maps of degree `k`** `J_k:C0->Z` that transform covariantly under the full signed `S4` action. The equivalent linear space is `Hom_S4(Sym^k C0,Z)`.

For the conjugacy classes `1^4, 2·1·1, 3·1, 2·2, 4` of sizes `1,6,8,3,6`, the exact characters are:

| Representation | `1^4` | `2·1·1` | `3·1` | `2·2` | `4` |
|:--|--:|--:|--:|--:|--:|
| `Z` (signed edge-cycle) | 3 | -1 | 0 | -1 | 1 |
| `Sym^0 C0` | 1 | 1 | 1 | 1 | 1 |
| `Sym^1 C0` | 4 | 2 | 1 | 0 | 0 |
| `Sym^2 C0` | 10 | 4 | 1 | 2 | 0 |
| `Sym^3 C0` | 20 | 6 | 2 | 0 | 0 |

By the character inner-product formula, `dim Hom_S4(Sym^k C0,Z)` is **0,0,0,1** for `k=0,1,2,3`, respectively. Hence **no full-`S4` equivariant nonzero constant, linear or quadratic source can map a single vertex scalar field into the conserved edge-cycle carrier; exactly one cubic generator exists, up to overall scalar**.

This is a strong **NO-GO / scoped** for lower-degree sources. It does **not** exclude linear sources supplied by a separately typed oriented edge/face carrier, broken symmetry, spinor variables, a second independent field, or a larger graph. It is not a statement that all physical currents begin cubically.

## 5. Theorem K4-J — Explicit unique cubic source and exact conservation

For an oriented edge `i<j` define the antisymmetric cubic 1-cochain

`eta_ij(b) = b_i b_j^2 - b_i^2 b_j = b_i b_j(b_j-b_i)`.

Define the face stress and edge current

` t(b)=B2^T eta(b)`,  `J_cub(b)=B2 t(b)=B2 B2^T eta(b)=4 P_Z eta(b)`.

On an oriented triangle `i<j<k`, direct expansion gives

` t_ijk(b)=(b_i-b_j)(b_j-b_k)(b_k-b_i)`.

It is the Vandermonde alternating cubic. Consequently:

1. **Orientation/locality:** `t` is an oriented face 2-cochain, polynomial in the three incident scalar values, and covariant under all 24 vertex relabelings.
2. **No arbitrary direction:** `t` and `J_cub` are defined entirely from `b` and incidence. Their overall **scale and physical units remain undetermined**.
3. **Discrete Bianchi:** `B3^T t = (B2 B3)^T eta = 0` exactly. Thus `t` is a face curvature-shaped compatible 2-cochain, unlike an arbitrary one-face holonomy assignment.
4. **Current continuity:** `B1 J_cub = B1 B2 t =0` exactly.
5. **Uniform-stock null:** `b -> b+c 1` leaves `t` unchanged; `b -> lambda b` scales `t` and `J_cub` by `lambda^3`. Identical values on a face give zero face stress. This supplies a cubic *contrast scaling*, not an independently predicted contrast.

For the exact fixture `b=(0,1,2,3)`, with the ascending vertex/face/edge basis,

` t=(2,6,6,2)`,  `J_cub=(8,4,-12,4,4,8)`,  `||t||^2=80`,  `||J_cub||^2=320`.

**Exact independent verification:** generated incidence and signed representation checks over all 24 elements; a second hard-coded-incidence algebraic calculation. Character multiplicities independently checked by the symmetric-power trace formula and polynomial basis. This is the principal constructive closure of this execution.

## 6. CANDIDATE C — Periodic compact action and a stable nonflat demonstration

Nothing in the present O09 ledger demands the next coupling. It is constructed **solely as a target-blind admissibility test** and must not be promoted as current UD canon.

Let the separately typed compact link phase be `alpha in (R/2pi Z)^6` and let `Phi=B2^T alpha` be its four oriented face fluxes. Choose new constants `kappa>0` and `g` with unestablished native units, and optional burden storage functional `U_B(b)`:

`V(alpha,b) = kappa sum_f [1-cos(Phi_f)] - g sum_f t_f(b) sin(Phi_f) + U_B(b)`.

The second term is gauge-invariant, periodic, face-local, and `S4`-invariant: both `t_f` and `sin(Phi_f)` flip sign on orientation reversal. Its phase gradient is

`nabla_alpha V = B2 [kappa sin(Phi) - g (t(b) .* cos(Phi))]`.

Thus the **required source** in the phase force balance is

`J_b^candidate(alpha,b)=g B2[t(b) .* cos(Phi)]`, obeying `B1 J_b^candidate=0` EXACTLY. The coefficient `g`, the independent Wilson stiffness `kappa`, and their relative normalization are **not sourced from O09**.

The phase Hessian at fixed `b` is

`H_phase = B2 diag[kappa cos(Phi_f)+g t_f(b) sin(Phi_f)] B2^T`.

**Exact nonflat stable fixture.** Fix `b=(0,1,2,3)` and define `epsilon=g/kappa`. Put

`Phi*=(arctan(2 epsilon), arctan(6 epsilon), arctan(6 epsilon), arctan(2 epsilon))`.

It obeys the 3-cochain Bianchi identity `B3^T Phi*=0`. Hence it is realizable by a link phase `alpha*=B2 Phi*/4`. On each face,

`kappa sin(Phi*_f)-g t_f cos(Phi*_f)=0`.

The Hessian has strictly positive face weights `kappa sqrt(1+epsilon^2 t_f^2)`. Therefore all three transverse modes are stable; the three gauge-gradient zero modes remain gauge. The potential difference relative to the flat configuration at the same frozen `b` is

`V(Phi*,b)-V(0,b)=kappa [4-2sqrt(1+4 epsilon^2)-2sqrt(1+36 epsilon^2)] < 0` for `epsilon !=0`.

This *does not contradict* the previous source-free Wilson no-go: it adds an explicit symmetry-breaking, nonzero matter source and assumes its burden pattern is sustained. The proof is **conditional existence** in a newly constructed action, not emergence from O09. It also does **not** imply a unique physical coupling or an identified photon sector.

**Small-coupling consequence:** For generic fixed `b`, after fixing vertex-gauge directions, the Hessian at `alpha=0,g=0` is `kappa B2B2^T>0` on `Z`. The implicit-function theorem gives a unique nearby phase stationary point with

`Phi = (g/kappa) t(b) + O((g/kappa)^3)`.

This predicts a **cubic leading source contrast** conditional on the choice of coupling, not a measured discrepancy or native physical constant.

## 7. OPTIONAL mathematical flow — full stock and work receipts (not O09)

It is possible to make a complete *conditional* dissipative mathematical model without violating conservation, but this does not establish native adoption. Let `E(alpha,b)=V(alpha,b)` including a separately declared fixed `U_B(b)` and let `mu_b,mu_alpha>0` be independently chosen event-mobility constants. Put

`dot b= -mu_b B1 B1^T nabla_b E`, `dot alpha = -mu_alpha nabla_alpha E`.

Then, with `j_b=-mu_b B1^T nabla_b E`, `dot b=B1 j_b`, so

`d/ds [sum_i b_i]=0`,

`dot E = -mu_b ||B1^T nabla_b E||^2 -mu_alpha ||nabla_alpha E||^2 <= 0`.

If an explicit sink stock `E_sink` obeys `dot E_sink=-dot E`, the total `E+E_sink` is **exactly** constant. Gauge invariance ensures `nabla_alpha E` lies in the edge-cycle subspace. These are source/sink **accounting** identities for a declared gradient flow; the mobility, burden storage, native time, phase-to-Hodge map and physical energy unit have not been selected. This is not secretly the O09 canonical evolution.

## 8. Decisions, counterexamples and next required gate

**EXACT / AUTO_LOCK proposed only within declared proof scope:** the `S4` cubic-selection theorem and explicit `J_cub` continuity/Bianchi identities have complete algebraic proofs and two calculation routes; they can be submitted as a scoped mathematical theorem without physical promotion. Independent non-constructor review remains required by project governance before broader acceptance.

**NO-GO:** O09 alone, without a Hamiltonian and modal-to-link phase map, cannot uniquely determine a local edge source. Lower-degree equivariant vertex-scalar sources vanish on the declared single-field carrier.

**CANDIDATE:** `-g t sin Phi` and the dissipative completion demonstrate a legal local, gauge-respecting source architecture, not an action derived from O09 or the historical G05. Identical burden values force `J_cub=0`; a cubic source cannot persist unless native burden dynamics actually produce and retain nonuniform vertex values. Uniformizing background or restored `S4` symmetry returns the null.

**OPEN_GATED:** (1) derive or reject a source map from accepted current burden state to `b in C0`; (2) derive `g/kappa` and/or a source-selected face action from O09/Q136 without target fitting; (3) derive an O09 modal-phase-to-link-phase intertwiner respecting carrier and action units; (4) specify physical clock/lapse and two-polarization propagation on glued 3D spatial complexes; (5) preregister line/covariance/redshift tests against independent data. **Physical promotion remains 0.**

## 9. Versions and evidence

- Current recovered O09 source: `https://unified-dynamics-public.ben-w-mayes.chatgpt.site/evidence/ledger-recovery/` and `https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/ledger-recovery-v0.1/library_LEDGER_v0.85.json`, row **O09**, G05, Q140. The filename says v0.85, internal scientific_revision v0.43; source custody was independently checked in the project's dated recovery record. These are source entries, not independent proof review.
- Local uploaded `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (2026-08-22), Q140, Q153–154, G05, original SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`.
- Previous K4 Wilson-branch audit `UD_FACE_RESPONSE_ACTION_AUDIT_v0.1`, 2026-10-31, §2–7, source-history branch, SHA-256 manifest and full two-page PDF; review PR `https://github.com/ud-tetra/UD/pull/471`.
- Present computations: `verify_cubic_source.py` (independently generated incidences, exact 24-element covariance, character multiplicities, explicit current) and `independent_action_check.py` (separately hard-coded incidences, O09 first variation, exact nonflat source-balance example, symbolic gradient/stock/sink receipts). Both executed successfully.
- No CODATA/Planck/DESI value, lepton mass, bare UD fraction or detector error was used in deriving any result. No new physical prediction has been verified.
