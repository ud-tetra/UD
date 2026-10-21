# UD native crossing-to-receipt audit v0.1

2026-10-01, America/Chicago. Development lane. Constructor: Codex. Independent review: none. Physical promotion:0.

## Result

A declared queue and recording adapter can preserve resolved native crossing identities through simultaneous detections and publication delays. It retains one receipt per published crossing token, suppresses duplicate processing, and preserves the existing conditional causal-receipt equivalence for independent publications.

This is an exact conditional bridge, not an internally selected UD detector. The new assumptions are resolved-root access, a per-cell FIFO and nonwrapping ordinal, root-authorized readiness preparations, publication of pending tokens after their occurrence, and acknowledgment-based credit release.

Two limits are now explicit:

- Lossless capture of an independently continuing clock during arbitrarily long recording stalls requires unbounded pending identity storage, or a new admission/backreaction law.

- Under the earlier one-publication-per-fresh-crossing policy, a backlog can persist after a stall. Queuing alone does not restore immediate wave/event alignment.

This continues the [phase-aware gate-transition audit](https://chatgpt.com/space/page_5bff6953e73481919729f0a5e0ab8526). Its all-four-face gluing falsifier and earlier hash-locked releases remain unchanged.

## Source boundary

Current manuscript version9, SA-TIME-009, supplies a candidate publication contract: atomic acquisition of the complete observed edge support, grouped immutable bundles, nonwrapping edge versions, actor inference from distinct changed-edge signatures, durable recording before release, compatible receipt union and predecessor identities. Its source explicitly says those recording rules are not derived from the ledger's real support generator.

The existing readiness controller is assumed ready when publication is attempted. This audit adds a restricted root-to-readiness adapter; it does not derive four independent face preparations from one root.

The previous gate audit supplies a native cell port u_t=0 with g_t=(B3ᵀf)_t!=0. The recording audit takes exact resolved instances of that port as input. It does not turn a receipt into evidence that an authentic physical crossing occurred.

Retrieved manuscript windows3990–4089,4090–4259 and4255–4354 are retained as source snapshots. Their hashes identify the retrieved text, not the whole manuscript bytes.

## 1. Exact capture and duplicate suppression

The capture state retains a previous nonzero side, a zero latch, an expected post-root side and a local crossing ordinal.

For a transverse root u=0,g!=0:

- The incoming side must be opposite the sign of g.

- Accept one new ordinal and latch that root.

- Repeated observations of the same zero while latched add no ordinal.

- A nonzero sample on the sign(g) side rearms the detector.

An initial zero has no known preceding side and is initialization, not a counted event. A nontransverse zero remains OPEN. A sign reversal without a resolved zero, the wrong root direction, or a contradictory post-root side is rejected rather than silently repaired.

These are exact arming rules conditional on resolving every relevant root and obtaining an intervening nonzero side. They do not locate zeros from a numerical sample grid. Endpoint signs alone cannot certify crossing multiplicity without a timing/root-resolution contract.

Verification includes16 isolated coherent roots with repeated zero observations, and8 simultaneous root pairs from the previously verified glued pure mode. Reversing a cell orientation basis changes signs but preserves its root ordinals.

The two-cell shared-only graph still cannot infer which endpoint acted: their changed-edge supports coincide. Adding queues does not repair that observation failure. The full publication fixtures use a separate identifying five-cell star; they verify the adapter conditional on its input, not that those synthetic simultaneous star detections are a derived star eigenmode.

## 2. Three event stages and their balance

Use distinct quantities:

| Symbol | Meaning |
|---|---|
| D | Resolved crossings captured |
| Q | Captured tokens still awaiting publication |
| P | Successful cell publications |
| R_union | Distinct accepted publication receipts retained anywhere |
| U | Published bundles not yet durably recorded |

At every finite cut of the declared lossless adapter:

~~~text
D = P + Q
P = |R_union| + |U|
D = Q + |R_union| + |U|.
~~~

The first relation needs lossless capture/FIFO handling. The second inherits the existing durable-publication contract. A pending crossing is not already a published tick, and an unrecorded publication is not already retained observation.

Each queued token is addressed by cell and local ordinal. The outgoing bundle supplies the ordinal but no actor label. The detector infers the actor from the complete changed-edge support, then forms the crossing identity. FIFO checking prevents gaps in each actor's accepted ordinal sequence.

The root identity and edge/version publication identity are distinct. Their association is extra receipt content. Edge versions prove distinct protocol occurrences under the contract; they do not authenticate the originating waveform.

## 3. Candidate adapter and resource accounting

The concrete branch performs:

1. Capture a resolved crossing once and append its local ordinal.

2. When its cell has a pending head token, one available authorization credit and clear observed slots, perform the four ordinary readiness preparations as explicit zero-tick operations.

3. Publish one source cell-bit flip, reset readiness, pop exactly that head token, reserve one credit and install the complete immutable observed-support bundle.

4. Infer the actor and validate the complete active bundle and next expected root ordinal.

5. Durably retain its receipt before releasing the slots and reserved credit.

Each publication abstracts four preparation operations plus one source commit. Native waveform time is not identified with that operation count.

Available plus reserved credit stays one per cell. Duplicate acknowledgment returns no additional credit and contributes no new event. Credits are independent declared registers; they are not quantized amplitude support.

This is a separate acknowledgment-release proposal. SA-TIME-004 released a reserved credit at the negative crossing of a selected periodic port. The new law does not silently replace that branch. It also permits pending-token publication after occurrence, rather than inheriting the prior fresh-positive-only eligibility window.

The continuous native amplitudes receive no jump or backreaction in this adapter. This does not admit the previous per-commit Cayley amplitude lift. The binary publisher remains coupled to buffer occupancy and credit acknowledgment; it is not a proved passive measurement of independently evolving binary events.

## 4. Simultaneous roots, arbitration and causal equivalence

Detection of simultaneous cell roots appends distinct local tokens; it imposes no arbitrary global order. Publication requires all observed support slots or none. Conflicting actors serialize, while actors on disjoint supports may have outstanding bundles together.

On a five-cell star:
-120 serial actor orders for one simultaneous token per cell preserve all five occurrences.

- Those orders yield16 distinct causal receipt records, determined by which leaves publish before the center. Equality of root occurrence time does not select a unique publication history.

- The24 leaf-publication orders combined with24 acknowledgment orders give576 independent schedules. All preserve the same leaf receipts and the center's four-parent receipt.

This equivalence retains crossing associations, per-interface chains, causal receipts and counts. It does not retain every intermediate global binary snapshot or the full native-time ordering. Rescheduling publication after a trusted finite capture set is available does not establish equivalence of arbitrary complete wave/record histories.

Fair arbitration is needed for liveness. Disjoint updates commute under the declared per-cell resources and observed supports. Shared banks, additional hidden dependencies or richer observation invalidate that independence premise.

## 5. Retained observation can arrive out of order

A copied center receipt may arrive before its four leaf predecessors. The receiver must retain that receipt with unresolved references.

| Delivered records | Raw distinct count | Parent-closed count |
|---|---:|---:|
| Center alone |1|0|
| Center plus one leaf |2|1|
| Center plus two leaves |3|2|
| Center plus three leaves |4|3|
| Complete fork/join |5|5|

Compatible immutable set-union merge converges under duplicated/out-of-order delivery. Conflicting payloads claiming the same identity are rejected. Closing each replica before merging can lose information; raw receipts must remain available.

The global union is a mathematical verification view. It is not instantly available to every observer. These counts and DAG depth remain event summaries, not physical time.

## 6. Published bits need not track the instantaneous amplitude phase

Let the detector phase bit start from an explicit reference and toggle once per accepted root. The published bit toggles once per successfully published token. For each cell,

~~~text
detected_bit XOR published_bit = Q_cell mod2.
~~~

Thus even a correct delayed recorder can disagree with the current detector phase. Conversely, an even backlog makes the bits agree while multiple crossing identities are still pending. Equality of two bits is not proof of complete event history.

A scalar cell reference must be declared consistently with orientation changes. At a root the instantaneous amplitude sign is undefined; side-limit and initialization conventions remain part of the interface. Publication delay, retained-observer delay and wave phase cannot be identified without those conventions.

## 7. Capacity and catch-up limits

### Arbitrarily long stalls

Withhold recording of one published bundle on a repeatedly active cell. Its observed slots remain occupied, preventing later publication while native roots continue.

After N captured roots, at most one has published, so Q≥N−1. For any finite pending capacity K, choosing N>K+1 exceeds it. The replay checks capacities1–8; the balance argument proves the unbounded conditional claim.

An admitted loss counter would change the accounting to D=P+Q+L_drop. An admission selector would distinguish all detected roots from admitted roots. Backreaction could change the source flow itself. Each is a different law; none follows from versioned receipts.

### Fresh-crossing-only publication

Suppose one cell already owes m crossings, then each subsequent native opportunity adds one new crossing and permits at most one publication. After n such opportunities:

~~~text
D = D0+n,  P ≤ P0+n,  Q ≥ m.
~~~

The backlog cannot decrease under those conditions. The exact fixture retains an initial debt of5 across12 fresh opportunities. A burst, changed eligibility, slowed/stopped capture or native feedback changes the premise and requires admission.

The shared-service fixture similarly declares two arriving roots and at most one publication per service round, yielding Q≥n after n rounds. This is a protocol capacity example, not a universal physical throughput bound.

### Liveness versus bounded delay

For a finite admitted capture set, eventual acknowledgment and fair publication can drain all tokens. With continuing arrivals, starvation-free arbitration and eventual service can preserve each token's eventual fate while backlog grows. A rotating-occupancy star fixture gives every leaf repeated publication and acknowledgment while the center never regains all four free slots. Even strong fairness of enabled transitions does not guarantee recurrent eligibility. Liveness needs an arbitration law that eventually grants a pending head its complete support, rather than fairness only after it becomes enabled. No bounded waiting time or capacity follows.

## Source-selection status and next bounded target

The mathematical recording bridge is conditionally coherent. Its physical/source bottleneck is now capacity and event admission, rather than another bookkeeping protocol.

Next test: can a bounded UD resource state select which cell roots become events, or feed back on the native flow while preserving support/ownership and the claimed propagation sector?

Require a concrete balance distinguishing detected, admitted, published, retained and rejected crossings. Test whether its action follows from existing UD laws. If the native waveform continues independently, report delayed observational counts. If feedback is introduced, recheck the generator, sector closure, frequencies and locality. Do not select a lossless infinite queue merely because it avoids stalling.

## Verification and limits

The replay passes67324 exact assertion checks across120 serial schedules,576 independent publication/acknowledgment schedules, duplicated-root capture,24 parent-delivery orders, credit reuse, FIFO lag, causal closure and capacity fixtures. This is repeated verification of finitely many protocol fixtures, not67324 independent experiments.

The preserved previous release replays1765 gate-transition checks and the earlier146-check amplitude/readiness audit. Archive manifests and extracted replay outputs are verified.

- EXACT / DERIVED: balances, parity lag, duplicate/merge identities and stated capacity limits.

- EXACT CONDITIONAL: capture/FIFO/receipt correctness under resolved-root access and the declared reliable adapter.

- CANDIDATE: new capture state, queues, root-to-readiness authorization, credit release and arbitration.

- OPEN: root-resolver authenticity, finite capacity/admission, source-selected coupling and physical implementation.

- Physical promotion:0. No primitive action, coefficient, registry rung or prior claim bin is changed.

No adversarial authentication, crashes, numerical root detection, storage exhaustion recovery, actual network deployment or physical realization is claimed. Those omissions define the tested contract. Page text is read back; visual layout is unverified.
