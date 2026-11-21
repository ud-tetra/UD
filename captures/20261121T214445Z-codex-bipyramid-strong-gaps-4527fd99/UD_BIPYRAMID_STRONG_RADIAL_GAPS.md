# Strong radial coupling in PB3 and PB5

CYCLE-088 (#592) · **Physical Promotion = 0**

For the same compressed generators and radial edge-trace sinks as #595 and #596, take $g=\gamma_{\rm rad}$ and zero exterior damping. Exact factor expansions give

$$
\Delta_3(g)=\frac{3}{2g}+O(g^{-2}),\qquad
\Delta_5(g)=\frac{5-\sqrt5}{4g}+O(g^{-2}),\qquad
\lim_{g\to\infty}\frac{\Delta_5(g)}{\Delta_3(g)}
=\frac{5-\sqrt5}{6}\approx 0.460655337083.
$$

The ordering persists for sufficiently large $g$. Both gaps close in the singular projection limit.

## Root expansions

The replay reconstructs the incidence operators and verifies the stable characteristic factors from #596 symbolically. For $h=1/g$, write $z=z_0+hw$. The finite slow branches and their first-order damping coefficients $-\operatorname{Re}w$ are:

| Carrier | Characteristic factor | Limiting $z_0$ | Damping coefficient |
| --- | --- | --- | --- |
| PB3 | Quadratics | $0$ | $5,\;24/5$ |
| PB3 | Cubic | $\pm i\sqrt2$ | $3/2$ |
| PB5 | Quadratics | $0$ | $7,\;40/7$ |
| PB5 | Quartic | $0$ | $(9\pm\sqrt5)/2$ |
| PB5 | Sextic | $\pm i\sqrt2$ | $(5\pm\sqrt5)/4$ |

For the PB3 cubic the order-$h$ coefficient of $hC$ at $z_0$ is $z_0(2w+3)$. For the PB5 quartic the order-$h^2$ coefficient of $h^2 U$ at zero is $w^2+9w+19$. For the PB5 sextic the order-$h^2$ coefficient of $h^2 S$ at either $z_0$ is $-8w^2-20w-10$. Each scaled equation has simple roots. The other roots of the factors satisfy $z/g\to-1$, as seen by rescaling $z=gy$. These are the seven PB3 and eleven PB5 fast roots counted with multiplicity. Taking the smallest slow coefficient gives the displayed gaps.

The two leading factors are the same PB3 cubic and PB5 sextic used in #596's visibility argument. Since the exceptional positive coupling values for these factors are finite, their leading poles also govern the memory decay rates for sufficiently large $g$.

## Numerical cross-check and scope

An 801-point logarithmic sweep from $10^{-4}$ to $10^4$ found $\Delta_5/\Delta_3<1$ at each sample. The largest sampled ratio was approximately $0.681046668$ at $g=10^{-4}$. The exact weak and strong limits establish the ordering near both ends. The grid leaves an all-positive-coupling proof open.

## Independent review packet

| Comparison | Pinned head | CI run | Constructor review |
| --- | --- | --- | --- |
| Unit coupling (#595) | 09e5eff19a5247998d49bedb4b085c13020c871e | 44952381002 | 6008326332 |
| Weak coupling (#596) | 0d2c773cdad9a14192712283dee52052d73acd9c | 44952742601 | 6008364748 |

Review the exact memory denominator and numerical pole selection in #595, then the small-coupling branch expansions and visibility argument in #596. Each head passed its GitHub workflow, a fresh byte-for-byte replay, and capture size and SHA-256 verification. Independent review remains pending.
