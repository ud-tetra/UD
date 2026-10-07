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
