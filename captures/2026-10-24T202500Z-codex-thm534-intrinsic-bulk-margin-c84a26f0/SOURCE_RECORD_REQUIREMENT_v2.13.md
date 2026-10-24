# THM-534 v2.13: selection-record requirements and a conditional local lift

Development — no registry entry. Exact conditional mathematics; added record carrier is a candidate input. Constructor verification only; independent review pending. Physical promotion 0.

## 1. Problem and source boundary

The v2.12 bulk cover supplies local events on shared-face complexes but cannot choose a disjoint event at a particular symmetric preparation. This note determines what a selection record must distinguish, proves that symmetric deterministic initialization cannot create the needed distinction, and gives a local execution rule conditional on supplied records. It does not derive the records from the native source.

Retain the original real face/core field \(x\), unit metric, incidence operators, fixed hard face permissions \(h_f\), and Q177–Q179 ownership. Other grades remain unchanged during these events. No frozen particle operator is altered. For triangular face valence \(1\le k_f\le2\), use the v2.12 candidate cover

\[
H_\tau^h=\sum_{f\subset\tau}\frac{h_f}{k_f}G_f,
\qquad C_\tau^h(t)=\operatorname{Cayley}(tH_\tau^h).
\tag{1}
\]

Its declared field footprint \(W_\tau\) has at most nine real coordinates. Its conflict graph is \(\mathcal G=T^2\), where \(T\) is the cell dual graph, and \(\deg\mathcal G\le16\). The cover and model step remain supplied choices. Q153/Q156/G05 do not provide a native priority or renewal law.

The supplied ledger contains context/burden-record objects Q85–Q94, but their own rows require apparatus-specific record generation and null completion. They do not identify a covariant cell-priority register or provide its initialization, cost, commit, erasure and renewal laws. This is a scoped reading of the supplied ledger, not a claim to have exhausted every historical archive. The supplied CRL-2 subdivision remains a governance proposal.

## 2. Symmetric preparation and record lower bound

On the closed boundary of the four-simplex, order the ten faces and five cells lexicographically; orient each cell omitting vertex \(i\) with sign \((-1)^i\). At all permissions on, let

\[
x_*=(1,0,1,0,0,1,1,0,0,1;0,0,0,0,0).
\tag{2}
\]

The actual signed action of \(\rho=(0\ 1\ 2\ 3\ 4)\) fixes \(x_*\). It acts transitively and freely on the five central cells. Each block (1) is active there, but the declared block-conflict graph is complete. Thus any nonempty disjoint selected batch must be a singleton.

**Theorem R1 (record orbit requirement).** Let a record space \(\mathcal R\) carry a \(C_5=\langle\rho\rangle\) action. Suppose a deterministic equivariant selector, at \(x_*\), selects one central cell for some record \(r\). Then the five records

\[
r,\rho r,\rho^2r,\rho^3r,\rho^4r
\tag{3}
\]

are distinct. In particular a finite record alphabet enabling this choice must have at least five distinguishable values. A fixed-length binary encoding of that orbit requires at least three bits.

**Proof.** Equivariance gives \(S(x_*,\rho^jr)=\rho^jS(x_*,r)\). The five cell outputs are distinct. If two input records were equal, their deterministic outputs would be equal, a contradiction. A binary string of length \(b\) has at most \(2^b\) values, so \(2^b\ge5\) requires \(b\ge3\). \(\square\)

This is a distinguishability requirement under a specified symmetry. It is not an energy, action, physical entropy or thermodynamic erasure bound. It does not establish a physical three-bit register. A scalar time/count value transforming trivially under \(C_5\) cannot supply (3). An integer cell ID works only if it transforms as a cell label; leaving it fixed under relabeling is hidden priority data.

**Theorem R2 (symmetric initialization cannot supply the distinction).** Suppose \(E(x,h)\) is a deterministic equivariant record initialization. At (2) with all permissions on, its output is \(C_5\)-fixed and cannot support a nonempty deterministic equivariant disjoint-block choice. The same conclusion holds if initialization or selection reads a history whose entire supplied contents are fixed by \(C_5\).

