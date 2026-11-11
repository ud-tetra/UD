# THM-534 — Covariant seam-source and exact total-content continuity, v0.6

**Date:** 2026-10-21 | **Status:** EXACT conditional mathematics; CANDIDATE constitutive source map; NUMERICAL feedback check; packet-burden bridge OPEN | **Lane:** development / no registry promotion | **Physical promotion:** 0.

**Dependencies:** [v0.5 phase rigidity and closure no-go](THM534_NATIVE_SEAM_SELECTION_RIGIDITY_v0.5.md), [v0.4 oriented seam candidate](THM534_ORIENTED_SEAM_GENERATOR_AUDIT_v0.4.md), [v0.3 uniform incidence no-go](THM534_FORWARD_INCIDENCE_EVENT_PROGRAMME_v0.3.md). Historical THM-534 transition weights were exposed before this construction. This is **target-exposed exploratory development**, not confirmatory preregistration.

## 1. Typed construction and hypotheses

Let \(K=\Delta^3\) be the *filled* tetrahedral chain complex with ordered vertices \(0,1,2,3\), unit simplex-basis inner products, and signed alternating boundaries
\(B_1:\mathbb C^6\to\mathbb C^4\), \(B_2:\mathbb C^4\to\mathbb C^6\), \(B_3:\mathbb C\to\mathbb C^4\), satisfying \(B_1B_2=B_2B_3=0\).
Fix an incident oriented edge–face pair \((e,f)\) with incidence \(q=(B_2)_{ef}\in\{+1,-1\}\). The marked incidence is an *input boundary/event locator*; no current UD primitive selects it. Write \(e\) and \(f\) also for the corresponding unit basis vectors.

For \(z\in U(1)\), define the **candidate covariant coupling**, not a replacement topological differential,
\[
N_z:=B_2+(z-1)q\,e f^\dagger.
\]
The original topological chain complex and \(B_2\) remain unchanged. Define two typed curvature/closure-source receipts
\[
F_\downarrow(z):=B_1N_z\in\mathrm{Hom}(C_2,C_0),\qquad
F_\uparrow(z):=N_zB_3\in\mathrm{Hom}(C_3,C_1).
\]
They are *different typed carriers*, not scalar burden or physical stress-energy. Define the structural (dimensionless) frustration
\[
U(z):=\tfrac12(\|F_\downarrow(z)\|_F^2+\|F_\uparrow(z)\|_F^2).
\]
The full chain-state Hilbert space is \(H=C_0\oplus C_1\oplus C_2\oplus C_3\cong\mathbb C^{15}\). Amplitude \(\psi\in H\), squared-norm content \(n_a=|\psi_a|^2\), physical retained packet burden \(\rho\), a stochastic six-edge Markov matrix \(T\), and physical time are **distinct objects**. No identification is assumed.

## THM-534-S10 — Exact curvature receipt, source-free rigidity and nonzero-source response [EXACT / CANDIDATE]

Let \(z=e^{i\phi}\), \(\phi\in(-\pi,\pi]\). Then
\[
F_\downarrow=(z-1)q(B_1e)f^\dagger,\quad
F_\uparrow=(z-1)q(B_3)_f e,
\]
\[
\|F_\downarrow\|_F^2=2|z-1|^2,\quad
\|F_\uparrow\|_F^2=|z-1|^2,\quad
U(z)=3(1-\cos\phi).
\]
**Proof.** By \(\partial^2=0\), all terms proportional to the original \(B_2\) vanish. Each oriented edge boundary has squared norm \(2\); the selected component of the tetrahedral boundary has modulus \(1\). Finally \(|e^{i\phi}-1|^2=2(1-\cos\phi)\). QED.

Introduce a **proposed**, dimensionless, signed and orientation-sensitive source \(j\in\mathbb R\), with the *constitutive candidate* selection functional
\[
\mathcal V_j(\phi):=3(1-\cos\phi)-j\sin\phi.
\]
The sine coupling and the identification of its conjugate source are **not** derived from the admitted UD master action; the relative normalization defines the convention for \(j\). The unique global minimizer (mod \(2\pi\)) is
\[
\boxed{z_*(j)=\frac{3+ij}{\sqrt{9+j^2}}},\qquad
\mathcal V_j^\mathrm{min}=3-\sqrt{9+j^2}.
\]
For \(j\neq0\), \(z_*(j)\neq1\), and
\[
\boxed{\begin{aligned}
\|F_\downarrow(z_*)\|_F^2&=4\left(1-\frac3{\sqrt{9+j^2}}\right),\\
\|F_\uparrow(z_*)\|_F^2&=2\left(1-\frac3{\sqrt{9+j^2}}\right).
\end{aligned}}
\]
**Proof.** \(\mathcal V_j=3-3\cos\phi-j\sin\phi=3-\sqrt{9+j^2}\cos(\phi-\operatorname{atan2}(j,3))\). Its minimum is unique; substitute the sine/cosine of the minimizer into the receipt formulas. QED.

