# THM-534: native-carrier local face-margin prototype

Development — no registry entry. Exact conditional event construction on the original real support carrier; the selection prescription remains CANDIDATE. Constructor checked; independent review pending. Physical promotion 0.

## 1. Return to native carrier variables

This programme targets native locality and selection directly. It uses the original real face/core coordinates \(x\), signed incidences \(d_{f\tau}\), unit metric, Q171–Q173 support currents and Q177–Q179 ownership. It introduces no cotangent dual, complex support, gate momentum or physical energy Hamiltonian. This is a separate source-bound prototype, not the v2.4 enlarged model with variables silently removed. The full 23-coordinate carrier can retain its other coordinates unchanged during these face/core events.

Let \(G_f\) be the skew face-star generator coupling face \(f\) to *all* its incident cores with their original incidence signs. Set \(k_f=n_3(f)\). A single scalar weight multiplies the entire face star, consistent with the face-level placement of the Q173 gate. Soft weights and their evolution are additional constitutive structure; the ledger freezes hard face multiplication, not the rule below.

Faces conflict when they share a core. Denote the neighbors of face \(f\) in this graph by \(\mathcal C(f)\). Define the fixed read set

\[
\mathcal R_f=\bigcup_{g\in\{f\}\cup\mathcal C(f)}
\left(\{g\}\cup\{\tau:g\subset\tau\}\right),
\qquad E_f=\sum_{i\in\mathcal R_f}x_i^2.
\tag{1}
\]

All considered face events are initially assumed legally available under a separately justified hard admissibility predicate. A current score does not establish geometric closure or integrity. If a supplied frozen hard face permission \(h_f\in\{0,1\}\) restricts events, replace \(w_f\) by \(h_fw_f\). Conservation, independence and aggregate gain of active stars persist; robustness then concerns fixed permissions. Blocked neighbors may still suppress a winner under this precise masked policy. Every-hard-face-off remains absorbing, and this construction does not derive hard-permission changes or universal self-reset.

## 2. A declared aggregate-influx competition law

From the ungated instantaneous native currents define

\[
s_f(x)=\left[2x_f\sum_{\tau\supset f}d_{f\tau}x_\tau\right]_+,
\quad
r_f=\left[s_f-\max\big(\{0\}\cup\{s_g:g\in\mathcal C(f)\}\big)\right]_+.
\tag{2}
\]

The proposed dimensionless face weight is

\[
\boxed{w_f(x)=\begin{cases}
r_f/(k_fE_f),&E_f>0,\\0,&E_f=0.
\end{cases}}\tag{3}
\]

**Explicit new constitutive choice:** strict local superiority of *aggregate* inward face-to-core flow supplies activity, and activity vanishes proportionally to that superiority after local-stock normalization. This preference and normalization are not implied by Q171, Q173 or conservation. They are the source law to review, not a theorem that the native law has been recovered. No measured target or fitted coefficient enters (2)–(3), but event normalization and the law itself remain supplied choices.

**Theorem L1 (independence and bounds).** \(0\le w_f\le1/\sqrt{k_f}\). Positive-weight stars are mutually disjoint in field coordinates.

**Proof.** Cauchy–Schwarz gives

\[
s_f\le2\sqrt{k_f}|x_f|\|x_{\mathrm{core}(f)}\|
\le\sqrt{k_f}\big(x_f^2+\|x_{\mathrm{core}(f)}\|^2\big)
\le\sqrt{k_f}E_f.
\]

Thus (3) has the asserted bound. If two conflicting faces both had positive weight, (2) would require both \(s_f>s_g\) and \(s_g>s_f\), a contradiction. Distinct nonconflicting stars have distinct face coordinates and no shared core. \(\square\)

For a tetrahedral pseudomanifold with \(k_f\le2\), each face has at most six conflicting faces. The read set has at most seven faces and eight cores, hence at most **15 real coordinates**, independent of total carrier size; each event writes at most **three** field coordinates. Indeed, each of the at most six neighboring faces shares a core already incident to \(f\), and can introduce at most one further core. On \(K_-\), read-set sizes are nine for the shared face and six for each private face; write-set sizes are three and two. This locality bound does not apply unchanged to unbounded nonmanifold face valence.

## 3. Exact finite event and native support receipts

