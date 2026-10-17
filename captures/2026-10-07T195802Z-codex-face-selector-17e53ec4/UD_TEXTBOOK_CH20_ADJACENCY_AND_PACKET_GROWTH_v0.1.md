# Chapter 20 — Adjacency and Packet Growth

**Introduction to Unified Dynamics**  
**Part VII — Recursive Geometry Without Assuming Spacetime**  
**Status:** `MANUSCRIPT_READY_DRAFT`  
**Claim class:** `PEDAGOGICAL SYNTHESIS OF CURRENT UD CLUSTER-ADJACENCY BRIDGE`  
**Physical promotion:** `0`

---

## Learning Objectives

By the end of this chapter, you should be able to:

1. explain why recursive packet growth requires an adjacency selector rather than unrestricted copying;
2. distinguish the current default face-sharing selector \(G_{1,\rm default}=4\) from the dense alternate \(G_{1,\rm dense}=12\);
3. derive \(N_{2,\rm default}=768\) and \(N_{2,\rm dense}=2304\);
4. explain why the two branches have different governance status;
5. distinguish cluster capacity from physical lattice structure;
6. explain why face sharing is naturally compatible with tetrahedral closure bookkeeping;
7. explain why vertex sharing is denser but requires more global consistency machinery;
8. use clock arithmetic on the growth counts;
9. understand why the current branch ladder is structural rather than a universal recursion law;
10. identify the missing theorem needed for unrestricted multi-level packet growth.

---

# 20.1 Why Growth Needs a Rule

A single closed packet does not yet define a recursive universe. To grow a packet complex, the theory must specify which neighboring packets are allowed to attach, and by what relation.

If every imaginable attachment were permitted, the recursion would contain no selective structure. UD therefore introduces an **adjacency selector** downstream of local packet closure and upstream of any continuum or geometry claim.

# 20.2 The Current Starting Count

The first symmetry-resolved packet exposure count is

\[
\boxed{N_1=192.}
\]

A one-step cluster growth law has the structural form

\[
\boxed{N_2=G_1N_1,}
\]

where \(G_1\) is the admissible adjacency multiplicity for the selected branch.

# 20.3 Default Face-Sharing Branch

The current default selector is

\[
\boxed{G_{1,\rm default}=4.}
\]

Its intended structural role is face-sharing packet growth. A tetrahedron has four triangular faces, so face-sharing supplies a natural four-slot local adjacency count with comparatively little extra structure.

The resulting second-level count is

\[
\boxed{N_{2,\rm default}=4\cdot192=768.}
\]

Current governance classifies this as a **computed bridge / default native selector with tested-scope guard**. It is stronger than an unexplained guess and weaker than a universal recursion theorem.

# 20.4 Dense Vertex-Sharing Alternate

A denser admissible branch retains

\[
\boxed{G_{1,\rm dense}=12.}
\]

The corresponding count is

\[
\boxed{N_{2,\rm dense}=12\cdot192=2304.}
\]

This branch is an admissible high-density alternate, not the current default, because it requires additional global consistency machinery.

Thus \(4\) and \(12\) are not competing estimates of one quantity. They are different recursive adjacency branches.

# 20.5 Clock Arithmetic of the Growth Counts

Default branch:

\[
768=4\cdot192+0,
\qquad
\boxed{768\equiv0\pmod{192}}.
\]

On a 192-clock, 768 completes four exact cycles.

Dense branch:

\[
2304=12\cdot192+0,
\qquad
\boxed{2304\equiv0\pmod{192}}.
\]

On a 192-clock, 2304 completes twelve exact cycles.

Also,

\[
2304=3\cdot768+0,
\qquad
\boxed{2304\equiv0\pmod{768}}.
\]

These are exact capacity relations, not temporal statements.

# 20.6 Face Sharing Preserves a Natural Interface

Two tetrahedra that share one face share a complete 2-simplex. That interface already exists in the chain grammar as a \(C_2\) state.

Chapter 10 showed that a shared face is one support reservoir with cell-face currents into its neighboring cells. Thus face-sharing growth fits the current packet language naturally:

\[
\boxed{\text{cell}\leftrightarrow\text{shared face}\leftrightarrow\text{cell}.}
\]

This does not prove that every physical neighbor must be face-sharing. It explains why face sharing is the lower-assumption default in the present finite grammar.

# 20.7 Why Vertex Sharing Is Denser

