# THM-534: local robust contact strength and the native-selection source gate

Development — no registry entry. Exact conditional derivation for a new soft contact-strength candidate. This is not a derived native hard-admission or exclusive event-selection rule. Constructor checked; independent non-constructor review pending. Physical promotion 0.

## 1. Result and source boundary

For a potential face–cell incidence with signed coefficient \(d=\pm1\), write its two unique carrier amplitudes as \(f,t\), using the retained unit support metric. A local coefficient candidate is

\[
\boxed{m(f,t)=\frac{f^4+t^4}{(f^2+t^2)^2}},\qquad (f,t)\ne(0,0).
\tag{1}
\]

It uses only the two incident amplitudes, does not compare neighboring faces, does not form tie components, and has no fitted coefficient or tolerance. Its induced state maps are robust even near the vacuum, although the raw coefficient itself has no continuous vacuum extension. A conventional value \(m(0,0)=1\) is harmless because the zero state cannot move under the resulting map.

The source distinction is essential:

| Layer | What is available | Status here |
|---|---|---|
| Variables and receipts | Q169–Q173 unique carrier, squared support and signed incidence currents; Q177–Q179 ownership | Source-bound mathematical inputs |
| Soft strength | Real coefficient \(m\in[1/2,1]\) on a potential incidence | New conditional constitutive candidate |
| Hard permission | Whether the incidence may be used | OPEN; not selected by (1) |
| Exclusive event and clock | Which overlapping contact executes, and when | OPEN; not supplied by (1) |
| Physical action and identification | Action unit, physical time, quark/lepton correspondence | OPEN |

The attached ledger's Q156 explicitly leaves smooth conductance open. Its Q173 is a hard face-gate lane, not a declaration of equation (1). This capture extends a coefficient family without changing the frozen particle operators or metric. Equality of two internal ratios does not establish common provenance. In particular \(m(1,1)=1/2\) is not the shared-face ownership weight, a Born probability or an action coefficient.

The consulted reconstructed packet-modulation, transport, coherence, action, field and carrier files are placeholders, as recorded in SOURCE_DEPENDENCY_SCAN.json. The existing positive-stock/controller document also labels its constitutive and timing quantities as supplied designs. No native microscopic allocation principle is recovered from those materials. This is a scoped source finding, not a claim that no such source can exist elsewhere.

## 2. Why a globally continuous binary selector cannot do the job

**Theorem R1.** On a connected domain of local amplitude states, a deterministic, memoryless, continuous map into \(\{0,1\}\) is constant.

**Proof.** A continuous image of a connected set is connected. The only connected subsets of \(\{0,1\}\) are singletons. \(\square\)

The nonzero plane \(\mathbb R^2\setminus\{0\}\) is connected, so merely removing the vacuum does not avoid the result. A nontrivial hard switch may instead be robust on a margin-restricted domain, use discrete memory/hysteresis, or have a switching discontinuity. These are different premises, not contradictions of R1. Finite-noise physical robustness also needs a stated uncertainty model. At symmetric states, the earlier stabilizer obstruction independently prevents selecting an individual conflict edge equivariantly without additional distinguishing information.

Equation (1) therefore targets **soft strength**, not a globally robust nontrivial binary gate. It must not be reported as solving native admission by changing the meaning of selection.

## 3. Conditional derivation and the exact new assumption

Define the local stock shares

\[
N=f^2+t^2,\qquad p=\frac{f^2}{N},\quad q=\frac{t^2}{N},\quad p+q=1.
\]

These shares are dimensionless internal coordinates under the retained metric. For a shared face, the same unique face amplitude is used in each incident contact calculation; the local denominators are not summed into a duplicated global support stock.

**New allocation postulate A (not recovered in source).** A soft normalized response is a quadratic sum of the separate stock shares, invariant under exchanging the two roles, without a cross-share response term; a single occupied share has unit response.

**Theorem R2.** Postulate A uniquely gives equation (1) within that declared response class.

**Proof.** A separate quadratic response has the form \(A p^2+Cq^2\). Exchange symmetry requires \(A=C\); the endpoint normalization \(m(1,0)=m(0,1)=1\) requires \(A=C=1\). Thus \(m=p^2+q^2\), which is (1). \(\square\)

Exchange of a face with a cell is an additional constitutive symmetry in this postulate, not a simplicial carrier automorphism. Neither the quadratic response class nor absence of a cross term follows from support conservation.

Without the no-cross assumption, the family

\[
m_\beta=p^2+q^2+\beta pq,\qquad0\le\beta\le2
\]

