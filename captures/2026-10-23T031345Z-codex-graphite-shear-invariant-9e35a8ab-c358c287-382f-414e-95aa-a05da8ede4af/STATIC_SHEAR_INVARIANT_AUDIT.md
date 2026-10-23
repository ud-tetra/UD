# Static shear invariant and pressure gate

**Development — no registry entry · Constructor checked · Physical promotion 0 · 23 October 2026 UTC**

The conventional one-parameter $(2,1)$ first-harmonic potential [1, Table 5] uses a signed energy coefficient $U_1$ per upper atom, graphene lattice parameter $a=2.4660$ Å, moiré index $N_c=7$, carbon-12 mass $m_C$, rigid equal-and-opposite sliding of two sheets, and a specified minimum-energy path. Its *static area shear strength* is $\tau$ (Pa). Its rigid relative shear frequency is $f=c\tilde\nu$ (s$^{-1}$) with spectral wavenumber $\tilde\nu$ (cm$^{-1}$). It says nothing by itself about the finite-speed friction force in the 2026 experiment.

- Type II $U_1>0$: $f^2=2N_cU_1/(m_Ca^2)$ and $\tau=C_{II}\sqrt{N_c}U_1/a^3$. Set $q=-(1+\sqrt{33})/8$, $C_{II}=16\pi\sqrt{1-q^2}|1+2q|/3=6.182800612\ldots$. Then $\tau/\tilde\nu^2=(C_{II}/2)m_Cc^2/(a\sqrt{N_c})$.
- Type I $U_1<0$: $f^2=-4N_cU_1/(m_Ca^2)$ and $\tau=-(16\pi/\sqrt3)\sqrt{N_c}U_1/a^3$. Then $\tau/\tilde\nu^2=(4\pi/\sqrt3)m_Cc^2/(a\sqrt{N_c})$.

The constants are **8.4856459 × 10$^4$ Pa/(cm$^{-1}$)$^2$** for $(2,1)$ type II and **1.9914935 × 10$^5$ Pa/(cm$^{-1}$)$^2$** for hypothetical $(2,1)$ type I. The type I $(3,1)$ value is **1.4613567 × 10$^5$ Pa/(cm$^{-1}$)$^2$**. No fitted PES amplitude enters the ratio.

| Published calculation [1] | $\tilde\nu$ (cm$^{-1}$) | Table $\tau$ (Pa) | Invariant from rounded $\tilde\nu$ (Pa) | Difference |
| --- | ---: | ---: | ---: | ---: |
| $(2,1)$ rigid, type II | 0.404 | 13900 | 13849.93 | +0.36% |
| $(2,1)$ out-of-plane relaxed, type II | 0.510 | 22000 | 22071.16 | −0.32% |
| $(2,1)$ two atoms constrained, type II | 0.590 | 29500 | 29538.53 | −0.13% |
| $(3,1)$ rigid, type I | 0.214 | 6680 | 6692.43 | −0.19% |

This is a **same-source rounding and unit check**: both columns were calculated by the paper from the *same Fourier PES*. It provides no independent evidence for a physical amplitude. The KC model gives opposite $(2,1)$ registry type and much larger shear scale [1,2]; use its corresponding type I branch if applying this idealized ratio to that model.

For smooth $U_1(d(P))$ and fixed branch, $a(P)\tau(P)/\tilde\nu(P)^2$ is constant. Therefore $d\ln\tau/dP=2d\ln\tilde\nu/dP-d\ln a/dP$. At fixed $a$, $\tau'$ can be obtained from the **measured** $f'$ and $\tau$ within the model; it cannot be predicted numerically from the published equilibrium-only DFT tables. The sign of $U_1$ changes around 3.5 Å in the vdW-DF3 distance scan [1, Fig. 4]; there the log derivative is undefined and the branch formula switches. The normal compliance $dd/dP$, loss $D_h$, contact geometry, and finite-speed estimator are independent missing inputs. No numeric load response for the 2026 kinetic friction is claimed.

| Claim | Type | Direct dependency | Failure mode or next check |
| --- | --- | --- | --- |
| $\tau/\tilde\nu^2$ type II and I formulas | DERIVED conditional conventional identity | First-harmonic PES; specified MEP; two mobile sheets; $m_C,a,N_c$ | Higher harmonics or altered effective mass break the formula. |
| Tabulated values within 0.4% | NUMERICAL same-source replay | Rounded Tables 4–6, standard unit conversion | Not independent DFT verification or experiment. |
| $d\ln\tau/dP=2d\ln\tilde\nu/dP-d\ln a/dP$ | DERIVED conditional branch-local identity | Smooth $U_1(P)\ne0$ and fixed branch | Fails at registry switch, altered contact, or different mode. |
| Kinetic friction load response or UD-specific residual | OPEN | Bath loss, contact, speed, observed traces and uncertainties | No inference from static ratio; do not reuse Q120/Q128/Q163 as graphite damping. |

Source [1]: I. V. Lebedeva *et al.*, [arXiv:2511.01338](https://arxiv.org/pdf/2511.01338), Eq. (2), Tables 4–6, Fig. 4. Source [2]: A. S. Minkin *et al.*, [arXiv:2308.06302](https://arxiv.org/pdf/2308.06302), Eq. (4), Table II. Reproduce with `python3 reproduce_shear_invariant.py`. The proposed CRL-2 subdivision governance supplied with the session is followed as a development-lane labeling rule, not a promotion receipt.
