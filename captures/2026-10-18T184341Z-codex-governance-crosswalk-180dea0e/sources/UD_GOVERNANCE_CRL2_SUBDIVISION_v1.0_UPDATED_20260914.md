# Governance Amendment — CRL-2 Subdivision and Anti-Erosion Rules

**Status:** governance proposal. Amends the confidence-rating ladder and the
promotion/demotion procedure. **Physical promotion: 0.**

Derived from a measured error distribution over this development session:
zero errors in the exact-substrate layer, seven in the bridge layer, four
material — every material error found only on adversarial review, never during
construction. The amendment concentrates protection where the errors are.

---

## 1. CRL-2 subdivision

The current CRL-2 ("operational / measurement-facing") spans everything from a
written proposal to a replicated result. That range is too wide for one label.
Replace with:

```
CRL-2a  PROPOSED       bridge construction written down; author-checked only
CRL-2b  PRE-REGISTERED frozen before data AND passed >=1 adversarial review
                       by a party who did not construct it
CRL-2c  EXECUTED       survived one blinded run against its frozen rule
CRL-2d  REPLICATED     survived >=1 independent replication
```

**Eligibility gates:**
- 2a → 2b requires a *non-constructor* adversarial review on record.
- Only 2d is eligible for CRL-3 (physical-identification) consideration.
- No claim skips a rung.

**Current status of this session's output:** the pre-registration packet is
**CRL-2a**. It has been adversarially reviewed only by its own author (two
passes), which this session demonstrates is insufficient — two material and
four minor errors survived construction and were caught only on hostile
re-read. It is **not** CRL-2b until a non-constructor reviews it.

---

## 2. Anti-erosion rule (support depth)

Define, for any claim X:

```
depth(X) = 0                              if X is exact-substrate or empirical
depth(X) = 1 + max over dependencies D of depth(D)   otherwise
```

**Rule E1 — status is capped by depth.**
A claim cited only by other conditional claims gets *deeper*, never firmer.
Citation is not evidence. Status improves only by re-derivation against a
lower-depth anchor, never by accumulating dependents.

**Rule E2 — dependency expiry.**
If X depends on assumption A and A is revised or demoted, X auto-demotes to
"pending re-derivation" with no ruling required. Append-only.

**Rationale.** This is the specific mechanism that prevents the failure seen in
the abandoned exploratory thread, where a "structural choice" became
"canonicalized" across a chain in which no single step was individually wrong.
Each step raised apparent firmness by citation. E1 makes that impossible; E2
makes revision propagate.

---

## 3. Asymmetric promotion / demotion

```
PROMOTION (any rung):  requires non-constructor adversarial review,
                       then custodian ruling. Slow by design.
DEMOTION on falsify:   automatic, immediate, no ruling. Append-only.
```

The custodian is removed from the demotion path entirely. This is what makes a
faster promotion path safe to offer: safety never waits on custodian
availability.

---

## 4. Development lane vs registry lane

Separate *may not claim* from *may not work on*.

```
REGISTRY LANE   entries carrying a CRL status. Frozen frontiers apply.
DEVELOPMENT LANE analysis reaching no registry conclusion. Requires only
                 a label: "development — no registry entry." Frozen
                 frontiers do NOT apply.
```

Analysis that promotes nothing (e.g. showing a frozen family fails to
discriminate) belongs in the development lane and does not require frontier
re-entry. Promotion from development to registry requires the §3 procedure.

---

## 5. Retractions and provenance as first-class objects

**Retraction registry.** Every correction is a registry object with the same
standing as a claim: what was wrong, what replaced it, found-by (construction /
self-review / external). The session-level retraction ratio is published as a
diagnostic. A framework with zero recorded retractions after substantial
development is unaudited, not clean.

**Provenance field** on every claim: origin, constructor, reviewer(s),
dependency list, lane. This is the field that catches contamination — content
entering the lineage from outside the substrate — at entry rather than
downstream.

---

## 6. The limit this does not fix

Governance catches *category* errors: claiming CRL-2c when you hold CRL-2a.
It does **not** catch a wrong rule inside a correctly-labeled CRL-2a document.
This session is the evidence: every material error was correctly *inside* a
"proposed" document and still wrong. Only non-constructor adversarial review
catches that class.

Therefore the binding recommendation is procedural, not structural:
**no bridge claim advances past CRL-2a without review by someone who did not
build it.** Everything above raises the floor. It does not substitute for that
review.

**Physical promotion remains 0.**

---

## 7. 2026-09-14 topology/source governance extension

**Status:** active governance amendment.  
**Physical promotion remains 0.**

This section governs the current \(C_4/C_5\), Pachner, open-source,
archive/dissolution, and topology-scheduler branch.

### 7.1 Typed carrier identity is mandatory

Equal matrices, vectors, dimensions, or numerical values do **not** identify
objects with different carrier types or provenance.

