# THM-534: complex graph form, dark-state leakage and selection symmetry

Development — no registry entry. Exact deductions within the v2.4 candidate; constructor checked, independent review pending. Physical promotion 0.

## 1. Scope and fixed carrier

This analysis adds no new dynamical interaction. It examines v2.4's changed positive network model. Its canonical field pairs \((x,y)\), gate registers, minimal completion principle, potential profile and charge scale remain supplied candidates. The original frozen incidence operators and metric are retained as inputs. Representing the added pair as a complex number is an exact mathematical change of coordinates, not a derivation that the dual is native support.

Order the unique coordinates as faces \(012,013,014,023,024,123,124\), followed by cores \(\tau_0=[0123]\), \(\tau_1=-[0124]\). The eight contacts \((f,\tau,d)\) are

\[
(0,7,-1),(0,8,1),(1,7,1),(2,8,-1),
(3,7,-1),(4,8,1),(5,7,1),(6,8,-1).
\]

Their undirected graph is a connected tree with nine vertices and eight edges. This graph is the face/core incidence subsystem, not the entire 23-dimensional chain complex or a pentagonal particle carrier.

## 2. Exact complex representation

Let \(z=x+iy\), \(S_e=|z_f|^2+|z_\tau|^2\) and

\[
b_e=\mathbf e_f+i d_e\mathbf e_\tau,
\qquad B_e=b_eb_e^\dagger=P_e+iA_e.
\]

Then v2.4's positive contact cost is

\[
\boxed{Q_e=\frac12|b_e^\dagger z|^2
=\frac12|z_f-i d_e z_\tau|^2.}\tag{1}
\]

The canonical field equations are equivalently

\[
\boxed{i\dot z=L(q)z,
\quad L(q)=\sum_e\chi_e B_e+\sum_eU_eP_e\succeq0,}
\tag{2}
\]

and the Hamiltonian is

\[
H_+=\frac12\sum_ep_e^2+\frac12z^\dagger L(q)z.
\tag{3}
\]

**Proof.** The real equations give \(\dot z=Az-i\Omega z\), so \(i\dot z=(iA+\Omega)z\). Substituting \(\Omega=\sum_e(\chi_e+U_e)P_e\) proves (2). Equation (1) follows by expanding its squared modulus. Each \(B_e\) is a positive rank-one Hermitian matrix and each \(U_eP_e\) is positive. This establishes (3) with the original real canonical normalization; no Planck constant or physical time has been introduced. \(\square\)

The equation has the mathematical form of a finite Schrödinger equation with a state-coupled gate. That form alone is not a quantum, Born-rule or matter correspondence. The full field-plus-gate evolution is nonlinear because \(q,p\) respond to field costs.

## 3. The contact tree has a fixed graph-Laplacian gauge

Define

\[
s=(-1,1,1,-1,-1,1,1,1,-1),
\quad T_i=\begin{cases}s_i,&i\text{ a face},\\-i s_i,&i\text{ a core},\end{cases}
\quad z=Tu.
\]

For every contact, \(s_f=d_es_\tau\). Consequently

\[
\boxed{T^\dagger B_eT
=(\mathbf e_f-\mathbf e_\tau)(\mathbf e_f-\mathbf e_\tau)^{\mathsf T}.}\tag{4}
\]

Thus

\[
i\dot u=\left(\mathcal L_\chi+W\right)u,
\quad \mathcal L_\chi=\sum_e\chi_e c_ec_e^{\mathsf T},
\quad c_e=\mathbf e_f-\mathbf e_\tau,
\quad W=\sum_eU_eP_e,
\tag{5}
\]

and \(Q_e=|u_f-u_\tau|^2/2\). This removes all signed edge phases on this tree. On a graph with cycles, simultaneous removal requires a separate cycle-consistency check; no such generalization is assumed here. A basis gauge used to derive (5) is not an additional native physical selector.

**Theorem G1.** If \(m\) of the eight contacts have strictly positive admission weights and the others have zero weight, then

\[
\operatorname{rank}\mathcal L_\chi=m,
\qquad \dim_{\mathbb C}\ker\mathcal L_\chi=9-m.
\tag{6}
\]

The kernel consists of fields constant on each admitted connected component.

**Proof.** The quadratic form is \(u^\dagger\mathcal L_\chi u=\sum_e\chi_e|u_f-u_\tau|^2\); it vanishes precisely under the stated equality constraints. Every admitted subgraph of a tree is a forest with \(9-m\) components. Rank-nullity gives (6). \(\square\)

For all contacts admitted there is one complex admission-dark mode, \(u=a\mathbf1\). This is the kernel of the admission operator only. The full \(L\) has no nonzero kernel at finite gate positions with every \(U_e>0\), since its positive diagonal potential covers all nine coordinates. A zero admission cost is not a zero Hamiltonian store.

## 4. Diagonal wake potential generally destroys admission darkness

**Theorem G2 (frozen graph).** For a fixed admitted graph and fixed profiles, its admission-dark subspace is invariant under the full field generator \(\mathcal L_\chi+W\) if and only if \(W_i\) is constant on each admitted component.

**Proof.** The graph Laplacian annihilates a field constant on each component. Diagonal multiplication maps all such fields into the same subspace exactly when it has a common value within each component. Necessity follows by taking a field equal to one on a single component and zero elsewhere. \(\square\)

For evolving gates, maintaining this equality along the trajectory is an extra requirement; checking it at a single time is insufficient. Components can also change as contacts become admitted.

A sharp onset control starts all gates at \(q=p=0\), with uniform \(\beta>0\), potential \(U_e(0)=\beta\), and nonzero \(u(0)=a\mathbf1\). At this initial instant the admitted graph is empty, but the field is prepared in the common zero-cost subspace of *all eight* contact costs. The potential gives

