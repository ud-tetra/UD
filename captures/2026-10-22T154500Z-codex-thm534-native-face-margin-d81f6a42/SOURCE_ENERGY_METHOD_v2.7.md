# THM-534: full-energy and norm-preserving scheme with certified root receipts

Development — no registry entry. Conditional numerical-method construction for the existing positive candidate model. Constructor checked; independent review pending. Physical promotion 0.

## 1. Fixed Hamiltonian and the integration gap

The v2.6 canonical block map preserves frozen field energy but can add gate kinetic energy. This alternative numerical method targets the *complete* v2.4 Hamiltonian without changing the continuous equations:

\[
H(u,q,p)=\frac12\sum_ep_e^2+\frac12u^\dagger L(q)u,
\quad
L(q)=\sum_e[\chi_e(q_e)c_ec_e^{\mathsf T}+U_e(q_e)P_e],
\tag{1}
\]

where \(c_e=\mathbf e_f-\mathbf e_\tau\), \(U_e(q)=2\beta_e/[1+(q+1)^2]\), and \(\chi\) is the supplied quintic plateau. For fixed \(u\), write

\[
Q_e=\frac12|u_f-u_\tau|^2,\quad
S_e=|u_f|^2+|u_\tau|^2,\quad
V_e(q;u)=\chi_e(q)Q_e+\frac12U_e(q)S_e.
\tag{2}
\]

All stores are nonnegative. The canonical continuous equations are \(i\dot u=L(q)u\), \(\dot q=p\), \(\dot p_e=-\partial_qV_e\). The native status of the complex carrier, potential, charge and gate units is unchanged: CANDIDATE. This is a solver, not a new native law.

## 2. Two individually conservative substeps

Take a numerical step \(h>0\); negative steps define the inverse when discussing reversibility.

**Field substep \(F_\tau\).** Hold \(q,p\) fixed and apply the full-field Cayley map

\[
u^+=(I+i\tau L(q)/2)^{-1}(I-i\tau L(q)/2)u.
\tag{3}
\]

It preserves \(N=\|u\|^2\) and full \(H\), because its unitary matrix commutes with the *full* frozen \(L(q)\). Unlike v2.6, no gate kick is applied in this substep. It is not canonical on the combined field/gate phase space.

**Gate substep \(G_h\).** Hold \(u\) fixed. For every contact simultaneously, set \(a=q_e\), \(b=q_e^+\), \(r=p_e\), \(s=p_e^+\), and solve

\[
\boxed{b-a=h\frac{s+r}{2},\qquad
s-r=-hD_e(a,b),}\tag{4}
\]

where the divided difference is

\[
D_e(a,b)=\begin{cases}
[V_e(b;u)-V_e(a;u)]/(b-a),&b\ne a,\\
V'_e(a;u),&b=a.
\end{cases}\tag{5}
\]

This is a scalar nonlinear equation for each gate; overlap of field supports does not couple these scalar solves when \(u\) is held fixed. Multiplying the two equations in (4) gives

\[
\frac{s^2-r^2}{2}+V_e(b;u)-V_e(a;u)=0.
\tag{6}
\]

Thus \(G_h\) preserves full \(H\) and field norm. The diagonal definition in (5) is needed even if \(a=b\).

The vector fields approximated by these substeps sum to the full continuous candidate: the field part moves only \(u\), the gate part moves only \(q,p\). Each part separately has zero derivative of (1); neither is asserted to be a canonical Hamiltonian split on the full phase space.

## 3. A unique gate root under a checkable step bound

Eliminate \(s\) in (4). The scalar residual is

\[
\mathcal F(b)=b-a-hr+\frac{h^2}{2}D_e(a,b).
\tag{7}
\]

**Theorem E1.** With the fixed field in this gate substep, define

\[
M_e=15Q_e+2\beta_eS_e,
\qquad B_e=\frac{15}{8}Q_e+\beta_eS_e.
\tag{8}
\]

If \(h^2M_e<4\), there is exactly one root of (7), and it lies in

\[
\boxed{a+hr-\frac{h^2B_e}{2}
\le b\le a+hr+\frac{h^2B_e}{2}.}\tag{9}
\]

