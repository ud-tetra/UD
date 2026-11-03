# Finite-window joint carrier with clock, memory, records and reset supply

Development construction v0.1 · 14 October 2026 · public reading edition0.7

**RESULT.** A supplied finite state map can be reproduced for a declared finite window by one reversible joint permutation. Old states remain in memory, receipts remain in record cells, and each reset exchanges the whole payload with one fresh donor. A master clock accounts for episode selection and every reset address. It is not reset by a payload exchange. The construction establishes a conditional finite carrier, not a native Hodge realization or a permanent absorbing factor.

Status: CANDIDATE JOINT OPERATOR / EXACT CONDITIONAL WINDOW THEOREM. No registry entry. Independent human review pending. Physical promotion: **0**. All code and AI reviews below are constructor-team checks. No novelty priority or laboratory validation is claimed.

## 1. Declared finite map and complete input

Supply a nonempty finite set S, a total map F:S→S, an encoding e:S→Z_d with d=|S|, and a reset preparation s*. Choose e(s*)=0 and write f=eFe^-1. Every modular label has a declared successor; no invalid-state holes are permitted. Supply a total receipt map rho:Z_d→Z_m, m≥1. Choose N≥1 compute ticks per episode and B≥0 fresh reset blocks. There are B+1 episodes.

S must encode the complete target state, including its integrity flags, latent cache, response, active stock, source queue, cursor and frozen response branch. The master clock below is additional joint state. A receipt may deterministically describe both pre-state and F(pre-state); it must not hide unspecified source or observer input. If such input is needed, enlarge S or declare a different map.

The executable RSP example compiles the forward-invariant closure of one supplied prepared trajectory, through its complete fixed state. This is narrower than the entire family of RSP preparations. Its label table and full receipt dictionary are retained. Encoding is an authored choice, not a recovered native latent source. The algebra below also applies to any separately declared finite invariant family and any total f, including noninjective f.

## 2. Joint carrier and prepared bank

Let P=W⊗H_0⊗…⊗H_(N−1)⊗R_0⊗…⊗R_(N−1). Work and each history cell have d basis labels; each record cell has m labels. History label0 is an additive blank coding value, not an empty physical Hilbert space. Let

    D = dim P = d^(N+1) m^N,
    L = (B+1)(N+1),
    J = C ⊗ P ⊗ D_0 ⊗ … ⊗ D_(B−1),
    dim C = L,     dim D_j = D,     dim J = L D^(B+1).

The names D_j denote donor payload carriers, distinct from the scalar D. All registers are retained. An arbitrary spectator Y can be included; it is not silently traced out. Define the complete reset payload

    p* = |0>_W |0>_H^⊗N |0>_R^⊗N.

The ideal supplied preparation is clock |0>, active p*, and B independent donors in p*. Each untouched donor's whole-state independence and freshness are hypotheses. Counting only its W label or checking its marginals does not certify the bank. Approximate supply is charged once on the full joint domain (§8).

## 3. Exact reversible compute gate

At compute address i, act only on W,H_i,R_i:

    G_i(w,h,r) = (h + f(w) mod d, w, r + rho(w) mod m).

This can be performed by reversible receipt addition, reversible successor addition into H_i, and SWAP(W,H_i). Other cells remain unchanged. Its explicit inverse is

    w_old = h_new,
    h_old = w_new − f(h_new) mod d,
    r_old = r_new − rho(h_new) mod m.

Therefore G_i is a permutation on the **entire** label domain, including dirty memories and records. Linearly extended to the Hilbert space it is unitary; the inverse remains valid with arbitrary entangled spectators. Neither injectivity of f nor a stochastic assumption is needed.

For a fresh tap h=r=0, the output is (f(w),w,rho(w)). The old state is retained rather than erased. For dirty h, the work output is h+f(w), so the projected F law is not guaranteed. Receipt addition on a dirty cell can wrap to its blank label. Modularity is reversible label arithmetic, not a resource-refilling rule.

Computing a basis-label receipt coherently can entangle registers. It does not clone an arbitrary unknown quantum state, create a measurement outcome, or derive a Born distribution. RSP stock remains an integer coding coordinate with no established energy or chain-support identification.

## 4. Master clock and one fixed joint step

Write every clock address uniquely as c=j(N+1)+i, with 0≤j≤B and 0≤i≤N. Define the payload/bank permutation V_c:

| Address | V_c | Accounting |
|---|---|---|
| i<N | G_i on active payload | Consume the next fresh history/receipt tap |
| i=N, j<B | SWAP(P,D_j) | Fresh payload enters; whole old payload becomes outgoing donor j |
| i=N, j=B | Identity | Final address; no donor remains in the declared supply |

Define one fixed joint operator

    U = (clock shift c→c+1 mod L) [sum_c |c><c| ⊗ V_c].

Every block V_c is a permutation; the controlled direct sum and clock shift are permutations. The inverse first decrements the clock, then applies V_c^-1 at that recovered address. This proves global reversibility on every dirty configuration, not just the prepared subspace.

