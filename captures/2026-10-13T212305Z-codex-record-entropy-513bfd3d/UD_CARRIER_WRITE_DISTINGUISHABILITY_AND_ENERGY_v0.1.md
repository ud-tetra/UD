# Carrier write, retained distinguishability and energy

2026-10-13. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Outcome and scope

An explicit candidate unitary writes the exposed-face label of the five-tetrahedron carrier into the previously declared twelve-bit boundary memory. Its readout is perfect from a prepared blank. Its mean energy cost is derived, and the subsequent loss of stored information under the energy-conserving thermal collision model is computed exactly through 32 updates.

This is a source-bound mathematical extension using native face projectors, not a native UD interaction law. The memory tensor factors, Ising coupling J, carrier energy scale epsilon, pulse clock, bath temperature and resource preparation remain declared physical inputs. Ledger G05/G06 are not closed by this calculation. G is unused.

## 1. Explicit write unitary and pulse

Let C be the 47-dimensional chain carrier. Let P_f=|f><f| for its twelve exposed face coordinates, P=sum_f P_f, and Q=I−P. Let M be twelve memory bits with bit flips X_f. Declare

\[
\boxed{U_{\rm w}=Q\otimes I_M+\sum_f P_f\otimes X_f.}
\]

Orthogonal carrier projectors make U_w unitary and self-inverse. For the blank memory |0^12>, an exposed-face basis state |f> writes a single 1 at face f; every interior/complement coordinate writes the blank. All 192512 carrier-memory basis inputs are checked for the write involution.

One formal implementation is a pulse of duration tau with interaction-picture Hamiltonian

\[
K_{\rm w}=\frac{\pi\hbar}{2\tau}\sum_fP_f\otimes(I-X_f).
\]

On each controlled block exp[−i pi(I−X)/2]=X, so exp(−i tau K_w/hbar)=U_w. With free Hamiltonian H_0=H_C+H_M, a laboratory drive K_drive(t)=exp(−iH_0t/hbar) K_w exp(iH_0t/hbar) implements total evolution exp(−iH_0tau/hbar)U_w. The final free evolution changes neither free-energy expectation nor the diagonal memory readout.

This is a driven pulse prescription, not an autonomous controller derived from native dynamics. It requires phase/timing control. The transformed laboratory drive need not retain the apparent locality of K_w. No claim of a two-local or directly implementable physical device is made.

## 2. What information is written

For any carrier density matrix rho and a blank pointer, the reduced memory state after writing is

\[
\rho_M'=p_{\rm out}|0\rangle\langle0|+\sum_f p_f|e_f\rangle\langle e_f|,
\quad p_f=\operatorname{Tr}(P_f\rho),\ p_{\rm out}=\operatorname{Tr}(Q\rho).
\]

The reduced carrier state is the coarse pinching

\[
\mathcal D_R(\rho)=Q\rho Q+\sum_f P_f\rho P_f.
\]

The memory contains thirteen orthogonal outcomes, despite its much larger tensor-product capacity. One single-carrier write does not populate twelve independent binary records and does not close the extensive area-law gap.

To test retained information, introduce a classical reference label R, initially fair, choosing between carrier states |core cell> and |first exposed face>. These are real orthogonal native coordinates. The write produces memory states delta_blank and delta_onehot. Their trace distance is 1, their optimal equal-prior readout error is 0, and I(R:M)=ln2. The classical record entropy is k_B ln2.

For a coherent superposition instead, the write entangles C and M. The full C+M entropy is conserved by the unitary; local record entropy does not thereby establish irreversible thermodynamic entropy production. The reference R in the retention test denotes the label at write time, not the present carrier coordinate after continued native propagation.

## 3. Derived mean energy cost

Declare H_C=i epsilon B_K, with B_K=D^T−D on the five-tetrahedron carrier, and memory Hamiltonian

\[
H_M(m)=2J\,k(m),
\]

where k counts disagreeing adjacent face bits. The boundary dual graph has degree three. The blank has energy zero, and each one-hot face word has energy 6J.

For a blank memory, the mean pointer-energy increase is 6J p_boundary, p_boundary=sum_f p_f. Because native incidence only connects adjacent chain degrees, P H_C P=0. The coarse pinching therefore gives D_R^*(H_C)=QH_CQ. With pulse interaction off at the endpoints,

\[
\boxed{W_{\rm pulse}=6Jp_{\rm boundary}
+\operatorname{Tr}[(QH_CQ-H_C)\rho].}
\]

There is no bath during this ideal write, so this endpoint free-energy change is supplied as work. It includes carrier backaction; it is not generally just the memory cost. For real symmetric rho, the carrier mean-energy change vanishes because H_C is purely imaginary and antisymmetric off-diagonal. Thus the fair binary test has

\[
W_{\rm pulse}=3J.
\]

Complex carrier coherences can change this value or supply extractable work. The expression is a mean cost, not a minimum-work theorem or a bound on pulse-control complexity. Zero carrier mean energy does not make the interaction energy conserving: U_w fails to commute with the free Hamiltonian. The earlier stationary-apparatus covariance obstruction still applies to exact carrier pinching.

The prepared blank is a separate resource. Starting from memory Gibbs state tau_M at finite T, its free-energy increase to the chosen zero-energy pure blank is k_B T ln P(x), x=exp(−2 beta J). This is a necessary preparation-work bound under isothermal work accounting, not a finite exact preparation protocol. A finite full-rank thermal bath cannot perform an exact pure reset of a mixed local memory. Preparation, reset, drive and bath resources must not be omitted from a full-cycle cost.