The following are permanently distinct unless an explicit typed intertwiner is
proved:

```
C4_cell   admitted boundary-complete 4-simplex carrier used in active homology
C4_evt    transient five-seat Pachner event-mediator carrier
C5_ctx    higher context/source carrier feeding C4_evt
```

Required fields:

```
carrier_type
domain
codomain
admission_condition
source_provenance
dependency_ids
internal_claim_bin
correspondence_status
physical_promotion
```

**Rule T1 — no numerical aliasing.**
Identical local incidence columns do not permit carrier identification.

**Rule T2 — homology firewall.**
Only admitted topological cell carriers enter active simplicial homology.

**Rule T3 — source firewall.**
Open sources are carrier-typed and are not interchangeable.

### 7.2 Exact-launch / no-tolerance rule

**Rule L1.**
Numerical closeness to a launch amplitude, phase, score, or endpoint is not a
theory tolerance and may not authorize topology commit.

**Rule L2.**
Numerical root finding may locate a candidate event, but registry execution
requires either an exact analytic identity or a certified root proof of the
full frozen launch predicate.

**Rule L3.**
No post-exposure epsilon may convert `HOLD` into `PASS`.

### 7.3 Scalar-source nonidentifiability and vector-source provenance

**Rule S1.**
A scalar support source, source power, total budget, or norm cannot substitute
for a signed address-resolved source vector.

Minimum predictive source packet:

```
(source_vector,
 address_basis,
 orientation,
 provenance,
 validity_interval,
 support_power_receipt)
```

**Rule S2.**
If local source derives from a larger closed carrier, preserve both the local
receipt and global exchange parent.

**Rule S3.**
Residual extraction is not a constitutive derivation.

### 7.4 Causal batch custody and no-double-spend

**Rule C1.**
Every topology batch uses one frozen pre-batch state.

**Rule C2.**
Credits produced by a batch enter only the next frozen scheduler snapshot.

**Rule C3.**
Signed address amplitude, not pooled \(q^2\), is the routing object.

**Rule C4.**
Concurrent packets require an exact commuting/reducing-block receipt;
otherwise serialize by independently frozen precedence or HOLD.

### 7.5 Symmetry and precedence

**Rule Y1.**
Exact candidate-exchange symmetry preserving the full pre-event state and law
forces HOLD; deterministic covariant selection is forbidden.

**Rule Y2.**
A strict unique first-hit time of the complete frozen launch predicate is a
lawful parameter-free precedence receipt.

**Rule Y3.**
Address order, array order, lexical order, random numerical noise, and
post-exposure convenience are invalid precedence sources.

### 7.6 CRL firewall for internal topology mathematics

Exact combinatorics, homology, incidence identities, internal Hodge dynamics,
source-interface theorems, and synthetic simulations do not become CRL-2 merely
because they are exact or executed computationally.

```
CRL-1 / INTERNAL
    exact or derived substrate/internal mathematics, algorithms, simulations,
    governance receipts, and source-interface theorems with no frozen
    measurement-facing identification.

CRL-2a..2d
    operational / measurement-facing bridge objects under §1.
```

**Rule R1.**
Internal computational execution is not CRL-2c execution.

**Rule R2.**
A source-addendum may be exact conditional mathematics while remaining below
CRL-2.

**Rule R3.**
Only claims with an explicit frozen external/measurement mapping enter CRL-2.

### 7.7 Correspondence tuple remains mandatory

Every external-facing topology statement carries:

```
(internal_claim_bin, correspondence_status, physical_promotion)
```

Allowed tags remain:

```
FORMAL_CORRESPONDENCE
OPERATIONAL_CORRESPONDENCE
OBSERVABLE_SIGNATURE_CANDIDATE
QUANTITATIVE_CORRESPONDENCE_TEST
EXPERIMENTALLY_REALIZED_ANALOGUE
```

Correspondence never implies physical identity, causation, derivation, or
promotion.

### 7.8 AUTO_LOCK / AUTO_FREEZE interaction

AUTO_LOCK only after carrier type, assumptions, and dependencies are explicit.

AUTO_FREEZE immediately on:

- unproved carrier crossing;
- post-hoc numerical tolerance;
- scalar-to-vector source substitution;
- same-batch credit double-spend;
- unreceipted symmetry breaking;
- internal-to-CRL-2 category promotion without bridge/review gates.

Repairs remain append-only and versioned.

### 7.9 Current topology branch ruling

The following are internal registry objects, not CRL-2 evidence:

- \(C_4^{cell}\) mathematics;
- \(C_4^{evt}\) Pachner/event mathematics;
- \(C_5^{ctx}\) source-extension mathematics;
- exact topology schedulers/selectors;
- synthetic/geometric Pachner simulations;
- archive/dissolution history theorems.

Any later measurement-facing use enters CRL-2a independently.

**Physical promotion remains 0.**

