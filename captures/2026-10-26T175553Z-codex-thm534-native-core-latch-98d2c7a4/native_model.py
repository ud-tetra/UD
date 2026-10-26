"""Fresh standard-library exact reconstruction of the original native carrier."""
from fractions import Fraction as Q
from itertools import combinations
CELLS=[(0,1,2,3),(0,1,2,4)]
ORIENT=[1,-1]
SIMP=[sorted({s for c in CELLS for s in combinations(c,k)}) for k in range(1,5)]
OFF=[0,5,14,21]
N=23
def boundary(k):
    a=[[Q(0)]*len(SIMP[k]) for _ in SIMP[k-1]]
    for j,s in enumerate(SIMP[k]):
        for i in range(k+1):a[SIMP[k-1].index(s[:i]+s[i+1:])][j]=Q((-1)**i*(ORIENT[j] if k==3 else 1))
    return a
B=[boundary(k) for k in range(1,4)]
def native(h):
    assert len(h)==7 and all(v in (0,1) for v in h)
    a=[[Q(0)]*N for _ in range(N)]
    for k,b in enumerate(B):
        for i,row in enumerate(b):
            for j,d in enumerate(row):
                v=d*(h[i] if k==2 else 1)
                a[OFF[k]+i][OFF[k+1]+j]=-v
                a[OFF[k+1]+j][OFF[k]+i]=v
    return a
def mv(a,x):return [sum(v*w for v,w in zip(row,x)) for row in a]
def dot(x,y):return sum(v*w for v,w in zip(x,y))
def checkpoints():
    x=[Q(0)]*N
    for edge,v in [((0,1),-1),((0,2),1),((1,2),-1)]:x[5+SIMP[1].index(edge)]=Q(v)
    c=Q(24,37);feed=14+SIMP[2].index((0,1,4));out=14+SIMP[2].index((0,2,4))
    y=[v*Q(3,37) for v in x]
    for face,v in [((0,1,2),-48),((0,1,3),-20),((0,2,3),20),((1,2,3),-20)]:y[14+SIMP[2].index(face)]=Q(v,37)
    y[21]=c;z=y.copy();z[21]=Q(0)
    p0=x.copy();p0[feed]=c;p1=y.copy();p1[feed]=c
    p2=z.copy();p2[feed]=c;p2[out]=c;p3=x.copy();p3[out]=c
    return [p0,p1,p2,p3]
WEIGHTS=[]
for cell in CELLS:
    WEIGHTS.append([Q(int(set(s)<=set(cell)),sum(set(s)<=set(c) for c in CELLS)) for ss in SIMP for s in ss])
def stock(x,w):return sum(v*v*a for v,a in zip(x,w))
