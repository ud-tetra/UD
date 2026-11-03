# Metric-source admission — supplemental scope review v0.1

Date: 2026-10-14. Lane: development — no registry entry. Constructor-team AI source/scope review. Independent human review: pending. Physical promotion: 0.

## 1. Source-defined Gram Rules A/B: full ten-gate clock obstruction

Source C0173, *Geometric inner-product interface*, §4, states the positive squared-frequency factors of its fixed stretched-tetrahedron metric candidates as

\[
u=4/a,\quad v=2+2/a,\quad
x=4a/b,\quad y=2(a+1)/b,\quad z=4b/c,
\]

with full skew characteristic polynomial

\[
\lambda(\lambda^2+u)(\lambda^2+v)^2
(\lambda^2+x)(\lambda^2+y)^2(\lambda^2+z).
\]

Here a=((1+q)/2)^p, b=((2q+1)/3)^p, c=q^p, q=r²>0, and p=1 or 2 names the source's two distinct candidate rules. The parameter a is a **metric entry**, not the coefficient of a skew-channel matrix in C0190. Source semantics must distinguish those identically spelled parameters.

The source formulas imply the exact algebraic constraint

\[
\frac{u}{v}=\frac{2}{a+1},\qquad
\frac{x}{y}=\frac{2a}{a+1},\qquad
\boxed{\frac{u}{v}+\frac{x}{y}=2}.
\]

This relation requires only a,b>0 and does not depend on selecting q or p. A common rate adjustment multiplies all squared frequencies by the same positive scalar and leaves the relation unchanged.

For the full n=10 programme, the five distinct positive squared targets are proportional to {1,4,9,16,25}. Exact admission in uncoupled identical copies of the same fixed q and same Rule A/B requires every target to appear in the native spectrum. There are at most five distinct positive native factors. Therefore a degenerate native spectrum already fails the target count. In the remaining case, all five distinct native factors must be assigned bijectively to the five targets, up to the common scalar. In particular, u,v,x,y must be assigned four distinct elements of that set.

There are 5·4·3·2=120 ordered assignments. Exact rational enumeration finds none satisfying u/v+x/y=2. A complete finite certificate is:

```python
from fractions import Fraction
from itertools import permutations

targets = (1, 4, 9, 16, 25)
assignments = list(permutations(targets, 4))
assert len(assignments) == 120
hits = [row for row in assignments
        if Fraction(row[0], row[1]) + Fraction(row[2], row[3]) == 2]
assert hits == []
```

Equivalently, the equality is the integer equation uy+xv=2vy on this finite set. This is an exhaustive mathematical elimination of a necessary condition, rather than a parameter fit, source selection or empirical test. It proves a **scoped NO-GO** for exact full n=10 generator admission using either source Gram rule, fixed q, identical uncoupled copies and a common rate adjustment. No target-fitted q is adopted. For even n≥12 the clock has at least six positive frequencies and the same five-band class fails the simpler count. This particular elimination does not settle n=8, where one of the five native bands could remain unused.

The smallest nonzero relation gap in the enumeration is 1/144, occurring for (u,v,x,y)=(4,9,25,16) and its swapped-pair counterpart. This rational diagnostic is **not** an operator residual bound, an endpoint-error bound or a physical observable. The no-go needs only the absence of exact equality.

The source itself describes Rules A/B as candidates, not selected native dynamics. Their S4-breaking stretched geometry remains outside the three-band equivariant no-go, while this additional source-family relation supplies a different obstruction. The proof does not extend to arbitrary nonuniform metrics, time-varying q, heterogeneous q/rule copies, coupled copies or endpoint-only admission.

## 2. Weighted Pachner families: irrational paired-rate obstruction

Source C0473 §8 supplies the positive block-control characteristic polynomials. Using degree coefficients a,b,c>0, the K-minus family has positive frequencies

\[
\{\sqrt3a,\sqrt5a;\ \sqrt3b,\sqrt5b;\ \sqrt3c,\sqrt5c\},
\]

with source multiplicities (1,3), (2,3), (1,1) for the three degree groups. The K-plus family has

\[
\{\sqrt5a;\ \sqrt2b,\sqrt5b;\ \sqrt2c,\sqrt5c\},
\]

with source multiplicities 4, (1,5), (1,2). Multiplicities are distinct from the number of distinct positive frequency values.

All positive clock frequencies for even padded n are 2κj, j=1,…,n/2, so any ratio of two of them is rational. In a fixed K-minus degree pair, both frequencies cannot match clock targets: that would require √(5/3) to equal a ratio of positive integers. In a fixed K-plus paired degree group, the same contradiction uses √(5/2). Squaring and reducing fractions proves both ratios irrational, independent of the values a,b,c or common rate. The singleton K-plus degree-one group supplies at most one target as well.

Consequently each of the three degree groups matches at most one distinct target-grid frequency. Across the whole native operator at most three target-grid frequencies can occur, even though its spectrum can contain six (K-minus) or five (K-plus) distinct positive bands. Identical uncoupled copies increase only multiplicities. Thus exact full-generator intertwining is impossible for every even padded n≥8 in these weighted families under the same fixed-coefficient/common-rate contract. Coincidences between groups decrease rather than increase the number of distinct matches.

This is a source-family **scoped NO-GO**, not a claim that weighting never helps. Heterogeneous coefficients across copies or coupling between copies can add frequencies and require another operator analysis. The result does not settle approximate admission or complete endpoint matching. It does not replace the source's requirement to select metric, coupling, encoding and physical rate without backsolving a desired spectrum.

## 3. Metric convention and evidence boundary

C0473 calls its coefficients positive block controls and explicitly freezes treating them as free promoted UD constants. Its inverse-product metric formula is valid under G ċ=A0c followed by whitening, as explained in source C0496§9. A fixed-boundary weighted-adjoint construction instead gives √(g(k−1)/gk). Either convention yields the respective block-frequency pairs once a,b,c are defined consistently; this supplement does not identify the conventions.

The proofs above concern full generator spectra and exact isometric intertwining in consistently normalized coordinates, with the energy origin fixed. They supply no endpoint-error lower bound, protected output/export mechanism, clock-to-seconds map or physical promotion. The enumeration was run with standard-library exact fractions by this constructor-team AI thread and returned 120 assignments, zero solutions. Independent human review remains pending.

Source text fields and hashes are recorded in `s4-metric-source-review.md`: C0173 SHA-256 a1e338c059bdb0aa426ba97a5e2d4436c6ca931eefa0f4d2ad1d9e49c0699d4f; C0473 SHA-256 d979a0e5d77e78eee5ea996045e9cc9acaf02ecb0c03ddc24c01533e0db7140a; C0496 SHA-256 05200f695017e1e4a381af0eac824df7410c6b570e856b94fe0c92b12e4567ac. These identify imported UTF-8 source content, not original PDF bytes.
