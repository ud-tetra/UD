"""Independent constructor check of a declared C10 action on the 600-cell boundary.

Coordinates use (a,b) for a+b*phi, with phi**2=phi+1. Actual vertex
coordinates are half the stored coordinates. All combinatorial tests are exact.
"""
from pathlib import Path
from itertools import permutations, product, combinations
from collections import Counter
import json
import numpy as np
import scipy.sparse as sp
import sympy as sy

R=Path(__file__).resolve().parent
checks=[]
def check(name,yes,**data):
    assert yes,name
    checks.append(dict(name=name,status='PASS',**data))
z=(0,0); one=(1,0); two=(2,0); ph=(0,1); inv=(-1,1)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):
    x,y=a;u,v=b
    return (x*u+y*v,x*v+y*u+y*v)
def total(xs):
    r=z
    for x in xs:r=add(r,x)
    return r
def parity(v):return -1 if sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))%2 else 1
verts=set()
for i in range(4):
    for sign in [-1,1]:
        v=[z]*4;v[i]=(2*sign,0);verts.add(tuple(v))
for signs in product([-1,1],repeat=4):verts.add(tuple((t,0) for t in signs))
even=[p for p in permutations(range(4)) if parity(p)==1]
for signs in product([-1,1],repeat=3):
    base=(z,tuple(signs[0]*a for a in one),tuple(signs[1]*a for a in ph),tuple(signs[2]*a for a in inv))
    for p in even:verts.add(tuple(base[i] for i in p))
verts=sorted(verts);index={v:i for i,v in enumerate(verts)}
check('exact_vertices_unit_norm',len(verts)==120 and all(total(mul(a,a) for a in v)==(4,0) for v in verts))
adj=[set() for _ in verts]
for i,j in combinations(range(120),2):
    if total(mul(a,b) for a,b in zip(verts[i],verts[j]))==(0,2):adj[i].add(j);adj[j].add(i)
