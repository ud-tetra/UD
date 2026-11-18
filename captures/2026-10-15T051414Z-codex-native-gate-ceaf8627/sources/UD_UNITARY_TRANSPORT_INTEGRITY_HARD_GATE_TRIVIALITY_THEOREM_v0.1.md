# UD Unitary-Transport Integrity Hard-Gate Triviality Theorem v0.1

**Date:** 2026-08-23  
**Physical promotion:** 0  
**Status:** `PASS — CONDITIONAL EXACT THEOREM`

Let transport on edge \(e\) be represented by

\[
U_e
\]

on a declared finite inner-product carrier.

Define

\[
T_{{\rm int},e}^{\rm hard}
=
\mathbf1[
U_e^\dagger U_e=I
].
\]

If the source restricts the transport family to exact unitary operators,

\[
U_e\in U(d)
\]

for every active edge, then

\[
\boxed{
T_{{\rm int},e}^{\rm hard}=1
}
\]

for every active edge and every event.

Thus the transport-integrity factor cannot dynamically close a gate in the exact closed-unitary sector.

### AUTO_LOCK

`CLOSED_UNITARY_TRANSPORT_FAMILY_MAKES_TRANSPORT_INTEGRITY_HARD_PREDICATE_DYNAMically_TRIVIAL_RULE_v0.1`

## Open-system implication

To obtain a nontrivial transport-integrity history, UD must source at least one of:

- nonunitary open-system transport;
- missing transport channel;
- explicitly projected/lost transport image;
- transport sink/dissipation law;
- source-defined integrity defect outside the unitary carrier.

The size of such a defect may be soft.

The hard predicate itself remains exact zero/nonzero unless a nonzero margin is independently sourced.
