# Weak radial coupling in PB3 and PB5

CYCLE-088 (#592) · Unit-coupling comparison (#595) · **Physical Promotion = 0**

For the pinned cell-average projections and radial edge-trace sinks, with zero exterior damping, write $g=\gamma_{\rm rad}$. The stable spectral gaps satisfy

$$
\Delta_3(g)=\frac{3}{10}g+O(g^2),\qquad
\Delta_5(g)=\frac{10-\sqrt5}{38}g+O(g^2),\qquad
\lim_{g\to0^+}\frac{\Delta_5(g)}{\Delta_3(g)}
=\frac{5(10-\sqrt5)}{57}.
$$

The limit is approximately $0.681046668640$. Both gaps vanish linearly. The ordering holds for sufficiently small positive $g$, and the unit-coupling comparison gives a ratio of approximately $0.630038644536$.

## Stable spectrum and damping slopes

The replay builds $L(g)=QAQ-gD$ over rational polynomial coefficients, with $D=MM^+$ and $A=\partial-\partial^\mathsf T$. Its characteristic polynomial on the full carrier includes one zero factor per resolved direction. After removing these and the fixed undamped factors established for PB3 and PB5, the exact stable polynomials factor as follows, up to constant normalization.

| Carrier | Stable characteristic polynomial |
| --- | --- |
| PB3 | $(z^2+gz+5)^4(5z^2+5gz+24) C(z,g)^2$ |
| PB5 | $(z^2+gz+7)^2(7z^2+7gz+40) U(z,g)^2 S(z,g)^2$ |

$$
\begin{aligned}
C(z,g)&=z^3+gz^2+5z+2g,\\
U(z,g)&=z^4+2gz^3+(9+g^2)z^2+9gz+19,\\
S(z,g)&=z^6+2gz^5+(9+g^2)z^4+13gz^3+(19+4g^2)z^2+18gz+4g^2.
\end{aligned}
$$

At each simple root of a factor at $g=0$ use $z'(0)=-p_g/p_z$. The quadratic factors and the quartic $U$ give damping slope $1/2$. The cubic $C$ gives slope $2/5$ at the origin and $3/10$ on the pair originating at $\pm i\sqrt5$. For the double zero of $S$, substitution $z=gw$ and division by $g^2$ gives $19w^2+18w+4$ at $g=0$, yielding slopes $(9\pm\sqrt5)/19$. The nonzero roots of $S$ have $x=z^2=(-9\pm\sqrt5)/2$ and slope $(2x^2+13x+18)/(2x(2x+9))$. These evaluate to $(10\mp\sqrt5)/38$, with the smaller value on the lower-frequency pair. Each minimum is separated from the remaining slopes.

## Visibility in the memory transform

The slow factors $C$ and $S$ are irreducible over $\mathbb Q(g)[z]$, as verified by the replay's factorization over $\mathbb Q[z,g]$ and monicity in $z$. Each occurs squared in the characteristic polynomial. At $g=1$ its specialization is coprime to the other factors and divides the reduced memory denominator. Consequently at least one entry of the polynomial memory numerator fails divisibility by the square of the slow factor over $\mathbb Q(g)[z]$. Monic division would otherwise preserve divisibility at $g=1$.

Remove any common copy of the slow factor from that entry and the characteristic denominator. The remaining entry numerator is coprime to the slow factor over $\mathbb Q(g)[z]$, so its resultant is a nonzero rational function of $g$. Away from finitely many exceptional values, the slow poles therefore survive. There is a positive interval adjacent to zero in which the memory pole rates share the spectral gap slopes above. The result concerns the exponential rate of the tail. The leading poles are oscillatory, and the calculation supplies no constant Frobenius prefactor, finite settling certificate, or all-coupling ordering.
