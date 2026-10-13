# Correlated boundary memory and thermal collisions

2026-10-13. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Outcome and declared inputs

This calculation replaces the single-carrier face alphabet by a declared tensor-product memory on the exposed boundary of the five-tetrahedron complex. It derives its full correlated Gibbs entropy, gives a local energy-conserving thermal collision, and tests coarse-to-fine consistency. The construction is a candidate physical extension. Native UD supplies the finite boundary incidence graph; it does not yet supply the memory tensor factors, coupling J, temperature T, bath supply, scheduling, carrier-to-memory write interaction, or horizon interpretation. G05 and G06 remain source-open in the supplied coefficient ledger. No gravitational constant is used.

Crucially, thermal memory entropy is denoted S_M rather than S_rec. An independently thermalized memory is not a record of the carrier. Its mutual information with that carrier is zero.

## 1. A many-body state on the actual boundary

The core tetrahedron with one attached tetrahedron per core face has twelve exposed triangles. The dual graph G has one vertex per exposed face and one edge per shared boundary edge. Exact enumeration gives N=12, M=18, degree three at every vertex. Thus one candidate binary memory per face has Hilbert space (C²) tensor-powered twelve times, dimension 4096. This is an added physical state space; it is not the earlier 47-dimensional simplex chain register.

For spin labels s_i in {−1,+1}, declare the diagonal Hamiltonian

\[
H_M(s)=J\sum_{(i,j)\in E(G)}(1-s_is_j)=2Jk(s),\qquad J>0,
\]

where k counts disagreeing neighbor pairs. Declare beta=1/(k_B T), T>0, and x=exp(−2 beta J). The Gibbs memory state is

\[
\tau_M=\sum_s \frac{x^{k(s)}}{P(x)}|s\rangle\langle s|,
\qquad P(x)=\sum_s x^{k(s)}.
\]

The exact partition polynomial from all 4096 configurations is

\[
\begin{aligned}
P(x)={}&2+32x^3+66x^4+120x^5+296x^6+480x^7\\
&+582x^8+720x^9+768x^{10}+576x^{11}\\
&+310x^{12}+120x^{13}+24x^{14}.
\end{aligned}
\]

The coefficients sum to 4096 and the two zero-disagreement states are the aligned configurations. All boundary loops are retained. No independent-face approximation is used.

With natural logarithms,

