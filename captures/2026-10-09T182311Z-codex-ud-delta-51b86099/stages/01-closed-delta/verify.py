"""Exact rational two-tetrahedron closure audit. Python standard library only."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

def transpose(a): return [list(x) for x in zip(*a)]
def mul(a,b): return [[sum(x*y for x,y in zip(r,c)) for c in transpose(b)] for r in a]
def scale(a,k): return [[k*x for x in r] for r in a]
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def zeros(m,n): return [[Q(0) for _ in range(n)] for _ in range(m)]
def eye(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def rref(a):
    a=[[Q(x) for x in r] for r in a]; i=0; piv=[]
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None: continue
        a[i],a[k]=a[k],a[i]; v=a[i][j]; a[i]=[x/v for x in a[i]]
        for k in range(len(a)):
            if k!=i:
                v=a[k][j]; a[k]=[x-v*y for x,y in zip(a[k],a[i])]
        piv.append(j); i+=1
        if i==len(a): break
    return a[:i],piv

cells=[(0,1,2,3),(0,1,2,4)]
simp=[sorted({t for c in cells for t in combinations(c,k+1)}) for k in range(4)]
flat=sum(simp,[]); n=len(flat); ix={t:i for i,t in enumerate(flat)}
B=zeros(n,n)
for t in flat:
    if len(t)>1:
        for j in range(len(t)): B[ix[t[:j]+t[j+1:]]][ix[t]]=Q((-1)**j)
A=add(transpose(B),scale(B,-1)); I=eye(n)
checks={}
def check(name,condition):
    checks[name]=bool(condition)
    assert condition,name
check('f_vector',[len(x) for x in simp]==[5,9,7,2])
check('boundary_squared_zero',mul(B,B)==zeros(n,n))
check('generator_skew',transpose(A)==scale(A,-1))

def closure(ts):
    R=[I[ix[t]] for t in ts]; O,_=rref(R); ranks=[len(O)]
    while True:
        N,_=rref(O+mul(O,A))
        if len(N)==len(O): break
        O=N; ranks.append(len(O))
    # RREF rows have an identity submatrix on pivot columns.
    O,piv=rref(O); OA=mul(O,A)
    H=[[row[j] for j in piv] for row in OA]
    check('closed_'+str(len(ts)),mul(H,O)==OA)
    return {'ranks':ranks,'R':R,'O':O,'H':H}

results={name:closure(ts) for name,ts in [
    ('cells',cells),('cells_shared_face',cells+[(0,1,2)]),
    ('all_faces_and_cells',simp[2]+cells)]}

# Same retained cells/shared face, same full norm, opposite next cell derivatives.
R=results['cells_shared_face']['R']
x=[[v] for v in I[ix[(0,1,2,3)]]]
u=[[v] for v in I[ix[(0,1,3)]]]
xp=add(x,u); xm=add(x,scale(u,-1))
check('counterexample_same_record',mul(R,xp)==mul(R,xm))
check('counterexample_same_norm',mul(transpose(xp),xp)==mul(transpose(xm),xm))
dxp=mul(R,mul(A,xp)); dxm=mul(R,mul(A,xm))
check('counterexample_different_next_derivative',dxp!=dxm)
check('counterexample_cell_stock_derivatives',2*dxp[0][0]==2 and 2*dxm[0][0]==-2)

# Four-coordinate exact quotient: q=c3, v=B3^T c2.
Rq=[I[ix[t]] for t in cells]; Rv=mul(Rq,A); R4=Rq+Rv
K=[[Q(4),Q(1)],[Q(1),Q(4)]]
H4=[[Q(0),Q(0),Q(1),Q(0)],[Q(0),Q(0),Q(0),Q(1)],
    [Q(-4),Q(-1),Q(0),Q(0)],[Q(-1),Q(-4),Q(0),Q(0)]]
check('four_coordinate_intertwiner',mul(R4,A)==mul(H4,R4))
check('four_coordinate_independent',len(rref(R4)[0])==4)
check('four_coordinate_minimal_linear_quotient',results['cells']['ranks']==[2,4])

# Six-coordinate quotient including the shared face and its derivative.
Rf=[I[ix[(0,1,2)]]]; Rw=mul(Rf,A); R6=R4+Rf+Rw
H6=[r+[Q(0),Q(0)] for r in H4]+[
    [Q(0),Q(0),Q(0),Q(0),Q(0),Q(1)],
    [Q(0),Q(0),Q(0),Q(0),Q(-5),Q(0)]]
check('six_coordinate_intertwiner',mul(R6,A)==mul(H6,R6))
check('six_coordinate_independent',len(rref(R6)[0])==6)
check('six_coordinate_minimal_linear_quotient',results['cells_shared_face']['ranks']==[3,6])

# Two local incidence rotations sharing the shared face do not commute.
f=ix[(0,1,2)]; t1,t2=map(ix.get,cells)
def incidence_rotation(t):
    L=zeros(n,n); L[t][f]=A[t][f]; L[f][t]=A[f][t]; return L
L1=incidence_rotation(t1); L2=incidence_rotation(t2)
comm=add(mul(L2,L1),scale(mul(L1,L2),-1))
check('shared_interface_updates_noncommuting',comm!=zeros(n,n))
check('order_witness',mul(comm,x)[t2][0]==-1)

out={'status':'development; exact finite linear model; no registry promotion',
     'generator':'A=B^T-B; increasing simplex orientation; unit metric',
     'simplex_order':flat,'closure_ranks':{k:v['ranks'] for k,v in results.items()},
     'counterexample':{'x_plus':'e0123+e013','x_minus':'e0123-e013',
                       'retained_derivative_plus':dxp,'retained_derivative_minus':dxm},
     'R4':R4,'H4':H4,'R6':R6,'H6':H6,'closure_records':results,'checks':checks,
     'passed':sum(checks.values()),'total':len(checks)}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({'closure_ranks':out['closure_ranks'],'passed':out['passed'],
                  'total':out['total'],'derivatives':[dxp,dxm]},default=str,indent=2))
