# UD PRED07 — Symmetry-breaking burden amplification and a sector-sensitive action: proof audit v1.0

**Date:** 2026-11-01. **Lane:** D0 mathematical development. **Proof status:** three new EXACT_CONDITIONAL milestones. **Review:** DEFERRED. **Physical promotion:** 0.

## RESULT

Two distinct requested proof obligations were tested using the typed Q153/Q162/Q169/G05 source interface and the previously captured PRED06 no-go results.

**Burden evolution:** The admitted, all-open Q162 mixing equation alone dissipates a K4 burden difference and cannot leave a perfectly homogeneous state. We constructed a **new**, conservative and S4-equivariant quadratic burden redistribution source that has an unstable uniform equilibrium for `gamma*M>4` and amplifies arbitrarily small, initially present asymmetry to a strict comparator threshold. It does **not** choose a unique address from exact symmetry, derive the gain, or cause cell excision.

**Action:** We proved K4 symmetry plus unit basis-edge norms does not uniquely determine a general cochain metric. A gauge-invariant period-squared action **can** separate integer winding sectors without curvature, but its noncompact winding lift and coefficient `tau` are new inputs. Consequently no source-complete absolute stiffness or physical action follows. Equality to the earlier harmonic quadratic action yields inverse matching `kappa_N=tau/P_N(G)`, not an independent derivation.

## 1. Authoritative sources and their limits

| Typed object | Exact source | What it supplies | What it does NOT supply |
|---|---|---|---|
| K4 and S4 | v0.39 source ledger P01-P04 (2026-08-22; SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`) | Four vertices, six edges, vertex permutation group | A preferred vertex or port from fully invariant data |
| Continuity | Same ledger Q153, line 235 | `Delta rho=B j_B+s_B` | Constitutive predictive source law |
| Conditional flux | Same ledger Q162, line 244 | `j_e=-(1/4)h_e(B1^Tb)_e` | The gain `gamma`, nonlinear reactions, physical clock |
| Fixed-carrier support | Same ledger Q169, line 251 | Skew Hodge–Dirac incidence and support norm | A topology-changing cell rule or sector-action metric |
| Master action weight | Same ledger G05, line 110 | Quarantined candidate; explicitly open action map | A proved coefficient `tau`, `kappa_N` or SI-energy map |
| Prior selector proofs | UD PR #490, commit `51c1885a140f732a9518760e1e3fcb2f431e2832` | S4 symmetry no-go; conditional burden/flux comparator; harmonic-action blindness | Endogenous source and stiffness |
| Prior carrier scaling | UD PR #487, commit `e3b74a8069d37807b92d184e3cab26df9b5817f9` | Unit-edge log norm bound on specified punctured carrier | Absolute native action coefficient |
| Historical recovery note | `docs/UD_Native_Gate_Trigger_and_Recovery_v0.1.md`, blob `4a16adf2a310da5f327fe9286e458fe3aba71161` | Hard gate factor/source ambiguity and recovery obstruction | Source-complete trigger/restoration evolution |

These dates and versions are source snapshots. The PRED06/PRED05 results are in **unmerged** PRs, and none of the source objects is promoted to a physical correspondence in this audit.

## 2. New exact proof milestones

- `UD-PM-PRED07-BUR-001_v1.0`: source-Q162-plus-*new* quadratic local redistribution; conserves total nonnegative burden, is S4-equivariant and amplifies generic perturbations if `gamma*M>4`. Uniform initial conditions remain fixed. The generator is not native-derived.
- `UD-PM-PRED07-MET-002_v1.0`: the K4 edge space admits distinct S4-invariant positive metrics even after every edge basis vector has norm one. Symmetry and edge normalization alone do not fix cochain action geometry; Q169's support metric cannot be silently identified with an action metric.
- `UD-PM-PRED07-ACT-003_v1.0`: a gauge-invariant nonlocal period term gives an exact `n=2` to `n=3` gap of `5*tau/2`, but requires a noncompact lift and a free, unsourced coefficient. Its existence does not prove the native master action.

## 3. Mathematical discrimination and resource limits

The candidate quadratic redistribution is *internally conservative*: its source-vector sum is zero, and on K4 it can be written as `s=B1(B1^T s/4)`. This identifies it as an additional **packet redistribution current**, not a new nonconservative incoming burden reservoir. Increasing burden variance is not by itself a proof of conserved energy; no dissipation/power/heat ledger is provided.

The 24 S4-permutation checks confirm covariance but do not prove that a homogeneous state spontaneously acquires an orientation. The exact ODE proof establishes **the opposite**: exact uniform data stay uniform. The selected vertex and outgoing port on generic trajectories originate in small, unprescribed initial asymmetries; their statistics and amplitude are source-open.

The proposed period action `tau*(period)^2/2` is gauge-invariant on a *closed* cochain space with a selected integral homology generator. It is not a local curvature-only term and cannot be read by the compact Wilson observable `exp(2*pi*i*n)=1` on integer periods. Its claimed gauge invariance is only under single-valued real exact cochain shifts; compact U(1) *large* gauge transformations that identify `n` with `n+1` do **not** preserve the period-squared action. An unwrapped sector must be independently sourced. A noncompact/historical winding register is additional data.

## 4. Assumption gates and next source theorem

1. Derive a physically or natively admitted source of initial symmetry-breaking burden fluctuations, or a stochastic kernel whose outcome distribution is S4-equivariant and whose event selection is generically unique. **Do not represent a single labeled realization as selection from a perfectly invariant deterministic state.**
2. Derive the nonlinear packet redistribution coefficient `gamma` and a resource/action ledger. The source Q153 residual equation cannot be inverted into a unique law by demanding contrast growth.
3. Derive from admitted parity/burden transport an actual supported-cell occupancy transition, including legal restoration and trail permanence; selecting a burden comparator is not a cell-excision proof.
4. Derive a typed integer winding lift and globally consistent cycle readout; native Z2^3 parity alone is insufficient.
5. Derive a source-defined action metric and coefficient (or test a physical bridge with units, calibration, uncertainty and held-out null), then compare the period action with the prior harmonic-norm scaling **without post-hoc matching**.

## 5. Verification

- Main exact audit: 24 S4 permutations, K4 Laplacian/projector identities, conservative-source expression, exact instability threshold, fixed-point, metric and gauge-invariance identities.
- Independent-method exact check: Fraction arithmetic, independently constructed K4 matrices, an exact nontrivial edge cross-term and a separate cycle-period computation.
- Numerical, **synthetic** ODE control: symmetric uniform preparation, unstable `gamma=2`, stable `gamma=1/2`, fixed mass/positivity and initial rank order. Late low-mode numerical differences reach floating precision; exact rank preservation comes from the proved scalar contrast equation, not solver output.
- 19 scoped tests passed locally. No physical experiment, independent non-constructor review or theorem promotion beyond declared conditional scope.

**Physical promotion remains 0.**
