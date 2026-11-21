#!/usr/bin/env python3
"""Exact Whitney/S4/signed-complement coframe audit. SymPy. No physical units."""
from itertools import permutations, product, combinations
from collections import Counter
import json
from pathlib import Path
import sympy as S

V=tuple(range(4)); edges=list(combinations(V,2)); faces=list(combinations(V,3));
matchings=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
x,y,z=S.symbols('x y z'); lam=[1-x-y-z,x,y,z]; variables=(x,y,z)
grad={i:S.Matrix([S.diff(lam[i],u) for u in variables]) for i in V}
W={e:lam[e[0]]*grad[e[1]]-lam[e[1]]*grad[e[0]] for e in edges}
cent={x:S.Rational(1,4),y:S.Rational(1,4),z:S.Rational(1,4)}

def perm_sign(seq):return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
def complement(e):return tuple(v for v in V if v not in e)
def dual1_matrix():
    D=S.zeros(6)
    for j,e in enumerate(edges):D[edges.index(complement(e)),j]=perm_sign(tuple(e)+complement(e))
    return D
D1=dual1_matrix()
assert D1**2==S.eye(6)

def cochain(c):return S.Matrix([c[e] for e in edges])
def from_vec(v):return dict(zip(edges,list(v)))
def field(c,subs=None):
    M=S.Matrix.vstack(*(sum((c[e]*W[e] for e in pair),S.zeros(3,1)).T for pair in matchings))
    return M if subs is None else M.subs(subs)

def signed_edge_perm(g):
    T=S.zeros(6)
    for j,(a,b) in enumerate(edges):
        e=tuple(sorted((g[a],g[b])));T[edges.index(e),j]=1 if g[a]<g[b] else -1
    return T

def matching_perm(g):
    R=S.zeros(3)
    for i,m in enumerate(matchings):
        img={tuple(sorted((g[a],g[b]))) for a,b in m}
        R[[j for j,n in enumerate(matchings) if set(n)==img][0],i]=1
    return R

def jacobian(g):
    inverse={g[i]:i for i in V}
    out=S.Matrix([lam[inverse[i]] for i in (1,2,3)])
    J=out.jacobian(variables)
    assert J.det()==perm_sign(g)
    return out,J

perms=list(permutations(V)); signs=list(product((-1,1),repeat=6));
all_codes={s:dict(zip(edges,s)) for s in signs};
rank_counts=Counter(); ranks={}; orbit_list=[];unseen=set(signs)
for g in perms:
    T=signed_edge_perm(g)
    assert D1*T==perm_sign(g)*T*D1
    assert matching_perm(g).det()==perm_sign(g)
    out,J=jacobian(g)
    g_sub=dict(zip(variables,list(out)))
    # Operator-level covariance at an off-centre rational site with arbitrary nonuniform edge amplitudes
    c0={e:S.Integer(1+idx) for idx,e in enumerate(edges)}
    c1=from_vec(T*cochain(c0))
    point={x:S.Rational(1,7),y:S.Rational(2,7),z:S.Rational(1,7)}
    lhs=field(c1).subs(g_sub, simultaneous=True).subs(point)
    rhs=(matching_perm(g)*field(c0)*J.inv()).subs(point)
    assert lhs==rhs,(g,lhs,rhs)

for key,c in all_codes.items():
    v=cochain(c); E=field(c,cent); r=E.rank();ranks[key]=r;rank_counts[r]+=1
    pair_products=tuple(c[u]*c[v] for u,v in matchings)
    valid=(pair_products==(1,-1,1) or pair_products==(-1,1,-1))
    assert (r==3)==valid,(key,r,pair_products)
    if valid:
        sig=1 if D1*v==v else -1
        assert D1*v==sig*v
        assert S.factor(field(c).det()-S.prod([c[e] for e in ((0,1),(0,2),(0,3))])*sum(l*l for l in lam))==0
    for g in perms:
        v2=signed_edge_perm(g)*v
        k=tuple(v2)
        assert ranks.get(k,r)==r or k not in ranks

while unseen:
    a=min(unseen); c=all_codes[a];O={tuple(signed_edge_perm(g)*cochain(c)) for g in perms};unseen-=O
    assert len(O) in (8,24)
    assert len({ranks[o] for o in O})==1
    det_at_cent=next(iter({field(all_codes[o],cent).det() for o in O}))
    orbit_list.append(dict(representative=list(a),size=len(O),barycenter_rank=ranks[a],determinant_at_barycenter=str(det_at_cent)))
