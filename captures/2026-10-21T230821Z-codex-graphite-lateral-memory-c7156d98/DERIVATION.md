# Conservative lateral-memory elimination

## Proposition and scope

Let a finite real symmetric positive-definite matrix be partitioned as
\[
D=\begin{pmatrix}A&C\\C^{\mathsf T}&V\end{pmatrix}\succ0,
\qquad q=\begin{pmatrix}\ell\\z\end{pmatrix},
\qquad \ddot q+Dq=0.
\]
Dots denote a mathematical normalized time \(\tau\). The equal common mass has been absorbed into this time. For the numerical application, \(D=H/h_*\), where \(h_*=\lambda_{\max}(H)\) and \(H\) is the qualified symmetric stiffness. This normalization does not identify a physical or native UD clock. The lateral dimensions are52/100 and the vertical dimensions27/51; these are the existing affine coordinate spaces.

Write \(\Omega=A^{1/2}\). Then the vertical trajectory is exactly characterized by its original \(z_0,\dot z_0\) and
\[
\boxed{\ddot z(\tau)+Sz(\tau)+\int_0^\tau K(\tau-s)\dot z(s)\,ds=f(\tau)}
\]
with
\[
S=V-C^{\mathsf T}A^{-1}C,\qquad
K(\tau)=C^{\mathsf T}A^{-1}\cos(\Omega\tau)C,
\]
\[
\eta_0=\ell_0+A^{-1}Cz_0,\qquad
f(\tau)=-C^{\mathsf T}\cos(\Omega\tau)\eta_0
-C^{\mathsf T}\Omega^{-1}\sin(\Omega\tau)\dot\ell_0.
\]
All matrix functions of \(A\) commute with each other. They are not moved across \(C\).

## Proof

The lateral equation and its variation-of-constants solution are
\[
\ddot\ell+A\ell=-Cz,
\]
\[
\ell(\tau)=\cos(\Omega\tau)\ell_0+
\Omega^{-1}\sin(\Omega\tau)\dot\ell_0
-\int_0^\tau\Omega^{-1}\sin(\Omega(\tau-s))Cz(s)\,ds.
\]
Since
\[
\frac{d}{ds}\cos(\Omega(\tau-s))=
\Omega\sin(\Omega(\tau-s)),
\]
integration by parts gives
\[
\begin{aligned}
\int_0^\tau\Omega^{-1}\sin(\Omega(\tau-s))Cz(s)\,ds
={}&A^{-1}Cz(\tau)-A^{-1}\cos(\Omega\tau)Cz_0\\
&-\int_0^\tau A^{-1}\cos(\Omega(\tau-s))C\dot z(s)\,ds.
\end{aligned}
\]
Substitution into \(\ddot z+Vz+C^{\mathsf T}\ell=0\) proves the stated equation, including the negative sign of both initial-source terms. At zero time its acceleration is
\[
\ddot z(0)=-Sz_0-C^{\mathsf T}\eta_0
=-Vz_0-C^{\mathsf T}\ell_0,
\]
which recovers the full equation. Omitting the initial source is valid for the conditional preparation \(\ell_0=-A^{-1}Cz_0\), \(\dot\ell_0=0\), and potentially other specially invisible preparations; it is not valid for arbitrary hidden initial states.

## Spectral realization and reconstruction

Let \(A=U\operatorname{diag}(\alpha_j)U^{\mathsf T}\), \(G=U^{\mathsf T}C\), \(\omega_j=\sqrt{\alpha_j}>0\). If \(g_j^{\mathsf T}\) is row \(j\) of \(G\),
\[
K(\tau)=\sum_j W_j\cos(\omega_j\tau),\qquad
W_j=\frac{g_jg_j^{\mathsf T}}{\alpha_j}\succeq0.
\]
Use separate auxiliary variables \(r_j,s_j\), initialized to zero:
\[
\dot r=G\dot z-\operatorname{diag}(\omega)s,\qquad
\dot s=\operatorname{diag}(\omega)r.
\]
The memory force is \(G^{\mathsf T}\operatorname{diag}(\alpha^{-1})r\). The initial source is evaluated explicitly, without using the full trajectory. This is an exact finite realization of the convolution. It is not a smaller total phase-state realization than the original system; retaining both auxiliaries carries the hidden history.

With \(\widehat\eta_0=U^{\mathsf T}\eta_0\) and \(\widehat v_{\ell0}=U^{\mathsf T}\dot\ell_0\), reconstruct the hidden state by
\[
\ell=U\left[\cos(\omega\tau)\widehat\eta_0+
\omega^{-1}\sin(\omega\tau)\widehat v_{\ell0}+\alpha^{-1}r\right]
-A^{-1}Cz,
\]
\[
\dot\ell=U\left[-\omega\sin(\omega\tau)\widehat\eta_0+
\cos(\omega\tau)\widehat v_{\ell0}-\omega^{-1}s\right].
\]
Products and functions inside these brackets act componentwise. Uniqueness of the finite linear initial-value problem, or direct substitution of the reconstruction, establishes equivalence with the full motion for every initial state.

## Storage and positive-type kernel

Completing the square yields
\[
\frac12\|\dot q\|^2+\frac12 q^{\mathsf T}Dq
=\frac12\|\dot\ell\|^2+\frac12\|\dot z\|^2
+\frac12z^{\mathsf T}Sz
+\frac12(\ell+A^{-1}Cz)^{\mathsf T}A(\ell+A^{-1}Cz).
\]
Thus \(S\succ0\), and the full energy is conserved. For arbitrary real sample vectors \(v_a\) and times \(t_a\),
\[
\sum_{a,b}v_a^{\mathsf T}K(t_a-t_b)v_b
=\sum_j\frac1{\alpha_j}\left|\sum_a
 e^{i\omega_jt_a}g_j^{\mathsf T}v_a\right|^2\ge0.
\]
This is positivity of the translation kernel, not pointwise positivity of \(K(\tau)\). Its oscillations can exchange energy reversibly.

## Transfer identity and absence of a derived friction law

For \(\operatorname{Re}s>0\),
\[
\widehat K(s)=C^{\mathsf T}A^{-1}s(s^2I+A)^{-1}C,
\]
\[
s^2I+S+s\widehat K(s)=s^2I+V-C^{\mathsf T}(s^2I+A)^{-1}C.
\]
The inverse of this expression is exactly the vertical block of \((s^2I+D)^{-1}\). This resolvent identity is independent of the trajectory test.

The finite kernel is a sum of oscillatory terms, with positive mode frequencies and no imposed reservoir. In particular,
\[
\lim_{\varepsilon\downarrow0}\int_0^\infty
 e^{-\varepsilon\tau}K(\tau)\,d\tau
=\lim_{\varepsilon\downarrow0}\sum_jW_j
\frac{\varepsilon}{\varepsilon^2+\alpha_j}=0.
\]
This zero Abel limit is not a measured friction coefficient or evidence that graphite has zero friction. A continuum limit, damping mechanism, stochastic preparation or source-selected physical reservoir would be additional hypotheses. None is introduced here. The argument is conventional block elimination and does not select a native UD/material correspondence.

The theorem is exact conditional on finite symmetric positive-definite \(D\). Application to the four matrices uses their finite-step numerical qualification. It is neither an exact certificate for the nonlinear atomistic potential nor non-constructor review.
