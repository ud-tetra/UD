#!/usr/bin/env python3
"""UD K4->K5: exact finite tests of topology-changing apex constructor and hidden-fiber twist.
Development model, no physical promotion or inferred native source law.
Python 3.10+, sympy. Uses no external data.
"""
import itertools, json, sys, hashlib
from collections import Counter
from fractions import Fraction
from pathlib import Path
from sympy import Matrix, eye, sqrt, simplify, zeros, symbols

checks=[]
def ck(name,cond):
    assert bool(cond), name
    checks.append(name)

def closure(maximal):
    faces=set()
    for f in maximal:
        for k in range(1,len(f)+1):
            for c in itertools.combinations(f,k): faces.add(c)
    return {i:sorted(f for f in faces if len(f)==i+1) for i in range(5)}

def boundary_matrix(simplices,k):
    if k<1:return Matrix.zeros(0,len(simplices.get(0,[])))
    lower=simplices.get(k-1,[]); upper=simplices.get(k,[])
    out=Matrix.zeros(len(lower),len(upper)); rows={s:i for i,s in enumerate(lower)}
    for j,t in enumerate(upper):
        for i in range(len(t)):
            face=t[:i]+t[i+1:]
            out[rows[face],j]+=(-1)**i
    return out

T=(0,1,2,3); apex=4; S=tuple(range(5))
old=closure([T]); shell_facets=list(itertools.combinations(S,4)); shell=closure(shell_facets)
filled=closure([S])
stellar=closure([face for face in shell_facets if face != T])  # 1-to-4 interior stellar refinement: old 3-cell removed

def fvector(c):return [len(c.get(k,[])) for k in range(5)]
ck('old_fvector',fvector(old)==[4,6,4,1,0]); ck('shell_fvector',fvector(shell)==[5,10,10,5,0]);ck('stellar_fvector',fvector(stellar)==[5,10,10,4,0]); ck('filled_fvector',fvector(filled)==[5,10,10,5,1]);
ck('shell_increment',(Matrix(fvector(shell))-Matrix(fvector(old)))==Matrix([1,4,6,4,0]));
ck('fill_increment',(Matrix(fvector(filled))-Matrix(fvector(shell)))==Matrix([0,0,0,0,1]));

for label,K in [('old',old),('stellar',stellar),('shell',shell),('filled',filled)]:
    for k in range(2,5):
        a=boundary_matrix(K,k-1)*boundary_matrix(K,k)
        ck(f'boundary_squared_{label}_{k}',a.is_zero_matrix)

b3=boundary_matrix(shell,3)
u=Matrix([(-1)**i for i in range(5)]) # omit vertex i
ck('oriented_5_facet_cycle',b3*u==zeros(b3.rows,1))
ck('oriented_cycle_unique',b3.rank()==4 and len(b3.nullspace())==1)
# Stellar fundamental class preserves the original 3D boundary with integral coefficients.
star_chain=Matrix([-u[i] for i in range(4)]+[0])
ck('stellar_children_have_old_boundary', b3*star_chain==b3*Matrix([0,0,0,0,1]))
ck('stellar_counting_norm_quadruples', simplify(star_chain.dot(star_chain))==4)
ck('unit_counting_stock_loses_half_boundary', b3*(star_chain/2)==b3*Matrix([0,0,0,0,1])/2)
ck('same_two_skeleton_in_all_K5_branches',all(stellar[k]==shell[k]==filled[k] for k in range(3)))
ck('stars_vs_shell_3_skeleton_differs',stellar[3]!=shell[3] and shell[3]==filled[3])
ck('shell_vs_filled_only_in_C4',shell[4]!=filled[4])
# At barycentric interior point, four child 3-volume determinants are one quarter of parent.
vertices3={0:Matrix([0,0,0]),1:Matrix([1,0,0]),2:Matrix([0,1,0]),3:Matrix([0,0,1]),4:Matrix([Fraction(1,4)]*3)}
def oriented_det3(tet):
    v0=vertices3[tet[0]]
    return Matrix.hstack(*[vertices3[i]-v0 for i in tet[1:]]).det()
basevol=abs(oriented_det3(T))/6
childvols=[abs(oriented_det3(t))/6 for t in stellar[3]]
ck('stellar_each_child_quarter_parent_volume',all(simplify(v/basevol)==Fraction(1,4) for v in childvols))
ck('stellar_volume_additive',simplify(sum(childvols)-basevol)==0)
ck('volume_weighted_cell_stock_invariant',simplify(sum(childvols)*1**2-basevol*1**2)==0)
for label,K in [('shell',shell),('filled',filled)]:
    d3=boundary_matrix(K,3); d4=boundary_matrix(K,4)
    b3dim=len(K[3])-d3.rank()-d4.rank()
    ck(f'Betti3_{label}', b3dim==(1 if label=='shell' else 0))

