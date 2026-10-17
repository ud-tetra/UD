# Finite Stock Acquisition: Joint Write, Disturbance and Preparation Cost

Version 0.1 | 15 October 2026 UTC | Development; physical promotion 0

The next missing interface was a finite instrument behind the bounded-error stock values. The construction below supplies one in a separately declared quantum encoding. It exposes two costs hidden by passive readout: strong measurement changes the observed carrier, and estimating its unperturbed stock values can require a large bank of fresh independent preparations.

The result is a conditional implementation and obstruction package. It does not infer that UD's real amplitudes are quantum states, that a boundary supports these registers, or that pure donor production has a normalized thermodynamic price. The known deterministic fixture can be calculated without a sensor; its role here is a common finite target for comparing observation contracts.

**Derived:** unitary write and full joint state; reduced instrument; exact disturbance and information-loss witnesses; finite-confidence sampling bound; pulse norm upper bounds; exact correlation-exporting renewal.

**Supplied:** amplitude encoding, independent preparations at the scan instants, pure pointer/record blanks, controlled pulses, free-flow cancellation, Born readout, timing, counting and retention.

**Open:** native realization, autonomous controller, physical spatial locality, thermal blank production, calibrated work/area and a horizon entropy density. Full inherited manuscript results are not all replayed. No independent review is claimed.

The report's D.18 section is reproduced verbatim in the revised manuscript, whose references [15] and [31]-[33] identify the primary background and companion evidence. The finite implementation is a construction; the no-disturbance statement is a no-go under its explicitly quantified premises.

## D.18 A finite acquisition instrument: outcomes, disturbance and supplied ensembles

### D.18.1 Declared encoding and an explicit write

The passive stock contract of D.16 supplies numbers close to $q_p=x^TD_px$. It does not supply an interaction that reads those numbers. Here we declare an auxiliary quantum implementation and expose its costs. This is a candidate bridge, not a consequence of the real carrier. Supply $R>0$, the encoding $|\psi_x\rangle=x/R\in\mathbb C^{15}$, and three mutually orthogonal rank-two edge-pair projectors $P_1,P_2,P_3=D_A,D_B,D_C$. Set $P_0=I-\sum_{j=1}^3P_j$, of rank nine. Then $p_j=\operatorname{Tr}(P_j\rho)$ and, for the encoded pure state, $q_j=R^2p_j$.

Supply two four-level registers $M,F$ in the independent pure blank $|00\rangle$. With $X_4|r\rangle=|r+1\pmod4\rangle$, apply

\[
U=\sum_{j=0}^3P_j\otimes X_4^j,
\qquad V=\sum_{r=0}^3|r\rangle\langle r|_M\otimes X_{4,F}^r.
\]

Orthogonality of the controls makes both operators unitary. The complete output is

\[
\Omega_{CMF}=\sum_{j,l}P_j\rho P_l\otimes|jj\rangle\langle ll|,
\quad
\Omega_{CM}=\sum_jP_j\rho P_j\otimes|j\rangle\langle j|.
\]

Tracing the explicitly counted register $F$ produces the second expression. No uncounted dephasing bath is needed for this mathematical channel. A supplied standard-basis readout of $M$ gives outcome $j$ with probability $p_j$ and conditional carrier $P_j\rho P_j/p_j$ when $p_j>0$. Standard instrument definitions are given in [32, §2.3.2]; the finite dilation above is specified here in full. It writes one four-valued outcome, not three exact probabilities. The Born readout and its downstream controller remain supplied operations.

For a pure input, the full output remains pure, while $S(M)=S(MF)=H(p)$ and $I(M:F)=H(p)$, in natural units. The sum of the two marginal entropies is $2H(p)$, not their joint entropy. Discarding $F$ is a coarse-graining, not proof of irreversible entropy production.

### D.18.2 Retention and back-action have different targets

Ignoring the record sends the carrier to $\Phi(\rho)=\sum_jP_j\rho P_j$. Within-block coherence survives; coherence between blocks does not. For a two-block pure state $\sqrt p\,|e\rangle+\sqrt{1-p}\,|v\rangle$,

\[
D_{\rm tr}(\rho,\Phi(\rho))=\sqrt{p(1-p)}.
\]

At $p=1/2$ this disturbance is $1/2$. The two orthogonal states $(|e\rangle\pm|v\rangle)/\sqrt2$ give identical record distributions and identical reduced carriers. Their complete joint outputs remain orthogonal because the write is an isometry. Thus a retained stock outcome does not retain every carrier distinction in an accessible marginal.

