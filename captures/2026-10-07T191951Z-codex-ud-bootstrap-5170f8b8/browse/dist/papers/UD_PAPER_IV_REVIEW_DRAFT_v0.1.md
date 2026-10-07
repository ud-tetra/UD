---
title: "Finite Prepared Quantum Controllers, Capture Windows and Correlation-Preserving Renewal"
subtitle: "Paper IV - Development draft 0.1"
author: "Benjamin Walker Mayes"
date: "4 October 2026"
---

**Independent researcher**  
ORCID: [0009-0002-5813-0724](https://orcid.org/0009-0002-5813-0724)

**Edition status.** A mathematical development draft for independent review. This paper consolidates the prepared mechanisms PT11-PT16, previously summarized in Paper III Section 13, without changing their source premises. Finite apparatus is supplied. No empirical validation, native preparation, local implementation or complete autonomous cycle is established. Physical promotion: zero. Independent human review: pending.

## Abstract

We formulate complete joint-system contracts for finite history controllers, capture and matched-register renewal. A supplied gate word is implemented by prefix dressing of an engineered perfect-transfer clock; its native/comparator mismatch is charged over the whole propagation interval. Coherent binary fuel produces a finite reference packet by energy-preserving exchanges, while stationary complete inputs under covariant processing obey a sharp preparation obstruction. A supplied timed terminal exchange protects output after pulse-off under a factorized background. A separate constant post-launch Hamiltonian supplies a finite retention interval, with a complete joint bound distinguished from its smaller marginal error. Matched renewal exports old correlations into a retained donor register; whole-bank supply admission and unconditional telescoping bounds prevent marginal-fidelity and postselection discounts. We state finite exhaustion, recurrence, energy conventions, implementation debits and acquisition limitations explicitly. These are conditional operator constructions, not a derivation of native apparatus or permanent autonomous storage.

# 1. Question, contribution and established ingredients

The question is whether a finite prepared controller can execute a supplied word, export its output and replace its consumed module while preserving a complete account of errors, energy and correlations. A propagation Hamiltonian, a capture operation, and the supply/trigger/router that repeats them are different objects. We construct the first two conditionally and state a finite renewal identity. We do not infer the third from their composition.

Engineered perfect state transfer is established prior art. Christandl et al. [1, Eqs. (13)-(15)] use a spin representation of a chain with square-root couplings. Our clock has $n+1$ addresses and corresponds to their $N=n+1$ sites with their rate parameter $2\kappa$. Prefix-dressed history propagation is a standard circuit-to-Hamiltonian ingredient. Caha, Landau and Nagaj [2, Sections 2 and 4] study history clocks and idling; their Theorem 2 concerns amplified ground-state history weight, whereas the retention estimate here is a real-time comparison on a supplied finite spin clock. We claim neither a new perfect-transfer principle nor the general history-clock construction.

Finite-clock resource and backreaction analysis has a substantial existing literature, including Woods, Silva and Oppenheim [3]. Their Quasi-Ideal clock is a different construction; no equivalence or superiority theorem is established here. Lostaglio and Mueller [4, Theorem 1] prohibit coherence broadcasting under their finite-reference covariant contract. Our fuel is consumed and renewal uses fresh donors; retaining an outgoing correlated donor is not an unchanged coherence catalyst. Unitary flag premeasurement is standard [5]. Duhamel estimates, swap identities and finite-dimensional analyticity are also established mathematical ingredients.

The contribution of this draft is a coordinated, source-traceable set of conditional contracts: actual native operators remain distinct from comparators; timed and static capture have different storage guarantees; complete joint error includes clock and spectator; renewal preserves exported correlations; and finite resource admission is charged at its full-bank domain. A comprehensive theorem-level novelty assessment is pending. The proofs below are supplied to make the stated comparisons reviewable, not to establish a priority claim.

Paper I supplies finite tetrahedral chain conventions, Paper II distinguishes complete receipts from incomplete observations, and Paper III supplies the operator comparisons in which these mechanisms arose [6]. None is a proof that the apparatus defined here occurs natively. Our Hilbert spaces are arbitrary declared finite carriers; apparatus address dimensions are not new spatial dimensions.

# 2. Joint domains, distances and error ownership

All spaces in this paper are finite-dimensional complex Hilbert spaces. Tensor identities are suppressed when their domain is declared. Hamiltonians are Hermitian. We use $\hbar=1$ as a mathematical convention; no laboratory unit or action normalization is inferred. The operator norm is $\|A\|=\sup_{\|v\|=1}\|Av\|$. For states,
\[
D_{\rm tr}(\rho,\sigma)=\frac12\|\rho-\sigma\|_1\in[0,1].
\]
A joint state includes every named register and arbitrary spectator $Y$, possibly correlated with the active body. Any free spectator dynamics is common to actual and comparison channels. A marginal statement explicitly names the traced registers. Probabilities, state distances and Hamiltonian norms have different types.

The work module is $W=(S,R,F)$: source bank $S$, reference $R$ and fuel $F$. Production clock $C$ has $n+1$ addresses. Capture adds a matched output bank $O$ and degenerate flag $L$; optional degenerate memory/witness registers are $M,E$. Static capture adds address clock $Q$ of dimension $N+1$. Donor $D$ matches the complete module being exchanged. $Y$ includes prior outputs, records, waste and every retained external correlation.

Matched means equal carrier dimensions and equal bare energy operators under the declared identification. It is stronger than equal mean energy. A blank output or fresh donor state is a supplied resource, not a state created by exchange.

**Lemma IV.1 (joint perturbation).** If $H,K$ are Hermitian and $\|H-K\|\le d$, then for any $t\ge0$,
\[
\|e^{-itH}-e^{-itK}\|\le td,
\quad D_{\rm tr}(U_H\rho U_H^\dagger,U_K\rho U_K^\dagger)\le\min\{1,td\},
\]
including arbitrary spectator extensions. For a time-dependent extra contact $V(u)$ on the same domain, replace $td$ by $\int_0^t\|V(u)\|\,du$.

*Proof.* Duhamel writes the propagator difference as an integral of unitary factors around $H-K$; submultiplicativity bounds it by $td$. On a purification, the vector difference has that bound, and pure-state trace distance is at most vector distance. Reduction contracts trace distance. The time-dependent proof uses the corresponding propagator identity. $\square$

If an event projector $P$ annihilates the comparison vector, its actual probability is at most $\min\{1,(td)^2\}$ on that purification. If comparison event amplitude is at most $a$, the actual probability is at most $\min\{1,(a+td)^2\}$. An initial full-joint state discrepancy instead changes any event probability by at most its trace distance; it is not automatically an amplitude-square debit.

All budgets below refer to a fixed pair of actual and ideal contracts. Additional supplied-state, contact, thermal, detector, storage and implementation errors must be admitted on matching domains. Shared errors are charged once, not repeated for each marginal or each quoted diagnostic.

# 3. Finite reference and coherent binary fuel

## 3.1 Source operator and finite shift margins

The source packages [7-9] use an actual oriented-ring spectrum $E_k=2J\sin(2\pi k/K)$, a prepared packet, a declared cutoff and tail probability $q_b$. A comparator $\bar E_k=\Delta a_k$ on the admitted cutoff uses certified integer labels; outside that cutoff it agrees with the actual operator. A source cell mismatch is bounded by $\Delta/2$, so for $m$ admitted cells a sufficient work mismatch is $d\le m\Delta/2$. This is an assumption/certificate of that source example, not a property of every Hamiltonian. The actual $H_S$ is never rounded.

Let $C_* =\max|a_k|$. To avoid collision with clock $C$, we write the source's shift margin as $C_*$. A finite ladder has
\[
M_R=L+2(m+1)C_*,\qquad n_0=(m+1)C_*,\qquad H_R=\Delta\sum_{a=0}^{M_R-1}a|a\rangle\langle a|.
\]
The packet occupies $n_0,\ldots,n_0+L-1$. Up to $m+1$ shifts of magnitude at most $C_*$ remain inside the declared window. Every gate extension outside its disjoint admitted exchange pairs is specified separately; reference wraparound is not used. The native receipt determining these shifts and packet coefficients is supplied.

The parent source's isolated production overlap yields a full source/reference bank bound
\[
\eta_{\rm bank}=\sqrt{1-(1-q_b)^m A_m^2},\qquad
A_m\ge\left(1-\frac{m\mu}{L}\right)_+,
\]
where $\mu$ and the signed-word overlap $A_m$ have their source definitions [7-8]. This is an inherited certificate, not newly proved for arbitrary interleaved contacts. A later contact on the same reference, fuel or clock needs its integrated joint channel bound. Isolation is an explicit dependency.

## 3.2 Energy-preserving producer

**Theorem IV.2 (binary fuel; PT12 producer).** Let $L=2^q$, $\Delta>0$, and supply independent fuel qubits $F_j$ in $|+\rangle$, with $H_{F_j}=\Delta2^j|1\rangle\langle1|$. Supply reference seed $|n_0\rangle$. There are disjoint energy-preserving exchanges that send
\[
|+\rangle_F^{\otimes q}|n_0\rangle_R\longmapsto
|0\rangle_F^{\otimes q}|\eta_L\rangle_R,\qquad
|\eta_L\rangle=\frac1{\sqrt L}\sum_{r=0}^{L-1}|n_0+r\rangle.
\]
The seed energy $n_0\Delta$ and all fuel coherence are inputs.

*Proof.* At step $j$ pair $|1\rangle|n_0+r\rangle$ with $|0\rangle|n_0+r+2^j\rangle$ whenever the $j$th bit of $r$ is zero in the declared packet block. Pairs are disjoint, preserve the sum of the two bare energies, and define a unitary permutation with identity on the complement. By induction, before step $j$ the populated reference labels are $r=0,\ldots,2^j-1$, so the current bit is zero. The next exchange doubles the uniform reference support and leaves fuel bit $j$ in ground state. After $q$ steps every binary label occurs once. $\square$

For the bit rule write $r=2^{j+1}u+v$ and $r\equiv v\pmod{2^{j+1}}$, with $0\le v<2^j$. Transfer replaces $v$ by $v+2^j$ on the declared pair. The modulus is a power of the prime 2. This rule defines pairs, not a recycling reservoir.

For ideal independent fuel, elementary geometric sums give
\[
\langle H_F\rangle=\frac{\Delta(L-1)}2,\qquad
\operatorname{Var}H_F=\frac{\Delta^2(L^2-1)}{12}.
\]
For a pure state and the specified time-translation generator, $F_Q=4\operatorname{Var}H_F$. Correlated pure fuel requires the variance of the complete sum, including covariance terms. For mixed fuel this equality is not generally valid. Arbitrary correlated fuel is transformed to its corresponding joint output; the producer does not replace it by an ideal independent packet.

## 3.3 Stationary complete-supply limitation

**Theorem IV.3 (stationary supply; PT12 obstruction).** Let the complete input be stationary under a declared additive total free-energy generator. Let the complete production channel be covariant for its input/output generators, and let the output reference generator have nondegenerate packet energies $(n_0+r)\Delta$, $\Delta>0$. Its reduced reference $\omega_R$ then obeys
\[
D_{\rm tr}(\omega_R,|\eta_L\rangle\langle\eta_L|)\ge1-\frac1L.
\]

*Proof.* Covariance preserves total stationarity. Partial trace under an additive output generator leaves a stationary reference. Its matrix is diagonal in the nondegenerate energy basis, so $\langle\eta_L|\omega_R|\eta_L\rangle=L^{-1}\sum_{r=0}^{L-1}(\omega_R)_{n_0+r,n_0+r}\le1/L$. The two-outcome measurement of the target projector gives the distance lower bound. The uniform diagonal packet has eigenvalues $1/L$ on the packet block; its difference from the pure uniform packet has trace norm $2(1-1/L)$, attaining the bound. $\square$

Any coherent fuel, reference, interacting controller or spectator that breaks complete stationarity must be counted. The theorem does not forbid preparation from admitted nonstationary resources, nor does it give a universal approximate-QFI cost. Degeneracy across packet energies would invalidate the diagonal step and requires a different statement.

# 4. Supplied history word and finite clock

Supply gates $U_1,\ldots,U_n$ commuting with a comparison work Hamiltonian $\bar H_W$. Define prefixes $P_0=I$, $P_j=U_j\cdots U_1$, and
\[
\mathcal W=\sum_{j=0}^n|j\rangle\langle j|_C\otimes P_j,
\quad H_C=\kappa\sum_{j=0}^{n-1}\sqrt{(j+1)(n-j)}
 (|j+1\rangle\langle j|+|j\rangle\langle j+1|),
\]
with $\kappa>0$. Let $H_p=\mathcal W(H_C\otimes I)\mathcal W^\dagger$ and
\[
H_{\rm act}=I_C\otimes H_W+H_p,\qquad
H_{\rm comp}=I_C\otimes\bar H_W+H_p,
\quad \|H_W-\bar H_W\|\le d.
\]
Gate-dependent hopping edges contain $U_j,U_j^\dagger$. Their synthesis is supplied; a nearest-neighbor address graph does not establish locality on the work registers.

**Theorem IV.4 (history propagation; PT11).** The clock has spectrum $\kappa(n-2j)$, $j=0,\ldots,n$, norm $\kappa n$ and amplitudes
\[
c_j(t)=(-i)^j\sqrt{\binom nj}\sin^j(\kappa t)\cos^{n-j}(\kappa t).
\]
From address 0, the comparator applies $P_n$ at $T=\pi/(2\kappa)$ with terminal probability one, and returns to prefix $P_0$ at $2T$. Actual/comparator propagator difference is at most $td$.

*Proof.* Identify address $j$ with the normalized symmetric sum of $n$ binary spin states of weight $j$. The operator $\kappa\sum_{a=1}^n X_a$ has the displayed adjacent matrix elements and restricts to $H_C$. Tensor products of single-spin rotations give $c_j(t)$; symmetric products of $X$ eigenstates give the spectrum. Since $[\bar H_W,\mathcal W]=0$,
\[
e^{-itH_{\rm comp}}|0\rangle|\psi\rangle
=\sum_j c_j(t)|j\rangle e^{-it\bar H_W}P_j|\psi\rangle.
\]
At $T$ only $j=n$ survives; at $2T$ only $j=0$ survives. The actual difference is $H_W-\bar H_W$, so Lemma IV.1 gives the last bound. The identity extends to mixed inputs and arbitrary spectators by purification. $\square$

The endpoint return is projective: the common factor at $2T$ is $(-1)^n$. Free work evolution is retained; the full work state need not recur. At integer endpoint index $\ell=2u+r$, $\ell\equiv r\pmod2$, the address is start for $r=0$ and terminal for $r=1$. The modulus 2 is prime. Returning the address does not refill a donor or provide a stopping rule.

**Corollary IV.5 (completion window).** Start the actual machine at address 0 with arbitrary work/spectator state. For $t=T+s\ge0$ and $|s|\le\sigma$, define
\[
a_C=\sqrt n\,\kappa\sigma+(T+\sigma)d.
\]
Its nonterminal probability is at most $\min\{1,a_C^2\}$.

*Proof.* The comparison terminal probability is $\cos^{2n}(\kappa s)$. The inequality $1-(1-z)^n\le nz$ for $z\in[0,1]$, together with $|\sin(\kappa s)|\le\kappa|s|$, bounds the nonterminal amplitude by $\sqrt n\kappa\sigma$. Lemma IV.1 adds at most $td\le(T+\sigma)d$ to this projected amplitude. $\square$

If the source terminal-branch target has its inherited isolated bank error $\eta_{\rm bank}$ and the native/comparator post-endpoint free phases differ by at most $|s|d$, a complete target bound is
\[
\eta_{\rm window}\le\min\{1,\eta_{\rm bank}+\sqrt n\kappa\sigma+(T+2\sigma)d\}.
\]
Here the comparator is compared to its normalized terminal branch, whose purification overlap has magnitude $|c_n|$, hence trace distance $\sqrt{1-|c_n|^2}$. Triangle inequality then supplies the displayed bound. The branch-target premise is essential: a generic arbitrary word is not a packet producer. The whole propagation mismatch replaces the earlier separately timed pulse debit; both are not charged for the same comparison interval.

# 5. Timed terminal capture and protected propagation

## 5.1 Guarded background and matched involution

Supply matched $S,O$ with $H_O=H_S$ and fresh $L=0$. Records $M,E$ are bare-degenerate. The production clock and flag use zero bare park energies in this architecture. Define
\[
H_{\rm free}=H_W+H_O,
\qquad H_{\rm bg}=H_{\rm free}+P_{L0}H_p,
\quad P_{L0}=|0\rangle\langle0|_L.
\]
The guard commutes with the flag and has norm at most $\kappa n$. $O$ has no background interaction: $H_{\rm bg}=H_O+H_{\rm rest}$. This conditional guard is an engineered input.

With terminal projector $P_n$ on $C$, set
\[
J=P_n\otimes\mathrm{SWAP}_{SO}\otimes X_L+(I-P_n)\otimes I,
\quad G_c=\frac{\pi}{2\tau_c}(I-J),\quad \tau_c>0.
\]
Matched bare energies imply $[J,H_{\rm free}]=0$, and $J^\dagger=J$, $J^2=I$. Thus $e^{-i\tau_c G_c}=J$ and $\|G_c\|\le\pi/\tau_c$, with equality when a negative-eigenvalue sector is present. The pulse swaps unknown states and correlations; it does not clone them or create a blank output.

**Theorem IV.6 (timed contact and flags; PT13).** For comparison $B_c=e^{-i\tau_cH_{\rm free}}J$ and actual $A_c=e^{-i\tau_c(H_{\rm bg}+G_c)}$,
\[
\|A_c-B_c\|\le\gamma_c=\tau_c\kappa n.
\]
For an incoming state with fresh flag and nonterminal probability at most $a_C^2$,
\[
p_{\rm NO\_CAPTURE}\le\min\{1,(a_C+\gamma_c)^2\},
\quad p_{\rm false\ tag}\le\min\{1,\gamma_c^2\}.
\]
The false terminal-tag event is $(I-P_n)P_{L1}$, not every flag-1 outcome.

*Proof.* The ideal pulse commutes with the free generator; actual/comparison generator difference is the guarded hopping of norm at most $\kappa n$. Lemma IV.1 proves the uniform contact bound. Ideal capture sends terminal fresh-flag inputs to flag 1 and nonterminal inputs to flag 0, so its no-capture amplitude equals the incoming nonterminal amplitude. The bad event annihilates ideal capture on every fresh-flag input because its flag-1 branch has terminal $C$. Projected amplitude triangle inequalities give both bounds. Free evolution preserves these projectors. $\square$

Additional active-contact integrated norms enter $\gamma_c$ only when their domains match. Initial supply error changes probabilities by at most the admitted joint distance. False-tag probability is a diagnostic already controlled by the unconditional joint bound; it is not charged again as an independent state error.

## 5.2 Full record, witness and pulse-off theorem

Copy the commuting flag to blank $M$, then to blank $E$ using controlled $X$. These copy unitaries commute with $H_{\rm bg}$; a Hermitian logarithm for each can also be chosen to commute, so ideal simultaneous background evolution factors. Supply and implementation of the copy controls remain costs. The complete dilation retains $L,M,E$ and all correlations. After reducing witness $E$, the operational record is
\[
\mathcal R(\rho)=\sum_{\ell=0,1}|\ell\rangle\langle\ell|_M\otimes P_{L\ell}\rho P_{L\ell}.
\]
Both branches are unnormalized. A classical operational reduction does not make the full pure dilation a classical state.

**Theorem IV.7 (post-switch output protection; PT13).** After the supplied capture and record contacts are off, evolution under $H_{\rm bg}$ gives for any actual input, including failures and false tags,
\[
\rho_{OM}(u)=(e^{-iuH_O}\otimes I_M)\rho_{OM}(0)(e^{iuH_O}\otimes I_M).
\]
Flag probabilities remain constant. In flag 1 the production hopping is parked.

*Proof.* The background factors as $H_O+H_{\rm rest}$ and acts trivially on $M$. In taking the reduced $OM$ state, conjugation by the rest unitary disappears under partial trace, even for correlated inputs. Commutation with $P_{L\ell}$ preserves flag populations; $P_{L0}H_p$ vanishes in flag 1. $\square$

Protection is exact for the isolated declared background, not a measured lifetime. A coupling to $O$ or a flag-flipping perturbation needs its own integrated bound. Common native free output phases remain in the target; no new comparator mismatch growing with storage time is charged when actual and target share that evolution.

**Lemma IV.8 (restricted capture posterior).** If the operational classical-quantum state has distance $\epsilon$ from an ideal state supported wholly on CAPTURED with target $\sigma$, and its actual capture probability is $p>0$, then its normalized captured state has distance at most $\min\{1,\epsilon/p\}$ from $\sigma$.

*Proof.* The block-diagonal norm gives $\epsilon\ge\tfrac12\|p\rho_{\rm cap}-\sigma\|_1+(1-p)/2$. Since $p(\rho_{\rm cap}-\sigma)=p\rho_{\rm cap}-\sigma+(1-p)\sigma$, triangle inequality gives $pD_{\rm tr}(\rho_{\rm cap},\sigma)\le\epsilon$. $\square$

This lemma does not apply unchanged to arbitrary detector outcomes whose ideal acceptance is below one. Capture/export timing, pulse-off and routing are supplied controls.

# 6. Closed finite first-entry obstruction

**Theorem IV.9 (PT14).** For one finite time-independent Hermitian $H$, a subspace invariant under $H$ is reducing. Its population cannot first increase from the orthogonal complement. If a fixed observable expectation under $e^{-itH}$ is constant on an open time interval, it is constant for all real $t$.

*Proof.* Hermiticity makes $\langle Hx,y\rangle=\langle x,Hy\rangle=0$ for $x$ in the orthogonal complement and $y$ in the invariant subspace. Its projector therefore commutes with $H$ and with the propagator; population is constant. Spectral decomposition expresses any expectation as a finite sum $\sum_{a,b}c_{ab}e^{it(E_a-E_b)}$, a real-analytic function of real time. A constant on an open interval has identically zero derivative by analytic continuation. $\square$

This is a restricted obstruction to exact permanent first-entry capture in a closed finite static model. It excludes neither finite-horizon approximate retention, a supplied change of Hamiltonian, nor an open reservoir with its own ledger. If the ideal $G_c$ stays on for $2\tau_c$, $J^2=I$ undoes the exchange. With a noncommuting background, exact reversal is not asserted; its deviation is a perturbation comparison.

# 7. Static post-launch capture and finite horizon

## 7.1 Address dressing

Retain $H_f=H_W+H_O$ and parent guarded background $H_b=H_f+V_p$, $\|V_p\|\le h_p$. Supply fresh $L,M,E=0$, terminal production projector $P_n$, and
\[
J_*=P_n\otimes\mathrm{SWAP}_{SO}\otimes X_LX_MX_E+(I-P_n)\otimes I.
\]
Then $J_*^2=I$ and $[J_*,H_f]=0$. The phase conventions, matched energies and blank records are inputs.

Supply clock $Q$ initially at address 0 and define $H_Q$ by the spin-clock formula of Section 4 with $n,\kappa$ replaced by $N,\lambda$, $N\ge1$, $\lambda>0$. Put $W_0=I$, $W_j=J_*$ for $j\ge1$ and
\[
\mathcal V=\sum_{j=0}^N|j\rangle\langle j|_Q\otimes W_j,
\quad H_d=\mathcal V(H_Q\otimes I)\mathcal V^\dagger,
\quad H_a=I_Q\otimes H_b+H_d,
\quad H_0=I_Q\otimes H_f+H_d.
\]
Only edge $0$-$1$ carries $J_*$; subsequent edges carry identity. The dressed generator has norm $\lambda N$. All couplings are constant after a supplied launch; launch alignment is not derived.

## 7.2 Complete versus marginal comparison

**Theorem IV.10 (static joint bound; PT16).** Set $r(t)=\cos^{2N}(\lambda t)$ and let $|\chi(t)\rangle=e^{-itH_Q}|0\rangle$. For any body/spectator state $\rho$, the actual evolution from $Q=0$ satisfies
\[
D_{\rm tr}\!\left(\rho_a(t),|\chi(t)\rangle\langle\chi(t)|\otimes
 e^{-itH_f}J_*\rho J_*e^{itH_f}\right)
\le\min\{1,th_p+2\sqrt{r(t)}\}.
\]
In the comparison alone, reducing $Q$ produces a mixture with weight $r$ on the pre-capture body and $1-r$ on the transferred body, so its reduced-body distance from the latter is at most $r$.

*Proof.* Section 4 and $[J_*,H_f]=0$ give on a purification
\[
|\Psi_0(t)\rangle=\sum_{j=0}^Nc_j(t)|j\rangle e^{-itH_f}W_j|\psi\rangle.
\]
Against the displayed fully transferred product target, the vector difference is $c_0(t)|0\rangle e^{-itH_f}(I-J_*)|\psi\rangle$, with norm at most $2|c_0|=2\sqrt r$. Actual/comparison propagator difference is bounded by $th_p$. Lemma IV.1 and triangle inequality give the complete bound. Orthogonal address reduction gives exactly the stated mixture; convexity bounds its distance by $r$. $\square$

The marginal $r$ cannot replace the complete $2\sqrt r$ when retaining the clock or reusing correlated resources. The target clock continues to evolve; it is not a classical scheduler.

For fresh records, incoming production nonterminal probability $p$ gives comparison NO_CAPTURE probability $p+(1-p)r$. If $\sqrt p\le a$, its amplitude is at most $a+\sqrt r$ and the actual probability is at most
\[
\min\{1,(a+\sqrt r+th_p)^2\}.
\]
The false-tag projector $(I-P_n)P_{L1}$ annihilates the comparison on fresh records, so its actual probability is at most $\min\{1,(th_p)^2\}$. As before, initial supply and extra contacts require additional admission; diagnostic probabilities do not become independent joint-error charges.

## 7.3 Window, return and resource tradeoff

**Corollary IV.11 (finite retention interval; PT16).** On
\[
\frac{\pi}{4\lambda}\le t\le\frac{3\pi}{4\lambda},
\qquad r(t)\le2^{-N},
\]
the complete debit is at most $\min\{1,3\pi h_p/(4\lambda)+2\,2^{-N/2}\}$. Comparator transfer is exact at $\pi/(2\lambda)$ and is undone at $\pi/\lambda$.

*Proof.* On the interval $|\cos(\lambda t)|\le1/\sqrt2$, and $t\le3\pi/(4\lambda)$. Theorem IV.10 gives the bound. At half a spin period the clock is at $N$, dressed by $J_*$; at a full projective period it is at 0, dressed by identity. $\square$

The last return includes record flips and free body evolution; it is not storage permanence. Actual departure from comparison is charged, so exact comparison recurrence is not an exact actual recurrence theorem. These are pointwise bounds, not continuously monitored first-entry or survival probabilities. Monitoring changes the channel.

Write interval duration $\mathcal H=\pi/(2\lambda)$. Its conservative parent-contact term is $3\mathcal H h_p/2$, while clock norm is $\pi N/(2\mathcal H)$. Padding decreases the boundary tail but not that parent term. This is a sufficient-bound tradeoff, not a lower bound on every possible apparatus. Long retention requires another owned shutdown, routing or reservoir mechanism.

# 8. Matched renewal and finite resource banks

## 8.1 Exact correlation export

**Theorem IV.12 (matched renewal; PT15).** For a finite active module $A$, an independent matched donor $D$ in target state $\sigma_D$, and arbitrary correlated old state $\rho_{AY}$,
\[
\mathrm{SWAP}_{AD}(\rho_{AY}\otimes\sigma_D)\mathrm{SWAP}_{AD}
=\sigma_A\otimes\rho_{DY}.
\]
Every old $A/Y$ correlation is transferred to $D/Y$.

*Proof.* Expand $\rho_{AY}$ in matrix units on $A$ and $Y$ and $\sigma_D$ in matrix units on $D$. Conjugating by SWAP exchanges the two identified module labels. Reordering tensor factors gives the displayed product. No partial trace or success conditioning is used. $\square$

For timed capture, $A=(S,R,F,C,L)$ while outputs, records and witnesses remain in $Y$. For static capture, include $Q$ in $A$. A replacement donor must include fresh coherent fuel, loaded reference, prepared clock and flag, any needed fresh source cells, and the appropriate endpoint free phase. Merely restoring a clock address does not restore the whole module. Exact independence of the ideal donor is a hypothesis; approximate correlations enter complete bank error.

For duration $\tau_r$, the matched principal-log exchange generator is $G_r=\pi(I-\mathrm{SWAP})/(2\tau_r)$. It commutes with the matched sum of bare free operators. Actual running interactions add architecture-specific full-joint contact bounds:

| Architecture | Running operator charged | Contact upper bound |
|:--|:--|:--|
| Original dressed controller against bare clock | $H_p-H_C$, norm at most $2\kappa n$ | $2\tau_r\kappa n$ |
| Guarded timed capture | $P_{L0}H_p$, norm at most $\kappa n$ | $\tau_r\kappa n$ |
| Static capture including $Q$ | Guarded parent plus $H_d$, norm at most $h_p+\lambda N$ | $\tau_r(h_p+\lambda N)$ |

The comparator/free split determines the debit. Copying a timed norm into static renewal would omit its capture clock. Static full-module renewal in the source is an algebraic continuation; no implemented autonomous renewal/router is certified.

## 8.2 Whole-bank admission and unconditional composition

**Proposition IV.13 (finite sequence budget).** Let the complete supplied resource bank $B$ and history $Y$ satisfy
\[
D_{\rm tr}(\omega_{BY},\sigma_B\otimes\omega_Y)\le\epsilon_F,
\]
where the ideal bank specifies independent fresh slots and all blanks. Suppose each actual operation differs from its matching ideal operation by at most $\epsilon_j$ on the full admitted joint state, with arbitrary spectator extension and the same retained domain. After $A$ operations,
\[
D_{\rm tr}(\rho_A,\rho_A^{\rm ideal})\le
\min\left\{1,\epsilon_F+\sum_{j=1}^{A}\epsilon_j\right\}.
\]

*Proof.* For actual channel $\Phi_j$ and ideal $\Psi_j$, insert the ideal input at step $j$. Contractivity bounds the first difference by the preceding joint error; the assumed operation comparison bounds the second by $\epsilon_j$. Induction starts with $\epsilon_F$. If different operations expose different registers, extend both by the same identity/free channel on all retained registers before using this argument. $\square$

A bound proved only for an isolated input does not automatically satisfy this uniform-domain hypothesis. Interleaving contacts on the same reference require a complete integrated comparison. Production, capture, renewal, routing, detector, storage, thermal and implementation terms are summed only on matching contracts. No-capture and false-tag diagnostics already covered by state distance are not double-counted. Full-bank admission is charged once; consumed slots and all failed histories remain.

Good marginals need not imply a good bank. Label bit 1 a successful slot. The uniform classical distribution on $110,101,011$ has marginal success $2/3$ at each of three slots but no $111$ outcome. Its complete distance from the all-success target is one, whereas the unjustified independent product would give success $8/27$. The factors are $8=2^3$, $27=3^3$; $8=0\cdot27+8$ and $8\equiv8\pmod{27}$. This witness rules out a marginal-product admission, not a valid complete correlated-state admission.

For $A$ supplied donor and output slots, attempts are $j=0,\ldots,A-1$; at $j=A$ the specified controller refuses and appends END_OF_SUPPLY. There is no modular wrap. Failure consumes a slot as success does. Reusing an old output as blank can swap previous data back into the machine. Slot selection, refusal and routing remain supplied policy, not a derived autonomous counter. Donor counts may be chosen freely; no prime-count requirement is inferred from the parity convention.

# 9. Energy conventions, records and implementation debts

During a constant machine interval total mean energy is conserved. For $H_{\rm act}=H_W+H_C+V$, $V=H_p-H_C$,
\[
\Delta\langle H_{\rm act}\rangle=0,
\qquad\Delta\langle H_W+H_C\rangle=-\Delta\langle V\rangle,
\quad\|V\|\le2\kappa n.
\]
This does not assert conservation of every subsystem's bare energy. Adding one global constant alters an energy origin without changing trajectories. A flag-conditioned offset changes the Hamiltonian and cannot be inserted as an innocent convention.

For the supplied constant capture pulse, switch-on/off signed mean work is
\[
W_c=\langle G_c\rangle_{\rm in}-\langle G_c\rangle_{\rm out}
=\Delta\langle H_{\rm bg}\rangle,
\qquad |W_c|\le2\pi\kappa n.
\]
Indeed $[H_{\rm free},G_c]=0$, so the rate of $\langle G_c\rangle$ is governed by the guard; integrating $|\langle i[P_{L0}H_p,G_c]\rangle|\le2\kappa n\|G_c\|$ over $\tau_c$ gives the bound. It is a signed mean-work estimate, not a work distribution, peak-power certificate or supply mechanism. An ideal commuting flag-copy pulse has zero net signed mean switching work under that convention, but consumes blank memory and creates correlations; record erasure is not free.

For fresh static clock address 0, $\langle H_d\rangle=0$ and $\langle H_d^2\rangle=\lambda^2N$ for every body state. The first statement follows from off-diagonal address support; the second from the first edge's squared magnitude $\lambda^2N$ and $J_*^2=I$. Body-only background cross covariance vanishes initially, so $\operatorname{Var}H_a=\operatorname{Var}H_b+\lambda^2N$. A global shift by $\lambda N$ changes the mean but not the variance. Address 0 is nonstationary under the engineered generator; zero mean in one convention does not imply free clock preparation.

The following ledger must accompany any finite example.

| Resource | Required specification | Unclosed acquisition/implementation gate |
|:--|:--|:--|
| Production clock | Dimension, state, norm, jitter, recurrence | Native supply, edge synthesis and launch |
| Reference/fuel | Complete state, seed energy, variance, shift margins | Coherent source and energy hierarchy |
| Timed capture | Matched carriers, duration, pulse and off-switch | Trigger, control tolerance and switching apparatus |
| Static capture | Fresh clock, full operator, horizon and return | Alignment, local coupling and export |
| Donor bank | Whole-bank error, spectator correlations, finite cap | Independent donors, routing and refusal |
| Output/records | Fresh slots, retained witness, acceptance convention | Calibration, acquisition and storage perturbations |

These gates prevent promotion from a prepared operator construction to a complete native autonomous cycle. The 30-to-23 face-gluing interface from Paper II is a separate direct-sum construction; equality of an ambient dimension with a Pachner comparison does not identify their carriers. No detector result is inferred from a six-quadrature or complete-receipt algebra alone.

# 10. Exact examples, replay and limitations

Take the source's $n=23$, $\kappa=4096=2^{12}$, so $h_p=94208=23\cdot2^{12}$. With supplied timed contact $\tau_c=2^{-30}$,
\[
\gamma_c=\frac{23}{2^{18}},\qquad
\gamma_c^2=\frac{529}{2^{36}}.
\]
For static $N=40=2^3\cdot5$, $\lambda=2^{32}$, clock dimension is 41 (prime) and norm $\lambda N=5\cdot2^{35}$. The uniform interval clock tail is
\[
r\le\frac1{2^{40}},\qquad2\sqrt r\le\frac1{2^{19}},
\quad\frac{3\pi h_p}{4\lambda}=\frac{69\pi}{2^{22}}.
\]
The interval begins at $\pi/2^{34}$ and ends at $3\pi/2^{34}$ after supplied launch. Its duration is $\pi/2^{33}$ in model units. Static renewal at $\tau_r=2^{-50}$ has contact upper bound
\[
\frac{h_p+\lambda N}{2^{50}}=\frac{41943063}{274877906944}.
\]
These values compare different declared architectures; their error columns are not interchangeable or summed as one apparatus. Huge dimensionless norms, very short horizons, coherent clock supply and unknown laboratory conversion are implementation debts. The parameters are supplied example inputs, not native coefficients selected to match an observation.

The executable `replay/verify_paper_iv.py` supplies exact finite-map checks and separate numerical joint comparisons. It includes spectator-entangled inputs, clock transfer/return, the capture involution, matched-energy commutation, static full-joint versus marginal distance, renewal correlation export, stationary reference bound and a correlated-bank negative control. It does not instantiate the large source parameter example, certify all acquisition conditions or establish the general proofs by enumeration. Its result receipt records actual executed counts and tolerances. The M4 check set and the original baseline are separate receipts.

Historical source receipts reported 7,644 exact plus 108 numerical controller checks, 947 exact plus 99 numerical capture checks, and 1,195 exact plus 192 numerical static-capture checks [8-10]. They are preserved as historical receipts; the new Paper IV replay is separately identified and does not claim to rerun those complete packages. Original complex-audit archive custody and alternative-tree optimization remain source-blocked in Paper II. Infinite scalar cyclicity remains open in Paper III. None is closed by controller extraction.

The narrow next theorem target is a complete bounded production-to-capture trigger and finite router on one owned joint domain, including failures, recurrence and exhaustion. A successful conditional word, capture window or swap does not supply that missing trigger. Upstream coherent fuel, clock preparation, native geometry/admission, physical action/time scales and empirical comparison remain open. Independent mathematical review and a complete novelty comparison are required before submission claims exceed this development draft.

# Appendix A. Stable claim/source crosswalk

| Earlier identifier and location | Current theorem(s) | Source dependency |
|:--|:--|:--|
| PT11; III Section 13.1 | IV.4-IV.5 | Controller audit 0.26 [8] |
| PT12; III Section 13.1 | IV.2-IV.3 | Finite ladder [7], coherent producer [8] |
| PT13; III Section 13.2 | IV.6-IV.8 | Capture/guard audit 0.27 [9] |
| PT14; III.C1 | IV.9 | Finite closed obstruction [9] |
| PT15; III Section 13.3 | IV.12-IV.13 | Controller/capture renewal [8-9] |
| PT16; III Section 13.4 | IV.10-IV.11 | Static capture audit 0.28 [10] |

Paper III retains its Section 13 summary, numbering and old proof of III.C1. The present paper supplies a dedicated treatment; it does not silently delete or supersede historical theorem locations. Source hashes, the 74-record F13 extraction register, correction dispositions and release history accompany the package. A family candidate record is source routing, not individual proof certification. No ledger coefficient or physical status is promoted by editorial extraction.

# Appendix B. Evidence status and declared domains

All theorems in this draft are exact conditional statements about supplied finite matrices, states or channels. The clock transfer ingredient is established prior art; new packaging does not change that. The actual-to-comparator statements use operator norm on the complete admitted domain. Source-overlap statements additionally depend on isolated production and the source's cutoff certificate. Numerical fixtures test specified small instances only. No physical data are present.

The source governance document distinguishes constructor checking from non-constructor review. The new draft remains in development with no registry promotion. A version increment denotes an editorial release, not a confidence-rung increase. All correction and source records are append-only, preserving the earlier releases and their original claims with dated replacements. The legacy coefficient ledger is retained as a versioned source baseline, not asserted to be a fresh audit of every later coefficient. Physical promotion remains zero.

# References

[1] M. Christandl, N. Datta, A. Ekert and A. J. Landahl, "Perfect state transfer in quantum spin networks," *Physical Review Letters* 92, 187902 (2004). doi:10.1103/PhysRevLett.92.187902. [arXiv:quant-ph/0309131](https://arxiv.org/abs/quant-ph/0309131).

[2] L. Caha, Z. Landau and D. Nagaj, "Clocks in Feynman's computer and Kitaev's local Hamiltonian: Bias, gaps, idling, and pulse tuning," *Physical Review A* 97, 062306 (2018). doi:10.1103/PhysRevA.97.062306. [arXiv:1712.07395](https://arxiv.org/abs/1712.07395).

[3] M. P. Woods, R. Silva and J. Oppenheim, "Autonomous quantum machines and finite-sized clocks," *Annales Henri Poincare* 20, 125-218 (2019). doi:10.1007/s00023-018-0736-9. [arXiv:1607.04591](https://arxiv.org/abs/1607.04591).

[4] M. Lostaglio and M. P. Mueller, "Coherence and asymmetry cannot be broadcast," *Physical Review Letters* 123, 020403 (2019). doi:10.1103/PhysRevLett.123.020403. [arXiv:1812.08214](https://arxiv.org/abs/1812.08214).

[5] F. Herbut, "A review of unitary quantum premeasurement theory," [arXiv:1412.7862](https://arxiv.org/abs/1412.7862) (2014).

[6] B. W. Mayes, Papers I-III, consolidated review drafts 1.1.1 (4 October 2026), supplied in the same package. Not represented as peer-reviewed publications.

[7] B. W. Mayes / Codex constructor, *Finite ladder reference and certified admission*, v0.1 (3 October 2026). Source package and hash in the accompanying custody register.

[8] B. W. Mayes / Codex constructor, *Finite history controller and coherent supply/reset*, v0.1, audit 0.26 (3 October 2026). Prepared construction, independent review pending.

[9] B. W. Mayes / Codex constructor, *Terminal capture, guarded latch and finite renewal*, v0.1, audit 0.27 (3 October 2026). Includes construction correction CL01.

[10] B. W. Mayes / Codex constructor, *Static capture clock and finite retention horizon*, v0.1, audit 0.28 (3 October 2026). Static renewal continuation is algebraic; autonomous routing remains open.
