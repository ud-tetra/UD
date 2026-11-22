# An upper bound on the PB5/PB3 gap-ratio minimizer

CYCLE-088 (#592) · **Physical Promotion = 0**

With zero exterior damping and the pinned compressed PB3 and PB5 operators, write $R(g)=\Delta_{\rm PB5}(g)/\Delta_{\rm PB3}(g)$ for $g>0$. Every global minimizer satisfies $g_*<4$. Together with #599, this gives $3/2<g_*<4$. The bound leaves the exact location and uniqueness open.

## Certified tail comparison

The replay reconstructs the pinned incidence operators and checks their stable characteristic factorizations. For each monic stable PB5 factor $p_5(z,g)$ of degree $n$, put $k=13/20$ and form $g^n p_5(z-k/g,g)$. This clears all denominators in $g$ with positive leading coefficient for $g>0$. Substitute $g=4+t$ into each leading Hurwitz determinant. The exact coefficient check gives positive constant coefficients and positive nonzero coefficients. Thus every determinant is positive on $t\ge0$. Routh–Hurwitz gives

$$\Delta_{\rm PB5}(g)>\frac{13}{20g}\qquad(g\ge4).$$

For PB3, use the stable cubic $C(z,g)=z^3+gz^2+5z+2g$ and let $K=157/100$. The polynomial $g^3 C(-g+2K/g,g)$ has positive constant and positive nonzero coefficients when expanded in $t=g-4$. Since $C(z,g)$ tends to minus infinity at the negative real end, it has a real root $-r<-g+2K/g$. The other two roots have mean real part $-(g-r)/2>-K/g$. Hence at least one PB3 stable root lies to the right of $-K/g$, and

$$\Delta_{\rm PB3}(g)<\frac{157}{100g}\qquad(g\ge4).$$

## Exclusion of the tail

Rational root isolation of the stable factors at $g=3$ encloses their rightmost real parts. The certificates combine as

$$
\frac{411}{1000}<R(3)<\frac{412}{1000}
<\frac{65}{157}<R(g)\qquad(g\ge4).
$$

Therefore the entire closed tail $[4,\infty)$ has larger ratios than the certified witness. The existence and lower bound from #599 give the stated two-sided exclusion. This certificate concerns the pinned spectral ratio and does not require a monotonicity assumption.
