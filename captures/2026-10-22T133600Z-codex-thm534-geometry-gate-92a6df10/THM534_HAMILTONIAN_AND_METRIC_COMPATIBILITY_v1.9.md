# THM-534: Hamiltonian and metric compatibility of local contact selection

Development — no registry entry. Exact conditional structural audit. Constructor checked; independent non-constructor review pending. Physical promotion 0. This supplements v1.8; its norm, receipt and Lipschitz theorems are retained. No frozen particle operator, metric or source document is rewritten.

## 1. Outcome and scope

The squared-share soft strength

\[
m(f,t)=\frac{f^4+t^4}{(f^2+t^2)^2}
\]

is not a linear orthogonal evolution, is not Hamiltonian with the fixed standard two-coordinate symplectic structure, and fails the Jacobi identity when used as the coefficient of a naive shared-core incidence Poisson tensor. These are additional structural tests, not contradictions of support conservation or robustness.

The strongest new result is conditional: if a shared-core bracket has only independent pair-local contact coefficients, obeys Jacobi, is continuously differentiable away from the pair vacuum, and has unit response on both occupied axes, then every such coefficient is identically one. This rules out the proposed nonconstant weighting within that declared class. It does not derive which contacts are admissible.

The attached v0.39 ledger supplies a fixed skew incidence generator and unit support geometry. A constant skew matrix is mathematically a Poisson tensor, with quadratic Hamiltonian \(H=\|x\|^2/2\). This construction supplies a useful compatibility test, not a source declaration that face and cell amplitudes are physically canonical conjugates. The ledger's other symplectic programme concerns separately typed spaces; no identification with this pair is imported. Requiring a Poisson extension is stated here as an additional structural condition. More general non-Hamiltonian constitutive models or newly sourced phase-space geometry remain logically possible.

## 2. Support norm is weaker than metric preservation

For a single permitted contact with \(d=1\), the v1.8 continuous candidate is

