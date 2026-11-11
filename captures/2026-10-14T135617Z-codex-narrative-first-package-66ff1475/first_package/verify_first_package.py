from itertools import combinations, permutations, product
from pathlib import Path
import json, math
import sympy as s
import numpy as np
from scipy.linalg import expm
from scipy.special import ndtr

ROOT=Path(__file__).resolve().parent

def carrier(cells):
    simp=[sorted({face for cell in cells for face in combinations(tuple(sorted(cell)),k+1)}) for k in range(4)]
    bd={}
    for k in range(1,4):
        d=s.zeros(len(simp[k-1]),len(simp[k]))
        for j,t in enumerate(simp[k]):
            for i in range(k+1):
                d[simp[k-1].index(t[:i]+t[i+1:]),j]=(-1)**i
        bd[k]=d
    off=[0]
    for group in simp:off.append(off[-1]+len(group))
    D=s.zeros(off[-1])
    for k,d in bd.items():D[off[k-1]:off[k],off[k]:off[k+1]]=d
    A=D.T-D
    assert A.T==-A
    for k in (2,3):assert bd[k-1]*bd[k]==s.zeros(len(simp[k-2]),len(simp[k]))
    return simp,bd,off,A

x=s.symbols('x')
configs={
 'core_star':[(0,1,2,3),(1,2,3,4),(0,2,3,5),(0,1,3,6),(0,1,2,7)],
 'chain':[(0,1,2,3),(1,2,3,4),(2,3,4,5),(3,4,5,6),(4,5,6,7)]}
out={}
for name,cells in configs.items():
    simp,bd,off,A=carrier(cells)
    assert list(map(len,simp))==[8,18,16,5]
    assert sum(sum(set(face)<=set(c) for c in cells)==1 for face in simp[2])==12
    cp=s.factor(A.charpoly(x).as_expr())
    H=bd[3].T*bd[3]
    eig=np.linalg.eigvalsh(np.array((-A*A).tolist(),float))
    h=float(math.sqrt(eig[-1]))
    assert s.trace(-A*A)==2*sum(sum(abs(z) for z in d) for d in bd.values())
    # Fixed unit-norm preparations in first and last generated cell coordinates.
    delta=np.zeros(off[-1]);delta[off[3]]=1;delta[off[3]+4]=-1
    # Same admitted norm ceiling, using a common exact scale rather than an estimated norm.
    _,diag=(8*s.eye(off[-1])+A*A).LDLdecomposition()
    assert all(diag[i,i]>0 for i in range(off[-1]))
    An=np.array(A.tolist(),float)/math.sqrt(8)
    times=np.linspace(0,math.pi,129)
    margins=[float(np.linalg.norm((expm(t*An)@delta)[off[3]:off[4]])) for t in times]
    sigma=.25
    errors=[float(ndtr(-r/(2*sigma))) for r in margins]
    out[name]={'cells':cells,'f':[8,18,16,5],'chain_dimension':47,'boundary_faces':12,
      'characteristic_polynomial':str(cp),'top_gram':H.tolist(),
      'top_gram_charpoly':str(s.factor(H.charpoly(x).as_expr())),
      'operator_norm_numeric':h,'max_laplacian_numeric':h*h,
      'common_scale':str(s.sqrt(8)),'admitted_norm_budget':1,
      'exact_norm_ceiling_certificate':'8I-L positive definite by rational LDL',
      'numeric_grid':{'T':math.pi,'points':129,'sigma':sigma,
      'smallest_sampled_cell_distance':min(margins),'largest_sampled_readout_error':max(errors),
      'analytic_grid_cover_error_upper_bound':float(ndtr(-max(0,min(margins)-math.sqrt(2)*math.pi/256)/(2*sigma))),
      'grid_cover_proof':'norm ceiling 1 gives distance Lipschitz constant sqrt(2); nearest grid point at most pi/256 away; floating evaluations not interval-certified'}}
    # Store exact incidence certificate in reproducible text.
    (ROOT/f'{name}_matrices.json').write_text(json.dumps({'simplices':simp,'boundary':{str(k):d.tolist() for k,d in bd.items()},'characteristic_polynomial':str(cp)},default=int,indent=2)+'\n')

# Two-cell exact equations, and matched derivative observation.
simp,bd,off,A=carrier([(0,1,2,3),(0,1,2,4)])
assert s.factor(A.charpoly(x).as_expr())==x*(x*x+3)**4*(x*x+5)**7
t=s.symbols('t',real=True)
dq=s.cos(s.sqrt(3)*t)*s.Matrix([1,-1])
dv=dq.diff(t)/s.sqrt(3)
assert s.simplify((dq.T*dq+dv.T*dv)[0])==2
sigma=.25
out['two_cell_noise']={'sigma':sigma,'cell_only_error_at_snapshot_zero':.5,
 'cell_plus_normalized_derivative_error':float(ndtr(-1/(math.sqrt(2)*sigma))),
 'noise_model':'independent isotropic Gaussian on declared observations; equal priors'}

