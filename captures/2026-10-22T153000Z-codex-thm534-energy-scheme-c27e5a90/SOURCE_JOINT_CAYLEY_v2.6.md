# THM-534: local joint Cayley lift and the full-energy limit

Development — no registry entry. Exact conditional finite-map construction for the v2.4/v2.5 candidate. Constructor checked; independent review pending. Physical promotion 0.

## 1. Purpose and fixed model

The preceding symmetry obstruction concerns selecting an independent primitive contact. It does not prohibit a joint overlapping event. This construction supplies a local canonical finite map for such a block, while preserving its distinction from the continuous full Hamiltonian. It introduces no new physical identification or claim of a native event-priority rule.

Use the v2.5 fixed unitary gauge \(u=T^\dagger(x+iy)\). On a block \(B\) of contacts define

\[
L_B(q)=\sum_{e\in B}\big[\chi_e(q_e)c_ec_e^{\mathsf T}+U_e(q_e)P_e\big],
\quad c_e=\mathbf e_f-\mathbf e_\tau,
\quad U_e=\frac{2\beta_e}{1+(q_e+1)^2}.
\tag{1}
\]

The candidate field Hamiltonian of the block is \(E_B=u^\dagger L_Bu/2\). All matrices in (1) act only on the block's endpoint coordinates. Gate positions are frozen during the finite field map. The model parameter step \(\varepsilon>0\), profile, charge and event unit remain supplied; no action/time calibration is made.

## 2. Fixed topological blocks on the two-cell carrier

Use contact indices from v2.5. A carrier-invariant decomposition is

| Block | Contacts | Complex field coordinates | Gate pairs |
|---|---|---|---|
| Shared-face star \(B_S\) | \(0,1\) | \(0,7,8\) | 2 |
| Private star at \(\tau_0\), \(B_0\) | \(2,4,6\) | \(1,3,5,7\) | 3 |
| Private star at \(\tau_1\), \(B_1\) | \(3,5,7\) | \(2,4,6,8\) | 3 |

The shared block is invariant under carrier automorphisms. The two private blocks are interchanged by cell reflection and form an unordered pair. They have disjoint field coordinates and disjoint gates, so their full lifted maps commute. Each block has bounded footprint on this carrier: respectively 10 or 14 real canonical coordinates, including field components and gates. The private pair has no preferred internal order. The shared block overlaps both private blocks, so no universal commutation or priority is asserted for those pairs.

This is a state-independent topological decomposition, not an equal-stock tie clustering rule. Small stock perturbations do not change these blocks. Choosing which block or block family runs next, its event duration, and charging/reset semantics are still open. Local boundedness here is not a theorem for arbitrary larger automorphism orbits or arbitrary nonmanifold face valence.

## 3. A joint finite map with the required gate kick

Put \(a=\varepsilon/2\), \(C=I+iaL_B\), and define

