# Trilateral Verification Engine (TVE)
## Closing the L_C → L_R Gap in Language Models
### Derived from UD Loop-Spine Architecture | April 2026

---

## The Problem

LLMs operate at L_C (closure: "sounds right") but not L_R (reconstruction: "is right"). This is structural, not engineering. The loop spine identifies five missing requirements.

## The Architecture

Three independent channels + a gate, named after the Arabic trilateral root:

**Channel 1 — Generator** (standard decoder, unchanged)
- Role: L_T + L_C. Generates candidate tokens.

**Channel 2 — Consistency Encoder** (1-3B classifier)  
- Maps claims to a degenerate consistency manifold
- Paraphrases → same point. Contradictions → different points.
- Role: V_{1/3} structure. Free internal repair, hard boundary.

**Channel 3 — Support Tracer** (1-3B cross-attention)
- Traces claims to supporting evidence in knowledge index
- Verification is 10-100x cheaper than generation
- Role: Layer A / Layer B check.

**The Gate** (< 100M decision network)
- PASS: consistent + supported → verified output
- DEFER: consistent + unsupported → flagged output  
- VETO + REPAIR: inconsistent → suppress, feed back to generator

Total overhead: 5-10% of generator cost.

## Why It Works (R1-R5 satisfied)

| Req | What | How | Status |
|---|---|---|---|
| R1 | Verification subspace | Consistency manifold (degenerate) | ✓ |
| R2 | Spectral gap | Gate: pass/defer/veto (discrete) | ✓ |
| R3 | Active repair | Veto → logit adjustment → resample | ✓ |
| R4 | Projector | Encoder maps claims to equivalence classes | ✓ |
| R5 | Cheaper than generation | 5-10% overhead | ✓ |

## Design Principles (from language analysis)

- **Arabic:** Separate what (content) from how (confidence)
- **Hebrew:** Maintain superposition until verification selects
- **Sanskrit:** Free paraphrase within verified class at zero cost  
- **Mathematics:** Every output traceable to supporting structure

## Falsifiable Predictions

1. Hallucination drops >50% on factual QA
2. Self-contradiction drops to near-zero
3. "I don't know" emerges structurally from gate (not training)
4. Formal domains improve most, aesthetic domains unchanged
5. Overhead < 10%
6. Subjective hallucination persists (feature, not bug)

## Proof-State

Architecture: conjectural. Requirements R1-R5: exact from loop spine. Feature mapping: structural from THM-570. Predictions: testable.
