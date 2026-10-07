#!/usr/bin/env python3
"""Exact rational/Gaussian-integer audit; no continuum identification inferred."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
ROOT=Path(__file__).resolve().parents[1];checks=[]
def check(name,ok):
    assert bool(ok),name
    checks.append(name)
def subsets(t):
    return [tuple(v) for r in range(1,len(t)+1) for v in itertools.combinations(t,r)]
def build(tops):
    nodes=sorted({v for t in tops for v in subsets(t)},key=lambda x:(len(x),x));lookup={v:i for i,v in enumerate(nodes)}
    edges=[]
    for s in nodes:
        for t in nodes:
            if len(t)==len(s)+1 and set(s)<set(t):edges.append((s,t))
    ei={e:i for i,e in enumerate(edges)};D=S.zeros(len(nodes),len(edges));A=S.zeros(len(nodes))
    for i,(s,t) in enumerate(edges):
        D[lookup[s],i]=-1;D[lookup[t],i]=1
        added=next(v for v in t if v not in s);b=(-1)**t.index(added)
        A[lookup[t],lookup[s]]=b;A[lookup[s],lookup[t]]=-b
    squares=[]
    for s in nodes:
        for t in nodes:
            if len(t)==len(s)+2 and set(s)<set(t):squares.append((s,tuple(v for v in t if v not in s)))
    qi={q:i for i,q in enumerate(squares)};C=S.zeros(len(edges),len(squares))
    for col,(s,(a,b)) in enumerate(squares):
        sa=tuple(sorted(s+(a,)));sb=tuple(sorted(s+(b,)));t=tuple(sorted(s+(a,b)))
        for e,sgn in [((s,sa),1),((sa,t),1),((sb,t),-1),((s,sb),-1)]:C[ei[e],col]=sgn
    cubes=[]
    for s in nodes:
        for t in nodes:
            if len(t)==len(s)+3 and set(s)<set(t):cubes.append((s,tuple(v for v in t if v not in s)))
    B=S.zeros(len(squares),len(cubes))
    for col,(s,abc) in enumerate(cubes):
        for k,v in enumerate(abc):
            rem=tuple(x for x in abc if x!=v);upper=tuple(sorted(s+(v,)))
            B[qi[(upper,rem)],col]+=(-1)**k;B[qi[(s,rem)],col]-=(-1)**k
    return nodes,edges,squares,cubes,D,C,B,A
def plain(M):return [[str(x) for x in row] for row in M.tolist()]
def rank_mod(M,p=101):
    a=[[int(S.numer(x))%p*pow(int(S.denom(x))%p,-1,p)%p for x in row] for row in M.tolist()]
    row=0
    for col in range(M.cols):
        pivot=next((i for i in range(row,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[row],a[pivot]=a[pivot],a[row];inv=pow(a[row][col],-1,p)
        a[row]=[(v*inv)%p for v in a[row]]
        for i in range(row+1,len(a)):
            if a[i][col]:
                factor=a[i][col];a[i]=[(u-factor*v)%p for u,v in zip(a[i],a[row])]
        row+=1
        if row==len(a):break
    return row

def main():
    x=S.symbols('x0:4');F=S.zeros(4);F[0,1]=x[0];F[1,0]=-x[0]
    J=S.Matrix([sum(S.diff(F[i,j],x[i]) for i in range(4)) for j in range(4)])
    check('continuum antisymmetric single divergence counterexample',F+F.T==S.zeros(4) and J==S.Matrix([0,1,0,0]))
    check('continuum double divergence counterexample identity',sum(S.diff(J[i],x[i]) for i in range(4))==0)
    cases={
        'tetrahedron':[(0,1,2,3)],
        'two_tets_shared_face':[(0,1,2,3),(0,1,2,4)],
        'three_tets_shared_edge':[(0,1,2,3),(0,1,2,4),(0,1,3,4)],
        'pentachoron_boundary':list(itertools.combinations(range(5),4)),
        'hollow_tetrahedron':list(itertools.combinations(range(4),3)),
        'unfilled_triangle_loop':[(0,1),(1,2),(0,2)]}
    expected={'tetrahedron':(15,28,18,4,14,14,4,0),
        'two_tets_shared_face':(23,47,33,8,22,25,8,0),
        'three_tets_shared_edge':(27,59,45,12,26,33,12,0),
        'pentachoron_boundary':(30,70,60,20,29,41,19,0),
        'hollow_tetrahedron':(14,24,12,0,13,11,0,0),
        'unfilled_triangle_loop':(6,6,0,0,5,0,0,1)}
    results=[];matrices={};tet=None
    for name,tops in cases.items():
        nodes,edges,squares,cubes,D,C,B,A=build(tops);v,e,f,n_cubes=len(nodes),len(edges),len(squares),len(cubes)
        rd,rc,rb=D.rank(),C.rank(),B.rank();h1=e-rd-rc
        check(name+': exact counts/ranks/topological residual',(v,e,f,n_cubes,rd,rc,rb,h1)==expected[name])
        sc=smith_normal_form(C,domain=S.ZZ);sq=smith_normal_form(B,domain=S.ZZ)
        ic=[abs(sc[i,i]) for i in range(min(sc.shape)) if sc[i,i]]
        iq=[abs(sq[i,i]) for i in range(min(sq.shape)) if sq[i,i]]
        check(name+': square image has unit nonzero Smith invariants',len(ic)==rc and all(x==1 for x in ic))
        check(name+': cube image has unit nonzero Smith invariants',len(iq)==rb and all(x==1 for x in iq))
        check(name+': graph boundary times square boundary zero',D*C==S.zeros(v,f))
        check(name+': square boundary times cube boundary zero',C*B==S.zeros(e,n_cubes))
        check(name+': full generator is skew',A+A.T==S.zeros(v))
        check(name+': total divergence vanishes',S.ones(1,v)*D==S.zeros(1,e))
        cycle_basis=S.Matrix.hstack(*D.nullspace())
        check(name+': mod101 witness stock derivatives plus cycle probes determine all currents',rank_mod(D.col_join(cycle_basis.T))==e)
        check(name+': mod101 witness local square probes miss exactly noncurl cycles',rank_mod(D.col_join(C.T))==e-h1)
        coarse_rank=None
        c=S.Matrix([S.Integer((i%5)-2) for i in range(v)])
        j=S.Matrix([2*A[nodes.index(t),nodes.index(s)]*c[nodes.index(s)]*c[nodes.index(t)] for s,t in edges])
        dotrho=S.Matrix([2*c[i]*(A*c)[i] for i in range(v)])
        check(name+': actual real support continuity',D*j==dotrho)
        check(name+': total quadratic support conserved',sum(dotrho)==0)
        z=S.Matrix([S.Integer((i%3)-1)+S.I*S.Integer((i%4)-2) for i in range(v)])
        jz=S.Matrix([2*S.re(S.conjugate(z[nodes.index(t)])*A[nodes.index(t),nodes.index(s)]*z[nodes.index(s)]) for s,t in edges])
        dz=S.Matrix([2*S.re(S.conjugate(z[i])*(A*z)[i]) for i in range(v)])
        check(name+': complex support uses real current part',D*jz==dz)
        if all(len(t)==4 for t in tops):
            ownership=S.zeros(len(tops),v)
            for i,simplex in enumerate(nodes):
                owners=[k for k,t in enumerate(tops) if set(simplex)<=set(t)]
                for k in owners:ownership[k,i]=S.Rational(1,len(owners))
            check(name+': equal-top-star ownership sums to one',S.ones(1,len(tops))*ownership==S.ones(1,v))
            stockdot=S.Matrix([sum((ownership[k,nodes.index(t)]-ownership[k,nodes.index(s)])*j[i] for i,(s,t) in enumerate(edges)) for k in range(len(tops))])
            check(name+': Q179 ownership continuity rederived',ownership*dotrho==stockdot)
            check(name+': equal-share stocks cannot detect added circulation',ownership*D*C==S.zeros(len(tops),C.cols))
            coarse_rank=(ownership*D).rank()
            check(name+': equal-share cell derivative rank equals cell count minus one',coarse_rank==len(tops)-1)
        # Exact simplicial boundaries remain a separate complex.
        bydim=[[t for t in nodes if len(t)==d+1] for d in range(4)];bs=[]
        for dim in range(1,4):
            b=S.zeros(len(bydim[dim-1]),len(bydim[dim]))
            for col,t in enumerate(bydim[dim]):
                for kk in range(len(t)):b[bydim[dim-1].index(t[:kk]+t[kk+1:]),col]=(-1)**kk
            bs.append(b)
        check(name+': original B1B2=0',bs[0]*bs[1]==S.zeros(len(bydim[0]),len(bydim[2])))
        check(name+': original B2B3=0',bs[1]*bs[2]==S.zeros(len(bydim[1]),len(bydim[3])))
        if h1==0:
            check(name+': every graph cycle spanned by square curls',rc==e-rd)
        else:
            loop=D.nullspace()[0]
            check(name+': closed loop cannot be a square curl',D*loop==S.zeros(v,1) and C.cols==0 and loop!=S.zeros(e,1))
        result={'name':name,'simplicial_f_vector':[len(z) for z in bydim],
            'Hasse_cells':[v,e,f,n_cubes],'rank_D':rd,'rank_C':rc,'rank_Bcube':rb,
            'nonzero_C_Smith_invariants':[int(x) for x in ic],
            'nonzero_cube_Smith_invariants':[int(x) for x in iq],
            'divergence_invisible_current_dimension':e-rd,'noncurl_cycle_dimension':h1,
            'square_potential_ambiguity_dimension':f-rc,'cube_image_dimension':rb,
            'extra_closed_square_dimension':f-rc-rb}
        result['minimum_additional_linear_probes_with_full_stock_derivatives']=e-rd
        result['equal_share_cell_derivative_rank']=coarse_rank
        result['minimum_additional_linear_probes_with_only_cell_derivatives']=None if coarse_rank is None else e-coarse_rank
        results.append(result);matrices[name]={'nodes':nodes,'edges':edges,'squares':squares,'cubes':cubes,
            'graph_boundary_D':plain(D),'diamond_boundary_C':plain(C),'cube_boundary':plain(B),'skew_generator_A':plain(A)}
        if name=='tetrahedron':tet=(nodes,edges,D,C,B,A)
    nodes,edges,D,C,B,A=tet;v,e=len(nodes),len(edges)
    # Normalized ready witness is represented as integer c then divide density/current by2.
    c=S.zeros(v,1);c[nodes.index((1,))]=1;c[nodes.index((0,1))]=1
    j=S.Matrix([A[nodes.index(t),nodes.index(s)]*c[nodes.index(s)]*c[nodes.index(t)] for s,t in edges])
    s=D*j
    check('normalized current witness has exactly one unit incidence',sum(abs(x) for x in j)==1)
    check('nonzero stock derivative despite skew generator',s[nodes.index((1,))]==-1 and s[nodes.index((0,1))]==1)
    check('pure-curl ansatz excludes valid dynamic witness',D*C==S.zeros(v,C.cols) and s!=S.zeros(v,1))
    cc=S.zeros(v,1);cc[nodes.index((0,1,3))]=1;cc[nodes.index((0,1,2,3))]=1
    jj=S.Matrix([A[nodes.index(t),nodes.index(ss)]*cc[nodes.index(ss)]*cc[nodes.index(t)] for ss,t in edges])
    ss=D*jj
    check('normalized face/core witness keeps nonzero interface-stock derivative',ss[nodes.index((0,1,3))]==-1 and ss[nodes.index((0,1,2,3))]==1)
    check('Q172 face reservoir not erased by antisymmetry',sum(abs(x) for x in jj)==1 and sum(ss)==0)
    L=D*D.T;phi=L.gauss_jordan_solve(s)[0];free=sorted(phi.free_symbols,key=str)
    phi=phi.subs({z:0 for z in free});phi-=S.ones(v,1)*sum(phi)/v
    jgrad=D.T*phi;loop=j-jgrad
    check('minimum Euclidean gradient current reproduces source',D*jgrad==s and sum(phi)==0)
    check('actual-current minus gradient is a graph cycle',D*loop==S.zeros(v,1))
    check('dynamic witness contains nonzero divergence-invisible circulation',loop!=S.zeros(e,1))
    qsol=C.gauss_jordan_solve(loop)[0];qsol=qsol.subs({z:0 for z in qsol.free_symbols})
    check('dynamic circulation has explicit rational diamond potential',C*qsol==loop)
    check('gradient and circulation orthogonal',jgrad.dot(loop)==0)
    check('curl ambiguity survives full node-stock derivatives',D*(j+C[:,0])==D*j)
    W=S.Matrix([[S.Rational(1,2) if i%2==0 else S.Rational(1,3) for i in range(v)],
        [S.Rational(1,2) if i%2==0 else S.Rational(2,3) for i in range(v)]])
    check('owned fixed stocks preserve total',S.ones(1,2)*W==S.ones(1,v))
    check('coarse stock derivatives also cannot see curls',W*D*(j+C[:,0])==W*D*j)
    M0=S.diag(*[S.Rational(i+1,i+2) for i in range(v)])
    M1=S.diag(*[S.Rational(i+2,i+3) for i in range(e)])
    M2=S.diag(*[S.Rational(i+3,i+4) for i in range(C.cols)])
    delta1=M0.inv()*D*M1;delta2=M1.inv()*C*M2
    check('matched weighted codifferentials square to zero',delta1*delta2==S.zeros(v,C.cols))
    wrong=delta1*C*M2
    check('mismatched intermediate metric gives nonzero false divergence',wrong!=S.zeros(v,C.cols))
    r=S.Matrix([S.Rational((i%3)-1,7) for i in range(v)]);source=S.Matrix([2*c[i]*r[i]/2 for i in range(v)])
    explicit_open_dot=S.Matrix([c[i]*(A*c+r)[i] for i in range(v)])
    check('open-source local continuity from explicit amplitude derivative',explicit_open_dot==s+source)
    check('open-source bookkeeping keeps global injection',sum(s+source)==sum(source))
    out={'status':'PASS','software':{'python_sympy':S.__version__,'rank_witness_modulus':101},'exact_checks':len(checks),'numerical_checks':0,'checks':checks,'cases':results,
        'normalized_dynamic_witness':{'nonzero_current_edge':[[list(edges[i][0]),list(edges[i][1]),str(j[i])] for i in range(e) if j[i]],
            'node_stock_derivative':[[list(nodes[i]),str(s[i])] for i in range(v) if s[i]],
            'Euclidean_gradient_current':[str(x) for x in jgrad],
            'circulation_residual':[str(x) for x in loop],'diamond_potential':[str(x) for x in qsol]},
        'normalized_face_core_witness':{'nonzero_current_edge':[[list(edges[i][0]),list(edges[i][1]),str(jj[i])] for i in range(e) if jj[i]],
            'node_stock_derivative':[[list(nodes[i]),str(ss[i])] for i in range(v) if ss[i]]},
        'scope':'exact exploratory current representation/identifiability audit; no Maxwell or source-law derivation',
        'open_system_closure':'OPEN','independent_review':'PENDING','physical_promotion':0,'ledger_mutation':False}
    (ROOT/'audit').mkdir(exist_ok=True)
    (ROOT/'audit/MATRICES.json').write_text(json.dumps(matrices,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
