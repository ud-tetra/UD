# UD local-source selection: a gated edge, score transport and conditional retention

Version 0.1 | 15 October 2026 UTC | Development; no registry entry | Physical promotion 0

## Result

A declared local edge-contact gate can turn the six-way fibration-score tie of a single-vertex input into a unique preference. This supplies an explicit finite mechanism beyond the preceding free-flow conservation theorem. It does not derive the localized preparation, occurrence of the gate, its clock, or an irreversible physical record from native UD.

On the regular 600-cell boundary with unit incidence metric, start from a unit vertex amplitude e_u. Close the two vertex contacts of one incident edge during 0≤t≤tau, with tau=1/100 in model-time units. Keep all other contacts and the simplex registers. Restore the free generator afterward. The selected right-quaternion fibration H_e is the unique cyclic subgroup determined by that edge. At the end of the pulse, its score exceeds each of the five competitors by at least

\[
\boxed{\Delta_* = \frac{17}{12500000}>0.}
\]

The mathematical score gap is conserved after restoration of the symmetric generator. The required switching and source choice are supplied. A fixed closed static machine is not shown to create a permanent robust preference autonomously, and the selected label has not been physically acquired into memory.

The new replay passes 21 exact finite/algebraic checks and two separately labelled numerical corroborations. It includes exact Taylor coefficients, subgroup symmetry, norm and timing bounds, source-kernel counts and two useful no-go tests. Its numerical endpoint gap is approximately 9.996e-6; that value corroborates the smaller rigorous bound and is not used to prove it. Constructor checking is not independent review.

## 1. State and operators

Use the preceding real carrier C0⊕C1⊕C2⊕C3 of dimension 2640, sorted oriented simplex bases and unit simplex metric. Let A(a,b,c) be its skew incidence generator. The six right-quaternion cyclic subgroups H of order ten define real orthogonal projectors

\[
\Pi_H=\frac1{10}\sum_{h\in H}\rho(h),\qquad
s_H(x)=x^T\Pi_Hx=\|\Pi_Hx\|^2.
\]

Each projector has rank 264. Free dynamics commutes with all six. These are the zero-character coherence scores of the preceding declared selector; they are not six probabilities that must sum to one.

For an oriented edge e=(u,v), let b_e=B1 e_e be its signed endpoint vector. Thus ||b_e||=sqrt(2). Define the real skew response supported on that edge register and its two endpoint registers:

\[
E_e=\begin{pmatrix}0&-b_e e_e^T&0&0\\
e_e b_e^T&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
\qquad \|E_e\|=\sqrt2.
\]

An orientation change of the edge is accompanied by its chain-basis sign change; it does not change the underlying candidate contact rule. The edge remains a simplex with a register. This operation is a contact gate, not simplicial edge deletion or a Pachner move.

The running response is L=A(a,b,c)+gamma E_e. Its effective coefficient on the selected vertex–edge contact is a+gamma. A hard closure has gamma=−a, so that coefficient becomes zero. The norm ||x|| is conserved for every real gamma. This preserves the carrier support norm, not a calibrated physical energy.

This response has a source-bound connection to the historical ledger's Q167 masked vertex–edge support flow, while Q173 concerns the separate face-contact lane. Extending a mask to the declared global carrier specifies a mathematical response interaction. The ledger does not provide a source law predicting which mask changes or when. Its Q153 constitutive source and G05 action normalization remain open.

## 2. Score-flow law

For fixed H and x'=Lx, skewness and [A,Pi_H]=0 give

\[
\dot s_H=\gamma x^T[\Pi_H,E_e]x
=2\gamma(\Pi_Hx)^T E_e(I-\Pi_H)x.
\]

Writing kappa_H=||Pi_H E_e(I−Pi_H)||≤sqrt(2) and ||x||=R,

\[
|\dot s_H|\le2|\gamma|\kappa_H\sqrt{s_H(R^2-s_H)}
\le |\gamma|\kappa_HR^2.
\]

The gate can transfer coherence weight between the H-invariant component and its orthogonal complement. These are closed norm transfers, not entropy-production terms. The formula remains valid with a supplied time-dependent gamma(t); it does not determine gamma(t).

For a pair of candidate fibrations put Q=Pi_H−Pi_J and g_HJ=x^TQx. Since Q is a difference of orthogonal projectors, ||Q||≤1. For a unit state, a residual skew perturbation F during intended free retention gives |dot g_HJ|≤2||F||. This provides the retention-error bound below.

## 3. A unique fibration from one local edge

