# THM-534 v1.2 — Glued Face-Contact Reset and Owned-Support Source Gate

**Date:** 2026-10-21 · **State:** EXACT conditional finite algebra, EXPLICIT CANDIDATE RESET, scoped NO-GO · **Review:** constructor-only, independent non-constructor review pending · **Physical promotion:** 0 · **Lane:** development/no registry promotion.

**Source-bound dependencies:** `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, Q169–Q173 and Q177–Q179 (and Q170 support control-volume); [THM534_FACE_CORE_RECEIPT_GATE_v1.1.md](THM534_FACE_CORE_RECEIPT_GATE_v1.1.md), S42–S48. The historical THM-534 transition-probability derivation is still SOURCE-BLOCKED. This is target-exposed mathematical exploration, not a preregistered physical bridge.

## Typed construction and conventions

Let `Kminus` comprise the two *filled* tetrahedra τ0=[0123] and τ1=−[0124] (opposite cell orientations across their shared face), glued on face f*=[012]. The unique simplices have `f=(5,9,7,2)` and total chain dimension `23`, as in the frozen Kminus register. Face order:

`(012,013,014,023,024,123,124)`.

The global signed face–cell incidence `D=B3:C3=R²→C2=R⁷` is

```text
             τ0 τ1
012          -1 +1
013          +1  0
014           0 -1
023          -1  0
024           0 +1
123          +1  0
124           0 -1
```

A face–cell **contact gate** `h_(f,τ)∈{0,1}` is defined only where `D_(f,τ)≠0`; there are **eight** such contacts, not seven. Let `M=D∘H` (entrywise product). The original chain topology and `D` remain fixed when contacts close. The auxiliary face/core state `(z,t)∈R⁷⊕R²` evolves by the skew generator

\[
A_H=\begin{pmatrix}0&-M\\M^{\mathsf T}&0\end{pmatrix},\quad
u^+=\left(I-\tfrac18 A_H\right)^{-1}\left(I+\tfrac18 A_H\right)\nu,
\quad \nu=(z,t),
\]

with an explicit **dimensionless** event-step `ε=1/4`. The step is a candidate exact integration of the sourced support bilinear Q171–Q173; its event clock is **not physical time**. This is not a law for the hard-contact bits themselves.

Define for face f and cell τ the *actual completed midpoint support transfer*:

\[
J_{f\tau}=2\varepsilon M_{f\tau} z_f^{mid} t_\tau^{mid}.
\]

Here `z_f²` is face-interface support and `t_τ²` is cell-core support. The total `||z||²+||t||²` is a different carrier from vertex-burden stock, physical energy, or the previous THM-534 six-edge stochastic readout.

## THM-534-S49 — Exact gluing, multiplicity ownership and partition of support [EXACT]

For each unique simplex σ of Kminus, let `n3(σ)` be the number of tetrahedral cells containing σ, and set `w_(σ,τ)=1/n3(σ)` when `σ⊆τ`, otherwise zero. Then, for any amplitudes `(c_σ)` on the unique simplices,

\[
\sum_{\tau\in\{\tau_0,\tau_1\}}\sum_{\sigma\subseteq\tau}w_{\sigma\tau}|c_\sigma|²
=\sum_{\sigma\in Kminus}|c_\sigma|².
\]

**Proof:** each σ has exactly `n3(σ)` containing cells, so the sum of its weights is one. The shared face has `w=1/2` on each cell; each unique face has weight one on its containing cell. This is precisely the Q177–Q178 ownership identity, not new physical evidence. QED.

## THM-534-S50 — Exact finite-event and equal-share flux receipts [EXACT CONDITIONAL]

For every gate mask, Cayley step and finite initial state, the face and cell support balances are

\[
\Delta(z_f²)=-\sum_\tau J_{f\tau},\qquad
\Delta(t_\tau²)=\sum_f J_{f\tau}.
\]

Define owned face/cell stock `S_τ^owned=t_τ²+Σ_{f⊂τ}w_(f,τ) z_f²`. Then

\[
\boxed{\Delta S_\tau^{owned}=\sum_f\left(J_{f\tau}-w_{f\tau}\sum_{\tau'}J_{f\tau'}\right),\qquad
\sum_\tau\Delta S_\tau^{owned}=0.}
\]

**Proof:** real skewness of `A_H` makes Cayley orthogonal; the midpoint polarization identity gives each support change exactly. Substituting the ownership weights yields the displayed cell-wise formula. Summing over cells cancels every face receipt since `Στ w_(f,τ)=1`. QED. The identity is the finite-event counterpart to Q179, and requires no independently invented physical source.

## THM-534-S51 — Global contact-dead reset obstruction [EXACT / NO-GO]

**Hypotheses:** all eight face–cell contact gates vanish at event n; the face/core state receives no independent boundary/source forcing; the next gate selector uses only *actual completed contact transfer receipts* and sends an all-zero receipt vector to all-zero gates. Then

\[
A_{H_n}=0,\quad \nu_{n+1}=\nu_n,\quad J_{n}=0,\quad H_{n+1}=0.
\]

Inductively the all-contact-dead state is absorbing. This remains true even if the inactive carrier contains nonzero stored support amplitudes. Zero support with arbitrary gated bilinear contacts is a separate absorbing case. QED.

**Limits:** A rule that senses latent amplitude, closure history, an *ungated prospective* bilinear, a surviving edge–face contact, an external source/boundary receipt or a new reset clock is outside these hypotheses. The no-go is about **receipt-only** reset and cannot be generalized to every imaginable packet source.

## THM-534-S52 — Unshared-face-to-shared-face conditional reset witness [EXACT CONDITIONAL]

Fix face amplitudes `z_012=z_013=1`, all other face amplitudes zero and both cell amplitudes zero; total support norm is 2. Initially admit only the *unshared* contact `(013,τ0)`; both contacts of shared face `012` are **off**. At `ε=1/4`, the exact midpoint Cayley step gives

\[
t_{\tau_0,1}=\frac{16}{65},\qquad
\Delta(t_{\tau_0}²)=\frac{256}{4225}>0,\qquad
z_{012,1}=1.
\]

**Constructive candidate event rule:** permit `(012,τ0)` on the *next* event iff the *previous, independently admitted* unshared-face contact produced positive completed core-stock gain; keep `(012,τ1)` disabled. Then on event 2 the newly admitted shared-face transfer is

\[
\boxed{J_{012,\tau_0}=-\frac{61824}{511225}\neq0.}
\]

The actual sign is **negative** (cell-to-face), so this witness establishes a contact reopening and nonzero current, **not** a positive shared-face ingress. Its exact owner deltas are `−30912/511225` and `+30912/511225`. QED by direct rational midpoint evolution.

The source of the first current is the independently admitted `(013,τ0)` contact. The shared-face reset rule is an **additional chosen constitutive predicate**, not a theorem that Q173 or Q177 selects it. A no-reset rule applied to the identical first state/receipt is also compatible with support continuity and would keep `J_012,τ0=0` on event 2. This is a counterexample to claimed uniqueness of Q173 reset semantics.

## THM-534-S53 — Shared-face ownership transfer despite disabled neighboring contact [EXACT / TYPED WARNING]

For a shared-face current pair `a=J_(012,τ0)` and `b=J_(012,τ1)`, the shared-face contribution to the owned-support changes obeys

\[
\boxed{(\Delta S_{\tau_0}^{owned},\Delta S_{\tau_1}^{owned})_{012}
=\bigl((a-b)/2,(b-a)/2\bigr).}
\]

Even if `b=0`, each owner has an equal-and-opposite **accounting** change `(a/2,-a/2)` because the interface reservoir is jointly owned. It is *not* evidence for a physical flow **through** the τ1-disabled contact. The total global support remains exactly conserved. QED by Q177 ownership plus S50.

## THM-534-S54 — Finite admissible-contact family and reset nonuniqueness [EXACT / NUMERICAL]

There are eight face–cell incidences on the two-cell carrier, so exactly `2^8=256` binary gate masks. A separately implemented exact rational solver checked **every mask** against all seven local face receipts, both cell receipts, and both owned-support changes on one fixed nonzero initial state. All passed. This is scoped exact finite enumeration, not a theorem on all source histories beyond the already proved S50.

Two distinct reset conventions—for example the conditional shared-contact admission in S52 and permanently closed shared contacts—give different subsequent currents from the *same* frozen Q169–Q179 source, initial amplitudes and first-step receipts, while both preserve all mathematical support conservation requirements. Hence Q173 contact factorization, Q177 ownership and Q179 continuity do **not** uniquely determine a deterministic reset predicate. QED as an explicit model nonidentifiability counterexample.

## THM-534-S55 — Signed automorphism covariance of glued contact receipts [EXACT]

The abstract two-cell complex has automorphism group `S3 × C2` of order 12: arbitrary permutations of the shared-face vertices `(0,1,2)` and exchange of the two apices `(3,4)`. For each such automorphism let `Q2` and `Q3` denote its **signed** permutation actions on the oriented face and cell bases. They obey `Q2 D=D Q3`. If contact gates are permuted with their incidence slots, the masked matrix transforms as `M'=Q2 M Q3ᵀ`, and therefore the nine-dimensional skew generator and its Cayley update intertwine. Each unoriented completed stock-transfer receipt is permuted, and the Q177 equal-share owned-support vector is permuted between the two cells without a spurious sign change. The conditional reset predicate based on completed core-stock gain is consequently covariant **provided that the admitted seed contact is also relabeled**.