Freeze all weights from one pre-event snapshot. For a declared dimensionless model step \(0<\varepsilon\le1\), apply

\[
\boxed{\Phi_\varepsilon(x)=
\operatorname{Cayley}\!\left(\varepsilon\sum_fw_f(x)G_f\right)x.}\tag{4}
\]

Because the active stars are disjoint, (4) is exactly the parallel collection of their small star Cayley maps. There is no global inverse to compute and no arbitrary ordering of overlapping active events. Face stars with weight zero act as identity. The value \(\varepsilon=1\) is an event convention, not a physical action-unit derivation.

**Theorem L2.** The update preserves the original real \(\|x\|^2\), and for \(m=(x+\Phi_\varepsilon(x))/2\),

\[
\mathcal J_{f\tau}=2\varepsilon w_f d_{f\tau}m_fm_\tau,
\quad
\Delta x_f^2=-\sum_\tau\mathcal J_{f\tau},
\quad
\Delta x_\tau^2=\sum_f\mathcal J_{f\tau}.
\tag{5}
\]

Every fixed equal-share owned-cell receipt follows by applying its Q177 weights to (5).

**Proof.** At the frozen snapshot, the generator is real skew, so its Cayley map is orthogonal. Its midpoint equation is \(\Delta x=\varepsilon\sum_fw_fG_fm\). Multiplication coordinatewise by \(2m_i\) gives (5), then fixed ownership weights give the owned receipts. This argument includes zero weights and changes in which face wins at different snapshots. \(\square\)

**Theorem L3 (actual aggregate inflow).** Every active star has strictly positive *executed aggregate* core-stock gain under (4) for \(0<\varepsilon\le1\).

**Proof.** For one active star, let \(a=|x_f|>0\), \(b=|\sum_\tau d_{f\tau}x_\tau|/\sqrt{k_f}>0\). Positivity of \(s_f\) means its face and bright-core amplitudes have matching signs. The other core components are dark under this isolated star. In its two-dimensional bright plane, the generator has strength \(\sqrt{k_f}\). Put \(t=\varepsilon\sqrt{k_f}w_f/2\). Equations (2)–(3) imply

\[
0<t\le\frac{\varepsilon ab}{E_f},\quad
m_a=\frac{a-tb}{1+t^2}>0,
\quad m_b=\frac{b+ta}{1+t^2}>0,
\]

since \(E_f\ge a^2+b^2>b^2\) and \(\varepsilon\le1\). Thus the exact bright-core gain is \(2\varepsilon\sqrt{k_f}w_fm_am_b>0\). Disjointness makes this the actual parallel-event gain. \(\square\)

This is aggregate gain, not guaranteed gain of each incident core. Individual signed receipts in (5) remain necessary: one core can lose while the total incident-core stock increases. A rule requiring every incident core to gain would be an additional eligibility condition.

The snapshot qualification is essential. Disjoint active stars have disjoint writes, but their read sets can include one another's core coordinates. Recomputing a weight after another event is therefore a different map and can depend on order. For example, prepare \(x_0=-1/2,x_1=x_2=2,x_7=1,x_8=-1\), with other coordinates zero. Both private faces 013 and 014 initially win with weight \(8/25\). Their frozen maps commute; their maps with weights recomputed between executions do not. The accompanying verifier retains this distinction. A local event reads bounded data, but the displayed parallel rule still assumes a common pre-event snapshot; no native asynchronous clock or snapshot register has been derived.

## 4. Robust update even when the winner set changes

The weight itself can have a directional limit at a zero read-set stock, but the *state increment* has a unique zero limit there. For \(k_f\le2\) one obtains the global increment bound

\[
\left\|D\big[(\operatorname{Cayley}(\varepsilon w_fG_f)-I)x\big]\right\|
\le13\varepsilon
\tag{6}
\]

at differentiability points with \(E_f>0\), and the increment extends continuously by zero at \(E_f=0\).

