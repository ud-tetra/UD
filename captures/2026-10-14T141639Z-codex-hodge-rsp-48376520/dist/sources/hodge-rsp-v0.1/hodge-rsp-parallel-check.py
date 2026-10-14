"""Finite factor audit and exact K4 witness; constructor-team AI verification only."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib, importlib.util, itertools, json, sys, time

SITE=Path(sys.argv[1] if len(sys.argv)>1 else '/workspace/sites/unified-dynamics-public').resolve()
OUT=Path(sys.argv[2] if len(sys.argv)>2 else '/workspace/scratch/384298a218b5/hodge-rsp-parallel-results.json').resolve()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
input_hashes={name:sha(SITE/name) for name in ['rsp1.py','response_contract.py']}
sys.path.insert(0,str(SITE))
spec=importlib.util.spec_from_file_location('rsp1_factor_actual',SITE/'rsp1.py')
rsp=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rsp;spec.loader.exec_module(rsp)
started=time.monotonic()

def orbit(F,x):
    path=[]
    while x not in path:path.append(x);x=F[x]
    return path,path[path.index(x):]

generic_maps=generic_factor_tests=exact_factors=0
generic_by_size={}
for n in range(1,5):
    good=0
    for F in itertools.product(range(n),repeat=n):
        paths=[orbit(F,x) for x in range(n)]
        if any(len(cycle)!=1 for path,cycle in paths):continue
        good+=1;generic_maps+=1
        # Hitting distance is an independent strict potential for these acyclic maps.
        V=[len(path)-1 for path,cycle in paths]
        assert all(F[x]==x or V[F[x]]<V[x] for x in range(n))
        for m in range(1,5):
            for U in itertools.permutations(range(m)):
                for phi in itertools.product(range(n),repeat=m):
                    generic_factor_tests+=1
                    if all(phi[U[x]]==F[phi[x]] for x in range(m)):
                        exact_factors+=1
                        assert all(F[y]==y for y in phi)
                        image=set(phi)
                        assert image=={F[y] for y in image}
    generic_by_size[n]=good

T=(1,0,0);bank=((1,0,0),(0,0,0));states=[]
for L in itertools.product((0,1),repeat=3):
    for q in itertools.product((0,1),repeat=3):
        if any(t*l>v or v>t for t,l,v in zip(T,L,q)):continue
        for r0 in range(2):
            for cursor in range(3):
                for branch in 'CH':states.append(rsp.State(T,L,q,(r0,0,0),bank,cursor,branch))
domain=set(states);successors={s:rsp.transition(s)['state'] for s in states}
assert set(successors.values())<=domain
max_settling=0;fixed=0
for s in states:
    path=[];x=s
    while x not in path:
        path.append(x);y=successors[x]
        if y!=x:assert rsp.potential(y)<rsp.potential(x)
        x=y
    cycle=path[path.index(x):]
    assert len(cycle)==1
    max_settling=max(max_settling,len(path)-1)
    if successors[s]==s:fixed+=1

# Build the filled tetrahedron's oriented incidence matrices from ordered simplices.
chains=[list(itertools.combinations(range(4),k+1)) for k in range(4)]
boundaries=[]
for k in range(1,4):
    B=[[Q(0) for column in chains[k]] for row in chains[k-1]]
    for j,simplex in enumerate(chains[k]):
        for omitted in range(k+1):
            face=simplex[:omitted]+simplex[omitted+1:]
            B[chains[k-1].index(face)][j]=Q((-1)**omitted)
    boundaries.append(B)
offsets=[0,4,10,14];A=[[Q(0) for _ in range(15)] for _ in range(15)]
for k,B in enumerate(boundaries,1):
    for i,row in enumerate(B):
        for j,value in enumerate(row):
            A[offsets[k-1]+i][offsets[k]+j]=-value
            A[offsets[k]+j][offsets[k-1]+i]=value
def mv(M,x):return tuple(sum(a*b for a,b in zip(row,x)) for row in M)
def scaled(c,x):return tuple(c*v for v in x)
v=tuple(map(Q,(1,-1,0,0)+(0,)*11))
u=scaled(Q(1,2),mv(A,v))
assert mv(A,v)==scaled(2,u) and mv(A,u)==scaled(-2,v)
assert all(A[i][j]==-A[j][i] for i in range(15) for j in range(15))
quarter_orbit=[v,u,scaled(-1,v),scaled(-1,u)]
assert len(set(quarter_orbit))==4
norms=[sum(a*a for a in x) for x in quarter_orbit]
assert norms==[Q(2)]*4

window_results={}
for branch in 'CH':
    s0=rsp.State(T,(0,0,0),(0,0,0),(1,0,0),branch=branch)
    s1=rsp.transition(s0)['state'];s2=rsp.transition(s1)['state']
    assert rsp.transition(s2)['state']==s2 and s0!=s2
    decode={quarter_orbit[0]:s0,quarter_orbit[1]:s1,quarter_orbit[2]:s2,quarter_orbit[3]:s2}
    equality=[decode[quarter_orbit[(i+1)%4]]==rsp.transition(decode[quarter_orbit[i]])['state'] for i in range(4)]
    assert equality==[True,True,True,False]
    window_results[branch]={'sample_delta_internal':'pi/4','native_period_steps':4,'intertwining_each_step':equality,'first_mismatch':'wrap from -u back to v','native_squared_norm':[str(a) for a in norms],'decoded_stock':[rsp.available_stock(decode[x]) for x in quarter_orbit],'initial_source_state':str(s0),'fixed_source_state':str(s2)}

# A rational circle rotation of infinite order: cos(alpha)=3/5, sin(alpha)=4/5.
# No positive power equals 1 (rational root-of-unity cosine restriction); the
# positivity example is illustrative and does not establish global native RSP decoding.
x,y=Q(1),Q(0);positive_tests=0;closest=None
for n in range(1,121):
    x,y=Q(3,5)*x-Q(4,5)*y,Q(4,5)*x+Q(3,5)*y
    witness=x*x*y*y
    assert witness>0
    positive_tests+=1
    distance=(x-1)**2+y*y
    if closest is None or distance<closest[1]:closest=(n,distance)
assert closest[1]<Q(1,100)

# Anti-overclaim witness: unbounded preparations destroy uniform finite settling.
# U(n)=n+1 is onto Z; F(k)=max(k-1,0); phi(n)=max(-n,0).
for n in range(-100,101):
    assert max(-(n+1),0)==max(max(-n,0)-1,0)
assert max(-(-1),0)==1

assert all(sha(SITE/name)==digest for name,digest in input_hashes.items())
report={
 'status':'PASS','physical_promotion':0,
 'scope':'Constructor-team AI mathematical verification. No native law recovered, no physical correspondence, no independent external review or registry promotion.',
 'input_hashes':input_hashes,'checker_sha256':sha(__file__),
 'formal_claims':{
  'surjective_factor':'For finite strict-descent F and surjective U on invariant D, exact state-only phi U=F phi gives Y=phi(D)=F(Y)=F^N(Y) subset FixF. No decoder regularity required.',
  'finite_order':'If U^m=id, intertwining implies F^m phi(x)=phi(x); strict descent excludes nonfixed periodic factors.',
  'recurrent_robust':'If U^{n_j}x returns to x with arbitrarily large n_j and phi(U^{n_j}x)=phi(x), eventual settling forces phi(x) fixed. Local constancy on a relative neighborhood suffices.',
  'continuity_limit':'Recurrence alone is insufficient on one-sided forward domains. Exact-zero positivity can differ at all sufficiently close nonzero return phases. This does not evade the surjective-domain obstruction.',
  'window_limit':'A finite window of distinct frequency-2 phase states can carry a prepared lookup of any finite candidate trajectory. Wrap or recurrent robust extension remains obstructed; no norm-token identification follows.'},
 'unbounded_preparation_counterexample':{'native_map':'U(n)=n+1 on Z','source_map':'F(k)=max(k-1,0) on nonnegative integers','decoder':'phi(n)=max(-n,0)','exact_intertwining':'For every integer n; checked n=-100..100 and immediate piecewise identity','nonfixed_image_witness':'phi(-1)=1','limit':'The surjective theorem needs finite fixed preparation or uniform finite settling. Strict integer descent alone across unbounded resources does not suffice.'},
 'generic_finite_factor_checks':{'strict_descent_maps':generic_maps,'maps_by_carrier_size':generic_by_size,'surjective_permutation_decoder_tests':generic_factor_tests,'exact_factors_all_fixed':exact_factors},
 'actual_rsp_prepared_graph':{'states':len(states),'fixed_states':fixed,'maximum_settling_updates':max_settling,'cycles':'fixed points only','integrity':list(T),'bank':list(bank),'stocks':'0 or1 on the sole intact seat','cursor':'0..2','branches':['C','H']},
 'exact_k4_frequency_plane':{'chain_dimensions':[4,6,4,1],'vector_v':[str(a) for a in v],'vector_u':[str(a) for a in u],'verified':['A^T=-A','Av=2u','Au=-2v','four distinct exact quarter-turn states','constant squared norm2'],'scope':'An actual invariant frequency-2 subspace of the declared unit-metric filled tetrahedron, with the displayed sign convention.'},
 'quarter_turn_windows':window_results,
 'raw_positivity_return_example':{'rotation':['3/5','4/5'],'zero_initial_value':True,'strict_positive_nonzero_samples_checked':positive_tests,'closest_return_within_120_samples':{'index':closest[0],'squared_distance_decimal':float(closest[1]),'initial_decoder':0,'return_decoder':1},'scope':'Exact rational finite samples illustrate failure of local constancy. Recurrence and infinite-order statements require the stated mathematical argument, not finite sampling.'},
 'elapsed_seconds':round(time.monotonic()-started,3)
}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','generic_factor_tests':generic_factor_tests,'exact_factors_all_fixed':exact_factors,'actual_rsp_states':len(states),'quarter_turn_windows':'both branches match3 steps and fail at wrap','checker_sha256':sha(__file__),'results_sha256':sha(OUT),'elapsed_seconds':report['elapsed_seconds']},indent=2))