**Proof:** oriented simplicial boundary equivariance and signed basis orthogonality give the matrix identities, and the exact midpoint bilinear contains two copies of every induced basis sign. All 12 automorphisms were exhaustively checked with rational matrices on the S52 two-event witness. QED. This does **not** prove that the reset predicate is source-selected or physically invariant under a larger group than the carrier's actual automorphism group.

## Governance and decisions

**AUTO_LOCK (scoped mathematical claims):** S49 gluing partition, S50 finite typed continuity, S51 receipt-only all-contact-dead obstruction, S52 exact conditional witness, S53 ownership ledger, S54 exact finite mask count, S55 signed automorphism covariance. **AUTO_FREEZE:** promotion of the candidate reset to a native UD primitive, claim of globally all-off spontaneous recovery, identification of owned-support reallocation with transport through a disabled face contact, physical mass-energy/spacetime/EM recovery, renewal probabilities or THM-534 historical source restoration.

**OPEN_GATED:** derive a separately admitted event/independent source/latent memory readout that decides Q173 hard face contact, with state and timing; specify face/core reservoir capacity and open-system receipt for Kminus and larger complexes; prove continued gate closure/fracture/reopen cycles under a native rule; independently validate physical observable, units and nonconstructor proof. No change to physical promotion 0.

## Verification

[`verify_face_reset_v1_2.py`](verify_face_reset_v1_2.py) — exact SymPy chain matrices, gluing and source witness. [`verify_face_reset_fraction_v1_2.py`](verify_face_reset_fraction_v1_2.py) — independent-code standard-library Fraction implementation and all 256 gate-mask exact receipts. Both tests and the 12 signed carrier automorphisms executed by same constructor, **not an independent external review**. Source hashes and console receipts in the release manifest. No fitting, external data, or physical claim.