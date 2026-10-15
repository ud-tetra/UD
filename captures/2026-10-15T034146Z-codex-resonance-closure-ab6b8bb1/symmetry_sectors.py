"""Exact signed simplex and ordinary link actions of tetrahedral relabelings."""
from itertools import permutations
import sympy as s
from mode_model import graph,reduction

def actions(g,p):
    n=len(g['simplices']);m=len(g['edges']);rho=s.zeros(n);node=s.zeros(n);link=s.zeros(m)
    mapping=[]
    for j,t in enumerate(g['simplices']):
        v=[p[x] for x in t];i=g['simplices'].index(tuple(sorted(v)))
        sg=(-1)**sum(v[a]>v[b] for a in range(len(v)) for b in range(a+1,len(v)))
        rho[i,j]=sg;node[i,j]=1;mapping.append(i)
    for e,(i,j) in enumerate(g['edges']):link[g['edges'].index((mapping[i],mapping[j])),e]=1
    return rho,node,link

def sectors(g):
    Lp,PT,P0=reduction(g)
    groups={'S3_vertex_stabilizer':[(0,)+p for p in permutations((1,2,3))],
            'C4_vertex_cycle':[tuple((j+k)%4 for j in range(4)) for k in range(4)]}
    result={}
    for name,group in groups.items():
        acts=[actions(g,p) for p in group]
        matter=sum((q[0] for q in acts),s.zeros(15))/len(group)
        nodes=sum((q[1] for q in acts),s.zeros(15))/len(group)
        links=sum((q[2] for q in acts),s.zeros(28))/len(group)
        W=PT*links
        basis=s.Matrix.hstack(*W.columnspace())
        gram=basis.T*basis;left=gram.inv()*basis.T;small=left*g['K']*basis
        d=s.zeros(15,1)
        if name.startswith('S3'):
            d[4:10,:]=s.Matrix([1,1,1,0,0,0])
        else:d[4:10,:]=s.Matrix([1,0,-1,1,0,1])
        result[name]={'group':group,'actions':acts,'matter':matter,'nodes':nodes,'links':links,
                     'cycle':W,'basis':basis,'left':left,'small_K':small,'seed_D':d}
    return result

def embedded_resolvent(sector,t,frequency_squared):
    F=sector['small_K'];Z=sector['basis']
    return Z*(t*F-frequency_squared*s.eye(F.rows)).inv()*sector['left']
