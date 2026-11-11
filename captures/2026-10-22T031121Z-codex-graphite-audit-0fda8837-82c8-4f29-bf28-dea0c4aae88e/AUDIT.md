# Adversarial self-audit of graphite residual response

**Scope:** append-only correction/qualification of
`captures/2026-10-22T030626Z-codex-graphite-residual-ba6a8b1a-73e0-4af4-86fd-acbc0bb680f4/RESEARCH_NOTE.md`.
Development — no registry entry. Constructor self-audit, not independent review.
Physical promotion 0. The earlier capture and its manifest are unchanged.

## Algebra checked

For a single channel set $\omega=kv$, $A=\kappa-m\omega^2$,
$B=\eta\omega$, $D=A^2+B^2$. With $\eta>0$ and fixed $v>0$, the unique
long-time periodic solution of
$m\ddot q+\eta\dot q+\kappa q=g\cos(\omega t+\phi)$ is

$$q(t)=\frac{g}{D}\big[A\cos(\omega t+\phi)
 +B\sin(\omega t+\phi)\big].$$

The resisting force on the slider is
$f_x=-\partial_x U=-gkq\sin(\omega t+\phi)$.
Over one cycle, $\langle f_x\rangle=-g^2kB/(2D)$, so its *positive drag
magnitude* is

$$F_d=-\langle f_x\rangle
=\frac{g^2\eta k^2v}{2[(\kappa-mk^2v^2)^2+(\eta kv)^2]}.
\tag{A1}$$

Independently, $\eta\langle\dot q^2\rangle/v=F_d$, confirming the sign,
factor $1/2$, powers of $k$ and $v$, and energy balance. With $g$ in force
units, $\kappa$ in force/length, $\eta$ in mass/time and $k$ in inverse
length, (A1) has force units.

For a sum of independent modes, the $v\to0^+$ coefficient is
$\sum_jg_j^2\eta_jk_j^2/(2\kappa_j^2)$ and the next analytic correction is
$O(v^3)$ at fixed positive stiffness. For one mode with $m'=k'=0$ and
$g\ne0$, $\eta>0$, differentiation yields equation (3) in the original
capture exactly.

A separate fourth-order numerical integration of the driven differential
equation at $m=0.9$, $\eta=0.7$, $\kappa=4$, $g=1.3$, $k=1.1$, $v=1.5$ (all
arbitrary consistent units), after discarding 20 periods, gave
$F_d^{\rm integration}=0.287378032182$ and
$F_d^{\rm formula}=0.287378031731$. The integration also gave
$\eta\langle\dot q^2\rangle/v=0.287378032548$. This tests the formula
independently of its algebra, but is a constructor check, not a molecular
friction measurement. A central finite difference of $\log F_d$ in a
load-dependent numerical example checked equation (3) to $1.5\times10^{-11}$.

## Repairs to reading the original equations

1. **Damped domain:** Interpret (1) as a periodic steady kinetic-drag law
   with $\eta_j>0$ for every included mode (and $v>0$, $k_j>0$). At
   $\eta_j=0$ away from resonance, a bounded closed mode transfers zero
   *long-time mean* power. At $\eta_j=0$ and
   $\kappa_j=m_jk_j^2v^2$, the displayed fraction becomes $0/0$ and no
   bounded periodic steady solution exists. It must not be evaluated by
   substitution or interpreted as infinite steady friction.
2. **Logarithmic domain:** Equation (3) only applies to a channel with
   $g_j\ne0$, $\eta_j>0$, $k_j>0$ and hence $F_j>0$. Use the derivative of
   (A1), rather than $\partial_L\log F_j$, when a channel crosses zero.
   A total load slope is $\sum_j\partial_L F_j$; its logarithmic slope is
   $\sum_j(F_j/F_{\rm extra})\partial_L\log F_j$ if
   $F_{\rm extra}>0$. A flat sum need not mean each channel is flat.
3. **Load-dependent geometry/mass:** Equation (3) explicitly holds $m,k$
   load-independent. If either varies, write
   $D=(\kappa-mk^2v^2)^2+(\eta kv)^2$ and use

   $$\partial_L\log F_d=2g'/g+\eta'/\eta+2k'/k-D'/D,$$
   $$D'=2(\kappa-mk^2v^2)(\kappa'-m'k^2v^2-2mkk'v^2)
   +2\eta kv(\eta'kv+\eta k'v). \tag{A2}$$

   In the low-speed limit, the load slope also contains $2k'/k$. A
   contact/strain model must justify setting it to zero.
4. **Identifiability:** (A1) is a standard damped-oscillator result. Even a
   verified velocity-linear excess and paired-angle equality would not
   identify UD. Independently sourcing the native observable-to-carbon
   coupling, damping/export law and load dependence, while excluding their
   double counting in the conventional baseline, remains required.

The 60° complement, the signed-residual definition and the conditional
finite-harmonic no-go survive this audit. The finite closed argument requires
bounded energy under the imposed drive; at undamped resonances and on finite
transients it gives no steady-friction inference. Numerical values above
are unitless trial inputs, not graphite predictions.
