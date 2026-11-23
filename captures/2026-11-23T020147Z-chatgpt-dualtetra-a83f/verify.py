#!/usr/bin/env python3
"""Exact two-tetrahedral contacts and source-interface controls; SymPy required.
No physical calibration, no imported kinetic coupling or metric emergence.
"""
import json
from itertools import combinations, permutations
from pathlib import Path
from collections import Counter
import sympy as S

V=[S.Matrix(x) for x in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
E=list(combinations(range(4),2))
I=S.eye(3)
Qstar=S.Matrix([[-61,-22,58],[62,-19,58],[-2,82,29]])/87
assert Qstar.T*Qstar==I and Qstar.det()==1


def detail(p,q,r,s):
    """Closed segments p+t(q-p),r+u(s-r); exact contact and type."""
    d=q-p;e=s-r;w=r-p;n=d.cross(e); n2=S.expand(n.dot(n));
    cop=S.expand(w.dot(n))
    if n2:
        if cop: return {'contact':False,'coplanarity':cop}
        t=S.cancel(w.cross(e).dot(n)/n2)
        u=S.cancel(w.cross(d).dot(n)/n2)
        if not (0<=t<=1 and 0<=u<=1):return {'contact':False,'coplanarity':cop,'t':t,'u':u}
        point=p+t*d
        sign=S.sign(point.dot(n))
        return {'contact':True,'coplanarity':cop,'t':t,'u':u,'point':tuple(point),'type':'interior' if 0<t<1 and 0<u<1 else 'endpoint', 'radial_sign':int(sign)}
    if w.cross(d)!=S.zeros(3,1):return {'contact':False,'coplanarity':0,'type':'parallel_disjoint'}
    # Collinear closed segments; compare projections onto a nonzero direction component.
    k=next(k for k in range(3) if d[k]); x1=p[k];x2=q[k];y1=r[k];y2=s[k]
    left=max(min(x1,x2),min(y1,y2));right=min(max(x1,x2),max(y1,y2))
    return {'contact':left<=right,'coplanarity':0,'type':'overlap' if left<right else ('endpoint' if left==right else 'collinear_disjoint')}


def audit(Q):
    B=[-Q*x for x in V]; contacts=[]; nonzero=[]; coplanar=[]; types=Counter()
    for i,e in enumerate(E):
        for j,f in enumerate(E):
            z=detail(V[e[0]],V[e[1]],B[f[0]],B[f[1]])
            if z['contact']:
                contacts.append(dict(A=e,B=f,t=str(z.get('t')),u=str(z.get('u')),point=list(map(str,z['point'])) if 'point' in z else None,type=z['type'],radial_sign=z.get('radial_sign')))
                types[z['type']]+=1
            if z['coplanarity']!=0:nonzero.append(z['coplanarity'])
            else:coplanar.append((e,f))
    return dict(contacts=contacts,ncontacts=len(contacts),nonzero_coplanarity=len(nonzero),zero_coplanarity=len(coplanar),types=dict(types),all_coplanarity_nonzero=len(nonzero)==36,first_four_coplanarity=list(map(str,nonzero[:4])))

identity=audit(I);rational=audit(Qstar)
Qquarter=S.Matrix([[0,-1,0],[1,0,0],[0,0,1]])
quarter=audit(Qquarter)
print('QUARTER TURN',quarter['ncontacts'],quarter['types'])
print('CANONICAL ncontacts',identity['ncontacts'],'types',identity['types'])
for z in identity['contacts']:print(z)
print('QSTAR',rational['ncontacts'],rational['nonzero_coplanarity'],rational['first_four_coplanarity'])
assert identity['ncontacts']==6
assert all(z['type']=='interior' and z['t']=='1/2' and z['u']=='1/2' for z in identity['contacts'])
assert rational['ncontacts']==0 and rational['all_coplanarity_nonzero']
assert all(set(x['A']).isdisjoint(x['B']) for x in identity['contacts'])
assert set(z['radial_sign'] for z in identity['contacts'])=={1,-1}

C=S.zeros(6)
Cs=S.zeros(6)
for z in identity['contacts']:
    i=E.index(tuple(z['A']));j=E.index(tuple(z['B']))
    C[i,j]=1; Cs[i,j]=z['radial_sign']
assert C*C==S.eye(6) and C==C.T
assert dict(C.eigenvals())=={S.Integer(-1):3,S.Integer(1):3}
# Previous UD PR #578/#579 D1: signed opposite-edge complement (+,-,+).
D1=S.zeros(6)
for i,j,sgn in [(0,5,1),(1,4,-1),(2,3,1)]:
    D1[i,j]=sgn;D1[j,i]=sgn
assert Cs==D1 and D1*D1==S.eye(6)
print('C=',C,'signed=',Cs,'signed eigs=',Cs.eigenvals())

# Exact K4 chain generator on degrees (4,6,4,1), as source JOP v2.5 §3.1.
Simp=[list(combinations(range(4),k)) for k in range(1,5)]
idx={tuple(s):k for k,s in enumerate(sum(Simp,[]))}
A=S.zeros(15)
for s in sum(Simp[1:],[]):
    j=idx[s]
    for k in range(len(s)):
        f=s[:k]+s[k+1:];i=idx[f];A[i,j]=(-1)**(k+1);A[j,i]=(-1)**k
assert A.T==-A
assert S.factor(A.charpoly().as_expr())==S.Symbol('lambda')*(S.Symbol('lambda')**2+4)**7

# Proposed *external* contact to edge coupling: 30x30 offdiagonal block; kappa=1 illustrative only.
K=S.zeros(15)
for i in range(6):
    for j in range(6):K[4+i,4+j]=C[i,j]
G0=S.diag(A,A)
G1=G0.copy()
G1[:15,15:]=K;G1[15:,:15]=-K.T
assert G1.T==-G1
z=S.Symbol('z')
p0=S.factor(G0.charpoly(z).as_expr());p1=S.factor(G1.charpoly(z).as_expr());
print('uncoupled charpoly:',p0)
print('conditional coupled charpoly:',p1)
assert p0!=p1
Ksign=S.zeros(15); Kid=S.zeros(15)
Ksign[4:10,4:10]=Cs;Kid[4:10,4:10]=S.eye(6)
def contact_charpoly(L):
    T=G0.copy();T[:15,15:]=L;T[15:,:15]=-L.T
    return S.factor(T.charpoly(z).as_expr())
p_sign=contact_charpoly(Ksign)
p_controledge=contact_charpoly(Kid)
assert p1==p_sign==p_controledge
kappa=S.Symbol('kappa',real=True)
poly_expect=z**2*(z**2+4)**2*(z**4+(8+kappa**2)*z**2+16)**6
poly_generic={}
for key,link in [('unsigned',C),('signed_D1',Cs),('ordinary_identity',S.eye(6))]:
    T=S.zeros(15)
    T[4:10,4:10]=kappa*link
    poly_generic[key]=contact_charpoly(T)
    assert S.expand(poly_generic[key]-poly_expect)==0
assert S.factor(poly_expect.subs(kappa,0))==p0

# internal support exchange: for state (x,y), intercell flow exactly +2*x^T K y and -2*x^T K y
x=S.Matrix([0]*4+[1]*6+[0]*5); y=S.Matrix([0]*4+[1]*6+[0]*5)
ex=2*(x.T*K*y)[0]
print('kappa1 support exchange +,-:',ex,-ex)

# Geometry covariance: A4 symmetry group maps V into itself as 3D signed permutation rotations.
from itertools import product
proper=[]
for perm in permutations(range(3)):
 for signs in product((-1,1),repeat=3):
    M=S.zeros(3)
    for i in range(3):M[i,perm[i]]=signs[i]
    if M.det()==1 and set(map(tuple,[M*x for x in V]))==set(map(tuple,V)):proper.append(M)
assert len(proper)==12
for rot in proper:
    ar=audit(rot)
    assert ar['ncontacts']==6 and ar['types'].get('interior')==6

out={
  'source_class':'exact_construction_not_ud_dynamics',
  'vertices':[list(map(int,v)) for v in V],
  'edges':[list(x) for x in E],
  'Qstar':[[str(x) for x in row] for row in Qstar.tolist()],
  'Qstar_det':str(Qstar.det()),
  'Qstar_orthogonal':True,
  'identity':identity,
  'Qstar_test':rational,
  'quarter_turn_test':quarter,
  'contact_matrix':C.tolist(),
  'signed_radial_contact_matrix':Cs.tolist(),
  'contact_eigenvalues':{str(k):v for k,v in C.eigenvals().items()},
  'contact_matrix_C2_I':C*C==S.eye(6),
  'signed_contact_equals_prior_D1':Cs==D1,
  'iso_spectral_null_across_contact_orthogonalizations':p1==p_sign==p_controledge,
  'modal_illustrative_signed_coupling_charpoly':str(p_sign),
  'modal_control_orthogonal_edge_identity_charpoly':str(p_controledge),
  'signed_radial_contact_eigenvalues':{str(k):v for k,v in Cs.eigenvals().items()},
  'symmetry_proper_rotations':len(proper),
  'modal_uncoupled_charpoly':str(p0),
  'modal_illustrative_unit_coupling_charpoly':str(p1),
  'illustrative_exchange':str(ex),
  'symbolic_coupling_charpoly':str(S.factor(poly_expect)),
  'signed_vs_unsigned_symbolic_isospectral':all(S.expand(v-poly_expect)==0 for v in poly_generic.values()),
  'illustrative_conductance_status':'introduced_external_kappa_not_native',
  'physical_promotion':0,
  'native_cross_contact_coupling':'OPEN',
}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True,default=str)+'\n')
print('PASS exact contact/source-interface and illustrative modal tests')
