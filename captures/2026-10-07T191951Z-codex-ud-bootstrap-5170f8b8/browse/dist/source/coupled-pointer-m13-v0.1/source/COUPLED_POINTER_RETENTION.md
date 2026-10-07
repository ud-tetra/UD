---
title: "A Finite Pair-Qubit Pointer Clock with a Certified Joint Retention Window"
subtitle: "UD M13 development addendum 0.1"
author: "Benjamin Walker Mayes / Codex constructor"
date: "5 October 2026"
---

**Development — no registry entry. Independent review pending. Physical promotion 0.** This continues WBS 5.2 after M12. The result is a finite, constant, pair-qubit generator for the same completed toy work operation ZX, with a certified full clock/work/spectator window. The resource upper bounds are enormous. It does not implement the retained 380-qubit production/capture/renewal word, chronological X-then-Z gates, native clock formation, or an efficient realization. No ledger coefficient is added or altered.

# 1. Owned factors, fixed reference, and constant pair generator

Name one pointer qubit P, N clock qubits C_j, and one work qubit B. All clocks start in the supplied product state $|c_0\rangle=|0\rangle_P|0\rangle^{\otimes N}_C$. Work B may be entangled with arbitrary spectators R. There is no external action after launch. Positive engineered scales are $\kappa,\Omega,G$, with $g=G/N$. This kappa is the toy comparison scale, distinct from the retained full-controller kappa_0.

Predeclare the independent auxiliary reference by its clock-only generator
\[
H_C=\Omega X_P+\kappa\sum_{j=1}^N X_j+g\sum_{j=1}^N Z_PZ_j,
\qquad |\chi_C(t)\rangle=e^{-itH_C}|c_0\rangle.
\]
This is a reference evolution specified before constructing or executing the work propagator; it is not the actual work-coupled clock marginal. Define $V=ZX=iY_B$ and the mathematical dressing
\[
W=|0\rangle\langle0|_P\otimes I_B+|1\rangle\langle1|_P\otimes V,
\]
with identity on every C_j and R. The proposed complete generator is
\[
H=W(H_C\otimes I_B)W^\dagger
=\Omega Y_PY_B+\kappa\sum_{j=1}^N X_j+g\sum_{j=1}^N Z_PZ_j.
\]
The identity follows by multiplying the two pointer off-diagonal blocks: $WX_PW^\dagger=Y_PY_B$; every other clock term commutes with W. W is used to prove the propagator, not as an uncharged launch circuit. Every physical generator term is onsite or two-qubit; the work and pointer genuinely interact. Connectivity is a star, with degree N at P; geometric locality is not established. Each qubit's full space is retained, with no encoded padding or discarded reservoir.

The target at the same actual elapsed t is the predeclared pure clock reference tensor the completed work/spectator state $(V\otimes I_R)\rho_{BR}(V^\dagger\otimes I_R)$. This circuit compresses the known product ZX; it does not claim an ordered noncommuting gate history. We use the unchanged toy interval
\[
T=\frac{\pi}{2\kappa},\qquad \mathcal I=[2T/3,4T/3]=[\pi/(3\kappa),2\pi/(3\kappa)].
\]

# 2. Exact full-state reduction to a pointer probability

**Theorem M13.1.** Write $|\chi_C(t)\rangle=|0\rangle_P|a(t)\rangle+|1\rangle_P|b(t)\rangle$, and set $p_0(t)=\|a(t)\|^2$. For supplied ready clocks, the supremum of complete trace distance over work inputs and arbitrary spectators is exactly
\[
E(t)=\sqrt{2p_0(t)-p_0(t)^2}\le\sqrt2\sqrt{p_0(t)}.
\]

