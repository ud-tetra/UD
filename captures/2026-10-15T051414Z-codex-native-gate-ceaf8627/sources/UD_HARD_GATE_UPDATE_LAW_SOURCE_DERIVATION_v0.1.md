# UD Hard-Gate Update-Law Source Derivation v0.1

**Date:** 2026-08-23  
**NEXUS:** HELD  
**CROWN:** OFF  
**Physical promotion:** 0  
**Verdict:** `PARTIAL_PASS__BOOLEAN_UPDATE_FACTORIZATION_CLOSED__PREDICATE_DYNAMICS_SOURCE_BLOCKED`

## 1. Current source object

The current hard boundary gate is

\[
h_e
=
C_{{\rm cl},e}^{\rm hard}
T_{{\rm int},e}^{\rm hard}.
\]

This is sufficient to derive exact Boolean transition causes, provided the two factors are themselves available event by event.

## 2. Minimal update form

For primitive event \(E_n\),

\[
\boxed{
h_e^{n}
=
C_{{\rm cl},e}^{\rm hard}(E_n)
T_{{\rm int},e}^{\rm hard}(E_n).
}
\]

The gate history is therefore reducible to the paired predicate histories

\[
\left\{
C_{{\rm cl},e}^{\rm hard}(E_n),
T_{{\rm int},e}^{\rm hard}(E_n)
\right\}.
\]

This is a useful reduction:

\[
\boxed{
\text{gate-history problem}
\to
\text{closure-predicate history}
+
\text{transport-predicate history}.
}
\]

## 3. Current source gap

The current reproducible source package does not supply source-complete transition laws of the form

\[
C_{{\rm cl},e}^{\rm hard}(E_{n+1})
=
\mathcal C(\text{primitive packet data})
\]

and

\[
T_{{\rm int},e}^{\rm hard}(E_{n+1})
=
\mathcal T(\text{primitive packet data})
\]

with exact threshold/source definitions sufficient to replay an ordered gate history.

Therefore no historical \(M_{\rm loss}\) can yet be reconstructed from current v0.39.

### AUTO_LOCK

`HARD_GATE_HISTORY_REDUCES_TO_CLOSURE_AND_TRANSPORT_PREDICATE_HISTORIES_BUT_CURRENT_PREDICATE_DYNAMICS_ARE_SOURCE_BLOCKED_RULE_v0.1`

## 4. Required primitive derivation

The next source-complete law must define, for every relevant edge/face channel:

\[
C_{\rm cl}^{\rm hard}
:
\mathcal X_{\rm packet}
\to\{0,1\},
\]

\[
T_{\rm int}^{\rm hard}
:
\mathcal X_{\rm packet}
\to\{0,1\}.
\]

Each must provide:

- exact input carrier;
- exact threshold/zero criterion;
- relabeling covariance;
- event update rule;
- null/reduction limit;
- no free tuning scalar.

## 5. Conclusion

The hard-gate formula is not the missing attenuation coefficient.

It is the logical selector architecture.

The missing object is now narrower:

\[
\boxed{
\text{primitive packet state}
\to
(C_{\rm cl}^{\rm hard},T_{\rm int}^{\rm hard})
\to
h_e.
}
\]
