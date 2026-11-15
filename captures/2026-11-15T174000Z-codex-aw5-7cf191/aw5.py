"""Exact AW5 replay. Requires SymPy."""
from itertools import combinations
from functools import reduce
from sympy import Matrix, zeros, eye, factor, symbols

def build(cells):
    basis = [sorted({s for t in cells for s in combinations(t,k)}) for k in range(1,5)]
    ds = [Matrix(len(lo),len(hi),lambda i,j:sum((-1)**q for q in range(len(hi[j])) if hi[j][:q]+hi[j][q+1:]==lo[i])) for lo,hi in zip(basis,basis[1:])]
    assert all(d*e == zeros(d.rows,e.cols) for d,e in zip(ds,ds[1:]))
    return basis,ds

hub = (0,1,2,3)
leaves = [tuple(v for v in hub if v != i)+(4+i,) for i in hub]
lam = symbols("lambda")
for cells in ([hub], [hub]+leaves, leaves):
    b,d=build(cells)
    n=list(map(len,b))
    ranks=[0]+[m.rank() for m in d]+[0]
    print("f, betti:",n,[size-ranks[i]-ranks[i+1] for i,size in enumerate(n)])
    grams=[m.T*m for m in d]
    print("skew charpoly:",factor(lam**(sum(n)-2*sum(ranks))*reduce(lambda a,g:a*factor((lam**2*eye(g.rows)+g).det(method="domain-ge")/lam**(2*(g.rows-g.rank()))),grams,1)))
    print("top Gram eigenvalues:",grams[-1].eigenvals())
    if len(cells)==5:
        ext=[i for i in range(n[2]) if sum(x!=0 for x in d[2].row(i))==1]
        for q in (3,5):
            for k,g in enumerate(grams):
                vecs=(g-q*eye(g.rows)).nullspace()
                if not vecs:
                    continue
                V=Matrix.hstack(*vecs)
                if k==1:
                    F=V
                    G=F.extract(ext,range(F.cols)); print("face compression eigenvalues:", ( (F.T*F).inv()*G.T*G ).eigenvals())
                    print("squared frequency, coexact face dim, boundary rank:",q,V.cols,F.extract(ext,range(F.cols)).rank())
                elif k==2:
                    F=d[2]*V
                    print("squared frequency, top dim, boundary rank:",q,V.cols,F.extract(ext,range(F.cols)).rank())
    if cells == leaves:
        full_basis,full_d=build([hub]+leaves)
        z=full_d[2][:,full_basis[3].index(hub)]
        assert d[1]*z==zeros(d[1].rows,1)
        h=z-d[2]*(d[2].T*z)/4
        assert d[1]*h==zeros(d[1].rows,1) and d[2].T*h==zeros(4,1)
        print("shell pairings:",list(d[2].T*z),"harmonic support:",sum(v!=0 for v in h))

# Signed simplices are oriented by their increasing global vertex labels.
# Sum compatible copied coordinates onto each unique simplex.
filled_basis,_ = build([hub]+leaves)
single_basis,single_d = build([hub])
def skew(basis, boundaries):
    offsets=[0]
    for layer in basis:
        offsets.append(offsets[-1]+len(layer))
    b=zeros(offsets[-1])
    for k,d in enumerate(boundaries):
        b[offsets[k]:offsets[k+1],offsets[k+1]:offsets[k+2]]=d
    return b.T-b

from sympy import diag
copied = diag(*[skew(single_basis,single_d)]*5)
unique = [s for layer in filled_basis for s in layer]
projection=zeros(47,75)
for i,tet in enumerate([hub]+leaves):
    for j,s in enumerate(s for layer in build([tet])[0] for s in layer):
        projection[unique.index(s),15*i+j]=1
derivative=projection*copied
second=derivative*copied
first_jet=projection.col_join(derivative)
assert copied**3 == -4*copied
print("copied sum readout ranks P, [P;PA], [P;PA;PA²]:",
      projection.rank(),first_jet.rank(),first_jet.col_join(second).rank())
