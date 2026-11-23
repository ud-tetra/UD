#!/usr/bin/env python3
"""Second algorithm: pure stdlib Fraction segment intersection and Faddeev-LeVerrier 30x30 characteristic polynomial."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

points=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
edges=list(combinations(range(4),2))
q=[[F(v,87) for v in row] for row in [[-61,-22,58],[62,-19,58],[-2,82,29]]]
I=[[int(i==j) for j in range(3)] for i in range(3)]
Q90=[[0,-1,0],[1,0,0],[0,0,1]]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(A):return dot(A[0],cross(A[1],A[2]))
def times(Q,v):return tuple(dot(r,v) for r in Q)
def contact(p,q0,r,s):
    u=sub(q0,p);v=sub(s,r);w=sub(r,p);normal=cross(u,v)
    if dot(normal,normal)==0:
        if cross(w,u)!=(0,0,0):return ('none',None)
        j=next(i for i in range(3) if u[i])
        lo=max(min(p[j],q0[j]),min(r[j],s[j]));hi=min(max(p[j],q0[j]),max(r[j],s[j]))
        return ('overlap' if lo<hi else ('endpoint' if lo==hi else 'none'),None)
    # independent coplanarity from three-row determinant
    if det3((u,v,w))!=0:return ('none',None)
    t=F(dot(cross(w,v),normal),dot(normal,normal))
    z=F(dot(cross(w,u),normal),dot(normal,normal))
    if t<0 or t>1 or z<0 or z>1:return ('none',None)
    pt=add(p,mul(t,u))
    return ('interior' if 0<t<1 and 0<z<1 else 'endpoint',(t,z,pt,1 if dot(pt,normal)>0 else -1))

def calc(Q):
    A=points;B=[mul(-1,times(Q,x)) for x in A];hits=[];cop_nonzero=0
    for i,(a,b) in enumerate(edges):
        for j,(c,d) in enumerate(edges):
            u=sub(A[b],A[a]);v=sub(B[d],B[c]);w=sub(B[c],A[a]);cop=det3((u,v,w))
            cop_nonzero+= int(cop!=0)
            kind,x=contact(A[a],A[b],B[c],B[d])
            if kind!='none':hits.append((i,j,kind,x))
    return hits,cop_nonzero

six,n0=calc(I)
zero,n1=calc(q)
merge,n2=calc(Q90)
assert len(six)==6 and all(h[2]=='interior' and h[3][0:2]==(F(1,2),F(1,2)) for h in six)
assert sorted((i,j) for i,j,_,_ in six)==[(0,5),(1,4),(2,3),(3,2),(4,1),(5,0)]
assert len(zero)==0 and n1==36
assert len(merge)==30 and sum(t[2]=='overlap' for t in merge)==6 and sum(t[2]=='endpoint' for t in merge)==24
assert all(sum(q[k][i]*q[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
assert det3(q)==1
signed=[[0]*6 for _ in range(6)]
for i,j,_,x in six:signed[i][j]=x[-1]
assert signed[0][5]==signed[5][0]==1 and signed[1][4]==signed[4][1]==-1 and signed[2][3]==signed[3][2]==1

# Independent 15-chain incidence reconstruction, no SymPy.
chains=[c for d in range(1,5) for c in combinations(range(4),d)];ix={c:i for i,c in enumerate(chains)}
A=[[0]*15 for _ in range(15)]
for c in chains:
    if len(c)==1:continue
    j=ix[c]
    for k in range(len(c)):
        i=ix[c[:k]+c[k+1:]]
        A[i][j]=(-1)**(k+1);A[j][i]=(-1)**k

def full(K):
    H=[[0]*30 for _ in range(30)]
    for i in range(15):
        for j in range(15):H[i][j]=A[i][j];H[15+i][15+j]=A[i][j]
    for i in range(6):
        for j in range(6):H[4+i][15+4+j]=K[i][j];H[15+4+j][4+i]=-K[i][j]
    return H

def mm(A,B):
    n=len(A);C=[[0]*n for _ in range(n)]
    for i,row in enumerate(A):
        for k,t in enumerate(row):
            if t:
                for j,b in enumerate(B[k]):
                    if b:C[i][j]+=t*b
    return C

def charpoly(H):
    n=len(H);B=[[int(i==j) for j in range(n)] for i in range(n)];res=[1]
    for k in range(1,n+1):
        B=mm(H,B)
        tr=sum(B[i][i] for i in range(n))
        assert tr%k==0
        c=-tr//k;res.append(c)
        for i in range(n):B[i][i]+=c
    assert all(not x for row in B for x in row)
    return res

def polymul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def polypow(a,k):
    z=[1]
    for _ in range(k):z=polymul(z,a)
    return z
# Coefficients descending: z^30 polynomial, expected z²(z²+4)²(z⁴+9z²+16)^6.
expected=polymul([1,0,0],polymul(polypow([1,0,4],2),polypow([1,0,9,0,16],6)))
uncoupled=polymul([1,0,0],polypow([1,0,4],14))
C=[[int((i,j) in {(0,5),(1,4),(2,3),(3,2),(4,1),(5,0)}) for j in range(6)] for i in range(6)]
Z=[[0]*6 for _ in range(6)]
Id=[[int(i==j) for j in range(6)] for i in range(6)]
assert charpoly(full(C))==expected
assert charpoly(full(signed))==expected
assert charpoly(full(Id))==expected
assert charpoly(full(Z))==uncoupled
result={
 'backend':'stdlib fractions exact independent algorithm',
 'identity_contacts':len(six),'identity_interior':6,'identity_signed_contact_matrix':signed,
 'generic_contacts':len(zero),'generic_noncoplanar_pairs':n1,
 'quarter_turn_contact_pairs':len(merge),'quarter_turn_overlap_pairs':6,'quarter_turn_endpoint_pairs':24,
 'closed_chain_uncoupled_charpoly':'z^2*(z^2+4)^14',
 'illustrative_orthogonal_contact_charpoly':'z^2*(z^2+4)^2*(z^4+9*z^2+16)^6',
 'controls':['unsigned contact','signed contact','identity contact','zero coupling'],
 'all_exact_tests':'PASS','native_coupling_status':'OPEN',
 'physical_promotion':0
}
Path(__file__).with_name('replay_results.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print('PASS stdlib exact segment classifier, signed contact, and 30x30 characteristic polynomial controls')