*Proof.* W is the identity on the supplied initial pointer. Thus the actual pure state is $W(|\chi_C(t)\rangle|\psi\rangle)$ for every purified work/spectator input. Its overlap with $|\chi_C(t)\rangle V|\psi\rangle$ is $1-p_0+p_0\langle\psi|V^\dagger|\psi\rangle$. Since $V^\dagger=-iY$, the latter expectation is purely imaginary. The squared overlap is at least $(1-p_0)^2$, attained by work |0>, including the case with no spectator. Pure-state trace distance gives the formula. Purification and contractivity give the mixed-input upper bound. No marginal is substituted for the joint comparison. In particular the actual clock can depend on work; the reference clock does not. $\square$

An exact endpoint is not promised. The certificate will bound the full interval, including T. This avoids treating a correct endpoint as a plateau.

# 3. Finite-clock fluctuation and pointer-following estimates

For analysis only, introduce the time-dependent product reference: each C_j evolves freely under kappa X, and the pointer follows
\[
K_P(t)=\Omega X_P+G\cos(2\kappa t)Z_P.
\]
This time-dependent generator is **not** an implemented control schedule. It is used only to estimate the constant H_C. Let $|\varphi(t)\rangle$ be this product evolution from the same supplied initial state.

**Lemma M13.2 (finite-clock fluctuation).** For every $0\le t\le4T/3$,
\[
\|e^{-itH_C}|c_0\rangle-|\varphi(t)\rangle\|
\le \frac{G}{\sqrt N}\int_0^t|\sin(2\kappa s)|\,ds
\le\frac{5G}{4\kappa\sqrt N}.
\]

*Proof.* The generator difference acting on the product reference is $gZ_P\sum_j[Z_j-\cos(2\kappa t)]$. Its squared norm is $g^2N\sin^2(2\kappa t)$: independent product spins have zero cross covariances, and pointer Z has norm one on every pointer state. State-dependent Duhamel integration uses unitary propagation of this residual. At the upper time the integral is $[2+1/2]/(2\kappa)=5/(4\kappa)$; the integral is monotone before that. This owns back-reaction as a finite joint-state error rather than replacing the clock by an infinite classical field. $\square$

**Lemma M13.3 (elementary following bound).** Over the entire observation interval, the product-reference pointer has wrong-pointer amplitude at most
\[
A_P=\frac{3\Omega}{2G}+\frac{4\kappa G}{\Omega^2}.
\]

*Proof.* Put $D(t)=G\cos(2\kappa t)$, $E_P(t)=\sqrt{\Omega^2+D(t)^2}$, and choose a continuous angle $\theta\in(0,\pi)$ with $\sin\theta=\Omega/E_P$, $\cos\theta=D/E_P$. The initial upper eigenvector differs from pointer |0> by Euclidean norm at most $\Omega/(2G)$. During the window $D\le-G/2$, so its wrong-pointer component is at most $\Omega/(2|D|)\le\Omega/G$.

It remains to bound transition from the upper instantaneous eigenvector. In the eigenbasis with dynamical phases removed, the off-diagonal coupling has magnitude $|f|$, where
\[
f=\dot\theta/2=\frac{\kappa\Omega G\sin(2\kappa t)}{E_P^2},
\quad \dot\phi=2E_P,
\quad a=f/(2E_P),
\quad |a|\le a_{\max}=\frac{\kappa G}{2\Omega^2}.
\]
Integration by parts in $c_-(t)=\pm\int_0^t f(s)e^{\pm i\phi(s)}c_+(s)ds$ gives
\[
|c_-(t)|\le |a(t)|+|a(0)|+\int_0^t|\dot a|ds
+\int_0^t|a|\,|f|ds.
\]
Here $a(0)=0$ and $|\dot c_+|\le|f|$. On $0\le2\kappa t\le4\pi/3$, a has one positive maximum, returns to zero at pi, and then decreases to a negative value. Indeed its derivative with respect to $x=2\kappa t$ has the sign of $\cos x$, since the positive numerator factor is $\Omega^2+G^2\cos^2x+3G^2\sin^2x$. Hence $|a(t)|+\int|\dot a|\le4a_{\max}$, also for any earlier t. The total variation of theta is at most $2\pi$, giving $\int|f|\le\pi$. Thus $|c_-|\le(4+\pi)a_{\max}<8a_{\max}=4\kappa G/\Omega^2$. The initial-state discrepancy, upper-vector wrong component and lower-vector amplitude add to the displayed bound. No infinite-time Landau–Zener formula or unproved adiabatic slogan is used. $\square$

