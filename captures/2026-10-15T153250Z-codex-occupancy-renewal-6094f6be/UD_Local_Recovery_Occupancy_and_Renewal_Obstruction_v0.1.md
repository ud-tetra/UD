# UD local recovery, positive occupancy and renewal obstruction v0.1

15 October 2026 UTC. Separate manuscript development addendum. Constructor checked; independent review pending. Physical promotion 0.

**Result.** A recovery port supported on one vertex and its twelve incident edges can preserve the full protected sector only when its edge contacts form a balanced signed star. Unequal local gate masks violate this condition. Separately, the reciprocal signed-burden model cannot itself be a nonnegative occupancy law for all admitted signed carrier states. A declared positive/negative register lift reproduces the signed equation, but reveals an additional occupancy state and source/sink traffic absent from the signed storage receipt. Thus neither the capacity trigger nor complete renewal cost follows from the previous passive model.

## 1. Source boundary

The attached coefficient ledger v0.39(2) distinguishes C03 (7/768, structural ratio; local admissibility law open), Q153/Q158 (continuity/residual receipts; predictive source law open), Q156 (hard gate h=C_cl T_int), Q162 (conditional relaxational gradient flux), and Q178 (micro support stock; renewal terms open). These are exact source locators, not inferred physical laws. The attached CRL-2 proposal explicitly separates constructor checks from independent review.

The preceding development source is `UD_Protected_Retention_Robustness_and_Port_Condition_v0.1.md`, PR114, commit `a575840cd2e4df93874f0bcac7b621390f83b77f`. It supplies the finite 600-cell input and conditional signed recovery model. Its referenced September normalization repair distinguishes normalization N from rate gamma. The recovered winding-source nonidentifiability theorem fixes a direction only on its declared K4 event; it supplies no 600-cell amplitude or drain law.

The attached coherence, master-action, packet-field and carrier-definition Markdown files contain only placeholder statements. They cannot select this cross-port or trigger. No archived code was executed. `Gap2_FINAL_Finite_Genesis.png` remains unavailable and was not used. The current repository base is `4d87860ab3876458a221c04c8e566d6c610df568`; its latest residual-Gauss capture belongs to a separate candidate gauge-action lane and is not imported as a burden law.

## 2. Locality selects a balanced star, but leaves two amplitudes

Use the restored real skew chain generator A, boundary B1, and

\[
P_{\rm cyc}=I-B_1^T(B_1B_1^T)^+B_1,
\qquad P=\operatorname{diag}(0,P_{\rm cyc},I,I).
\]

For reciprocal recovery c'=Ac+Fz, z'=-F^Tc-Rz, universal protection is PF=0. This statement concerns the supplied unit-metric carrier and the full protected space, not an arbitrary changed metric or a smaller code.

Consider one burden coordinate at vertex u. Its carrier output is confined to vertex u and its edge star. Let g_i be the twelve outward oriented unit edge vectors and T the matrix with columns g_i. Write the edge output as T a.

**Local port theorem.** P_cyc T a=0 if and only if a is constant.

Proof: a gradient has zero circulation around every triangle. For a triangle (u,v,w), the edge (v,w) is outside the allowed star, so its amplitude is zero. Zero circulation therefore requires equal outward amplitudes on (u,v) and (u,w). The vertex link is a connected icosahedral graph; these equalities force all twelve a_i equal. Conversely T1=-B1^T e_u is a gradient and is annihilated by P_cyc. The replay independently verifies rank(B2^T T)=11 and its constant kernel on the declared finite complex.

Consequently the most general port column with this strict support is

\[
\boxed{F_u=\beta_u I_0 e_u+\alpha_u I_1 B_1^T e_u.}
\]

Both coefficients remain free. Protection and strict locality determine a two-dimensional family; they do not select alpha, beta, units, signs or rates. Vertex-only coupling is the alpha=0 member. A proper subset of the twelve edge contacts cannot carry a nonzero safe star output. This is a support theorem, not an actuator construction.

For a proposed edge mask h, the output alpha diag(h) B1^T e_u is safe only when alpha=0 or all twelve h_i are equal. An all-on/all-off star preserves the range condition, including state-dependent scalar switching while the equations are well-defined. Independent edge gating generally does not. The source rule h_e=C_cl,e T_int,e does not enforce star-wise equality by itself. Either its admitted recovery states must prove that equality or the implementation needs a different, explicitly sourced port. This conclusion does not prohibit the separate cut writer from temporarily leaving the safe class.

### Exact size of a local imbalance

Let a_perp=a-(1/12)(1^T a)1. The leakage Gram matrix G=T^T P_cyc T has spectrum

\[
0^{(1)},\quad (2899/3150)^{(5)},\quad
\left(6823/7560\pm899\sqrt5/75600\right)^{(3)}.
\]