\[
F(f,t)=m(f,t)(-t,f)=m(x)Jx,
\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

It preserves \(\|x\|^2\). However, a fixed linear orthogonal evolution must preserve inner products between all pairs of states, not just each state's norm. At the v1.8 control step \(\varepsilon=1/4\), its frozen-coefficient Cayley primitive gives

\[
\Phi(1,0)=\left(\frac{63}{65},\frac{16}{65}\right),\quad
\Phi(1,1)=\left(\frac{223}{257},\frac{287}{257}\right).
\]

Their original inner product is 1, while the transformed inner product is

\[
\left\langle\Phi(1,0),\Phi(1,1)\right\rangle
=\frac{18641}{16705}\ne1.
\]

The continuous field also fails additivity:

\[
F(1,1)=(-1/2,1/2)\ne F(1,0)+F(0,1)=(-1,1).
\]

Consequently neither candidate can be called the same frozen linear orthogonal operator, or a unitary map merely because it preserves support norm. This does not assert that all UD dynamics must be linear; it identifies a change of model class that requires its own source interpretation.

## 3. Fixed-area Hamiltonian test

**Theorem G1.** A \(C^1\) field \(F=mJx\) on the punctured plane preserves the standard area locally only if \(m\) is constant along circles. If \(m\) is also invariant under positive amplitude rescaling, it is constant throughout the punctured plane. Unit occupied-axis normalization then selects \(m=1\).

**Proof.** Since \(\operatorname{div}(Jx)=0\),

\[
\operatorname{div}F=Jx\cdot\nabla m=\partial_\theta m.
\]

Fixed-area preservation requires this expression to vanish, so \(m\) is constant on each circle. Rescaling invariance makes it independent of radius as well. A fixed standard symplectic Hamiltonian field has zero divergence, so the same necessary condition applies. Conversely a radial \(m(N)\), \(N=f^2+t^2\), has the Hamiltonian representation \(F=J\nabla H\) with \(H(N)=\tfrac12\int^Nm(u)\,du\); the rescaling-invariant normalized case is the unit field. \(\square\)

For the squared-share coefficient, at \((f,t)=(1,2)\),

\[
m=\frac{17}{25},\quad
\nabla m=\left(-\frac{48}{125},\frac{24}{125}\right),\quad
\operatorname{div}F=\frac{24}{25}\ne0.
\]

The frozen finite primitive fails area preservation too. Writing its angular increment as \(\alpha=2\arctan(\varepsilon m/2)\), it preserves radius and maps \(\theta\mapsto\theta+\alpha(\theta)\). Its determinant is

\[
\det D\Phi=1+
\frac{\varepsilon\,\partial_\theta m}{1+(\varepsilon m/2)^2}.
\]

At \((1,2)\) and the control step this equals \(49889/40289\), not one. Area failure and the earlier global bi-Lipschitz bounds are compatible; a bounded Jacobian need not have determinant one.

## 4. A local area repair is new geometry and does not repair the finite step

On the punctured plane, the continuous field preserves the weighted area density

\[
\rho=\frac1m,\qquad \operatorname{div}(\rho F)=\operatorname{div}(Jx)=0.
\]

Equivalently \(P=mJ\) is a valid two-dimensional Poisson tensor there and \(F=P\nabla(\|x\|^2/2)\). In two dimensions its Jacobi identity is automatic. More generally \(\rho=\psi(N)/m\), for any suitable positive radial \(\psi\), is invariant. Thus a conserved density is not uniquely selected. The coefficient has no continuous vacuum extension, so this does not supply a smooth global symplectic form at zero. Nor does the density follow from the frozen unit metric or determine an action unit.

The direct continuous-field density repair does not make the frozen finite primitive symplectic. At \(x=(1,1)\), \(\det D\Phi(x)=1\), but \(m(\Phi(x))>m(x)\). The weighted area multiplier is exactly

\[
\det D\Phi(x)\frac{\rho(\Phi(x))}{\rho(x)}
=\frac{66049^2}{66049^2+16320^2}<1.
\]

The same counterexample applies to every positive radial factor \(\psi(N)\), since \(N\) is unchanged. It shows why the continuous nonlinear field and its frozen-coefficient finite primitive cannot be treated as the same exact flow. Other possible discrete invariant measures are not classified here.

For an isolated pair, positive \(m\) also leaves the continuous unparameterized orbits unchanged: they are circles, with \(d\theta/ds=m(\theta)\). Here \(m=(3+\cos4\theta)/4\), so the model-parameter period is

\[
T=\int_0^{2\pi}\frac{d\theta}{m(\theta)}=2\sqrt2\,\pi.
\]

To evaluate it, each quarter-turn contributes \(\int_0^{2\pi}du/(3+\cos u)=\pi/\sqrt2\), using \(u=4\theta\) and the tangent half-angle substitution. This is a state-dependent clock reparameterization of the unit circular orbit, not a physical time, a finite-primitive event period, or a physical meaning for \(\sqrt2\).

## 5. Shared-core Jacobi obstruction

Now use two face amplitudes \(f_1,f_2\) incident to the same core \(t\). The naive antisymmetric bracket has only

\[
P^{f_i t}=-d_i m_i(f_i,t),\qquad
P^{t f_i}=d_i m_i(f_i,t),\qquad P^{f_1f_2}=0.
\]

Its Jacobi component for \((f_1,f_2,t)\) is

\[
\mathcal J^{f_1f_2t}
=d_1d_2\left(m_1\partial_t m_2-m_2\partial_t m_1\right).
\tag{5}
\]

**Proof.** Insert the displayed entries into
\(\mathcal J^{ijk}=\sum_\ell(P^{i\ell}\partial_\ell P^{jk}+P^{j\ell}\partial_\ell P^{ki}+P^{k\ell}\partial_\ell P^{ij})\).
Only the two shared-core terms survive, giving (5). \(\square\)

On \(K_-\), take private faces \(013\) and \(123\), both with \(d_i=1\) in cell \([0123]\), and set \((f_1,f_2,t)=(1,2,1)\). Then

\[
m_1=\frac12,\quad \partial_t m_1=0,\quad
m_2=\frac{17}{25},\quad\partial_t m_2=-\frac{48}{125},
\qquad\mathcal J^{f_1f_2t}=-\frac{24}{125}\ne0.
\]

The other six carrier amplitudes may all equal one, so every contact lies away from its pair vacuum. Extra incidences do not change this component: the two selected private faces each touch only this core, and their mutual bracket entry is identically zero. This is therefore an obstruction in the actual nine-coordinate face/core carrier, not only an abstract three-coordinate example.

A common nonvanishing scalar rescaling \(P\mapsto\lambda(x)P\) cannot remove this component. The two \(\partial_t\lambda\) terms cancel, leaving \(\lambda^2\mathcal J^{f_1f_2t}\). In particular a common clock factor does not turn this particular naive extension into a Poisson bracket. This does not exclude adding new bracket entries, dependence on more variables, or a separately sourced enlarged state space.

The Jacobi failure rules out the displayed tensor as a Poisson tensor. It does not prove that the vector field has no Hamiltonian representation with any other tensor or enlarged state.

## 6. Unit-response theorem within the pair-local bracket class

**Theorem G2.** Suppose the bracket above is required to obey Jacobi for all allowed triples, each \(m_i\) is \(C^1\) away from the pair vacuum, and for every nonzero argument

\[
m_i(0,t)=1,\qquad m_i(f,0)=1.
\]

Then \(m_i(f,t)=1\) for every nonvacuum pair on each contact in this overlapping two-contact family. No scale-invariance or role-exchange assumption is needed for this theorem.

**Proof.** Set \(f_1=0\), \(t\ne0\). The axis condition gives \(m_1=1\) and \(\partial_t m_1=0\). Equation (5) therefore requires \(\partial_t m_2(f_2,t)=0\) for every \(f_2\). For \(f_2\ne0\), \(m_2\) is constant on each half-line \(t>0\) and \(t<0\). Continuity at \((f_2,0)\), together with \(m_2(f_2,0)=1\), sets both constants to one. The other axis already has value one. Interchange the two contacts to obtain the same conclusion for \(m_1\). \(\square\)

The endpoint assumptions are the v1.8 unit-response postulate, not a new assertion of source closure. A rule that vanishes on an occupied axis, depends on neighbors beyond its pair, introduces new face–face bracket terms, or is non-Hamiltonian can leave this class. Such departures need their own source and conservation audit; they are not silently prohibited by this conditional theorem. Allowing only one active contact avoids this overlapping-star obstruction, but selecting that contact is precisely the still-open admission/scheduling task.

## 7. Verification, disposition and next source obligation

The fresh Fraction verifier passes 160 norm/determinant checks, 160 continuous weighted-area checks, 2,688 global Jacobi-component checks across 32 non-Poisson state controls, 1,008 signed Jacobi covariance checks, and three scalar-rescaling controls. The fixed unit tensor and isolated single-contact tensor each pass all 84 Jacobi components. The rational witnesses above are checked exactly. Only newly authored code is executed. The period formula is proved analytically, not asserted as a numerical control.

This is a compatibility obstruction, not a retraction of the proved v1.8 statements. Norm conservation and finite perturbation bounds survive. The squared-share law remains a conditional soft-response model that is non-Hamiltonian relative to the tested fixed structure, or requires independently sourced geometry; it is not eligible to be called the same frozen linear/Poisson dynamics.

For the native-selection programme, the resulting constraint is useful: **retain the source-bound unit incidence response if the present pair-local bracket and its unit endpoint responses must remain Poisson; put genuine selection in a separately derived admissibility, readiness or memory mechanism.** That mechanism still needs its own state variables, transition receipts, margins and event semantics. Alternatively an explicitly new global geometric source can be investigated, but local pairwise density fixes do not supply it automatically.

Native hard admission, exclusive event selection, physical action and particle identification remain OPEN. Constructor verification is not independent review. Physical promotion 0.