**Theorem M13.4 (uniform joint certificate).** Combining projection contractivity with the two lemmas yields
\[
\sup_{t\in\mathcal I}E(t)\le\sqrt2\left[
\frac{3\Omega}{2G}+\frac{4\kappa G}{\Omega^2}
+\frac{5G}{4\kappa\sqrt N}\right].
\]
The bound is uniform on every admitted work/spectator input, with the explicitly supplied pure clocks. This is a sufficient analytical certificate; its value is not the actual optimum error. The finite-clock proof is symbolic and does not require dense propagation of the enormous admitted instances.

# 4. Two explicit finite envelopes and an arbitrary-accuracy family

The parameters below are predeclared finite design instances. N is the count of binary clock factors, not their Hilbert dimension. All scales are engineered; no native UD coefficient or measured capability is asserted. Use $\sqrt2<3/2$ for outward rational certificates.

| Instance | N | G/kappa | Omega/kappa | g/kappa | Wrong-pointer amplitude bound | Outward joint bound | Gate |
|---|---|---|---|---|---|---|---|
| Toy-window example | $2^{52}$ | $2^{20}$ | $2^{14}$ | $2^{-32}$ | $15/256$ | $45/512<11/100$ | Toy window certified |
| Provisional timer-debit example | $2^{134}$ | $2^{50}$ | $2^{34}$ | $2^{-84}$ | $25/2^{19}$ | $75/2^{20}<1/5000$ | This toy's ideal joint timer error fits that allocation |

The latter meets only the M11 timer/correlation allocation for this operation under ideal preparation and exact couplings. It does not certify the inherited full semantic bank, other four allocations, a generic gate word, native preparation or the unsized full-controller resource envelope. The clock state differs from a reusable fresh clock; every C_j and P remains in the reference and actual domains.

The two instances have total binary-factor count $N+2$, clock dimension $2^{N+1}$ and complete clock/work dimension $2^{N+2}$; dimension prime factorizations have sole prime 2. For even exponents q, $N=2^q$ and $\sqrt N=2^{q/2}$ are exact. Time arithmetic stays $T=\pi/(2\kappa)$ and $\mathcal I=[\pi/(3\kappa),2\pi/(3\kappa)]$, with denominators 2 and $3=3^1$ retained explicitly. Taking kappa equal to kappa_0 would align this toy's interval with M11, but would not implement M11's full semantics.

For any requested ideal joint error $0<\epsilon\le1$, a finite member follows directly: set $r=\Omega/G=\epsilon/8$, choose $G/\kappa\ge2048/\epsilon^3$, and choose integer $N\ge[10G/(\kappa\epsilon)]^2$. The three amplitude terms are then at most $3\epsilon/16,\epsilon/8,\epsilon/8$, respectively. Their sum is $7\epsilon/16$ and the joint error is less than $21\epsilon/32<\epsilon$. This existence bound scales at most as $G=O(\epsilon^{-3})$, $\Omega=O(\epsilon^{-2})$, $N=O(\epsilon^{-8})$. It is not a lower bound, an optimal scaling, or an efficiency claim.

# 5. Resources, structured costs, defects and recurrence

Group each support once. There is one PB pair of norm Omega, N distinct P–C_j pairs of norm g, and N onsite clock terms of norm kappa. Predeclare
\[
N_{\max}=N+2,\quad h_{\max}=\max(\Omega,\kappa,g),
\quad J_{\max}=\Omega+N\kappa+G.
\]
All caps are met by construction. No splitting trick changes a support's norm. The total generator norm is at most J_max; no equality is claimed. For the supplied clocks and arbitrary work state, mean energy is G and variance is $\Omega^2+N\kappa^2$, because the off-diagonal PB and individual spin-flip images are mutually orthogonal. Energy spread is their square root. State preparation is supplied, with zero ideal defect in this mathematical instance; thermodynamic preparation work, native readiness and launch precision are unresolved. These caps admit huge costs rather than proving acceptable full-controller costs.

