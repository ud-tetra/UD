# Certified exterior-only PB3 and PB5 settling

CYCLE-088 (#592) · **Physical Promotion = 0** · Constructor evidence pending independent review.

Use the raw exterior Whitney edge sink in [PR #606](https://github.com/ud-tetra/UD/pull/606) at $g_{\rm ext}=4$ and zero radial damping. Compare with the two-cell benchmark horizon $T=2\pi/\sqrt{32/7}$ and tolerance $1/62$.

Write $d=16/3$, $\Omega_3^2=24/5$, $\Omega_5^2=40/7$ and
$$
\alpha_n=d/2-\sqrt{d^2/4-\Omega_n^2},\qquad
\beta_n=d/2+\sqrt{d^2/4-\Omega_n^2}.
$$
In PB3 the radicand is $64/9-24/5=104/45$. In PB5 it is $88/63$. Both rings satisfy $0<\alpha_n<\beta_n<d$.

## Contour calculation and norm bound

Let $P_0$ project onto the normalized collective channel and $P_\perp=I-P_0$. For a positively oriented contour enclosing the three poles, the finite-dimensional resolvent formula gives the normalized memory kernel
$$
\widetilde K_n(t)=-\frac{1}{2\pi i}\oint e^{tz}
\left[\frac{P_\perp}{z+d}+\frac{zP_0}{(z+\alpha_n)(z+\beta_n)}\right]dz
=k_0(t)P_0+k_\perp(t)P_\perp,
$$
where the residues give
$$
k_0(t)=\frac{\alpha_n e^{-\alpha_n t}-\beta_n e^{-\beta_n t}}{\beta_n-\alpha_n},
\qquad k_\perp(t)=-e^{-dt}.
$$
For unit vectors $x,y$, Cauchy–Schwarz and the orthogonality of the projectors give
$$
|x^*\widetilde K_n(t)y|
\le \max(|k_0|,|k_\perp|)\sum_{j\in\{0,\perp\}}\|P_jx\|\|P_jy\|
\le \max(|k_0|,|k_\perp|).
$$
Both channel norms attain the corresponding scalar amplitudes. Since the two collective-mode terms have opposite signs,
$$
\|\widetilde K_n(t)\|_2\le
\max\left(
\frac{\alpha_n e^{-\alpha_n t}}{\beta_n-\alpha_n},
\frac{\beta_n e^{-\beta_n t}}{\beta_n-\alpha_n},e^{-dt}
\right).
$$
The same argument gives the maximum of the last two terms as the exact pointwise error after retaining only the slow residue
$\alpha_n e^{-\alpha_n t}P_0/(\beta_n-\alpha_n)$.

Every term in the envelope is decreasing in time. With rational enclosures of $\alpha_n,\beta_n$, and a reciprocal Taylor bound on $e^{-x}$, the replay certifies these strict upper bounds uniformly for $t\ge29/10$.

| Ring | Normalized kernel norm | Slow-residue approximation error |
| --- | ---: | ---: |
| PB3 | $17/1250=0.0136$ | $37/5{,}000{,}000$ |
| PB5 | $17/2000=0.0085$ | $3/125{,}000$ |

Since $T>29/10$, both bounds hold for every $t\ge T$ and are below $1/62$. This establishes a sufficient settling horizon at the declared coupling. Optimization of the coupling or horizon, the error of a local-in-time approximation to the resolved evolution, and physical calibration remain open.

Run `python3 replay_ring_settling.py` and compare stdout to `replay-results.txt`. The script uses the Python standard library.

## Independent review checklist

- Replay the rational invariant-subspace identities in the resolvent capture.
- Check the residue signs, orthogonal channel norm, and rational exponential bounds.
- Verify the matching two-cell tolerance and horizon, with raw exterior coupling 4 and zero radial damping throughout this certificate.
