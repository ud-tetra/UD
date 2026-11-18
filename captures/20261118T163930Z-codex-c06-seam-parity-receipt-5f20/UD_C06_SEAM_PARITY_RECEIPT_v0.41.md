# C06 parity and common-capture seam receipt audit v0.41

**EXACT / NO-GO** for enforcing purity with nonnegative diagonal masks or treating unrestricted staggered reads as one state. **EXACT / CONDITIONAL** for common-capture recovery and the skew bound. **CANDIDATE** for a parity-resolved capture-and-cut interface. **Physical Promotion = 0.**

## Gate scope and an incidence readout

Ledger v0.39 Q156 admits the hard product of closure and integrity; Q167 admits fixed binary masked signed incidence currents and Q173 a binary face gate. The native gate trigger and recovery audit v0.1, §§2–2.2, derives factor updates given their histories, with a separate historical veto typed to site load. None of those inspected rules supplies a projection from ordinary edge coordinates \(X=E\oplus W\) to pair-odd \(W=T_2\). A gate might be supplied with independently certified odd input. That certification is a different datum.

For a nonnegative diagonal edge mask \(D=\operatorname{diag}(d_e)\), test a pure even vector with pair values \(a_i\ne0\), \(\sum_i a_i=0\). The output can be odd only if every \(a_i(d_e+d_{\bar e})=0\), forcing all weights to vanish for this input, even for a payload-chosen mask. If the output is first projected to mean zero, the three products must instead share a common value. The \(a_i\) have both signs, so that common value is zero and all weights must still vanish. Fixed masks preserving the full odd space have equal weights within each opposite pair, and do not reject general even input except by vanishing. This scoped test excludes nontrivial stock-preserving purification by these masks, while permitting a gate to reject an input or act on already certified stock.

An exact algebraic alternative uses unsigned endpoint incidence \(A:\mathbb R^6\to\mathbb R^4\) from v0.36. It kills \(E\), because every vertex sees one edge per opposite pair. On \(X\), \(A^\mathsf TA=2P_-\), from the v0.36 incidence identities. Since \(Ax\) sums to zero, any three vertex sums \(p\) determine the fourth as \(-\mathbf1^\mathsf Tp\). The true odd squared norm is \((\|p\|^2+(\mathbf1^\mathsf Tp)^2)/2\), with the polarized form giving inner products. This is an exact rank-three observer on mixed inputs if the three star sums are available at a common capture. Each sum includes an edge beyond the face; it is neither a single-face raw read nor a dynamical projection or transfer.

## Common capture and timing bound

C06 v0.40 gives the five-edge recovery per register. The native crossing-to-receipt audit v0.1, §§1 and 4–7, supplies a conditional resolved-root ordinal and publication/retention protocol. It permits publication delays and out-of-order retained observations. Neither that protocol nor the synchronous routing stencil of C06 v0.21 supplies an atomic five-value amplitude capture. Capturing several values at one model instant and publishing them later preserves the snapshot; a state also needs an authoritative capture link to avoid delayed actuation, as in v0.33.

Suppose the three face samples are at \(t\), and the two opposite samples differ from their values at \(t\) by \(\delta_1,\delta_2\). Trace recovery imputes error \(-\delta_1-\delta_2\) on the missing opposite sample. If \(x\) is the true register and \(\hat x\) the reconstructed register, then
\[
\|P_-(\hat x-x(t))\|^2
=\tfrac12\left[\delta_1^2+\delta_2^2+(\delta_1+\delta_2)^2\right]
=\delta_1^2+\delta_2^2+\delta_1\delta_2.
\]
For independent certified bounds \(|\delta_i|\le D_i\), the sharp worst case is \(D_1^2+D_2^2+D_1D_2\), attained by errors of the same sign at the bounds. For rate bounds \(L_i\) on each transition interval, \(D_i=L_i|t_i-t|\) is admissible. This quantifies residual assurance at a reported zero without silently declaring exact zero. It assumes face times coincide and the model mean-zero trace is exact.

## Exact false completion despite a known stock total

A mixed, norm-preserving two-sector comparator shows why total stock alone cannot authenticate capture time. Encode donor and archive as the real and imaginary components. Let the common spatial profile on the three face representatives be \(w=(1,-1,0)\). At capture times \(t_0,t_1\) in the same forward odd lobe, set the normalized odd phases to \(o_0=(3+4i)/5,\ o_1=(5+12i)/13\). Take even coefficients \(e_0=(-32+9i)/65,\ e_1=-e_0\). These values admit separate scalar skew rotations: the odd angle advances between the two first-lobe values, while the even angle advances by \(\pi\) on the same interval. The comparator grants this even rate and preparation independently; they are not sourced native parameters.

Read the face at \(t_0\) and two opposite edges at \(t_1\), leaving the third to trace. The inferred odd coefficient is \((o_0+o_1+e_0-e_1)/2=i\). Thus the false snapshot has zero donor, full archive, exactly the known odd stock, and passes the inferred downward correlation guard. The actual odd donor fractions are \(9/25\) and \(25/169\) at the two capture times. The timing obstruction therefore applies even to a stock-checked receipt. By contrast, the v0.40 \(2/5\) residual is a single mixed spatial witness, not an upper bound. Under its true downward, archive-dominant condition, the hidden residual can approach \(1/2\) from below by scaling a hidden zero-sum donor against its orthogonal archive.

## Time transport can become singular

For one oriented opposite pair, suppose exact scalar sector transport factors \(h_o,h_e\) over the capture interval are supplied. If the early face and late opposite observations are \(a=o+e\) and \(b=-h_o o+h_e e\), then \(o=(h_e a-b)/(h_o+h_e)\) when the denominator is nonzero. Two distinct pairs then recover their odd and even parts; the even trace gives the third even value and its early face value finishes the odd recovery. At \(h_e=-h_o\), the late value is \(-h_o a\) and supplies no new information. Even exact rates and known timestamps can fail at that relative phase.

For an exact collision on \(w=(1,-1,0)\), let \(h_o=(4+3i)/5,\ h_e=-h_o\). Compare early sector coefficients \((o,e)=(i,1/3)\) and \(((3+4i)/5,(-4+3i)/15)\). Each history has odd norm squared one, even norm squared \(1/9\) and the same early face coefficient \(a=(1+3i)/3\). The late opposite coefficient is the same in both histories. At the early time, one donor is empty and the other retains \(9/25\). At the late time the roles reverse. Thus the observations, exact transport factors and both stock totals still do not identify a common zero-donor state.

## Candidate and remaining source question

An interface can bind both registers to one resolved capture state in a common frame, certify odd stock via simultaneous five-edge readings or the three vertex sums per register, and test positive stock, alignment and the first directed guard. A declared atomic cut then preserves the archive and original half-stock readout, while later publication records the event. Independently sourced exact time transport of staggered samples could replace common capture. The audited protocols supply neither the required capture/transport nor a rule authorizing and committing the cut. This candidate therefore remains an internal interface, with native authority and physical promotion open.

The adjacent replay checks all 64 masks against a generic even witness, all faces over a bounded mixed grid for star recovery, exact phase- and stock-preserving timestamp aliasing, and the sharp stale-sample bound.
