# UD C06 tetrahedral response source v0.1

**Status** · EXACT for the declared finite orbit calculations. NO-GO for forcing equal weight by tetrahedral symmetry alone. CANDIDATE (agile) for the edge/axis source. OPEN for native selection and physical interpretation. Physical Promotion = 0.

**Dependencies** · [Paper III v1.1.1, Proposition 3 and No-go 4](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-00-UD_PAPER_III_REVIEW_DRAFT_v1.1.1.md). [Recovered coefficient ledger, v0.85 filename, rows C01, C05 and C06](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/ledger-recovery-v0.1/library_LEDGER_v0.85.json). The ledger locks the structural ratio and freezes its current q-pairing Hamiltonian interpretation. Its internal scientific revision field reads v0.43. The corresponding rows in the supplied v0.39 Markdown agree. This note leaves the frozen interpretation in place.

## Object and source

Use the Euclidean standard vertex representation $V$ of $S_4$. Take tetrahedral vertex directions $(\pm1,\pm1,\pm1)$ with product $+1$. Equal vertex lengths and equal mutual inner products realize the regular tetrahedron, and the four vertex permutations act orthogonally. The response space is $W=\operatorname{Sym}^2_0(V)$ with Frobenius inner product. In these coordinates $E$ is the trace-free diagonal subspace and $T_2$ is the symmetric off-diagonal subspace.

For a unit direction $n$ define $P_n=nn^\mathsf{T}-I/3$. For a finite set of unoriented lines $L$ define the uniform quadratic functional and its associated operator
```math
F_L(Q)=\frac1{|L|}\sum_{n\in L}(n^\mathsf{T}Qn)^2
=\langle Q,M_LQ\rangle,
\qquad M_L=\frac1{|L|}\sum_{n\in L} P_n\otimes P_n.
```
Here $F_L:W\to\mathbb R$ is nonnegative and $M_L:W\to W$. The brackets in $P_n\otimes P_n$ denote the rank-one map $Q\mapsto P_n\langle P_n,Q\rangle$. A relabeling permutes any full line orbit and leaves $F_L$ invariant. This static, metric-dependent quadratic probe is a declared model. Its construction supplies no source timing, dynamics, or physical units.

## Exact weights and the obstruction

Writing $Q=Q_E+Q_{T_2}$, every invariant real quadratic functional has the form $a\|Q_E\|_F^2+b\|Q_{T_2}\|_F^2$ by the inequivalent irreducible decomposition and Schur's lemma. The separate sector projectors give invariant functionals with different weights. This proves the symmetry-only obstruction.

| Uniform orbit | Lines | Weight on each $E$ component | Weight on each $T_2$ component |
| --- | ---: | ---: | ---: |
| Edge directions | 6 | $1/12$ | $1/6$ |
| Opposite-edge midpoint axes | 3 | $1/3$ | $0$ |
| Center-to-vertex lines | 4 | $0$ | $2/9$ |

On edge lines $(e_i\pm e_j)/\sqrt2$, the response before squaring is $-Q_{kk}/2\pm Q_{ij}$, where $k$ is the remaining axis. Summing both signs and averaging over the six edges gives $\sum_k Q_{kk}^2/12+\sum_{i<j} Q_{ij}^2/3$. The off-diagonal Frobenius norm counts each $Q_{ij}$ twice. Each opposite-edge midpoint line is a coordinate axis, so its squared response is $Q_{ii}^2$. The vertex directions have equal squared coordinates, so the trace-free diagonal terms cancel. Averaging over the four vertex signs cancels the cross terms between off-diagonal entries and gives $4\sum_{i<j}Q_{ij}^2/9$.

**NO-GO, scoped.** Any nonnegative unit-total mixture restricted to edges and vertices has a larger per-component weight on $T_2$ than on $E$. Equal weights are impossible in that family.

## Exact conditional equalization

