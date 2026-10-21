# UD finite admission and wave-feedback discriminator v0.1

2026-10-02, America/Chicago. Development lane. Constructor: Codex. Independent review: none. Physical promotion:0.

## Result

Finite event slots can enforce a bounded admission rule while leaving native amplitudes unchanged, but rejected crossings must remain explicit in the event balance. Such admission no longer preserves every native sign flip as a published event.

Global scalar pausing preserves the original wave orbit under a changed phase clock. Local whole-cell pausing preserves norm and the closed face–cell sector, but changes the generator. An exact example shows that a paused zero arrival can resume toward the original sign, so it is not necessarily a completed sign crossing.

The newer finite-stock observer does not supply the missing local event rule: two valid preparations have identical complete whole-path stock histories but different local crossing counts.

This continues the [crossing-to-receipt audit](https://chatgpt.com/space/page_1d61c0bcba848191ae09ff45b49f3aec). No earlier release, primitive action, coefficient or registry claim is changed.

## Sources inspected

1. The preserved crossing-to-receipt release: resolved-root capture and queued publication are explicitly candidate assumptions. The slot/count limit is independent of how the native port is resolved.

2. UD_FINITE_STOCK_OBSERVER_CONTRACT_v0.1_RELEASE, materialized current version0: exact known-frequency reconstruction of whole-path mean core stock, modal-sign nonidentifiability, precision and fixed-horizon conditioning limits. Its note explicitly adopts no physical acquisition protocol or new source law.

3. The retrieved UD_BIDIRECTIONAL_SUPPORT_BURDEN_CURRENT_RUNTIME_RESULT_v0.1 report, dated2026-09-18: its inspected runtime has support flow c'=A_K c and a separate burden lane, with the specified reciprocal vertical cross operator absent. It calls normalization unidentified, not zero, and does not establish a physical zero coupling.

The runtime report's finding has that archived scope. It does not exclude later candidate addenda or all conceivable UD feedback. Neither it nor the inspected October2 observer contract supplies the finite root-admission or pause law tested here.

Archive identities, versions and byte fingerprints are retained in SOURCE_INDEX.json. Original files are not replaced.

## 1. Finite event-slot admission

Let K be a declared positive integer number of active event slots for one cell, counting both queued tokens and published-but-unrecorded bundles. K is a resource premise, not derived from tetrahedral geometry or real support.

Use:

- D: detected native roots.

- A: admitted roots.

- J: rejected roots.

- Q: admitted queued tokens.

- U: published but unrecorded tokens.

- R: durably retained distinct events.

- P: publications, including U.

Candidate rule: detect every resolved root; admit it only if Q+U<K. Otherwise increment J. Publication moves one token Q→U. Retention moves U→R and frees one slot.

Exact balances:

~~~text
D = A + J
A = Q + U + R
P = U + R
D = J + Q + U + R
0 <= Q+U <= K.
~~~

No amplitude backreaction is introduced. The waveform can continue while events are rejected. A bounded slot store is not a bounded lifetime history: exact counters, nonreused identities and permanently retained receipts still require growing representation.

### Identity repair

Admission creates gaps in native root ordinals. For K=1, admitting root1, rejecting root2 while its slot is occupied, then admitting root3 gives:

| Native root identity | Admitted occurrence identity |
|---|---|
|1|1|
|3|2|

The earlier validator requiring consecutive native ordinals cannot be imported unchanged. A correct receipt distinguishes native root identity, contiguous admission/publication sequence and explicit rejection accounting.

For phase bits initialized from the same reference:

~~~text
detected_bit XOR published_bit = (J+Q) mod2.
detected_bit XOR retained_bit  = (J+Q+U) mod2.
~~~

A rejected crossing can therefore change the wave phase without a publication. Even parity agreement does not certify a complete history.

The replay exhausts729 five-operation traces over detect/publish/retain and capacities1,2,3. It checks balances, occupancy, admission continuity and parity.

## 2. Full stock reconstruction does not recover local crossings

For the coherent two-tetrahedron path,

~~~text
G = [[4,-1],[-1,4]]
v3 = (1,1)/sqrt2,   eigenvalue3
v5 = (1,-1)/sqrt2,  eigenvalue5.
~~~

Choose zero initial modal slopes and the two preparations

~~~text
t_plus(0)  = 2v3 + v5
t_minus(0) = 2v3 - v5.
~~~

They share the same entire mean core-stock trajectory:

~~~text
rho(zeta) = [4 cos²(sqrt3 zeta) + cos²(sqrt5 zeta)]/2.
~~~

But cell1 has

~~~text
u_plus  = [2 cos(sqrt3 zeta) + cos(sqrt5 zeta)]/sqrt2
u_minus = [2 cos(sqrt3 zeta) - cos(sqrt5 zeta)]/sqrt2.
~~~

Set T=pi/(2sqrt3). Since1<sqrt(5/3)<2, sqrt5 T lies strictly between pi/2 and pi.

The plus coordinate starts positive, ends negative and is strictly decreasing on(0,T]: both sine terms in its derivative are positive. It has exactly one transverse root in that window.

The minus coordinate stays positive. Before pi/(2sqrt5), cos(sqrt3 zeta)>=cos(sqrt5 zeta)>0. Afterwards the second cosine is nonpositive and the first remains nonnegative; the endpoint is strictly positive. It has no root on[0,T].

Thus a complete noiseless stock record leaves local crossing counts1 versus0 unresolved. Finite samples cannot repair information absent even from the whole output trajectory.

This is a specific scalar-observer obstruction. It does not exclude signed cell ports, additional cross-mode observations or another declared observer. The source sampling theorem remains valid for its whole-stock target.

## 3. Global pause: original orbit, new control law

A scalar feedback proposal has

~~~text
dc/dtau = gamma(tau) A c,   gamma in{0,1}
theta(tau) = integral gamma(s) ds
c(tau) = exp(theta(tau) A)c(0).
~~~

Norm and the native invariant subspaces are preserved. The source follows the same orbit as a function of theta. But gamma, the resource-to-pause mapping, and the relationship between execution parameter tau and native phase theta are new content.

A pause creates a zero plateau if triggered at a cell root. The original transverse-crossing detector cannot simply treat that plateau as another transverse root in tau. First arrival, deferred crossing completion and resumed side must be distinguished.

A shared gate depending on all occupied event slots also adds global control. This is not a derived local interaction or physical clock law.

## 4. Local whole-cell pause: conservation without orbit equivalence

For the face–cell sector, put a diagonal cell gate Lambda into both adjoint blocks:

~~~text
A_Lambda = [[0,-B3 Lambda],[Lambda B3^T,0]].
~~~

It remains skew. Also B2 B3 Lambda=0, so the closed face–cell sector is preserved. This differs from arbitrary face masking, which need not preserve that closure.

Nevertheless, on the two-cell path the original top generator has rank4 and frequencies sqrt3,sqrt5. With Lambda=diag(0,1), its rank is2 and the active neighbor pair has frequency2. The original dispersion/clock identities cannot be asserted unchanged.

### Exact pause-at-zero falsifier

Write b0,b1 for the coherent boundary columns, so b0^T b1=-1 and ||b1||²=4. At a root take

~~~text
u0=0, u1=0, f=-b1
g0=b0^T f=+1.
~~~

This root can be approached from u0<0 under the original generator. Pause cell0 while letting cell1 evolve. Its neighbor half-return at active duration pi/2 sends f=-b1 to f=+b1, with u1 back at zero. Norm and closure are preserved, and u0 remains zero throughout the pause.

Now g0=-1. Reopening cell0 sends it back into u0<0, the same sign from which it arrived. The complete hybrid trajectory touches a zero plateau and returns; it does not complete the sign flip promised by the original transverse-root interpretation.

Recording an event on first arrival is possible as a separately declared event convention. It cannot simultaneously be claimed to count completed native sign crossings without another guard.

## 5. Branch comparison

| Proposal | Bounded active slots | Original wave orbit | Main obligation |
|---|---|---|---|
| Admit/reject without feedback |Yes|Unchanged|Keep rejected roots and revised identities |
| Lossless independent clock during arbitrary stalls |No uniform finite bound|Unchanged|Growing storage or bounded-service premise |
| Global scalar pause |Possible conditionally|Same orbit under theta|Global control and plateau semantics |
| Local whole-cell pause |Possible conditionally|Generally changed|Recheck modes and crossing completion |

No row is selected by the inspected sources. Conservation alone cannot choose one.

## Next bounded target

The useful discriminator is now a source-mechanism question: can a declared UD capacity state select admission or a feedback transition without fitting a new coefficient?

Require a typed capacity variable and a law explaining its coupling to the chain. If admission rejects roots, preserve the detected/admitted/rejected balance. If a local pause is chosen, the event token should remain provisional until crossing completion is established, or be explicitly renamed a zero-arrival event. Recheck the cubic/BCC propagation spectrum under the admitted coupling.

Avoid deriving a finite capacity from a real stock value without a quantization or ownership law. The newer sampling contract supplies an observer precision budget, not event slots or resource renewal.

## Verification and standing

3673 exact constructor assertions pass, including729 admission traces, rational boundary/Gram identities, all four binary whole-cell masks and the neighbor half-return certificate. The stock crossing count is proved by analytic inequalities, not a root grid.

The recovered prior crossing release and the finite-stock observer are retained and replayed in the package. Replay is mathematical/software evidence, not measurement or independent review.

Internal results are EXACT for the declared carriers; admission/feedback rules are CANDIDATE and their consequences EXACT CONDITIONAL. External correspondence is OPEN. Physical promotion remains0. Rejected interpretations are retained with failure, mitigation and replay conditions. Page content is verified by readback; visual layout is unverified.
