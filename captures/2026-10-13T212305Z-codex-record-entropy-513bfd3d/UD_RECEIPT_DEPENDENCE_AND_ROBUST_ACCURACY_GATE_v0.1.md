# Receipt dependence and a robust accuracy gate

2026-10-13. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Result

The previous independent-receipt majority formula is replaced by sharp bounds using joint error probabilities. Full three-way independence is not necessary for the declared one-percent final-error guarantee. A sufficiently small pair joint-error sum suffices, even when decision faults depend on one another and on receipt errors.

The bounds identify source quantities that UD must independently derive; they do not establish those quantities. Native action normalization and recording-source provenance remain open under G05/G06. G was unused. The prior physical gates, thermal kernel, ideal reverse cleanup and ideal downstream fanout retain their declared scope.

## 1. Exact majority identity

Let E_i indicate that receipt i disagrees with the original binary carrier label. Do not assume that the three errors are independent. Define

\[
p=\frac13\sum_iP(E_i=1),\qquad
a=\frac13\sum_{i<j}P(E_i=E_j=1),\qquad
b=P(E_1=E_2=E_3=1).
\]

These are mean marginal, mean pair joint, and triple joint error probabilities. The identity

\[
\mathbf1_{E_1+E_2+E_3\ge2}
=E_1E_2+E_1E_3+E_2E_3-2E_1E_2E_3
\]

holds on all eight binary patterns. Therefore majority error is exactly

\[
\boxed{m=3a-2b.}
\]

No permutation symmetry is required. Quantities may be averaged over the fair source label; conditional source-specific statistics can instead be treated separately.

## 2. Sharp joint-moment bounds

Let Q_k=P(sum_i E_i=k). The moments give

\[
Q_0=1-3p+3a-b,\quad Q_1=3p-6a+3b,
\quad Q_2=3a-3b,\quad Q_3=b.
\]

Nonnegativity is equivalent to

\[
b_{\min}=\max(0,2a-p)\le b\le
b_{\max}=\min(a,1-3p+3a).
\]

Thus, for feasible moments,

\[
\boxed{3a-2b_{\max}\le m\le3a-2b_{\min}.}
\]

The bounds are sharp. Choose b at either endpoint, construct the nonnegative Q_k, and distribute Q_k uniformly among the binomial(3,k) patterns of weight k. This gives an explicit law attaining each bound. The checker verifies normalization, moments and majority error of those witnesses using fractions.

With only marginal mean p=1/100, majority error can be anywhere from zero to 3/200. The worst case puts mass 3p/2 on exactly-two-error patterns. Therefore a quoted one-percent receipt error alone does not certify a majority advantage; the resulting majority can be worse than a single receipt.

| p | Mean pair joint a | Sharp majority-error interval |
|---|---|---|
| 1/100 | 1/10000 | [1/10000, 3/10000] |
| 1/100 | 1/1000 | [1/1000, 3/1000] |
| 1/100 | 1/100 | {1/100} |

For pairwise independent equal-marginal receipts, a=p². Triple independence need not hold, and m need not equal 3p²−2p³. Nonetheless the worst-case m<=3p² is small enough for the current criterion.

## 3. Decision faults without an independence assumption

Let L denote the parity of the three forward majority-target faults and the seed-copy fault. Suppose each of those four event probabilities is bounded by q. By the union bound,

\[
P(L=1)\le4q.
\]

This remains valid for correlated decision events. The final seed is wrong when receipt-majority error and L disagree. Consequently

\[
p_{\rm seed}\le m+P(L=1)\le3a-2b_{\min}+4q\le3a+4q.
\]

No independence between acquisition and decision errors is required for these upper bounds. They are sufficient guarantees, not exact formulas for every joint law. The previous parity formula [1−(1−2q)^4]/2 remains exact only under its independent decision-fault model.

