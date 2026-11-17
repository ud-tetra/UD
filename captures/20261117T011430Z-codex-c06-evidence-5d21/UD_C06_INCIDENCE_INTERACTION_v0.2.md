# UD C06 incidence interaction v0.2

**Status** · EXACT for the declared interaction and algebraic readout. CANDIDATE (agile) for a native source. OPEN for selection of the receipt dynamics and deficit allocation. Physical Promotion = 0.

**Dependencies** · UD C06 tetrahedral response source v0.1, exact line averages. [Paper III v1.1.1, Proposition 3](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-00-UD_PAPER_III_REVIEW_DRAFT_v1.1.1.md) for the response space. [Recovered coefficient ledger, v0.85 filename, C05–C06](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/ledger-recovery-v0.1/library_LEDGER_v0.85.json) for the physical source gate. This is an additive discovery note.

## Fixed incidence rule and evolution

On one regular filled tetrahedron, let $W$ be the real, trace-free symmetric matrices on the Euclidean standard vertex representation. Use the Frobenius metric and the decomposition $W=E\oplus T_2$. For an unoriented unit line $n$, use the scalar functional $x_n(Q)=n^\mathsf{T}Qn$.

Introduce a real receipt register with one orthogonal coordinate per edge–face incidence $(e,f)$, and one per unordered opposite-edge pair $p$. The local readout map $R:W\to\mathbb R^{15}$ records $x_{n_e}(Q)$ in each incidence coordinate, where $n_e$ is the edge line, and $x_{m_p}(Q)$ in the pair coordinate, where $m_p$ joins the two edge midpoints. Both kinds use the same unit amplitude gain. The 15 receipt coordinates are distinct from the 15 simplex amplitudes of the UD chain carrier.

The closed, dimensionless interaction on $W\oplus\mathbb R^{15}$ is
```math
\dot Q=-R^*z,\qquad \dot z=RQ,\qquad Q(0)=Q_0,\quad z(0)=0.
```
This is a skew generator with the declared metrics, so $\|Q\|_F^2+\|z\|^2$ is conserved. Relabelings permute the receipts and act by orthogonal conjugation on $Q$. The readout is $\|z\|^2$. The undeclared physical scales, compartments, and conversion to the UD chain generator are open.

Each of six edges lies in two triangular faces. Each of the three opposite-edge pairs is recorded once. Thus the count yields a 2:1 per-direction multiplicity, with edge and axis orbit weights $12/15$ and $3/15$ when every receipt is counted once. These weights are obtained by counting the specified inventory, without using the isotropy equation or a measured coupling in the calculation. Selecting these two receipt families, equal gain, and orthogonal receipt coordinates are model assumptions. The result is exploratory given prior exposure to the required ratio.

## Exact signal-combination test

The squared responses summed over flags give $\|Q_E\|_F^2+2\|Q_{T_2}\|_F^2$. The three pair-axis responses give $\|Q_E\|_F^2$. Thus $R^*R=2I_W$. For the declared dynamics, $Q(t)=\cos(\sqrt2t)Q_0$ and $z(t)=\sin(\sqrt2t) RQ_0/\sqrt2$. The receipt norm is $\sin^2(\sqrt2t)\|Q_0\|_F^2$. The average readout Gram operator per receipt is $(2/15)I_W$ and its trace-normalization is $I_W/5$.

For the unsigned coherent comparator, a face records the sum of its three edge responses before squaring. Each face meets one edge from each opposite pair. The diagonal response is proportional to the trace and cancels. On the off-diagonal sector the four face sign triples have mutually orthogonal columns with squared length four. Their squared sums therefore give $2\|Q_{T_2}\|_F^2$. Adding the same pair-axis readout yields weights $1$ and $2$ in the two sectors. This comparator is equivariant and uses the same tetrahedral incidences. It does not use the signed UD boundary map.

