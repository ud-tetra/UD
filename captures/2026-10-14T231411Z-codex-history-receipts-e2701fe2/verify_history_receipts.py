"""Exact finite-history/reference-kernel checks, independently authored.

Scope: all-open declared Boolean/permutation graph. No native UD event selection
or physical winding is inferred. No imported source code is executed.
"""
from pathlib import Path
from itertools import permutations, product
from collections import Counter, defaultdict
from fractions import Fraction
import json
import sympy as s

root=Path(__file__).resolve().parent
perms=list(permutations(range(3)));ident=(0,1,2)
def parity(g):return sum(g[i]>g[j] for i in range(3) for j in range(i+1,3))%2
def act(g,x):return sum(((x>>i)&1)<<g[i] for i in range(3))
def mul(h,g):return tuple(h[g[i]] for i in range(3))
def inv(g):return tuple(g.index(i) for i in range(3))
def weight(x):return x.bit_count()
def receipt(x,g,a):
    y=act(g,x);z=y if a==-1 else y^(1<<a)
    return (weight(x),weight(z),a,parity(g)),z

edges=[];fibers=defaultdict(list);P=s.zeros(8)
for x,g,a in product(range(8),perms,(-1,0,1,2)):
    q,z=receipt(x,g,a);e=(x,g,a,z,q);edges.append(e);fibers[q].append(e);P[x,z]+=s.Rational(1,24)
assert len(edges)==192 and len(fibers)==44
assert P==P.T and all(sum(P[i,:])==1 for i in range(8))
assert set(len(v) for v in fibers.values())=={3,6,9}
assert Counter(len(v) for v in fibers.values())=={3:28,6:12,9:4}
# A null-distinguished contract separates (identity frame, no flip) from active
# fixed-weight events. It has 44 active labels and one null symbol, not 44 total.
def flagged(e):return None if e[1]==ident and e[2]==-1 else e[4]
flagged_fibers=defaultdict(list)
for e in edges:flagged_fibers[flagged(e)].append(e)
assert len(flagged_fibers)==45 and len(flagged_fibers[None])==8
assert Counter(len(v) for q,v in flagged_fibers.items() if q is not None)=={2:2,3:26,6:14,9:2}
# Null conflation is a coarsening of words conditional on known initial weight.
# It is not a map on the 45 standalone symbols: null itself omits that weight.
assert len({e[4] for e in flagged_fibers[None]})==4
for x in range(8):
    first=[e for e in edges if e[0]==x]
    for e1 in first:
        for e2 in (e for e in edges if e[0]==e1[3]):
            w=weight(x);decoded=[]
            for event in (e1,e2):
                q=flagged(event)
                decoded.append((w,w,-1,0) if q is None else q)
                if q is not None:w=q[1]
            assert decoded==[e1[4],e2[4]]
Q=s.zeros(4)
for w in range(4):
    x=next(x for x in range(8) if weight(x)==w)
    for z in range(8):Q[w,weight(z)]+=P[x,z]
    for y in range(8):
        if weight(y)==w:
            assert all(sum(P[y,z] for z in range(8) if weight(z)==v)==Q[w,v] for v in range(4))
pi=s.Matrix([[s.Rational(1,8),s.Rational(3,8),s.Rational(3,8),s.Rational(1,8)]])
assert pi*Q==pi and Q.charpoly().as_expr().factor()==(s.Symbol('lambda')-1)*s.Symbol('lambda')*(2*s.Symbol('lambda')-1)*(2*s.Symbol('lambda')+1)/4
# A fixed initial state can lift every compatible receipt at that weight.
for x in range(8):
    attainable={e[4] for e in edges if e[0]==x}
    assert attainable=={q for q in fibers if q[0]==weight(x)}
    active={flagged(e) for e in edges if e[0]==x and flagged(e) is not None}
    assert active=={q for q in flagged_fibers if q is not None and q[0]==weight(x)}
