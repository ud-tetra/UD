# UD pair-to-edge mask bridge obstruction v0.1

**10 October 2026 UTC. Development lane — no registry entry.** This is a constructor-checked finite theorem under stated types, not an admitted constitutive law.

## Source question

The additional [Tetrahedral Packet Complexes site](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/) represents three opposite-edge matching classes by a binary triple. Its [idle-mask theorem](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/#/doc/idleMaskTheorem) constrains pair-indexed \((T,L,q)\) by \(q\leq T\) and \(TL\leq q\), leaving \(q\) free at intact-null \((T,L)=(1,0)\). [Paper I](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.pdf) gives the \(S_4\to S_3\) matching action with four-element kernel and says the source of event receipts remains open. The supplied coefficient ledger v0.39(2), Q156, instead defines an edge-indexed hard product \(h_e=C_{{\rm cl},e}^{\rm hard}T_{{\rm int},e}^{\rm hard}\); Q167 algebraically verifies its vertex–edge current over all \(2^6=64\) single-tetrahedron masks.

The question is whether **pair-indexed state alone** can produce every six-edge hard mask through a deterministic rule covariant under all tetrahedral vertex relabelings. This asks about representation capacity, not physical realizability of each algebraic mask.

## Exact symmetry obstruction

The three matching classes are \(P_A=\{01,23\}\), \(P_B=\{02,13\}\), and \(P_C=\{03,12\}\). Let \(V_4=\ker(S_4\to S_3)\). Every element of \(V_4\) acts trivially on any state made solely of pair-indexed bits, including triples \(q,T,L\). On edges, \(V_4\) exchanges the two edges in each matching class. Therefore any deterministic \(S_4\)-equivariant map \(F\) from such pair state to a six-edge binary mask obeys

\[
F(x)=F(gx)=gF(x)\quad(g\in V_4).
\]

Its output must be constant on each opposite-edge pair. There are only \(2^3=8\) such masks among the \(2^6=64\) algebraically allowed masks. Thus **56 single-tetrahedron mask patterns cannot be represented by any pair-only equivariant map**, regardless of its nonlinear Boolean formula. The conclusion does not assert that the excluded masks occur in UD; it shows what a proposed pair-to-edge bridge cannot cover without an edge-resolved state or an explicitly declared symmetry reduction.

For illustration, the mathematically natural *candidate* lift copies each pair bit to both member edges: \(C_e=q_{P(e)}\), \(T_e=T_{P(e)}\), \(h_e=q_{P(e)}T_{P(e)}\). This candidate is \(S_4\)-equivariant, but **the sources do not identify these differently typed factors**. The idle-mask constraints admit \(5^3=125\) three-pair \((T,L,q)\) states; their candidate hard masks realize all eight pair-constant patterns and no other masks. At an intact-null pair, fixed \((T,L)=(1,0)\) still allows both \(q=0\) and \(q=1\), producing different candidate hard masks. Symmetry and admissibility leave the switch unresolved.

## Replay and interpretation

Run `python3 verify.py`. Fifteen exact assertions pass: all 24 vertex permutations, the four kernel elements and their edge orbits, equivariance of the candidate copy lift, closure of the 125 admissible states under relabeling, the eight-mask image, 56-mask complement, and an intact-null divergent pair. The general map obstruction follows from the kernel-fixed proof above; the finite replay checks its carrier and the candidate fixture.

This sharpens the [live-site crosswalk](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T161257Z-codex-site-crosswalk-3f6a18b7). An edge-resolved receipt must carry information that transforms nontrivially under \(V_4\) if all 64 algebraic masks are intended. A separate source could instead restrict the physical mask family to pair-constant patterns. Either route still needs a pre-event law for the intact-null response, event address and ordering, and the relation to face gates. The site's operational Hodge margins are not a proved substitute for those hard semantic predicates.

## Governance footer

- **EXACT (conditional types):** pair-only \(S_4\)-equivariant output is opposite-edge constant; 15 replay checks pass.
- **CANDIDATE:** copy \(q,T\) from pair classes onto both member edges; no sourced typed identification.
- **OPEN:** permitted edge-mask family, edge-resolved source receipts, intact-null decision, hard gate update and timing.
- **Review:** constructor verification only; independent adversarial review pending. **Physical promotion: 0.**
