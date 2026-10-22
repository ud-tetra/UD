# THM-534: bounded stored potential, depletion and conditional opening

Development — no registry entry. Exact conditional model; constructor checked, independent review pending. Physical promotion 0.

## 1. Fixed carrier, changed candidate interaction

The v2.2 linear wake interaction is unbounded below. Replace that *candidate* interaction while retaining the original skew carrier, metric, particle operators and the supplied canonical coordinates \((x,y,q,p)\). For each signed face/core contact \(e\), let \(P_e\) project onto its two endpoints,

\[
S_e=x^{\mathsf T}P_ex,\qquad
\ell_e=y^{\mathsf T}A_ex,\qquad
A(q)=\sum_e\chi_e(q_e)A_e.
\]

Use the supplied bounded potential profile

\[
U_e(q)=\frac{2\beta_e}{1+(q+1)^2},\qquad \beta_e>0,
\quad R_e=\frac12U_e(q_e)S_e,
\tag{1}
\]

and Hamiltonian

\[
\boxed{H=K+C+R,
\quad K=\frac12\sum_ep_e^2,
\quad C=\sum_e\chi_e\ell_e,
\quad R=\sum_eR_e.}
\tag{2}
\]

The positive quantities \(R_e\) are stored interaction potential, not extra independent reservoir coordinates. The shift in (1), \(\beta_e\), canonical units and gate preparation remain supplied constitutive choices. There is no source derivation making them parameter-free or identifying them with native physical energy. Q169–Q173/Q177–Q179 anchor original support receipts; Q153, Q156 and G05 remain open at their stated constitutive and physical boundaries.

Canonical differentiation gives

\[
\begin{aligned}
\dot x&=Ax, &\dot y&=Ay-F, &F&=\sum_eU_eP_ex,\\
\dot q_e&=p_e, &\dot p_e&=f_e-\chi'_e\ell_e,
&f_e&=-\frac12U'_eS_e
=\frac{2\beta_e(q_e+1)S_e}{[1+(q_e+1)^2]^2}.
\end{aligned}
\tag{3}
\]

The auxiliary source changes sign relative to the v2.2 negative-potential example, as required by the new Hamiltonian. Original \(x\)-norm and owned-support continuity remain unchanged. The auxiliary cut receipt has source \(-2\sum_{i\in R_0}y_iF_i\) for any fixed volume \(R_0\); the old boundary-only auxiliary budget cannot be silently reused.

## 2. Exact network depletion receipt and its limitation

