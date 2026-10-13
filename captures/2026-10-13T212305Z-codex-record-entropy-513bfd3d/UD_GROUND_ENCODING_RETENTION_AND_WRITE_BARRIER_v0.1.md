# Ground encoding, retention and write barrier

2026-10-13. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Result and scope

The next controlled comparison changes the memory encoding while preserving the prior binary carrier test, boundary graph, Ising Hamiltonian and thermal update rule. A complementary ground-state encoding substantially improves finite-step retention over the one-hot word. It has zero net endpoint work for the real carrier test states, but a 10J single-bit transition barrier, a prepared orientation resource, and a driven carrier control. It encodes one bit in twelve memory factors and is not an extensive horizon-area record law.

The native face projector is the source anchor. Memory factors, J, temperature, blank preparation, control and update scheduling remain declared candidates. Ledger G05/G06 remain open. No gravitational constant is used.

## 1. Complementary ground-state write

Let A=P_f be the projector onto the exposed face used in the earlier binary test. R=0 prepares the interior core cell and R=1 prepares that face, each with probability 1/2. The twelve-bit blank is |0^12>. Let F=product_i X_i, the global bit complement. Declare

\[
U_g=(I-A)\otimes I+A\otimes F.
\]

This unitary writes |0^12> for R=0 and |1^12> for R=1. The two pointer words are orthogonal and give exact initial readout, I(R:M)=ln2. As before, a pulse generator (pi hbar/2 tau) A tensor (I−F) implements this controlled unitary in the interaction picture. Its laboratory implementation requires timed drive control; the collective operator F is not a local single-bit interaction.

The memory Hamiltonian is H_M=J sum_edges(1−Z_iZ_j)=2J k(m). Complementing both ends of every edge leaves each product Z_iZ_j unchanged, hence

\[
[F,H_M]=0.
\]

Both written ground words have H_M=0. More generally the global complement preserves memory energy for every input word. The controlled write can therefore bypass a memory barrier if its collective generator is available, but this availability is an added control assumption.

The carrier marginal is pinched into A and I−A. With H_C=i epsilon B_K and real test inputs, its mean energy change is zero. Consequently the net endpoint pulse work is exactly zero for this test. For general rho it is the carrier backaction term

\[
W_g=\operatorname{Tr}\{[AH_CA+(I-A)H_C(I-A)-H_C]\rho\}.
\]

The write remains noncommuting with native carrier energy and requires a control resource. Zero net endpoint work is not zero drive strength, zero resource preparation, zero full-cycle cost, or a native energy-conserving recorder.

For the connected boundary graph, the only zero-disagreement words are all-zero and all-one. Therefore, among XOR writes from the fixed blank, all-one is the unique nontrivial codeword minimizing endpoint memory energy. This is an exact endpoint-energy optimization, not a claim that this encoding is globally optimal for logical lifetime or capacity.

## 2. Exact local energy barrier

Restrict implementation to paths of single-bit flips from blank to all-one. A configuration S has energy 2J times the number of boundary graph edges crossing S and its complement.

For monotone paths, dynamic programming computes

\[
b(\varnothing)=0,\qquad
b(S)=\max\{k(S),\min_{i\in S}b(S\setminus\{i\})\}.
\]

The optimum is b(all)=5, corresponding to peak memory energy 10J. A witness flip order and each intermediate energy are included in results.json. An independent threshold-reachability calculation allows arbitrary single-bit flips, revisits and nonmonotone paths. The all-one word is unreachable within energies at most 8J and reachable within at most 10J. Thus the unrestricted single-bit path barrier is also exactly 10J.

This is a classical configuration-path barrier. It is not a lower bound for arbitrary coherent collective control, and no Arrhenius lifetime or physical time is inferred from it. Sequential writes can require transient positive work and later recover energy even when net endpoint work is zero. Their dissipative losses and intermediate carrier backaction are not supplied by this graph calculation.

## 3. Retained distinguishability under the same bath

Use the previous uniform-site Gibbs resampling kernel at x=exp(−2 beta J)=1/3. Its per-update probabilities have denominator 336. Global complement is an exact symmetry of the kernel, so if p_r(m) is the distribution after r updates from all-zero, the distribution from all-one is p_r(complement(m)). The replay checks the symmetry for every memory word.