The episode label j, compute address i, donor selection and reset timing are all encoded in C and the supplied operator. No uncounted external reset trigger is needed for this discrete construction. The design nevertheless supplies that schedule; it does not derive a native event-trigger, gate coupling or refusal mechanism from Hodge flow. The raw U has an identity final payload block followed by clock wrap, **not** an irreversible END_OF_SUPPLY latch. Paper IV's supplied refusal policy uses no modular supply wrap and is a different contract.

## 5. Finite-window theorem and outgoing records

**Theorem JC.1.** From the ideal preparation, during the first K=L−1=(B+1)N+B transitions, each of the B+1 episodes implements exactly N target ticks. At compute prefix k (0≤k≤N) its active work is f^k(0), its used history cells are (0,f(0),…,f^(k−1)(0)), and its used records are (rho(0),rho(f(0)),…,rho(f^(k−1)(0))). Unused taps remain0. Each completed reset transfers that entire episode payload into D_j and starts the next payload at p*. Completed outgoing blocks are not contacted again inside the declared window.

*Proof.* At an episode start P=p*. Assuming the prefix identity, the next tapped history and record cells are0. The fresh-tap identity in §3 extends the prefix by one state and one receipt. After N computes the scheduled SWAP sends the whole completed payload to donor j and brings in its untouched p*, establishing the next episode start. The schedule never revisits a consumed donor during K transitions. There are (B+1)N computes and B swaps; the final clock address is L−1. Induction proves every statement. □

Outgoing record cells are not an additional duplicate output bank: they are the record factors of the consumed matched donor blocks after SWAP. Each also retains the old work and history. The active final episode retains its N records, so there are BN exported records and N active records. A supplied computational-basis readout can inspect these labels; physical detection and retention perturbations are separate gates.

For arbitrary old correlated payload rho_PY and a fresh independent donor sigma_D=p*,

    SWAP_PD (rho_PY ⊗ sigma_D) SWAP_PD = sigma_P ⊗ rho_DY.

This is Paper IV IV.12's correlation-export identity on the declared matched payload dimensions. Nothing is discarded, postselected or thermally erased. Old P/Y correlations move to D/Y. A classical product preparation suffices for the exact displayed trace, but the underlying unitary acts coherently on any admitted input.

## 6. Explicit resource ledger

| Resource | Allocated capacity / usage | Final disposition |
|---|---|---|
| Master clock | L addresses; prepared c=0; K certified advances | c=L−1; no fresh clock supplied by a payload SWAP |
| Work | B+1 d-level factors across active+donors | B old final work values outgoing, one active |
| Old-state memory | (B+1)N d-level cells | BN outgoing, N active; none erased |
| Receipt memory | (B+1)N m-level cells | BN outgoing, N active; includes fixed-work ticks |
| Payload resets | B independent prepared D-dimensional donors | B SWAPs; no untouched reset block remains |
| Schedule/operator | One supplied U with all controlled blocks and shift | Native synthesis, locality and preparation remain open |
| Retained spectator | Y unchanged by identity extension | All correlations still in complete joint receipt |

Separate binary register encoding allocates

    ceil(log2 L) + (B+1)[(N+1)ceil(log2 d)+N ceil(log2 m)] bits.

These are **allocated capacity**, not entropy, heat, actual qubit count on a certified device, or an optimal memory theorem. A fixed known trajectory can be compressed; reversible recomputation/uncomputation could alter the tradeoff. No N log d minimal-garbage claim is made. For a universal single tick with fresh common auxiliaries, a noninjective f requires an outgoing auxiliary with dimension at least max_y |f^-1(y)|: orthogonal inputs with the same output work must remain orthogonal somewhere in the joint output. That narrow collision bound does not fix the cost of acquiring blank resources.

Example: d=3,m=4,N=4,B=1 gives L=10, D=62,208, dim J=38,698,352,640 and separate binary capacity40 bits. The declared window has9 transitions:4 compute,1 reset/export,4 compute. It uses8 history and8 receipt cells, exports4 receipts and leaves4 active. The large dimension is a register allocation, not a new spatial dimension or native tetrahedral carrier size.

For RSP resource coordinates, additionally count stock on each **work factor**: active stock plus each untouched donor's prepared stock plus each outgoing donor's remaining stock. Inside the window an inspection reduces this total by its exact consumed_tokens; a renewal internal to RSP preserves it; a payload SWAP merely moves the work factors and preserves the total. History and receipt factors hold nonspendable descriptions and are excluded from this inventory. Runnable stock excludes already outgoing blocks. The displayed B=1 one-token example supplies2 encoded tokens, consumes1 in each episode, and finishes with0 active,0 unspent and0 outgoing remaining. These are logical RSP tokens, not additional physical fuel or energy. Short windows and latching preparations can export unused stock; it remains recorded rather than declared consumed.

## 7. Wrap, clock reset and complete re-preparation