**Theorem P1.** Along (3), \(H\) and \(N=\|x\|^2\) are conserved. With \(\dot\chi_e=\chi'_e p_e\), the local receipts are

\[
\dot R_e=-f_ep_e+\frac{U_e}{2}\dot S_e,
\qquad
\dot K_e=f_ep_e-\ell_e\dot\chi_e.
\tag{4}
\]

Consequently

\[
\boxed{\dot K+\dot R
=\sum_e\left(\frac{U_e}{2}\dot S_e-\ell_e\dot\chi_e\right),}
\tag{5}
\]

and the change of \(C\) is precisely the negative of the right hand side.

**Proof.** Equation (4) is the chain rule for (1) and the gate equation. Skewness gives \(\dot N=0\), and the canonical bracket gives \(\dot H=0\). For a direct coupling check, differentiation gives

\[
\dot\ell_e=y^{\mathsf T}[A_e,A]x-F^{\mathsf T}A_ex,
\quad
\dot C=\sum_e\ell_e\dot\chi_e-F^{\mathsf T}Ax.
\]

The double commutator sum cancels because \(\sum_e\chi_e[A_e,A]=[A,A]=0\). Since \(\dot S_e=2x^{\mathsf T}P_eAx\), \(F^{\mathsf T}Ax=\sum_e(U_e/2)\dot S_e\). This proves the claimed receipt directly. \(\square\)

The potential is globally nonnegative and bounded: \(0<U_e\le2\beta_e\). Thus

\[
0\le R\le\sum_e\beta_eS_e
\le b_*N,\qquad
b_*:=\max_i\sum_{e\ni i}\beta_e.
\tag{6}
\]

For uniform \(\beta\) on the eight contacts of \(K_-\), \(b_*=4\beta\). This bounds stored potential at every network state; it does not make \(R_e\) monotone. Incoming support and gate reversal can replenish it through (4).

Crucially, \(C=y^{\mathsf T}Ax\) remains sign-indefinite and unbounded over unrestricted \(y\). Equation (5) is therefore not a proof that all network kinetic work is funded only by initial \(R\). A globally bounded potential component is weaker than a positive finite-resource Hamiltonian. Only the isolated invariant preparation below supplies a closed nonnegative funding receipt. No finite reservoir, generic network completion, or reset is claimed for arbitrary overlapping contacts.

## 3. Isolated opening theorem with a strict burden margin

For one isolated contact, restrict both fields to its pair. Then \(S=\|x\|^2\) and \(\ell=y^{\mathsf T}A_ex\) are constant, including under the auxiliary source \(-Ux\): its extra contribution is \(-U x^{\mathsf T}A_ex=0\). Initialize \(q(0)=p(0)=0\), \(S>0\), with arbitrary finite \(y(0)\). Write

\[
B=\frac{\beta S}{2},\quad
\phi(q)=1-\frac{U(q)}\beta
=\frac{q(q+2)}{q^2+2q+2},\quad
D(q)=B\phi(q)-\ell\chi(q).
\tag{7}
\]

Energy conservation gives the exact first integral

\[
\frac{p^2}{2}=D(q),\qquad \ddot q(0)=B>0.
\tag{8}
\]

Let \(\chi\) be the supplied quintic plateau profile on \([0,1]\), so \(0\le\chi'\le15/8\), \(\chi(0)=0\), \(\chi(1)=1\). Define \(\ell_+=\max(\ell,0)\).

**Theorem P2.** If

\[
\boxed{\delta=B-\frac{25}{8}\ell_+>0,} \tag{9}
\]

then the isolated gate reaches \(q=1\) from rest in finite model time and

\[
T_{\rm on}\le2\sqrt{\frac5{6\delta}}.
\tag{10}
\]

**Proof.** For \(0\le q\le1\),

\[
\phi(q)\ge\frac35q,
\quad
5(q+2)-3(q^2+2q+2)=(1-q)(3q+4)\ge0.
\]

The derivative bound gives \(\chi(q)\le(15/8)q\le(25/8)\phi(q)\). Hence \(D(q)\ge\delta\phi(q)\ge3\delta q/5>0\) for \(q>0\). Since \(\ddot q(0)=B>0\), positive motion starts by local uniqueness and Taylor expansion. It cannot stop inside the interval because (8) then has a strictly positive right hand side. The travel-time integral is bounded by

\[
\int_0^1\frac{dq}{\sqrt{2D(q)}}
\le\int_0^1\sqrt{\frac5{6\delta q}}\,dq
=2\sqrt{\frac5{6\delta}}.
\]

The integrable square-root singularity at rest is essential: the earlier prepared-momentum proof is not being reused at \(p=0\). \(\square\)

This is sufficient, not necessary. At arrival the exact kinetic stock is

\[
K_{\rm on}=\frac35B-\ell. \tag{11}
\]

For example, if \(\ell>3B/5\), full arrival is impossible since (11) is negative. Small auxiliary preparation is allowed by (9); a worst-case bound \(B\ge B_{\min}\), \(\ell_+\le L\) gives a robust sufficient margin \(B_{\min}-(25/8)L>0\), conditional on isolation, the chosen profile, potential and initial gate position/rest preparation. This is not robustness to arbitrary network influx or arbitrary constitutive changes.

## 4. Closed positive funding for zero initial dual

For \(y(0)=0\), \(\ell=0\). The isolated solution obeys

\[
\boxed{K+R=B,\qquad
K=B\phi(q),\quad R=\frac{\beta S}{1+(q+1)^2}.}
\tag{12}
\]

On the positive-motion branch, \(R\) decreases and \(K\) increases, with \(0\le K<B\). The potential source replaces the unbounded linear work supply of v2.2. At opening,

\[
R_{\rm on}=\frac{\beta S}{5},\qquad
K_{\rm on}=\frac{3\beta S}{10};
\tag{13}
\]

as \(q\to\infty\), \(R\to0\), \(K\to B\) and \(p\to\sqrt{\beta S}\). Complete depletion is asymptotic, not a finite-position cutoff.

The exact opening time is the quadrature

\[
T_{\rm on}=\frac1{\sqrt{\beta S}}
\int_0^1\sqrt{\frac{q^2+2q+2}{q(q+2)}}\,dq.
\tag{14}
\]

Because \((3/5)q\le\phi(q)\le q\) on the interval,

\[
\boxed{\frac2{\sqrt{\beta S}}
\le T_{\rm on}\le2\sqrt{\frac5{3\beta S}}.}
\tag{15}
\]

For \(\beta=S=1\), a chosen exact-control preparation, this gives \(2\le T_{\rm on}<8/3\). The coefficient is not fitted to particle targets and has no physical action/time identification.

The auxiliary field remains necessary. Writing \(x(s)=\exp(A_e\theta(s))x(0)\), \(\theta'=\chi(q)\), and \(y(s)=a(s)x(s)\), one has \(a'=-U(q)\). Its total amplitude is finite for this isolated zero-dual preparation: before opening \(U\le\beta\), and afterward \(p\ge p_{\rm on}=\sqrt{3\beta S/5}\), while \(U(q)\le2\beta/(q+1)^2\). Therefore

\[
|a(\infty)|\le\beta T_{\rm on}+
\frac1{p_{\rm on}}\int_1^\infty\frac{2\beta}{(q+1)^2}dq
=\beta T_{\rm on}+\frac\beta{p_{\rm on}}.
\tag{16}
\]

This bounds an auxiliary record; it does not erase or reset it. The gate coasts after the on plateau, retaining nonzero momentum. Recharging the potential requires reversing the gate and returning work under a lawful interaction; no automatic cycle has been supplied.

## 5. What remains open

This construction removes the unbounded wake-potential defect in the isolated control, proves a positive finite funding receipt there, and supplies a strict sufficient opening margin for an isolated nonzero-dual preparation. It does not repair the sign-indefinite bilinear network Hamiltonian, select one contact exclusively, derive a native reservoir carrier, fix \(\beta\) or the profile, implement reset, or derive physical energy/action/time and quark/lepton correspondence.

Fresh exact controls check canonical gradients, Hamiltonian and depletion identities, original and auxiliary cuts, rational profile inequalities, the opening and adverse-burden receipts, and bounded potential inventory. Finite checks supplement the proofs; no archived scripts are executed. Next: address overlapping contacts with an explicitly positive interaction store, or prove the precise obstruction to keeping the current cotangent model while obtaining such a store. Independent review remains pending. Physical promotion 0.