For \(j=0\), the unique minimizer is \(z=1\), recovering S5/S6 flatness. **NO-GO (scope):** a phase-independent scalar burden contribution added to \(\mathcal V_0\) cannot select curvature. A scalar coupled through a *new* even function of \(\phi\) could change that result, but is a changed constitutive law, not a counterexample.

**Exact diagnostic**, not calibration: \(j=4\) yields \(z=(3+4i)/5\), \(\|F_\downarrow\|_F^2=8/5\), \(\|F_\uparrow\|_F^2=4/5\), \(U=6/5\), \(\mathcal V=-2\). No target THM-534 spectrum was used to choose \(j=4\).

## THM-534-S11 — Skew transport and exact local finite-step continuity [EXACT CONDITIONAL]

For any \(z\in U(1)\) define the skew-adjoint **chain-state amplitude** generator
\[
A_z=\begin{pmatrix}
0&B_1&0&0\\ -B_1^\dagger&0&N_z&0\\
0&-N_z^\dagger&0&B_3\\0&0&-B_3^\dagger&0
\end{pmatrix}\quad (A_z^\dagger=-A_z).
\]
Fix any real dimensionless step \(h\neq0\), or allow \(z=z_n\) and \(h=h_n\) to depend on the present state/history but remain finite and real. Define the implicit-midpoint/Cayley update
\[
\psi^{n+1}-\psi^n=h_nA_{z_n}\psi^{n+1/2},\qquad
\psi^{n+1/2}=\tfrac12(\psi^{n+1}+\psi^n).
\]
Then \(C_{h_n,z_n}:=(I-h_nA_{z_n}/2)^{-1}(I+h_nA_{z_n}/2)\) exists, is unitary, and the **total chain-state squared norm** is exactly conserved:
\[
\sum_{a=1}^{15}|\psi^{n+1}_a|^2=\sum_{a=1}^{15}|\psi^n_a|^2.
\]
More strongly, for every basis state \(a\) the exact finite-step receipt is
\[
|\psi_a^{n+1}|^2-|\psi_a^n|^2
=\sum_{b=1}^{15}J^{n+1/2}_{a\leftarrow b},\quad
J^{n+1/2}_{a\leftarrow b}:=
2h_n\operatorname{Re}\left(\overline{\psi^{n+1/2}_a}(A_{z_n})_{ab}\psi^{n+1/2}_b\right),
\]
with \(J_{a\leftarrow b}=-J_{b\leftarrow a}\).
**Proof.** Skew-adjointness makes \(I-hA/2\) nonsingular for real h and implies \(C^\dagger C=I\). The polarization identity
\(|b|^2-|a|^2=2\operatorname{Re}[\overline{(a+b)/2}(b-a)]\), together with the midpoint update, proves the local receipt. Skew-adjointness proves current antisymmetry and cancellation after summing all 15 sectors. This proof works even when \(z_n\) depends on the state at the beginning of every step. QED.

**No hidden physical conservation:** the conserved quantity is \(\|\psi\|^2\) in the declared metric, *not* energy, retained packet burden \(\rho\), \(U(z)\), nor an observable probability. The original topological differential remains nilpotent, but the separate covariant \(N_z\) has \(B_1N_z\neq0\), \(N_zB_3\neq0\); this is represented explicitly by \(F_\downarrow,F_\uparrow\), not silently claimed to preserve covariant nilpotency.

## THM-534-S12 — Endogenous oriented phase-current candidate [EXACT CONDITIONAL / NUMERICAL]

Define the **dimensionless** current readout from the present complex chain state at the marked incidence:
\[
j_n:=2\operatorname{Im}\left(\overline{\psi^n_e}\,q\,\psi^n_f\right),
\quad z_n:=z_*(j_n)=\frac{3+ij_n}{\sqrt{9+j_n^2}},
\quad \psi^{n+1}:=C_{h,z_n}\psi^n.
\]
This is a fully specified **candidate constitutive update** once \((e,f)\), \(h\), and \(\psi^0\) are supplied. It uses no empirical target to set a transition probability; it is **not** established as the unique UD source law.

