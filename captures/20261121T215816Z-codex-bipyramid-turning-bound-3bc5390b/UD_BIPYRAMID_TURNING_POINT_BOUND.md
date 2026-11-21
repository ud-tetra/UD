# A lower bound on the bipyramid gap-ratio minimizer

CYCLE-088 (#592) · **Physical Promotion = 0**

Use the pinned PB3 and PB5 compressed operators with zero exterior damping and radial coupling $g>0$. Write $R(g)=\Delta_{\rm PB5}(g)/\Delta_{\rm PB3}(g)$. Every global minimizer satisfies **$g_*>3/2$**. A two-point Padé model estimates its own minimum at $g\approx3.24353$. The rigorous bound follows from the original operators.

## Two-point Padé estimate

Set $x=g^2$ and write $R(g)=A+Vx+O(x^2)$ at zero and $R(g)=C+E/x+O(x^{-2})$ at infinity. The pinned limits and the weak-coupling root expansion give

$$
A=\frac{5(10-\sqrt5)}{57},\qquad
V=-\frac{42812\sqrt5}{3258025}-\frac{37628}{1954815},
\qquad C=\frac{5-\sqrt5}{6},\qquad E=-\frac{\sqrt5}{3}.
$$

For $V$, implicit coefficient matching at the separated slow roots of the PB3 cubic and PB5 sextic gives the respective $g^3$ gap coefficients $-6/625$ and $-(1850+404\sqrt5)/130321$. The symmetry of the characteristic factors under $(z,g)\mapsto(-z,-g)$ and conjugation makes each local damping series odd in $g$. The two strong-coupling gap coefficients of $g^{-3}$ from #598 are $3/2$ and $(5-3\sqrt5)/4$.

Choose the free linear denominator coefficient of the two-point $[2/2]$ family to be zero. With $b=V/E>0$, the resulting model is

$$
P(x)=\frac{A+Vx+Cb x^2}{1+b x^2}.
$$

The numerator of $P'(x)$ is $V+2b(C-A)x-bVx^2$. Its two roots have opposite signs, and the positive root gives the unique minimum on $x>0$. The actual minimizer's location and uniqueness are outside this approximation.

## Exact exclusion interval

The PB3 cubic $z^3+gz^2+5z+2g$ has a negative real root $-r$ with $r>0$. Its equation implies $g/r=(r^2+5)/(r^2+2)<5/2$. The other two roots have mean real part $-(g-r)/2$, so the PB3 stable gap obeys $\Delta_{\rm PB3}(g)\le(g-r)/2<3g/10$.

The replay verifies the pinned characteristic factorizations. Put $k=7/50$ and shift each stable PB5 factor by $z\mapsto z-kg$. For each leading Hurwitz determinant $H(g)$ of these monic factors, let $d=\deg H$. The replay checks that $(1+t)^dH((3/2)t/(1+t))$ has nonnegative coefficients, at least one positive coefficient, and degree $d$ with positive leading coefficient. Thus each determinant is positive for $0<g<3/2$, and the leading coefficient gives positivity at $g=3/2$. Routh–Hurwitz yields $\Delta_{\rm PB5}(g)>kg$ throughout this interval, including its upper endpoint. In particular,

$$
R(g)>\frac{7}{15}\quad (0<g\le 3/2),\qquad R(10)<\frac{4533}{10000}<\frac{7}{15}.
$$

The last comparison uses rational root isolation. The ratio is continuous on $g>0$ because the stable factors vary continuously and their gaps are positive for every finite positive coupling. Its endpoint limits both exceed $R(10)$, so it attains a global minimum in the interior. The exclusion interval proves the stated lower bound for every minimizer. The all-coupling PB3/PB5 gap ordering remains open.

## Review packet

The constructor verification in #598 links the pinned reviews for #595, #596, and #597. Independent approval remains pending.
