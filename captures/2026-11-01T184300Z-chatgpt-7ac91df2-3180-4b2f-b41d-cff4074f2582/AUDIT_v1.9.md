# Unified Dynamics — Spin-Sensitive Native Receipt and Lift-Null Discrimination Audit v1.9

**Date:** 2026-11-01. **Claim status:** `EXACT_CONDITIONAL` (mathematical results); `NO-GO_SCOPED`; `CANDIDATE` (readout and action); `OPEN` (source-owned birth). **Physical promotion:** **0**. **Registry:** NO ENTRY. 

## Result

The existing frozen UD transport-mismatch **formula** Q140 can distinguish the central Spin(3) sign if and only if its input is typed as a closed-loop **fundamental Spin(3) holonomy** instead of merely the induced SO(3) vector rotation. This is a mathematically useful specialization of an existing structural diagnostic. The admitted sources do **not** show that the packet state retains this lift, that a corresponding detector exists, or that its output can authorize a birth. An unqualified standalone edge trace is not invariant under independent endpoint gauge transformations.

For flat vector holonomy on an inherited triangular face and **fixed inherited Spin transport**, there are exactly four distinct newborn central-Spin lift classes after quotienting by the newborn-vertex gauge. Two independent gauge-invariant binary Wilson-loop signs distinguish them (third sign follows from inherited face parity). The predecessor audit v1.8 established the fourfold lifting; v1.9 gives the exact **minimal information size** and representation-dependent completeness tests.

An exploratory candidate formed by minimizing the **sum** of Q140 fundamental Spin mismatches on new triangles selects exactly one class for an inherited `+I` central face, but selects **three** equally optimal one-defect classes for an inherited `-I` central face. This is a *new minimizing action assumption*, not a frozen UD law; the odd-parity degeneracy is an explicit failed-selection control.

The fundamental Spin trace also has a half-turn blind spot: `diag(i,-i)` and its negative have identical trace and induced vector character. A coherent marked spinor with a supplied reference phase can distinguish them, but the extra preparation/readout is not supplied by the native event sources.

## 1. Object and source typed provenance