**Proof of bound.** Write \(R=\sqrt{E_f}\). Every competing score is a positive part of a quadratic form of operator norm at most \(\sqrt2\) on the read set. Thus \(\|\nabla r_f\|\le4\sqrt2R\) almost everywhere, and \(r_f\le\sqrt{k_f}E_f\) gives \(\|\nabla w_f\|\le6\sqrt2/R\). The frozen Cayley increment operator has norm at most \(\varepsilon w_f\sqrt{k_f}\le\varepsilon\). Its derivative with respect to \(w_f\), applied to the star coordinates, has norm at most \(\varepsilon\sqrt{k_f}R\). The chain rule gives \(\varepsilon+12\varepsilon\). Finally the increment norm is at most \(\varepsilon R\), proving its zero extension. Integrating the bounded piecewise derivatives along lines, splitting at zero read-set stock when necessary, gives the global Lipschitz result. \(\square\)

The associated candidate local vector field \(F(x)=\sum_fw_f(x)G_fx\) is also globally Lipschitz on this finite carrier, conserves the original norm, and has a well-posed norm-bounded flow. This formal model parameter is not physical time.

On \(K_-\) there are seven faces, so the whole map is Lipschitz with the deliberately conservative bound

\[
\|\Phi_\varepsilon(x)-\Phi_\varepsilon(y)\|
\le(1+91\varepsilon)\|x-y\|.
\tag{7}
\]

At a score tie, the affected face margins vanish and their increments approach zero; the method does not switch a finite-amplitude contact map discontinuously. This continuity is a property of the displayed response law, not proof of a uniquely sourced constitutive law. Step size, physical rate and canonical structure are not obtained from (7).

## 5. Exact symmetric witness and a decisive nonuniqueness control

Use the original real state

\[
x=(-1,1,1,-1,-1,1,1,1,-1)
\]

in the ordered seven-face/two-core coordinates of \(K_-\). It is fixed by the signed cell reflection and the shared-vertex 3-cycle. Every primitive face/core current has ungated value 2. The shared face has aggregate score 4; every private face has score 2. Thus only the *whole shared face star* wins, with

\[
r_0=2,\quad E_0=9,\quad k_0=2,\quad w_0=\frac19.
\]

For \(\varepsilon=1\), the affected coordinates and currents are exactly

\[
x'_0=-\frac{125}{163},\quad
x'_7=\frac{179}{163},\quad x'_8=-\frac{179}{163},
\quad
\mathcal J_{0,7}=\mathcal J_{0,8}=\frac{5472}{26569}>0.
\tag{8}
\]

Original norm remains 9. Equal-share owned-cell stocks both remain \(9/2\): each cell's core gain is balanced by half of the shared-face loss. Both incidence contacts are admitted equally; this does not evade the earlier impossibility of a singleton primitive contact at this symmetric state.

Now replace the score in (2) by the equally source-readable *mean* inward flow \(\widetilde s_f=s_f/k_f\), using the same competition and normalization structure. All seven scores at this state equal 2, so every margin vanishes and the state is fixed. Both policies are local, equivariant, norm-conservative and tie-continuous; both use only native support coordinates and geometric multiplicities, yet they predict different events. Consequently these structural requirements and the current source ledger do **not** select the aggregate law uniquely.

## 6. Selection source obligation and next experiment in mathematics

The aggregate policy is a concrete, bounded-locality candidate on the native real carrier, with no added carrier degrees of freedom. It supplies an autonomous next-snapshot weight from local data and an exact forward conservative event. The remaining native-source obligation is narrow and explicit: justify why aggregate rather than mean current should determine competition, why strict-margin/local-stock normalization is the correct response, and what selects the event normalization and renewal/reset semantics. Q153/Q156/Q173 do not already assert these choices.

The law need not maintain progress: exact competing ties can stall; no fairness, universal reopening, sustained throughput or cycle/reset theorem follows. It does not conserve the separate enlarged model's Hamiltonian and is not claimed to be a canonical Hamiltonian event. Original native support norm/ownership and physical energy remain distinct. Later steps should compare aggregate, mean and additional sourced eligibility predicates on held-out carrier preparations, with selection differences and stalls retained as falsifiers rather than hidden by label priority.

Fresh exact controls verify native face-star permission masks, midpoint and owned receipts, aggregate positivity, all twelve signed carrier automorphisms, local read/write sets, the symmetric aggregate/mean contrast, and tie/vacuum perturbations. Constructor verification is not independent peer review. No archived code is executed. Native constitutive uniqueness, physical action/time and quark/lepton identification remain OPEN. Physical promotion 0.