check('nearest_neighbor_graph',all(len(n)==12 for n in adj) and sum(map(len,adj))//2==720)
cells=[[(i,) for i in range(120)]]
for k in range(1,4):
    nxt=[]
    for c in cells[-1]:
        common=set.intersection(*(adj[i] for i in c))
        nxt += [c+(j,) for j in sorted(common) if j>c[-1]]
    cells.append(nxt)
check('boundary_f_vector',[len(c) for c in cells]==[120,720,1200,600])
check('tetrahedra_maximal',all(not set.intersection(*(adj[i] for i in c)) for c in cells[3]))
face_use=Counter(f for c in cells[3] for f in combinations(c,3))
edge_use=Counter(e for c in cells[3] for e in combinations(c,2))
check('closed_face_and_edge_incidence',set(face_use.values())=={2} and set(edge_use.values())=={5})
def qmul(v,w):
    out=[add(mul(v[0],w[0]),neg(total(mul(v[i],w[i]) for i in range(1,4))))]
    for i,j,k in [(1,2,3),(2,3,1),(3,1,2)]:
        out.append(total([mul(v[0],w[i]),mul(v[i],w[0]),mul(v[j],w[k]),neg(mul(v[k],w[j]))]))
    assert all(a%2==b%2==0 for a,b in out)
    return tuple((a//2,b//2) for a,b in out)
check('quaternion_vertex_set_closed',all(qmul(v,w) in index for v in verts for w in verts))
g=next(v for v in verts if v[0]==ph)
vp=[index[qmul(v,g)] for v in verts]
powers=[tuple(range(120))]
for _ in range(10):powers.append(tuple(vp[i] for i in powers[-1]))
check('right_multiplication_order_ten',len(set(powers[:-1]))==10 and powers[-1]==powers[0],generator_twice_coordinates=g)
check('fifth_power_antipodal',all(verts[powers[5][i]]==tuple(neg(a) for a in verts[i]) for i in range(120)))
qconj=lambda v:(v[0],)+tuple(neg(a) for a in v[1:])
hopf=[qmul(qmul(v,g),qconj(v)) for v in verts]
base=sorted(set(hopf));basecounts=Counter(hopf)
check('hopf_conjugacy_base_twelve_fibers',len(base)==12 and set(basecounts.values())=={10} and all(hopf[vp[i]]==hopf[i] for i in range(120)))
baseadj=[sum(total(mul(a,b) for a,b in zip(v,w))==(0,2) for w in base if w!=v) for v in base]
check('hopf_base_icosahedral_graph',baseadj==[5]*12)
ids=[{c:i for i,c in enumerate(cs)} for cs in cells]
actions=[]
orbits=[]
for d,cs in enumerate(cells):
    images=[tuple(vp[v] for v in c) for c in cs]
    dest=[ids[d][tuple(sorted(c))] for c in images]
    signs=[parity(c) for c in images]
    T=sp.csc_matrix((signs,(dest,range(len(cs)))),shape=(len(cs),len(cs)),dtype=np.int64)
    actions.append(T)
    seen=set();oo=[]
    for i in range(len(cs)):
        if i in seen:continue
        o=[];j=i;sgn=1
        while j not in o:o.append(j);sgn*=signs[j];j=dest[j]
        assert j==i and len(o)==10 and sgn==1
        oo.append(o);seen.update(o)
    orbits.append(oo)
check('all_simplex_orbits_free',[len(o) for o in orbits]==[12,72,120,60])
B=[]
for d in range(1,4):
    rows=[];cols=[];data=[]
    for i,c in enumerate(cells[d]):
        for k in range(d+1):rows.append(ids[d-1][c[:k]+c[k+1:]]);cols.append(i);data.append((-1)**k)
    B.append(sp.csc_matrix((data,(rows,cols)),shape=(len(cells[d-1]),len(cells[d])),dtype=np.int64))
check('boundary_squared_zero',all((B[j]*B[j+1]).nnz==0 for j in range(2)))
check('signed_chain_equivariance',all((actions[d-1]*B[d-1]-B[d-1]*actions[d]).nnz==0 for d in range(1,4)))
A=sp.bmat([[None,-B[0],None,None],[B[0].T,None,-B[1],None],[None,B[1].T,None,-B[2]],[None,None,B[2].T,None]],format='csc')
T=sp.block_diag(actions,format='csc')
check('full_skew_generator_commutes',A.shape==(2640,2640) and (A+A.T).nnz==0 and (A*T-T*A).nnz==0)
check('each_degree_exchange_commutes',all((actions[d-1]*B[d-1]-B[d-1]*actions[d]).nnz==0 for d in range(1,4)))
# Exact cyclic character traces; no floating Fourier ranks used.
traces=[];power=sp.eye(2640,dtype=np.int64,format='csc')
for r in range(10):traces.append(int(power.diagonal().sum()));power=power*T
check('regular_character_from_free_action',traces==[2640]+[0]*9 and (power-sp.eye(2640)).nnz==0)
check('character_sector_dimensions',2640//10==264 and [len(c)//10 for c in cells]==[12,72,120,60])
# A Fourier sector is a character, not a spatial fiber. Average a vertex fiber,
# then one incidence action produces a nonzero edge vector.
vv=np.zeros(120,dtype=np.int64);vv[orbits[0][0]]=1
check('individual_spatial_fiber_not_full_chain_invariant',np.count_nonzero(B[0].T@vv)>0)
# Lift a consistent orientation from adjacency; this also checks connected dual graph.
fmap={}
for cidx,c in enumerate(cells[3]):
    for k in range(4):fmap.setdefault(c[:k]+c[k+1:],[]).append((cidx,(-1)**k))
orient={0:1};todo=[0]
while todo:
    cidx=todo.pop();c=cells[3][cidx]
    for k in range(4):
        f=c[:k]+c[k+1:];(a,sa),(b,sb)=fmap[f]
        other,signother=(b,sb) if a==cidx else (a,sa)
        val=-orient[cidx]*((-1)**k)*signother
        if other in orient:assert orient[other]==val
        else:orient[other]=val;todo.append(other)
fund=np.array([orient[i] for i in range(600)],dtype=np.int64)
check('fundamental_cycle_and_dual_connectivity',len(orient)==600 and np.count_nonzero(B[2]@fund)==0)
check('both_harmonic_witnesses_in_trivial_sector',np.array_equal(actions[3]@fund,fund) and np.array_equal(actions[0]@np.ones(120,dtype=np.int64),np.ones(120,dtype=np.int64)))
# Exact rank certificate modulo a prime, bounded above over Q by incidence and cycle.
def rank_mod(M,p=1009):
    rows=[]
    for row in M.tocsr():rows.append({int(j):int(v)%p for j,v in zip(row.indices,row.data) if int(v)%p})
    piv={}
    for row in rows:
        while row:
            k=min(row)
            if k not in piv:
                invv=pow(row[k],-1,p);piv[k]={j:(v*invv)%p for j,v in row.items()};break
            q=row[k]
            for j,v in piv[k].items():
                new=(row.get(j,0)-q*v)%p
                if new:row[j]=new
                elif j in row:del row[j]
    return len(piv)
ranks=[rank_mod(m) for m in B]
check('exact_boundary_ranks_by_modular_lower_and_chain_upper',ranks==[119,601,599],prime=1009,modular_ranks=ranks)
check('betti_and_total_generator_rank',[len(cells[d])-(ranks[d-1] if d else 0)-(ranks[d] if d<3 else 0) for d in range(4)]==[1,0,0,1] and 2*sum(ranks)==2638)
# Small exact pentachoron control under the same unit-incidence convention.
def simple_generator(filled=True):
    cs=[list(combinations(range(5),k)) for k in range(1,6 if filled else 5)]
    dims=[len(c) for c in cs];offs=[sum(dims[:i]) for i in range(len(cs))];Q=sy.zeros(sum(dims))
    for d in range(1,len(cs)):
        for j,c in enumerate(cs[d]):
            for k in range(d+1):
                i=cs[d-1].index(c[:k]+c[k+1:]);a,b=offs[d-1]+i,offs[d]+j
                Q[a,b]=-(-1)**k;Q[b,a]=(-1)**k
    return Q
u=sy.symbols('u');Af=simple_generator(True);Ab=simple_generator(False)
check('pentachoron_filled_and_boundary_spectra',sy.expand(Af.charpoly(u).as_expr()-u*(u*u+5)**15)==0 and sy.expand(Ab.charpoly(u).as_expr()-u*u*(u*u+5)**14)==0)
# Full unnormalized spectrum cannot be 1->4 invariant: the state dimension changes.
subdivision=[tuple(sorted((4,)+tuple(i for i in range(4) if i!=j))) for j in range(4)]
subcounts=[len({f for c in subdivision for f in combinations(c,k)}) for k in range(1,5)]
check('three_dimensional_one_to_four_count_change',subcounts==[5,10,10,4] and sum(subcounts)==29)
cert={'status':'PASS','physical_promotion':0,'independent_review':False,'check_families':len(checks),'checks':checks,'f_vector':[len(c) for c in cells],'boundary_ranks':ranks,'betti':[1,0,0,1],'A_rank':2638,'character_dimensions':[264]*10,'per_degree_character_dimensions':[12,72,120,60],'real_invariant_dimensions':[264,264,528,528,528,528],'generator_twice_coordinates':g,'orbit_counts':[len(o) for o in orbits],'trace_T_powers':traces,'scope':'Exact Q(phi) vertices and integer chain/symmetry tests; Fourier projector identities proved in report; no full 600-cell eigenvalue list, gauge identification or RG calculation.'}
(R/'HOPF_SECTOR_CHECKS.json').write_text(json.dumps(cert,indent=2)+'\n')
(R/'COMPLEX_AND_ACTION.json').write_text(json.dumps({'vertex_field':'actual coordinate = (a+b phi)/2, phi^2=phi+1','vertices':verts,'simplices':cells,'right_generator':g,'vertex_permutation':vp,'signed_simplex_permutations':[[{'destination':int(T.indices[T.indptr[j]]),'sign':int(T.data[T.indptr[j]])} for j in range(T.shape[1])] for T in actions]},separators=(',',':'))+'\n')
print(json.dumps({k:cert[k] for k in ['status','check_families','f_vector','boundary_ranks','betti','character_dimensions']}))