has the same endpoint normalization and exchange symmetry, remains between \(1/2\) and 1, and supplies conservative support-receipt-compatible soft maps. At \(\beta=0\) it gives (1); at \(\beta=2\) it gives the all-open unit coefficient. Both endpoints are parameter-free rules. Thus even forbidding fitted parameters does not establish native uniqueness. The displayed family describes nonidentifiability; no value of \(\beta\) is promoted as a UD constant.

A face-only linear share \(m=p\) would be unique under a different affine-allocation postulate. It fails a useful recovery control: at \(f=0,t\ne0\), it closes the interaction and prevents face replenishment. That negative result motivates testing (1) but does not prove that nature selects it.

## 4. Local nonlinear field and rigorous robustness

For an independently permitted contact define

\[
F_d(f,t)=d\,m(f,t)(-t,f),\qquad F_d(0,0)=0.
\tag{2}
\]

**Theorem R3.** This field preserves \(f^2+t^2\), is covariant under signed incidence-basis changes, and is globally 2-Lipschitz in Euclidean amplitude norm.

**Proof.** The inner product of \((f,t)\) with \((-t,f)\) is zero, so the norm derivative vanishes. Squaring removes amplitude-basis signs in \(m\); transforming \(d\) with the corresponding incidence signs transports (2). Also \(1/2\le m\le1\), so \(\|F_d(x)\|\le\|x\|\) and the zero extension is continuous.

For \(N>0\), put \(a=(f^2-t^2)/N\). Direct differentiation gives

\[
m=\frac{1+a^2}{2},\qquad
N\|\nabla m\|^2=4a^2(1-a^2)\le1,
\]

with the exact certificate

\[
1-N\|\nabla m\|^2=(2a^2-1)^2\ge0.
\]

Writing \(J_d(f,t)=d(-t,f)\),

\[
DF_d=mJ_d+(J_dx)(\nabla m)^{\mathsf T},\qquad
\|DF_d\|\le m+\|x\|\|\nabla m\|\le2.
\]

Integrate this derivative bound along the line segment between two nonzero points. If the segment passes through zero, split it there and use continuity. The same global Lipschitz bound follows. \(\square\)

This is robustness of the **state dynamics**, not continuity of the raw coefficient at the vacuum: \(m(\delta,0)=1\), whereas \(m(\delta,\delta)=1/2\), even as \(\delta\to0\). Any claim requiring the coefficient itself to be globally continuous still fails.

For a fixed potential-contact graph of maximum incidence degree \(\Delta\), a sum of these independently permitted contact fields is at most \(2\Delta\)-Lipschitz. Indeed, Cauchy–Schwarz at each coordinate and then the pair bound give

\[
\|F(x)-F(y)\|^2
\le\Delta\sum_e\|F_e(x_e)-F_e(y_e)\|^2
\le4\Delta^2\|x-y\|^2.
\]

The face/core graph of \(K_-\) has \(\Delta=4\), yielding bound 8. Global norm conservation follows by summing pairwise cancellation. This defines a well-posed local nonlinear differential model with fixed permissions. Its parameter is mathematical evolution, not physical time or a discrete UD event count. Local dependence of a differential field alone is not a finite-speed spacetime propagation theorem.

## 5. A strictly two-coordinate finite primitive

For one contact, compute \(h=a_e m(f,t)\) from its pre-event state, with independently supplied fixed permission \(a_e\in\{0,1\}\). Let

\[
b=\frac{\varepsilon h}{2},\qquad
c=\frac{1-b^2}{1+b^2},\quad s=\frac{2b}{1+b^2},
\]

and apply

\[
\boxed{\Phi_{d,\varepsilon}(f,t)=(cf-dst,\;dsf+ct).}
\tag{3}
\]

This is a new local frozen-coefficient Cayley primitive, using exactly two amplitude coordinates. It is not a global inverse, a joint tie-block event or the exact finite-time flow of the nonlinear field (2). Its derivative at \(\varepsilon=0\) agrees with (2). The declared control step remains \(\varepsilon=1/4\); it is not selected as a native action unit.

**Theorem R4.** Equation (3) preserves the pair norm and obeys completed midpoint receipts. With permission held fixed, it is globally bi-Lipschitz for \(|\varepsilon|<1\), with

\[
(1-|\varepsilon|)\|x-y\|
\le\|\Phi(x)-\Phi(y)\|
\le(1+|\varepsilon|)\|x-y\|.
\tag{4}
\]

In particular the bounds are \(3/4\) and \(5/4\) at the control step.

