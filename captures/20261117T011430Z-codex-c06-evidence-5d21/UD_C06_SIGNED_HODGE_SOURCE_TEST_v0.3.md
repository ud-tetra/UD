# UD C06 signed Hodge source test v0.3

**Status** · EXACT for the declared preparation and edge support readout. NO-GO for positive isotropy via linear equivariant preparation into the ordinary signed chain carrier. Physical Promotion = 0.

**Provenance** · [Paper I v1.1.1, §§4.1–4.3 and Appendix A](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-03-UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) supplies the oriented generator. [Paper III v1.1.1, §2, Theorem 1 and Proposition 3](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-00-UD_PAPER_III_REVIEW_DRAFT_v1.1.1.md) supplies the representations. [Coefficient Ledger v0.85 filename, C05–C06](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/ledger-recovery-v0.1/library_LEDGER_v0.85.json) supplies the physical source gate. Prior incidence interaction v0.2 supplies the definition of the contrast $m-g-h$.

## Source-defined interaction with declared preparation

Use the closed, dimensionless, unit-metric skew Hodge–Dirac evolution $\dot c=(B^T-B)c$ on the 15 oriented chains of one filled tetrahedron. There are no external drives. Its conserved quantity is $\|c\|^2$. For the response input $Q\in W=\operatorname{Sym}^2_0(V)=E\oplus T_2$ use the Frobenius metric and the regular vertex directions $n_i=(\pm1,\pm1,\pm1)/\sqrt3$ with product of signs $+1$. Fix $c(0)=(PQ,0,0,0)$ by $(PQ)_i=n_i^TQn_i$. Read the squared norm of the actual oriented edge amplitudes, $Y_s(Q)=\|c_1(s)\|^2$. The preparation and readout are chosen for this test. Only the signed generator comes from the cited Paper I.

The diagonal sector gives zero at every vertex because $n_{ij}^2=1/3$ and $\operatorname{tr}Q=0$. The off-diagonal sector has $\|PQ\|^2=(8/9)\|Q_{T_2}\|_F^2$, since the three off-diagonal sign columns on the four vertices are orthogonal with squared length four. The vertex sum is zero. The source identities $B_1B_1^T=4I-\mathbf1\mathbf1^T$ and $B_1B_2=0$ close the evolution on the mean-zero vertices and the image of $B_1^T$. In particular
```math
c_1(s)=\tfrac12\sin(2s) B_1^TPQ,
\qquad Y_s(Q)=\tfrac89\sin^2(2s)\|Q_{T_2}\|_F^2.
```
Thus $w_E-w_{T_2}=-(8/9)\sin^2(2s)$, and for the short-time coefficient $\lim_{s\to0} Y_s/s^2$ the exact contrast is $-32/9$. This equals the quantity called $m-g-h$ in the prior incidence model when used as an effective sector contrast. Separate flag gains $m,g,h$ have no specified channel identification in the signed chain test. At $s\in(\pi/2)\mathbb Z$ the entire response vanishes, leaving no trace-normalization. Away from those times the trace-normalized spectrum has two zero weights and three weights of $1/3$.

## Scope of the obstruction

Paper III's signed chain representation contains no $E$. Any linear $S_4$-equivariant preparation $W\to\mathcal C$ therefore annihilates $E$, by inequivalence of irreducible representations. Any subsequent deterministic evolution and readout of the resulting chain state has the same output for $Q$ and $Q+Q_E$. In particular, even a different equivariant linear chain preparation cannot produce positive equal response on all five directions through this interface. This argument applies to direct sums of ordinary signed-chain copies, for their diagonal relabeling action, as well.

A differentiable equivariant preparation at the zero probe has the same rank obstruction in its derivative. For a readout defined as the squared norm of an amplitude whose baseline is zero, the leading quadratic response uses that derivative alone. The statement leaves finite nonlinear responses and bilinear chain observables open. No inference about measured coupling follows.

## Exact replay

The independent calculation generates all signed boundary entries by alternating deletion, verifies the multiplicity of $E$ by a 24-permutation character average, and checks both Gram matrices and closure of the evolution. It uses Python 3 and the standard library.

```python
from fractions import Fraction
from itertools import combinations, permutations, product

from math import prod

simplices = [s for k in range(1, 5) for s in combinations(range(4), k)]
index = {s: i for i, s in enumerate(simplices)}
a = [[0]*15 for _ in simplices]
for column, simplex in enumerate(simplices):
    if len(simplex) == 1:
        continue
    for j in range(len(simplex)):
        row = index[simplex[:j] + simplex[j+1:]]
        a[column][row], a[row][column] = (-1)**j, -(-1)**j

def act(matrix, vector):
    return [sum(x*y for x, y in zip(row, vector)) for row in matrix]

def dot(x, y):
    return sum(a*b for a, b in zip(x, y))

def permute(p, s):
    return tuple(sorted(p[v] for v in s))

matchings = [
    frozenset(((0,i), tuple(j for j in range(1,4) if j != i))) for i in range(1,4)
]
inner = 0
for p in permutations(range(4)):
    matching_trace = sum(frozenset(permute(p, e) for e in m) == m for m in matchings)
    chain_trace = 0
    for s in simplices:
        if permute(p, s) == s:
            inversions = sum(p[x] > p[y] for x, y in combinations(s, 2))
            chain_trace += (-1)**inversions
    inner += (matching_trace - 1)*chain_trace
assert Fraction(inner, 24) == 0

vertices = [v for v in product((-1,1), repeat=3) if prod(v) == 1]
basis = [
    ((1,0,0),(0,-1,0),(0,0,0)), ((1,0,0),(0,1,0),(0,0,-2)),
    ((0,1,0),(1,0,0),(0,0,0)), ((0,0,1),(0,0,0),(1,0,0)),
    ((0,0,0),(0,0,1),(0,1,0)),
]
preps = [[Fraction(dot(v, act(q, v)), 3) for v in vertices] + [0]*11 for q in basis]
slopes = [act(a, q) for q in preps]
assert all(sum(q[:4]) == 0 for q in preps)
assert all(q[:4] + q[10:] == [0]*9 for q in slopes)
assert all(act(a, slope) == [-4*x for x in q] for q, slope in zip(preps, slopes))
for i,j in product(range(5), repeat=2):
    norm = sum(x*x for row in basis[i] for x in row) if i == j and i >= 2 else 0
    assert dot(preps[i], preps[j]) == Fraction(8,9)*norm
    assert dot(slopes[i], slopes[j]) == Fraction(32,9)*norm
print("PASS · 24-permutation character check and 25 exact Gram entries for preparation and edge slope")
```

Observed result: PASS · 24-permutation character check and 25 exact Gram entries for preparation and edge slope.
