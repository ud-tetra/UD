# UD native-current first-jet activity certificate v0.1

**Date:** 10 October 2026 UTC. **Physical promotion:** 0. Constructor verification; independent review pending.

## Source and scope

Ledger Q166 supplies the real directed adjacent-degree support-current form \(J_{\sigma\tau}=2B_{\sigma\tau}c_\sigma c_\tau\) for degrees 01, 12 and 23. Q165 supplies the native support register. The preceding [native-current address audit](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T152820Z-codex-current-address-d4a8b320) found an active face–cell orbit on which the Q167 vertex–edge currents stay zero. This continuation checks whether **all 47 native directed incidence currents and their first Lie derivatives** detect activity at an instant. It uses the fixed, ungated two-tetrahedron generator \(A=B^T-B\) and its dimensionless native evolution parameter. No derivative is identified with physical seconds or a primitive gate event.

## The exact theorem

On \(K=\langle0123,0124\rangle\), let \(c\in\mathbb R^{23}\). For every oriented adjacent-degree incidence \((i,j)\) with nonzero boundary coefficient \(b_{ij}=\pm1\), put

\[
J_{ij}(c)=2b_{ij}c_i c_j,
\qquad
L_AJ_{ij}(c)=2b_{ij}\bigl((Ac)_i c_j+c_i(Ac)_j\bigr).
\]

The carrier has \(18\) vertex–edge, \(21\) edge–face and \(8\) face–cell incidences, totaling \(47\). The exact rational rank is \(\operatorname{rank}A=22\), and \(\ker A\) is the uniform vertex line.

\[
\boxed{
Ac\ne0
\quad\Longleftrightarrow\quad
\exists(i,j):\ J_{ij}(c)\ne0\ \text{or}\ L_AJ_{ij}(c)\ne0.
}
\]

**Proof of the nontrivial direction.** Suppose every \(J_{ij}=0\), so along each incidence at least one endpoint amplitude is zero. The support of \(c\) is an independent set in the incidence graph. If \(Ac\ne0\), pick coordinate \(j\) with \((Ac)_j\ne0\). Its own amplitude must be zero: if \(c_j\ne0\), every incident neighbor amplitude is zero, forcing \((Ac)_j=0\). Since \((Ac)_j\) is a nonzero sum of incident contributions, some neighbor \(i\) has \(c_i\ne0\). Then on that incidence, \(L_AJ_{ij}=2b_{ij}c_i(Ac)_j\ne0\) (with the corresponding index order). This argument holds for any finite skew incidence generator with nonzero link weights. Conversely on this carrier, \(Ac=0\) means \(c\) is uniform on vertices and zero on higher degrees, so both every current and every slope vanish. \(\square\)

The rank calculation establishes that last carrier-specific converse. On a different complex with additional zero modes, a stationary mode needs a separate current check before claiming the same equivalence.

## Exact blind-instant witness

Set all vertices, edges and faces to zero and take the two cell amplitudes \(c_3=(1,-1)\). The state is active because its face derivative is \(-B_3(1,-1)\ne0\). All \(47\) directed currents are zero at this instant. The two shared-face incidence slopes vanish, while each of the six private face–cell current slopes equals exactly \(-2\). Thus the first jet detects activity at a snapshot where a current-only observer is blind.

This example is distinct from the all-time **vertex–edge** blindness in the previous audit. On its ongoing face–cell orbit, face–cell currents generally become nonzero. The first jet repairs instantaneous activity detection by using all adjacent degrees; it does not create a localized edge address.

## Replay and disposition

Run `python3 verify.py` in this release directory. The standard-library Fraction replay checks \(f=(5,9,7,2)\), the 47 incidence counts, skewness, rank 22 and uniform null mode, the exact blind instant, and 23 singleton preparations. **12 named assertions pass.** The general theorem rests on the proof above; the finite fixtures are constructor checks, not independent review.

- **EXACT:** \((J,L_AJ)\) detects native activity on this fixed carrier.
- **OPEN:** whether this Lie-derivative observation is causally available before a primitive event, a choice of particular edge/face when several slopes tie, a source-selected Boolean predicate update, and event timing.
- **NO PROMOTION:** activity detection is not gate admissibility, and the native evolution parameter is not physical time. Physical promotion remains 0.

At the displayed witness, six slopes are equal and the shared-face slopes are zero. A next candidate may retain the **set** of active incidences as a covariant receipt, but any single-edge/face choice needs an additional prospective address or a sourced multi-incidence event rule. Do not break the tie by an arbitrary label order.
