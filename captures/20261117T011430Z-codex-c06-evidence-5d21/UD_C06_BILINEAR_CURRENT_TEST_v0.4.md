# UD C06 bilinear current test v0.4

**Status** · EXACT for the declared polarized current maps. NO-GO for positive isotropy under the tested norms and nonnegative relation energies. OPEN for a native source selecting a metric on the current. Physical Promotion = 0.

**Provenance** · [Paper I v1.1.1, §§4.2–4.3, 5.1](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-03-UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md). [Paper III v1.1.1, §2 Theorem 1 and Proposition 3, and §9 relation Laplacians](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-00-UD_PAPER_III_REVIEW_DRAFT_v1.1.1.md). [Coefficient Ledger, C05–C06](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/ledger-recovery-v0.1/library_LEDGER_v0.85.json).

## Corrections to the v0.3 reception audit

The signed chain decomposition is $A_1\oplus2A_2\oplus2T_1\oplus2T_2$. In the displayed edge response of v0.3, $32/9$ is the coefficient of $s^2$, while the second derivative at zero is $(64/9)\|Q_{T_2}\|_F^2$. The contrast of the quadratic coefficients remains $-32/9$. The linear preparation obstruction is a statement about the specified carrier and equivariance. It leaves additional carriers, auxiliary contexts and nonlinear preparation with higher-order readouts logically open. Adding a bilinear readout after a preparation that already erases $E$ will still erase $E$.

## Construction

On one regular filled tetrahedron set $a_v=v/2$ for the four sign triples $v$ of product $+1$. The map $u\mapsto x$, $x_v=a_v^Tu$, is an isometry from $V=\mathbb R^3$ to the mean-zero vertex amplitudes, since $\sum_v a_va_v^T=I$. Prepare $c(0)=(x,0,0,0)$. The unit-metric signed Hodge flow has vertex and edge components $c_0=\cos(2s)x$ and $c_1=\tfrac12\sin(2s)B_1^Tx$, with higher components zero. The total chain support is conserved. Paper I's incidence current is $J_{ve}=2(B_1)_{ve}c_{0v}c_{1e}$.

For increasing orientation $e=(i,j)$, define $d_e=a_j-a_i$ and $n_e=d_e/\sqrt2$. Extend the current from $uu^T$ to symmetric matrix inputs by polarization, then restrict to $W=\operatorname{Sym}_0^2(V)=E\oplus T_2$:
```math
L_{ve,s}(Q)=\tfrac12\sin(4s)(B_1)_{ve}\,a_v^TQd_e,
\qquad N_{e,s}(Q)=\sum_{v\in e} L_{ve,s}(Q)=\sin(4s)n_e^TQn_e.
```
A change of edge orientation flips both incidence and direction. The current outputs are naturally ordinary real incidence or edge scalars. A trace-free probe is a linear combination of rank-one preparation receipts, in general with signed coefficients. This construction is a linear map on the quadratic input, with no claim that an arbitrary trace-free matrix is a single prepared chain state.

## Exact response weights

The Euclidean output norms give the following Gram eigenvalues relative to the Frobenius input metric, after factoring out $\sin^2(4s)$.

| Readout | $E$ | $T_2$ |
| --- | ---: | ---: |
| Twelve endpoint currents squared separately | $1/4$ | $3/4$ |
| Six net edge currents squared | $1/2$ | $1$ |
| Adjacent-edge difference energy of net currents | $3$ | $4$ |
| Opposite-edge difference energy of net currents | $0$ | $2$ |

For the net readout, each opposite pair has directions $(e_i\pm e_j)/\sqrt2$, so each pair sums to $-Q_{kk}$ and its difference is $2Q_{ij}$. Summing the squared net components gives $\|Q_E\|_F^2/2+\|Q_{T_2}\|_F^2$. For the endpoint readout, write $m_e=(a_i+a_j)/2$. The sum of the squared two endpoint terms before applying the prefactor equals $2(m_e^TQd_e)^2+(d_e^TQd_e)^2/2$. Across all six edges, the first term contributes $\|Q_{T_2}\|_F^2$, the second $\|Q_E\|_F^2+2\|Q_{T_2}\|_F^2$. The prefactor supplies the additional factor $1/4$. Paper III's relation Laplacians act on signed-current values treated as edge scalars. Their sector eigenvalues $(6,4)$ and $(0,2)$ multiply the net readout's $(1/2,1)$.

Both direct norms recover $E$ at nonzero response times. All four forms favor $T_2$ strictly when the time factor is nonzero. Every nonzero nonnegative combination of these squared readouts therefore fails positive isotropy. When $s\in(\pi/4)\mathbb Z$, the response is zero.

The net current's normalized opposite-pair sums and differences isolate $E$ and $T_2$ respectively. Their squared weights are $1/2$ and $1$ after removing the common time factor. An axis-pair sum readout with twice the squared gain of the difference readout would equalize the two sectors. This is a condition on a candidate metric. Deriving that metric or its competing value from dynamics, and deriving the deficit allocation, remain open.

## Exact replay

The verifier removes the common scalar $\sin(4s)$ and checks all 25 entries of the polarized Gram forms for both readouts and both relation energies. Python 3 standard library only.

```python
from fractions import Fraction as F
from itertools import combinations, product
from math import prod

vertices = [v for v in product((-1, 1), repeat=3) if prod(v) == 1]
edges = list(combinations(range(4), 2))
basis = [
    ((1, 0, 0), (0, -1, 0), (0, 0, 0)),
    ((1, 0, 0), (0, 1, 0), (0, 0, -2)),
    ((0, 1, 0), (1, 0, 0), (0, 0, 0)),
    ((0, 0, 1), (0, 0, 0), (1, 0, 0)),
    ((0, 0, 0), (0, 0, 1), (0, 1, 0)),
]

def readouts(q):
    endpoints, net = [], []
    for i, j in edges:
        diff = [b-a for a,b in zip(vertices[i], vertices[j])]
        terms = [
            F(sign*sum(vertices[v][k]*q[k][l]*diff[l]
                       for k,l in product(range(3), repeat=2)), 8)
            for v,sign in [(i,-1),(j,1)]
        ]
        endpoints += terms
        net.append(sum(terms))
    return endpoints, net

def dot(a, b):
    return sum(x*y for x,y in zip(a,b))

for i,j in product(range(5), repeat=2):
    ends_i, net_i = readouts(basis[i])
    ends_j, net_j = readouts(basis[j])
    norm = sum(x*x for row in basis[i] for x in row) if i == j else 0
    assert dot(ends_i, ends_j) == norm * (F(1,4) if i < 2 else F(3,4))
    assert dot(net_i, net_j) == norm * (F(1,2) if i < 2 else 1)
    for overlap in (0,1):
        form = sum((net_i[a]-net_i[b])*(net_j[a]-net_j[b])
                   for a,b in combinations(range(6),2)
                   if len(set(edges[a]) & set(edges[b])) == overlap)
        expected = (0 if i < 2 else 2) if overlap == 0 else (3 if i < 2 else 4)
        assert form == norm * expected
print('PASS · 25 rational Gram entries for both current readouts and both relation energies')
```

Observed replay result: PASS · 25 rational Gram entries for both current readouts and both relation energies.