| Structured quantity | Exact value | Reason |
|---|---|---|
| Pauli count L | $2N+1$ | N onsite X, N pointer/clock ZZ, one pointer/work YY |
| Coefficient sum Lambda | $\Omega+N\kappa+G$ | All coefficients positive |
| Anticommute coefficient C | $G(\Omega+\kappa)$ | PB YY anticommutes with every P–C ZZ; each clock X anticommutes only with its own ZZ |
| Literal M10 parity basis action B | $(2N+4)\pi$ | X onsite contributes pi; ZZ pair pi; YY pair four pi |

If an external digital simulation is chosen, its inherited sufficient bound is $t^2G(\Omega+\kappa)/r_{\rm dig}$ with literal action $r_{\rm dig}(2N+4)\pi+t\Lambda$. This is an optional comparison; implementing that schedule would change the autonomous-generator claim. No dense exponential in dimension $2^{N+2}$ was executed.

For implementation generator defect delta and full initial preparation trace-distance defect eta, add at most $t\delta+\eta$ to the ideal joint certificate. For errors only in the star couplings, $\delta\le N\max_j|\Delta g_j|$ is a valid worst-case sufficient bound; small g does not eliminate aggregate calibration cost. All clock terms and backgrounds are included. A modified actual generator is still compared against the same frozen H_C reference. No measured defect budget is available.

This is a finite observation window, not an absorbing record. The complete finite-dimensional constant Hermitian propagator has arbitrarily close returns to identity by simultaneous eigenphase approximation. Work |0> then approaches its initial state and is far from the completed V|0> target. The clocks are not reset, discarded or renewed. No permanent exhaustion, exact periodic recurrence time or reusable launch is claimed.

# 6. WBS dispositions, replay and research context

| WBS | Executed here | Still open |
|---|---|---|
| 5.2 | Explicit coupled pair-qubit architecture and finite full-state toy window certificate | Full retained program and useful resource envelope |
| 4.3 / 5.3 | Uniform joint theorem with spectators and finite back-reaction cost | Full-bank correlations, failure and exhaustion semantics |
| 1.3 / 4.1 | Explicit two-instance N/h/J/energy and supplied-clock requirements | Native preparation, practical bounds and full-controller sizing |
| 3.1–3.2 | General-N structured operator and exact L/Lambda/C/B | Complete retained 380-qubit source-word realization |
| 8 | Authored source, constructor checks, hashes and preserved prerequisites | Non-constructor review; no registry promotion |

M11's fixed direct-encoding obstruction and M12's independent single-work-qubit theorem remain valid. This design leaves M12's failed family through genuine PB coupling and additional owned factors. The next effort should reduce these upper bounds and test smaller N through the permutation-symmetric clock representation before scaling the source word. A finite existence certificate is a different gate from an efficient full controller.

Replay checks finite small-N dressing, work/spectator propagation and the exact joint distance, clock residual variance, structured costs and exact Fraction inequalities for the enormous instances. Small-N checks do not pretend to simulate the large clock. The written integration-by-parts and Duhamel proofs supply the dimension-independent guarantee.

Research context: finite autonomous clock back-reaction is a prior research subject; see Woods, Silva and Oppenheim, [Autonomous quantum machines and the finite sized Quasi-Ideal clock](https://arxiv.org/abs/1607.04591). Explicit adiabatic error estimates likewise have prior literature; see Jansen, Ruskai and Seiler, [Bounds for the adiabatic approximation with applications to quantum computation](https://arxiv.org/abs/quant-ph/0603175). Those papers are context, not substitutions for the self-contained bounds above. No novelty or priority claim is made. The attached ledger and governance remain unchanged; missing Gap2_FINAL_Finite_Genesis.png was unavailable and not used.