Take u to be the identity quaternion vertex, which loses no generality by left symmetry. Every incident neighbor v is an element with scalar part cos(pi/5), hence generates a cyclic subgroup H_e=⟨u^(-1)v⟩ of order ten. Reversing the edge replaces its relative quaternion by its inverse and leaves the subgroup unchanged.

There are twelve incident edges at each vertex, two associated with each of the six H. The source vertex and edge are the only geometric labels supplied. H_e is calculated from them; an entire fibre or a global fibration label is not separately supplied to the gate.

For the initial state x(0)=e_u, every s_H(0)=1/10. Thus the preparation localizes a vertex but initially selects none of the six axes. This input is not a fully rotation-invariant state.

The common stabilizer of the ordered source edge contains a fivefold rotation. It fixes H_e and cycles the other five H. It commutes with A and E_e and fixes e_u. Consequently all five competing scores are equal throughout this experiment. The replay verifies the signed chain action and the five-cycle exactly.

Let

\[
g_J(t)=s_{H_e}(e^{tL}e_u)-s_J(e^{tL}e_u),\qquad J\ne H_e.
\]

Each g_J begins at zero, with zero first derivative. Its exact second derivative gives

\[
\boxed{g_J(t)=\frac{\gamma^2}{10}t^2+O(t^4).}
\]

There is no term linear in gamma. In the half-second-derivative expression

\[
\tfrac12 g_J''(0)=(Le_u)^TQ(Le_u)+e_u^TQL^2e_u,
\]

the mixed A/E term cancels by B1 equivariance and symmetry of Q. At a vertex input only the a-channel can contribute to that mixed term; b and c do not enter. The pure E term is 1/10 for every competitor. The integer signed-action calculation supplies exact rational certificates for these statements. The leading coefficient is gamma^2/10 for either sign of the local change; replacing it by a change of the squared background edge coefficient would be incorrect.

Time parity improves the remainder. The degree grading J=diag((-1)^k I_Ck) anticommutes with L, commutes with Q, and fixes e_u. Hence g_J(t)=g_J(−t), and its odd derivatives at zero vanish. For ||L||≤M,

\[
|g_J^{(4)}(t)|\le16M^4,
\qquad
\boxed{g_J(t)\ge\frac{\gamma^2}{10}t^2-\frac23M^4t^4.}
\]

The derivative bound follows by four commutators with L and norm preservation. Taylor's theorem applies on the complete interval. This is a finite-time inequality, not a numerical extrapolation from a short trajectory.

## 4. A hard-gate witness with no background cancellation

Choose the declared unit coefficients a=b=c=1 and gamma=−1. The source closes the selected edge's two endpoint contacts while the remaining background runs. No cancellation of A is assumed.

The preceding exact spectral factors and a new exact algebraic Sturm check show ||A||<4. With ||E_e||=sqrt(2), ||L||<6 is a conservative bound. Therefore

\[
g_J(t)\ge\frac1{10}t^2-864t^4>0
\quad\text{for}\quad0<t<\frac1{\sqrt{8640}}.
\]

For all 0<t≤1/100, g_J(t)≥(17/1250)t^2. At tau=1/100 this yields Delta_*=17/12500000. All five competitors obey the same bound, establishing a unique winning H_e throughout that positive-time window. The value 1/100 is a supplied sufficient test duration in an uncalibrated model clock, not a derived universal time or coupling constant.

An actual duration in [99/10000,101/10000] also stays inside the proved positive window. The replay supplies the exact positive lower bound at the upper endpoint; the quartic lower bound is decreasing over this particular interval. A different timing interval must be checked against the same inequality.

The gate must not be interpreted as a new nilpotent boundary while retaining the old B2. Its modified contact map K1=B1(I−D_e) has

\[
\|K_1B_2\|_F^2=10,
\]

where D_e projects onto the selected edge. The response remains skew and norm-conserving, but the free Hodge factorization does not apply to its active interval. The selection proof uses the actual perturbed matrix and norm bounds, not that invalid extrapolation.

## 5. Persistence, uncertainty and an isolation benchmark

Restore the original A at the supplied time tau. Then every s_H and every gap is constant, because [A,Pi_H]=0. The selected diagnostic label persists in that ideal model even though the carrier amplitudes continue evolving. This is conservation of a global diagnostic after a supplied switch. It is not an acquired classical record, a bath-induced irreversible event, or an autonomous latch.

If ideal and actual final states are both unit norm and ||x_actual−x_ideal||≤delta, then

\[
|s_H(x_{\rm actual})-s_H(x_{\rm ideal})|\le2\delta,
\quad
g_J^{\rm actual}\ge\Delta_*-4\delta.
\]

