# THM-534: canonical gate backreaction and conditional readiness

Development — no registry entry. Exact conditional construction on an enlarged state space. Constructor checked; independent non-constructor review pending. Physical promotion 0. Native gate registers, their preparation, admission and reset remain OPEN.

## 1. What changes and what is derived

The preceding v1.9 audit excluded a naive state-weighted incidence Poisson tensor under its stated conditions. A constructive alternative is to keep the Poisson tensor constant and place gating in a Hamiltonian on an enlarged cotangent space. This derives the backreaction that accompanies a chosen gate model. It does not derive the new registers or their constitutive law from UD.

Retain the nine unique face/core coordinates \(x\) of \(K_-\), with signed contact generators \(A_e\). On the face/core pair of contact \(e=(f,\tau)\),

\[
A_e=\begin{pmatrix}0&-d_e\\d_e&0\end{pmatrix},\qquad d_e=D_{f\tau}=\pm1,
\]

embedded by zero elsewhere. Add a dual coordinate \(y\) conjugate to every component of \(x\), and a gate coordinate/momentum \((q_e,p_e)\) for each of the eight incidences. This is a 34-coordinate canonical model: \(9+9+8+8\). It is not the original 23-dimensional chain carrier or a particle-degree count. The original metric and frozen operators are retained as mathematical inputs; the new registers have no physical action-unit identification.

Let \(h_e=\chi_e(q_e)\), with \(\chi_e\) a supplied smooth monotone profile equal to zero on the off plateau and one on the on plateau. Set

\[
A(q)=\sum_e\chi_e(q_e)A_e,\qquad
\ell_e=y^{\mathsf T}A_ex=d_e(y_\tau x_f-y_fx_\tau).
\]

For a free-gate control model, choose

\[
\boxed{H(x,y,q,p)=\frac12\sum_ep_e^2+y^{\mathsf T}A(q)x.}
\tag{1}
\]

The canonical bracket pairs \(x_i\) with \(y_i\), and \(q_e\) with \(p_e\). It is constant, so its Jacobi identity is automatic, including where contacts overlap. Unit gate kinetic normalization and the profile coordinate scale are declared controls, not derived UD constants.

## 2. Forced backreaction and conserved quantities

**Theorem L1.** Hamilton's equations for (1) are

