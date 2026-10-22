# THM-534: local ingress reserve and conditional gate readiness

Development — no registry entry. Exact conditional mathematics in the supplied v2.0 canonical extension. Constructor checked; independent review pending. Physical promotion 0.

## 1. Model and source boundary

Retain the signed face/core carrier and the candidate cotangent gate equations of v2.0:

\[
\dot x=A(q)x,\quad \dot y=A(q)y,\quad \dot q_e=p_e,
\quad \dot p_e=-\chi'_e(q_e)\ell_e,
\quad \ell_e=d_e(y_\tau x_f-y_fx_\tau).
\tag{1}
\]

Here \(A(q)=\sum_e\chi_e(q_e)A_e\), each contact generator is skew with pair matrix \(\left(\begin{smallmatrix}0&-d_e\\d_e&0\end{smallmatrix}\right)\). Profiles are locally Lipschitz with locally Lipschitz derivative, nondecreasing, zero for \(q\le0\), one for \(q\ge1\). The coordinate parameter \(s\) is model time without physical-unit identification. The dual \(y\), gate pair, free kinetic normalization and profile remain supplied candidate structure. No original particle operator or metric is changed.

Q170/Q171/Q172 supply the original support cut receipts; the analogous \(y\) receipts below follow from the added candidate equation. A future ingress budget for either field is an explicit additional assumption. Neither Q153 nor Q156 supplies that budget or an autonomous wake law.

## 2. Exact local cut accounting

Fix a control volume \(R\) containing both endpoints of a target contact \(e\). For \(z=x,y\), let

\[
S_z=\sum_{i\in R}z_i^2,\qquad
J_a^z=2d_a\chi_a z_{f_a}z_{\tau_a}.
\]

A boundary contact has exactly one endpoint in \(R\); set \(\sigma_R(a)=+1\) when its core is inside and \(-1\) when its face is inside. Define

\[
I_z=\sum_{a\in\partial R}[\sigma_R(a)J_a^z]_+,
\qquad O_z=\sum_{a\in\partial R}[-\sigma_R(a)J_a^z]_+.
\]

Then internal currents cancel exactly and

\[
\dot S_z=I_z-O_z. \tag{2}
\]

Assume a declared nonnegative credit \(b_z^0\) bounds cumulative *positive* ingress through the horizon of interest:

\[
\int_0^s I_z(u)\,du\le b_z^0.
\tag{3}
\]

This counts repeated entry, even if the same stock later exits. Define diagnostic remaining credit and stock envelope

\[
b_z(s)=b_z^0-\int_0^s I_z(u)du\ge0,
\quad U_z=S_z+b_z,
\quad \dot U_z=-O_z\le0.
\tag{4}
\]

These are accounting observers, not newly added Hamiltonian forces. A signed net-flow receipt cannot replace (3). A monitor that detects negative credit has detected failure of the hypothesis; it has not enforced a boundary capacity.

Since the target endpoints lie in \(R\), Cauchy–Schwarz and arithmetic–geometric mean give

\[
|\ell_e|\le\sqrt{S_xS_y}\le\sqrt{U_xU_y}
\le C(s):=\frac{U_x+U_y}{2},\qquad
\dot C=-\frac{O_x+O_y}{2}\le0.
\tag{5}
\]

The arithmetic bound is deliberately conservative and uses only rational operations for rational receipt data. It introduces no fitted coefficient. It does not make the assumed ingress credits parameter-free native quantities.

## 3. A nondecreasing local readiness reserve

**Theorem R1.** Let the target start with \(q_0\le0\), \(p_0>0\), and let

\[
K=\frac{p_e^2}{2},\qquad
\mathcal R=K-C(1-\chi_e(q_e)),\qquad
r_0=\mathcal R(0)=\frac{p_0^2}{2}-C(0)>0.
\tag{6}
\]

If (3) holds throughout the declared horizon

\[
T_*:=\frac{1-q_0}{\sqrt{2r_0}}, \tag{7}
\]

then the gate reaches \(q_e=1\) by \(T_*\). Until arrival, \(p_e\ge\sqrt{2r_0}\) and \(\mathcal R(s)\ge r_0\).

