# Unified Dynamics — Primitive \(\Omega_0\) Source Recovery and Adversarial Growth Audit

**Version:** v1.2 (source reconciliation and scoped amendment)  
**Date:** 2026-10-31, America/Chicago  
**Lane/status:** `DEVELOPMENT_NO_REGISTRY_ENTRY`; `SOURCE_RECOVERED__CONDITIONAL_COFACE_LAW__NATIVE_EVENT_AND_RESOURCE_OPEN`  
**Physical promotion:** **0**  
**Constructor:** GPT-6 (source recovery, proofs, executable checks)  
**Nonconstructor adversarial reviewer:** **not yet assigned / not completed**. Independent second implementation is not nonconstructor review.

## 1. Question and scoped answer

**Question.** Recover a source-backed primitive pre-birth rule that transitions from a point/edge/triangle to a filled tetrahedron or adds an adjacent tetrahedron without choosing the target cell after the fact. Independently attack the previous HOLD/BIRTH nonuniqueness witnesses and Q153–Q173 source interpretation.

**Answer.** There is an *explicit, historical, target-aware generative rewrite proposal* that earlier v1.0/v1.1 reports did not fully include: `ADMISSIBLE_COFACE_EXTENSION` and `BOUNDARY_FACET_PROPAGATION`. Under a binary alphabet and multiplicity cap 2, local maximal completion terminates at a balanced \(K_4\) simplex, and boundary propagation adds legal face-glued tetrahedra. This repairs the overly broad claim that no growth operation exists. It does **not** provide a native event clock, unique frontier choice, newborn burden/phase/Spin(3) seam, environment resource debit, persistence selector, or physical energy correspondence. The previous no-go for a unique event from *closure/symmetry/support alone* remains intact under its stated hypotheses.

The same original binary-label rule also gives a conditional **direct \(K_5\) simplex obstruction**: among five vertices at least three share a label, making an inadmissible monochromatic triangle. Multiple face-glued \(K_4\) tetrahedra can nevertheless form connected 3D clusters without adding the prohibited apex-to-apex edge. This is a property of the *chosen binary trion rule*; the choice \(q=2\) and historical tetrahedral target were explicitly disclosed, so it is **not a target-blind derivation of physical three-dimensionality**.

## 2. Controlling evidence and typed provenance

