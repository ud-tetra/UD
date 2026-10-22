# Graphite angle-pair residual: conditional quantitative response

**Status:** development — no registry entry. Constructor: Codex, 2026-10-22.
**Physical promotion:** 0. No experimental friction data or independent review in this capture.

## 1. Observable and symmetry control

The abstract of Chen *et al.*, *Physical Review Letters* **137**, 166201
(2026), DOI [10.1103/ly48-b4l2](https://doi.org/10.1103/ly48-b4l2), reports
small **sharp friction peaks**, with negligible load dependence, at 21.8° and
38.2°. Both correspond to the `(2,1)` commensurate moiré pattern. The abstract
does not supply digitized force-versus-load or force-versus-velocity traces or
their uncertainty. Neither peak is a measured exact zero.

The triangular Bravais vectors satisfy
$|a_1|=|a_2|=a$ and $a_1\cdot a_2=a^2/2$. For
$u=2a_1+a_2$, $w=a_1+2a_2$, we obtain
$|u|^2=|w|^2=7a^2$ and $u\cdot w=13a^2/2$, hence

$$\theta_-=\cos^{-1}(13/14)=21.786789298\ldots^\circ,\qquad
\theta_+=60^\circ-\theta_-=38.213210702\ldots^\circ.$$

The pair is one ordinary hexagonal-lattice symmetry orbit, not two
independent fitted angles. Graphene's atomic lattice has a two-site honeycomb
basis, and actual graphite registry, flake shape and sliding direction must be
carried through a symmetry comparison. A triangle-face interpretation does not
follow from the sum alone.

Fix an experimental protocol with twist $\theta$, speed $v>0$, normal load
$L$, temperature $T$, sliding direction $\hat e$, contact and preparation $c$.
Let $F_0(\theta,v,L,T,\hat e,c)$ be a frozen, independently validated
conventional honeycomb/moiré prediction, including its ordinary relaxation,
phonon and dissipative channels. Define the **signed modeling residual**

$$R(\theta,v,L,T,\hat e,c)=F_{\rm measured}-F_0.$$

$R$ includes model and measurement error; it is not itself a UD signal.
Under an *ideal* matched-interface 60° symmetry, with the direction and
translation/registry transformed appropriately, the angle-pair null is
$R(\theta_-)=R(\theta_+)$. Differences in uncontrolled contact or the
graphite stacking basis void that equality. Symmetry alone places no positive
lower bound on $R$.

## 2. What the present closed calculation predicts

The existing finite positive-frequency hidden-mode calculation eliminates
internal coordinates into a reversible cosine memory kernel, with zero
zero-frequency Abel integral. With bounded driven trajectories away from exact
undamped resonances, net internal energy gain over $N$ periods is bounded,
therefore long-time mean power transfer per period tends to zero:

$$\lim_{N\to\infty}\frac{E(N\mathcal T)-E(0)}{N\mathcal T}=0,
\qquad F^{\rm closed}_{\rm excess,diss}=0.$$

This is an **exact conditional no-go for steady dissipative excess** in the
declared finite closed harmonic model. It does not predict a zero total
measured friction or static corrugation. At an exact undamped resonance,
boundedness fails, so the stated long-time argument cannot be applied.

The most recent released sliding calculations left two `(2,1)`-labeled
references on derivative-qualification HOLD; the earlier 4/4 reversible
memory qualification did not supply a bath, physical clock, or UD-to-carbon
map. The `21`/`31` case names are source labels, not automatically the two
measured complementary angles. Do not extract a physical frequency, load
slope or friction amplitude from these runs.

## 3. A minimal *conditional* excess-force law

To state exactly what new inputs would be needed, introduce an optional
additional displacement mode $q_j$ for each of three symmetry-related
in-plane reciprocal channels $j$. Along a slider trajectory $x=vt$, set
$k_j=|G_j\cdot\hat e|>0$ (inverse length) and $\omega_j=k_jv$. For one channel
take a linearized coupling energy and phenomenological damped equation

$$U_j(q_j,x)=\tfrac12\kappa_j q_j^2-g_jq_j\cos(k_jx+\phi_j),\qquad
m_j\ddot q_j+\eta_j\dot q_j+\kappa_jq_j=g_j\cos(\omega_jt+\phi_j),$$

where $\kappa_j>0$, $m_j>0$, $\eta_j\ge0$. The modes here are a **trial
constitutive architecture**, not a derived UD mode or an additional fit
licensed by the paper. In this parametrization $g_j$ has units of force,
$\eta_j$ of mass/time, and $k_j$ of inverse length. For independent modes,
the positive mean dissipated power is

$$\overline P_j=\frac{g_j^2\eta_j\omega_j^2}
{2[(\kappa_j-m_j\omega_j^2)^2+(\eta_j\omega_j)^2]}.$$

Thus the **testable excess under these supplied assumptions** is

$$\boxed{F_{\rm extra}(\theta,v,L)=
\sum_{j=1}^{3}\frac{g_j(\theta,L)^2\eta_j(\theta,L)k_j(\theta)^2v}
{2\{[\kappa_j(\theta,L)-m_j(\theta,L)k_j(\theta)^2v^2]^2+
[\eta_j(\theta,L)k_j(\theta)v]^2\}}.} \tag{1}$$

The formula is an *added dissipative contribution* if the baseline genuinely
omits these degrees of freedom. If $F_0$ already contains them, adding (1)
double counts. A negative empirical $R$ cannot be explained by (1) alone.
If $k_j=0$, that channel is unforced along the chosen direction and contributes
zero; evaluate its limit separately from the displayed $k_j>0$ expression.

For the low-speed regime $m_jk_j^2v^2\ll\kappa_j$ and
$\eta_jk_jv\ll\kappa_j$,

$$F_{\rm extra}=v\sum_{j=1}^3
\frac{g_j^2\eta_j k_j^2}{2\kappa_j^2}+O(v^3), \tag{2}$$

which gives a quantitative, velocity-linear prediction once *independently*
measured/source-derived $g_j,\eta_j,\kappa_j,k_j$ are supplied. In particular,
symmetry-related channels may be tied by rotations, but neither the 60° angle
sum nor the UD unit-weight carrier fixes their dimensional values.

For one channel, holding $m,k$ load-independent, the local normal-load
logarithmic slope is exactly

$$\frac{\partial\log F_j}{\partial L}=
2\frac{g_j'}{g_j}+\frac{\eta_j'}{\eta_j}
-\frac{2(\kappa_j-m_jk_j^2v^2)\kappa_j'+
2\eta_j\eta_j'k_j^2v^2}
{(\kappa_j-m_jk_j^2v^2)^2+(\eta_jk_jv)^2}, \tag{3}$$

where primes mean derivatives with respect to load. At low speed the slope
of $F_j/v$ is
$2g_j'/g_j+\eta_j'/\eta_j-2\kappa_j'/\kappa_j+O(v^2)$.
**Load independence** requires this combination to be small *or* cancellation
among independently contributing channels. It is not entailed by triangular
geometry. A real observed flat total-friction curve also does not separately
constrain this excess if the baseline and excess load slopes cancel.

## 4. Discriminating measurement and pre-fit gate

1. Freeze $F_0$ and its uncertainty from an atomistic and experimental control
   analysis that uses neither the targeted residual nor a freely refitted UD
   amplitude. Match contact area, speed, direction, temperature, pressure,
   registry and stacking at both orientations. Measure full angular and load
   traces, not just the two rounded angle values.
2. Infer or derive $g_j,\kappa_j,m_j,\eta_j$ from independent structural,
   vibrational and linewidth measurements under the same loads; specify how
   any *native* UD face observable maps to $q_j$ and to carbon forces. Freeze
   their load functions before inspecting $R$. A three-channel pattern or
   Lorentzian resonance without this map remains conventional phonon physics.
3. Compare the precomputed amplitude $R/v$ and load derivative with (2)-(3),
   including combined uncertainty of $F_0$ and the measurement; check the
   velocity dependence against the *same* fixed parameters in (1). Apply the
   symmetry transformation to the full traces at $\theta_\pm$. If an excess
   lies outside the uncertainty envelope, test whether it survives stronger
   ordinary relaxation, phonon, defect and contact-area baselines before
   attributing it to UD.

The existing UD coefficient ledger v0.39 has zero current seam-sector
pairing source under equal weights (`Q22`), and its edge-class anisotropy
`Q14/Q20` requires a source-selected nonuniform contact before activation.
It does not supply $g_j,\eta_j,\kappa_j$ or their graphite load dependence.
That historical ledger does not overrule later project amendments. Therefore
the **only presently parameter-free dissipative excess in the declared closed
model is zero**; (1)-(3) are conditional functions, not a nonzero UD numerical
forecast. Physical promotion remains 0.

## Source/provenance register

- External experimental primary abstract: Chen *et al.* (2026), DOI above;
  full paper and supplement not asserted as read.
- Internal finite conservative reduction: `captures/2026-10-21T230821Z-codex-graphite-lateral-memory-c7156d98/`, reversible-kernel derivation in open draft [PR 334](https://github.com/ud-tetra/UD/pull/334); this source is not yet on main.
- Latest derivative qualification: `captures/2026-10-22T025511Z-codex-graphite-boundary-146db834/REPORT.md` in the same draft PR, 0/2 `21`-labeled cases pass boundary-aware protocol.
- Uploaded historical `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, `Q14`, `Q20`, `Q22` (source data, not current promotion).
- Uploaded `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md` (development lane; independent review prerequisite to registry advancement).
- The uploaded packet-modulation, triangular-transport and seam-phase Markdown files are reconstructed placeholders; they supply no constitutive force or bath law. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not inspected.