- **Geometric carrier:** an already admitted triangular face `012` in a 3D simplicial complex; prospective newborn vertex `w` is not yet part of the native complex. Hypothetical completions have spokes `U_{0w},U_{1w},U_{2w}`.
- **Group:** `Spin(3)≅SU(2)` on candidate links, with a fixed inherited old-vertex Spin frame; `SO(3)` vector projection is a **different representation** of those same group elements. The finite central subgroup `{±I}` is exact mathematical structure.
- **Gauge:** newborn-vertex change multiplies all three spokes by the same right factor. It does not change their relative two elements. A Wilson loop is conjugated by a gauge transformation at its anchored vertex; its trace is invariant. The trace of a single *open* link is not generally invariant.
- **Source binding:** `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (2026-08-22), row **Q140** `δ_U(U)=1−ReTr(U)/d`, mathematical transport mismatch; **G05** master loop-action weight remains OPEN; **Q153–Q158** predictive source/sink open; **Q162** burden current conditional; **Q169–Q173** support evolution on already admitted chain carriers. The Q140 parameter `d` is a *representation dimension*, not a physical spacetime dimension. Row **Q70** uses a distinct pairing representation and is **not** implicitly a fundamental Spin detector.
- **Repository:** `ud-tetra/UD`, main commit `a78193d420f3bac957be081aed0525fbc1457825`, `Docs/UD event admission and interface memory.md` SHA `6719d0f77622eac59c5c88fc163b49adda664e6e`, `Docs/UD native coface growth and cluster selection audit.md` SHA `9ac884d727e65ddd4ed1c277d2ed4a7b91135d73`, `Docs/UD contact receipts and access requirements.md` SHA `a397ae9bdae9ce4269e1bf9d3dc9780ecf74aa80`, `docs/UD_Local_Source_Selection_v0.1.md` SHA `ce5d4417032ce933d8cf06d4ca54b4be7279c011`; all retain separate generated event/source obligations. The local-source test supplies its perturbation and clock, not a native coface scheduler.
- **Predecessor:** v1.8 `UD_NATIVE_BIRTH_RECEIPT_SPIN_READOUT_v1.8/AUDIT_v1.8.md` and draft GitHub PR #500, 1,575 constructor checks; source states native Spin detector and birth authorization OPEN.
- **Designated portal:** `https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/`, 2026-11-01 front page: Papers I–III 1.1.1/IV 0.1, physical promotion 0.
- **Archive caution:** `seam_phase_transport.md`, `packet_modulation_layer.md`, `dirac_like_packet_equation.md` in the supplied reconstruction are placeholder text, **not** source implementations for Spin-sign measurement or birth.

## 2. EXACT—representation-dependent closed-loop trace and interference

For `H∈SU(2)`, let its normalized fundamental trace be `c=Tr_2(H)/2=cos θ`, which is real in SU(2). Then

\[
δ_{\rm Spin}(H)=1-c,\qquad
δ_{\rm vector}(\operatorname{Ad}H)=1-\frac{|\operatorname{Tr}_2(H)|^2-1}{3}
=\frac43(1-c^2).
\]

Hence

\[
\boxed{δ_{\rm vector}=\frac43 δ_{\rm Spin}(2-δ_{\rm Spin}).}
\]

The map is generally **two-to-one** in `δ_Spin∈[0,2]`: `δ_Spin` and `2−δ_Spin` project to the same vector mismatch. In particular at central `H=+I_2` versus `-I_2`, `δ_Spin=0` versus `2` while `δ_vector=0` for both. No physical normalization/energy interpretation is inferred.

For normalized `ψ∈C²`, the supplied coherent equal-reference-path operation gives

\[
P(H,ψ)=\|\tfrac12(I+H)ψ\|^2
=\frac12+\frac14\Re\operatorname{Tr}_2 H
=\boxed{1-\frac12δ_{\rm Spin}(H)}.
\]

The equality follows from `H+H†=Tr_2(H) I`, true for SU(2). It is gauge-invariant under `H↦gHg⁻¹, ψ↦gψ` **when the same coherent reference path and prepared endpoint frames are given**. Thus the equal-phase two-path scalar contains no more conjugacy-class information than the fundamental trace already does. This is *not* a source-owned UD measurement contract.

**Half-turn blind-spot control:** `H_+=diag(i,-i)`, `H_-=-H_+` have `δ_Spin=1`, `δ_vector=4/3` and equal-phase `P=1/2`. With marked spinor `ψ=(1,0)` and separately supplied relative reference phase `η=−π/2`, the amended observable `||[I+e^{iη}H]ψ/2||²` yields `1` and `0`. This requires **additional reference-phase and spinor-polarization information**; an isolated unmarked SU(2) trace does not distinguish these half-turn loops, whose conjugacy classes coincide as standalone loops.

## 3. EXACT—four Spin lifts and exactly two independent bits

For a fixed vector-flat inherited old face, let its **Spin central** holonomy be `p∈{+1,-1}`. Fix old signed edge lifts `a01,a02,a12`, so `p=a01 a02 a12`. New spoke lift signs `s0,s1,s2∈{±1}` yield new face central signs

\[
q_{01}=a_{01}s_0s_1,\quad q_{02}=a_{02}s_0s_2,\quad q_{12}=a_{12}s_1s_2.
\]

The newborn sign gauge `s_i↦−s_i` leaves `q` invariant. There are eight spoke sign choices, two in each gauge orbit, hence **four** physically distinct *mathematical Spin connection* classes with old Spin data fixed. The Bianchi sign law is

\[
\boxed{q_{01}q_{02}q_{12}=p.}
\]

For `p=+1`, admissible `q` patterns are `(+++)`, `(+--)`, `(-+-)`, `(--+)`. For `p=-1`, they are `(++-)`, `(+-+)`, `(-++)`, `(---)`.

**Minimal binary information theorem:** Two selected independent Wilson-loop signs `q01,q02` determine `q12=p q01 q02`. They distinguish four classes; zero or one bit distinguishes at most two classes. Therefore **exactly two binary bits suffice and are information-theoretically necessary**, given an already known old Spin parity `p`. If `p` is *not* known, a third bit (or separately readable old Spin loop) is required to distinguish all eight pattern/parity combinations. The theorem is scoped to **central flat-vector lift controls**, not an arbitrary SU(2) connection or physical communication channel.

A vector-only observer maps all these central signs to `I_3` and cannot see the two-bit distinction. A set of Spin fundamental Wilson-loop traces can resolve the central patterns, provided a packet-native receipt actually records them.

## 4. CANDIDATE—minimizing Q140 loop mismatch still fails on twisted inherited face

Consider the *proposed*, not source-owned, cost

\[
\mathcal C_{\rm trial}(q)=\sum_{f\in\{01w,02w,12w\}}δ_{\rm Spin}(q_f),
\]

which is an **internal dimensionless diagnostic** only. This proposal assumes (a) fundamental Spin loop typing, (b) sum over the three new faces, and (c) minimization. None of (a–c) is specified as a native coface-action rule by Q140.

`δ_Spin(+I)=0`, `δ_Spin(−I)=2` implies exactly:

| Inherited central parity | Candidate cost values | Minimizers | Meaning |
| --- | --- | --- | --- |
| `p=+1` | `{0,4,4,4}` | 1 (all-flat) | only conditional minimum, no birth trigger |
| `p=−1` | `{2,2,2,6}` | 3 (one twist on any new face) | irreducible parity-frustration degeneracy |

The odd-parity source retains one central sign defect even if minimizing this cost. It cannot choose **which** new face carries it without an additional asymmetry, nonlocal context, or new rule.

This is a concrete counterexample to treating an exact readout and a parameter-free algebraic sum as a complete source-derived birth selector.

## 5. NO-GO—causal birth interface and gauge ownership

The old packet state, old face links, old burden, original graph label and any *old-state-only* causal receipts can be held fixed while all four prospective new-lift classes remain admissible as mathematical extensions. Let `π` forget the three new spokes from a prepared extension. The fiber of `π` above that fixed old-state central flat-vector setup has cardinality four. No function of `π` alone can reconstruct an arbitrary unknown element of that fiber. A deterministic choice of one **is possible only after adding a selection rule**; nonuniqueness is not an impossibility theorem for new dynamics.

Existing event-admission sources provide conditional local first admissibility, inherited face identities, and conditional receipt recording. They do not establish pre-birth **Spin lift acquisition**, signed gauge-frame retention, a source-owned Q140 closed-loop detector/receipt, a tie/competition arbiter, a positive formation debit, donor, or event clock. Observing a **post-birth** loop cannot be retroactively reused as a predictive pre-birth cause unless the candidate links and readout are already registered by an independently admitted source mechanism.

A spin-sensitive signal could be used in an *explicitly new* conditional event contract, but any resulting dynamical claim must identify its carrier and prepared reference, coupling to the event generator, source/clock, and a falsifying null comparison. Event count is not physical time; quadratic support is not physical energy.

## 6. Reproducibility and governance

Run `python3 verify_spin_trace_v1_9.py` (SymPy), and `python3 independent_binary_lifts_v1_9.py` (standard library only). The tests share no implementation imports. Both are same-constructor independent-method checks, not independent peer review. JSON results and terminal run receipts are included.

**AUTO_LOCK scoped mathematical statements (subject to independent review):** SU2-to-SO3 character relation and two-to-one mismatch; 2-bit minimum for central lift; old-parity Bianchi rule and four classes; central Q140 sensitivity; zero-trace half-turn ambiguity; candidate cost minimizer multiplicities; gauge-invariance of paired trace and spinor-prepared interference.

**AUTO_FREEZE unsupported promotions:** 'the existing Q140 register is a native Spin detector', 'the Spin signal selects an actual birth', 'a two-bit channel has been measured', 'Q140 is a physical energy/action', 'the mathematical reference phase is source-generated', 'the twist represents a hidden spacetime dimension', or 'resource/clock/debit follow from Spin holonomy'.

**OPEN_GATED:** native Spin-group/link source and lift choice, gauge-invariant closed Wilson receipt, coherent reference initialization, source-selected event/facet, full newborn packet and cost, resource donor, clock/readout and independently falsifiable physical correspondence.

**NEXT:** Search for a versioned native Spin-sign acquisition or spinor interference operator whose event coupling is explicitly source-derived; otherwise stop the birth-selection branch at this exact source obstruction. External nonconstructor review remains required.
