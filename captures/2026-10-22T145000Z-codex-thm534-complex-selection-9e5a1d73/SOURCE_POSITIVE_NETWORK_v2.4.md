# THM-534: positive network completion and its support tradeoff

Development — no registry entry. Exact conditional mathematics; new candidate dynamics, constructor checked, independent review pending. Physical promotion 0.

## 1. What can and cannot be retained

The v2.3 candidate gives bounded positive potential but retains the sign-indefinite term \(y^{\mathsf T}A(q)x\). Here \(A(q)=\sum_e\chi_e(q_e)A_e\), where \(A_e\) is the signed face/core skew generator. Original incidence operators and metric remain fixed mathematical inputs. The canonical auxiliary fields and gate pairs are supplied candidate structure.

**Theorem N1 (canonical lower-bound obstruction).** Fix the canonical pairs \((x,y)\) and suppose a differentiable Hamiltonian retains \(\dot x=A(q)x\) at every state with unrestricted \(y\in\mathbb R^n\). Then

\[
H=y^{\mathsf T}A(q)x+F(x,q,p).
\tag{1}
\]

At every fixed \((x,q,p)\) for which \(A(q)x\ne0\), this Hamiltonian is unbounded below over \(y\).

**Proof.** The equation \(H_y=A(q)x\) integrates to (1). Set \(y=-tA(q)x\); then \(H=-t\|A(q)x\|^2+F\to-\infty\) as \(t\to\infty\). \(\square\)

Adding only a support/gate potential cannot repair this lower bound. The theorem assumes the same canonical bracket, exact displayed \(x\)-flow, and an unrestricted dual. It does not exclude constrained dual spaces, another bracket, or another native carrier. It is a structural reason to stop calling the existing cotangent Hamiltonian a positive native resource account.

## 2. Minimal local isotropic completion

For contact \(e=(f,\tau)\), define combined pair stock and angular coupling

\[
S_e=x_f^2+x_\tau^2+y_f^2+y_\tau^2,
\qquad \ell_e=d_e(y_\tau x_f-y_fx_\tau).
\]

Within the declared family of isotropic contact completions, set

\[
Q_{e,a}=\ell_e+\frac a2S_e.
\]

**Theorem N2.** \(Q_{e,a}\ge0\) for all pair states if and only if \(a\ge1\). At the minimum \(a=1\),

\[
\boxed{Q_e=\ell_e+\frac12S_e
=\frac12\big[(x_f+d_ey_\tau)^2+(x_\tau-d_ey_f)^2\big]\ge0.}
\tag{2}
\]

**Proof.** Cauchy–Schwarz gives \(|\ell_e|\le S_e/2\), proving sufficiency. The state \(x_f=1,y_\tau=-d_e,x_\tau=y_f=0\) gives \(S_e=2,\ell_e=-1\), hence \(Q_{e,a}=a-1<0\) if \(a<1\). Expansion proves (2). \(\square\)

The coefficient one is forced by positivity plus *minimality within this specified completion family*. Selecting that family and minimality remains a new modeling choice; it is not a native source derivation or a unique completion theorem over all Hamiltonians. No fitted particle number enters the calculation.

## 3. Positive Hamiltonian on the overlapping carrier

Use the v2.3 supplied profile \(U_e(q)=2\beta_e/[1+(q+1)^2]\), \(\beta_e>0\), and the monotone quintic plateau \(\chi_e\in[0,1]\). Define

\[
\boxed{H_+=K+V+R,
\quad K=\frac12\sum_ep_e^2,
\quad V=\sum_e\chi_e Q_e,
\quad R=\frac12\sum_eU_eS_e.}
\tag{3}
\]

Each term is nonnegative. Let \(P_e\) project onto the two contact coordinates, and set

\[
\Omega(q)=\sum_e(\chi_e+U_e)P_e,
\quad f_e=-\frac12U'_eS_e.
\]

The canonical equations are

\[
\boxed{\begin{aligned}
\dot x&=Ax+\Omega y,&\dot y&=Ay-\Omega x,\\
\dot q_e&=p_e,&\dot p_e&=f_e-\chi'_eQ_e.
\end{aligned}}\tag{4}
\]

These differ from v2.3, and N1 does not apply because the original \(x\)-flow is no longer retained. The original metric and frozen operators are not overwritten: this is a separate enlarged candidate with changed equations and observable accounting.

**Theorem N3 (network stock and kinetic bound).** On any finite contact carrier, including overlapping contacts, (4) conserves \(H_+\) and

\[
N=\|x\|^2+\|y\|^2.
\]

Every finite initial state satisfies the all-time bound

\[
\boxed{0\le K(s),\ V(s),\ R(s)\le H_+(0),
\qquad \sum_ep_e(s)^2\le2H_+(0).}\tag{5}
\]

**Proof.** Hamiltonian conservation follows from the constant canonical bracket. Skewness of \(A\) and symmetry of \(\Omega\) give

\[
\dot N=2x^{\mathsf T}Ax+2y^{\mathsf T}Ay
+2x^{\mathsf T}\Omega y-2y^{\mathsf T}\Omega x=0.
\]

Equation (2), \(\chi_e\ge0\), and \(U_e>0\) prove nonnegativity of every store in (3); conservation then gives (5). With bounded fields from \(N\), bounded momenta from (5), and smooth bounded profiles and derivatives, finite-time escape is excluded. The local solution extends for every finite model-time interval. \(\square\)

These are bounds on simultaneous stored quantities. Repeated reversible exchanges may accumulate arbitrarily large gross transferred work; (5) is not a bound on \(\int[\dot K]_+ds\), nor a theorem of irreversible work cost, finite memory or physical energy. Initial \(H_+\) is a declared preparation, not a native charging rule.