**Proof.** The profiles satisfy \(|\chi'|\le15/8\), \(|\chi''|\le15\), \(|U'|\le2\beta_e\), and \(|U''|\le4\beta_e\). For the rational profile the last inequality follows, with \(z=(q+1)^2\ge0\), from \(|1-3z|\le(1+z)^3\). Hence \(|V'_e|\le B_e\), \(|V''_e|\le M_e\). The integral representation

\[
D_e(a,b)=\int_0^1V'_e(a+t(b-a))\,dt
\]

gives \(|D_e|\le B_e\) and \(|\partial_bD_e|\le M_e/2\). Therefore \(\mathcal F'(b)\ge1-h^2M_e/4>0\). The linear term in (7) and bounded divided difference imply opposite infinite limits. The interval (9) has nonpositive/ nonnegative residual at its endpoints, so it brackets the unique root. \(\square\)

For every contact \(Q_e\le S_e\le N\). Thus the uniform sufficient condition

\[
\boxed{h^2(15+2\beta_{\max})N<4}\tag{10}
\]

can be checked from the initial norm and fixed charges, before any physical target exposure. It is an algorithmic step restriction, not a derived physical clock or action unit. If \(N=0\), gate motion is free and (7) is linear. Using a stronger fixed bound or a declared margin away from equality avoids root-conditioning ambiguity.

## 4. Symmetric full step and exact invariant bound

Compose

\[
\boxed{\Phi_h=F_{h/2}\circ G_h\circ F_{h/2}.}\tag{11}
\]

Here the rightmost field step uses the old gate positions and the leftmost uses the new positions. The field after the first half-step is held fixed throughout all gate solves.

**Theorem E2.** With exact roots and the per-gate bounds of E1 (in particular, (10)), (11) is a uniquely defined complete one-step update on the finite carrier. It preserves \(N\) and the complete \(H\), including all overlapping contact terms. It is time reversible. Every sequence of such exact accepted steps satisfies

\[
0\le K_n,V_n,R_n\le H_0,
\qquad \sum_ep_{e,n}^2\le2H_0.
\tag{12}
\]

**Proof.** Both substeps conserve the same two invariants, so their composition does too. Positivity of (1) gives (12). Cayley inversion sends \(F_h\) to \(F_{-h}\). Swapping endpoints in (4) and changing \(h\) to \(-h\) gives the inverse gate step; uniqueness selects it. The symmetric composition is therefore reversible. \(\square\)

On smooth profile regions this method is second-order consistent: the field Cayley map matches its frozen exponential through quadratic order; (4) gives \(b-a=hr-h^2V'(a)/2+O(h^3)\) and \(s-r=-hV'(a)-h^2V''(a)r/2+O(h^3)\). Expanding the symmetric composition yields the full continuous equations through quadratic order. No untested global convergence order across profile-boundary crossings is claimed. Invariant preservation does not by itself guarantee small trajectory error or correct threshold-crossing times.

This step uses the full coupled field resolvent. Sparsity of \(L\) does not make its inverse a bounded-support native contact event. Substituting one local block in (3) generally loses full-H preservation through the other blocks. The construction therefore fills an integration gap on the finite model; it does not supply a local event scheduler or native selection principle.

## 5. Numerical roots receive an explicit energy receipt

Finite bisection does not generally produce an exact root. For a chosen rational approximation \(\widetilde b\), enforce kinematics exactly by

\[
\widetilde s=2(\widetilde b-a)/h-r.
\]

With \(\rho=\mathcal F(\widetilde b)\), its exact gate energy defect is

\[
\boxed{\eta_e=\frac{\widetilde s^2-r^2}{2}+V_e(\widetilde b)-V_e(a)
=\frac{2(\widetilde b-a)}{h^2}\rho.}\tag{13}
\]

Both full-field maps still conserve the energy at their frozen positions. Hence, for exactly computed rational Cayley maps, the full computed step satisfies

\[
H_{n+1}-H_n=\sum_e\eta_{e,n},
\qquad
K_n,V_n,R_n\le H_0+\sum_{k<n,e}|\eta_{e,k}|.
\tag{14}
\]

A root bracket \([b_-,b_+]\) gives the midpoint error \(|\widetilde b-b_*|\le(b_+-b_-)/2\), and the kinematically defined momentum error is at most \((b_+-b_-)/|h|\). A finite solver must record both its root bracket and its force residual, not merely a small energy defect: energy can coincide accidentally even at a wrong root. Floating field linear solves would require their own additional residual receipt; the accompanying implementation uses exact Gaussian-rational elimination.

## 6. A full-step obstruction to claiming canonical preservation

For a single gate step, write \(D_a=\partial_aD\), \(D_b=\partial_bD\). Implicit differentiation of (7) gives the determinant on \((a,r)\):

\[
\boxed{\det D G_h=\frac{1+(h^2/2)D_a}{1+(h^2/2)D_b}.}\tag{15}
\]

It is generally not one for a nonquadratic potential. Each field half-step has real Jacobian determinant one on the full variables: it is triangular in field/gate blocks, its real field Jacobian determinant is \( |\det R|^2=1 \), and \(q,p\) are unchanged. Each gate map is triangular with identity field block. Thus a nonunit determinant in (15) also obstructs symplecticity of the full composition; it cannot be dismissed as just a substep artifact.

An exact isolated preparation uses \(u_f=u_\tau=1\), hence \(Q=0,S=2\), \(\beta=1/2\), \(a=0\), \(r=16/41\), \(h=1/2\). The local root bound is \(h^2M=1/2<4\). Both field half-steps preserve this common-mode field up to a phase, so the gate potential is

\[
V(q)=\frac1{1+(q+1)^2}.
\]

The exact gate solution and derivatives are

\[
b=\frac14,\quad s=\frac{25}{41},\quad
D=-\frac{18}{41},\quad D_a=\frac{10}{41},\quad D_b=\frac{392}{1681}.
\]

Both endpoint energies are \(1937/3362\), while the *full-step* determinant is

\[
\boxed{\det D\Phi_h=\frac{6929}{6920}\ne1.}\tag{16}
\]

This supplies the promised tradeoff: energy/norm conservation of the completed method is exact in its mathematical definition, but canonical preservation is not. No general no-go against all energy-preserving symplectic algorithms is inferred; this is a countercontrol for the displayed method.

## 7. Verification and remaining source boundary

Fresh exact arithmetic checks frozen field invariants and contact receipts, global gate derivative bounds, unique-root brackets, scalar energy/residual identities, a complete overlapping-carrier step with certified root intervals, and the exact noncanonical full-step witness. Numerical root approximations are reported separately from the exact mathematical conservation theorem. No archived scripts are executed.

The positive candidate now has a complete energy-accounted finite scheme, conditional on its supplied carrier and potentials. Canonical finite integration, native bounded-locality scheduling, event time, charging/reset, native complex-support identification and physical particle correspondence remain OPEN. No physical action quantum is derived. Independent review pending. Physical promotion 0.