\[
\dot x=A(q)x,\quad \dot y=A(q)y,\quad
\dot q_e=p_e,\quad \boxed{\dot p_e=-\chi'_e(q_e)\ell_e.}
\tag{2}
\]

They conserve \(H\), \(\|x\|^2\) and \(\|y\|^2\).

**Proof.** The canonical derivatives are \(H_y=Ax\), \(H_x=A^{\mathsf T}y=-Ay\), \(H_{q_e}=\chi'_e\ell_e\), \(H_{p_e}=p_e\). They give (2). Antisymmetry gives \(x^{\mathsf T}Ax=y^{\mathsf T}Ay=0\). The remaining Hamiltonian derivative is

\[
\dot H=\sum_e\left(p_e\dot p_e+\chi'_e(q_e)\ell_e\dot q_e\right)=0.
\]

The \(x,y\) contributions cancel by the canonical equations. \(\square\)

The backreaction is necessary within this canonical realization. Requiring \(\dot x=A(q)x\) and integrating \(H_y=A(q)x\) forces \(H=y^{\mathsf T}A(q)x+K(x,q,p)\). Requiring the displayed cotangent equation for \(y\) removes \(K_x\); choosing \(\dot q=p\) gives the kinetic term plus a possible gate potential \(V(q)\). The general gate force then also contains \(-V'(q)\). Setting \(V=0\) is the present control, not a source theorem selecting a free gate.

If one changes \(q\) while omitting \(-\chi'\ell\), the Hamiltonian derivative contains \(p\chi'\ell\). An exact control below gives \(15/4\ne0\). A commanded switch with no gate response is therefore not the closed Hamiltonian system (1).

For the original support coordinates, instantaneous contact currents remain

\[
J_e=2d_e\chi_e(q_e)x_fx_\tau.
\]

They give \(d(x_f^2)/ds=-\sum_{e\ni f}J_e\) and \(d(x_\tau^2)/ds=\sum_{e\ni\tau}J_e\). Substitution into the frozen equal-share weights gives the same Q177–Q179 owned-support continuity. These are support receipts. Their interpretation is distinct from the mathematical Hamiltonian \(H\), and neither has been identified with physical energy.

## 3. Switching receipt and readiness margin

The gate kinetic receipt is

\[
\frac{d}{ds}\frac{p_e^2}{2}=-\ell_e\frac{d\chi_e}{ds},\qquad
\Delta\frac{p_e^2}{2}=-\int\ell_e\,d\chi_e.
\tag{3}
\]

For one isolated contact, \(\ell\) is conserved and (3) reduces to \(\Delta(p^2/2)=-\ell\Delta\chi\). In a network,

\[
\dot\ell_e=y^{\mathsf T}[A_e,A(q)]x.
\]

Overlapping contacts can therefore change \(\ell_e\). Using its initial value as a permanent network budget would be unjustified. Disjoint contact generators commute.

**Theorem L2.** Suppose an initially off gate has \(p_e(0)>0\), its profile is nondecreasing from 0 to 1 over \(0\le q\le1\), and conserved global bounds give \(\|x\|\le X\), \(\|y\|\le Y\). If

\[
\delta=\frac{p_e(0)^2}{2}-XY>0,
\tag{4}
\]

then this gate reaches the on plateau in finite model-parameter time, with

\[
p_e^2\ge2\delta,\qquad
T_{\mathrm{on}}\le\frac{1-q_e(0)}{\sqrt{2\delta}}.
\]

**Proof.** Each \(A_e\) has operator norm one, so \(|\ell_e|\le XY\). While \(p_e>0\), divide (3) by \(\dot q_e=p_e\) and integrate in \(q_e\). Monotonicity gives

\[
\frac{p_e(q)^2}{2}
\ge\frac{p_e(0)^2}{2}-XY\chi_e(q)\ge\delta.
\]

The positive margin prevents a first zero of \(p_e\), so the bound continues throughout the transition. Integrate \(\dot q_e\ge\sqrt{2\delta}\) to obtain the time bound. \(\square\)

The condition remains valid with preparation uncertainty if \(p_{\min}>0\), \(X_{\max},Y_{\max}\) are applicable upper bounds, the initial gate remains off, and \(p_{\min}^2/2-X_{\max}Y_{\max}>0\). For an exact illustrative control,

\[
p_{\min}=\frac{15}{8},\quad X_{\max}=Y_{\max}=\frac98,
\quad q_e(0)\in\left[-\frac38,-\frac18\right]
\]

give \(\delta=63/128\) and \(T_{\mathrm{on}}\le11/\sqrt{63}<11/7\). These are chosen model bounds, not physical calibration records or native thresholds.

This is a local certificate for an isolated pair. In the full network it uses global conserved norms and is **not** a bounded-locality native readiness law. A local replacement would need a justified control-volume ingress/reserve bound, with receipts for future inflow; the current local stock alone need not bound later \(\ell_e\).

For the displayed quintic isolated-contact control with \(\ell>0\), the exact kinetic barrier is \(\ell\): positive energy strictly below it has an interior turning point and reverses before \(\chi=1\), whereas a strict surplus crosses. Equality need not give finite-time arrival for a flat smooth on plateau. This distinction prevents treating a nonnegative reserve as a strict readiness margin.

## 4. Off gates do not bootstrap and switching work is not yet physical

**Theorem L3.** In the free-gate model, an off-plateau gate initially at rest stays off, even while other contacts evolve.

**Proof.** On that plateau \(\chi=\chi'=0\). Thus \(p=0\) gives \(\dot q=\dot p=0\), irrespective of changing \(x,y\). Local uniqueness preserves this gate state. If every gate is off and at rest, \(A=0\) and the full state is stationary. \(\square\)

The model therefore requires a charged/prepared gate, an independent gate potential/source, or another wake interaction. It does not derive reopening merely from a positive core-stock receipt. The distinction is substantive: autonomous equations can implement a prepared switch without selecting or preparing it natively.

The bilinear \(\ell_e\) is sign-indefinite. In particular \(y=0\) gives zero reaction work while \(x\ne0\) may still rotate under a separately prepared moving gate. Changing the dual preparation changes the gate receipt without changing the original support stock. The Hamiltonian is not bounded below over unrestricted dual preparations. Thus (3) is not a positive physical switching-cost theorem, a native action quantum, or an identification of support norm with energy. The dual registers and their units remain a source obligation.

An opened free gate can coast on its plateau. This construction supplies neither a reusable latch/reset cycle nor a finite-capacity memory ledger. Gate preparation, return, record retention and renewal require additional dynamics and accounting.

## 5. A finite canonical contact primitive with mandatory momentum kick

A finite conditional contact can preserve the enlarged symplectic form exactly while retaining the earlier carrier Cayley update. For fixed \(q\), set

\[
R(q)=\operatorname{Cayley}(\varepsilon\chi(q)A_e),\qquad
\theta(q)=2\arctan\frac{\varepsilon\chi(q)}2.
\]

The local six-coordinate map is

\[
x'=R(q)x,\quad y'=R(q)y,\quad q'=q,\qquad
\boxed{p'=p-\theta'(q)\ell_e},
\quad\theta'=\frac{\varepsilon\chi'}{1+(\varepsilon\chi/2)^2}.
\tag{5}
\]

Only the two incident coordinates in each of \(x,y\) and that gate pair are changed.

**Theorem L4.** Equation (5) is canonical and preserves both support norms and \(\ell_e\).

**Proof.** Orthogonality of \(R\), and its commutation with \(A_e\), preserve the norms and \(\ell_e=y^{\mathsf T}A_ex\). Moreover \(R^{\mathsf T}R'=\theta'A_e\), so the canonical one-form transforms as

\[
(y')^{\mathsf T}dx'+p'\,dq'
=y^{\mathsf T}dx+\theta'\ell_e\,dq+(p-\theta'\ell_e)\,dq
=y^{\mathsf T}dx+p\,dq.
\]

Taking exterior derivatives proves symplectic preservation. Omitting the momentum kick leaves an uncancelled term and generally fails this test. \(\square\)

This map is a contact substep, not the exact finite flow or energy-preserving integrator of the full Hamiltonian (1). It can be interpreted as the unit-parameter flow of \(\theta(q)\ell_e\). Gate free flight and overlapping contacts need separate treatment for a full integrator; no unreported splitting or total-energy certificate is claimed here. Its carrier midpoint receipts use the frozen \(\chi(q)\), just as in the earlier contact primitive.

For exact controls, use the supplied \(C^2\) plateau profile

\[
\chi(q)=\begin{cases}
0,&q\le0,\\
10q^3-15q^4+6q^5,&0<q<1,\\
1,&q\ge1.
\end{cases}
\]

Then \(0\le\chi'\le15/8\). The shape is chosen for smoothness, not derived from UD. Other smooth monotone profiles give different timing with the same structural receipts and margin theorem.

At \(q=1/2\), \(d=1\), \(\varepsilon=1/4\), \(x=(1,0)\), \(y=(0,1)\), \(p=2\), equation (5) gives

\[
x'=\frac1{257}(255,32),\quad
y'=\frac1{257}(-32,255),\quad p'=\frac{394}{257}.
\]

The omitted-reaction continuous control has \(\dot H=15/4\). The finite contact substep instead is exactly canonical, but changes the full \(H\) by \(-54480/66049\). This explicit defect is retained to prevent confusing symplecticity of a substep with energy preservation of the complete evolution.

## 6. Verification and source disposition

Fresh standard-library Fraction controls check 64 continuous Hamiltonian/norm/owned-support cases, all 256 plateau masks, 768 signed extended-state symmetry cases, 512 angular-commutator identities, 112 exact finite-map symplectic Jacobians, and 357 readiness-margin controls. Exact forward differentiation is used for the six-coordinate Jacobian; no floating tolerance is used. All 439 nonzero angular-rate controls are retained as evidence that an isolated-contact constant-\(\ell\) budget cannot be assumed in a network. The proofs, not the finite controls alone, establish the general statements. No archived code is executed.

The enlarged model avoids v1.9's Jacobi obstruction because it uses a constant canonical bracket with new conjugate registers; it does not refute the theorem for the original pair-local weighted bracket. The support-flow generator remains unit-strength on admitted plateaus. Transitions and their auxiliary preparation are explicit additions, not native source closure.

The next native-source obligation is sharply localized: identify a lawful gate/dual carrier and its preparation; derive a wake and reset interaction with receipts; and replace global readiness bounds by sourced local control-volume reserve/ingress bounds if bounded locality is required. Exclusive contact selection, physical time/action, positive physical energy and quark/lepton identification remain OPEN. Physical promotion 0.