## 4. Local receipts reveal the changed observable

Since \(\Omega\) is diagonal, at each coordinate \(i\),

\[
\frac{d}{ds}x_i^2=2x_i(Ax)_i+2\Omega_i x_iy_i,
\quad
\frac{d}{ds}y_i^2=2y_i(Ay)_i-2\Omega_i x_iy_i.
\tag{6}
\]

The exchange terms cancel in \(n_i=x_i^2+y_i^2\). Consequently the combined contact current is

\[
J_e^{\rm joint}=2d_e\chi_e(x_fx_\tau+y_fy_\tau),
\tag{7}
\]

and for every fixed control volume \(T\),

\[
\frac{d}{ds}\sum_{i\in T}n_i
=\sum_{e\in\partial T}\sigma_T(e)J_e^{\rm joint}.
\tag{8}
\]

The original \(x\)-only support instead acquires a source in (6). In particular, starting with \(y=0\) generally creates \(y\), and the old \(x\)-only norm does not remain constant thereafter. Original Q170/Q177–Q179 receipts cannot be advertised unchanged as receipts of this new observable. Equal-share ownership can be *applied algebraically* to \(n_i\), but identifying the added dual with native support remains a separate source obligation.

The exact gate and potential receipts are

\[
\dot K_e=f_ep_e-Q_e\dot\chi_e,
\qquad
\dot R_e=-f_ep_e+\frac{U_e}{2}\dot S_e,
\tag{9}
\]

and

\[
\dot V=\sum_e\left(Q_e\dot\chi_e-\frac{U_e}{2}\dot S_e\right).
\tag{10}
\]

For (10), the term \(\sum_e\chi_e\dot Q_e\) is the Poisson interaction between the quadratic contact Hamiltonian \(V\) and the diagonal potential \(R\); it equals \(-\sum_e(U_e/2)\dot S_e\), while the self-bracket of \(V\) vanishes. Alternatively, differentiate (3), use (9) and \(\dot H_+=0\). Transport can increase a particular \(R_e\), but it cannot hide a negative unbounded store: (5) accounts for all stores, including overlaps.

Overlapping \(R_e\) are distinct terms of the candidate interaction potential, not independently claimed copies of native stock. The source derivation and allocation of their initial charge have not been supplied.

## 5. Isolated completion now pays a positive admission cost

For one isolated contact, \(\Omega=(\chi+U)I\) on its pair, and both \(S\) and \(\ell\) are constant. This follows by skewness; the new \(\Omega\) terms contribute \(-\Omega x^{\mathsf T}A_ex+\Omega y^{\mathsf T}A_ey=0\) to \(\dot\ell\). Thus \(Q=\ell+S/2\ge0\) is constant. At \(q(0)=p(0)=0\), set

\[
B=\frac{\beta S}{2},\qquad
\phi(q)=\frac{q(q+2)}{q^2+2q+2}.
\]

The conserved positive funding equation becomes

\[
\boxed{K+\chi(q)Q+R=B,
\qquad \frac{p^2}{2}=B\phi(q)-Q\chi(q).}\tag{11}
\]

At rest, \(\ddot q(0)=B>0\) if \(S>0\). With the same quintic profile, the v2.3 inequality \(\chi(q)\le(25/8)\phi(q)\) gives the sufficient condition

\[
\delta=B-\frac{25}{8}Q>0
\quad\Longrightarrow\quad
T_{\rm on}\le2\sqrt{\frac5{6\delta}}.
\tag{12}
\]

**Proof.** The first integral gives \(p^2/2\ge\delta\phi(q)\ge(3/5)\delta q\) on \([0,1]\). Positive initial acceleration initiates motion; the strict margin excludes an interior zero of \(p\). Integrating \(dq/p\) gives (12), including the integrable square-root singularity at rest. \(\square\)

At arrival,

\[
K_{\rm on}=\frac35B-Q.\tag{13}
\]

For initial \(y=0\), \(Q=S/2\). Thus \(\beta>5/3\) is necessary for a strictly positive arrival speed, while \(\beta>25/8\) is a sufficient finite-opening condition from (12). These are not equivalent thresholds; interior barriers may matter. The old v2.3 zero-dual opening result for \(\beta=1\) does not transfer: here (13) would be negative. This countercontrol records the new admission cost rather than suppressing it.

For a chosen exact preparation \(\beta=4,S=1,y=0\),

\[
B=2,\quad Q=\frac12,\quad\delta=\frac7{16},\quad
R_{\rm on}=\frac45,\quad V_{\rm on}=\frac12,
\quad K_{\rm on}=\frac7{10}.
\]

The stores sum to 2, and \(T_{\rm on}\le2\sqrt{40/21}\). The coefficient \(\beta=4\) is an illustrative declared charge, not a derived UD constant. Gate coasting, auxiliary record retention and automatic reset remain unresolved. The isolated proof is not an opening theorem for competing overlapping contacts.

## 6. Result and source boundary

This supplies a positive finite stored-quantity account for the enlarged network, including overlaps, at the explicit cost of changing original support dynamics. Minimal local isotropic completion removes the sign-indefinite term as a hidden resource. The combined norm and its local cut receipts close exactly; their identification with native support does not.

The source ledger establishes original chain geometry and support cuts, not the added canonical dual, its conversion into a second support field, the positivity/minimality principle, the potential profile, charge scale or native admission/reset rule. Q153/Q156/G05 remain open. No physical energy/time/action or quark/lepton correspondence is inferred. Fresh exact controls accompany the general proofs; constructor verification is not independent review. Physical promotion 0.
