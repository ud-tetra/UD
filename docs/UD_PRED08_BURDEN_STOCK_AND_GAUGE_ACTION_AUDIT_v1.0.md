# UD PRED08 — Burden gain, resource stock, and winding action source audit v1.0

**Date:** 2026-11-01. **Scope:** UD proof-first development D0. **Physical promotion:** 0. **Independent non-constructor review:** DEFERRED. **Source authority:** established mathematical facts remain scoped to their exact version; proposal authority does not establish physical truth.

## RESULT

**No source-complete endogenous gain/action coefficient was derived.** The admitted Q162 passive current cannot amplify a perfectly symmetric burden state or make contrast increase; Q153/Q158 leave the constitutive source open. A new conservative, finite-stock active redistribution and an S4-in-law stochastic preparation give an **exact conditional** construction of a unique seed and port, but the event and its cost are *added premises*. The same model has an exact dissipation no-go preventing permanent burden contrast with finite initial resource.

On a carrier with H1=Z, a compact U(1) edge-link state does not determine an unwrapped integer winding lift. A new relative reference can make a period action invariant under an explicitly restricted diagonal large-lift group, but it introduces a second typed carrier and retains a free action coefficient. Exact 0-cochain gauge updates cannot change the winding sector on a fixed complex. These results constrain but do not complete the native UD sector action.

## 1. Explicit versioned sources and limits

