# UD Forward-Selection and Four-No-Go Source Audit — v0.1

**Date:** 2026-11-19. **Scope:** source-bound finite mathematics; source-authenticated event admission is not established. **Status:** EXACT_CONDITIONAL / NO-GO_SCOPED / OPEN_GATED. **Physical Promotion:** 0. **Lane:** development, no accepted-registry amendment.

## 1. Source identities and version control

- **UD main:** `cef84ca5c996ec21b67247c74ee85c2c6c5dd995` (2026-11-18), especially `docs/governance/UD-SCOPE-001-observable-domain-falsifiability.md` and append-only capture governance. Read source; no writes to frozen files.
- **UD-Physics integrated:** `03722496f5b00e8f3f01b2400e4015eb65fdebc4` (2026-11-18), `BOOTLOADER.md`, Discovery v1.2, `docs/UD_MATHEMATICAL_METHOD_v1.0.md`, concurrency v2.0. Reading existing sources is not evidence of claim ownership.
- **Recovered ledger:** `UD/captures/2026-10-21T151000Z-codex-exit03-recovery-98dc7b12/library_LEDGER_v0.85.json`, Git blob `93e2ca31eba625989087275a71c4857848e321c6`, 723 objects, 87 `LOCKED_NO_GO` bins, physical promotion 0; internal `scientific_revision=v0.43`. The claimed label `v0.85.2` is NOT independently source authenticated.
- **POC-1 native event source:** `TETRAHEDRAL_PACKET_COMPLEXES_JOP_LEAN_MANUSCRIPT_v2.5_POC1_LAB_IMPLEMENTATION_READY.md` (personal Library `libfile_eb315486c110819199861a466b40fc3c`), §§4.4–4.5. Explicitly constitutive candidate, not an authenticated event or endpoint fixture.
- **Hinge calculation:** `UD_POC1_IDLE_HINGE_ACTION_AUDIT_v0.1.md` (personal Library, 2026-11-19, §2). Exact conditional mask and two input preparations.
- **Edge strain:** `EDGE_STRAIN_TO_SUPPORT_AMPLITUDE_CONSTITUTIVE_SOURCE_AUDIT_v0.1.md` (personal Library `libfile_2ee214edca088191a0456621df881b4a`), §§2–4, 8–9: support-to-shape readout available; reverse strain-to-support and gate law OPEN.
- **Additional audit:** [UD PR #490](https://github.com/ud-tetra/UD/pull/490), `proofs/milestones/UD-PM-PRED06-SEL-001_v1.0.md`, exact symmetry obstruction (PR open/stacked, independent review deferred); [UD PR #57](https://github.com/ud-tetra/UD/pull/57), source spectral correction (open and not accepted canon); [UD PR #329](https://github.com/ud-tetra/UD/pull/329), merged provenance recovery; [UD PR #472](https://github.com/ud-tetra/UD/pull/472), candidate cubic source (open/draft).
- **Identifier collision:** `POC-1` denotes a different experimental scorer custody in [UD issue #147](https://github.com/ud-tetra/UD/issues/147). In this report use `POC1_CONSTITUTIVE_HINGE`, not a global bare `POC-1`, and do not rename pre-existing source objects.

## 2. Typed mathematical question and completeness contract

Let `K` be a finite filled simplicial complex; source state `x` comprises its **specified** binary/framing/register state and, when available, edge amplitudes, seam links, burden, gate integrity, pre-event source receipts and event-boundary evidence. These are not automatically coordinates of `X_1=S4×Theta` (a distinct 192-exposure set). Specify a finite set of source-*admitted* histories `H(x)`, an action `S_x:H(x)→R`, a terminal map `end:H(x)→Y`, and an allowed quotient `q:Y→Y/∼`. A proposed deterministic minimum-action **observable** selector exists iff:

`H(x) != ∅`, `M(x)=argmin_{h∈H(x)} S_x(h) != ∅`, and `|{q(end(h)):h∈M(x)}|=1`.

This is EXACT as a characterization; it is NOT a native construction of `H`, `S`, event occurrence, or the admissible quotient. If `M` contains different histories mapping to the same observable endpoint, observable selection is unique but history selection is not. If `M` contains two endpoint classes, there is no deterministic observable selection without additional data or a separately sourced rule. The action need not be differentiable on finite H; `δS=0` requires its own variation prescription, and stationary points need not be unique minima.

An invariant state with stabilizer `G_x` and invariant action yields orbit-constant costs. Uniqueness requires a singleton **entire minimizing endpoint image**, not constancy on individual symmetry orbits. Counterexample: `G=C2` exchanges `a↔b` and fixes `c`; `S(a)=S(b)=S(c)=0`, `end(a)=end(b)=0` and `end(c)=1`.

## 3. Exhaustive symmetry tests on native toy state spaces

**Declared toy:** raw *vertex* assignments `b∈(Z2)^V`, with **every** filled-tetrahedral triangular face required to be nonmonochromatic. Minimum allowed nontrivial changes flip the fewest vertex bits while remaining admitted. This is a source-admissibility toy, not the full dressed `S4×Theta` carrier and not a physical event law. Group actions are automorphisms of each **filled complex**.

- `K4=[0123]`: 6 admitted of 16 raw assignments (exactly two 1-bits); no admitted 1-bit moves. All 6 belong to one connected admissible minimum-2-bit graph, each with **4** neighbors. The stabilizer is transitive on a state's 4 allowed neighbors, so equivariance forbids selecting exactly one neighbor from its fully symmetric preparation. Conditional *given that an event happens and moves to one minimum neighbor*, a symmetric Markov kernel assigns each `1/4`. The total outgoing hazard `λ(x)≥0` is unselected.
- `Kminus=[0123]∪[0124]`: 5 vertices, 9 edges, 7 faces, 2 cells. 6 admitted of 32 raw assignments; no admitted 1-bit moves. The minimum-2-bit graph is **two disconnected triangles**; every state has **2** neighbors. Automorphism group is `S3×C2`, order 12, and its stabilizer is transitive on either successor pair. Conditional probabilities are `1/2` each; the event hazard and transition between components remain unselected.
- **Explicit generator nonidentifiability:** On either graph set `Q_λ(x,y)=λ/d(x)` for allowed neighbor edges, `Q_λ(x,x)=-λ`, other entries zero, any native positive **dimensionless** scalar `λ`. Both `λ=1` and `λ=2` satisfy identical admissibility, covariance, and source-free probability normalization, and have different relaxation times. These constants are **adversarial counterexamples**, not UD coefficients. An event count or graph automorphism does not define a physical clock.

**NO-GO_SCOPED:** No deterministic equivariant *single* nontrivial successor from such a state under those assumptions. Allowing a hold/no-event option, source asymmetry, added history, boundary fields, or stochastic rules changes the hypothesis. Merely choosing a uniform stochastic branch does not derive the event trigger or rate.

## 4. Hinge kinetic action: exact tie is stronger than a static degeneracy

On the **filled** `K4` chain space `C=R^15` with increasing simplex orientations and unit coefficient metric, let `A=∂−∂ᵀ` (skew), `P` the two-edge projector onto `01,23`, `Q=I−P`. Define **candidate branch dynamics**

`c_o(s)=exp(sA)c`, `c_c(s)=exp(sQAQ)c`, `0≤s≤τ` with a common dimensionless interval `τ>0`. For `Pc=0`, the exact kinetic action `S_g=(1/2)∫||dot c_g||² ds = (τ/2)||A_g c||²` obeys

`S_o−S_c=(τ/2)||PAc||²≥0`.

Exhaustive integer-matrix tests of two source-given preparations: with edge `e_02` amplitude 1 and other edge/face/top coordinates zero, all vertex amplitudes 1 yield open/closed speed squares `(4,4)` and exact action **tie**; vertex amplitudes `(1,2,1,1)` give `(7,6)` and `S_o−S_c=τ/2`. In the tie, `Pc=PAc=0` and `A²c=−4(c−h)` with `h=(1,1,1,1;0...)`, so the cyclic subspace never enters `P` and **the complete nonstationary chain trajectories are identical**. Parity endpoint labels can still be *declared* different.

**CRITICAL ADMISSION GATE:** `T_p=1` is supplied; `L_p=0` holds for the pair due to zero tested edge amplitudes. POC-1 §4.5 *hypothesizes* that positive latent pair support obligates opening; its endpoint convention may authorize closure at the hinge. Neither history pair has been established as **simultaneously admitted** in a source-authenticated event. Therefore this conditional tie is neither a falsification of POC-1 nor a proof of its closure. It falsifies the **stronger unsupported assertion** that this Hodge kinetic term **alone** strictly favors one parity endpoint for every such hinge state. Matching strain=0 is a readout convention, not a sourced branch-work law.

## 5. Exact four-no-go reconciliation

1. **Q35 / G05:** v0.85 ledger `Q35` defines the endpoint defect `1−ReTr R(H)/d`; `G05` is a retired universal scalar proportionality to accumulated action. `O09` is the separate lifted history action `I_lift=(1/2)Σ a_ω Δφ̃_ω`, which can distinguish winding discarded by a finite endpoint image. The universal endpoint-defect→action scalarization is the locked obstruction. The unqualified assertion `G05 = parity blindness of an opponent's path filter` is **not source-authenticated**.
2. **Pachner / Q174–Q176:** on the unit-metric *global unique-simplex* skew Hodge operator, filled K4 squared frequencies are `4 (×14), 0 (×1)`; two-tet Kminus `3 (×8), 5 (×14), 0 (×1)`; three-tet Kplus `2 (×4), 5 (×22), 0 (×1)`. These correspond to eigenfrequencies `±i√3 (×4 pairs), ±i√5 (×7 pairs)` on Kminus and `±i√2 (×2 pairs), ±i√5 (×11 pairs)` on Kplus. The combined radicand `7` in the user's proposed narrative is not supported by these exact carriers. Each glued carrier has no finite positive common recurrence because the two positive squared frequencies have an irrational square-root ratio. This is a **same fixed-operator recurrence obstruction**; the combinatorial 2↔3 move is not the evolution `exp(sA)` and does not itself define a clock.
3. **No-Go 7.4 label:** no verified current GitHub source connects this specific numbered theorem to retrospective bit-offset matching. A separate algebraic lemma is true: for any prescribed endpoints `θ_i,θ_f`, choosing `a=θ_f⊕P_r θ_i` reconstructs them, so after-the-fact reconstruction is not a pre-event selection theorem. It does **not** prove a unique governing law absent an independent predicate. This lemma must not be stamped `LOCKED_NO_GO #7.4` without the exact version/section.
4. **Undressed gauge:** requiring all four **unsigned** face vertex sums `θ_i+θ_j+θ_k=0 mod 2π` for a single K4 gives integer constraint matrix Smith diagonal `(1,1,1,3)` and only global third-root phase states. **EXACT_CONDITIONAL:** the collapse follows from that *specific* undressed constraint, not all gauge models. Independent U(1) 1-cochain links with `U'ij=g_i Uij g_j^{-1}` permit covariant plaquettes, but they do not by themselves define the physical gauge sector or an evolution law.

No result is promoted by applying these observations to uninspected Gibsonian source mathematics. The structures of different proposed frameworks cannot be declared identical merely because they share tetrahedra or clock language.

## 6. Acceptance contract and next discriminant

Do **not** let a chosen action supply its own admission predicate or endpoint quotient. Before a physical-facing claim, require an authenticated pre-event packet `(x, T, Λ, ρ, U, χ, gate, clock)` with source version and timestamp; an independently sourced event-occurrence rule; an exact local history admission predicate (including both hinge candidates if the tie is to be tested); branch-dependent work/current/receipt, if any; source-budget conservation; an explicit observable endpoint projection and admissible quotient; and a target-blind criterion for when action or probability resolves all admitted histories. Test the matched nonstationary hinge and strict comparison alongside open/sham and asymmetric-preparation controls. If only one branch is admitted, action selection is not the reason for its exclusivity; attribute the result to admission. If two admitted branch endpoints have equal action, deterministic least-action selection is **unclosed** and a stochastic or additional pre-event source rule is required. A different branch-dependent strain law is a **new versioned candidate** until derived from source.

Verification: local `python verify.py` (SymPy exact matrices, Smith form, finite enumeration, exact eigenspectra) and independent pure-standard-library `python replay_stdlib.py` passed. Constructor-context replays only; separate non-constructor review and GitHub CI pending. `Physical Promotion = 0`.