\[
\langle k\rangle=\frac{xP'(x)}{P(x)},\qquad
\boxed{\frac{S_M}{k_B}=\ln P(x)-\ln x\,\frac{xP'(x)}{P(x)}}.
\]

At the declared rational replay point x=1/3, not selected by native UD,

\[
P(1/3)=\frac{2^{23}}{3^{13}},\qquad\langle k\rangle=\frac{11}{4},
\qquad S_M=k_B\left(23\ln2-\frac{41}{4}\ln3\right).
\]

The mean energy is (11/2)J. The displayed entropy is about 4.68161 k_B, compared with the maximum 12 k_B ln2. These fractions and logarithm coefficients follow from the declared state, not from gravitational matching.

## 2. Exact energy-conserving local update

Fix one face i and hold its three neighbor labels z fixed during the update. Their signed sum m is ±1 or ±3. The lower-energy label agrees with their majority, and the higher-energy label h=1 has gap g=2J|m|, hence g is 2J or 6J.

Supply two fresh bath qubits, with Hamiltonians 2J n_2 and 6J n_6, in their independent Gibbs states at the same beta. Their excitation probabilities are

\[
q_2=\frac{x}{1+x},\qquad q_6=\frac{x^3}{1+x^3}.
\]

Conditioned on the neighbor basis labels, swap the memory's energy-ordered bit h with the bath qubit having the matching gap. Leave the other bath qubit unchanged. The neighbors themselves are unchanged. This defines a permutation unitary V_i on memory and the two bath bits.

In each neighbor block, the memory energy has the form E_rest(z)+E_min(z)+g h. A swap with a bath bit of the same gap conserves g(h+b), so

\[
[V_i,H_M+H_B]=0.
\]

The checker verifies this on every basis state for all twelve sites: 196608 energy and involution checks. Tracing the used bath replaces the selected memory bit by its conditional Gibbs distribution. Because the bath state is initially independent of the memory, the conditional preparation does not smuggle in pre-existing neighbor/bath correlations. The neighbor dependence occurs in the unitary, not in bath initialization.

This construction avoids the earlier stationary-apparatus obstruction because it implements a thermal population update for a diagonal memory Hamiltonian, rather than simplex dephasing of the noncommuting native carrier Hamiltonian. It does not solve the carrier recording problem.

At x=1/3, the bath excitation probabilities are exactly 1/4 and 1/28. Selecting a site uniformly gives a Markov kernel with exact detailed balance against tau_M, checked on all 49152 oriented single-bit flips. Every flip probability is positive at finite beta J; the chain is irreducible and has self-loops, so tau_M is its unique stationary distribution.

Energy conservation is a scoped property of this collision. Timing, preparing and routing fresh baths, retaining outgoing baths, and eventually resetting resources remain part of a complete apparatus model. The construction does not supply a native clock or an autonomous local control implementation.

## 3. Entropy, heat and record stability

For a memory state initially independent of a fresh Gibbs bath, each collision satisfies

\[
\Delta S_M+\frac{Q_B}{T}
=k_B\{I(M':B')+D(\rho_B'\Vert\tau_B)\}\ge0,
\]

where Q_B is the bath energy increase. This follows directly by adding I=Delta s_M+Delta s_B and D=beta Q_B−Delta s_B. Since the collision conserves free energy expectation, Delta E_M=−Q_B. Heat and entropy now have an explicitly declared microscopic account.

At the Gibbs stationary state, tau_M tensor tau_B is the Gibbs state of H_M+H_B and is invariant under V_i. Hence mean heat and entropy production vanish at stationarity. Memory entropy remains positive. Random equilibrium fluctuations are not irreversible accumulation of records.

The update also limits static retention. At x=1/3, for every configuration the probability of leaving it during one uniform-site update is at least 1/28. The probability of no departure over r updates is at most (27/28)^r and the mean first departure time is at most 28 update attempts. These are configuration-retention bounds, not logical-bit lifetime bounds; revisits and collective encodings are different questions. There is no physical time conversion without a source for the attempt rate.

If tau_M is prepared independently of the carrier and all these collisions act only on M+B, then I(C:M)=0 throughout. The entropy above is a memory state statistic and potential local information capacity. To call it record-formation entropy requires an actual carrier-dependent write process, a retained distinguishability observable, and a lifetime criterion. Neither entropy nor spatial placement alone supplies those properties.

## 4. Conditional extensive entropy and area

An exactly soluble comparison uses a connected spanning tree of the dual graph. Choosing the tree is an additional candidate input and need not preserve the full boundary symmetry. On an N-node tree, the root bit and N−1 disagreement bits give a bijection with configurations, so

\[
P_{\rm tree}(x)=2(1+x)^{N-1},\quad q=\frac{x}{1+x},
\quad\frac{S_{M,\rm tree}}{k_B}=\ln2+(N-1)h(q).
\]

The checker independently enumerates the twelve-node tree and verifies its disagreement multiplicities 2 binomial(11,k). With equal face areas a0 and A=N a0,

\[
S_{M,\rm tree}=\frac{k_B h(q)}{a_0}A+k_B[\ln2-h(q)].
\]

This is an exact conditional area law for the tree memory. It retains correlations and fixes its coefficient from declared J/T and a0. It is not a native horizon-area law.

For the full looped graph, a single coefficient cannot be inferred from the tree result. For any finite ferromagnetic graph of maximum degree d, the conditional probability of a spin given all others lies between q_d and 1−q_d, where q_d=1/(1+exp(2 beta J d)). Therefore H(s_i|others)>=h(q_d). Conditioning on only previous spins gives entropy no smaller. The chain rule yields

\[
N h(q_d)\le S_M/k_B\le N\ln2.
\]

For degree-three boundary graphs at fixed finite J/T and fixed a0, this proves positive extensive entropy bounds without independence. It does not prove convergence to a unique entropy density for an unspecified family. The family, couplings, boundary conditions and physical area scale must be supplied independently. On the twelve-face graph at x=1/3, q_d=1/28 and the bound is verified.

Large-area growth with fixed patch area must be distinguished from finer resolution of a fixed-area boundary.

## 5. Refinement does not preserve the chosen thermal state automatically

As a minimal graph-refinement test, subdivide one tree edge by adding an intermediate spin. Give each new edge coupling J' and let x'=exp(−2 beta J'). Summing over the inserted spin gives weight 1+x'^2 for equal endpoints and 2x' for unequal endpoints. Thus

\[
x_{\rm eff}=\frac{2x'}{1+x'^2},\qquad
\tanh(\beta J_{\rm eff})=\tanh^2(\beta J').
\]

Keeping the original coupling unchanged on both new edges changes the coarse state. For x'=1/3, x_eff=3/5, not 1/3. Preserving an original x instead requires the new value

\[
x'=\frac{x}{1+\sqrt{1-x^2}}.
\]

This is only an edge-series refinement test, not a full tetrahedral subdivision law. It already shows that a coupling map is needed.

Even with exact coarse-marginal matching, joint entropy obeys

\[
S_{\rm fine}=S_{\rm coarse}+k_B H(\mathrm{new\ labels}\mid\mathrm{coarse\ labels}).
\]

The extra conditional entropy is strictly positive for finite-temperature full-support inserted spins. Exact preservation of total entropy at unchanged area requires deterministic new labels, or retaining the original coarse readout, or an independently derived renormalized entropy convention. Therefore thermalizing every newly introduced face at fixed J/T does not provide a resolution-independent physical entropy density.

## Disposition and next source gate

CHECKED: full correlated finite partition polynomial; exact Gibbs entropy; local energy-conserving bath collision; detailed balance; conditional extensive bounds; spanning-tree area coefficient; refinement coupling mismatch; zero carrier information under independent preparation.

CANDIDATE: boundary tensor factors, Ising energy, bath spectrum, J/T, area metric, site schedule and tree comparison. OPEN: native carrier-to-memory coupling, prepared blank/resource account, logical retention, refinement state map, continuum density, horizon identification and gravitational normalization.

Next, construct and test a carrier-dependent write interaction together with its resource state. Require nonzero carrier/record information, a stated retention criterion, and explicit energy conservation/work accounting. The exact Gibbs entropy above cannot substitute for that recording derivation.

No ledger, registry, website or repository entries were changed. Physical promotion remains 0; independent review OPEN. Gap2_FINAL_Finite_Genesis.png remains unavailable and was unused.