## 4. Exact retention under the thermal collision model

After the write, decouple the carrier. Apply the previous memory collision kernel: choose one site uniformly and replace its bit by the Gibbs conditional probability, using independent fresh bath qubits with gaps 2J and 6J. At x=1/3 the two excited-state probabilities are 1/4 and 1/28. Every transition has denominator 336 after uniform site selection. The replay propagates both conditional memory distributions with integer weights, then reports exact rational trace distances and energy means.

For diagonal states, trace distance equals total variation. The optimal equal-prior error is

\[
D_r=\frac12\sum_m|p_r(m|0)-p_r(m|1)|,
\qquad P_{\rm err}^{\rm opt}(r)=\frac{1-D_r}{2}.
\]

The error formula follows by choosing the more likely label for each full memory word. Information is

\[
I(R:M_r)=\frac12\sum_{a=0}^1\sum_m p_r(m|a)
\ln\frac{2p_r(m|a)}{p_r(m|0)+p_r(m|1)}.
\]

The reference information and D_r cannot increase under a common memory-only channel. The code checks exact monotonicity of D_r at every update through 32.

| Updates | Full-memory distinguishability D | Optimal error | I(R:M), nats | Cumulative mean bath heat / J |
|---|---:|---:|---:|---:|
| 0 | 1 | 0 | ln2 | 0 |
| 1 | 11/12 | 1/24 | 0.541623 | 0 |
| 2 | 0.841234 | 0.079383 | 0.451359 | −0.006803 |
| 4 | 0.711386 | 0.144307 | 0.333798 | −0.036129 |
| 8 | 0.526517 | 0.236741 | 0.203173 | −0.135159 |
| 16 | 0.334253 | 0.332874 | 0.090847 | −0.398533 |
| 32 | 0.177707 | 0.411147 | 0.028799 | −0.923548 |

All D and heat values are exact rationals in results.json; decimals in the table are display values. Information decimals are evaluations of the stated logarithm formula, not certified interval estimates.

At one update the conditional memory energy means are exactly 3J/14 and 81J/14. The mean stays 3J. The blank branch absorbs 3J/14 from its bath; the one-hot branch releases 3J/14, so their mean heat cancels even though information decreases. Thus mean heat alone does not measure record loss.

The one-step information is also expressible exactly as

\[
I_1=\ln2-\frac{117}{224}h(1/13)-\frac{281}{672}h(1/281).
\]

Every spin flip and every self-loop is positive. Any memory word can reach any other within twelve update steps, padding a flip path with self-loops. Each chosen transition has probability at least 1/336, giving

\[
P^{12}(m,t)\ge336^{-12},\quad
\alpha=4096/336^{12},\quad
D_r\le(1-\alpha)^{\lfloor r/12\rfloor}.
\]

This deliberately conservative minorization proves eventual loss: D_r tends to zero, error tends to 1/2, and reference information tends to zero. Both labels converge to the same memory Gibbs state. Its mean energy is 11J/2 at this replay point, so the long-time cumulative mean bath heat is −5J/2: the memory gains heat while losing the recorded label.

Uniform site selection can be accounted for by a fresh degenerate twelve-state control in its uniform thermal state, included with the bath. The selected-site controlled collision then conserves memory+bath+control energy. Omitting that control when applying a microscopic entropy identity would omit possible correlations. This does not derive autonomous scheduling or free bath renewal.

With bath collisions disabled, the diagonal Ising Hamiltonian preserves the pointer words exactly. Under this closed-memory model D=1 indefinitely. This is a conditional isolation result; disconnecting the bath, omitted noise, and physical retention are source questions.

## 5. Fidelity–cost comparison without a pure blank

Apply the same controlled bit flip to a memory initially in the full correlated Gibbs state, independently of the fair binary input. The two pointer states are tau_M and X_f tau_M X_f. Exact enumeration gives

\[
D=51/64,\qquad P_{\rm err}^{\rm opt}=13/128,
\qquad W_{\rm pulse}=\frac{25}{12}J.
\]

The three neighbors are all equal with Gibbs probability 133/192; otherwise their majority gap is 2J. Thus

\[
I(R:M)=\ln2-\frac{133}{192}h(1/28)-\frac{59}{192}h(1/4)
\approx0.413616.
\]

The Gibbs pointer writes genuine but imperfect carrier information at lower pulse work than the pure-blank case. It avoids assuming exact pure preparation. Under subsequent relaxation its memory energy returns to equilibrium, releasing mean heat 25J/12 as the reference information vanishes. At infinite temperature the Gibbs state is uniform and invariant under X_f, so this write records no label at all. Pointer preparation is therefore a fidelity resource, not only an energetic convention.

## Disposition

CHECKED under declared mathematics: projector-controlled write and pulse; pointer statistics; mean work including carrier backaction; exact blank-vs-Gibbs fidelity/cost; finite-step retained distinguishability; eventual thermal erasure.

OPEN: a native UD source for this interaction, energy/clock calibration, drive/blank/bath preparation and renewal, physical error model, logical retention code, many-write extensive boundary state, refinement consistency and causal horizon. No registry, ledger, repository or website was updated. Physical promotion 0; independent review OPEN. Gap2_FINAL_Finite_Genesis.png was unavailable and unused.

Next gate: optimize a declared retention criterion against full-cycle resources, and derive a source-selected autonomous write/control rule. A positive recorded mutual information now exists in this candidate, but neither it nor the Ising entropy establishes a gravitational area law.
