#!/usr/bin/env python3
"""Independently authored audit; source code in imported DOCX files is never executed."""
import collections,hashlib,itertools as it,json,math,pathlib,sys
import numpy as np
import sympy as s
R=pathlib.Path(__file__).resolve().parent;W=R.parent;checks={}
def check(name,condition,**data):
 assert condition,(name,data)
 checks[name]={'passed':True,**data}
# The explicitly declared tree/chord split is source data, independently reconstructed here.
tree=[(0,4),(0,5),(0,6),(1,4),(1,7),(1,8),(2,5),(2,9),(3,6),(4,10),(4,11),(5,12),(7,13),(10,14)]
chords=[(2,7),(3,8),(3,9),(5,10),(6,11),(6,12),(7,10),(8,11),(8,13),(9,12),(9,13),(11,14),(12,14),(13,14)]
simplices=[t for k in range(1,5) for t in it.combinations(range(4),k)]
hasse={(i,j) for i,x in enumerate(simplices) for j,y in enumerate(simplices) if len(y)==len(x)+1 and set(x)<set(y)}
check('declared_14_14_Hasse_split',set(tree).isdisjoint(chords) and set(tree+chords)==hasse and len(hasse)==28)
def incidence(edges):
 Q=s.zeros(len(edges),15)
 for i,(u,v) in enumerate(edges):Q[i,u]=Q[i,v]=1
 return Q
S,H=incidence(tree),incidence(chords);C=H*S.T*(S*S.T).inv();M=s.eye(14).col_join(C);N=(-C.T).col_join(s.eye(14))
v=s.Matrix([-1]*4+[1]*6+[-1]*4+[1])
check('integer_path_factorization',H==C*S and all(x in [-1,0,1] for x in C),rank_S=S.rank(),rank_H=H.rank(),rank_C=C.rank())
check('parity_measurement_gauge',S.rank()==14 and S*v==s.zeros(14,1) and H*v==s.zeros(14,1))
check('covariance_embedding_and_constraints',M.rank()==14 and M.T*N==s.zeros(14) and N.rank()==14)
Sig=s.diag(*range(1,15));Sigma=M*Sig*M.T
check('positive_covariance_rank',Sigma.rank()==14 and Sigma*N==s.zeros(28,14),
      theorem='For PSD training covariance of rank r, rank(M Sigma M^T)=r and nullity=28-r')
sing=M*s.diag(1,*([0]*13))*M.T
check('singular_covariance_kernel_qualification',sing.rank()==1,rank=1,nullity=27,advertised_constraint_columns=14)
rowlengths=[sum(abs(x) for x in C.row(i)) for i in range(14)]
check('path_noise_amplification',max(rowlengths)>1,max_row_l1=int(max(rowlengths)),row_path_lengths=list(map(int,rowlengths)),
      deterministic_bound='epsilon_H + ||C||_infinity*epsilon_S')
L=(-C).row_join(s.eye(14))
check('common_field_error_blindness',L*M==s.zeros(14),blind_error_dimension=14)
Rc=L*L.T
check('independent_unit_noise_residual',Rc==s.eye(14)+C*C.T and Rc.is_positive_definite,
      covariance='sigma^2*(I+C*C^T), not zero')
bias=s.eye(14)[:,0];biased_noise=s.zeros(14,1).col_join(bias)
check('constant_bias_not_seen_by_covariance',L*biased_noise==bias and bias!=s.zeros(14,1),
      written_counterexample='e_S=0, e_H=b constant: mean residual b, covariance zero')
# An identity latent covariance: exact residual distribution is fixed entirely by sensor errors.
Q=s.Matrix(s.symbols('x0:15'));check('noiseless_pointwise_residual',H*Q-C*S*Q==s.zeros(14,1),gaussian_assumption_required=False)
# Build native skew A only to distinguish measurement parity from a conserved mode.
A=s.zeros(15)
for i,j in hasse:
 low,up=simplices[i],simplices[j];deleted=next(k for k in range(len(up)) if up[:k]+up[k+1:]==low);sign=(-1)**deleted
 A[i,j]=-sign;A[j,i]=sign
check('measurement_gauge_is_not_harmonic',A*v!=s.zeros(15,1),norm_Av_squared=int((A*v).dot(A*v)))
# Boolean pair orbits; this is a different domain from the 44 receipt alphabet.
bits=list(it.product(range(2),repeat=3));perms=list(it.permutations(range(3)))
pairset={frozenset(p) for p in it.combinations(bits,2)}
same={p for p in pairset if len({sum(x)%2 for x in p})==1};cross=pairset-same
def orbit_sizes(domain,group):
 todo=set(domain);out=[]
 while todo:
  pair=next(iter(todo));o={frozenset(tuple(x[g[j]]^comp for j in range(3)) for x in pair) for g,comp in group};out.append(o);todo-=o
 return sorted(map(len,out)),out
g6=[(p,0) for p in perms];g12=[(p,c) for p in perms for c in range(2)]
check('Boolean_pair_partitions',len(same)==12 and len(cross)==16 and orbit_sizes(same,g6)[0]==[3]*4
 and orbit_sizes(same,g12)[0]==[6,6] and orbit_sizes(cross,g12)[0]==[1,3,6,6])
stab=[(p,0) for p in perms if p[0]==0]
check('matching_stabilizer_orbits',orbit_sizes(same,stab)[0]==[1]*4+[2]*4 and orbit_sizes(cross,stab)[0]==[1]*4+[2]*6)
antipodes={frozenset((x,tuple(1-a for a in x))) for x in bits}
full=[(p,w) for p in perms for w in bits]
fullorbit={frozenset(tuple(x[p[j]]^w[j] for j in range(3)) for x in [(0,0,0),(1,1,1)]) for p,w in full}
check('singlet_group_scope',len(fullorbit)==4 and fullorbit==antipodes,
      restricted_S3_times_complement_orbit=1,full_affine_orbit=4,no_operator_or_attractor_derived=True)