Thus delta<Delta_*/4=17/50000000 suffices at the nominal endpoint. This small conservative margin must be used if the preference is to be operationally read. With initial error delta_in and uniform skew generator mismatch eta during a pulse of duration tau_actual, Duhamel gives delta≤delta_in+eta tau_actual. For duration uncertainty inside the certified interval, use that interval's minimum ideal gap and compare at the same actual duration. The timing allowance must not then be charged again as an independent state error.

After restoration, a residual contact error with norm at most eta_off changes a unit-state gap by at most 2 eta_off t. A positive actual margin Delta therefore remains positive for t<Delta/(2 eta_off), or indefinitely under the ideal zero-error free generator. This is a conditional retention bound, not evidence of perfect physical isolation.

A separate benchmark illustrates the stronger control assumption needed for an exact large gap. If the background is explicitly off/cancelled and only gamma E_e runs, an isolated three-coordinate exchange gives

\[
s_{H_e}(t)=\frac1{10}+\frac1{20}\sin^2(\sqrt2\gamma t),
\qquad s_J(t)=\frac1{10}\quad(J\ne H_e).
\]

It reaches gap 1/20 at pi/(2sqrt(2)|gamma|), with integrated source norm pi/2. The replay verifies its projection quadratic forms exactly. This benchmark does not justify treating the always-running background as absent; its cancellation and clock would be additional resources.

If the perturbed finite skew generator is left on forever, no strictly positive uniform gap from the initially tied state is established. In fact finite orthogonal evolution has approximate return times to its initial state, so an eventual positive lower gap valid for all later times is impossible under that closed constant-generator contract. Switching or an open/state-changing mechanism must be included for robust permanent preference. Approximate recurrence does not prohibit a useful finite selection window.

## 6. Two negative tests constrain the source

First, a face-only 2↔3 contact response cannot affect a vertex-only preparation. The subspace C0⊕im(B1^T) has dimension 120+119=239 and is invariant under the free generator. B2^T B1^T=0, and every such face-contact perturbation annihilates this subspace. Even time-dependent face masks therefore leave its trajectory and conserved fibration scores unchanged. Dense Fourier mixing of an operator does not imply that a given input reaches its active support.

Second, the full rotation-invariant real-amplitude subspace has degree dimensions (1,0,0,1). The new finite check constructs this fixed space using two left and two right binary-group generators. Its two vectors are the constant vertex mode and oriented fundamental three-cycle, both harmonic. The declared vertex-edge gates and row-weighted face-contact gates annihilate both. Thus this source cannot create a nonstationary preference from a fully rotation-invariant pure chain amplitude. The localized e_u input is a substantive preparation premise.

An isotropic ensemble with covariance I/2640 is also unchanged by any fixed orthogonal evolution. Its mean score remains Tr(Pi_H)/2640=1/10 for every H. Individual seeded histories and an ensemble-preferred direction must not be conflated.

## 7. A covariant, fully specified candidate source kernel

Here is a complete conditional source trial, distinct from a derivation of why UD realizes it:

1. Supply a vertex preparation e_u, the declared unit-weight carrier and a source-start tick.
2. Draw one of the twelve edges incident to u uniformly and independently of the carrier preparation.
3. Close its vertex contacts for tau=1/100, then restore them.
4. Return the incident-edge receipt and the mathematically implied H_e, along with the state, timing and uncertainty contract. A rejected random draw or failed preparation is an explicit NO_EVENT/failure outcome.

The vertex stabilizer acts transitively on those twelve incident edges. Under the declared restriction to exactly one such edge and rotational covariance, its distribution is forced to be uniform. The assumption that one edge must be chosen, its eligibility, the source-start tick and its gate duration are newly supplied premises. Symmetry alone does not imply that any trial occurs.

Two incident edges correspond to each H. Hence

\[
\Pr(H_e=H)=\frac2{12}=\frac16.
\]

The law is covariant and has no preferred ensemble axis. Each realized branch has a uniquely selected diagnostic fibration in the proved window. A right-family/chirality convention is retained from the preceding construction; including reflections requires treating the corresponding left family as well.

The carrier/source joint law during the ideal active interval is explicitly

\[
\mu_t=\frac1{12}\sum_{e\ni u}
\delta_e\otimes\delta_{\exp(t(A-E_e))e_u}.
\]

