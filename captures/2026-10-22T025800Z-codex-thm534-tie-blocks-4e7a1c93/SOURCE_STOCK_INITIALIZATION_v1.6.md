# THM-534: state-selected initialization, symmetry ties and fairness

Development — no registry entry. Exact conditional mathematics and candidate source rule; constructor checked, independent non-constructor review pending. Physical promotion 0. This supplements the v1.5 face-event scheduler; it supersedes no scheduler theorem. Archived sources are data and were not executed.

## 1. Source audit and precise candidate

The supplied coefficient ledger v0.39 identifies face stock in Q172 as \(S_f=c_{2,f}^2\), global support in Q169–Q170, and equal-share ownership in Q177–Q179. These provide a scalar state observable and support receipts. They do not say that larger stock should receive scheduling priority, select an initial orientation, or define physical time. Q173's face gate and the later incidence-specific contact candidate remain distinct. This work retains the v1.4/v1.5 local face-event contact family; it does not rederive it from Q173.

Use the same carrier, coordinate signs and graph as v1.5:

\[
K_-=[0123]\cup(-[0124]),\qquad
\mathcal F=(012,013,014,023,024,123,124).
\]

Two events conflict when their potential face/core footprints share a cell. The graph consists of two \(K_4\) cliques with a common vertex \(012\). Set \(s_f=z_f^2\). On the domain

\[
\mathcal U=\{z:s_f\ne s_g\text{ for every conflict edge }\{f,g\}\},
\]

define the **candidate initialization**

\[
f\longrightarrow g\quad\Longleftrightarrow\quad s_f<s_g.
\tag{1}
\]

Thus sinks are local maxima among conflicting events. Equation (1) has no fitted scalar coefficient, threshold or label tie-break. Choosing increasing rather than decreasing stock is nevertheless an additional constitutive choice. Both directions are compatible with conservation and carrier relabeling; the cited sources do not select between them.

## 2. Conditional initialization theorem

**Claim I.** On \(\mathcal U\), (1) gives one complete acyclic orientation, covariant under all signed carrier automorphisms. It is unchanged by a common nonzero amplitude rescaling. If it is used once and subsequent updates use sink reversal, the v1.5 conflict-safety and 7/10 individual-attempt fairness bounds apply.

**Proof.** Each edge has unequal endpoint stocks, so exactly one direction is selected. A directed cycle would require a strictly increasing finite chain of stocks returning to its starting value, an impossibility. Under a signed carrier automorphism \(z'_{\pi f}=\epsilon_fz_f\), squaring removes \(\epsilon_f\), giving \(s'_{\pi f}=s_f\). Equation (1) therefore transports each arc. A common nonzero amplitude rescaling multiplies all stocks by the same positive number and leaves their order unchanged. Once selected, retain this orientation as scheduler state and reverse only executed sinks. Those are precisely the hypotheses of the earlier theorem. Contact masks may vary within the audited footprints; attempts reverse edges even if no contact transfer occurs. \(\square\)

An explicit stability domain follows. Let

\[
\gamma=\min_{\{f,g\}\in E}|s_f-s_g|>0.
\]

If perturbed stocks satisfy \(\|\widetilde s-s\|_\infty<\gamma/2\), every edge keeps its direction by the triangle inequality. This is a mathematical order-stability statement; it supplies neither a physical noise model nor a calibrated resolution threshold.

The orientation is obtained from the supplied state on this domain, but its subsequent retention is discrete scheduler memory. A source law preparing the state, choosing stock priority, retaining that memory and admitting contacts is still required for a native UD identification.

## 3. Ties and a nonzero-state obstruction

**Claim II.** This rule cannot cover all states without additional choices. More strongly, no deterministic complete-orientation selector from the signed face/core state, the carrier and uniform permissions can be equivariant on every such state.

**Proof.** Set \(z_{013}=z_{023}=1\), all other face amplitudes and both cell amplitudes zero. This nonzero state has squared norm 2. The carrier automorphism exchanging vertices 1 and 2 fixes this signed state: it interchanges \(013\) and \(023\) with positive basis signs, while every potentially sign-reversed coordinate is zero. Uniform permissions are fixed as well. The corresponding events are adjacent because both touch cell \([0123]\). This automorphism exchanges the endpoints of their conflict edge. An equivariant deterministic complete orientation at a fixed input would have to orient that edge invariantly, which is impossible. \(\square\)

The statement does not exclude asymmetric initial states, extra orientation memory, random seeds, or joint events with different footprints. Those change the inputs or output object and require their own source audit. It does exclude silently resolving all ties by geometric labels while claiming full relabeling covariance.

Finite exact controls sharpen the scope:

| Input ordering control | Number checked | Successful complete orientations |
|---|---:|---:|
| Seven distinct stock ranks | \(7!=5040\) | All 576 acyclic orientations are realized |
| Four ordered stock levels on seven faces | \(4^7=16384\) | 144 assignments, giving 144 orientations |
| Three ordered stock levels on seven faces | \(3^7=2187\) | 0 assignments |