The replay reconstructs G from the incidence matrices and an exactly certified rational vertex pseudoinverse. Its integer multiple K=151200 G satisfies

\[
K(K-139152I)\big[(K-136460I)^2-5(1798)^2I\big]=0.
\]

Exact ranks and trace fix the displayed multiplicities. The smallest nonzero eigenvalue exceeds 7/8 and the largest is less than one. Hence

\[
\boxed{\frac78\|a_\perp\|^2
\le\|P_{\rm cyc}T a\|^2\le\|a_\perp\|^2.}
\]

Common gain changes are safe; unequal gains feed the protected sector at almost their full squared imbalance. This provides an exact geometric error observable for a future contact-balancing specification. It does not identify a physical calibration tolerance.

## 3. A signed coordinate cannot automatically be positive occupancy

The passive normalized model is

\[
c'=Ac+Fz,\qquad z'=-F^Tc-Rz,
\qquad H=\tfrac12(\|c\|^2+\|z\|^2),
\qquad H'=-z^TRz.
\]

**Positivity obstruction.** If the admitted carrier states include both signs of every direction, a nonzero reciprocal F cannot preserve z>=0 for every such state starting at z=0. Choose a nonzero column f_i of F and c=f_i (or its norm-bounded positive rescaling). Then z_i'=-||f_i||^2<0 at that boundary. This immediately leaves the nonnegative orthant. No drain R repairs the blank-state derivative, because Rz=0 there.

With constant invertible normalization z=N b, the same argument applies to any nonzero row of N^{-1}F^T at b=0. Changing units does not turn a signed linear transfer into a globally positive occupancy law.

This does not invalidate a signed response/deviation coordinate. A positive background, a restricted state domain, a nonlinear reaction rule or two positive registers are possible additional models; each needs its own stock, source and capacity receipts. The obstruction concerns identifying the existing coordinate with occupancy without supplying those premises.

## 4. A declared positive-register lift and its minimum traffic

For an explicit candidate completion, set z=p-n with p,n>=0 and restrict the drain to

\[
R=\kappa L+rI,\qquad\kappa\ge0,\quad r\ge0,
\]

where L is an unweighted graph Laplacian. Then -R has nonnegative off-diagonal entries. For q=-F^T c, define q_+=max(q,0) and q_-=max(-q,0) componentwise, and declare

\[
p'=-Rp+q_+,\qquad n'=-Rn+q_-.
\]

The nonnegative orthant is invariant: at a zero register coordinate all incoming off-diagonal and source terms are nonnegative. Subtraction gives z'=-Rz+q exactly, so the projected signed carrier/burden dynamics are unchanged. This is a newly declared candidate law, not a recovered UD primitive or microscopic reaction construction.

Any nonnegative source pair s_+,s_- realizing the same difference q has

\[
s_++s_-\ge |q|
\]

componentwise. The rectified lift attains equality, and therefore minimizes instantaneous gross source injection **within the class with the same two-register drain and nonnegative source terms**. It is not a universal cost optimum over all possible encodings, annihilation reactions or reservoirs.

The missing state is m=p+n:

