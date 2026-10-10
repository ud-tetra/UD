# UD mask-source readiness and decisive-event contract v0.1

**10 October 2026 UTC · development protocol · no source law promoted · physical promotion 0.**

## Result and source inventory

**EXACT conditional:** The edge mask is \(h_e=C_eT_e\) for binary hard closure and transport-integrity predicates. The factor histories determine a supplied mask history and Boolean cause tags. They do not determine the next factor state from primitive packet data. This distinction is explicit in `UD_HARD_GATE_UPDATE_LAW_SOURCE_DERIVATION_v0.1.md` (23 August 2026, §§1–4; Library `libfile_a80bf50559c88191a8b3b411cb38d93c`) and `UD_HARD_GATE_BOOLEAN_FACTOR_UPDATE_THEOREM_v0.1.md` (23 August 2026, Gate closure/opening and What is not derived; `libfile_10b3069a88a48191bd7190f02f91807b`). `HARD_GATE_TRANSITION_TRIGGER_AND_SOFT_MARGIN_SOURCE_AUDIT_v0.1.md` (28 August 2026, §§1–5, 8–9; `libfile_92f3e465e4008191a62746ef92d52a4c`) explicitly finds the trigger, rate, and soft margins unidentified. The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q156/Q167/Q173) confirms the edge product and conditional currents, and lists gate-transition receipts as a dependency.

**EXACT scoped pair result:** The live site's [Idle-Response Lineage and Gate-History Boundary v0.1](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/#/doc/idleResponseLineage), `theorem/UD_CLOSE_VS_HOLD_GATE_HISTORY_NONIDENTIFIABILITY_THEOREM_v0.1.md` and `governance/UD_MINIMUM_IDLE_GATE_SOURCE_CONTRACT_v0.2.json`, admits both pair responses \(q_+=0\) and \(q_+=1\) on a source-authenticated intact terminal sink \((T_-,L_-,q_-)=(1,1,1)\to(T_+,L_+)=(1,0)\). Its existing `prereg/UD_INTACT_SINK_CLOSE_VS_HOLD_PREREG_v0.1.json` already freezes this discriminator. ZIP source contract SHA-256 `49c183d8a145e272e82a471b274861abbc4f3c8c00df4968ea44ec0b21b0e485`; prereg SHA-256 `6c521041d369b66bb7e6cba8dbcb8d84dba3b0c1ac2bfa42c0e64282d90954e2`.

**Typed firewall:** Pair response \(q_p\) and edge factors \((C_e,T_e)\) have different carriers and semantics. No sourced map identifies them. Their two missing decision laws are tested separately until a source-authenticated pair-to-edge intertwiner exists. The previously merged [edge receipt carrier v0.1](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T162352Z-codex-edge-receipt-9061c3ae) is a complete mask encoding, not an update law.

## Pre-event candidate interface (OPEN_GATED)

A proposed deterministic edge constructor must freeze \(\mathcal X_{\rm pre}\), the primitive packet state and typed closure/transport state, \(\mathcal E_{\rm pre}\), the event descriptor known before its endpoint, and an edge set \(E\). It must provide a source-derived function

\[
F_E:\mathcal X_{\rm pre}\times\mathcal E_{\rm pre}\longrightarrow\{0,1\}^{E}\times\{0,1\}^{E},
\quad (x_n,e_n)\mapsto(C_{n+1},T_{n+1}),
\qquad h_{e,n+1}=C_{e,n+1}T_{e,n+1}.
\]

An equivalent lower-level constructor may output post-event closure receipts \(r'_{\alpha}\) and transport maps \(U'_e\), followed by *previously declared* requirement sets, domain/overlap/reverse-map tests, and the sourced hard predicates. It must specify full domain, boundary/null behavior, simultaneous-event ordering, \(S_4\) relabeling covariance, and what counts as one event. No post-event receipt, observed factor, or target mask may enter \(F_E\). Event index is not physical time.

For the pair carrier a separate candidate \(G:\mathcal P_{\rm pre}\times\mathcal R_{\rm sink}\to\{0,1\}\) must predict \(q_{p,n+1}\) on the intact-sink stratum before its gate endpoint is revealed. It must use an independently specified gate response functional or source-authenticated idle-gate receipt; the terminal-sink label alone is insufficient. If \(\mathcal R_{\rm sink}\) is known only after the event, this tests **conditional response**, not pre-event timing. A pre-event prediction of *when* a switch occurs also requires a source law that predicts the sink and factor transitions from pre-event variables. Controls remain \(T_+=0\Rightarrow q_+=0\) and \(T_+L_+=1\Rightarrow q_+=1\).

## Frozen decision and adversarial fixtures

`PROTOCOL.json` fixes inputs, outputs, exclusions, and acceptance rules. `verify.py` checks two exact ambiguous fibers. Edge: the same reduced pre-state \((C,T)=(1,1)\) with an unresolved primitive-event token admits both \((C',T')=(1,1)\) and \((0,1)\), hence next masks 1 and 0. Pair: the same intact-sink pre-record admits both close and hold. Any deterministic predictor of either target from *those reduced inputs alone* fails on at least one completion. This is a conditional information-sufficiency obstruction; a richer sourced pre-event variable can split the fiber and creates a new test branch.

No source-complete \(F_E\) or \(G\) was found in the inspected versions. **SOURCE_BLOCKED** is the actual readiness verdict; the fixtures are synthetic adversarial controls, not a held-out run. A future candidate must be frozen with source paths, exact versions/hashes, code, normalization, and interpretation before target exposure. On source-authenticated held-out events within its declared domain, one mismatch rejects a universal deterministic rule. A test without an edge switch and an intact sink with a gate readout is INCONCLUSIVE for the respective branch; baseline persistence/close/hold results must be reported. Once endpoints are exposed, amended analysis is exploratory until fresh independent data are used.

## Governance

The supplied `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md` (SHA-256 `8e9e8159fe2e5c4bdc234712e02db0151fc77f4a92c140372279a1e9717689a4`, §§1–2) labels a constructor-only proposal CRL-2a, with non-constructor review needed before 2b. This packet freezes a proposed test contract; it does not claim CRL-2b, an executed blind result, a physical correspondence, or a new mask law. Physical promotion stays 0.