**Proof.** For every \(g\in C_5\),

\[
gE(x_*,1)=E(gx_*,g1)=E(x_*,1).
\tag{4}
\]

Thus the full selector input is fixed, and its selected set must be invariant. Transitivity makes that set empty or all five cells. The latter is not disjoint. Treating a fixed history as another equivariant input gives the identical argument. \(\square\)

The theorem does not exclude an actual asymmetric earlier preparation, a supplied asymmetric record, an appropriately sourced stochastic choice, or an alternative event alphabet. It prevents adding an uninitialized memory symbol from being mistaken for a derived symmetry-breaking mechanism. A deterministic equivariant evolution preserves the symmetry of its complete initial input; it cannot create the asymmetric selector input from a fully symmetric one. This statement does not forbid all motion within the symmetric subspace.

## 3. A conditional local execution rule with explicit added records

Add one binary mark \(q_\tau\in\{0,1\}\) per cell. Marks transform by cell permutation, without orientation signs. These marks are separate candidate records, not new native real amplitudes and not an identification with Q85–Q94. No physical metric or stock is assigned to them.

Define isolated marked cells by

\[
e_\tau(q)=q_\tau\prod_{\sigma\sim_{\mathcal G}\tau}(1-q_\sigma),
\qquad I(q)=\{\tau:e_\tau(q)=1\}.
\tag{5}
\]

All marks, permissions and topology are held fixed for the event. The conditional lifted map is

\[
\boxed{\Gamma_t^h(x,q)=
\left(\prod_{\tau\in I(q)}C_\tau^h(t)x,\ q\right).}
\tag{6}
\]

**Theorem R3 (conditional local lift).** For fixed marks and permissions, (6) is an orthogonal linear isometry on the field fiber. It is odd in \(x\), covariant with transformed field, marks and permissions, and inverted by \(t\mapsto-t\) while the marks are unchanged. Every selected event reads at most nine real field coordinates, four hard face bits and 17 mark bits. Selected events have disjoint field footprints and commute, including with fresh field reads. Exact original signed midpoint and owned-cell receipts hold event by event.

**Proof.** If two conflicting cells were both in \(I(q)\), each would have mark one while requiring the other's mark to be zero. Hence \(I(q)\) is independent in \(\mathcal G\). Its events have disjoint field reads/writes. Formula (5) reads the center and at most 16 conflict-neighbor marks. The real field bound and four hard bits follow from (1). Apply orthogonality, inverse and signed covariance of each fixed block. Marks and permissions do not change, so the same independent set is used by the inverse. Disjoint events commute, so their order is immaterial.