# Cyclic cocycle and projective trivializing cochain in exact phase exponents.
n=13;mod=n*n;objects=list(it.product(range(n),repeat=2))
def w(a,b,c):return a*((b+c)//n)%n
check('cyclic_three_cocycle',all((w(b,c,d)+w(a,(b+c)%n,d)+w(a,b,c)-w((a+b)%n,c,d)-w(a,b,(c+d)%n))%n==0
 for a,b,c,d in it.product(range(n),repeat=4)),quadruples=n**4)
check('cyclic_nonthrivial_class_witness',sum(w(1,j,1) for j in range(n))%n==1,
      witness='product_j omega_k(1,j,1)=exp(2*pi*i*k/13), whereas coboundaries telescope to 1')
check('slant_coboundary_keeps_phase',all((a*x+a*y-a*((x+y)%n)-n*a*((x+y)//n))%mod==0 for a,x,y in it.product(range(n),repeat=3)),
      epsilon_a_x='exp(2*pi*i*k*a*x/169)',spin_a1_b0='exp(2*pi*i*k/169)')
def fusion(x,y,k):
 a,b=x;c,d=y;return ((a+c)%n,(b+d+2*k*((a+c)//n))%n)
def twist(x,k):a,b=x;return (n*a*b+k*a*a)%mod
def bilinear(x,y,k):a,b=x;c,d=y;return (n*(a*d+c*b)+2*k*a*c)%mod
check('twisted_fusion_and_balancing',all((twist(fusion(x,y,k),k)-twist(x,k)-twist(y,k)-bilinear(x,y,k))%mod==0
 for k in range(n) for x in objects for y in objects))
check('bilinear_nondegeneracy',all(any(bilinear(x,y,1)!=0 for y in objects) for x in objects if x!=(0,0)))
def order(x,k):
 y=(0,0)
 for j in range(1,mod+1):
  y=fusion(y,x,k)
  if y==(0,0):return j
check('twisted_fusion_group',order((1,0),0)==13 and all(order((1,0),k)==169 for k in range(1,n)),
      k0='C13 x C13',nonzero_k='C169',meaning='169 labels do not imply componentwise flux-charge addition')
check('pure_charge_isotropic_subgroup',all(twist((0,b),k)==0 and bilinear((0,b),(0,d),k)==0
 for k in range(n) for b,d in it.product(range(n),repeat=2)),order=13)
# Exact Gauss sum polynomial in zeta_169, with rational cyclotomic reduction.
z=s.symbols('z');phi=s.cyclotomic_poly(169,z)
check('normalized_Gauss_sum',all(s.rem(sum(z**twist(x,k) for x in objects)-13,phi,z)==0 for k in range(n)),
      normalized_sum=1,central_charge_mod_8=0)
# Finite-field reduction gives an exact disproof of the imported modular identity.
p=53;root=pow(2,4,p);assert pow(root,13,p)==1 and root!=1
Sin=np.array([[pow(root,(-(a*d+c*b))%13,p)*pow(13,-1,p)%p for c,d in objects] for a,b in objects],dtype=np.int64)
badT=np.array([pow(root,(a*b+7*a*a)%13,p) for a,b in objects],dtype=np.int64)
B=Sin*badT[None,:]%p;diff=(B@B%p@B-Sin@Sin)%p
bad=np.argwhere(diff!=0);i,j=map(int,bad[0])
check('imported_modular_identity_fails',len(bad)>0,modulus=p,primitive_root_13=root,
      witness_row=list(objects[i]),witness_column=list(objects[j]),residual=int(diff[i,j]),
      argument='A complex identity over Z[zeta_13,1/13] would survive this reduction')
# Necessary checks of repaired modular matrices in characteristic 677 (not a complex proof).
p2=677;root2=next(pow(g,4,p2) for g in range(2,p2) if pow(pow(g,4,p2),13,p2)!=1)
assert pow(root2,169,p2)==1
Sc=np.array([[pow(root2,(-bilinear(x,y,1))%169,p2)*pow(13,-1,p2)%p2 for y in objects] for x in objects],dtype=np.int64)
Tc=np.array([pow(root2,twist(x,1),p2) for x in objects],dtype=np.int64);U=Sc*Tc[None,:]%p2
check('repaired_modular_reduction',np.array_equal(U@U%p2@U%p2,Sc@Sc%p2),
      scope='exact necessary finite-field check; complex identities follow from metric-group character orthogonality and Gauss-sum proof')
certificate={'tree_edges':tree,'chord_edges':chords,'S':S.tolist(),'H':H.tolist(),'C':C.tolist(),
 'C_rank':C.rank(),'path_lengths':rowlengths,'residual_unit_noise_covariance':Rc.tolist(),
 'imported_modular_failure':checks['imported_modular_identity_fails']}
(R/'COVARIANCE_AND_PHASE_CERTIFICATES.json').write_text(json.dumps(certificate,default=int,indent=2)+'\n')
out={'passed':True,'check_families':len(checks),'checks':checks,'physical_promotion':0,
 'scope':'Finite algebra and repaired conditional examples; no independent review, native action, sensor, gapping protection or area law',
 'environment':{'python':sys.version,'sympy':s.__version__,'numpy':np.__version__}}
(R/'RESEARCH_BATCH4_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'passed':True,'check_families':len(checks),'path_lengths':list(map(int,rowlengths)),
 'modular_failure_witness':checks['imported_modular_identity_fails']}))
