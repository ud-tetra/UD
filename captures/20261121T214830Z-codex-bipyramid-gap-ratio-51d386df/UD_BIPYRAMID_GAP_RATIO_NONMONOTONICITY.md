# The PB5/PB3 radial gap ratio is nonmonotone

CYCLE-088 (#592) · Unit, weak and strong captures (#595–#597) · **Physical Promotion = 0**

With zero exterior damping, write $g=\gamma_{\rm rad}$ and $R(g)=\Delta_{\rm PB5}(g)/\Delta_{\rm PB3}(g)$. The ratio increases for sufficiently large $g$:

$$
R(g)=\frac{5-\sqrt5}{6}-\frac{\sqrt5}{3g^2}+O(g^{-4}),
\qquad
R'(g)=\frac{2\sqrt5}{3g^3}+O(g^{-5}).
$$

The weak-limit ratio is larger than the strong-limit ratio. Together with the eventual upturn, this rules out both global monotone decrease and global monotone increase.

## Exact expansion

Use the stable characteristic factors verified in #597. The separated leading branches at large $g$ come from the PB3 cubic $C$ and PB5 sextic $S$,

$$
\begin{aligned}
C(z,g)&=z^3+gz^2+5z+2g,\\
S(z,g)&=z^6+2gz^5+(9+g^2)z^4+13gz^3+(19+4g^2)z^2+18gz+4g^2.
\end{aligned}
$$

Set $h=1/g$, $z=i\sqrt2+h\,w(h)$ and $F(w,h)=p(i\sqrt2+hw,1/h)$. The negative powers of $h$ cancel for both factors. The leading equations $F(w,0)=0$ have simple roots at $w_0=-3/2$ for $C$ and $w_0=-(5-\sqrt5)/4$ for $S$. The implicit function theorem gives analytic branches. Write $F=F_0+hF_1+h^2F_2+\cdots$ and $w=w_0+h w_1+h^2 w_2+\cdots$. Coefficient matching gives

$$
w_1=-\frac{F_1}{F_0'},\qquad
w_2=-\frac{F_2+F_1'w_1+\tfrac12 F_0''w_1^2}{F_0'},
$$

with all expressions evaluated at $w_0$. The symmetry $p(-z,-g)=\pm p(z,g)$ and real coefficients give $w(-h)=\overline{w(h)}$ by uniqueness. Thus the real damping expansion has only odd powers of $h$. The exact coefficients are:

| Carrier | Coefficient of $g^{-1}$ in the gap | Coefficient of $g^{-3}$ in the gap |
| --- | ---: | ---: |
| PB3 | $3/2$ | $3/2$ |
| PB5 | $(5-\sqrt5)/4$ | $(5-3\sqrt5)/4$ |

Dividing these analytic series yields the ratio and permits termwise differentiation near $h=0$. The leading branches remain visible in the memory kernels in this regime by the established finite-exception argument.

## Independent exact counterexample

The replay isolates all distinct stable roots in rational intervals or complex rectangles at two positive couplings and bounds the rightmost real parts. Its rational certificates are

$$
\frac{4532}{10000}<R(10)<\frac{4533}{10000},
\qquad
\frac{4605}{10000}<R(100)<\frac{4607}{10000}.
$$

In particular, the strong-limit constant is above $R(10)$. The sampled absence of a PB3/PB5 rate reversal is consistent with this upturn. The strict ordering $R(g)<1$ at every positive coupling remains a separate question.
