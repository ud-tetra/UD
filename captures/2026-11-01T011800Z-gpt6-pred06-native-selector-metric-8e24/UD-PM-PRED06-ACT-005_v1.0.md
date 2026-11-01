# UD-PM-PRED06-ACT-005 v1.0 — Curvature/Hodge-only quadratic action is blind to flat integer winding sectors

**Kind:** NO-GO (harmonic kernel). **Status:** EXACT_CONDITIONAL / VERIFIED_SCOPED. **Review:** DEFERRED. **Physical promotion:** 0.

## Domain, operators and source

Let \(K\) be a finite oriented simplicial complex with \(H^1(K;\mathbb R)\ne0\). Use real 1-cochains \(a\in C^1(K;\mathbb R)\), the source unit-simplex inner product, exterior coboundary \(d_1=\partial_2^{\mathsf T}\), and divergence \(\delta_1=\partial_1\). Let \(h\ne0\) be the unit-period harmonic representative: \(d_1h=0=\delta_1h\). Its integer sectors are \(a_n=n h\), \(n\in\mathbb Z\). The harmonic state exists in the previously constructed punctured complex under its separate topology assumptions.

The archived source ledger Q169 contains a skew Hodge–Dirac incidence generator, Q165 a norm-preserving support quantity, and Q31 a structural curvature observable distinct from an action coefficient. G05 (master loop weight) is source-open in ledger v0.39. The existence of any particular *physical* action term is not inferred from these source objects.

## Theorem

For any function \(\Phi\) depending only on divergence and curvature \((\delta_1a,d_1a)\), the sector values \(\Phi(\delta_1a_n,d_1a_n)=\Phi(0,0)\) are identical for every integer \(n\). In particular for any positive coefficients \(\alpha,\beta\),
\[
S_{\mathrm{Hodge}}(a)=\frac\alpha2\|d_1a\|^2+\frac\beta2\|\delta_1a\|^2
\quad\Rightarrow\quad
S_{\mathrm{Hodge}}(3h)-S_{\mathrm{Hodge}}(2h)=0.
\]
Likewise the degree-1 block of the Hodge–Dirac generator annihilates \((0,h,0,0)\), so a pure quadratic Dirac-derivative action \(\|A_K(0,a,0,0)\|^2\) cannot split these sectors.

**Proof.** The coboundary and codifferential are linear, and \(h\) belongs to their common kernel. Hence \(d_1(nh)=n d_1h=0\) and \(\delta_1(nh)=0\) for all \(n\). Substitution into any functional of just these arguments gives a common value; the displayed action vanishes on each sector. The Hodge–Dirac degree-1 image has only the adjacent boundary/coboundary entries, each zero on \(h\). QED.

## Exact finite witness and scope

An independently triangulated eight-triangle annulus has \((V,E,F)=(8,16,8)\), boundary ranks \((7,8)\), and \(\beta_1=1\). An exact rational harmonic cochain has period one, squared unit-metric norm \(5/8\), but both curvature and divergence vanish identically. Its nonzero period is therefore invisible to the displayed Hodge-derivative action.

A harmonic-mass/stock term \(\lambda\|h\|^2/2\), a nonlocal period term, a coupling to additional fields, an independently source-normalized charge, or a boundary/holonomy constraint could distinguish sectors; each is **additional dynamical/action input**. If the unit-period integer is read only as \(\exp(2\pi i n)\), all sectors have the same periodic readout 1. This is a scoped obstruction to a pure derivative/curvature-only action, not a universal statement about all possible UD actions. No physical promotion.