| Source | Version / identification | Relevant content | Source authority / caveat |
|---|---|---|---|
| `GRAPH_FIRST_LOCAL_ADMISSIBLE_COFACE_EXTENSION_PRIMITIVE_INDE.md` | Aug 2026 original Library file, `libfile_305337e32dcc8191b6e79908e8e4d14a`; title says v0.1, Library version marker not used as theory version | §§2–4 definition, terminal counts, local gluing; §5 Euler table; §7 target disclosure | Source proposal. §5 incorrectly states attachment changes Euler by +1; later superseded *for that claim only* by Oct 2 exact correction |
| `GRAPH_FIRST_PRIMITIVE_AUGMENTATION_MINIMIZATION_FOR_PRIORITY.md` | Earlier v0.1 Library file `libfile_ca5e233b012c81918b82b92f406fb5ec` | §4 local coface candidate, §5 maximal rule, §7 boundary-facet propagation | Designates candidate as `BEST_CURRENT_PRIMITIVE_CANDIDATE`; target-aware, not empirical law |
| `UD native coface growth and cluster selection audit.md` | 2026-10-02; GitHub blob `9ac884d727e65ddd4ed1c277d2ed4a7b91135d73`; original Library `UD_NATIVE_GROWTH_SELECTION_AUDIT_v0.1.md` | Replays 1,4,24,192,1920 histories and 2140 transitions; Euler correction; no unique cluster selector | `CANDIDATE_DEVELOPMENT_MATHEMATICS`, independent review pending |
| `UD inherited pattern retention through one coface birth.md` | 2026-10-02; GitHub blob `b15f92ddccfe888af19c43fe4842b087ef644cbf` | Six legal attachment locations, exact inherited-tag comparisons; newborn state open | Conditional supplied carrier and gates, not formed physical packet |
| `UD event admission and interface memory.md` | Oct 2026; GitHub blob `6719d0f77622eac59c5c88fc163b49adda664e6` | Local conditional first-admissibility and separate global shared authorization | Prepared local event does not authorize shared topology change |
| `UD_C5_CONTEXT_ADMISSION_AUDIT_AND_OCCUPANCY_LAW_v0.1.md` | 2026-09-14; Library `libfile_7418760dd3288191bcc88439f6128524` | §§14–22 registered *context* address onset \(\mu_\alpha=h_\alpha^Tc_4\), \(\ddot W=2\mu^2\) | Typed \(C_5^{ctx}\), *not* spatial \(C_3\); CRL-1, unpromoted |
| `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` | 2026-08-22; SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63` | G05, Q153–Q179 | Frozen receipt/support equations; constitutive birth/source terms open |
| `UD_K4_OMEGA0_PREBIRTH_SOURCE_CHANNEL_AUDIT_v1.1.md` | 2026-10-31, local predecessor | Oriented linear coupling uniqueness, conserved-transfer nonuniqueness | Narrow prior no-go stands; previous source coverage incomplete |
| `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md` | governance **proposal**, §§1–5 | Nonconstructor review before CRL promotion, retraction/provenance entries | No automatic promotion based on this constructor's checks |

**Source handling:** The original August source documents were read directly via Library. Their `.txt` snapshots are extracted-text copies, not byte-identical raw Markdown, because raw-byte materialization was not authorized. The October 2 audit was acquired as a raw Library copy and the identical substantive GitHub document was inspected. GitHub blob SHA and exact filenames establish repository identity. Do not infer a stronger current canonical state from archival claims labeled `LOCKED CANON` without the current ledger and independent proof.

## 3. Formal definitions and local completion theorem — EXACT under premises

State a finite graph \(G=(V,E)\) with vertex label \(b:V\to\{0,\ldots,q-1\}\), where \(q\ge 1\) is a **chosen** alphabet size. A candidate simplex \(\sigma\) is locally admissible when every label multiplicity \(c_j(\sigma)\le2\). A coface operation chooses an unsaturated label \(j\), creates a new vertex \(w\) with \(b(w)=j\), joins \(w\) to all vertices in \(\sigma\), and declares the enlarged simplex \(\sigma\cup\{w\}\) admissible. Topological simplex filling is defined by the rewrite; it is not an observed or energy-funded emergence law.

Define the exact integer deficit

\[
D(\sigma)=\sum_{j=0}^{q-1}(2-c_j(\sigma)).
\]

Every executed operation lowers \(D\) by exactly 1. A **maximal finite extension history**, if executed rather than indefinitely idled, ends at \(D=0\): precisely \(2q\) vertices and dimension \(2q-1\). Its count vector is uniquely \((2,\ldots,2)\) up to labeling and vertex permutations. The count of label-completion histories from \(c\) is the multinomial

\[
N(c)=\frac{D!}{\prod_{j=0}^{q-1}(2-c_j)!}.
\]

**EXACT replay:** 1,086 distinct nonempty count-vector seeds across \(q=1,\ldots,6\) were checked by independent dynamic recurrence and factorial formula. The *event time*, initial seed from absolute emptiness, choice among simultaneously legal label increments and any physical dimension are not fixed. For \(q=2\), the endpoint is a balanced \(K_4\). For \(q=3\), it is a \(K_6\); the binary alphabet is essential to the 3D conclusion.

## 4. Binary trion obstruction and gluing — EXACT under premises

For a complete graph \(K_n\), a monochromatic 3-clique exists iff some binary label occurs at least 3 times. Direct enumeration gives admissible binary labelings

\[
|\mathcal A(K_1)|,\ldots,|\mathcal A(K_6)|=(2,4,6,6,0,0).
\]

Hence \(K_4\) permits exactly six distinct assignments with counts \((2,2)\), while **every** binary labeling of \(K_5\) violates the trion restriction. The pigeonhole proof establishes the all-\(K_5\) result, not just the tested six cases.

A different operation glues a new completed \(K_4\) tetrahedron along one currently exposed triangular facet. The triangle contains two vertices of one binary label and one of the other, so the newborn's label is uniquely fixed as the deficient label. It attaches to the three face vertices, not to the old tetrahedron's opposite apex. The two opposite apices therefore have the same label but lack a connecting edge. Adding that edge would introduce a monochromatic triangle. Two face-glued \(K_4\)s have five vertices and **nine** distinct edges, not \(K_5\)'s ten.

The construction can therefore grow a 3D tetrahedral cluster **without** forming a 4D spatial simplex. It does not prohibit a separate 3+1 temporal geometry or context carrier, whose incidence, causal and metric bridge would need independent definitions.

## 5. Boundary propagation and explicit nonuniqueness — EXACT under premises

Let \(\mathcal T_m\) be a stacked 3-ball of \(m\) tetrahedra. Select a boundary triangle belonging to exactly one tetrahedron, append a fresh vertex of the unique deficient binary label, and add exactly the three new edges, three new triangular faces and one new tetrahedron. Thus

\[
\Delta f=(1,3,3,1),\qquad \Delta\chi=1-3+3-1=0.
\]

Every new tetrahedron has one existing neighbor across its attachment face, the cell-dual graph remains a tree, and

\[
f(m)=(m+3,3m+3,3m+1,m),\qquad
B_m^{\rm face}=2m+2.
\]

If all legal frontier choices are retained as history branches, the history count is

\[
H_1=1,\qquad H_{m+1}=H_m(2m+2).
\]

Independent exact enumeration through \(m=5\) gives \(H=(1,4,24,192,1920)\), 2,140 attachment transitions, and at \(m=4\) both chain degree \((1,1,2,2)\) and star degree \((1,1,1,3)\). Neither history counts nor a branch's visual simplicity constitutes a native probability or preference.

**Symmetry subtlety:** The abstract, unlabeled \(K_4\) has \(S_4\). A *fixed decorated* seed with labels \((0,0,1,1)\) has only the label-preserving subgroup \(S_2\times S_2\), order 4. Its four boundary faces form two orbits of size 2; no particular face is invariant. Therefore label preservation alone cannot choose one of four physical attachment locations. Treating the fixed labeled seed as itself fully \(S_4\)-invariant is incorrect; \(S_4\) instead acts covariantly on the family of relabeled decorated seeds.

**Infinite-extension issue:** \(B_m^{\rm face}=2m+2>0\) for every finite \(m\). If fresh vertices, legal faceting and continual event admission are always available, the grammar has no intrinsic finite cluster-size stopping point. Inverse retraction is a candidate, but when to retract versus attach remains an independent decision.

## 6. Q153–Q173 source audit and two genuinely distinct birth tasks

**Task A — complete an existing 2-shell into a filled 3-cell.** With all four triangular faces present, the oriented boundary vector can be formed before admitting a candidate interior. However, ledger Q169–Q173's *dynamic* support generator operates on a declared \(C_0\oplus C_1\oplus C_2\oplus C_3\) carrier. It does not decide the binary occupancy bit for an absent \(C_3\). Q173's current \(J_{23}=2h_f B_{3,f\tau}c_{2,f}c_{3,\tau}\) starts at zero for zero interior amplitude even if the *amplitude derivative* in a registered carrier is nonzero.

**Task B — create a new vertex, three new faces and an adjacent tetrahedron.** The coface rewrite mathematically supplies a new cell inventory, but the three new face amplitudes and three seam transport links are **not part of the prior actual carrier**. The shell-to-interior amplitude generator on a pre-existing \(C_3\) slot cannot be used as a direct source for this new-vertex operation without a typed initialization/transport map.

The receipt \(\Delta\rho=B_1j_B+s_B\) (Q153) and residual definition \(s_B:=\Delta\rho-B_1j_B\) (Q158) do not predict the new \(s_B\) from the old state. Q162's conditional relaxational burden flux does not create incidence entries or newborn frame/phase. Q169–Q179 establish micro support conservation and cell ownership **on admitted complexes**, not admission itself. G05 remains an open action normalization/obstruction bridge. A positive newborn support while all existing support, sources and boundary flux remain unchanged violates the declared closed support budget; transfer magnitudes are not selected by this observation.

The original source's claim `\Delta\chi=+1` for boundary attachment is **falsified** by the exact f-vector. The October 2 source explicitly repairs it to zero. **No existing source file was silently edited**; this is a scoped, append-only correction.

## 7. Narrow candidate onset from a separately typed context source

The Sep 14 `UD_C5_CONTEXT_ADMISSION...v0.1` defines a registered **context-address** candidate with overlap \(\mu_\alpha=h_\alpha^Tc_4^{ctx}\), zero initial context amplitude, and initial squared-amplitude acceleration \(\ddot W_\alpha(0)=2\mu_\alpha^2\). It selects the unique positive maximum in that context family; ties/zero drive mean HOLD. It expressly does not identify \(C_5^{ctx}\) with a spatial dimension or remove the need to register candidate descriptors.

As an **analogy / conditional calculation only**, register a candidate tetrahedral \(C_3\) slot, choose unit counting metric and the already known skew incidence block on \(C_2\oplus C_3\):

\[
J=\begin{pmatrix}0&-u\\u^T&0\end{pmatrix},\qquad
u=(-1,1,-1,1)^T,\quad u^Tu=4.
\]

Then for \(c_2(0)=u/2\), \(c_3(0)=0\), one has \(\dot c_3(0)=u^Tc_2(0)=2\) and

\[
c_3(s)=\sin(2s),\quad
S_2(s)+S_3(s)=1,\quad
\ddot S_3(0)=8.
\]

This exact result is checked by a third, separate symbolic program. In the *registered carrier* the source determines the initial amplitude derivative relative to the declared dimensionless parameter \(s\); this narrows the statement that all post-admission transfer magnitudes are arbitrary. It does **not** authorize the prior creation of that carrier, a positive waiting time, a physical duration, a native filling event, or a universal \(C_5^{ctx}\to C_3^{cell}\) transfer.

## 8. Adversarial audit and prior-claim amendment

| Claim / potential error | Review verdict | Amendment / condition |
|---|---|---|
| “There is no primitive growth rule anywhere in UD” | **FALSE at broad source level** | Historical coface rewrite found. Replace with “no source-complete event/formation law demonstrated” |
| “The coface rewrite derives why all reality is 3D” | **BLOCKED** | \(q=2\) and the cap are assumed, with target exposure disclosed; \(q=3\) permits higher dimension |
| “Four face-attachment choices imply a preferred first direction” | **NO-GO** | Four frontier choices, two fixed-label symmetry orbits; source choice/rate not specified |
| “A legal four-cell chain is structurally the same as a star” | **FALSIFIED** | Both are legal and have distinct dual degree sequences from the same seed |
| “Coface boundary attachment raises Euler characteristic by 1” | **FALSIFIED** | Exact \(\Delta\chi=0\); original archived text preserved, Oct 2 amendment identified |
| “Conservation alone gives a unique newborn support transfer” | **NO-GO under prior hypotheses** | Multiple lossless transfers or zero-amplitude newborn comparison outcomes exist; source drive remains open |
| “The \(C_5^{ctx}\) onset selector is the missing \(\Omega_0\) tetrahedron event rule” | **TYPE MISMATCH** | Context address is not 3D cell; registering candidate and selecting contact still open |
| “A zero initial Q173 support current prevents cell amplitude growth” | **FALSE if cell slot admitted** | \(\dot S_3(0)=0\) may coexist with \(\ddot S_3(0)>0\) |
| “A positive birth from nothing was reproduced” | **NOT SUPPORTED** | Existing seed and candidate inventory required; absolute genesis source not derived |
| “S4 fixed decorated seed has four interchangeable faces” | **SCOPE REPAIR** | Only \(S_2\times S_2\) preserves fixed labels; covariant full S4 acts on decorated seed family |
| “This is a nonconstructor-reviewed bridge” | **FALSE** | Same-constructor adversarial implementation and review packet only; third-party review PENDING |

The previous v1.1 mathematical theorem about the uniquely oriented linear coupling remains valid on its declared carrier. Its broader rhetoric that no native source even specifies a topology-growth operation is **superseded by this source-recovery amendment**. The prior HOLD/BIRTH no-go is not globally retracted: it still applies to conservation/closure/symmetry constraints *without the new event generator and resource laws*.

**No type or normalization collisions accepted:** \(192\) legal growth histories at four cells is not the original 192-state packet capacity; \(4/3\) geometric frame does not automatically equal the frozen F03 dyad; Q169 \(S_\mu\) is not a physical energy unit; \(C_5^{ctx}\) is not a five-dimensional spacetime claim.

## 9. Execution and reproducibility

Three executable programs were run locally:

1. `UD_OMEGA0_ARCHIVE_COFACE_REPLAY_v1_2.py`: **30,878** exact assertions, all 1,086 nonempty local count seeds \(q=1\ldots6\), all 1,920 five-cell histories, and \(K_5\) exclusion.
2. `UD_OMEGA0_SOURCE_ADVERSARIAL_REVIEW_VERIFY_v1_2.py`: **86** independently implemented exact assertions using a different label enumeration and explicitly constructed chain/star witnesses. This is still the same research constructor.
3. `UD_OMEGA0_REGISTERED_SLOT_ONSET_CHECK_v1_2.py`: **37** exact symbolic assertions for the already-registered \(C_2\leftrightarrow C_3\) skew flow, its onset, and conservation.

These are executable conditional mathematical checks; assertion totals are neither independent scientific reviews nor empirical evidence. The source records were read and archived snapshots were preserved with their retrieval types. The underlying August Markdown sources could be materialized only as extracted **text**, not authenticated original raw bytes. No repository-wide CI or physical test is inferred from these local results.

## 10. Verdict and reopening conditions

**AUTO_LOCK (mathematical scope):** conditional coface termination theorem, local q2 \(K_5\) obstruction, exact boundary attachment f-vector and \(\chi\) correction, dual-tree/boundary count, same-seed chain/star witnesses, and registered-slot onset conditional on incidence dynamics. The source-side *review status* is development and nonconstructor-PENDING; this is not a custodian canonical promotion.

**AUTO_FREEZE:** (i) claiming native physical spontaneous point-to-K4 formation, (ii) universal 3D selection without the binary/cap premise, (iii) source-derived preference for frontier facets or cluster motifs, (iv) use of context \(C_5\) as spatial \(C_3\), (v) fully funded energy/burden birth, and (vi) broad assertion that no topology growth candidate exists anywhere in UD.

**Reopening gate:** A versioned primitive law must determine, from prior admitted state, (a) vertex/face candidate enumeration without target-forcing, (b) event time/authorization and one frontier facet, (c) newborn \(\rho,\theta,\chi\) and seam links, (d) burden/support source-debit and open-system boundary receipt, and (e) persistence/stability against HOLD, alternate facets, retraction and nonbinary controls. Require nonconstructor adversarial review before CRL promotion, with exact source/version and held-out comparisons. **Physical promotion remains 0.**