\[
\boxed{m'=-Rm+|q|,\qquad m\ge |z|.}
\]

For aggregate occupancy M=1^T m and a closed graph,

\[
\boxed{M'=-rM+\|q\|_1.}
\]

Thus pure gradient mixing (r=0) cannot remove this aggregate stock. With blank registers, the total gross source W(T)=integral_0^T ||q||_1 ds and sink D(T)=r integral_0^T M ds obey W(T)=M(T)+D(T). Restoration of a low-occupancy readiness condition requires a genuine sink or another explicitly modelled removal process; diffusion alone does not suffice.

Even a quadratic register-stock convention exposes the hidden common mode. If H_lift=(||c||^2+||p||^2+||n||^2)/2, then

\[
\boxed{H_{\rm lift}-H=p^T n
=\tfrac14(\|m\|^2-\|z\|^2)\ge0.}
\]

It is absent from the signed storage law. Neither quadratic convention has yet been identified with joules or thermodynamic entropy.

## 5. An exactly soluble counterexample to a complete-cost inference

Consider the invariant normalized uniform vertex/burden mode of F=gamma I0 with R=kappa L+rI. The constant vertex vector is killed by A, and L kills the constant burden vector. Its modal equations are

\[
c'=\gamma z,\qquad z'=-\gamma c-rz,
\qquad(c(0),z(0))=(1,0).
\]

The same equations also define a standalone scalar benchmark. For a graph with V vertices, the normalized constant basis vector is 1/sqrt(V); aggregate register occupancy and source traffic are sqrt(V) times the modal quantities below. These dimensionless normalizations must not be silently interchanged.

At r=0, c=cos(gamma s), z=-sin(gamma s). After every full period, c,z and H return to their initial values. Yet the rectified lift accumulates four units of modal occupancy per period. After one period p=n=2, so M=4 and H_lift-H=4. After N periods M=4N. The signed state therefore fails to determine occupancy even along one trajectory initialized with blank positive registers. Infinite recurring operation needs unbounded stock or an added renewal law.

For 0<r<2gamma, put a=r/2, omega=sqrt(gamma^2-a^2), delta=arctan(a/omega). The exact signed solution is

\[
c(s)=e^{-as}\left(\cos\omega s+\frac a\omega\sin\omega s\right),
\qquad z(s)=-\frac\gamma\omega e^{-as}\sin\omega s.
\]

It decays to zero, and the signed exported quadratic storage is exactly r integral z^2 ds=1/2. But the total minimum rectified modal source traffic is

\[
\boxed{W_\infty=\int_0^\infty\gamma|c(s)|ds
=\frac r\gamma+
\frac{2\exp[-a(\pi/2+\delta)/\omega]}
{1-\exp[-a\pi/\omega]}.}
\]

Derivation: c changes sign at t_k=(pi/2+delta+k pi)/omega. An antiderivative is

\[
\frac{e^{-as}}{\gamma^2}
\left[-2a\cos\omega s+
\frac{\omega^2-a^2}{\omega}\sin\omega s\right].
\]

Its values at the sign changes alternate as (-1)^k exp(-a t_k)/gamma. Sum the first positive interval and the geometric series of subsequent absolute integrals. This yields the displayed expression. In this stable scalar lift M tends to zero, so total sink traffic equals W_infinity as well.

As r/gamma tends to zero from above,

\[
\boxed{W_\infty\sim\frac{4\gamma}{\pi r},}
\]

while signed storage export remains 1/2. Consequently that export receipt supplies no uniform bound on total occupancy source/renewal traffic across this admitted family.

| gamma/r | Minimum gross modal source traffic | Signed storage export |
|---:|---:|---:|
| 2 | 2.7477593 | 1/2 |
| 10 | 12.7716014 | 1/2 |
| 100 | 127.3278709 | 1/2 |

These decimals are numerical evaluations of the analytic formula, not empirical costs. Traffic, stock, energy and entropy remain distinct typed quantities. A per-source and per-sink physical cost law would be needed to convert traffic into energy. The rectifiers, supplied sources and sinks have no derived physical apparatus here.

## 6. What this resolves about a native trigger and restoration

An occupancy guard would have to act on a declared m or positive stock rho, rather than on signed z without further justification. It also needs a sourced normalization, capacity and switching law. Many threshold/hysteresis functions fit the same signed equations; neither preservation nor passivity picks one. The structural ratio 7/768 is not an occupancy threshold merely because a register has been added.

The new conclusions are closure requirements, not an invented native gate law:

| Obligation | Current result | Remaining source task |
|---|---|---|
| Local safe recovery image | Balanced signed star plus local vertex output | Select the two amplitudes and realize the full contact pattern |
| Gate compatibility | Nonconstant star masks generally leak | Prove allowed recovery masks are balanced, or derive an alternative port |
| Nonnegative burden | Linear signed identification fails globally | Declare positive stock or deviation semantics |
| Occupancy source | Rectified two-register lift is a candidate | Derive sources and their apparatus/resource budget |
| Restoration | Gradient mixing conserves aggregate occupancy | Supply a true drain, exported destination and renewal rule |
| Native initiation | Signed state does not determine hidden occupancy | Supply the observable, capacity normalization and predictive switching rule |

This gives the next package a concrete target: a local positive-stock source/sink mechanism with balanced recovery contacts, rather than another threshold chosen from a numerical target. A smaller protected code, background-offset representation or different nonlinear response remains possible, but requires a new declared model and verification.

## 7. Verification and manuscript use

The package has 34 exact finite checks and six numerical corroborations. Exact checks include incidence nilpotence, local rank/uniqueness, independent rational Gram reconstruction, its annihilator/multiplicities and imbalance bounds. The positivity and occupancy theorems have the proofs above; finite algebraic examples corroborate their identities rather than replacing their universal proofs. Numerical diagnostics compare the throughput formula with sign-resolved integration at three rate ratios and verify one positive-register trajectory against the exact signed solution.

The development addendum strengthens the manuscript narrative: persistence requires an inaccessible geometric sector, while a reusable recorder additionally requires positive stock and paid renewal. A passive signed equation can establish the former without establishing the latter. All claims retain their stated model premises. No physical identification, experimental confirmation, thermodynamic normalization or independent review is claimed.