\[
W_i(0)=\beta\deg(i),\qquad
\dot u_i(0)=-i\beta\deg(i)a.
\]

Hence, for every contact,

\[
Q_e(0)=\dot Q_e(0)=0,
\quad
\boxed{\ddot Q_e(0)
=\beta^2\big[\deg(f)-\deg(\tau)\big]^2|a|^2.}\tag{7}
\]

Indeed, differentiate \(|u_f-u_\tau|^2/2\) at a zero difference: its second derivative is \(|\dot u_f-\dot u_\tau|^2\). Gate motion does not modify the initial first derivative used here. Core degrees are four, the shared-face degree is two and private-face degrees are one. Thus \(\ddot Q_e(0)=4\beta^2|a|^2\) on two shared-face contacts, and \(9\beta^2|a|^2\) on six private-face contacts. All eight costs immediately become positive for sufficiently small positive time. This is an exact local Taylor statement, not a complete trajectory simulation.

The same initial state gives \(S_e=2|a|^2\), \(\dot p_e(0)=\beta|a|^2\) for every contact. It initiates all gates equally. Subsequent unequal degree-induced costs can differentiate contact classes, but do not establish a unique winner or completion.

## 5. A positive-stock reflection prevents a universal singleton selector

Consider the carrier reflection exchanging vertices \(3\leftrightarrow4\) while fixing \(0,1,2\). On the ordered fields, its signed orthogonal matrix \(P\) fixes face 012, exchanges face pairs \(013\leftrightarrow014\), \(023\leftrightarrow024\), \(123\leftrightarrow124\), and maps the two oriented cores by negative exchange. It obeys

\[
PA_eP^{\mathsf T}=A_{r(e)},
\quad r=(0\ 1)(2\ 3)(4\ 5)(6\ 7).
\tag{8}
\]

The nonzero state \(z=T\mathbf1\), with identical \(q_e,p_e,\beta_e\), is fixed by this reflection exactly, not merely up to a complex phase. Its combined stock is nine and each contact stock is two.

**Theorem G3.** No deterministic selector which is equivariant under this carrier reflection can return exactly one incidence contact on every such positive-stock state.

**Proof.** If \(F\) returned one contact at the displayed fixed state \(X\), equivariance would require \(F(X)=F(rX)=rF(X)\). But (8) has no fixed contact. This is a contradiction. \(\square\)

This is an obstruction to a universal singleton rule, not to local nonexclusive admission, selecting a reflection orbit, or returning an abstention/batch. Nor does it exclude a selector with asymmetric preparation, a supplied orientation/register, or randomness with its own source and receipts. None of those inputs is derived here.

The full candidate ODE is also reflection-equivariant. Local uniqueness therefore preserves the reflection-fixed state space: paired gate trajectories satisfy \(q_e(s)=q_{r(e)}(s)\), \(p_e(s)=p_{r(e)}(s)\). Any first arrival at the on threshold from this preparation comes in at least a reflected pair. An autonomous trajectory cannot manufacture an exact singleton from this exact symmetric preparation while preserving the symmetry assumptions. Perturbed preparations can split paired arrivals; this does not define a robust unique limit at the symmetric state.

**Theorem G4 (independent contact batches).** Impose equivariance also under the carrier rotation \(0\mapsto1\mapsto2\mapsto0\), fixing vertices 3 and 4. The same positive-stock state is fixed by its signed action. On contacts, the group generated by this rotation and the reflection has exactly two orbits: the two shared-face contacts and the six private-face contacts. No nonempty union of these orbits is pairwise disjoint in endpoint support. Consequently, at this state every deterministic equivariant batch of mutually independent primitive contacts is empty.

**Proof.** A batch at a state fixed by the group must be a union of contact orbits. The two shared-face contacts overlap on face 012. The private orbit contains three contacts at each core, so it also has overlaps. Either nonempty orbit, or their union, therefore fails pairwise independence. \(\square\)

This does not exclude a simultaneous joint Hamiltonian event on an overlapping block. The shared orbit spans three complex field coordinates; the private orbit splits into two disjoint stars, each spanning four complex field coordinates. Treating either orbit as one joint event changes the event unit and requires its own source and finite-map receipts. It also does not prove that the unchanged symmetric equations cannot run: they already evolve all overlapping contributions together. The obstruction is to extracting a nonempty *independent primitive-contact scheduler batch* from this state under the stated symmetries.

## 6. Implication for a local robust native selection rule

The complex graph form removes an algebraic ambiguity: combined support is exactly \(|z_i|^2\), and the positive contact cost is a graph difference after the fixed gauge. It does not remove the source obligation identifying the added field as native. Q167's historical two-register notation is not evidence that its registers are these cotangent coordinates; no symbol-based identification is made. This ledger does not supply a complex-support or measurement postulate closing that gap.

A viable next selector must explicitly say what it returns at symmetric states: a compatible batch/orbit, abstention, or a winner determined by a sourced asymmetry. The exact two-contact reflection orbit is not automatically a safe scheduler batch: some reflected contacts overlap on the shared face. Conflict compatibility and the event unit need separate checks. Native single-contact priority, reset, physical units, and particle correspondence remain OPEN.

Fresh exact controls verify the fixed gauge, all 256 forest ranks/kernels and invariant-batch classifications, real/complex field equivalence, gate forces and cut currents, onset leakage, signed reflection covariance and the fixed-state witness. The proofs establish the general results; finite checks are constructor verification. No archived scripts are executed. Independent review pending. Physical promotion 0.
