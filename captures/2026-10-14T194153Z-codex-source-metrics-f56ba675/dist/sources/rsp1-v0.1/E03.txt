# UD packet-to-switch source recovery v0.2

**12 October 2026 UTC · development — no registry entry · physical promotion 0.** The newly available `packet_modulation_layer.md` is a three-line reconstructed-repository placeholder, so it supplies no packet modulation equation, move grammar, proposal law, feedback, or K4 readout. This note supersedes only the prior *availability* statement in the packet-action audit v0.1; that audit's conditional exact calculations stand. A source-complete UD switch law was **not** obtained.

## Typed source audit

| Source and exact location | What it supplies | What it does not supply |
|---|---|---|
| Attached `project_sources/02-packet_modulation_layer.md`, SHA-256 `a3275849a09d9c29cb3f8a369fc7ca113ba3cd7529e7db443529097ccaf088ec`, all three lines | Filename and placeholder notice only | Modulation dynamics or a predictive gate |
| Historical March 2026 `distinction_dynamics_manuscript.pdf`, SHA-256 `909ac4bfbb07ab815d15463648278877a7452989797589bf630564a0afa9f1ef`, §§2, 4, 13 | Packet variables `(rho_i,theta_i,chi_i)`, transport `U_ij`, displayed action, illustrative Metropolis acceptance | Normalized move proposal/eligibility, graph renewal, physical clock, bridge from local `chi_i` to K4 pair `Theta` |
| [Paper I v1.1.1 §7.4–7.5](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) | Exact affine `Theta` map **given** frame/offset receipts | Pre-event source of frame, offset, mask, admission, timing; idle mask can alias intact null |
| Supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q153, Q158, Q161–Q168, Q173, Q178–Q179 | Continuity identities, residual receipt, **conditional** normalized burden-mixing flow, hard masks and support currents | Constitutive source/sink, gate-transition, renewal, and K4 receipt-source laws; normalized attempt parameter is not physical time |
| Supplied `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`, SHA-256 `8e9e8159fe2e5c4bdc234712e02db0151fc77f4a92c140372279a1e9717689a4`, §§1–4 | Governance **proposal** for development versus registry and independent review | Scientific event source; it is not an accepted source receipt |

The historical packet coordinate `chi_i`, Paper I §8.2's prepared polarity `chi`, and K4's three-bit pair `Theta` have distinct definitions. The matching Greek letter creates no map among them. In particular, Q162–Q163's burden current/decay on a dimensionless attempt convention does not define a proposal distribution for binary switches. Q158's `s_B=Delta rho-B j_B` is a residual after a change, not a predictive constitutive source.

## EXACT conditional mathematical criterion: visible Markov closure

**Object.** Let `Z` be a finite *complete* source state space, including any packet, graph, frame, source/sink, hidden history, previous completed-switch index, and renewal variables needed for the update. Let `K: Z x Z -> [0,1]` be a row-stochastic one-attempt transition kernel. Let `h: Z -> O` be a fixed, pre-event typed visible readout, for example `O=(oriented frame, three K4 pair bits, required switch-index memory)`. Its carrier map must be independently specified; it is not constructed by reading endpoints. For an output frame `r`, event receipt compares `Theta+` to the source bits transported to the output basis, `P_{pi(r)} Theta-`, using XOR. A frame-only transition and a bit switch remain separate tags.

**Claim.** A time-homogeneous Markov kernel `\bar K` on visible `O` gives the law of `h(Z_n)` for **every** initial complete state if and only if, for all `z,z'` with `h(z)=h(z')` and every visible `o'`, the row sums agree:

\[
\sum_{y:h(y)=o'}K(z,y)=\sum_{y:h(y)=o'}K(z',y).\tag{L}
\]

**Proof.** Necessity: start once from `z` and once from `z'`; both have the same visible initial value, so their one-step visible distributions must be equal. Sufficiency: define `\bar K(o,o')` to be the common row sum in (L). Conditional on any visible history, the complete current state is a mixture over the fiber `h^{-1}(o)`. Every point in that fiber has the same next visible distribution, so the mixture has distribution `\bar K(o,·)` independently of earlier visible history. This proves the Markov property for all initial laws. This elementary strong-lumpability criterion does not assert that UD supplies `K`, `h`, or (L). Special prepared ensembles may have weaker closure; that would be a separately stated preparation-dependent claim.

**Switch and strict-null calculus, if a source kernel exists.** Let `xi(z,y)` be the declared frame-aligned binary event receipt and let `N(z,y)=K(z,y) 1[xi(z,y)=000]` be the sub-stochastic null kernel. For initial complete state `z`,

\[
P_z(\text{switch next attempt})=\sum_y K(z,y)1[\xi(z,y)\ne000],\qquad
P_z(\text{no switch for }m\text{ attempts})=e_z^T N^m\mathbf1.\tag{N}
\]

The second identity multiplies kernels along all null paths and therefore includes feedback and renewal of hidden state. It reduces to `(1-r)^m` only under additional constant-hazard assumptions. If a normalized proposal `q(a|z)` and accepted update `T_a(z)` are supplied, and rejected moves stay in the same state, then the one-attempt switch chance is `sum_a q(a|z) Acc(z,a) 1[xi(z,T_a(z)) != 000]`. Metropolis acceptance alone supplies `Acc`, not `q`, `T_a`, or `xi`. An attempt count is not a calibrated physical time; a holding-time/clock map with units is a separate bridge.

## Exact constructed witnesses; not UD dynamics

The attached `verify.py` evaluates a four-state `Z={(h,theta): h,theta in {0,1}}` with hidden-state-specific switch proposals `r_0=1/4`, `r_1=1/2`. Holding `h` fixed, the two full states `(0,0)` and `(1,0)` have the **same visible bit** `theta=0` but next-bit distributions `(3/4,1/4)` and `(1/2,1/2)`. Hence (L) fails and no universal `theta`-only Markov law exists for this constructed kernel. Adding the hidden `h` makes the full law well defined. This is a counterexample to automatic projection, not a finding that UD itself is non-lumpable.

A second constructed kernel toggles `h` on every attempt while keeping the **same first-attempt** visible distribution from `(0,0)`. Equation (N) gives three-attempt strict-null probabilities `27/64` with fixed `h` and `9/32` with renewing `h`. Thus matching one-step switch chances do not determine null-window histories. The script checks row sums, probabilities, one-step equality, projection failure, and the exact rational null results. No endpoint target was opened or scored.

## Source-complete return and disposition

An actual UD source submission needs a versioned `Z` and initial/boundary preparation; admissible moves and a normalized generator/kernel with tie and simultaneous-contact semantics; predictive packet/support/burden sources and sinks; update and renewal maps; a fixed carrier/frame-aligned `h` and `xi`; the event/attempt observation schedule; and, for physical claims, a calibrated time/measurement bridge. Apply (L) to any proposed **compact** visible record. If it fails, retain the needed hidden state rather than fitting a visible rate. Then freeze its rule before independent full-endpoint and null-window exposure under OP03.

**Disposition:** EXACT conditional criterion (L) and identities (N); EXACT finite constructed witnesses; NO-GO recovery of a *source-complete UD* rule from these available files; OPEN source dynamics, K4 bridge, event clock and independent endpoint test. The [prior packet-action audit v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-12T141129Z-codex-packet-source-755aaa68/SOURCE_AUDIT.md) remains valid under its explicit conditional move grammar. `Gap2_FINAL_Finite_Genesis.png` was unavailable and was not used. No source rule is AUTO_LOCKed; physical promotion 0.
