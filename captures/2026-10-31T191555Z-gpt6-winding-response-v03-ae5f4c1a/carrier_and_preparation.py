#!/usr/bin/env python3
"""UD PRED-01/02 assumption-scoped mathematics. No native or physical carrier claim.

Python 3 + SymPy (for exact matrices) + NumPy (independent numeric rank check).
No external datasets, no calibration, no physical promotion.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import Counter
from fractions import Fraction
from math import factorial
from pathlib import Path
import sympy as s
import numpy as np


def simplices(m: int, decorate=True):
    assert m >= 4
    tri=[]; tet=[]
    u=lambda i:i%m
    v=lambda i:m+i%m
    for i in range(m):
        j=(i+1)%m
        tri.extend([tuple(sorted((u(i),u(j),v(j)))),
                    tuple(sorted((u(i),v(i),v(j))))])
    nextid=2*m
    if decorate:
        for root in range(2*m):
            fresh=tuple(range(nextid,nextid+3)); nextid+=3
            tetra=tuple(sorted((root,*fresh)))
            tet.append(tetra)
            tri.extend(tuple(sorted(t)) for t in itertools.combinations(tetra,3))
    tri=sorted(set(tri))
    edges=sorted(set(tuple(sorted(e)) for face in tri for e in itertools.combinations(face,2)))
    verts=list(range(nextid))
    return {"vertices":verts, "edges":edges, "triangles":tri,"tetrahedra":tet}


def incidence(low,high):
    low_map={obj:i for i,obj in enumerate(low)}
    B=s.zeros(len(low),len(high))
    for col,sigma in enumerate(high):
        for omit in range(len(sigma)):
            face=sigma[:omit]+sigma[omit+1:]
            B[low_map[face],col]+=(-1)**omit
    return B


def chain(m=8,decorate=True):
    S=simplices(m,decorate)
    verts=[(v,) for v in S['vertices']]
    B1=incidence(verts,S['edges'])
    B2=incidence(S['edges'],S['triangles'])
    B3=incidence(S['triangles'],S['tetrahedra'])
    return S,B1,B2,B3


def lifted_cochain(S,m,n):
    E={tuple(e):i for i,e in enumerate(S['edges'])}
    vec=s.zeros(len(E),1)
    h=s.Rational(n,m)
    def set_edge(a,b,value):
        e=tuple(sorted((a,b)))
        assert vec[E[e]]==0, (a,b)
        vec[E[e]]=value if (a,b)==e else -value
    for i in range(m):
        j=(i+1)%m
        set_edge(i,j,h)
        set_edge(m+i,m+j,h)
        set_edge(i,m+i,-h/2)
        set_edge(i,m+j,h/2)
    return vec


def period(S,a,m):
    E={tuple(e):i for i,e in enumerate(S['edges'])}
    value=s.Rational(0)
    for i in range(m):
        j=(i+1)%m
        edge=tuple(sorted((i,j)))
        value+=a[E[edge]] * (1 if (i,j)==edge else -1)
    return value


def action(a,gamma=0):
    gamma=s.Rational(gamma)
    return s.Rational(1,2)*(a.T*a)[0]+gamma*sum(x**4 for x in a)


def seam_slip(S,m):
    """Closed integer 1-cochain supported on a three-edge annular cut."""
    E={tuple(e):i for i,e in enumerate(S['edges'])}
    z=s.zeros(len(E),1)
    def set_directed(a,b):
        e=tuple(sorted((a,b)))
        assert z[E[e]]==0
        z[E[e]]=1 if e==(a,b) else -1
    set_directed(m-1,0)        # circumferential cut on lower circle
    set_directed(2*m-1,m)      # circumferential cut on upper circle
    set_directed(m-1,m)        # crossing diagonal on same cut
    return z


def seam_receipts(m=8,decorate=True):
    S,B1,B2,B3=chain(m,decorate)
    z=seam_slip(S,m)
    a1=lifted_cochain(S,m,1)
    assert B2.T*z==s.zeros(B2.cols,1)
    assert period(S,z,m)==1
    assert (z.T*z)[0]==3
    # An exact witness confirms z and the harmonic unit carry the same H^1 period.
    phi=s.zeros(len(S['vertices']),1)
    for i in range(m):
        phi[i]=s.Rational(i,m)
        phi[m+i]=s.Rational(i,m)-s.Rational(1,2*m)
    if decorate:
        for root in range(2*m):
            for new in range(2*m+3*root,2*m+3*root+3):
                phi[new]=phi[root]
    assert z==a1-B1.T*phi
    result=[]
    for n in range(4):
        an=lifted_cochain(S,m,n)
        anew=lifted_cochain(S,m,n+1)
        W=s.factor(action(an+z)-action(an))
        retained=s.factor(action(anew)-action(an))
        diss=s.factor(action(an+z)-action(anew))
        assert W==retained+diss
        assert W==s.Rational(3,2)+s.Rational(5*n,2*m)
        assert retained==s.Rational(5*(2*n+1),4*m)
        assert diss==s.Rational(3,2)-s.Rational(5,4*m)
        assert diss>0
        result.append({"n_to_nplus1":str(n)+"->"+str(n+1),
                       "gross_injected_work":str(W),
                       "retained_equilibrium_increment":str(retained),
                       "dissipated_remainder":str(diss),
                       "exact_receipt_balanced":True})
    return {"local_source_support_edges":3,"nonexact_closed_source":True,
            "winding_increment":1,"source_receipts":result,
            "gross_two_event_ratio":str(s.factor(s.Rational(3,2)+s.Rational(5,2*m))/s.Rational(3,2)),
            "retained_two_event_ratio":"3",
            "readout_nonuniqueness":"Gross source work != retained cost increment; calibration/readout required"}


def relax_phase_slip(m=8,steps=1000):
    S,B1,B2,B3=chain(m,decorate=True)
    a2=lifted_cochain(S,m,2)
    a3=lifted_cochain(S,m,3)
    z=seam_slip(S,m)
    A=np.asarray(B1,dtype=float)
    degree=np.diag(A@A.T)
    D=float(np.max(degree))
    eta=1/(4*D)
    eigs=np.linalg.eigvalsh(A@A.T)
    lambda_plus=float(min(x for x in eigs if x>1e-9))
    lambda_max=float(eigs[-1])
    assert 0<eta<2/lambda_max
    a=np.asarray(a2+z,dtype=float).flatten()
    target=np.asarray(a3,dtype=float).flatten()
    x0=np.linalg.norm(a-target)
    e0=0.5*np.dot(a,a)
    energies=[e0]
    samples=[]
    for step in range(1,steps+1):
        a -= eta * (A.T@(A@a))
        e=0.5*np.dot(a,a)
        assert e<=energies[-1]+1e-12
        energies.append(e)
        if step in (1,10,100,1000):
            samples.append({"step":step,"error_to_winding3_minimizer":float(np.linalg.norm(a-target)),
                            "excess_action":float(e-action(a3))})
    assert np.linalg.norm(a-target)<x0
    return {"update":"a_next=a-eta*B1.T*B1*a; preserves cohomology and decreases S0",
            "eta":eta,"max_vertex_degree":D,"lambda2_graph":lambda_plus,"lambda_max_graph":lambda_max,
            "contraction_on_exact_sector_bound":1-eta*lambda_plus,
            "initial_distance_to_n3":float(x0),"final_distance_to_n3":float(np.linalg.norm(a-target)),
            "sampled":samples,"discrete_steps_are_physical_time":False,
            "physical_promotion":0}


def capped_annulus_beta(m=8):
    """Cap inner circular ring by a cone. That contractible disk eliminates H^1."""
    S=simplices(m,decorate=False)
    center=2*m
    triangles=S['triangles']+[tuple(sorted((center,i,(i+1)%m))) for i in range(m)]
    edges=sorted(set(tuple(sorted(e)) for t in triangles for e in itertools.combinations(t,2)))
    B1=incidence([(i,) for i in range(2*m+1)],edges)
    B2=incidence(edges,sorted(set(triangles)))
    assert B1*B2==s.zeros(B1.rows,B2.cols)
    r1=int(B1.rank());r2=int(B2.rank())
    return {"vertices":2*m+1,"edges":len(edges),"faces":len(triangles),
            "betti":[2*m+1-r1,len(edges)-r1-r2,len(triangles)-r2],
            "topological_result":"capping hole -> H1=0, no nontrivial annular winding period"}


def build_carrier(m=8,decorate=True,rank_check=False):
    S,B1,B2,B3=chain(m,decorate)
    assert B1*B2==s.zeros(B1.rows,B2.cols)
    assert B2*B3==s.zeros(B2.rows,B3.cols)
    vals=[]
    for n in range(5):
        a=lifted_cochain(S,m,n)
        assert B2.T*a==s.zeros(B2.cols,1), 'non-flat local face'
        assert B1*a==s.zeros(B1.rows,1), 'not co-closed at nodes'
        assert period(S,a,m)==n
        assert (a.T*a)[0]==s.Rational(5*n*n,2*m)
        assert action(a)==s.Rational(5*n*n,4*m)
        assert action(a,1)==s.Rational(5*n*n,4*m)+s.Rational(17*n**4,8*m**3)
        vals.append({"n":n,"lifted_period":n,"norm_squared":str((a.T*a)[0]),
                     "quadratic_action":str(action(a)),"quartic_gamma1_action":str(action(a,1))})
    a2=lifted_cochain(S,m,2)
    # A nontrivial exact shift is orthogonal to the minimizer.
    phi=s.Matrix([s.Rational((i%7)-3,11) for i in range(len(S['vertices']))])
    ex=B1.T*phi
    assert (ex.T*a2)[0]==0
    assert action(a2+ex)-action(a2)==s.Rational(1,2)*(ex.T*ex)[0]>0
    assert period(S,a2+ex,m)==2
    Q=[s.Rational(5*(2*k+1),4*m) for k in range(4)]
    assert Q[2]-2*Q[1]+Q[0]==0
    quart=[s.Rational(5*(2*k+1),4*m)+s.Rational(17*((k+1)**4-k**4),8*m**3) for k in range(4)]
    def h4(e):return (e[1]-e[0])*(e[3]-e[2])-(e[2]-e[1])**2
    assert h4(Q)==0
    assert h4(quart)!=0
    output={"m":m,"decorated":decorate,"N0_vertices":len(S['vertices']),
            "N1_edges":len(S['edges']),"N2_faces":len(S['triangles']),"N3_tetra":len(S['tetrahedra']),
            "euler":len(S['vertices'])-len(S['edges'])+len(S['triangles'])-len(S['tetrahedra']),
            "boundary_squared_zero":True,"closed_and_coclosed":True,
            "period_conserved_under_exact_shifts":True,"quadratic_strict_minimum_under_nonconstant_gauge":True,
            "structural_formula":"S_0(n)=5*n^2/(4*m)","quartic_formula":"S_gamma(n)=5*n^2/(4*m)+17*gamma*n^4/(8*m^3)",
            "states":vals,
            "quadratic_event_increments":[str(x) for x in Q],
            "quartic_event_increments_gamma1":[str(x) for x in quart],
            "quadratic_D2":str(Q[2]-2*Q[1]+Q[0]),
            "quartic_D2":str(quart[2]-2*quart[1]+quart[0]),
            "quadratic_H4":str(h4(Q)),"quartic_H4":str(h4(quart)),
            "delta_action_2_to_3":str(vals[3]['quadratic_action'])+" - "+str(vals[2]['quadratic_action'])+" = "+str(s.Rational(25,4*m)),
            "physics_promotion":0}
    if rank_check:
        for label,mat in [('B1',B1),('B2',B2),('B3',B3)]:
            output['rank_'+label]=int(mat.rank())
        output['betti']=[len(S['vertices'])-output['rank_B1'],
                         len(S['edges'])-output['rank_B1']-output['rank_B2'],
                         len(S['triangles'])-output['rank_B2']-output['rank_B3'],
                         len(S['tetrahedra'])-output['rank_B3']]
        assert output['betti']==[1,1,0,0]
    else:
        # Independent floating numerical rank; exact betti is established by retraction.
        rank=[int(np.linalg.matrix_rank(np.array(M,dtype=float),tol=1e-9)) for M in (B1,B2,B3)]
        output['rank_numeric_B1_B2_B3']=rank
        output['betti_numeric']=[len(S['vertices'])-rank[0],len(S['edges'])-rank[0]-rank[1],
                                 len(S['triangles'])-rank[1]-rank[2],len(S['tetrahedra'])-rank[2]]
        assert output['betti_numeric']==[1,1,0,0]
    return output


TYPES=((0,0),(0,1),(1,1))
def states27():return list(itertools.product(TYPES,repeat=3))
def state_json(x):return [[int(a),int(b)] for a,b in x]
def shell(x):return sum(pair[0] for pair in x)
def has_partial(x):return (0,1) in x

def canonical_orbit(x):return tuple(sorted(x))

def schedule54(seed=20261031):
    # Shuffled first pass, rotated second pass; each repeated class is separated by 18 or 45 trials.
    from random import Random
    order=list(states27())
    Random(seed).shuffle(order)
    second=order[9:]+order[:9]
    samples=order+second
    pos={x:[] for x in order}
    for j,x in enumerate(samples):pos[x].append(j)
    assert len(samples)==54 and all(len(loc)==2 for loc in pos.values())
    assert min(loc[1]-loc[0] for loc in pos.values())==18
    return samples,pos


def orbit_reps():
    orbits={}
    for x in states27():orbits.setdefault(canonical_orbit(x),[]).append(x)
    return orbits


def q_representatives(x):
    """Assumed endpoint representative laws consistent with Part B's X-table.

    These are examples, not proof of exact native §7.5 source formulas.
    """
    omega=tuple(a for a,g in x)
    g=tuple(g for a,g in x)
    weight=sum(omega)
    return {'R0':omega,
            'R2':(1,1,1) if weight>=2 else omega,
            'R1':(1,1,1) if weight>=1 else (0,0,0),
            'Rtop':(1,1,1),
            'MTA':g}


def robust_endpoint_design():
    """Exact six-class minimal design for a chosen five-law representative family."""
    P=((0,1),(0,1),(0,1))
    S1=((1,1),(0,0),(0,0))
    S1b=((0,0),(1,1),(0,0))
    S2a=((1,1),(1,1),(0,0))
    S2b=((1,1),(0,0),(1,1))
    S2c=((0,0),(1,1),(1,1))
    six=(P,S1,S1b,S2a,S2b,S2c)
    assert len(set(six))==6
    families=list(q_representatives(P).keys())
    def signature(fam,samples):
        return sum((list(q_representatives(x)[fam]) for x in samples),[])
    def distance(f1,f2,samples):
        return sum(a!=b for a,b in zip(signature(f1,samples),signature(f2,samples)))
    d={f1+'__'+f2:distance(f1,f2,six) for i,f1 in enumerate(families) for f2 in families[i+1:]}
    assert min(d.values())>=3
    assert distance('R0','R2',six)==3
    # A representative from shell2 changes one bit R0 versus R2, so >=3 such samples.
    # Shell1 changes two bits R2 versus R1, so >=2 shell1 samples.
    # Shell0 changes three bits R1 versus Rtop, so >=1 shell0 sample.
    # These disjoint requirements force >=3+2+1=6 unique exposures.
    for x in states27():
        q=q_representatives(x)
        assert sum(q['R0'])==shell(x)
        assert sum(q['R2'])-shell(x)==(1 if shell(x)==2 else 0)
        assert sum(q['R1'])-shell(x)==(2 if shell(x)==1 else (1 if shell(x)==2 else 0))
        assert sum(q['Rtop'])-shell(x)==3-shell(x)
    twice=list(six)+list(six[2:])+list(six[:2])
    assert Counter(twice)=={x:2 for x in six}
    d_twice={f1+'__'+f2:distance(f1,f2,twice) for i,f1 in enumerate(families) for f2 in families[i+1:]}
    assert min(d_twice.values())>=6
    return {'family_labels':families,
            'status':'EXACT_CONDITIONAL for chosen X-table-consistent endpoint laws',
            'minimal_six_observations': [state_json(x) for x in six],
            'two_pass_twelve_observations':[state_json(x) for x in twice],
            'min_pairwise_bit_distance_six':min(d.values()),
            'min_pairwise_bit_distance_twelve':min(d_twice.values()),
            'pairwise_distances_six':d,
            'pairwise_distances_twelve':d_twice,
            'endpoint_signatures_six':{f:signature(f,six) for f in families},
            'lower_bound_proof':'R0/R2: >=3 shell2; R2/R1: >=2 shell1; R1/Rtop: >=1 shell0, each disjoint -> 6 exposures minimum at distance >=3',
            'warning':'Source X-table alone does not uniquely fix vector endpoint law; real §7.5 rule and preparation must be independently sourced before experimental claim.'}


def audit_preparation(seed=20261031):
    states=states27()
    assert len(states)==27 and len(set(states))==27
    counts=Counter(shell(x) for x in states)
    assert dict(counts)=={0:8,1:12,2:6,3:1}
    assert sum(has_partial(x) for x in states)==19
    s0=((0,1),(0,0),(0,0))
    s1=((1,1),(0,0),(0,0))
    s2=((1,1),(1,1),(0,0))
    minimal=(s0,s1,s2,s0)
    assert {shell(x) for x in minimal}=={0,1,2}
    assert has_partial(minimal[0])
    assert any(minimal.count(x)==2 for x in minimal)
    full,positions=schedule54(seed)
    assert Counter(full)=={x:2 for x in states}
    orbits=orbit_reps()
    assert len(orbits)==10
    assert Counter(map(len,orbits.values()))=={1:3,3:6,6:1}
    # 20 observations (2 per orbit representative) is enough to replay on the QUOTIENT, not validate S3 equivariance.
    orbit_sched=[next(iter(orbits[k])) for k in sorted(orbits)]*2
    assert len(orbit_sched)==20
    assert all(orbit_sched.count(x)==2 for x in orbit_sched[:10])
    partials=sum(has_partial(x) for x in full)
    return {"formal_27_states":[state_json(x) for x in states],
            "minimal_gate_plus_one_replay_count":4,
            "minimal_schedule":[state_json(x) for x in minimal],
            "full_27_class_twopass_count":len(full),
            "full_54_schedule":[{"index":i+1,"class":state_json(x),"shell":shell(x),
                                 "partial_present":has_partial(x),"pass":1 if i<27 else 2}
                               for i,x in enumerate(full)],
            "minimum_repeat_lag":min(p[1]-p[0] for p in positions.values()),
            "shell_counts_27":dict(sorted(counts.items())),
            "partial_present_classes":sum(has_partial(x) for x in states),
            "partial_present_observations_full":partials,
            "S3_orbit_count":len(orbits),
            "S3_orbit_sizes":dict(sorted(Counter(len(v) for v in orbits.values()).items())),
            "S3_quotient_two_pass_count_conditional":len(orbit_sched),
            "quotient_20_schedule":[{"index":i+1,"class":state_json(x)} for i,x in enumerate(orbit_sched)],
            "S3_quotient_validity":"CANDIDATE - requires independent permutation-equivariance tests",
            "representative_endpoint_design":robust_endpoint_design(),
            "physical_preparation":"OPEN - no edge-level, apparatus-level source built",
            "physics_promotion":0}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',default='RESULTS.json')
    ap.add_argument('--m',type=int,default=8)
    ap.add_argument('--seed',type=int,default=20261031)
    ap.add_argument('--exact-ranks',action='store_true')
    a=ap.parse_args()
    result={"run_type":"EXACT_CONDITIONAL_CARRIER_CONSTRUCTION_AND_RESPONSE_PREPARATION",
            "date":"2026-10-31","source_scope":"assumed annular seam + contractible K4 decorations",
            "carrier":build_carrier(m=a.m,rank_check=a.exact_ranks),
            "preparation":audit_preparation(seed=a.seed),
            "seam_source":seam_receipts(m=a.m),
            "relaxation":relax_phase_slip(m=a.m),
            "capped_boundary_control":capped_annulus_beta(m=a.m),
            "review":"DEFERRED","physics_promotion":0}
    Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('PASS: annulus chain identities, harmonic representative, n=2/3 finite carriers, response scheduling')
    print('  carrier betti:',result['carrier'].get('betti',result['carrier'].get('betti_numeric')))
    print('  n=2->3 cost:',result['carrier']['delta_action_2_to_3'])
    print('  quadratic D2:',result['carrier']['quadratic_D2'],'quartic D2:',result['carrier']['quartic_D2'])
    print('  schedules:',result['preparation']['minimal_gate_plus_one_replay_count'],result['preparation']['full_27_class_twopass_count'],result['preparation']['S3_quotient_two_pass_count_conditional'])

if __name__=='__main__':main()
