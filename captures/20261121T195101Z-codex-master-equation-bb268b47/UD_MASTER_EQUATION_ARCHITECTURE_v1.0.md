# Unified Dynamics master equation architecture v1.0

**Scope.** Finite carrier identities are exact. The worked coarse-graining gives exact coefficients under specified transport and interaction laws. The packet PDE and four-dimensional action are candidate bridges. **Physical Promotion = 0.**

## Tier 1 · Finite chain dynamics

Let \(C=\bigoplus_{r=0}^{3}C_r(\mathcal K;\mathbb R)\) with orthonormal oriented simplex basis. The simplicial boundary \(B\) obeys \(B^2=0\). The skew operator \(A=B-B^\mathsf T\) generates \(\dot c=Ac\), with \(c(t)=e^{tA}c(0)\) and conserved stock \(\|c\|^2\). Nilpotency is the chain identity. A physical current and charge interpretation requires a separate map.

For a specified sink \(D=\sum_a\gamma_a P_a\), with \(\gamma_a\ge0\) and \(P_a=M_a M_a^+\), let \(G=A-D\). Then
\[
\dot c=Gc,\qquad \tfrac{d}{dt}\|c\|^2=-2c^\mathsf T D c .
\]
For the uncentered second moment \(\Sigma=\mathbb E[cc^\mathsf T]\) with a common deterministic \(G\),
\[
\dot\Sigma=G\Sigma+\Sigma G^\mathsf T=[A,\Sigma]-\{D,\Sigma\}.
\]
This is retained evolution and generally loses trace. Upon complexification, \(K_0=e^{\Delta t G}\) is a contraction for \(\Delta t\ge0\). One exact trace-preserving completion uses the isometry
\[
V c=K_0c\oplus (I-K_0^\dagger K_0)^{1/2}c .
\]
The first output block gives retained evolution. Discarding or resetting the complementary block prescribes an additional model of the environment. The completion does not fix the physical environment or imply a unique trace-preserving dynamics on the retained carrier. The PB5 radial operator is a declared example of a sink. [Merged PB5 radial projector, UD #583](https://github.com/ud-tetra/UD/pull/583)

## Exact coarse projection with memory

Choose normalized resolved columns \(U\) in the declared chain metric, where \(U^\dagger U=I\). Complex amplitudes use the complexified carrier. A real carrier needs a supplied two-quadrature realization or a selected complex modal sector to give this phase a native meaning. Set \(a=U^\dagger c\), \(P=UU^\dagger\), \(Q=I-P\), and \(\eta=Qc\). Write \(G_{aa}=U^\dagger G U\), \(G_{aQ}=U^\dagger GQ\), \(G_{Qa}=QGU\), and let \(G_{QQ}=QGQ\) act on \(\operatorname{im}Q\). Variation of constants gives exactly
\[
\dot a(t)=G_{aa}a(t)+G_{aQ}e^{tG_{QQ}}\eta(0)
 +\int_0^t G_{aQ}e^{(t-s)G_{QQ}}G_{Qa}a(s)\,ds .
\]
This provides a concrete test for a proposed local-in-time closure. For all initial states, an autonomous equation on \(a\) closes exactly when \(G_{aQ}=0\). For prepared resolved initial states, \(G_{Qa}=0\) also suffices. Otherwise the initial unresolved state or memory can contribute. The exact projected equation is linear in the state and the unresolved initial data. It cannot by itself identify a cubic amplitude term in a fixed linear coordinate. [Chorin, Hald and Kupferman, projection and memory](https://math.huji.ac.il/~razk/Publications/PDF/CHK00.pdf)

## Tier 2 · Explicit \(K_4\) coarse-graining and coefficient audit

### An explicit orthogonal projection and interpolation

Use a reference model with one filled tetrahedron per periodic cubic cell, with cell label \(n\), mesh spacing \(h>0\), and orthogonal cell blocks \(C_n\cong\mathbb C^{15}\). This model specifies intercell coupling separately. It is not a claim about the chain matrix of a given face-glued complex. In each cell \(u\) is the vector with value \(1/2\) on its four vertices and zero on all other simplices. Thus \(u^\dagger u=1\) and the isolated cell generator satisfies \(A_{\rm cell}u=0\). Let \(U\) inject one copy of \(u\) per cell. For the cube \(Q_n\) of volume \(h^3\), define
\[
a_n=(U^\dagger c)_n=\tfrac12\sum_{v\ \text{in cell }n} c_{n,v},\qquad
(\Pi_{\rm cont}^{(h)}c)(x)=h^{-3/2}a_n,\quad x\in Q_n.
\]
The interpolation \(I_h:a\mapsto h^{-3/2}a_n\) on \(Q_n\) is an isometry, so \(\Pi_{\rm cont}^{(h)}=I_hU^\dagger\) and \(\|\Pi_{\rm cont}^{(h)}c\|_{L^2}^2=\|Pc\|^2\). This is an explicit map to piecewise-constant fields. A smooth limit still requires convergence estimates, a scaling of the intercell interactions, and a geometric chart. For a genuinely shared chain carrier, the columns must be reconstructed, with their overlap Gram and any rank constraints accounted for.

### Mass from transport dispersion

Take units with effective \(\hbar=1\) in the model and complexify \(H_{\rm cell}=iA_{\rm cell}\). Supply the Hermitian intercell Hamiltonian \(U L_J U^\dagger\) with
\[
 (L_J a)_n=\sum_{\ell=1}^3 J_\ell(2a_n-a_{n+e_\ell}-a_{n-e_\ell}),\qquad J_\ell>0.
\]
The cell and hopping Hamiltonians preserve the resolved subspace. On the lattice the exact dispersion is
\[
 E(k)=2\sum_\ell J_\ell(1-\cos(k_\ell h)),\qquad
 (\mathsf m^{-1})_{\ell j}=\partial_{k_\ell}\partial_{k_j}E(0)
       =2J_\ell h^2\delta_{\ell j}.
\]
For isotropic hopping \(J_\ell=J\), the candidate scalar mass is \(m_{\rm eff}=1/(2Jh^2)\). This is the coefficient of \(-\nabla^2/(2m_{\rm eff})\) in the long-wavelength model. A refining family at fixed mass needs \(Jh^2\) to approach a finite positive limit. The general test for a proposed periodic native generator is to exhibit a smooth isolated band, compute its Hessian at the carrier momentum, and check branch stability and phase realization. A degenerate unresolved band may require multiple envelope components. The supplied hopping model is an exactly decoupled example, where no claim of isolation from every other band is needed.

### Cubic coefficient from a separate interaction law

Supply a local vertex energy \(g_v\sum_{n,v}|c_{n,v}|^4/2\), with real \(g_v\). Its complex Hamiltonian gradient is \(g_v|c_{n,v}|^2c_{n,v}\) on vertex coordinates and zero on other grades. On the uniform mode \(c_n=a_nu\), the gradient remains in that mode. Substitution gives the exact amplitude equation
\[
 i\dot a_n=(L_J a)_n+g_v\left(\sum_{v=1}^{4}|u_v|^4\right)|a_n|^2a_n
          =(L_J a)_n+\frac{g_v}{4}|a_n|^2a_n.
\]
With the chosen density normalization \(a_n=h^{3/2}\Psi_n\), the field coefficient is \(\Lambda_{\rm nl}=g_v h^3/4\). For a refining family at fixed nonzero cubic strength, \(g_v h^3\) must have a finite nonzero limit. This is a quartic model input. A true capacity-saturation law would need its own independently sourced energy and expansion.

**Identifiability.** The four vertices and the uniform preparation fix the overlap factor \(1/4\) for this interaction. Varying \(J\) or \(g_v\), including taking \(g_v=0\), preserves the local tetrahedral carrier, its boundary incidence, and the resolved projection. Hence capacities alone cannot select either coefficient. The open work is to source intercell adjacency weights, length and time normalization, phase realization, and a multipacket interaction law without fitting these observables.

### Candidate packet equation and conditional hydrodynamics

With an independently supplied gauge link law and smooth limit, a scalar model may take the form
\[
 i\partial_t\Psi=\left[-(\nabla-iq\mathbf A)^2/(2m_{\rm eff})
      +\varphi+V_{\rm eff}(\rho,\chi)+\Lambda_{\rm nl}\rho\right]\Psi,\qquad
 \rho=|\Psi|^2 .
\]
Here \(m_{\rm eff}\) is a positive scalar, \(\varphi\) is a scalar potential in frequency units, and the potentials and cubic coefficient are real. Under \(\Psi\mapsto e^{iq\alpha}\Psi\), the potentials transform as \(\mathbf A\mapsto\mathbf A+\nabla\alpha\) and \(\varphi\mapsto\varphi-q\partial_t\alpha\). On smooth regions with \(\rho>0\), writing \(\Psi=\sqrt{\rho}\,e^{i\theta}\) gives
\[
 \partial_t\rho+\nabla\cdot(\rho v)=0,\qquad
 v=(\nabla\theta-q\mathbf A)/m_{\rm eff},
\]
\[
 \partial_t\theta+\tfrac12m_{\rm eff}|v|^2+\varphi+
 V_{\rm eff}(\rho,\chi)+\Lambda_{\rm nl}\rho
 -\frac{\nabla^2\sqrt{\rho}}{2m_{\rm eff}\sqrt{\rho}}=0 .
\]
The last term follows by rewriting the candidate kinetic operator. The lattice origin of that operator, its physical units, and a coframe-tension identification require separate demonstrations. Dissipation would modify the continuity equation and should be derived or specified for that open model.

## Tier 3 · Candidate effective variational bridge

For a supplied four-dimensional geometry, a candidate local bulk action is
\[
 S_{\rm eff}=\int d^4x\,\sqrt{-g}\,
 (\mathcal L_{\rm grav}+\mathcal L_{\rm gauge}+\mathcal L_{\rm matter}
    +\mathcal L_{\Sigma}+\mathcal L_{\rm Yukawa}+\mathcal L_\phi),\qquad
 \delta S_{\rm eff}=0 .
\]
Write all six sectors as scalars relative to the same volume form. With signature \((-+++)\), the trial content is:

| Sector | Candidate content and required link |
| --- | --- |
| Gravity and depth | A curvature term \(R/(2\kappa)\), depth kinetic and potential terms, and a depth–burden source. Requires a metric, curvature, and source map. |
| Gauge | Curvature-squared terms. Requires links, continuum connection data, representation content, and a demonstrated \(U(1)\), \(SU(2)\), or \(SU(3)\) bridge for any group claimed. |
| Matter | Covariant spinor kinetic term and a bare mass \(m_0\). Requires a spinor bundle, covariant derivative, and microscopic matter map. |
| Order parameter | Covariant kinetic and potential terms for \(\Sigma\), separate from the Tier 1 covariance. |
| Yukawa | A gauge-invariant coupling when the assigned representations permit it. For a real singlet example with coupling \(-y\Sigma\bar\psi\psi\), the background mass is \(m_0+y\langle\Sigma\rangle\). |
| Scalar burden | A scalar kinetic term and potential with a declared normalization and independent burden observable. |

This specification organizes candidate conservative terms. The stationary bulk variation, with declared boundary data, supplies no irreversible dynamics for the Tier 1 sink. A bath, additional degrees of freedom, or a separately justified open-system variational construction would be required. A discrete spin sign supplies no derivation of physical fermion statistics.

## Provenance summary

| Result | Status |
| --- | --- |
| Finite skew conservation, retained covariance, memory equation | Exact for the declared chain metric and operators |
| \(\Pi_{\rm cont}^{(h)}\), \(m_{\rm eff}^{-1}=2Jh^2\), \(\Lambda_{\rm nl}=g_vh^3/4\) | Exact within the supplied reference model |
| Unique coefficients from simplex capacity alone | Underdetermined by the declared carrier and fixed linear projection |
| Continuum packet dynamics and four-dimensional action | Candidate bridges with source laws and convergence still open |

The companion replay checks the normalized 15-coordinate \(K_4\) mode, linear projector and sample memory coefficients, exact vertex-quartic overlap, and small-wavevector dispersion. This is constructor verification.