For two supplied hypotheses with probabilities $p^{(0)},p^{(1)}$, the memory distance is $\frac12\sum_j|p_j^{(0)}-p_j^{(1)}|$; equal-prior optimal error is one half of one minus this distance. For $m$ independent preparations, replace these distributions by their product distributions. Counts are sufficient for this particular discrimination problem: grouping sequences with equal counts leaves total variation unchanged. As an exact small example, four Bernoulli outcomes with parameters $1/4$ and $3/4$ have distance $11/16$ and error $5/32$. This is retained distinguishability of declared hypotheses, not information about an unspecified universe.

Returning the measured carrier to free evolution gives an interleaving of $\Phi$ and $e^{sA}$, rather than the unmeasured trajectory. A unit vertex preparation illustrates the failure directly: immediately after the complete write and record reduction, every stock derivative vanishes, since the original generator couples adjacent degrees and $\Phi(\rho)$ has no coherences between an edge pair and its adjacent degrees. An unmeasured unit vertex instead has $q_p(s)=\sin^2(2s)/4$, with nonzero derivative at generic sampling times. A fresh-ensemble protocol can estimate the unperturbed stocks; repeated strong measurement of the same carrier cannot silently inherit that contract.

There is also an exact passive-readout obstruction. If an isometry leaves every admitted pure carrier unchanged, $W|\psi\rangle=|\psi\rangle|r_\psi\rangle$, preservation of inner products implies $\langle r_\psi|r_\phi\rangle=1$ whenever $\langle\psi|\phi\rangle\ne0$. On a connected family of nonorthogonal states all records are the same, up to immaterial phases. An exact universal stock record with zero disturbance is therefore unavailable under that contract. Orthogonal promises, state preparation information and approximate instruments are different contracts.

After the contacts are off, exact retention follows only under the supplied factorization $H_{\rm bg}=H_{MF}+H_{\rm rest}$, including every spectator, with the record basis stationary or its known free evolution retained. A uniform full-joint generator mismatch of norm at most $d$ over duration $t$ gives comparison distance at most $\min\{1,td\}$. If the two hypothesis outputs have respective retention errors $\delta_0,\delta_1$, triangle inequalities give retained memory distance at least $\max\{0,D_{\rm ideal}-\delta_0-\delta_1\}$. These are conditional protection bounds, not a derived isolation mechanism; any such errors enter the operation budget below.

### D.18.3 A finite-confidence bridge to the sampled contract

For normalized stocks, supply $m$ independent copies of $\rho_k$ at each of $K$ sample instants. These are new preparations, not clones made from a single unknown input. Apply the instrument to each copy and set $\widehat p_{jk}=N_{jk}/m$. One multinomial trial samples all three indicators, which are mutually exclusive and need not be independent of each other. Independence across copies at a fixed tick suffices. Hoeffding's bound and a union bound give

\[
\Pr\{\max_{j=1,2,3;k}|\widehat p_{jk}-p_{jk}|>\epsilon\}
\le 6K e^{-2m\epsilon^2}.
\]

No independence across ticks is needed for that union bound. For completeness, the scalar exponential estimate follows by writing $f(t)=\log\mathbb E e^{t(X-\mathbb EX)}$ for $X\in[0,1]$. Under exponential tilting $f''(t)$ is a variance, at most $1/4$, so $f(t)\le t^2/8$. Multiplication across independent trials, Markov's inequality, optimization at $t=4\epsilon$, and both signs give $2e^{-2m\epsilon^2}$. This is the standard concentration method of [33], not a UD-specific law.

Choose the D.16 normalized fixture, $K=129$, $\epsilon=1/128$, and the explicit sufficient allocation $m=98304$. The failure bound is $774e^{-12}<1/100$. This is a conservative construction, not a sample-complexity lower bound or an optimized sensor. It needs $Km=12681216$ independently prepared carrier inputs. The actual bound is approximately $0.004756$; the strict $1/100$ certificate uses a rational lower Taylor bound on $e^{12}$.

Use the exact rational counts directly in the certified guards: rise if $N_{jk}/m-\epsilon\ge h$, fall if $N_{jk}/m+\epsilon\le\ell$. No additional six-bit quantization error is charged or silently omitted. On the joint good event the D.16 reach, persistence and slope premises imply the same $D=11/192$ detection-delay and per-address word contract, with the same exclusions for global order and endpoint coverage. The guarantee is now probabilistic. An actual joint preparation bank within trace distance $\eta$ of the ideal product bank and a full-joint operation comparison error $\gamma$ raise the failure bound by at most $\eta+\gamma$. Correct single-copy marginals alone do not establish independence or this bank bound.

Sample times refer to the input snapshots. If writing and processing finish after a bounded latency $L$, the completion delay is at most $D+L$. Completion timestamps need that latency interval; they cannot be treated as input times. Parallel banks or adequate throughput, preparation scheduling, clock calibration and processing are explicit extra resources. A known deterministic fixture can instead be calculated from its known preparation; the large ensemble is a readout construction for unknown supplied states, not information newly learned from an already known trace.

