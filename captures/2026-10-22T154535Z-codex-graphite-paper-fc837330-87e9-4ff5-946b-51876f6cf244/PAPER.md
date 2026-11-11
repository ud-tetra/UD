# Commensurate graphite superlubricity: geometry, dissipation, and a testable Unified Dynamics correspondence

**Working paper, 22 October 2026. Development — no registry entry.** Constructor checked; no independent review or physical promotion. This is a theory and experimental-design note, not a claim that UD has already explained the experiment.

## Abstract

Chen *et al.* report narrow friction **peaks** at graphite twist angles approximately 21.8° and 38.2°, corresponding to the (2,1) commensurate moiré, with negligible measured load dependence. Other higher-order commensurate orientations have no detectable peak. We derive the exact paired angles from triangular Bravais geometry and show why their sum of 60° is symmetry information already present in the ordinary honeycomb lattice. A reciprocal-lattice selection rule suppresses registry corrugation at the (2,1) interface relative to alignment without requiring a new UD degree of freedom. We formulate a conditional UD correspondence in terms of an independently sourced transport-to-mode coupling and passive loss port. It gives a dimensional velocity-response law and a symmetry null test, but its material coupling and damping are presently unknown. A static, fixed-cell graphite Hessian remains numerically unqualified. The resulting paper claim is an exact geometric explanation plus a preregistrable route to test an additional UD effect, rather than a fitted friction coefficient.

## 1. Observation, source scope, and cleaned research question

