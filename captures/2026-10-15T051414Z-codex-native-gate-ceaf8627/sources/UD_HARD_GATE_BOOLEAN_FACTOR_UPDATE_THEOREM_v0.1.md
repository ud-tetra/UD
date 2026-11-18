# UD Hard-Gate Boolean-Factor Update Theorem v0.1

**Date:** 2026-08-23  
**Physical promotion:** 0  
**Status:** `PASS — EXACT CONDITIONAL BOOLEAN THEOREM`

Current source gives the hard gate in factored form

\[
\boxed{
h_e
=
C_{{\rm cl},e}^{\rm hard}
T_{{\rm int},e}^{\rm hard}.
}
\]

Assume the declared hard factors are Boolean:

\[
C_{{\rm cl},e}^{\rm hard},
T_{{\rm int},e}^{\rm hard}
\in\{0,1\}.
\]

Then \(h_e\) is their logical AND.

## Gate closure

A gate closes between events \(n-1\) and \(n\),

\[
h_e^{n-1}=1,
\qquad
h_e^n=0,
\]

iff

\[
C_{e}^{n-1}=1,
\qquad
T_{e}^{n-1}=1
\]

and at least one post-event factor fails:

\[
\boxed{
C_e^n=0
\quad\lor\quad
T_e^n=0.
}
\]

Thus closure events admit exact cause tags:

1. closure-admissibility failure:
   \[
   C:1\to0,\quad T^n=1;
   \]
2. transport-integrity failure:
   \[
   T:1\to0,\quad C^n=1;
   \]
3. joint failure:
   \[
   C^n=T^n=0.
   \]

### AUTO_LOCK

`HARD_GATE_CLOSURE_OCCURS_IFF_PREVIOUS_CLOSURE_AND_TRANSPORT_PREDICATES_PASS_AND_AT_LEAST_ONE_POSTEVENT_PREDICATE_FAILS_THEOREM_v0.1`

## Gate opening

A gate opens,

\[
h_e^{n-1}=0,
\qquad
h_e^n=1,
\]

iff both post-event predicates pass:

\[
C_e^n=T_e^n=1
\]

and at least one pre-event predicate failed.

### AUTO_LOCK

`HARD_GATE_OPENING_OCCURS_IFF_BOTH_POSTEVENT_HARD_PREDICATES_PASS_AFTER_AT_LEAST_ONE_PREVIOUS_FAILURE_THEOREM_v0.1`

## What is not derived

This theorem does not derive the temporal laws for

\[
C_{{\rm cl},e}^{\rm hard}(n)
\]

or

\[
T_{{\rm int},e}^{\rm hard}(n).
\]

It closes only the Boolean factor logic once those predicate states are supplied.
