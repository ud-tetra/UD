# THM-534: local wake and its mandatory auxiliary source

Development — no registry entry. Exact conditional mathematics, with an explicit new candidate potential. Constructor checked; independent review pending. Physical promotion 0.

## 1. Question and fixed inputs

The v2.0 free-gate Hamiltonian and v2.1 ingress certificate leave a resting off gate stationary. Can a local original-stock term initiate motion without an externally supplied positive gate momentum? Retain the signed contact carrier, original metric and operators, and the supplied canonical pairs \((x,y)\), \((q_e,p_e)\). Set

\[
H_0=\frac12\sum_ep_e^2+y^{\mathsf T}A(q)x,
\quad A(q)=\sum_e\chi_e(q_e)A_e,
\quad \ell_e=y^{\mathsf T}A_ex.
\tag{1}
\]

The auxiliary registers, canonical interpretation, profile and kinetic normalization are candidates, not native UD derivations. Original support receipts follow Q169–Q173 and Q177–Q179. Q153 leaves constitutive source laws open. This work does not fill that gap by relabeling a chosen potential as a native source.

## 2. Rigidity when both support equations are retained

**Theorem W1.** On a connected product coordinate domain, suppose an added differentiable Hamiltonian term \(W(x,y,q)\) retains both original equations

\[
\dot x=A(q)x,\qquad \dot y=A(q)y.
\]

Then \(W\) is independent of \(x,y\). Its gate force cannot depend on local support stock.

**Proof.** Canonical differentiation gives \(\dot x=Ax+W_y\), \(\dot y=Ay-W_x\). The retained equations force \(W_y=W_x=0\) at every state. Connectedness of the support-coordinate fibers makes \(W=V(q)\). Thus \(-W_q\) is independent of support. \(\square\)

If only the original \(x\)-equation is retained, \(W_y=0\) implies \(W=W(x,q)\), and the required auxiliary source is \(-W_x\). This statement concerns Hamiltonians of the displayed form with the same canonical structure; it does not exclude other brackets, new reservoirs, noncanonical models, or waking by a support-independent gate potential.

## 3. A declared local potential and its complete equations

For each contact let \(P_e\) project onto its face and core coordinates and let

\[
S_e=x^{\mathsf T}P_ex=x_f^2+x_\tau^2.
\]

Choose supplied differentiable profiles \(g_e(q_e)\), and add

\[
\boxed{H=H_0-\frac12\sum_e g_e(q_e)S_e.}
\tag{2}
\]

Then the complete canonical equations are

\[
\boxed{\begin{aligned}
\dot x&=A(q)x,\\
\dot y&=A(q)y+\sum_e g_e(q_e)P_ex,\\
\dot q_e&=p_e,\\
\dot p_e&=-\chi'_e(q_e)\ell_e+\frac12g'_e(q_e)S_e.
\end{aligned}}
\tag{3}
\]

The new momentum force and the auxiliary source are the two derivatives of the same interaction. It is not legitimate to claim this canonical Hamiltonian while silently retaining the old homogeneous \(y\)-equation. The new term does not change the original \(x\)-flow, its global norm, or its Q177 ownership weights. It does change the supplied enlarged model and its auxiliary continuity.

For \(F=\sum_e g_e P_ex\), the new receipts are

\[
\frac{d}{ds}\|x\|^2=0,\qquad
\frac{d}{ds}\|y\|^2=2y^{\mathsf T}F,
\tag{4}
\]

and for any fixed control volume \(R\),

\[
\dot S_y(R)=I_y(R)-O_y(R)+2\sum_{i\in R}y_iF_i.
\tag{5}
\]

The original \(x\) cut equation is unchanged. Hamiltonian conservation follows directly:

\[
H_x=-Ay-F,\quad H_y=Ax,\quad
\dot H=H_x\cdot H_y-H_y\cdot H_x+
\sum_e(H_{q_e}p_e+p_e[-H_{q_e}])=0.
\]