**Gauge typing.** If all states and the reference boundary \(B_2\) transform covariantly under degreewise unitary basis changes, then \(\overline{\psi_e}(B_2)_{ef}\psi_f\) is invariant under the corresponding diagonal phase changes. Arbitrary non-diagonal basis mixing does not preserve the marked-incidence readout without an additional selection map.

**Nonflat existence witness.** Take \(\psi_e^0=1/\sqrt2\), \(\psi_f^0=iq/\sqrt2\), other components zero. Then \(j_0=1\), \(z_0=(3+i)/\sqrt{10}\neq1\), so both curvature receipts are nonzero. By S11 the subsequent finite-step update still conserves the total norm exactly.

**NUMERICAL:** An exploratory 30-step double-precision run with \(h=1/10\) found maximum local continuity residual \(6.11\times10^{-16}\), no total norm drift above \(10^{-13}\), and a strictly nonzero j over the tested interval. These are finite diagnostic computations, not independent evidence for UD physics.

**Real-subspace control.** If \(\psi^0\) is real in the declared oriented basis, \(j_0=0\), \(z_0=1\). Since the flat Cayley matrix is real, induction gives \(\psi^n\) real, \(j_n=0\) and \(z_n=1\) for all steps. Thus the candidate feedback does **not** spontaneously produce phase curvature from the purely real sector. A nonzero complex relative phase, signed source/boundary input or additional symmetry-breaking dynamics is required.

## THM-534-S13 — Burden-to-curvature bridge obstruction [OPEN / NO-GO UNDER RESTRICTED INPUTS]

The results above permit mathematical *source curvature plus total chain-amplitude continuity*. They do **not** derive a source from positive packet burden \(\rho\), a packet boundary influx, or a conserved physical stress-energy current. An admissible bridge must separately supply:
1. a native signed oriented \(j=j(\rho,\theta,\chi,\sigma,b;\,\text{seam},\text{context})\), including units, gauge transformation and a source-selection criterion for the marked incidence;
2. a packet burden law \(\Delta\rho+\delta J_\rho=S_\rho\) with explicit reservoirs/boundary accounts, then a independently checked total continuity receipt;
3. a physically justified normalization between the structural \(j\), the curvature diagnostic \(U\), the chain-state norm and any measured charge/current;
4. the generator/metric/event-time choice and an a priori stochastic or experimental readout;
5. a future held-out test with frozen acceptance criteria and non-constructor review.

A **scalar, phase-independent** packet burden term and the bare minimization of \(U\) alone select \(z=1\). Any nonflat response requires genuinely new oriented coupling, imposed boundary data, altered carrier/metric, or another rule. This is an exact scoped obstruction to inferring curvature solely from source-free closure, not a universal obstruction to UD transport.

## Source/exposure and status ledger

| Object | Status | Meaning |
|---|---|---|
| \(F_\downarrow,F_\uparrow,U(z)\) | EXACT CONDITIONAL | typed structural curvature/closure diagnostics |
| \(\mathcal V_j=U-j\sin\phi\) | CANDIDATE | added constitutive source coupling; not from frozen action |
| minimizer \(z_*(j)\), receipt identities | EXACT CONDITIONAL | follow for that explicitly defined functional |
| \(A_z\), Cayley local signed flux | EXACT CONDITIONAL | chain-state amplitude norm conservation, not packet burden |
| \(j_n=2\operatorname{Im}(\bar\psi_e q\psi_f)\) | CANDIDATE | gauge-covariant under declared diagonal transformations; link and map not uniquely source-selected |
| 30-step run, 10-step real control | NUMERICAL | constructor tests only |
| THM-534 probabilities (1/2,1/6,1/12) | SOURCE-BLOCKED | no microscopic derivation recovered |
| Born probabilities / physical time / SI unit bridge | OPEN_GATED | no promotion |
| Physical promotion | 0 | unchanged |

**Reopening criterion:** source-complete packet orientation/burden event rule selecting \(j\), the marked incidence and the event measure; verify physical burden continuity under that rule. No retrospective fitting to historical THM-534.

## Reproduction
- [Exact v0.6 symbolic and Cayley test](verify_thm534_covariant_source_v0_6.py).
- [Endogenous phase feedback and real-sector negative control](verify_thm534_endogenous_phase_v0_6.py).
- Local constructor replay PASS on both scripts, 2026-10-21. Independent reviewer: PENDING. No registry entry, no physical promotion.