# Pre-carrier old tet -> new shell: canonical naming x_T=tag(T,event).
# This is a FUNCTORIAL constructor, not an autonomous selection law.

def apex_name(vertices,event='event_0'):
    return ('APEX',tuple(sorted(vertices)),event)

import math
for perm in itertools.permutations(range(4)):
    ck(f'apex_equivariance_{"".join(map(str,perm))}',apex_name([perm[i] for i in range(4)])==apex_name(T))

# Exact Householder support rotation of old facet onto unique shell cycle
q=u/sqrt(5); e=Matrix([0,0,0,0,1]); w=e-q
H=eye(5)-2*(w*w.T)/(w.dot(w))
ck('householder_maps_old_tet_to_closed_shell',all(simplify(a-b)==0 for a,b in zip(H*e,q)))
ck('householder_orthogonal',all(simplify(a-b)==0 for a,b in zip(H.T*H,eye(5))))
ck('householder_involution',all(simplify(a-b)==0 for a,b in zip(H*H,eye(5))))
ck('support_1_over_5_4_over_5', simplify(q[4]**2)==Fraction(1,5) and simplify(sum(q[i]**2 for i in range(4)))==Fraction(4,5))
ck('old_nonzero_boundary',b3*e!=zeros(b3.rows,1))
ck('closed_new_boundary',b3*q==zeros(b3.rows,1))

# Flat Z2 twists on K5 complete 2-skeleton: all are exact coboundaries.
edges=list(itertools.combinations(range(5),2));tris=list(itertools.combinations(range(5),3));
edgeidx={e:i for i,e in enumerate(edges)}
flat=[]; nonflat_hist=Counter()
for bits in itertools.product((0,1),repeat=len(edges)):
    curvature=[(bits[edgeidx[(i,j)]]+bits[edgeidx[(j,k)]]+bits[edgeidx[(i,k)]])%2 for i,j,k in tris]
    nonflat_hist[sum(curvature)]+=1
    if not any(curvature):
        flat.append(bits)
        g=[0]+[bits[edgeidx[(0,i)]] for i in range(1,5)]
        ck('flat_twist_gauge_trivial_'+str(len(flat)),all(bits[edgeidx[(i,j)]]==(g[i]+g[j])%2 for i,j in edges))
ck('exact_16_flat_z2_assignments',len(flat)==16)
ck('flat_twist_all_from_vertex_gauge',len({tuple((g[i]+g[j])%2 for i,j in edges) for g in itertools.product((0,1),repeat=5)})==16)

# Gram hidden-coordinate test, for a nonuniform base and apex.
X=Matrix([[1,0,0,Fraction(1,4)], [0,1,0,Fraction(1,4)], [0,0,1,Fraction(1,4)], [0,0,0,Fraction(1,2)]])
V=Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0]])
G=X.T*X; Gobs=(V*X).T*(V*X)
ck('four_dim_metric_full_rank',G.rank()==4 and simplify(G.det())==Fraction(1,4))
ck('three_dim_readout_rank_three',Gobs.rank()==3 and Gobs.det()==0)
z=Matrix([[0,0,0,Fraction(1,2)]])
ck('missing_rank_one_normal_metric',G-Gobs==z.T*z)
ck('normal_sign_reflection_invisible',X.T*X==(Matrix.diag(1,1,1,-1)*X).T*(Matrix.diag(1,1,1,-1)*X))

# Finite twisted Klein x circle Laplacian; y,z base coordinates in constant modes.
N=4; M=4; kappa=3

def laplacian(twisted=True):
    L=Matrix.zeros(N*M,N*M)
    idx=lambda x,j:x*M+j
    E=set()
    for x in range(N):
        for j in range(M):
            y=x+1; j2=j
            if y==N:
                y=0; j2=(-j)%M if twisted else j
            a,b=sorted([idx(x,j),idx(y,j2)])
            E.add((a,b,1))
            a,b=sorted([idx(x,j),idx(x,(j+1)%M)])
            E.add((a,b,kappa))
    for a,b,wgt in E:
        L[a,a]+=wgt;L[b,b]+=wgt
        L[a,b]-=wgt;L[b,a]-=wgt
    return L

Lt=laplacian(True); Lu=laplacian(False)
ck('twisted_graph_laplacian_symmetric',Lt==Lt.T)
ck('twisted_graph_laplacian_zero_mode',Lt*Matrix([1]*(N*M))==zeros(N*M,1))

# Fibre-constant visible field embeds as Q; P=Q*Q^T is orthogonal projection.
Q=Matrix.zeros(N*M,N)
for x in range(N):
    for j in range(M):Q[x*M+j,x]=Fraction(1,2)