# Concrete nonuniform positive stationary law, realized without changing support.
target=s.Matrix([[s.Rational(1,4)]*4]);flux=[s.Rational(1,32)]*3
bs=[flux[w]/target[w] if w<3 else s.Rational(0) for w in range(4)]
ds=[flux[w-1]/target[w] if w>0 else s.Rational(0) for w in range(4)]
Pc=s.zeros(8)
for x,g,a,z,q in edges:
    w=weight(x);y=act(g,x)
    k=(1-bs[w]-ds[w]) if a==-1 else (bs[w]/(3-w) if not ((y>>a)&1) else ds[w]/w)
    Pc[x,z]+=k/6
pi_fine=s.Matrix([[target[weight(x)]/s.binomial(3,weight(x)) for x in range(8)]])
assert all(sum(Pc[i,:])==1 for i in range(8)) and pi_fine*Pc==pi_fine

# Oriented graph-cycle counterexample: a chosen additive edge functional.
cycle=(1,2,0);reverse=inv(cycle)
def omega(e):
    x,g,a,z,q=e
    if x==0 and a==-1:return 1 if g==cycle else (-1 if g==reverse else 0)
    return 0
index={(e[0],e[1],e[2]):e for e in edges}
for e in edges:
    x,g,a,z,q=e;ar=-1 if a==-1 else inv(g)[a]
    assert omega(index[(z,inv(g),ar)])==-omega(e)
q0=(0,0,-1,0);values={omega(e) for e in fibers[q0]}
assert values=={-1,0,1} and len(fibers[q0])==3
assert {omega(e) for e in flagged_fibers[q0]}=={-1,1}
# Exact finite-horizon attainable winding counts/distributions on one receipt word.
hist={0:1};horizon=[]
for N in range(1,13):
    new=Counter()
    for w,count in hist.items():
        for step in (-1,0,1):new[w+step]+=count
    hist=dict(new)
    assert set(hist)==set(range(-N,N+1)) and sum(hist.values())==3**N
    horizon.append({'N':N,'winding_values':len(hist),'required_fixed_length_bits':(2*N).bit_length(),'conditional_distribution_numerators':{str(w):v for w,v in sorted(hist.items())},'denominator':3**N})
hist={0:1};flagged_horizon=[]
for N in range(1,13):
    new=Counter()
    for w,count in hist.items():
        for step in (-1,1):new[w+step]+=count
    hist=dict(new)
    assert set(hist)==set(range(-N,N+1,2)) and sum(hist.values())==2**N
    flagged_horizon.append({'N':N,'winding_values':len(hist),'required_fixed_length_bits':N.bit_length(),'conditional_distribution_numerators':{str(w):v for w,v in sorted(hist.items())},'denominator':2**N})

# Linear exact certificate for the scalar/frame-consistent no-loop theorem.
# Unknowns f(x,g) (48 frame increments) and t(x,a) (24 flip increments).
fkeys=[(x,g) for x in range(8) for g in perms];tkeys=list(product(range(8),range(3)))
fi={k:i for i,k in enumerate(fkeys)};ti={k:48+i for i,k in enumerate(tkeys)}
rows=set()
def row(terms):
    v=[0]*72
    for i,c in terms:v[i]+=c
    if any(v):rows.add(tuple(v))
for x,g,h in product(range(8),perms,perms):
    # Frame composition f(x,hg)=f(x,g)+f(gx,h).
    row([(fi[x,mul(h,g)],1),(fi[x,g],-1),(fi[act(g,x),h],-1)])
    row([(fi[act(h,x),mul(mul(h,g),inv(h))],1),(fi[x,g],-1)])
for x,a in tkeys:
    row([(ti[x,a],1),(ti[x^(1<<a),a],1)])
    for h in perms:row([(ti[act(h,x),h[a]],1),(ti[x,a],-1)])
