# UD C06 opposite-pair gain test v0.5

**Status** · EXACT for the declared linear operators, metric projections and finite replay. NO-GO for the stated nonnegative relation energies and for the orthogonal pushforward of the 12 edge–face flags. CANDIDATE (agile) for an augmented matching-sum readout. Native selection and deficit allocation remain OPEN. Physical Promotion = 0.

**Sources** · [Paper III v1.1.1, §9, relation algebra and No-go 14](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-00-UD_PAPER_III_REVIEW_DRAFT_v1.1.1.md). [Paper I v1.1.1, §5.1](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-03-UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md). [Coefficient Ledger, C05–C06](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/ledger-recovery-v0.1/library_LEDGER_v0.85.json). Predecessors are the v0.2 incidence interaction and v0.4 polarized bilinear current.

## Audit normalization and typed gain

Strip the common factor $\sin(4s)$ from the v0.4 polarized net current on a regular filled tetrahedron, so $x_e=n_e^T Q n_e$ with $Q$ trace-free symmetric and $Q$ measured in the Frobenius metric. This stripped map is defined directly for all $s$. The original current vanishes when $\sin(4s)=0$. On each opposite pair use orthonormal modes $S_k=(x_{e_1}+x_{e_2})/\sqrt2$ and $D_k=(x_{e_1}-x_{e_2})/\sqrt2$. The raw sums and differences evaluate to $-Q_{kk}$ and $2Q_{ij}$, and their squared norms are $\|Q_E\|_F^2$ and $2\|Q_{T_2}\|_F^2$. The weights $1/2$ and $1$ belong to the normalized modes. Both conventions give the same necessary gain ratio $2:1$.

The edge current is mean-zero. In the standard six-edge permutation module it belongs to $E\oplus T_2$. For an edge-space energy $x^TMx$, denote the two eigenvalues of $M$ on these sectors by $\mu_+,\mu_-$. These are squared gains. The $Q$-space response weights are $(\mu_+/2,\mu_-)$. Positive equalization therefore requires $\mu_+=2\mu_->0$.

## Paper III relation interactions

Take the source relation matrices $L_{\rm adj}$, $L_{\rm opp}$ on all six edge coordinates. The interaction energy
```math
x^TMx,\qquad M=cI+aL_{\rm adj}+bL_{\rm opp},\qquad a,b,c\ge0
```
has squared gains $(c+6a,c+4a+2b)$. Their ratio is at most $3/2$ for any nontrivial such energy. Equivalently, $\mu_+-2\mu_-=-c-2a-4b<0$. The unit adjacent and unit opposite cases follow without tuning. Counting every distinct edge relation once gives $a=b=1,c=0$, yielding a ratio of $1$.

As a separate candidate interaction, let the dimensionless closed edge current evolve by the dissipative equation $\dot x=-(aL_{\rm adj}+bL_{\rm opp})x$ and read its Euclidean squared norm after time $t\ge0$. This conserves the total sum, contracts the Euclidean norm and yields a squared-gain ratio $\exp(4(b-a)t)$. Equal per-relation rates give $1$ at all times. With $b>a$ an isolated time $t=\ln(2)/[4(b-a)]$ gives $2$, conditional on the declared diffusion and sampling time. The source relation algebra supplies no such selected time. The static theorem above concerns the quadratic form of the relation operators, not the norm after a dynamical filter.

## 12 edge–face flags

Let $F x$ copy each edge scalar onto its two edge–face flags, using unit Euclidean metrics on both spaces. Then $F^*F=2I$. This flag energy gives edge squared gains $(2,2)$, independent of pair parity. If instead the input is an arbitrary flag vector and its aggregate edge current is $x=F^*y$, the least Euclidean flag cost at fixed $x$ is $\|x\|^2/2$, attained at $y=Fx/2$. This follows by orthogonality to $\ker F^*$. Orthogonal passage to the pair modes gives $(1/2,1/2)$ for that cost. In both directions the ratio is $1$.

The v0.2 fixed equalization includes three distinct midpoint-axis receipts alongside the twelve flags and counts their squared responses separately with equal gains. On the current map, the normalized pair sums satisfy $S_k=-Q_{kk}/\sqrt2$, so the axis receipt $Q_{kk}$ contributes $2S_k^2$. The flags give $2\|x\|^2$. Together they produce $2(I+\Pi_+)$ as an edge-space metric. The pair-sum contribution in this identity comes from the added axis receipts.

## Conditional matching readout

The normalized matching-address map $U$ records one sum per opposite pair with entries $1/\sqrt2$ on its two edges. Then $U^*U=\Pi_+$, the orthogonal projector onto pair-even edge modes, and $U U^*=I$ on the three matching addresses. The comparison readout $x\mapsto(x,Ux)$ into orthogonal registers has pullback metric $I+\Pi_+$ and meets the ratio exactly because a separate normalized matching-sum register is read at the same amplitude gain as the direct edge register. A source law must still derive that register and its specified joint readout, or an equivalent metric, and separately derive allocation of $7/192$ by response trace fractions.

## Exact replay

The Python 3 replay constructs the edges, matchings, face flags and relation Laplacians from the vertex labels and checks each operator on a basis of both sectors in rational arithmetic.

```python
from fractions import Fraction as F
from itertools import combinations

edges = list(combinations(range(4), 2))
faces = list(combinations(range(4), 3))
pairs = [(i,j) for i,j in combinations(range(6),2)
         if not set(edges[i]) & set(edges[j])]
flags = [(face,i) for face in faces for i,e in enumerate(edges)
         if set(e) <= set(face)]

def relation_laplacian(x, shared):
    return [sum(x[i]-x[j] for j,f in enumerate(edges)
                if i != j and len(set(e) & set(f)) == shared)
            for i,e in enumerate(edges)]

def even_projection(x):
    result = [0]*6
    for i,j in pairs:
        result[i] = result[j] = F(x[i]+x[j],2)
    return result

def dot(x, y):
    return sum(a*b for a,b in zip(x,y))

def sum_flags(y):
    return [sum(z for (_,i),z in zip(flags,y) if i == j) for j in range(6)]

def basis_vector(pair_coefficients, even):
    result = [0]*6
    for (i,j),c in zip(pairs,pair_coefficients):
        result[i],result[j] = c,c if even else -c
    return result

basis_e = [basis_vector(c, True) for c in ((1,-1,0),(1,1,-2))]
basis_t = [basis_vector(c, False) for c in ((1,0,0),(0,1,0),(0,0,1))]
assert len(pairs) == 3 and len(flags) == 12
for even,basis in [(True,basis_e),(False,basis_t)]:
    for x in basis:
        assert sum(x) == 0
        assert relation_laplacian(x,1) == [(6 if even else 4)*v for v in x]
        assert relation_laplacian(x,0) == [(0 if even else 2)*v for v in x]
        assert sum_flags([x[i] for _,i in flags]) == [2*v for v in x]
        y = [F(x[i],2) for _,i in flags]
        assert sum_flags(y) == x and dot(y,y) == F(1,2)*dot(x,x)
        p = even_projection(x)
        assert [v+w for v,w in zip(x,p)] == [(2 if even else 1)*v for v in x]
        assert sum(F((x[i]+x[j])**2,2) for i,j in pairs) == dot(x,p)
print('PASS · relation operators, flag lift and minimum-norm aggregation, and matching-sum metric')
```

Observed result: PASS · relation operators, flag lift and minimum-norm aggregation, and matching-sum metric.