**Proof.** The matrix in (3) is a rotation since \(c^2+s^2=1\). Its Cayley midpoint equation gives

\[
I=2\varepsilon d h\bar f\bar t,\qquad
(f')^2-f^2=-I,\quad (t')^2-t^2=I.
\]

The existing equal-share owned-support receipt follows by inserting these two changes in the unique carrier; no face coordinate is duplicated. Put \(\alpha(x)=2\arctan(\varepsilon a_em(x)/2)\). The derivative of (3) is its orthogonal rotation plus a rank-one term of norm

\[
\|x\|\|\nabla\alpha\|
=\frac{|\varepsilon|a_e\|x\|\|\nabla m\|}
       {1+(\varepsilon a_em/2)^2}\le|\varepsilon|.
\]

Hence its derivative norm is at most \(1+|\varepsilon|\), and its smallest singular value is at least \(1-|\varepsilon|\). Global upper bounds follow by segment integration and continuity at zero. To justify the global lower bound, use polar coordinates: (3) preserves radius and maps angle \(\theta\) to \(\theta+d\alpha(\theta)\). Its derivative is positive and at least \(1-|\varepsilon|\), and it has degree one on the circle. Thus it is a global homeomorphism, with inverse derivative norm at most \((1-|\varepsilon|)^{-1}\). Apply the same segment argument to the inverse. \(\square\)

The primitive is also equivariant under signed carrier relabeling and homogeneous under a common nonzero amplitude rescaling. Disjoint contact primitives commute. Overlapping primitives generally do not: the verifier gives an exact counterexample. Therefore (3) does not silently supply a native scheduler or fairness theorem. If hard permissions themselves switch discontinuously as a function of state, bound (4) does not certify that additional switching law.

## 6. Seed, replenishment, and remaining failures

With an independently permitted \(d=1\) contact and the control step,

\[
\Phi(1,0)=\left(\frac{63}{65},\frac{16}{65}\right),\qquad
\Phi(0,1)=\left(-\frac{16}{65},\frac{63}{65}\right).
\]

Thus a nonempty face can seed an empty core, and a nonempty core can replenish an empty face. The signed current is determined by the completed event; instantaneous \(ft=0\) does not imply a zero completed transfer. This is a conditional two-coordinate mechanism, not proof that a previously forbidden contact may open.

Two response laws remain distinguishable at a balanced input:

\[
\Phi_{m}(1,1)=\left(\frac{223}{257},\frac{287}{257}\right),\qquad
\Phi_{\mathrm{unit}}(1,1)=\left(\frac{47}{65},\frac{79}{65}\right).
\]

Both are local, norm-preserving and robust. For a supplied sequence of contact attempts, repeated perturbation bounds can accumulate; equation (4) is not a contraction or an infinite-horizon error certificate.

These are exact prospective model discriminators, not physical observations or target matches. They show why the allocation postulate needs independent source justification.

All-off permissions still give identity maps. The symmetric nonzero state \(z_{013}=z_{023}=1\), other face/core amplitudes zero, remains stationary under the all-permitted **sum field** (2), because the two core-source terms cancel. The separate finite contact maps need not preserve that state, but choosing an order for overlapping contacts is additional information. No universal recovery, spontaneous symmetry breaking, source renewal or hard-gate bootstrap is inferred.

## 7. Verification and native-source gate

The fresh Fraction verifier passes 324 primitive sign/permission controls, 80 exact gradient certificates, 26,244 pairwise perturbation-bound controls, 7,776 signed carrier covariance controls, 256 supplied-permission-mask paths, and 15 disjoint-contact commutation controls. It separately checks seed/replenishment, the face-only failure, raw vacuum-coefficient discontinuity, source nonuniqueness, overlapping order dependence and the nonzero stationary field. Fixed-order mask paths are controls with supplied order, not a derived schedule. Only newly authored code is executed.

The genuine progress is a concrete bounded-footprint state map with a proved global perturbation certificate and explicit local support receipts. It avoids the unbounded tie-component footprint and finite state-update jump of v1.7. It achieves this by changing to a soft coefficient, not by proving a native hard selector.

To call this **native UD selection**, independently recover or derive a packet-level response functional that forces the response class and no-cross allocation in postulate A; derive actual hard admission and a compatible event mechanism; then audit the joint dynamics and physical action map. Until those gates close, the correct conclusion is **local robust conditional contact-strength candidate; native selection OPEN**. The original sources' underdetermination cannot be repaired by relabeling this new assumption as a theorem.
