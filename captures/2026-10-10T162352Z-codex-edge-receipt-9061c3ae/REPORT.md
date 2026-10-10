# UD six-edge receipt carrier and intact-sink decision boundary v0.1

**10 October 2026 UTC · development lane · constructor-checked · physical promotion 0.**

## Source, scope, and typed question

The live site's [Paper I, §7.4–7.5 and F05](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/#/manuscript?section=F05) leaves the pre-event receipt source open. Its [Idle-Mask and Retention-Preselector Audit v0.1](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/#/doc/idleMaskAudit) gives pair-addressed binary integrity \(T_p\), latent support \(L_p\), viable obligation \(\omega_p=T_pL_p\), and open response \(q_p\), with \(\omega_p\le q_p\le T_p\). Its [Idle-Response Lineage/Gate-History No-Go v0.1](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/#/doc/idleResponseLineage) shows that a terminal sink with retained integrity does not choose close versus hold. The supplied **UD Coefficient Provenance Ledger v0.39(2), Q156/Q167** instead has edge-addressed hard factors \(C_{{\rm cl},e}\), \(T_{{\rm int},e}\), and product \(h_e=C_{{\rm cl},e}T_{{\rm int},e}\), and checks the algebra for all 64 binary six-edge masks. These are distinct objects, even if one eventually assigns them equal numerical values.

The previous [pair-to-edge obstruction v0.1](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T161720Z-codex-pair-edge-22aece15) proves that a deterministic \(S_4\)-equivariant map from pair-only state yields only eight pair-constant masks. Here the exact question is the capacity of an **edge-mask record**, not whether all 64 masks are UD-admissible physical states.

## Exact carrier theorem

Let the four vertex labels be \(0,1,2,3\) and let \(E=\{01,02,03,12,13,23\}\). Its three opposite-edge pairs are \(P_0=(01,23)\), \(P_1=(02,13)\), and \(P_2=(03,12)\); the displayed order is a coordinate convention. The binary mask space is \(M=\{0,1\}^{E}\). Define the record set

\[
R=\prod_{p=0}^2\{(0,\bot),(1,0),(1,1),(2,\bot)\}.
\]

For \(m\in M\), let \(n_p=m_{e_{p,0}}+m_{e_{p,1}}\). If \(n_p=1\), set \(s_p=m_{e_{p,0}}\); otherwise set \(s_p=\bot\). Then \(\operatorname{enc}:M\to R\), \(m\mapsto((n_p,s_p))_p\), is a bijection: \(n=0\) means \((0,0)\), \(n=2\) means \((1,1)\), and \((1,s)\) means \((s,1-s)\). Both sides contain \(4^3=2^6=64\) states. This is an exact, invertible representation, not a source law.

Under \(\pi\in S_4\), permute the three pairs and, when an ordered first edge maps to the target pair's second edge, flip the mixed selector \(s\mapsto1-s\). The action on \(R\) satisfies \(\operatorname{enc}(\pi m)=\pi\operatorname{enc}(m)\). Thus the six-edge record is symmetry covariant, with the within-pair selector transforming nontrivially under the Klein-four kernel \(V_4=\ker(S_4\to S_3)\).

**Independent orbit check.** Each of the three nonidentity elements of \(V_4\) fixes 16 binary masks; identity fixes 64. Burnside gives \((64+3\cdot16)/4=28\) orbits. Direct orbit enumeration also gives 28. Pair counts alone have \(3^3=27\) signatures, but the all-mixed count signature \((1,1,1)\) has *two* \(V_4\) orbits, distinguished by selector parity in the stated coordinate convention. Every other count signature has one orbit. Parity here is a kernel-orbit invariant for that special signature, not a physical chirality or dynamics claim.

## Decision rule still missing

The site audit fixes \(q=0\) for failed integrity and \(q=1\) for viable output, leaving \((T,L)=(1,0)\) ambiguous. Under a previously saturated pair \(q_-=T_-L_-\), the site's close rule \(q_+=T_+L_+\) and hold rule \(q_+=T_+(q_-\lor T_+L_+)\) disagree in exactly one of 16 source transitions: \((T_-,L_-)=(1,1)\to(T_+,L_+)=(1,0)\). Both satisfy the frozen inequality. That is a counterexample to selecting the response from lineage and gate history alone, reproduced here independently as a finite check; it does not prove either rule true. Without previous saturation, disagreement includes any previously open intact-null input with the same intact-null output.

The carrier \(R\) can **record** a supplied edge mask and track externally supplied changes. It does not decide \(C_{{\rm cl},e}\), \(T_{{\rm int},e}\), the product's next value, which pair-level \(q_p\) affects which edge, or the event's physical time. A native decision contract must identify a pre-event state and receipt, domain and codomain, an edge-resolved factor update (or a sourced restriction to pair-constant masks), the intact-sink close/hold rule, and event-order/clock convention. This is the next source dependency. Operational Hodge margins on the live site are typed soft transport margins; reusing them as hard semantic edge factors needs a separate intertwining argument.

## Reproduction and disposition

Run `python3 verify.py` from this package. Standard library only. It verifies bijection; all 24 relabelings on all 64 masks; the four kernel elements; fixed-point and independent direct-orbit counts; count-signature multiplicities; the site's five admissible pair triples; and all 16 saturated local transitions. `results.json` records exact integers. The count of 1,551 assertions is an implementation count, not independent experiments.

- **EXACT, conditional mathematical scope:** invertible covariant record; 28 \(V_4\) orbits; one saturated transition where close/hold differ.
- **CANDIDATE:** use this record as an edge receipt type; no UD event constructor or factor map sourced.
- **OPEN_GATED:** source-admitted edge-mask family, pair-to-edge factor bridge, intact-sink response, hard update, event order and physical clock.
- **NO-GO under present constraints:** the record and pair lineage alone cannot predict the intact-sink switch.
- **Governance:** constructor checks only, non-constructor review pending; no registry promotion; physical promotion remains 0. Prior releases are preserved without amendment.