assert rank_counts=={2:48,3:16}
assert sorted(o['size'] for o in orbit_list)==[8,8,24,24]

a,b,d=S.symbols('a b d'); factor=sum(l*l for l in lam)
for eig in (1,-1):
    c={(0,1):a,(2,3):eig*a,(0,2):b,(1,3):-eig*b,(0,3):d,(1,2):eig*d}
    assert D1*cochain(c)==eig*cochain(c)
    assert S.factor(field(c).det()-a*b*d*factor)==0
    assert field(c,cent).det()==a*b*d/4
assert S.factor(factor.subs(cent))==S.Rational(1,4)
# The dual eigensector condition is sufficient, NOT necessary for arbitrary real amplitudes.
perturbed={(0,1):S.Integer(1),(2,3):S.Integer(1),(0,2):S.Integer(1),(1,3):-S.Rational(9,10),(0,3):S.Integer(1),(1,2):S.Integer(1)}
assert D1*cochain(perturbed)!=cochain(perturbed) and D1*cochain(perturbed)!=-cochain(perturbed)
assert S.factor(field(perturbed).det()-factor+S.Rational(1,10)*(x*x+z*z))==0
# Hence det >= (9/10)*sum lambda_i^2 >= 9/40 on the closed simplex.
# Symmetric support/positive latent indicator cannot see edge-sign distinctions.
vertex={i:S.Integer(1) for i in V}
for key,c in all_codes.items():
    latent=[2*abs(c[e])*(abs(vertex[e[0]])+abs(vertex[e[1]])) for e in edges]
    assert latent==[4]*6
    assert sum(c[e]**2 for e in edges)==6
# At any fully S4-invariant oriented-edge cochain, each edge is reversed by a vertex swap: its coefficient vanishes.
F=S.eye(6)
for g in perms:F=F.col_join(signed_edge_perm(g)-S.eye(6))
assert F.nullspace()==[]
# Whitney interpolation commutes with coboundary on C0 -> C1, using B1^T.
u=S.symbols('u0:4'); W0=sum(lam[i]*u[i] for i in V)
coef={(i,j):u[j]-u[i] for i,j in edges}
W1=sum((coef[e]*W[e] for e in edges),S.zeros(3,1))
assert S.simplify(W1-S.Matrix([S.diff(W0,t) for t in variables]))==S.zeros(3,1)
# 2D Riemannian Hodge star on one-forms satisfies star^2=-I, unlike D1^2=I.
assert D1**2==S.eye(6) and D1!=-S.eye(6)
# A positive smooth metric Hodge star_2 cannot be represented by the involutory D1 on all real Whitney 1-forms.

result={
 'version':'v0.1','status':'EXACT_CONDITIONAL/NO_GO_SCOPED',
 'full_S4_elements':24,'sign_patterns':64,'rank_counts_at_barycenter':dict(sorted(rank_counts.items())),
 'sign_orbits':sorted(orbit_list,key=lambda o:(-o['size'],o['representative'])),
 'rank_three_sign_condition':'c01*c23 == c03*c12 == -(c02*c13) == ±1',
 'signed_complement_D1':[[int(D1[i,j]) for j in range(6)] for i in range(6)],
 'D1_square':'I6','D1_S4_relation':'D1*T1(g)=sgn(g)*T1(g)*D1',
 'global_coframe_sufficient_condition':'D1*c=±c; c01*c02*c03 !=0',
 'determinant_formula':'c01*c02*c03 * (lambda0^2+lambda1^2+lambda2^2+lambda3^2)',
 'lower_bound_sum_lambda_squared':'1/4',
 'Whitney0_coboundary':'d W0 = W1 delta0',
 'S4_fixed_signed_edge_vectors_dim':0,
 'same_modulus_support_hidden_sign_patterns':64,
 'Hodge2_square':'-I on real tangent 1-forms; not D1',
 'Hodge3_type':'Omega1 -> Omega2; not Omega1',
 'non_eigen_global_coframe_counterexample':'c13=-9/10 while other c=(1,1,1,1,1) suitably oriented; det=sum(lambda_i^2)-(x^2+z^2)/10 >= 9/40',
 'phase_gauge_sign_law':'NOT_SOURCE_DERIVED',
 'physical_promotion':0
}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('PASS: 64 signs, 24 S4 affine covariance, 4 orbits, dual eigensectors, determinant and Whitney coboundary')
print('RESULT:',json.dumps({'orbits':result['sign_orbits'],'rank_counts':result['rank_counts_at_barycenter']}))