After switching, replace the branch state by exp((t−tau)A) exp(tau(A−E_e)) e_u. This is a classical distribution over the declared real amplitudes and source addresses, not a quantum encoding or a collapse postulate. Taking the mean generator is not the same as this mixture of branch evolutions. The mean edge response is symmetric under the source-vertex stabilizer and keeps the six scores tied for this initial state. It cannot be substituted for a realized seed when analyzing branch selection.

The source already carries the chosen edge information. A label R=H_e calculated from that receipt has entropy ln(6), while the edge receipt has entropy ln(12)=ln(6)+ln(2). This records or processes supplied branch information. It does not establish newly acquired information about an unknown carrier, nor replace the prior acquisition apparatus.

## 8. Source and renewal ledger

| Resource | Declared provision and remaining boundary |
| --- | --- |
| Carrier state | Localized vertex amplitude e_u; preparation and verification supplied |
| Source address | One of twelve incident edges; source vertex/configuration also retained |
| Randomness | Independent uniform twelve-way donor, or the finite-bit construction below |
| Gate contacts | Exactly the two vertex contacts of the selected edge; source deviation norm sqrt(2) in the unit convention |
| Duration | Nominal 1/100 model units; nominal integrated source norm sqrt(2)/100 |
| Restoration | Supplied timing and switch; residual-error allowance required for retention |
| Label storage | Six possible H labels need three fixed binary bits; source-edge receipt and failure metadata are additional |
| Acquisition | Source-address readout can predict the branch label; verifying the carrier score needs its own finite-error instrument |
| Renewal | Fresh independent random donor and, for repeated trials, a newly admitted localized carrier state or an explicit reset/transfer mechanism |
| Physical cost | No action scale, joule normalization, thermal donor production or physical area map is derived |

A uniform twelve-way donor is not an exact always-successful output of a fixed number b of fair independent bits: 12 does not divide 2^b. One explicit alternative reads four fresh bits, accepts labels 0 through 11, and retries on 12 through 15. Its unlimited expected bit use is 4/(3/4)=16/3. Capping it at r attempts uses at most 4r bits and has NO_EVENT probability 4^(-r). Conditional on success the twelve labels are exactly uniform. The geometric neighbor enumeration is a coding convention; the accepted distribution is covariant. Rejected bits, controller work, finite delay and source independence remain in the ledger.

The draw can be completed before the admitted source-start tick. If the tick precedes the draw, random-draw latency must be included in the trial's timing contract. No unbounded rejection process is silently placed inside the certified short contact window.

Changing the carrier to another shape or assuming a thermal bath does not eliminate these provisions. Neither norm conservation nor a source receipt supplies a cost-free reset. No physical promotion, entropy-area law or native event-source closure is inferred.

## 9. Disposition and next closure

DERIVED on the declared carrier: score-current identity; exact local tie-breaking coefficients; finite positive selection and timing windows; ideal and imperfect post-switch retention contracts; protected-input no-go tests; and the covariant edge-to-fibration pushforward under the proposed source kernel.

CANDIDATE: one eligible incident edge is gated at a supplied tick, with the stated localized preparation, donor and restoration rule. This is a concrete source model that can be reviewed and falsified within the finite theory. It is not a recovered native UD occurrence law.

OPEN: derive or recover what physical/constitutive readiness closes the chosen contact, how the start tick and restoration arise, how localized preparations and donor renewals are supplied, and which operational criterion makes this coherence score the relevant observable. The next native-source task is to connect that eligibility/closure law to typed burden, readiness or transport variables rather than assigning a gate by fiat.

This is a separate development package. The prior reduced-generator/spectral report is preserved and pinned to GitHub commit 2c4e4c89d25817cb0120916e28014c8b77a5527f (PR106), with its complete package hash. The current narrative manuscript is not revised here. The source register pins the current repository base, source hashes and verification scope. All analysis is constructor work, not independent review.

## Reproducibility

Run `python verify_local_source.py` with NumPy, SciPy and SymPy. It reads baseline/COMPLEX_AND_ACTION.json and baseline/EXACT_SPECTRA.json, reconstructs the signed chain actions and sparse matrices, derives exact rational score derivatives, checks the fivefold stabilizer and fixed spaces, certifies the free norm bound with exact Sturm signs, and writes LOCAL_SOURCE_CHECKS.json and LOCAL_SOURCE_DATA.json. The trajectory and switch-off propagation checks are labelled numerical corroboration. General commutator, Taylor, robustness, covariance and recurrence conclusions have written proofs above.

No imported partner or archived executable is run. Earlier full manuscript and apparatus replays are not all repeated. The supplied historical ledger and governance proposal remain historical sources with their original status. `Gap2_FINAL_Finite_Genesis.png` was unavailable and is excluded.