Equation (5) means that v2.1's boundary-only credit for \(y\) is insufficient here. To reuse its envelope argument one must additionally bound the positive part of this local source, using remaining credit for \(I_y+[2\sum_{i\in R}y_iF_i]_+\). The envelope derivative then contains the negative part of the source as well as outflow, and is nonpositive. In addition, its gate reserve derivative acquires the extra term \(\tfrac12g'_e S_e p_e\). The previous proof can be extended on a positive-motion interval if \(g'_e\ge0\) and the stronger source-plus-ingress credit contract holds. This is a new conditional contract, not an already available capacity theorem.

## 4. Wake from rest and an exact isolated opening solution

Use the explicit control

\[
g(q)=\alpha q,\qquad \alpha>0.
\tag{6}
\]

The coefficient \(\alpha\), including its units and normalization, is supplied. Choosing \(\alpha=1\) in controls does not derive a parameter-free native law. At \(q=p=0\), \(\chi=\chi'=0\), and

\[
\ddot q(0)=\dot p(0)=\frac\alpha2 S_e(0).
\tag{7}
\]

Thus positive local stock initiates gate motion from rest. For a locally Lipschitz vector field with \(S_e(0)>0\), continuity gives \(q(s)>0\), \(p(s)>0\) for sufficiently small positive \(s\). This is local initiation, not a general network completion theorem. At zero local stock the displayed initial acceleration is zero; future stock arrival requires a separate trajectory analysis.

**Theorem W2.** Consider only one isolated contact, with no other active interactions or wake terms, restrict \(x,y\) to its pair, and initialize \(q(0)=p(0)=0\), \(y(0)=0\), \(S=\|x(0)\|^2>0\). For any smooth plateau profile \(\chi\), equation (3) has the exact solution

\[
\begin{aligned}
q(s)&=\frac{\alpha S}{4}s^2,&
p(s)&=\frac{\alpha S}{2}s,\\
x(s)&=\exp\!\left(A_e\int_0^s\chi(q(u))\,du\right)x(0),&
y(s)&=\frac{\alpha^2S}{12}s^3x(s).
\end{aligned}
\tag{8}
\]

In particular \(\ell(s)=0\), and the gate reaches \(q=1\) at

\[
\boxed{T_{\rm on}=\frac2{\sqrt{\alpha S}}.} \tag{9}
\]

**Proof.** Orthogonality gives constant \(S\). With \(y=a(s)x(s)\), skewness gives \(\ell=a x^{\mathsf T}A_ex=0\). The auxiliary equation becomes \(a'=\alpha q\), while the gate equation is \(p'=\alpha S/2\), \(q'=p\). Integrating with the declared initial conditions gives (8); substitution verifies every equation, and uniqueness establishes the solution. Equation (9) follows from \(q(T)=1\). \(\square\)

For the supplied quintic \(\chi(q)=10q^3-15q^4+6q^5\) on \([0,1]\), put \(k=\alpha S/4\). Before arrival the rotation angle has the exact polynomial expression

\[
\theta(s)=\frac{10k^3}{7}s^7-\frac{15k^4}{9}s^9+
\frac{6k^5}{11}s^{11},\qquad \theta'=\chi(ks^2).
\tag{10}
\]

This is an analytic conditional prediction for the isolated chosen model. It is not a preregistered physical measurement or a prediction for arbitrary overlapping contacts. In the network, \(S_e\) and \(\ell_e\) vary and the adverse term \(-\chi'_e\ell_e\) need not vanish. Positive initial acceleration alone does not establish full opening there.

## 5. What supplies the motion, and what the model fails to supply

Along (8),

\[
\frac{p^2}{2}=\frac{\alpha qS}{2},\qquad
H=\frac{p^2}{2}-\frac{\alpha qS}{2}=0,
\quad \|y\|^2=\frac{\alpha^4S^3}{144}s^6.
\tag{11}
\]

Gate kinetic growth is offset by a decreasing interaction potential. The auxiliary norm grows; it is not an uncharged conserved stock. The potential \(-\alpha qS/2\) is unbounded below for \(q\to+\infty\). In this isolated solution the gate continues to accelerate after reaching its on plateau. The interaction supplies unlimited model work, and neither a finite-capacity reservoir nor a reusable latch/reset cycle has been constructed. Original \(x\)-support remains conserved throughout: it is not depleted by the wake and therefore cannot be called a finite fuel ledger for the kinetic growth.

A bounded profile does not by itself supply universal completion. For example, take \(g(q)=q(1-2q)\) on the transition interval, with a smooth bounded extension outside a neighborhood of that interval. It has \(g'(0)=1\), \(g(0)=0\), and a later zero at \(q_b=1/2\). In the isolated aligned solution \(\ell=0\), conservation gives \(p^2/2=g(q)S/2\); the gate cannot cross a region where \(g<0\). Positive onset force alone is consequently insufficient. Source law, available potential drop and completion must be checked separately.

If the same wake term is attached equivariantly to every contact, all contacts with positive initial stock can begin moving. This supplies no exclusive selector among competing contacts. The original all-off-rest obstruction is escaped by a new interaction, not disproved for the free-gate model.

## 6. Source disposition and next test

The source documents support the original skew flow and its cut receipts. They do not identify the auxiliary dual as native matter, select \(g\), fix \(\alpha\), supply a finite potential reservoir, or derive reset. The present new result is the exact mandatory-source theorem and a constructive isolated wake control, with its funding limitation exposed.

The fresh standard-library verifier checks exact canonical derivatives and Hamiltonian cancellation on the signed carrier, original and auxiliary cut balances, rational wake controls, and polynomial identities for the isolated solution and quintic angle. These are constructor checks supplementing the proofs, not independent peer review. No archived code is executed.

The strongest next step is a finite-capacity interaction with an explicit reservoir receipt, while preserving original support accounting and proving completion for overlapping contacts. Native selection, physical energy/time/action, and quark/lepton identification remain OPEN. Physical promotion 0.