Storage is still assumed to use fresh independent bath states and to depend only on the written seed. If its ideal-seed error is e0 and the average seed error is s, the final equal-prior error is e0+(1−2e0)s while s<=1/2. The formula also allows unequal errors conditional on R=0 and R=1: s is their average. It follows by subtracting the two binary-mixture memory distributions.

For the current 32-update ground storage and target epsilon=1/100, define

\[
s_*=\frac{\epsilon-e_0}{1-2e_0}.
\]

The replay's exact rational e0 gives s* approximately 0.000775497742. A robust sufficient source gate is

\[
\boxed{3a+4q\le s_*.}
\]

A tighter version uses 3a−2b_min+4q if p is also available. These gates retain ideal reverse cleanup and ideal fanout; faults outside the four stated decision events need their own terms.

## 4. Conditional guarantee at the current test point

For p=1/100, a=p²=1/10000 and q=1/10000,

\[
p_{\rm seed}\le\frac7{10000},
\quad e_{\rm final}\le e_0+(1-2e_0)\frac7{10000}
\approx0.009925897279<\frac1{100}.
\]

The final inequality is checked exactly using fractions. Thus pairwise independent receipt errors, together with four bounded decision-event marginals, suffice for the accuracy target. Neither three-way receipt independence nor decision-event independence is needed for this guarantee.

With q fixed at 1/10000, the looser sufficient pair-joint ceiling is

\[
a\le\frac{s_*-4q}{3}
\approx0.000125165914.
\]

If all receipt marginals equal p=1/100, define the average pair correlation coefficient by

\[
\bar\rho=\frac{a-p^2}{p(1-p)}.
\]

The ceiling corresponds to bar rho approximately 0.00254201153. This is an average bound, not an individual bound on every pair. Unequal marginals require their actual pair probabilities rather than this equal-marginal correlation conversion.

The bounds are requirements for a declared source model, not measured or native UD correlation values. A small change in shared error can consume the prior margin, so repeating acquisition without a joint-state source law remains insufficient.

## 5. Entropy/resource correction

The receipt workspace contains the joint error flags after carrier uncopies. Under correlated errors its entropy is H(E1,E2,E3), not automatically 3h(p). The general inequality is

\[
H(E_1,E_2,E_3)\le\sum_i h(p_i).
\]

Equality requires error independence. Similarly the output parity garbage can correlate with the receipt flags, so the previous additive 3h(p)+h(u3) expression remains scoped to its independent fault channels. A correlated source can have smaller garbage entropy while producing larger majority error. Reset cost and source fidelity must therefore be derived from different functionals of the same joint state.

The earlier majority release is preserved as an independent-model result. This report adds the correlated-model scope; it does not overwrite its exact conditional formulas or change any registry status.

## 6. What a native source derivation must supply

A source-complete apparatus model must define the receipt-error flags and their pre-decision joint state. If F_i are commuting error projectors on distinct flag registers with state rho_F, then

\[
p_i=\operatorname{Tr}(\rho_F F_i),\quad
a_{ij}=\operatorname{Tr}(\rho_F F_iF_j),\quad
b=\operatorname{Tr}(\rho_F F_1F_2F_3).
\]

The inequality gate can be tested directly on those source-derived quantities. Declaring product flag states and factorized conditional interactions can establish independence within a candidate apparatus, but it does not derive product preparation from native incidence motion. Shared control, carrier drift, bath reuse and coupling errors must be included in the actual joint-state evolution if present.

The supplied source copies and coefficient ledger do not provide this current apparatus joint-state law. The next source task is therefore precise: derive or bound the pair joint-error sum and the four decision-event probabilities using an energetically specified flag environment. The thermodynamic record-to-horizon bridge remains open even if the accuracy gate passes.

Disposition: exact conditional joint-probability theorem and robust accuracy gate checked. Native moments, clock, fault energy, full reset and apparatus area OPEN. Physical promotion 0; independent review OPEN. Development — no registry entry. No ledger, registry, site or repository changes. Gap2_FINAL_Finite_Genesis.png remained unavailable and unused.
