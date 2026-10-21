2026-10-02, America/Chicago. Development lane. Constructor: Codex. Independent review: none. Physical promotion: 0.

The candidate crossing guard now separates a zero arrival from a completed change of sign. It cancels the exact local-pause counterexample from the preceding audit. But coupling this guard to a full-capacity pause can deadlock: a cell held at zero cannot complete the crossing needed to release its provisional event slot.

This audit concerns the event interface for UD propagation. It does not establish that UD selects a cube, BCC geometry, a physical clock, or a finite capacity. Earlier releases remain unchanged.

## Sources and scope

The preserved [finite admission audit](https://chatgpt.com/space/page_af2900aa0fb88191bde7d32bf236244b) supplies the coherent two-cell carrier, its local-pause counterexample, and the distinction between capacity and whole-stock observation. Its complete release is included as a source snapshot.

The additionally inspected SOURCE_ADDENDUM_EVENT_S5_NEUTRAL_NATURAL_COTANGENT_LIFT_v0.1_AUDIT, dated September 18, is explicitly a candidate with partial source admission. Under its natural cotangent-lift premise, the Hamiltonian has scalar kinetic and potential terms and a periodic event phase. Sections 8–11 leave the kinetic coefficient, the potential identification, the absence of gyroscopic terms, and identification with the Hodge complex structure open.

That conditional oscillator does not supply an integer event-slot capacity, a cell-root acquisition rule, a support-to-event coupling, or a slot-release transition. A retained real oscillator state is not itself a finite set of durable event records. Its scalar coefficients are not imported as tunable capacity parameters here. This finding is limited to the inspected addendum; it is not a claim that every later UD proposal lacks feedback.

## Candidate completion guard

Assume a continuous cell coordinate with an initialized nonzero sign reference and a fully resolved zero segment: no hidden departures and returns are allowed between the witnesses. The candidate protocol is:

1. On the first zero arrival, reserve one provisional slot and retain the incoming sign and arrival identity.

2. While the coordinate remains zero, keep the token provisional. Duplicate zero observations create no new identity.

3. On departure to the opposite side, convert the provisional token into one committed completion.

4. On departure to the incoming side, cancel the provisional token and release its slot.

5. Publish and retain only committed completions. A later arrival receives a new arrival identity.

This counts resolved sign changes across zero segments, including a plateau followed by an opposite-side departure. Such a hybrid completion need not be transverse in the execution parameter, and its time is not automatically the native transverse-root time. Tangencies that return to the incoming side do not commit. Initialization exactly at zero remains outside the contract.

The software guard receives resolved segment observations; it does not implement a physical or numerical detector. A direct nonzero sign reversal without a resolved zero is marked unresolved and does not fabricate a trusted completion count. Even with matching endpoint signs, hidden trajectories can contain two or more crossings. Opposite endpoint signs establish odd crossing parity for a continuous path, not a unique crossing identity.

Simultaneously reversing the coordinate orientation and its incoming reference leaves arrival, completion, cancellation and publication counts unchanged. An untransformed external sign reference would not have that property.

## Exact local pause discrimination

For the coherent two-cell carrier, let the boundary columns be b0 and b1, with Gram matrix:

```text
B3^T B3 = [[4,-1],[-1,4]].
```

At the zero arrival take u0=u1=0 and f=-b1. The nominal cell0 slope is b0^T f=+1, so its immediate incoming side under the native generator is negative. Pause cell0 and let cell1 evolve for its half-return of duration pi/2. Then f becomes +b1, both cell coordinates remain zero at that endpoint, and the resumed cell0 slope is -1. The face norm squared remains 4.

Cell0 therefore departs into the same negative side. The guard produces one arrival, one cancellation and zero committed crossings. The previous arrival-only convention would have recorded an event that does not describe a completed sign change.

This is an exact conditional trajectory on a declared hybrid generator. It does not show that native unpaused propagation has a false transverse root.

## Capacity balances and identities

Let Z count detected zero arrivals, C committed completions, X cancelled admitted returns, J rejected arrivals and P currently provisional tokens. Let Q be committed queued events, U published unretained events and R retained events. For declared positive integer capacity K:

```text
Z = C + X + J + P
C = Q + U + R
P + Q + U <= K.
```

Rejection is applied at arrival when no slot is available. J is a count of rejected arrivals, not necessarily rejected completed crossings: a rejected arrival can later return to its incoming side. The guard would need further typed accounting to classify rejected completions. Cancellation and rejection create gaps in arrival identities. Committed sequence identities remain separate; arrival2 can become completion1.

Conversion P→Q preserves occupancy. Cancellation reduces occupancy by one. Publication Q→U preserves occupancy; durable retention U→R releases one active slot. Counters and retained lifetime history still grow. Finite active capacity is not finite exact lifetime storage.

## Conditional deadlock

Consider the candidate feedback policy that pauses source advance whenever occupancy reaches K, while allowing publication only after crossing completion and capacity release only after durable retention. Take K=1, no older queued or published event, and a newly reserved token at zero:

| Required transition | Blocking condition |
|---|---|
| Depart zero and complete | Full occupancy pauses the source |
| Publish completion | Token is still provisional |
| Retain publication and release | Nothing has been published |

The state has P=1, Q=U=0. All three progress transitions are disabled. Duplicate zero observations cannot repair it. The exhaustive guard replay includes this state and an exact fixed-point replay of 100 further service cycles.

This proves deadlock for the stated policy and state. It does not prove that every finite capacity design deadlocks. An independently releasable older event, cancellation, timeout or external intervention changes the premises. Fair scheduling of enabled transitions cannot help when no relevant transition is enabled.

## Candidate escape and its limits

A concrete escape is to reserve the provisional slot before pausing and exempt that cell from the capacity pause until its zero segment resolves. Commitment uses the already reserved slot and does not require an additional one. In the single-cell fixture, departure, publication and retention then complete at capacity1.

The exemption is a new feedback rule, not a law derived from the inspected sources. It does not prove finite-time departure for a generally coupled cell: a plateau can persist, the resume direction can change, and other cells can still face starvation. A global phase advance can preserve the native orbit, but may bring additional cells to roots requiring their own reservations. Separately acknowledging provisional arrivals could also release capacity, but the retained object would need an explicit provisional status and later completion or cancellation record.

## Verification and interpretation

The standard-library replay checks every cut of 8748 sign traces, their 8748 orientation reversals, and 12500 sign/publication/retention schedules. It also checks the coherent Gram reflection certificate, plateau deduplication, cancellation and rearming, missed-root classification, same-endpoint ambiguity, and the deadlock and escape fixtures. 193859 exact assertions pass; their totals and fixtures are recorded in the results file.

These are constructor tests of the declared interface and rational certificate, not independent review, physical acquisition, or empirical validation. The initial signs, resolved segments and integer capacities are premises. No coefficient is fitted and no physical promotion is made.

The geometry question now requires two separate admissions: a source-selected chain or lattice and a source-selected event coupling. A norm-preserving propagation carrier or event oscillator alone does not choose either. Testing cubic or BCC modes under an unspecified capacity law would conflate those steps.

The next bounded target is to inspect the current development gap inventory for an admitted capacity variable and an explicit reciprocal coupling. If one exists, test whether it guarantees zero departure and whether its coupled propagation retains the proposed cubic spectrum. If it does not, keep the completion exemption as a candidate and retain the deadlock as a falsifier of the full-slot pause policy.

Page text is checked by readback. Visual layout is unverified.