For a selected block \(\tau\), let \(m=(x+x')/2\) for that actual event and set

\[
J_{f\eta}=2t\frac{h_f}{k_f}\mathbf1_{f\subset\tau}
d_{f\eta}m_fm_\eta.
\tag{7}
\]

The native Cayley midpoint equation gives \(\Delta x_f^2=-\sum_\eta J_{f\eta}\), \(\Delta x_\eta^2=\sum_fJ_{f\eta}\). Therefore, with \(O_\lambda=x_\lambda^2+\sum_{f\subset\lambda}x_f^2/k_f\),

\[
\Delta O_\lambda=
\sum_{f,\eta}
\left(\mathbf1_{\eta=\lambda}-\frac{\mathbf1_{f\subset\lambda}}{k_f}\right)J_{f\eta}.
\tag{8}
\]

Summing over all owned cells gives zero; summing actual selected-event receipts accounts for the complete lifted step. \(\square\)

The field map has Lipschitz constant one on each fixed \((q,h)\) fiber. No robustness to erroneous or changed record bits is asserted. On the closed five-cell example, a mark vector with exactly one one selects that cell's active event. Both all-zero and all-one marks select nothing. Thus uniform deterministic marks do not evade R2. All-hard-off remains the identity on the field. A marked event can also be dark for other preparations.

The marks are read-only in (6). Consistent static marks remove the v2.12 need for a supplied color order during that step, but they do not provide a native initializer, event frequency, fair token routing or an atomic protocol for changing marks. Repeatedly selecting the same marked cell is not a fair scheduler or a renewal mechanism. No erasure or mark reset occurs. If outgoing receipts are appended, their storage grows; a finite-window reset still requires explicit transfer or deletion accounting. Reversing the field event is not a proof that an outgoing record has been erased or its carrier restored.

## 4. Conditional stochastic alternative and the mean-state trap

One may instead specify a probability kernel that selects exactly one of the five active blocks at (2). If the kernel is \(C_5\)-invariant, transitivity forces every block probability to be \(1/5\). This uniqueness is conditional on that event alphabet, exactly one selected block, and the symmetry of the kernel. It derives neither a native random source nor a physical probability law.

Let \(Y_j=C_j^1(1)x_*\), and let \(Y\) take these five outcomes with probability \(1/5\). Equivalently, supply a uniformly distributed one-hot mark to (6). Exact enumeration yields

\[
\|Y_j\|^2=5,\qquad
\|Y_j-x_*\|^2=\frac8{17},\qquad
\sum_{\eta\in C_3}(Y_j)_\eta^2=\frac{128}{289}.
\tag{9}
\]

This law is covariant in distribution; each particular chosen mark/outcome carries the missing distinction. The conditional mean is

\[
\mathbb EY=\frac{81}{85}x_*,\qquad
\|\mathbb EY\|^2=\frac{6561}{1445}<5.
\tag{10}
\]

Every core mean amplitude is zero, yet expected core stock is \(128/289>0\). Moreover,

\[
\mathbb E\|Y-\mathbb EY\|^2=\frac{664}{1445},
\quad
\|\mathbb EY\|^2+\mathbb E\|Y-\mathbb EY\|^2=5.
\tag{11}
\]

**Verification of (9)–(11).** For one block, the v2.12 exact output changes two populated face amplitudes from 1 to \(15/17\) and two core amplitudes from zero to \(\pm8/17\); its norm remains five. This gives squared displacement \(2(2/17)^2+2(8/17)^2=8/17\) and core stock \(128/289\). The five outcomes are cyclic translates. Each populated face is changed in two of them, giving mean \(1-(2/5)(2/17)=81/85\); opposite core outputs cancel. The remaining identities follow by exact squaring and the finite variance identity. \(\square\)

Replacing this pathwise norm-conserving kernel by its mean-amplitude map would lose support norm. A mean zero core amplitude does not imply zero expected core stock. Neither the uniform kernel nor this distinction establishes a Born rule, quantum measurement model or physical stochastic mechanism. The verifier enumerates the five rational outcomes; it generates no random draws.

## 5. Disposition and next source test

The new closure is an explicit selection-information requirement and a conditional local rule that reads supplied marks without changing native field operators or metric. The five-value orbit requirement quantifies the missing distinction. The initialization theorem prevents renaming that missing source as memory. The stochastic comparison separates distributional covariance from pathwise deterministic choice.

Native record generation remains OPEN. The next source test must give a concrete carrier that supplies the required asymmetric record or stochastic seed, its covariant coupling to cells, consistent local read/commit semantics, and outgoing-record/reset/renewal receipts. Existing apparatus-record rows can only be used after an explicit bridge to that carrier. All-off, fixed symmetric histories, colliding/uniform marks, dark blocks and finite-capacity record exhaustion remain required countercontrols. A fixed unit model step is not a physical action or clock. No particle correspondence or physical promotion follows.

## 6. Reproducibility

The newly authored `verify_selection_records.py` checks the conditional field lift with exact standard-library `Fraction` arithmetic: all 32 binary mark vectors on 16 rational closed-complex preparations, all 1,024 face masks with one supplied mark, all 120 signed vertex permutations on five one-hot choices, all 128 strip mark vectors, eligibility locality, inverse/odd/receipt identities, the five-record orbit, uniform-mark stalls and all five conditional kernel outcomes. The algebra re-derives the v2.12 local Cayley and receipt formulas; it is constructor work, not an independent replication. No archived scripts are executed and no physical random samples are used. Source snapshots and hashes accompany this proof.