More generally, require a symmetric within-face readout with equal diagonal coefficient $g$ and equal off-diagonal coefficient $h$ on the three edge amplitudes. Let $m$ be the squared gain on pair-axis channels. The face quadratic form is positive semidefinite when $g+2h\ge0$ and $g-h\ge0$, with $m\ge0$ for the axis contributions. The weights are
```math
w_E=g-h+m,\qquad w_{T_2}=2g.
```
The condition for equal, positive weights is $m=g+h$ with $g>0$. With equal edge and axis gains ($m=g$), equality requires $h=0$. This is a no-go for forcing division by five from incidence or symmetry alone within the declared family. The independent-flag model gives a sufficient construction, and the coherent comparator falsifies universality across these local readouts.

**Next gate** · Derive the local squared gains and cross terms from a source-defined UD interaction, including its prepared state and readout. A different value of $m-g-h$ rules out equal response under this probe. Even a source-derived equal response would still require deriving the allocation of $7/192$ by its trace fractions.

## Reproduction

The exact Python 3 replay independently constructs the incidence sets and unit-line quadratic probes from the four vertices. It checks every matrix entry in a rational orthogonal basis for both readouts and the general formula at explicit gain/coherence controls.

```python
from fractions import Fraction
from itertools import combinations, product

vertices = [v for v in product((-1, 1), repeat=3) if v[0]*v[1]*v[2] == 1]
edges = tuple(combinations(range(4), 2))
faces = tuple(combinations(range(4), 3))
face_edges = [tuple(e for e in edges if set(e) <= set(f)) for f in faces]
pairs = tuple((e, f) for e, f in combinations(edges, 2) if not set(e) & set(f))
flags = [(face, edge) for face in face_edges for edge in face]
assert len(flags) == 12 and len(pairs) == 3
assert all(sum(e == edge for _, edge in flags) == 2 for e in edges)
basis = [
    ((1,0,0),(0,-1,0),(0,0,0)),
    ((1,0,0),(0,1,0),(0,0,-2)),
    ((0,1,0),(1,0,0),(0,0,0)),
    ((0,0,1),(0,0,0),(1,0,0)),
    ((0,0,0),(0,0,1),(0,1,0)),
]

def line_response(q, v):
    return Fraction(sum(q[i][j] * v[i] * v[j] for i in range(3) for j in range(3)),
                    sum(x*x for x in v))

def channels(q):
    edge_response = {
        (i, j): line_response(q, tuple(a-b for a, b in zip(vertices[i], vertices[j])))
        for i, j in edges
    }
    axis_response = []
    for (i, j), (k, l) in pairs:
        line = tuple(a+b for a, b in zip(vertices[i], vertices[j]))
        other = tuple(a+b for a, b in zip(vertices[k], vertices[l]))
        assert tuple(-x for x in line) == other
        axis_response.append(line_response(q, line))
    return (
        [edge_response[e] for _, e in flags],
        [sum(edge_response[e] for e in face) for face in face_edges],
        axis_response,
    )

def dot(x, y):
    return sum(a*b for a, b in zip(x, y))

for i, q in enumerate(basis):
    for j, r in enumerate(basis):
        diag = sum(a*a for row in q for a in row) if i == j else 0
        flag, face, pair = [dot(x,y) for x,y in zip(channels(q), channels(r))]
        assert flag == diag * (1 if i < 2 else 2)
        assert face == diag * (0 if i < 2 else 2)
        assert pair == diag * (1 if i < 2 else 0)
        assert flag+pair == 2*diag
        assert face+pair == diag * (1 if i < 2 else 2)
        for g, h, m in [(1,0,1),(1,1,1),(1,Fraction(-1,2),Fraction(1,2)),(2,1,3)]:
            assert g*flag+h*(face-flag)+m*pair == diag * (g-h+m if i < 2 else 2*g)

print("PASS · opposite-axis pairing, 12 incidences, 25 Gram entries per readout, four gain/coherence controls")
```

Observed replay result: PASS · opposite-axis pairing, 12 incidences, 25 Gram entries per readout, four gain/coherence controls.
