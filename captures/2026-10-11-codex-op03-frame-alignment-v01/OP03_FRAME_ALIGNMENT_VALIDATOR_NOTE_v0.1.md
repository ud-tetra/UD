# OP03 frame-alignment guard audit v0.1

**11 October 2026 UTC · pretarget constructor-side audit · no independent endpoint · physical promotion 0.** This note is an append-only clarification of a candidate implementation boundary. It does not amend the frozen acquisition protocol v0.2 or candidate v0.2.1 decision semantics, and it is not a non-constructor review.

## Source, object, and scope

- `UD_OPEN_SYSTEM_HAMMING_BUDGET_RECEIPT_INDEX_LAW_v0.2 (1).md` (30 August 2026), §§1.1, 7, 8, 10: the input is raw `theta^-` in the source pair basis; a certified relative frame `r` induces `bar(theta)^- = P_{pi(r)} theta^-` in the output pair basis; the affine toggle compares `bar(theta)^-` to `theta+`.
- [Independent producer handoff v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-11T020241Z-codex-op03-producer-handoff-23f7e091/PROVIDER_HANDOFF_v0.1.md) requires a pre-event frame receipt and distinct full endpoint lane. The underlying acquisition protocol is `UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.2_RECEIPT_INDEX.md` (30 August 2026), §§Pre-event frame packet–Frozen prediction.
- [Candidate guard v0.2.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-11T014149Z-codex-memory-seat-b7043e45/PROTOCOL_v0.2.1_CANDIDATE.md), §§Inputs–Candidate decision order, already writes `a = bar(theta)^- XOR theta+` and preserves frame-only changes as separate typed records.
- [Constructor census](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-11T014149Z-codex-memory-seat-b7043e45/guard_replay.py) passes a single `theta` bit mask to `typed_guard` and tests only pair-coordinate relabeling covariance, not the raw-to-aligned frame step. Its 13,824 cases therefore certify the conditional seat guard when the input is already aligned; they do not certify caller alignment.

Let `raw` and `out` be three-bit masks in **different** pair-coordinate bases, `p = pi(r) in S3`, `bar = P_p raw`, and `seat` be the frozen coordinate-complete viable output seats in the output basis. When every open seat passes integrity, `out = 7 XOR seat`. The event flag is `bar XOR out != 0`. The tempting direct test `raw XOR out != 0` compares masks in different bases and is not generally invariant.

## Exact finite audit and independent count

`op03_frame_alignment_guard_check.py` enumerates 6 pair-frame permutations, 8 raw states, 8 output-seat masks, and 8 integrity masks. There are `3^3 = 27` integrity-admitted seat/integrity combinations, hence `6*8*27 = 1,296` admitted cases. It checks the event flag in the output basis and then redefines the whole typed packet under each of six output relabelings (`7,776` covariance comparisons).

| Result | Count | Meaning |
|---|---:|---|
| Identity-frame admitted | 216 | No raw/aligned distinction |
| Nonidentity-frame admitted | 1,080 | Alignment matters for some masks |
| Correct no-change | 162 | `bar XOR out = 0` |
| Correct Θ switch | 1,134 | `bar XOR out != 0` |
| Zero-index Θ switch | 216 | `popcount(out) = popcount(bar)` with nonzero toggle |
| Raw-versus-aligned event disagreement | 144 | Conditional misuse witness, not protocol failure |
| Relabeling covariance failures | 0 | Full typed packet transformed together |

The 144 count has a separate exact combinatorial check. Among the five nonidentity permutations, three transpositions each change two weight-one and two weight-two raw masks; for each changed raw mask, each of the two possible matching endpoints has `2^weight(raw)` compatible integrity masks. This gives `3*[2*(2*2)+2*(2*4)] = 72`. Two 3-cycles each change three weight-one and three weight-two masks, giving `2*[3*(2*2)+3*(2*4)] = 72`. Total `144`. The remaining masks either are fixed by the frame action or lead to the same event flag under both comparisons.

**Explicit conditional witness:** take raw mask `001` in source pair coordinates; a certified frame with pair projection swapping A and B gives aligned mask `010`. Frozen output seats A and C have seat mask `101`, intact integrity `111`, and endpoint mask `010`. Then `mu = 0`, correct affine toggle `010 XOR 010 = 000`, and the candidate returns `ADMISSIBLE_NO_CHANGE`. Directly comparing raw `001` with output `010` falsely emits toggle `011` and would reset the first-switch index one window too early. This is a pair-projection fixture; no independent physical frame or event is asserted.

## Disposition

**EXACT under finite three-seat masks:** 1,296 admitted cases, 144 potential raw/aligned event-label disagreements, and 0/7,776 typed relabeling failures, with an independent analytic count of the disagreements. **NO-GO for an unaligned caller:** it can misclassify a frame-only window as a Θ switch. **CANDIDATE implementation guard:** require `bar = P_{pi(r)} theta^-` after exact frame certification; verify the pre-event lineage dimension against `3 - popcount(bar)`; pass `bar` and output-basis seats to the seat/no-op guard; record both masks; advance `tau_Theta` only for nonzero aligned toggle. **OPEN:** integration with an independently governed producer, external adversarial review, source-complete signed S4 frame, hidden endpoints, and a physical bridge. The v0.2.1 protocol already specifies the correct formula, so no frozen decision threshold is changed.

Reproduce with `python3 op03_frame_alignment_guard_check.py > RESULTS.json`. The script uses only Python 3 standard library and integer arithmetic. `RESULTS.json` is a synthetic exact calculation, not a target score.