P=Q*Q.T
C4=Matrix([[2,-1,0,-1],[-1,2,-1,0],[0,-1,2,-1],[-1,0,-1,2]])
ck('invariant_base_zero_mode',Q.T*Lt*Q==C4)
ck('fibre_constant_sector_protected',Lt*P==P*Lt)
ck('twist_is_invisible_to_base_projection',Q.T*Lt*Q==Q.T*Lu*Q)

# Full spectrum: 4 fibre modes: 0, cos(1), sin(1), 2.
# n=1 cos even sees periodic x; sin odd sees antiperiodic x.
actual=Counter({simplify(eig):int(mul) for eig,mul in Lt.eigenvals().items()})
xs_p=[0,2,2,4]; xs_a=[2-sqrt(2),2+sqrt(2),2+sqrt(2),2-sqrt(2)]
expected=Counter()
for x in xs_p:expected[x]+=1  # fibre 0
for x in xs_p:expected[x+4*kappa]+=1 # fibre 2, eigen=4 kappa
for x in xs_p:expected[x+2*kappa]+=1 # cos fibre 1
for x in xs_a:expected[x+2*kappa]+=1 # sin fibre 1 antiperiodic
ck('twisted_spectrum_exact_Fourier_prediction',actual==expected)
actual_u=Counter({simplify(eig):int(mul) for eig,mul in Lu.eigenvals().items()})
expected_u=Counter()
for x in xs_p:expected_u[x]+=1
for x in xs_p:expected_u[x+4*kappa]+=1
for x in xs_p:expected_u[x+2*kappa]+=2
ck('untwisted_spectrum_control',actual_u==expected_u)
ck('twist_shifts_odd_nonzero_modes',actual!=actual_u)
ck('visible_base_low_modes_below_fibre_gap',max(xs_p)<2*kappa)

# Norm-parity: the holonomy along the x cycle acts on transverse fibre by reflection.
reflection=Matrix.zeros(M,M)
for j in range(M):reflection[(-j)%M,j]=1
ck('twist_reflection_involution',reflection*reflection==eye(M))
ck('twist_has_odd_fibre_sector',sorted(reflection.eigenvals().items())==[( -1,1),(1,3)])

result={
  'artifact':'UD_K4_K5_OMEGA_APEX_TWIST_VERIFY_v0.4',
  'date':'2026-10-31','source_status':'development_no_registry_entry','physical_promotion':0,
  'verification_group_count':len(checks),'checks_passed':True,
  'f_vectors':{'old':fvector(old),'stellar':fvector(stellar),'shell':fvector(shell),'filled':fvector(filled)},
  'shell_Betti3':1,'filled_Betti3':0,
  'normal_metric':{'det_G_full':'1/4','rank_G_full':4,'rank_G_visible':3,'rank_deficit':1},
  'stellar_refinement':{'counting_support_ratio':'4','boundary_cochain_preservation':True,'each_child_volume_ratio':'1/4','volume_weighted_support_ratio':'1','metric_dependence':'declared_volume_weighted_measure'},
  'support_prep':{'old_retained':'1/5','new_facets':'4/5','condition':'unweighted_C3_counting_norm_only'},
  'twist_cocycle':{'edge_assignments':2**10,'flat_assignments':len(flat),'flat_nontrivial_gauge_classes':0,'curvature_hist':dict(sorted(nonflat_hist.items()))},
  'twisted_graph':{'Nx':N,'Nfiber':M,'fiber_laplacian_weight':kappa,
                    'eigenvalues':[{'value':str(k),'multiplicity':v} for k,v in sorted(actual.items(),key=lambda x:float(x[0]))],
                    'untwisted_eigenvalues':[{'value':str(k),'multiplicity':v} for k,v in sorted(actual_u.items(),key=lambda x:float(x[0]))],
                    'visible_sector_eigenvalues':['0','2','2','4'],
                    'transverse_excitation_floor':'6',
                    'twist_is_detectable_in_odd_modes':True,
                    'four_dimensional_physical_promotion':False},
  'native_apex_birth_trigger':'OPEN__NOT_DERIVED_FROM_OMEGA0',
  'native_open_system_support_law':'OPEN__Q153_Q160_Q169_179',
  'native_metric_or_twist_selection':'OPEN',
  'method':'exact rational and radical symbolic checks; exhaustive 2^10 Z2 assignments; exact 16x16 graph diagonalization',
  'checks':checks
}
path=Path('/mnt/data/UD_K4_K5_OMEGA_APEX_TWIST_RESULTS_v0.4.json')
path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS',len(checks),'assertions')
print('f-vectors:',result['f_vectors'])
print('flat Z2 twists:',len(flat),'of',2**10,'curvature histogram',dict(sorted(nonflat_hist.items())))
print('twisted graph spec:',result['twisted_graph']['eigenvalues'])
print('twisted vs untwisted spectrum different:',actual!=actual_u)
print('low-sector projection exact and hidden normal rank check passed')
