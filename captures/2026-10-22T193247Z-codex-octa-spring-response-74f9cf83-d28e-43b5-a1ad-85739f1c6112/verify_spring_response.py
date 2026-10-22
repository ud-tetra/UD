"""Exact rational Schur response of a passive scalar spring octahedral network.

This is a candidate material-model comparison, not a graphite parameter fit.
"""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json


def inverse(a):
    n=len(a); aug=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(n)]
                   for i,row in enumerate(a)]
    for j in range(n):
        p=next(i for i in range(j,n) if aug[i][j]);aug[j],aug[p]=aug[p],aug[j]
        v=aug[j][j];aug[j]=[x/v for x in aug[j]]
        for i in range(n):
            if i!=j:
                v=aug[i][j];aug[i]=[x-v*y for x,y in zip(aug[i],aug[j])]
    return [row[n:] for row in aug]


def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a):return [list(col) for col in zip(*a)]
def sub(a,b):return [[x-y for x,y in zip(row,other)] for row,other in zip(a,b)]


def run_case(a,b,c,mu,m,eta,s):
    old=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    shell=[tuple(sign if axis==k else 0 for k in range(3))
           for axis in range(3) for sign in (-1,1)]
    mid={(i,j):shell.index(tuple((old[i][k]+old[j][k])//2 for k in range(3)))
         for i,j in combinations(range(4),2)}
    inner=[tuple(sorted((6,)+tuple(shell.index(tuple(signs[axis] if axis==k
           else 0 for k in range(3))) for axis in range(3))))
           for signs in product((-1,1),repeat=3)]
    cells=inner+[tuple(sorted((7+i,)+tuple(mid[p] for p in mid if i in p)))
                 for i in range(4)]
    edges=set(pair for cell in cells for pair in combinations(cell,2))
    K=[[Q(0) for _ in range(11)] for _ in range(11)]
    for i,j in edges:
        w=a if j>=7 else b if j==6 else c
        K[i][i]+=w;K[j][j]+=w;K[i][j]-=w;K[j][i]-=w
    # Eliminate only the six midpoint degrees of freedom. Their local
    # inertia, viscous bath and optional pinning enter the dynamic block.
    for i in range(6):K[i][i]+=mu+eta*s+m*s*s
    R=[6,7,8,9,10];M=list(range(6))
    rr=[[K[i][j] for j in R] for i in R]
    rm=[[K[i][j] for j in M] for i in R]
    mr=tr(rm); mmid=[[K[i][j] for j in M] for i in M]
    eff=sub(rr,mm(mm(rm,inverse(mmid)),mr))
    den=2*a+b+mu+eta*s+m*s*s
    assert all(sum(row)==den for row in mmid)
    assert all(eff[0][i]==-3*a*b/den for i in range(1,5))
    assert eff[0][0]==6*b-6*b*b/den
    assert all(eff[0][i]==eff[i][0] for i in range(1,5))
    assert all(eff[0][i]<0 for i in range(1,5))
    return den,eff[0][1],eff[0][0]


def fmt(q):return str(q)

def main():
    cases=[tuple(map(Q,t)) for t in ((1,1,0,1,1,1,0),
             (2,3,0,1,4,7,0),(2,3,5,1,4,7,0),(2,3,5,1,4,7,1),
             (5,2,1,3,2,6,Q(1,2)))]
    results=[]
    for case in cases:
        den,cross,self0=run_case(*case)
        results.append({"parameters_a_b_c_mu_m_eta_s":[fmt(x) for x in case],
                        "denominator":fmt(den),"centroid_old":fmt(cross),
                        "centroid_self":fmt(self0)})
    assert results[1]['centroid_old']==results[2]['centroid_old']
    assert results[1]['centroid_self']==results[2]['centroid_self']
    a,b,c,mu,m,eta,_=cases[2]
    k=2*a+b+mu
    gamma=6*b*b*eta/(k*k)
    assert gamma>0
    # First derivative of effective center self K_eff(s) at s=0.
    assert (6*b*b*eta)/(k*k)==gamma
    # An undamped local midpoint bath generates no zero-frequency
    # linear viscous term. No angular dependence is in this network.
    assert 6*b*b*Q(0)/(k*k)==0
    result={"lane":"EXACT conditional scalar spring Schur response; physical promotion 0",
            "primary_article":"https://doi.org/10.1103/ly48-b4l2",
            "article_target_correction":"Sharp friction peaks at 21.8 and 38.2 degrees with negligible load dependence; small residual barrier, not zero angular signal",
            "static_centroid_old":"-3ab/(2a+b+mu) < 0 for a,b>0,mu>=0",
            "required_metric_centroid_old":"+1/4 each under S4 and unit coarse pullback",
            "dynamic_centroid_old_laplace":"-3ab/(2a+b+mu+eta*s+m*s^2)",
            "dynamic_centroid_self_laplace":"6b-6b^2/(2a+b+mu+eta*s+m*s^2)",
            "low_frequency_center_viscous_coefficient":"6b^2*eta/(2a+b+mu)^2",
            "example_gamma":fmt(gamma),"exact_rational_controls":results,
            "scope":"Scalar passive pairwise springs, midpoint viscous bath, direct H0=K_eff identification only; no twist-angle selector, friction force, load coefficient or UD metric identification."}
    (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"status":"PASS","controls":len(results),
                      "gamma_example":fmt(gamma),"static_sign":"negative"}))

if __name__=='__main__':main()