M=s.Matrix(sorted(rows));rref,pivots=M.rref();rank=len(pivots)
assert rank==69
basis=s.zeros(72,3)
for x,a in tkeys:
    w=weight(x);up=not((x>>a)&1);basis[ti[x,a],w if up else w-1]=1 if up else -1
assert M*basis==s.zeros(M.rows,3) and basis.rank()==3
for e in edges:
    x,g,a,z,q=e
    for j in range(3):
        value=0 if a==-1 else basis[ti[act(g,x),a],j]
        F=lambda w:1 if w>j else 0
        assert value==F(weight(z))-F(weight(x))

# Quadratic burden depends on initial winding; cost alone has sign degeneracies.
N=4;kappa=s.Rational(3,2)
assert [kappa*((0+w)**2-0) for w in range(-N,N+1)]==[kappa*w*w for w in range(-N,N+1)]
assert kappa*((1+1)**2-1)==3*kappa

cert={'rows':M.rows,'columns':72,'rank':rank,'nullity':72-rank,'pivot_columns':list(pivots),'unknown_order':{'frame':[[x,list(g)] for x,g in fkeys],'flip':[list(t) for t in tkeys]},'constraint_rows':M.tolist(),'nullspace_basis':basis.tolist()}
(root/'SCALAR_WINDING_CERTIFICATE.json').write_text(json.dumps(cert,indent=2,default=int)+'\n')
checks={'status':'PASS','lane':'development - no registry entry','physical_promotion':0,'independent_review':False,
 'fine_graph':{'states':8,'action_distinct_edges':192,'actions_per_state':24,'active_receipts':44,'null_symbols':1,'null_distinguished_receipts_total':45,'active_receipt_fiber_histogram':dict(Counter(len(v) for q,v in flagged_fibers.items() if q is not None)),'null_fiber_size':8,'unflagged_codes':44,'null_conflation_is_word_coarsening_given_initial_weight':True,'unflagged_fiber_histogram':dict(Counter(len(v) for v in fibers.values())),'same_initial_weight_all_active_receipts_lift':True,'scope':'all-open declared permutation/one-bit graph, not native move admission'},
 'reference_kernel':{'fine_rows_sum_one':True,'fine_symmetric':True,'coarse_matrix':[[str(v) for v in Q.row(i)] for i in range(4)],'coarse_stationary':[str(v) for v in pi],'coarse_eigenvalues':['1','1/2','0','-1/2'],'alternative_stationary_target':[str(v) for v in target],'alternative_up_probabilities':[str(v) for v in bs],'alternative_down_probabilities':[str(v) for v in ds],'native_rate_selection':False},
 'winding_counterexample':{'receipt':q0,'same_initial_and_final_state':0,'one_step_hidden_values_null_distinguished':[-1,1],'one_step_hidden_values_unflagged':sorted(values),'reverse_antisymmetry':True,'frame_composition_compatibility':False,'full_S3_scalar_covariance':False,'finite_horizons_null_distinguished':flagged_horizon,'finite_horizons_unflagged':horizon,'resource_bound_null_distinguished':'N+1 supplemental symbols, ceil(log2(N+1)) fixed-length bits for exact total winding on this repeated active receipt word','resource_bound_unflagged':'2N+1 supplemental symbols, ceil(log2(2N+1)) fixed-length bits when the same code also hides null events'},
 'scalar_no_loop':{'unknowns':72,'constraint_rows':M.rows,'exact_rank':rank,'nullity':3,'basis':'three Hamming-shell potential differences','hypotheses':['real scalar increments','frame composition cocycle','full S3 scalar covariance','flip reversal antisymmetry','composite event equals frame then flip'],'conclusion':'W=F(w_final)-F(w_initial); closed histories have zero W'},
 'not_derived':['native admission masks and rates','physical winding interpretation','burden scale kappa','physical event time','apparatus acquisition, energy and area costs']}
(root/'HISTORY_RECEIPT_CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps({k:v for k,v in checks.items() if k!='winding_counterexample'},indent=2))