\[
R_B=C^{-1}(I-iaL_B),\qquad
u'=R_Bu,\quad q'=q,\quad
m=\frac{u+u'}2=C^{-1}u.
\tag{2}
\]

Write \(L_{B,e}=\partial L_B/\partial q_e\). The lifted gate update is

\[
\boxed{p'_e=p_e-\frac\varepsilon2 m^\dagger L_{B,e}m
=p_e-\varepsilon\left[
\frac{\chi'_e}2|m_f-m_\tau|^2+
\frac{U'_e}2(|m_f|^2+|m_\tau|^2)
\right],\quad e\in B.}
\tag{3}
\]

Other gate momenta are unchanged. **Theorem J1.** Equations (2)–(3) are a canonical transformation of the real field components and all included gate pairs, preserve combined field norm, and preserve \(E_B\) at fixed \(q\).

**Proof.** Hermiticity of \(L_B\) gives unitarity of \(R_B\), and \(R_B\) commutes with \(L_B\). Thus norm and \(u^\dagger L_Bu\) are preserved. Differentiating the resolvent without assuming \([L_B,L_{B,e}]=0\) gives

\[
\partial_eR_B=-i\varepsilon C^{-1}L_{B,e}C^{-1},
\quad
R_B^\dagger\partial_eR_B
=-i\varepsilon(C^{-1})^\dagger L_{B,e}C^{-1}.
\tag{4}
\]

Use the symmetric canonical one-form

\[
\lambda=-\frac12\operatorname{Im}(u^\dagger du)+\sum_ep_e\,dq_e.
\]

The field pullback adds \(-\tfrac12\operatorname{Im}(u^\dagger R_B^\dagger\partial_eR_Bu)\,dq_e\). Its coefficient is \(+\varepsilon m^\dagger L_{B,e}m/2\), since the quadratic form is real. The momentum kick (3) cancels it exactly. Hence \(\lambda'=\lambda\), proving symplectic preservation. This includes all mixed gate derivatives and does not require commuting contact terms. \(\square\)

The expression is a full block resolvent: multiplying individual contact Cayley maps generally gives a different transformation when their field supports overlap. A joint event must be declared as such.

## 4. Exact local midpoint receipts

Equation (2) is equivalent to

\[
u'-u=-i\varepsilon L_Bm.
\]

For each contact, define the finite combined-support transfer

\[
\boxed{\mathcal J_e=2\varepsilon\chi_e\operatorname{Im}(\overline m_fm_\tau).}\tag{5}
\]

The diagonal potential contributes no change to squared modulus at an individual coordinate. Thus

\[
|u_f'|^2-|u_f|^2=-\sum_{e\ni f}\mathcal J_e,
\quad
|u_\tau'|^2-|u_\tau|^2=\sum_{e\ni\tau}\mathcal J_e.
\tag{6}
\]

Boundary cuts and fixed ownership weights can be summed algebraically from (6). These are the candidate combined complex-support receipts, not the unchanged original real-only support law. Equation (3) is the midpoint quadratic gate-force receipt paired with the same field event.

## 5. Robust field map without stock-tie discontinuity

For Hermitian \(L,M\) and fixed \(\varepsilon\),

\[
R(L)=2(I+iaL)^{-1}-I,
\quad
\boxed{\|R(L)-R(M)\|\le\varepsilon\|L-M\|.}\tag{7}
\]

**Proof.** The resolvent identity gives

\[
R(L)-R(M)=-i\varepsilon(I+iaL)^{-1}(L-M)(I+iaM)^{-1}.
\]

Both inverse norms are at most one for Hermitian input. \(\square\)

In particular,

\[
\|R(L)u-R(M)v\|\le\|u-v\|+
\varepsilon\|L-M\|\,\|v\|.
\tag{8}
\]

For a fixed topological block the momentum kick is a smooth quadratic expression in the field and a smooth rational/profile expression in gate parameters. It is locally Lipschitz on bounded preparation sets; no global state-independent bound for its quadratic dependence is claimed. Equal support stocks do not merge or split these fixed blocks. This controls the map *after a block is supplied*. It does not prove continuity of an unsupplied discrete priority selector.

## 6. Symplectic substep is not a full-energy integrator

Even for a standalone block with full Hamiltonian \(H_B=\sum p_e^2/2+E_B\), only its frozen field term is conserved here. If \(\Delta p=p'-p\),

\[
\boxed{\Delta H_B=\sum_ep_e\Delta p_e+
\frac12\sum_e(\Delta p_e)^2.}\tag{9}
\]

For a block inside the full network, field changes can also alter the other blocks' energy terms. There is therefore no transfer of the continuous all-time \(H_+\) bound to a repeated sequence of these finite maps. A canonical free-flight step \(q'=q+\varepsilon p\) can be composed with them, but neither its full-energy conservation nor a completed stable integrator is claimed.

An exact shared-block countercontrol takes \(\varepsilon=1/4\), \(\beta_0=\beta_1=1\), \(q=p=0\), and \(u=(1,1,1)\) on face/core coordinates \((0,7,8)\). Then \(L_B=\operatorname{diag}(2,1,1)\), and

\[
u'_0=\frac{15-8i}{17},\quad
u'_7=u'_8=\frac{63-16i}{65},
\qquad p'_0=p'_1=\frac{266}{1105}.
\]

The frozen field energy stays 2, while the full block energy increases by

\[
\boxed{\Delta H_B=\frac{70756}{1221025}>0.}\tag{10}
\]

Here \(u'\) is the same field as in (2). The two gate kicks are equal, so the exact map preserves reflection symmetry and does not create a spurious singleton. Omitting the kick would remove this kinetic increment but would generally violate the canonical pullback.

## 7. Source synchronization and remaining obligations

The research branch advanced to `8bb4fba13966f277e42422152379850adbf61930` during this turn. Its new cumulative note explicitly retains source-open selection, reset and physical bridges. The current v1.2 manifest now records the correct 64-digit Fraction receipt SHA-256 ending `aaa56b9b`; the earlier malformed manifest is preserved in history. Release ZIPs are now indexed as present upstream. This turn inspected the new note and manifest as data and did not download/hash every ZIP or execute archived replay scripts. It does not claim to complete a ZIP byte audit.

A bounded symmetry-respecting joint block now has an exact canonical map, norm/current receipts and conditional robustness, but the native block-priority source, units, gate/dual carrier and reset remain open. The finite map's full-energy defect is a separate integrator obligation. This mathematical construction does not derive quark/lepton identities or a physical action quantum. Independent review remains pending. Physical promotion 0.