# Direct-sum copy gluing: common seven coordinates plus disjoint coordinates.
J=s.zeros(23,30)
for i in range(7):J[i,i]=1/s.sqrt(2);J[i,15+i]=1/s.sqrt(2)
for i in range(8):J[7+i,7+i]=1;J[15+i,22+i]=1
R=s.zeros(7,30)
for i in range(7):R[i,i]=1/s.sqrt(2);R[i,15+i]=-1/s.sqrt(2)
U=J.col_join(R)
assert s.simplify(U*U.T)==s.eye(30)
assert s.simplify(J.T*J+R.T*R)==s.eye(30)
out['interface']={'input_dimension':30,'visible_dimension':23,'residual_dimension':7,
 'orthogonal_completion':'PASS','norm_balance':'PASS','unit_calibration_factor':str(s.sqrt(2))}

# Actual simplex ordering and inherited direct-sum generator.
local=[carrier([(0,1,2,3)]),carrier([(0,1,2,4)])]
glued=carrier([(0,1,2,3),(0,1,2,4)])
s0=[face for group in local[0][0] for face in group]
s1=[face for group in local[1][0] for face in group]
sg=[face for group in glued[0] for face in group]
Q=s.zeros(23,30);R=s.zeros(7,30);nr=0
for i,face in enumerate(sg):
    ids=[]
    if face in s0:ids.append(s0.index(face))
    if face in s1:ids.append(15+s1.index(face))
    if len(ids)==2:
        Q[i,ids[0]]=Q[i,ids[1]]=1/s.sqrt(2)
        R[nr,ids[0]]=1/s.sqrt(2);R[nr,ids[1]]=-1/s.sqrt(2);nr+=1
    else:Q[i,ids[0]]=1
U=Q.col_join(R);Aold=s.diag(local[0][3],local[1][3]);Ag=glued[3]
assert U*U.T==s.eye(30)
G=U*Aold*U.T
assert G.T==-G
assert G[:23,23:].rank()==7
assert (G[:23,:23]-Ag).rank()==14
assert (Q*Aold-Ag*Q).rank()==21
out['interface'].update({'visible_residual_coupling_rank':7,'visible_generator_defect_rank':14,
 'projection_intertwining_defect_rank':21,'native_dynamic_intertwining':False})
(ROOT/'interface_matrices.json').write_text(json.dumps({'Q':Q.tolist(),'R':R.tolist(),
 'generator_coupling_rank':7,'visible_generator_defect_rank':14,'projection_intertwining_defect_rank':21},default=str,indent=2)+'\n')

# Underidentified move/receipt input: two symmetric completions.
theta=list(product((0,1),repeat=3))
for v in theta:
    assert v!=tuple(a^1 for a in v)
    for p in permutations(range(3)):
        pv=tuple(v[i] for i in p)
        assert tuple((a^1) for a in pv)==tuple((v[i]^1) for i in p)
out['selection']={'identity_and_complement_covariant':'PASS','same_native_input_distinct_endpoints':'PASS',
 'native_source_status':'OPEN; no constitutive law inferred'}

# Conditional closure lift, distinct from event selection and transport updates.
hard_cases=0
for old in theta:
 for p in permutations(range(3)):
  y=tuple(old[i] for i in p)
  for flip in theta:
   new=tuple(a^b for a,b in zip(y,flip))
   for gates in product((0,1),repeat=6):
    pre=[(1-y[j//2])*gates[j] for j in range(6)]
    post=[(1-new[j//2])*gates[j] for j in range(6)]
    closing=sum(pre[j]==1 and post[j]==0 for j in range(6))
    opening=sum(pre[j]==0 and post[j]==1 for j in range(6))
    assert closing==sum((1-y[i])*flip[i]*(gates[2*i]+gates[2*i+1]) for i in range(3))
    assert opening==sum(y[i]*flip[i]*(gates[2*i]+gates[2*i+1]) for i in range(3))
    hard_cases+=1
assert hard_cases==24576
out['selection']['conditional_fixed_gate_closure_cases']=hard_cases

# Correlation-aware Gaussian likelihood versus the invalid independent score.
cov=np.array([[1.,.5],[.5,1.]])
delta=np.array([1.,1.])
mah=float(delta@np.linalg.solve(cov,delta))
assert abs(mah-4/3)<1e-12
out['correlated_readout']={'mahalanobis_distance_squared':mah,
 'correct_error':float(ndtr(-math.sqrt(mah)/2)),
 'invalid_independent_error':float(ndtr(-math.sqrt(2)/2)),
 'scope':'stipulated positive-definite covariance, not measured noise'}

def clean(v):
    if isinstance(v,dict):return {k:clean(a) for k,a in v.items()}
    if isinstance(v,(list,tuple)):return [clean(a) for a in v]
    if isinstance(v,s.Integer):return int(v)
    return v
(ROOT/'results.json').write_text(json.dumps(clean(out),indent=2)+'\n')
print(json.dumps(clean(out),indent=2))