The K+1=L transition has identity payload action and wraps C to0. It does not uncompute history, clear receipts, replenish donors, restore stock or refresh correlations. Applying U further remains mathematically valid, but JC.1 no longer applies. There is no universal guarantee of either immediate failure or indefinite successful reuse. Trivial maps/preparations can recur harmlessly.

The supplied one-token C/H example has labels0→1→2→2, with rho=(1,2,3). At N=4 its final payload is W=2,H=(0,1,2,2),R=(1,2,3,3). After wrap the first dirty compute still gives W=2; the second gives 1+f(2)=0 mod3 instead of the desired fixed W=2. The witness records this failure. The continuing work is no longer an exact absorbing factor; it is an open-window projection of a closed reversible carrier.

A payload reset at an episode boundary resets its **relative** compute address only by moving the master clock to a new episode address. It does not reset C or renew the bank. Restoring only C to0 would expose used resources and is not complete re-preparation.

For complete restart of this same finite programme, a sufficient algebraic resource is one independent fresh matched donor J' of dimension dim J, prepared with clock0, active p* and B fresh payload donors. A supplied full SWAP(J,J') exports the entire old clock, memory, records, consumed bank and correlations, leaving J prepared again. This requires another fresh **complete-joint** resource and a supplied exchange operation; it is not implemented by the existing schedule or claimed autonomous. Repeating that larger reset merely moves the supply boundary. Alternatively U^-1 can undo the past, consuming reverse execution and retracting the recorded computation; it does not retain independent outgoing records while returning every resource to its initial state.

## 8. Error, energy, time and source debts

The displayed ideal label construction has zero algebraic implementation error. This is not a claim of zero experimental error. If actual complete supply differs from the ideal independent bank by at most epsilon_bank in trace distance, and every actual tick differs from its declared ideal joint channel by at most epsilon_t uniformly with arbitrary spectator extension, then after k≤K operations

    D_tr(actual_k,ideal_k) ≤ min(1, epsilon_bank + sum_(t=1)^k epsilon_t).

This is the telescoping full-domain comparison of Paper IV IV.13. Use matching retained domains and count shared errors once. Equal clock or output marginals do not establish whole-bank admission. Failure histories remain; no success postselection discount is used. No numeric error budget is certified without supplied bounds.

C is an ordinal clock. No SI tick duration, hbar bridge, physical fuel or laboratory Hamiltonian is established. A finite unitary admits a Hermitian matrix logarithm and can be assigned an engineered sampled Hamiltonian; this general fact does not identify a sparse Hodge generator, a local architecture, intermediate-time exact work updates or free clock acquisition. Paper IV IV.4 separately implements a supplied finite word with a prepared history Hamiltonian and its own return, norm, time and mismatch ledger. It must not be identified with this cyclic discrete clock without a new comparison.

The current carrier specifies no nonzero bare-energy operators, temperature or reservoir. A mathematical zero bare-energy convention makes matching trivial but supplies no physical reset-energy value. Physical energy-preserving SWAP requires matched bare operators under the register identification, stronger than equal dimensions. Arbitrary compute gates need not preserve a proposed physical bare energy. Switching, native/operator mismatch, clock coherence, transport, record retention and fresh-state acquisition remain explicit implementation debts. No joule cost, Landauer heat minimum or action normalization follows from the allocated cell count.

This answers the finite-window extension left open by the previous reversible-factor obstruction at the level of a **supplied larger joint carrier**. The decoder is guaranteed only on the prepared finite window and includes a joint history/clock outside the target S. It therefore does not contradict the total two-sided finite-image no-go. Native Hodge→joint-carrier coupling and source-selected prediction remain OPEN. The full research proof DAG, empirical score and independent human review remain open.

## 9. Reproduction, provenance and disposition

New authored files: joint_carrier.py; verify_joint_carrier.py; this proof; exact C/H witness and root verification. Separate parallel AI checker and source/scope review are preserved with their hashes. Tests exhaust small **dirty joint domains** as well as prepared windows, retain noninjective and correlated-input witnesses, and include dirty-memory, dirty-record, reused-donor and post-wrap negative controls. General size claims follow the explicit inverse and induction proofs rather than enumeration.

Run from the release root: `python joint_carrier.py`, `python verify_joint_carrier.py`, `python verify_dependencies_v07.py`. The parallel replay instructions are in the release README. Only newly authored standard-library code is executed; primary archived source code is not executed for ingestion.

Primary basis: Paper IV development draft0.1 §§2,4,8,9 (IV.4,IV.12,IV.13); RSP-1 finite pre-event source programme0.1 and its unchanged complete-state code; Hodge-to-RSP realization obstruction0.1 §§1–7. Original source branches C0593, HD readout C0926 and integrity C0635 retain their separate types. No source theorem is silently promoted to a native apparatus claim.

Disposition: finite-window mathematical joint carrier CONSTRUCTED CONDITIONALLY; clock/memory/record/donor accounting EXPLICIT; native operator/source acquisition OPEN; physical energy/time/detection OPEN; autonomous full-resource restart OPEN; independent human review PENDING; physical promotion0.