Let $p\in[0,1]$ be the total weight on the six edge lines and $1-p$ the total weight on the three midpoint axes, uniform within each orbit. Equal component weights require
```math
\frac{p}{12}+\frac{1-p}{3}=\frac{p}{6}
\quad\Longleftrightarrow\quad p=\frac45.
```
Thus every edge line receives $2/15$ and every axis $1/15$. The common eigenvalue is $2/15$, so $M=(2/15)I_W$ and $M/\operatorname{tr}M=I_W/5$. Equal weight per direction across all nine lines yields $p=2/3$ and unequal component weights. Equalization selects the weights within this two-orbit family, given the imposed equality criterion. It supplies no reason the native dynamics must satisfy that criterion.

If the structural deficit $7/192$ is allocated according to the trace-normalized $M$ in this conditional model, each orthonormal response direction receives $7/960$. This model explicitly supplies the extra hypotheses behind that division. A native source must derive the orbit measures and a response law that allocates the deficit by this operator. An independent physical correspondence would also require an observable, calibration, uncertainty and a falsifiable test. No measured coupling value enters the replay. The coupling target was already present in the project context, so this exploratory result carries no prospective registration.

**Reopening criterion** · Derive the edge-to-midpoint-axis weight ratio from a fixed local interaction or sampling law with independently specified multiplicities. Reject this equalized construction under that law if the result gives a different ratio or an observable outside the declared quadratic probe. Only one response operator is tested here. Other source families remain open.

## Exact replay

The code generates the lines from the four vertices, evaluates the bilinear forms on a rational orthogonal basis using the unnormalized integer directions, and checks all 25 matrix entries for each orbit and the mixture. Python 3 standard library only.

```python
from fractions import Fraction as F
from itertools import combinations, product

vertices = [v for v in product((-1, 1), repeat=3) if v[0]*v[1]*v[2] == 1]
edges, axes = set(), set()

def line(v):
    sign = next(x for x in v if x != 0)
    return tuple(x * (1 if sign > 0 else -1) for x in v)

for u, v in combinations(vertices, 2):
    edges.add(line(tuple(a-b for a, b in zip(u, v))))
    axes.add(line(tuple(a+b for a, b in zip(u, v))))
assert (len(edges), len(axes)) == (6, 3)

basis = [
    ((1,0,0),(0,-1,0),(0,0,0)),
    ((1,0,0),(0,1,0),(0,0,-2)),
    ((0,1,0),(1,0,0),(0,0,0)),
    ((0,0,1),(0,0,0),(1,0,0)),
    ((0,0,0),(0,0,1),(0,1,0)),
]

def response(q, v):
    return F(sum(q[i][j]*v[i]*v[j] for i in range(3) for j in range(3)),
             sum(x*x for x in v))

def gram(lines):
    return [[sum(response(q, v)*response(r, v) for v in lines)/len(lines)
             for r in basis] for q in basis]

g_edges, g_axes, g_vertices = map(gram, (edges, axes, vertices))
norms = [sum(x*x for row in q for x in row) for q in basis]
p = F(4, 5)
for i, j in product(range(5), repeat=2):
    norm = norms[i] if i == j else 0
    assert g_edges[i][j] == norm * (F(1, 12) if i < 2 else F(1, 6))
    assert g_axes[i][j] == norm * (F(1, 3) if i < 2 else 0)
    assert g_vertices[i][j] == norm * (0 if i < 2 else F(2, 9))
    assert p*g_edges[i][j]+(1-p)*g_axes[i][j] == F(2, 15)*norm
assert F(1, 3)/(F(1, 3)+F(1, 6)-F(1, 12)) == p
assert 5*F(2, 15) == F(2, 3)
assert F(2, 15)/F(2, 3)*F(7, 192) == F(7, 960)
print("PASS · exact Gram matrices for all three orbits and the unique edge/axis balance")
```

Observed replay result: PASS · exact Gram matrices for all three orbits and the unique edge/axis balance.