| Object | Source | Source-supported mathematical content | New / OPEN input |
|---|---|---|---|
| K4/S4 symmetry | Coefficient provenance ledger v0.39 (2026-08-22), P01-P04, SHA256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63` | Four vertices, six edges, 24 S4 permutations, eight opposite-edge parity states | No unique seed or unbounded integer lift |
| Burden balance | Same ledger Q153/Q158 | Delta rho = B j_B + s_B; s_B residual is not a predictive law | Constitutive source/gain and physical unit map |
| Passive current | Same ledger Q156/Q162 | j_B,e=-(1/4)h_e(B^T b)_e as conditional relaxational burden lane | Trigger and histories for hard gates |
| Support and fixed incidence | Same ledger Q165/Q169 | Unit-simplex support norm; fixed-carrier skew Hodge–Dirac | Distinct burden-action metric and topology-change law |
| Action weighting | Same ledger G05 and Q31 | Loop diagnostic distinct from master action weight | Absolute sector coefficient, physical calibration |
| Positive buffer model | `ud-tetra/UD/docs/UD_Positive_Stock_Balanced_Recovery_and_Predictive_Switching_v0.1.md`, 2026-10-15, §§2–4, blob `2f0bcbbf3af39b65bd507aeb511f7dfea93205f0` | One **new assumed** normalized storage/exchange model with conserved ledger | No unique packet gain or reserve choice is recovered |
| Symmetry/selection | `UD-PM-PRED06-SEL-001/002`, open PR #490, head `51c1885a140f732a9518760e1e3fcb2f431e2832` | Deterministic fully symmetric selection impossible; conditional burden/flux comparator | Initial asymmetry, threshold, context |
| Nonlinear active candidate | `UD-PM-PRED07-BUR-001`, open PR #491, head `b56f892b5fe9fbc9059ebd0f83a9113f6f4867a0` | Conservative modeled gain when gamma*M>4 without finite stock | Gamma, source budget, initial perturbation |
| Period action | `UD-PM-PRED07-ACT-003`, same PR #491 | Noncompact exact-shift-invariant period square with free tau | Integer winding lift, compact gauge compatibility |
| Harmonic/metric | PRED05-SCALE-002 and PRED06-MET-006, unmerged stacked PRs #487/#490 | Logarithmic cochain norm on specified punctured family with declared metric | Absolute action stiffness and physical energy |

The designated UD portal (https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/) continues to display physical promotion 0 and papers I–III 1.1.1 / IV 0.1 at this access; it does not accept or merge these proof proposals.

## 2. Five exact, separately typed mathematical milestones

**PRED08-BUR-001 / NO-GO:** For source-free Q162 with nonnegative contact masks, variance V is nonincreasing, with Vdot=-(1/4)||sqrt(H) B^T b||². Exact uniform remains uniform.

**PRED08-RES-002 / EXACT_CONDITIONAL:** Introduce Euclidean contrast stock V (distinct from Q165 carrier support energy), reserve R, dissipated stock D and a finite availability u(R)=R/(R+R*), R*>0. The active source s_i=gamma*b_i*(b_i-Q/M) conserves M and has nonnegative concentration-production scalar A=sum b_i³-Q²/M. Let the reserve pay gamma*u*A and D receive passive dissipation. Then V+R+D is conserved and initial contrast eigenvalues are -1+gamma*M*u(R0)/4. A uniform random ordered edge transfer epsilon produces a unique seed/port, conserving mass and debiting epsilon² from R. This is an **added stochastic rule**, not a sourced UD mechanism.

**PRED08-ASYM-003 / NO-GO:** Since Ddot=2V for all-open K4 and D is bounded by finite E0, integral V dt≤E0/2 and V(t)->0. The total model time spent with burden span≥delta is ≤2E0/delta². Finite conserved reserve permits transient growth but not a permanent nonzero contrast under these assumptions.

**PRED08-GAU-004 / NO-GO + CANDIDATE:** Compact edge links exp(2pi i a_e) identify integer edge lifts a and a+z, even when the periods differ; period-squared action is not compact-link-only. A second noncompact reference r and *diagonal* correlated lift shifts keep the relative period q=<a-r,Gamma> invariant. This changes the mathematical state/gauge group; independent integer shifts would invalidate it. Tau remains arbitrary.

**PRED08-COH-005 / NO-GO:** Fixed-carrier exact gauge updates a->a+d phi preserve the period on all cycles. A 2->3 winding transition requires a nonexact cohomology increment, nonclosed intermediate evolution, a topology change, or a separately declared source. A positive action gap does not itself supply a dynamical transition.

## 3. Typed null comparisons and failures

- **Null A:** Pure Q162/passive nonnegative mobility; predicts no contrast growth or symmetry breaking from uniform burden.
- **Candidate A:** PRED07 unbudgeted nonlinear redistribution; mathematically active but missing energy/source accounting.
- **Candidate B:** PRED08 finite-resource redistribution plus stochastic seed; complete *declared normalized stock ledger*, yet no native gain source, physical clock, cell excision or persistent contrast. Its kinetic coefficients/units are assumptions, not calibrated physics.
- **Null B:** Compact U(1) links only, no extra unwrapped register; cannot identify integer lift.
- **Candidate C:** Enlarged relative winding reference; well-defined under a *diagonal* gauge group but not sourced from K4 parity or G05.
- **No automatic physical identification:** neither candidate amplitude gamma nor period coupling tau follows from a number in the coefficient ledger. The Q165 support metric and new burden V are different typed objects.

## 4. Reproducibility and review boundary

- `verify_pred08.py`: SymPy 1.14 symbolic exact checks, S4 covariance, incidence identities, reservoir-ledger differential, stability, period and cohomology witnesses.
- `independent_exact.py`: separate standard-library fractions/permutation enumeration, 624 nonnegative burden grid points times 64 gates (39,936 source-passivity examples), 12 ordered edge jumps times 24 permutations, 125 exact vertex-potential updates.
- `test_pred08.py`: 24 unit tests; all PASS. These finite tests are not the general proofs.
- `numerical_control.py`: optional SciPy normalized example; finite gain then decay with accounting error <1e-10. **Synthetic only**; no physical data.
- `EXACT_AUDIT.json`, `INDEPENDENT_AUDIT.json`, `NUMERICAL_CONTROL.json`: exact and numerical receipts. Hashes in `MANIFEST.json`.

## 5. Precise reopening criteria

1. **Endogenous seed/gain:** Find a source-authorized nonpassive constitutive term or stochastic packet event with an explicitly conserved **native** budget, initial law and local gate evolution; if unprovable, retain passive-mixing no-go.
2. **Persistent defect:** Show a protected occupancy, topological barrier or external renewal that survives the finite-stock contrast-decay theorem under declared dynamics, rather than assuming permanent burden contrast.
3. **Gauge/sector action:** Source a typed noncompact unwrapped reference or an alternative gauge-invariant physical winding observable, define permitted gauge transformations and sector transitions, and fix the action coefficient/metric without inverse matching.
4. **Physical bridge:** Define calibrated measurement, uncertainty, baselines, falsification thresholds and held-out test. No correspondence is promoted without its own independent evidence.

**Research status:** Five new exact scoped mathematical records. Non-constructor review remains DEFERRED. Physical promotion remains **0**.