A vertex participates in more possible tetrahedral neighborhoods than a face does. Vertex-sharing can therefore generate a larger local cluster.

But denser adjacency also creates more opportunities for:

- incompatible closure histories;
- duplicate support ownership;
- route collisions;
- global relabeling constraints;
- inconsistent recurrence.

Higher local connectivity increases the burden on the global consistency proof.

# 20.8 Default Does Not Mean Fundamental

The current status of \(G_1=4\) is **default native selector under tested scope**. It is not yet a theorem that every future scale must use coordination four.

The next gate remains a general branch grammar and larger-scope recurrence law.

# 20.9 Packet Growth Is Not Spatial Expansion

The words “growth” and “neighbor” can tempt a geometric reading. At this stage they mean more finite packet cells, gluing interfaces, and transport/support relations.

No physical length scale has been introduced. Therefore

\[
\boxed{\text{packet growth}\neq\text{cosmological expansion},}
\]

and

\[
\boxed{\text{cluster adjacency}\neq\text{physical lattice spacing}.}
\]

# 20.10 Recursive Capacity Versus Recursive Dynamics

The multiplication \(N_2=G_1N_1\) counts structural exposure capacity. It does not specify:

- the order in which packets attach;
- how long attachment takes;
- whether all slots are occupied;
- whether packets detach;
- whether support survives;
- whether recursion terminates.

A recursive counting ladder is not yet a recursive dynamical law.

# 20.11 The Quarantined 32-Step Temptation

Earlier chapters found several native 32-counts. Current governance still freezes the claim that these imply a universal 32-layer sequential hierarchy.

To establish a 32-step depth, source would still need layer ordering, transition law, termination, event semantics, and per-layer retention or attenuation normalization.

Repeated appearance of 32 strengthens its status as a native finite cardinality, not as a proven clock.

# 20.12 A Minimal Growth Ledger

| Field | Example |
|---|---|
| seed capacity | \(N_1=192\) |
| adjacency selector | \(G_1\) |
| branch type | face-sharing / dense |
| next capacity | \(N_2=G_1N_1\) |
| gluing interface | face / other |
| support ownership | explicit |
| gate history | explicit |
| recursion status | tested / open |
| physical geometry | not yet promoted |

# 20.13 Chapter Checkpoint

You should now be able to derive

\[
N_{2,\rm default}=768,
\qquad
N_{2,\rm dense}=2304.
\]

You should also be able to explain why \(G_{1,\rm default}=4\) and \(G_{1,\rm dense}=12\) have different governance statuses and why recursive packet count is not physical spatial growth.

# Exercises

1. Compute \(4\cdot192\) and write the companion congruence modulo 192.
2. Compute \(12\cdot192\) and write the companion congruence modulo 192.
3. Compute \(2304/768\). What does the answer say structurally?
4. Why is a shared triangular face a stronger interface than sharing only one vertex?
5. Why must shared simplices be represented once in the global chain complex?
6. State one allowed and one over-strong interpretation of \(G_1=4\).
7. If only two of four face-sharing slots are occupied, distinguish adjacency capacity from current occupancy.
8. List five pieces of information absent from \(N_2=G_1N_1\).
9. Why can higher adjacency density increase the proof burden?
10. Give three reasons 768 is not yet a physical volume.

# Research Audit

The growth chapter tells us how larger packet complexes may be assembled. But different triangulations can represent the same coarse boundary topology.

The next chapter studies the local rewrite that tests this issue:

\[
\boxed{\text{Chapter 21 — Pachner Moves}.}
\]

# Chapter Summary

Current one-step packet growth has a default face-sharing branch

\[
G_{1,\rm default}=4
\]

and a dense alternate

\[
G_{1,\rm dense}=12.
\]

These yield 768 and 2304 respectively. The branch counts are exact once their selectors are declared; their general recursive authority remains gated.

The governing lesson is:

\[
\boxed{\text{larger packet complexes require an adjacency law, not merely repetition of the seed}.}
\]

## Source and Governance Note

The current coefficient baseline records \(G_{1,\rm default}=4\) as a computed bridge/default native selector with tested-scope guard, \(G_{1,\rm dense}=12\) as an admissible dense alternate, and 768/2304 as branch-split structural ladder candidates.

The original selector artifact explicitly classifies the branch as discrete packet-cluster governance, **not physical lattice or continuum geometry**.

**Physical promotion remains 0.**