**Proof.** On any interval before arrival with \(p_e>0\), write \(\dot\chi_e=\chi'_e p_e\ge0\). Equation (1) gives \(\dot K=-\ell_e\dot\chi_e\), hence

\[
\boxed{\dot{\mathcal R}
=(C-\ell_e)\dot\chi_e
+\frac{O_x+O_y}{2}(1-\chi_e)\ge0.}
\tag{8}
\]

Both terms are nonnegative by (5) and \(0\le\chi_e\le1\). Thus \(K=\mathcal R+C(1-\chi_e)\ge r_0\), which excludes a first zero of \(p_e\). This continuation argument extends the bounds to arrival or the full horizon. If arrival has not yet occurred, integration of \(\dot q_e\ge\sqrt{2r_0}\) gives \(q_e(T_*)\ge1\), a contradiction. The vector field has finite-horizon continuation: \(x,y\) have conserved global norms, bounded \(\chi'\) bounds gate acceleration, and finitely many gate coordinates cannot escape in finite time. These global existence facts are not used as the value of the local readiness bound. \(\square\)

For a finite declared horizon \(T\), it suffices to certify (3) independently on \([0,T]\), choose \(r_0>0\), and check

\[
2r_0T^2\ge(1-q_0)^2. \tag{9}
\]

One cannot justify (3) by assuming the opening which it is being used to prove. The theorem is profile-independent within its stated monotone class, and does not assume network \(\ell_e\) is constant. A strictly positive lower margin remains valid under perturbations that preserve the ingress contract and keep the worst-case initial reserve positive. This is conditional robustness, not robustness to arbitrary boundary influx or arbitrary changes in the candidate dynamics.

For a chosen exact control, let \(S_x(0)=S_y(0)=1/4\), \(b_x^0=b_y^0=1/4\), \(p_0=3/2\), \(q_0=0\). Then \(C(0)=1/2\), \(r_0=5/8\), and

\[
T_*\le 2/\sqrt5<1.
\]

These are illustrative model preparations, not measured UD constants. A rational horizon \(T=1\) passes (9). A feasible example can place amplitude \(1/2\) on the target face in both fields and take all boundary contacts closed; positive ingress is then zero. Nonzero bounded ingress is covered by the proof, not inferred from that special example.

## 4. Current local stock cannot certify arbitrary future influx

**Counterexample R2.** On \(K_-\), take target face \(013\) and core \(\tau_0\), with \(R=\{013,\tau_0\}\). The other face \(123\) meets the same core with incidence sign \(+1\). Hold the target gate closed and admit only that boundary contact. Start with

\[
x_{013}=1,\quad x_{\tau_0}=1,\quad x_{123}=M.
\]

All coordinates in \(R\) agree for every \(M\), and \(S_x(R,0)=2\). A single boundary Cayley step with declared numerical step \(\varepsilon=1/4\) gives

\[
x'_{\tau_0}=\frac{16M+63}{65},\quad
x'_{123}=\frac{63M-16}{65},\quad
S'_x(R)=1+\left(\frac{16M+63}{65}\right)^2.
\tag{10}
\]

The last quantity is unbounded as \(|M|\to\infty\), while total pair norm is conserved exactly. This is an algebraic boundary-transfer control, not a claim that the contact substep solves the full Hamiltonian. The continuous control with that boundary gate fixed on gives \(x_{\tau_0}(s)=M\sin s+\cos s\), also unbounded over \(M\) at any fixed \(0<s<\pi\). Thus no finite upper envelope based solely on initial coordinates in this \(R\) can cover arbitrary exterior preparations and admitted influx. Setting \(y\) only on the target face makes \(|\ell_e|=|x_{\tau_0}|\), so the problem also affects the required switching bound.

This does not exclude larger bounded neighborhoods with independently constrained boundary data, closed control volumes, physical finite-capacity laws or time-dependent local certificates. It excludes treating the current two-endpoint stock as a universal future network bound.

## 5. Certification does not supply wake, credits or reset

**Theorem R3.** A target gate initially at rest on the off plateau remains at rest there, regardless of boundary influx into \(R\).

**Proof.** At that gate \(\chi_e=\chi'_e=0\). Hence \(\dot q_e=p_e=0\) and \(\dot p_e=-\chi'_e\ell_e=0\), for all evolving values of \(x,y\). Local uniqueness preserves the stationary gate pair. \(\square\)

A positive support receipt or a positive unused ingress credit therefore cannot wake this model. The reserve criterion certifies an already prepared positive momentum; it is not a native admission mechanism. Incoming support is not gate kinetic preparation, and the dual budget is not an original native support register. Using these diagnostic observers actively to alter a canonical flow would require a separately derived interaction and its backreaction.

## 6. Review and next source obligations

The fresh verifier checks every one of 512 control volumes against all 256 admission masks, for each of two exact integer fields; reserve identities and signs at rational preparations; strict-margin horizon controls; exact unbounded-influx controls; and resting-off-gate force controls. Finite checks supplement the proofs and are not independent peer review or empirical confirmation. Source snapshots are read as data; their archived scripts are not executed.

The mathematical gap narrowed here is the replacement of a global readiness value by a local cut receipt plus an explicit future-ingress contract. The unresolved source obligations are: (i) identify native dual/gate registers and their units, (ii) derive and enforce local ingress capacity without assuming the desired admission outcome, (iii) derive a wake interaction and its conserved receipts, and (iv) derive reset/reuse. Exclusive selection, physical action/time/energy and quark/lepton correspondence remain OPEN. No physical promotion is made.