### D.18.4 Local controls, renewal and a resource ledger

An exact switched implementation exists in the supplied register model. Choose Hermitian logarithms $K_j$ with $e^{-iK_j}=X_4^j$, $\|K_j\|\le\pi$. A pulse of duration $\tau>0$ generated by $\sum_jP_j\otimes K_j/\tau$ implements $U$; a second pulse controlled by $M$ implements $V$. Each pulse has norm at most $\pi/\tau$. The first control is diagonal in the carrier simplex basis and couples only edge-coordinate populations to the pointer; the second couples pointer to record. This specifies register locality. A shared four-level bus, addressing, switching and any geometric implementation are supplied, so spatial locality on a physical tetrahedral boundary is not proved.

To keep the input fixed during these pulses, a running free generator $H_C=i\chi A$ is cancelled by a supplied control, or equivalently a justified interaction-picture implementation must be supplied. Here $\chi>0$ is an uncalibrated auxiliary energy/rate scale in the convention $\hbar=1$. With zero bare register energies, the explicit cancellation construction has integrated control norm bounded by $2\pi+2\tau\chi\|A\|$ per trial. This is an upper bound for the stated implementation, not a lower bound on work. Finite pulse widths and this cancellation cannot be replaced by a claim of free instantaneous measurements.

For real encoded inputs and these degenerate record Hamiltonians, initial and final mean carrier energy are both zero: a real symmetric density has zero trace against $iA$, also after $\Phi$. A cyclic externally switched interaction therefore has zero signed mean work under the bare-energy-change convention. Its nonzero disturbance, supplied pure blanks, pulse demand and discarded correlations remain. Zero signed work is compatible with a costly preparation/controller; it is not a complete physical energy budget.

Exact renewal swaps each used $MF$ pair with an independent new pure blank pair. Including every retained spectator $Y$, this sends $\rho_{MFY}\otimes|00\rangle\langle00|_{D}$ to $|00\rangle\langle00|_{MF}\otimes\rho_{DY}$. All correlations move to the spent donor. Its storage or further processing must be charged. This protocol has no thermal bath: a pure donor is supplied afresh at each renewal. Preparing that donor from a finite-temperature bath is a separate operation, with its Hamiltonian, work source, errors and exhaustion still required. Thermal erasure claims need those premises [15].

For the above allocation the input/record ledger is:

| Resource | Explicit allocation or boundary |
| --- | --- |
| Carrier preparations | 12681216 independent 15-level inputs; preparation and synchronization supplied |
| Blank pointer plus record supply | Two four-level pure registers per trial |
| Capacity if both raw register streams are retained | 50724864 qubit equivalents; entropy and useful information can be smaller |
| Current three count registers | 51 bits, with exact rational comparisons; fourth count follows from the total |
| All three-count summaries retained | 6579 bits over 129 ticks; raw registers require separate renewal/disposal |
| Trial counter and scan counter | 17 bits and 8 bits respectively, plus the prior response/mask and configuration registers |
| Controlled write pulses | Two per trial, plus cancellation, readout, arithmetic, retention and routing operations |
| Time and parallelism | At least the declared pulse durations per lane; sufficient throughput or parallel lanes must be supplied |
| Energy, geometry, bath renewal | Model scales/control bounds declared above; calibrated joules, physical area and thermal production of blanks remain OPEN |

The summary archive is not a reversible reset of the raw outputs: computing counts while retaining their inputs leaves the inputs and their correlations somewhere. An entropy or information-per-area comparison must include that destination and the preparation bank. The derived result closes an explicit auxiliary write and finite-confidence estimation interface, with a demonstrated disturbance obstruction. It does not close autonomous acquisition, native event selection, complete thermodynamic cost or a horizon-area normalization [31].

## Review and next closure order

1. Replace the supplied preparation bank with an explicit finite preparation source and synchronize it with acquisition; bound its joint error and exhaustion.
2. Derive a weak or otherwise back-action-aware observer on the same evolving carrier, then compare accuracy, latency, disturbance and consumed preparation capacity against this strong-measurement baseline. Optimal allocation is open.
3. Supply an autonomous counting/readout/controller and donor-production mechanism with Hamiltonians. Only then compare energy and retained information under a common retention/error target.
4. Supply the physical area/metric map before comparing any apparatus capacity to boundary area. No value of G or horizon density is inferred here.

The replay constructs incidence, controls, full write isometry, partial traces and finite certificates independently of imported working-note code. Its 26 finite check families validate examples and identities; the written general proofs carry the concentration, no-disturbance and error-composition conclusions. Constructor verification is not non-constructor peer review.
