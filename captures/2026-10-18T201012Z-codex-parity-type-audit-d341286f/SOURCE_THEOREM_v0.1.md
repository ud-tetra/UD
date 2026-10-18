# UD_HODGE_EVENT_RETAINED_PARITY_CARRIER_THEOREM_v0.1

**Date:** 2026-09-18  
**Status:** LOCKED INTERNAL MATHEMATICS / STANDALONE CARRIER THEOREM  
**Physical promotion:** 0

## Theorem

Let:

1. \(\mathcal H_{\rm evt}^{Hodge}\) be the selected rank-six Hodge event sector;
2. \(W:\mathbb R^6\to\mathcal H_{\rm evt}^{Hodge}\) be its exact orthonormal Darboux embedding;
3. \(T_H=W^\top\) be the Hodge→event Darboux coordinate map;
4. 
   \[
   R_{\rm fib}
   =
   \operatorname{diag}(I_3,-I_3)
   \]
   be canonical cotangent fiber inversion on the event carrier;
5. 
   \[
   \Theta_H
   =
   WR_{\rm fib}W^\top
   \]
   be the transported Hodge parity;
6. 
   \[
   \mathcal I_c
   =
   \operatorname{diag}(cI_3,c^{-1}I_3),
   \qquad c>0,
   \]
   be any orientation-preserving diagonal member of the Q121 \(S_4\)-equivariant symplectic carrier family;
7. 
   \[
   R_{qm}
   =
   \operatorname{diag}(I_3,-I_3)
   \]
   on the aligned retained carrier \(V_{3,q}\oplus V_{3,m}\).

Then the parity carrier diagram commutes:

\[
\boxed{
T_H\Theta_H
=
R_{\rm fib}T_H,
}
\]

and

\[
\boxed{
R_{\rm fib}\mathcal I_c
=
\mathcal I_cR_{qm}
}
\]

for every \(c>0\).

Therefore

\[
\boxed{
T_H\Theta_H
\mathcal I_c
=
R_{\rm fib}T_H\mathcal I_c
}
\]

with parity preserved at each carrier map.

---

## Proof

Because

\[
W^\top W=I_6,
\]

we have

\[
T_H\Theta_H
=
W^\top
WR_{\rm fib}W^\top
=
R_{\rm fib}W^\top
=
R_{\rm fib}T_H.
\]

Next,

\[
R_{\rm fib}
=
\begin{pmatrix}
I_3&0\\
0&-I_3
\end{pmatrix}
\]

and

\[
\mathcal I_c
=
\begin{pmatrix}
cI_3&0\\
0&c^{-1}I_3
\end{pmatrix}
\]

are block diagonal, so they commute:

\[
R_{\rm fib}\mathcal I_c
=
\mathcal I_cR_{qm}.
\]

No Hamiltonian coefficient or frequency enters either identity.

\[
\square
\]

---

## Corollary 1 — parity closes below dynamics

The theorem is independent of:

\[
k_{\rm event},
\qquad
\kappa_{\rm loop},
\qquad
c_{\rm evt\leftarrow HD},
\qquad
\omega_{\rm evt}.
\]

Therefore carrier-level parity compatibility is logically prior to and independent of the SA-023 Hamiltonian identity.

### AUTO_LOCK

`HODGE_EVENT_RETAINED_PARITY_CARRIER_DIAGRAM_COMMUTES_INDEPENDENTLY_OF_HAMILTONIAN_NORMALIZATION_v0.1`

---

## Corollary 2 — anti-symplectic type is preserved

On the event carrier,

\[
R_{\rm fib}^\top J_0R_{\rm fib}
=
-J_0.
\]

On the selected Hodge sector,

\[
\Theta_H^\top J_H\Theta_H
=
-J_H.
\]

Thus the Hodge and event parity operators have the same anti-symplectic type.

On the aligned retained carrier, \(R_{qm}\) likewise reverses the canonical symplectic form.

Hence the commuting diagram preserves both:

- \(3+3\) parity grading;
- anti-symplectic type.

---

## Corollary 3 — Lagrangian halves correspond

The event \(+/-\) parity sectors are

\[
W_3^Q,
\qquad
W_3^P.
\]

The selected Hodge \(+/-\) sectors are

\[
W(W_3^Q),
\qquad
W(W_3^P),
\]

which are the exact Hodge \(Q\) and \(P=JQ\) Lagrangian halves.

Under the diagonal Q121 alignment these correspond to

\[
V_{3,q},
\qquad
V_{3,m}.
\]

Therefore the parity carrier theorem preserves the entire rank-\(3+3\) Lagrangian decomposition.

---

## Copy-swap qualification

Q121 also permits the canonical copy swap

\[
S=
\begin{pmatrix}
0&I_3\\
I_3&0
\end{pmatrix}.
\]

It obeys

\[
\boxed{
SR_{qm}S^\top
=
-R_{qm}.
}
\]

Thus the copy-swapped branch preserves parity structure while exchanging the labels “even” and “odd”.

Any statement specifically naming \(q\) even and \(m\) odd must use the diagonal alignment branch.

---

## Scope

This theorem proves only carrier/parity structure.

It does not prove:

- SA-023 response/state Hamiltonian identity;
- physical time reversal;
- physical \(CP/T\) symmetry;
- event-response ontology;
- parity on the Hodge complement.

### Correspondence packet

- **internal object:** selected Hodge/event/retained carrier parity;
- **internal claim bin:** LOCKED INTERNAL MATHEMATICS;
- **correspondence status:** FORMAL_CORRESPONDENCE between typed carriers;
- **physical promotion:** 0.

---

## Governance

### AUTO_LOCK
- parity carrier commutation;
- anti-symplectic type preservation;
- Lagrangian \(3+3\) correspondence;
- independence from Hamiltonian normalization.

### AUTO_FREEZE
- using this theorem to claim SA-023;
- using it as physical time-reversal evidence;
- erasing the Q121 copy-swap qualification.

**Physical promotion:** 0.