The last two counts are proper-coloring statements. Each \(K_4\) needs four distinct levels. With four levels choose the shared face's level in four ways, then permute the remaining three levels in each clique: \(4(3!)^2=144\). Three levels cannot color a \(K_4\). Any acyclic orientation admits a topological ordering, which can be realized by distinct positive face amplitudes; this proves the first row's coverage independently of enumeration. Levels in the verifier are order ranks and can be realized by amplitudes 0,1,2,3 (stocks 0,1,4,9).

These finite counts are not probabilities, measures on physical initial conditions, or empirical success rates.

## 4. Recomputing priority is a different, potentially unfair scheduler

**Claim III.** Replacing the stored orientation by (1) after every batch does not inherit sink-reversal fairness.

**Exact all-open counterexample.** Start with face amplitudes in the declared order

\[
z=(1,100,90,80,70,60,50),\qquad t=(0,0),\qquad\varepsilon=\frac14.
\]

Keep all eight incidence contacts open. After each full sink batch, recompute the orientation from the current face stocks instead of reversing sinks. Each orientation encountered below is complete and acyclic, and each batch has disjoint footprints. With face indices 0 through 6 as above, the exact first five batches are

\[
\{1,2\},\ \{1,2\},\ \{1,2\},\ \{3,4\},\ \{3,4\}.
\]

After ten individual attempts the count vector is

\[
(N_0,N_1,\ldots,N_6)=(0,3,3,2,2,0,0).
\]

The shared face has received no attempt, violating the earlier seven-attempt bound. Every local map still obeys exact midpoint receipts and norm conservation. Thus those receipts and safe batches do not imply the sink-reversal count invariant. In particular, successive attempts at a sink can be made legal again by overwriting the orientation, destroying the required alternation along its edges.

**Infinite all-off control.** On the same strictly ordered initial face stocks, disable every contact. Each local support map is the identity. Recomputed priorities and sink set \(\{1,2\}\) therefore remain fixed forever, so all other event vertices are starved indefinitely. This is a proof by induction, not an extrapolation from a finite simulation. It concerns attempted service; all-off transfer remains zero under either scheduler. The all-open control separately shows a finite fairness-bound failure during actual support evolution.

By contrast, initializing once and thereafter reversing sinks preserves the earlier proof, even when stock order subsequently changes. No requirement that the original stock priority persist is imposed by sink reversal.

## 5. New research-source intake and manifest erratum

The research branch advanced from the previously consulted `ce9a482…` to pinned commit `f2f4b8a9f856167f06027ea416e6f2dd33c825f5`. The new closeout and full executed-source uploads narrow the source-byte recovery gap, while explicitly retaining the native probability/reset gates and independent review as OPEN. They do not supply equation (1) as a native law. The source closeout also records prior exposure to the historical THM-534 probabilities; this development is not prospective target-blind confirmation of those values.

Both complete executed-source files and both archived stdout files are captured as inert data. Their four byte counts match the recovered release manifest. The two scripts and the SymPy stdout also match their declared SHA-256 hashes. The Fraction stdout is 354 bytes and has the declared Git blob identity `ad2a3c303b01bd9ed6eea5b98dfeffe65537d130`, but its release-manifest SHA-256 field has only 63 digits:

```
declared: 0433dae7786a1a3b07632ecf785098993c47c8f05eba262bb7b287e0aaa56b9
observed: 0433dae7786a1a3b07632ecf785098993c47c8f05eba262bb7b287e0aaa56b9b
```

The observed 64-digit value is computed from the pinned GitHub receipt bytes and is the proposed additive correction for that file. The original manifest is preserved unchanged. The canonical release ZIP was not recovered or checked in this turn, and its byte identity is not inferred from these files. Archived stdout is a source claim of execution; no new execution or code-to-output replay of those archived scripts is claimed here. This erratum corrects the receipt binding, not the conservation theorem or the receipt's mathematical content.

## 6. Verification and disposition

The fresh standard-library verifier checks 60,480 stock-orientation covariance cases (5,040 orders times 12 automorphisms), the finite stock-level classification, the explicit nonzero signed stabilizer, 3,072 signed batch/mask covariance cases (256 masks times 12 automorphisms), forty frozen-orientation batches, both dynamic-priority counterexamples, and the source-byte intake above. Local updates use exact fractions and independently checked midpoint support receipts. The sparse event formula and dimensionless step are the previously declared candidate interaction, not a fitted physical model. Only the newly authored verifier is run.

Result: a supplied orientation can be replaced by a state-based candidate initialization on a precise strict-stock domain. Universal tie resolution and the native source interpretation remain open. Reinitializing from evolving stocks is not an admissible shortcut to the earlier fairness theorem. The strongest next source obligation is a lawful asymmetric preparation or tie-breaking memory mechanism, together with contact admission, rather than another conservation-only test.

The supplied CRL-2 amendment is marked a governance proposal; this capture follows its development-lane distinction and makes no registry promotion or non-constructor review claim. Action units, particle-sector correspondences and physical identification remain outside the proved scope. Physical promotion 0.