The primary source is W. Chen, J. Wang, Q. Zheng, and Z. Wu, *Physical Review Letters* **137**, 166201 (2026), DOI [10.1103/ly48-b4l2](https://doi.org/10.1103/ly48-b4l2). The accessible abstract reports sharp but small peaks at 21.8° and 38.2°, negligible peak load dependence in contrast with the aligned state, and exponentially decreasing sliding barriers with higher commensuration indices according to its theoretical analysis and simulations. The article body, supplement, raw friction curves, error bars, load range, and velocity series were not available for this note. “Friction vanishes at those angles” is therefore inaccurate: the peaks are detected, while many other commensurate peaks are undetectable. “Load independent” refers to the reported peak behavior within the tested range, not an exact all-load identity.

The research question is: **After a fully specified honeycomb/moiré, interlayer-potential, elastic, phonon, edge, and measurement model accounts for the angular peaks and their load response, does an independently specified UD transport law predict any residual friction or load dependence at the paired angles?** The measured load slope alone cannot be assigned to UD.

## 2. Exact triangular geometry of the two angles

Let \(\mathbf a_1\cdot\mathbf a_2=a^2/2\), with \(|\mathbf a_i|=a\). The honeycomb has a two-atom basis over this triangular Bravais lattice. For \((m,n)=(2,1)\), take equal-length supercell directions

\[
\mathbf t=2\mathbf a_1+\mathbf a_2,\qquad
\mathbf t'=\mathbf a_1+2\mathbf a_2.
\]

Their squared lengths are \(7a^2\), and their dot product is \(13a^2/2\). Their oriented cross product is \(3\sqrt3 a^2/2\). Thus

\[
\cos\theta={13\over14},\qquad
\sin\theta={3\sqrt3\over14},\qquad
\theta=21.7867892983\ldots^\circ.
\]

The opposite orientation, expressed in the 0°–60° lattice sector, is \(60^\circ-\theta=38.2132107017\ldots^\circ\). The two measured rounded angles add to 60° because the triangular Bravais lattice has hexagonal rotation/reflection equivalences. This is a useful consistency check, but the arithmetic does not by itself isolate a tetrahedral face or establish an extra UD sector. The index \(7=m^2+mn+n^2\) is a moiré cell index, not a UD coefficient.

For a mirror-symmetric interface **and a reflected sliding direction and experimental boundary conditions**, a scalar friction observable obeys the conditional null relation

\[
F(\theta,\mathbf e;N,v)=F(60^\circ-\theta,M\mathbf e;N,v).
\]

Here \(M\) is the reflection acting on the full specimen and drive. A difference with an unreflected direction or different edges does not contradict this relation. Any proposed chiral UD term must respect this transformation or identify and independently measure a symmetry-breaking material state.

## 3. What conventional registry filtering already supplies

For infinite, rigid, identical periodic layers with a translationally invariant interaction and convergent Fourier expansion, the bulk sliding energy has the form

\[
U_{\rm bulk}(\mathbf x,z)=U_0(z)+\sum_{\mathbf G\in\Lambda^*\cap R_\theta\Lambda^*,\,\mathbf G\ne0}
C_{\mathbf G}(z)e^{i\mathbf G\cdot\mathbf x}.
\]

Only reciprocal vectors common to both layers contribute a translational corrugation. In the exact lattice audit archived in the UD project, the first common nonzero reciprocal shell has squared length \(Q=7\) in units of the primitive reciprocal vector for (2,1), versus \(Q=1\) at alignment. A (3,1) control has \(Q=13\). A short-ranged interlayer interaction can make higher-wave-number coefficients small while leaving the \(\mathbf G=0\) mean adhesion. The two-atom honeycomb basis changes the coefficients but does not automatically annihilate this shell. This explains why commensurability need not imply large friction; the actual barrier, exponential rate, contact-size effects, and load slope require a physical interaction and dissipation model. A conservative energy landscape alone gives no steady heat rate.

The archived exact shell proof and the conditional mode-response derivation are in UD's graphite registry-to-mode capture on the draft graphite-coupling branch; the 2026 PRL abstract is an independent experimental/theoretical source. The source article's full quantitative fits have not been checked here.

## 4. The UD correspondence as a falsifiable conditional model

UD's existing finite-complex retention theorem distinguishes a protected carrier sector from a reciprocal burden port; protection for that *declared mathematical complex* requires a port with zero projection onto the protected sector (\(PF=0\)). It is not a theorem about carbon atoms or graphite phonons. A physical bridge would need an explicit map from a carbon bilayer's triangular cells, displacement fields, contact geometry, and environmental modes into the UD complex and its port, with units, conservation, and a source-selected coupling. A 60° angle, by itself, supplies none of those maps.

Let \(x=vt\) be sliding displacement and \(q\) a material mode, with an independently computed stable energy \(U(x,q;N)\). Its mixed derivative \(g=U_{qx}\), stiffness \(K=U_{qq}\), and bath operator \(\Gamma\succeq0\) must be fixed from material data without fitting the paired-angle friction targets. On a smooth low-speed stationary branch, the conventional passive response has

\[
F_{\rm diss}(v)=v\,\zeta+o(v),\qquad
\zeta=\left\langle\|\Gamma^{1/2}K^{-1}g\|^2\right\rangle.
\]

The angle brackets average one sliding period. This statement assumes a stable smooth branch, controlled rigid modes, steady response, and no stick-slip transitions; \(\zeta\) has units kg/s. It is **ordinary passive dynamics**. The genuinely UD hypothesis is narrower: a source-derived UD face/edge transport and port law imposes a nontrivial constraint on \(g\) or \(\Gamma\) across angle, load, and velocity that a conventional model with the same calibration budget does not impose. No such material map or sourced rate has yet passed the admission test. In particular, a mathematical protected subspace does not guarantee zero phonon excitation in graphite; cancelling net force can leave large local mode couplings.

For a *separate*, independently identifiable candidate UD lossy mode, a convenient discriminating response shape follows from the explicit model

\[
U_{\rm mode}=\tfrac12\kappa q^2-g\,q\cos(kx),\quad
m\ddot q+\eta\dot q+\kappa q=g\cos(kvt),
\]

giving the cycle-averaged dissipative force

\[
F_{\rm candidate}(v,N)=
{g(N)^2\eta(N)k^2v\over
2\{[\kappa(N)-mk^2v^2]^2+[\eta(N)kv]^2\}}.
\]

Here \(g\) is a force, \(\kappa\) is N/m, \(\eta\) is kg/s, and \(k\) is m\(^{-1}\). This is a **conditional response law, not a graphite fit, a UD-derived coupling, or a parameter-free prediction**. At \(v\to0\), for nonzero \(\kappa\), \(F_{\rm candidate}/v\to g^2\eta k^2/(2\kappa^2)\). If \(g,\eta,\kappa\) are nonzero and differentiable in load, its fractional low-speed load slope is \(2\partial_N\ln|g|+\partial_N\ln\eta-2\partial_N\ln\kappa+2\partial_N\ln k\); fixed lattice period sets the last term to zero. Apparent load independence can arise from compensating derivatives and is not a UD signature.

If the candidate couples to the *same* damped mode as a baseline drive \(g_0\), write \(g=g_0+g_{\rm U}\). At fixed \(m,\eta,\kappa,k\), the true excess is proportional to \(2\operatorname{Re}(g_0^*g_{\rm U})+|g_{\rm U}|^2\), and can have either sign. The displayed positive formula is an excess only under an independently justified separate-mode or orthogonality assumption. Subtracting two measured friction curves does not establish that assumption.

## 5. Present evidence and decisive next experiment

| Claim | Type | Present status |
|---|---|---|
| Pair \(\theta,60^\circ-\theta\), \(\cos\theta=13/14\) | Exact honeycomb geometry | Checked; no unique UD implication |
| Narrow peaks with little load dependence | Empirical report | Supported by accessible PRL abstract; raw series inaccessible |
| Common reciprocal shell \(Q=7\) for (2,1) | Conventional exact registry selection | Archived arithmetic proof under rigid periodic assumptions |
| UD graphite material port and damping | Physical correspondence | OPEN: no independently sourced map or coefficient |
| Full released 81-coordinate Hessian at two (2,1) preparations | Numerical gate | HOLD: one-sided, step-stability, and directional checks failed |
| Remaining friction or load coefficient after conventional baseline | Physical prediction | NO-GO with present data and numerical resolution |

The strongest next protocol is a **single forward model** across 0°, 21.7868°, 38.2132°, and at least one higher commensurate control (for example 32.2042° from (3,1)): use the same measured or independently parameterized interlayer potential, finite-contact geometry, elasticity, phonon coupling, bath law, temperature, load equilibrium, and drive direction. Freeze it before exposing held-out friction and velocity curves. Measure both paired angles under reflected drive/boundary conditions, with multiple loads and speeds. Compute a baseline predictive distribution \(F_0(\theta,N,v)\) and its error/parameter uncertainty. Only a reproducible excess \(R=F_{\rm obs}-F_0\), outside that uncertainty and replicated independently, creates an admission target for a UD material port. A source-derived UD law must then predict the excess shape and magnitude with no angle-specific refit. Fit-equivalent generic damped oscillators are conventional comparators and do not count as UD confirmation.

The archived numerical investigation isolated much of the held graphite finite-difference side discrepancy to the carbon angular term in the original REBO force. Its remaining stencil is sensitive to representational perturbations and lacks a stable tested step plateau; it is not a measured dissipation or load coefficient. The fixed-cell positive eigenvalues of an unqualified Hessian do not clear the derivative gate or prove full-cell stability. Improving that Hessian can aid a material-mode calculation, but it cannot by itself yield a friction law.

**Decision.** This paper establishes the conventional paired-angle geometry and a transparent conditional UD test. It does not claim that the current UD substrate explains load-independent graphite friction beyond established moiré physics. Development lane only, constructor checked, physical promotion 0. A non-constructor adversarial review is required before any CRL-2b claim; the attached CRL-2 subdivision remains a proposal.

## References and provenance

1. Chen, Wang, Zheng, and Wu, *Observation of Superlubricity at Commensurate Moiré Graphite Interfaces*, *Phys. Rev. Lett.* **137**, 166201 (2026), https://doi.org/10.1103/ly48-b4l2. Abstract inspected 22 October 2026; article and supplement unavailable.
2. UD graphite registry-to-mode hypothesis capture, draft branch `origin/graphite-334`, `captures/2026-10-21T164738Z-codex-graphite-coupling-5ff68aa8/REPORT.md` (exact shell arithmetic, conditional passive response).
3. UD protected-retention port theorem, `docs/UD_Protected_Retention_Robustness_and_Port_Condition_v0.1.md` on repository main (finite-complex scope).
4. UD draft PR #334 boundary-aware derivative capture; draft PRs #394, #396, and #399 source trace, error transfer, and force complement. These are constructor work, not independent validation.
5. Supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (physical promotion 0) and `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md` (proposal). The supplied `Gap2_FINAL_Finite_Genesis.png` did not materialize and was not used.