The optimal full-word readout error is

\[
D_r=\frac12\sum_m|p_r(m)-p_r(\bar m)|,
\quad P_{\rm err}^{\rm opt}=(1-D_r)/2.
\]

A feasible alternative measures all bits and uses majority vote, breaking ties randomly. Its error is computed exactly and is always at least the optimum. The replay uses integer path weights, reports exact rational probabilities and energies, and checks monotonicity of D_r through 128 updates. Logarithmic information is reported as a floating display value.

| Thermal updates | Ground encoding optimal error | Majority error | Earlier one-hot optimal error |
|---|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1/24 |
| 2 | 0 | 0 | 0.079383 |
| 4 | 0 | 0 | 0.144307 |
| 8 | 0.00001274 | 0.00001375 | 0.236741 |
| 16 | 0.00075667 | 0.00077078 | 0.332874 |
| 32 | 0.00923883 | 0.00934834 | 0.411147 |
| 64 | 0.04717227 | 0.04749628 | not computed previously |
| 128 | 0.13624588 | 0.13659575 | not computed previously |

Finite-step zero error has a direct support proof: after r single-site updates, no word can be more than r Hamming flips from its initial word. The radius-r supports about all-zero and all-one are disjoint for r<=5. The first overlap is possible at r=6. This protects distinguishability while configurations may already have changed; static configuration survival and logical retention are different quantities.

The calculation gives zero error for updates 0 through 5, and nonzero error thereafter. At 32 updates, I(R:M) is approximately 0.667610 nats, compared with approximately 0.028799 for the earlier one-hot encoding. Exact rational errors rather than display logarithms certify the retention comparison.

The finite thermal chain remains irreducible. Both initial codewords eventually converge to the same Gibbs state, so D_r tends to zero, error tends to 1/2, and recorded reference information tends to zero. There is no indefinitely stable finite-temperature memory here.

## 4. Energy and preparation accounting

The two conditional distributions have equal mean memory energy by complement symmetry. Initial memory energy is zero and, with energy-conserving bath collisions, cumulative mean bath heat is minus the memory energy increase. At equilibrium the memory energy is 11J/2, so cumulative mean bath heat tends to −11J/2. Thermalization supplies energy to the memory while eventually erasing the logical label. A sign of mean heat does not determine retention.

The finite-temperature Gibbs memory is exactly invariant under F, so using that pointer produces identical outputs for R=0 and R=1: D=0 and I(R:M)=0. The collective encoding requires preparation that selects an orientation. Even a zero-temperature equal mixture of the two ground words would be invariant and would not record the label under this XOR write. Low mean energy alone is insufficient.

A pure oriented blank has higher free energy than the finite-temperature Gibbs state by k_B T ln P(x). This preparation resource remains separate from the zero endpoint write work. Exact pure preparation with a finite full-rank bath is not furnished by this candidate. Resetting an unknown fair ground-encoded logical bit to the same oriented blank, without usable source-label information, raises memory free energy by k_B T ln2 under isothermal accounting. A reusable apparatus cannot infer zero cycle cost from zero write work.

## 5. Implication for entropy and area

This encoding improves retention by spending twelve memory factors on a single label. Its logical record entropy is at most k_B ln2, regardless of assigning all twelve exposed faces to that one code. It therefore does not provide a positive extensive record density as the boundary grows. The Gibbs entropy and the logical record entropy must remain typed separately.

The next comparison should jointly constrain logical capacity, readout error at a declared horizon of updates, and complete resource cost. Independent small encoding patches might provide extensive capacity, but their coupling, boundary interfaces and source-selected write rules must be derived. The present result supplies a controlled retention benchmark, not that construction.

## Disposition

CHECKED: collective write; unique minimum endpoint-energy nontrivial XOR codeword; exact 10J local path barrier; thermal complement symmetry; retained optimal and majority readout errors; preparation dependence; eventual information loss.

CANDIDATE: collective drive, symmetry-breaking pointer preparation, memory and bath Hamiltonians, clock and routing. OPEN: native autonomous source law, physical calibration and retention, many-bit density, refinement consistency and horizon map. Ledger, registry, repositories and site unchanged. Physical promotion 0; independent review OPEN. The unavailable Gap2_FINAL_Finite_Genesis.png was unused.
