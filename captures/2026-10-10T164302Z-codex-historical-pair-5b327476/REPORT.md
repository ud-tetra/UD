# UD historical directed-pair source recovery and edge-map limit v0.1

**10 October 2026 UTC · development addendum and scope amendment · physical promotion 0.**

## Source and type correction

The historical `UD_JOP_WORKING_MANUSCRIPT_THROUGH_SECTION11_v1.2_JOINT_REPLAY_GOVERNED.md` (30 August 2026; Library `libfile_8b9461fba6248191bb6d58dcf977a977`) contains a **conditional pair-event selector** that the [source-readiness capture](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T163105Z-codex-source-readiness-3c72f65b) did not enumerate. Its §6.1 *defines* a context-specific closure lift \(C_{{\rm cl},e}^{\rm hard}=1-\theta_{p(e)}\) for the opposite-edge pair \(p(e)\), and §6.2 defines a separate isometric edge transport test \(T_{{\rm int},e}^{\rm hard}=\mathbf1[I-U_e^\dagger U_e=0]\) for the declared contractive sector. The broader `UD_EDGE_CLOSURE_AND_TRANSPORT_INTEGRITY_HARD_GATE_DERIVATION_v0.1.md` (21 August 2026, §§II–IV; Library `libfile_e9d5b0d7a4bc81918822ae403d527626`) instead makes the closure requirement set context-dependent and the transport integrity predicate depend on the declared domain, overlap, and inverse conditions. These formulas cannot be silently identified across contexts.

**Amendment to earlier wording:** the [pair-to-edge capture v0.1](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T161720Z-codex-pair-edge-22aece15) correctly proves that *pair-only* equivariant state cannot realize all six-edge masks, but its statement that a pair-to-edge copy is unsourced needs qualification: §6.1 of this **historical manuscript** supplies the closure-factor copy in its declared context. It does not supply the edge transport-factor update, a universal identification of pair \(q\) with edge \(C\), or a current admitted six-edge switch law. The original capture remains preserved; this is an append-only versioned scope repair.

## Recovered conditional selector

The §7 *Theta Source-Balance Amendment v0.3* defines a separate Hamming budget \(\mu_\Theta\) and a burden objective over admissible pair states. Its *Directed Parity Source-Law Amendment v0.4* defines, on the **ungated** real skew edge-sector flow, the signed pair source

\[
\lambda_p^{S\pm}(s)=2c_1(s)^TP_p^{(1)}(B_1^Tc_0(s)-B_2c_2(s))
=\frac{d}{ds}\|P_p^{(1)}c_1(s)\|^2,
\quad G_{p,n}=\int_{s_{\tau_\Theta}}^{s_n}\lambda_p^{S\pm}(s)\,ds.
\]

With **additional** minimal-capacity alignment and one-pair locality assumptions it proposes \(\mu_{\Theta,n}=-\operatorname{sgn}\sum_pG_{p,n}\). For negative total it selects one currently open, integrity-passing pair with \(G_p<0\) maximizing \((-G_p,-W_p^{B2})\) and closes it. For positive total it selects one closed, integrity-passing pair with \(G_p>0\) maximizing \((G_p,W_p^{B2})\) and reopens it. At zero total it selects a unique admissible close/reopen swap maximizing \((W_q-W_p,G_q-G_p)\), subject to \(W_q>W_p\). Absent candidates or exact ties hold. Its event index is the first post-previous-event index at which the conditional selector emits a change. `UD_OP03_DIRECTED_PARITY_SOURCE_FRONTIER_UPDATE_v0.6.md` (Library `libfile_9f164176bcf8819197a96fdc1ecf31c7`) explicitly retains minimal-capacity alignment as a validation gate.

The historical §7 v0.5 relative-frame amendment and `UD_PREEVENT_RELATIVE_FRAME_SOURCE_LAW_v0.1.md` (Library `libfile_f5cc9aef39fc819180ce90b67b7ec4b5`) conditionally recover an \(S_4\) frame from **oriented six-dimensional \(C_1\) transport** after a co-moving null quotient. That is not the local edge map \(U_e\) tested by the §6.2 integrity gate. A frame certificate cannot be substituted for a local \(T_{{\rm int},e}\) update.

## Exact finite test and limits

Run `python3 verify.py`. The standard-library replay enumerates all \(8\) pair states, \(8\) pair-integrity masks, \(27\) signed source triples with entries \(-1,0,1\), and \(27\) nonnegative burden triples with entries \(0,1,2\): **46,656 synthetic receipt inputs**. All **279,936** \(S_3\) relabeling comparisons pass. The six branch counts in `results.json` sum exactly to 46,656; they are enumeration counts, not event probabilities. Every emitted swap increases the declared burden objective by the exact positive \((W_q-W_p)/4\). The direct controls include negative-source closure, positive-source hold when no closed pair exists, strict zero-source swap, tie hold, and integrity veto.

**CANDIDATE, not primitive closure:** The finite test verifies a selector *given* \((\theta,T^{\rm pair},G^{S\pm},W^{B2})\). It does not show that all synthetic inputs are dynamically reachable, that \(\mu_\Theta=-\operatorname{sgn}G_\Sigma\) follows from conservation, or that the required history window and pair-integrity receipts are generated before target exposure. No held-out event was scored. A nonzero signed source can still yield HOLD when no admissible address exists; the first-admissible convention then emits no event at that index. Event index has no calibrated physical time unit.

**OPEN_GATED local edge map:** Even within the historical §6.1 closure lift, the selector does not update \(U_e\) or the edge-resolved transport predicate \(T_{{\rm int},e}\). The six-edge mask \(h_e=C_eT_e\) remains conditional on those inputs. The current site's [Paper I F05](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/#/manuscript?section=F05) and [Idle-Response Lineage Boundary v0.1](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/#/doc/idleResponseLineage) leave the pre-event constitutive source and intact-sink response open; the historical pair selector is a separate candidate branch, not a resolution of that pair response without a typed intertwiner and source admission.

## Disposition

- **EXACT, conditional algebra:** the implemented v0.4 selector is deterministic and pair-relabeling covariant on its declared synthetic receipt domain; strict swaps improve its objective.
- **CANDIDATE:** signed-support-to-Hamming-budget law and first-admissible timing under supplied pre-event receipts; no held-out validation.
- **OPEN:** primitive event source, local edge transport update, context reconciliation, pair-to-edge response bridge, physical clock.
- **Governance:** constructor check only, non-constructor review pending, development lane under the supplied CRL-2 subdivision v1.0; physical promotion 0. Neither the original no-go nor the old source is overwritten.
