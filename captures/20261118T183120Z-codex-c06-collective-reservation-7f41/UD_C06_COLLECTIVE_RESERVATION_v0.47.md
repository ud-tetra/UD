# C06 collective reservation and typed veto finality v0.47

**EXACT / CONDITIONAL** for a shared reciprocal cut on one operation with a complete common pre-cut state and atomic consumption. **NO-GO** for an immediate sound decision from an asynchronous prefix that can still hide a relevant same-state veto. **CANDIDATE** for cell-level authority and abort-first precedence. **Physical Promotion = 0.**

## Source scope

C06 v0.46, “Exact exclusive-selection criterion” and “Typed veto and conservation,” resolves individual contact selection and reciprocal cutting. C06 v0.20, “Simultaneous receipts,” uses a shared atomic Ready guard for a batch of qualifying balance observations and leaves its native actuation open. C06 v0.21, “Shared actuation remains a transition law,” gives common tetrahedral support and admits both continuation and an atomic cut on the same incidence. Paper I v1.1.1 §§8.3–8.4 requires reciprocity and provides a legal distinct-face noncommutation witness as well as a conditional batch alternative. Native Gate Trigger and Recovery v0.1 §§2–2.1 and 6–7 defines the hard predicates for supplied histories and contexts. None of those source rules audited here grants the actuator here or establishes when its gate observations are final.

## Operation selection

Let a finite relabeling group act on prepared states, eligible contacts \(A(x)\), and operation instances. An operation instance identifies the cell, preparation epoch, actual donor/archive block, shared metric and operator with its adjoint, and directed first-root rule. Operator data are compared in a common frame. Equal matrix entries on different blocks or epochs still describe different operations.

Let \(\kappa\) be the equivariant contact-to-operation map and \(H=\operatorname{Stab}(x)\). A deterministic equivariant selector of one eligible operation exists on the orbit of \(x\) exactly when \(\kappa(A(x))\cap\operatorname{Fix}(H)\ne\varnothing\). Indeed, any chosen operation must be fixed under \(H\), and any such choice extends by transport \(q(gx)=gq(x)\), independently of the orbit representative. In particular, an equivariant singleton image is fixed even when every contact is moved by some symmetry. Thus four symmetric contacts can refer to one invariant cell operation whenever the target map is supplied. If the admissible targets instead form a pair interchanged by the stabilizer, there is still no exclusive equivariant cut. The v0.46 contact obstruction applies unchanged when a unique contact must own the cut.

## One reservation with a complete veto snapshot

Fix a nonempty, equivariantly prepared roster \(R_q\) for the operation \(q\). Roster membership remains fixed for that reservation, including after a predicate fails. At a common coherent pre-cut revision \(r\), receive both typed hard predicates from every roster contact. The complete failure set is
\[
V_r=\{(c,\mathrm{ClosureFail}):C_c(r)=0\}
\cup\{(c,\mathrm{IntegrityFail}):T_c(r)=0\}.
\]
A contact can contribute zero, one, or two causes. If all combinations are admissible, retaining the full set is equivalent to retaining each pair of Boolean outcomes. The product across the roster is sufficient for the single Boolean question \(V_r=\varnothing\). It cannot recover the failing contact or predicate. Recomputing the roster from passing gates would discard precisely the failing contacts. Reuse of a pass receipt from an earlier revision or from a separate operation invalidates a live decision.

The candidate uses one Ready token for \(q\). A complete revision must be live and final for the decision. Decision, identity amplitude reset, removal of both reciprocal coupling directions, and any terminal publication entitlement form one atomic transition. With this reservation, a complete revision with \(V_r\ne\varnothing\) commits Abort with all typed causes. If \(V_r=\varnothing\) and the first directed root is certified, it commits Held. A complete all-pass pre-root revision leaves the loader running. A missing, conflicting, or stale snapshot cannot authorize a terminal decision in this model. A repeated identical receipt can be deduplicated, and duplicate terminal requests cannot spend the same token twice. With abort-first precedence, a same-root veto gives Abort even when the available archive stock is full. These cases use the same state, root guard, and metrics on both sides of the transaction.

The rule commutes with relabeling because roster membership, all predicates and the root flag transport, failure collection commutes with relabeling, and the one reciprocal cut applies to the common operation. Terminal commits conservatively freeze the complete donor/archive stock by changing only the generator. The aligned first-lobe model starts with an empty archive and stock \(N>0\) in the donor. Its stocks at cut angle \(\theta\) are \(N\cos^2\theta\) and \(N\sin^2\theta\); at the first root the archive has \(N\), with the existing readout \(N/2\) under a Held receipt. A same-root Abort has the same amplitude state and a different authorization outcome. Strict temporal transversality is an assumption if the directed root test uses a nonzero time derivative; a finite phase arrival alone does not ensure it.

## Asynchronous finality obstruction

Assume immediate terminal choice at the first root, same-root veto priority, and visibility permitting a relevant observation to arrive after the decision. Construct two traces with the same observed prefix at the decision, one with all root predicates passing and one with a root-time failure hidden by delayed publication. Liveness requires Held in the former. Soundness forbids Held in the latter. Any deterministic rule of the common prefix has one output and cannot satisfy both. The same holds for a rule claiming certainty with randomness. A revision label alone cannot guarantee finality. A coherent, complete and immutable pre-cut state can resolve the ambiguity if it is available at the decision. Otherwise staying at the guarded boundary preserves the amplitudes but may stall. Incidence, an aggregate ready bit, and later receipt union supply no proof of same-state finality or its availability.

## Intake amendments

- The signed vertex potential \((1,1,-1,-1)\) alone has stabilizer \(S_2\times S_2\), order four, with two face orbits. Additional preparation data can reduce this group. The sign-quotiented ray instead admits an order-eight stabilizer, transitive on faces. The no-fixed-face example needs only \((01)(23)\) in the full preparation stabilizer.
- The v0.46 edge-mask replay has four feasible classes, including three unique, and seven obstructed classes. Those controls do not imply a universal obstruction.
- Strict uniform lease coverage requires a common finite \(L\) with \(\theta_x(L)>\pi/2\) on every admitted trace. A rate floor \(g_{\min}>0\) suffices if \(L>\pi/(2g_{\min})\). At equality a tie is possible and requires an admitted priority rule. Lack of a positive pointwise rate floor alone is insufficient to prove lack of a uniform lease.
- Transport integrity uses the relevant source-specific domain, overlap and reverse-map conditions. Gram defect is a scoped signature where the declared test reduces to it. Receipt typing therefore uses IntegrityFail.
- The reciprocal cut is structural. At the ideal root with donor zero, a forward-only surviving channel happens to leave the aligned state stationary. A surviving reverse coupling can regenerate the donor at once, and the forward-only remainder can change other cut states.

## Replay and next discriminant

The adjacent standard-library replay checks frozen rosters, typed vetoes, relabeling, live revisions, duplicate and mismatched requests, and exact stock controls. The replay is finite evidence for the declared model. Native grant, predicate histories, access to a complete root snapshot, and the priority of a simultaneous veto remain open. The discriminant is whether an admitted same-state source can prove root snapshot finality and give the one reciprocal cut authority without waiting for downstream publication.
