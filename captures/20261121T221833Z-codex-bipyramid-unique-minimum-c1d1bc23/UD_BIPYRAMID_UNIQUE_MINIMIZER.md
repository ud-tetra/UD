# The PB5/PB3 spectral-gap ratio has a unique global minimum

CYCLE-088 (#592) · **Physical Promotion = 0**

With zero exterior damping and the pinned stable characteristic factors from #600, the global minimizer of $R(g)=\Delta_{\rm PB5}(g)/\Delta_{\rm PB3}(g)$ is unique. Certified bisection encloses it in

$$
\frac{166059063}{52428800}<g_*<\frac{332118127}{104857600}.
$$

The endpoints are approximately $3.1673252678$ and $3.1673252773$. This enclosure applies to the spectral ratio of the original operators.

## Branch selection

The exterior exclusions in #599 and #600 reduce the problem to $[3/2,4]$. The replay uses the PB3 cubic and PB5 sextic there. For each parameter subinterval $J$, it proposes a center $c$ with positive imaginary part from a floating-point root at the midpoint $g_0$. It then uses outward-rounded interval arithmetic to certify a disk containing exactly one root for every $g\in J$. In particular, writing $p(c+v,g)=\sum_j P_j(g)v^j$ and $m=P_1(g_0)$, the disk radius $r$ passes the Rouché test

$$
\sup_{g\in J}\left(|P_0(g)|+|P_1(g)-m|r+
\sum_{j\ge2}|P_j(g)|r^j\right)<|m|r.
$$

The root stays above the real axis and to the right of the line $\operatorname{Re}z=-3/5$ in PB3 or $-1/3$ in PB5. Real coefficients supply the conjugate root. The replay encloses the coefficients of the quotient by this pair through monic polynomial division and uses shifted Hurwitz tests to place the quotient and all other stable factors strictly to the left of the respective line. These strict separations select the leading pair throughout the whole bracket. Simplicity and the implicit function theorem give analytic continuation of its upper-half-plane root.

## Uniqueness and bisection

Put $a=\Delta_{\rm PB3}$ and $b=\Delta_{\rm PB5}$, both positive. The sign of $R'$ is the sign of $N=b'a-ba'$, and $N'=b''a-ba''$. The replay encloses branch derivatives via

$$
z'=-\frac{p_g}{p_z},
\qquad
z''=-\frac{p_{gg}+2p_{zg}z'+p_{zz}(z')^2}{p_z}.
$$

| Certified interval | Sign |
| --- | --- |
| $[3/2,79/25]$ | $N<0$ |
| $[79/25,159/50]$ | $N'>0$ |
| $[159/50,4]$ | $N>0$ |

Thus $N$ crosses zero exactly once in the middle interval. Rational bisection with certified signs at the trial points gives the stated enclosure. The outer exclusions establish global uniqueness on $g>0$. Floating-point root guesses supply disk centers. The inequalities, branch selection and bisection signs are evaluated with 35-decimal outward-rounded intervals. The replay requires NumPy and mpmath.
