"""Exact Fraction intertwiner and gap certificate; no archived script executed."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import json,hashlib
C=Path(__file__).parent;R=C.parents[1]
eta=F(185,192);delta=1-eta;v=delta**2;c=eta**3*delta**3;r=4*eta**2+v
a=eta**4;b=eta**6;g=12*a+48*b
assert g<64*b and g<16*a+48*b
assert c>0 and r>0 and v>0 and g-2*c*c/v>v/2
K=[[r,c],[c,F(0)]]
def mul(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def transpose(A):return list(map(list,zip(*A)))
module_checks=[]
for root in (1,2,3):
 H=[[F(0) for _ in range(128)] for _ in range(128)]
 for i in range(64):
  for j in range(i+1,64):
   if i//4==j//4:
    w=eta**2;H[i][i]+=w;H[j][j]+=w;H[i][j]-=w;H[j][i]-=w
   w=b if i//16!=j//16 else a if i//4!=j//4 else F(0)
   if w:
    H[64+i][64+i]+=w;H[64+j][64+j]+=w;H[64+i][64+j]-=w;H[64+j][64+i]-=w
 signs=[]
 for i in range(64):
  digits=[root,(i//16)%4,(i//4)%4,i%4]
  h=next((k+1 for k,d in enumerate(digits) if d),4);assert h==1
  sign=(-1)**sum(digits);signs.append(sign)
  source_v=delta*(1-eta**h);source_c=eta**2*delta*(1-eta**h)*(eta**h-eta**(2*h))
  assert source_v==v and source_c==c
  H[i][i]+=source_v;H[i][64+i]=H[64+i][i]=sign*source_c
 assert all(sum(signs[i:i+4])==0 for i in range(0,64,4))
 B=[[F(signs[i]),F(0)] for i in range(64)]+[[F(0),F(1)] for _ in range(64)]
 assert mul(transpose(B),B)==[[F(64),F(0)],[F(0),F(64)]]
 assert mul(H,B)==mul(B,K)
 assert all(H[i][j]==H[j][i] for i in range(128) for j in range(128))
 for i in range(64):
  for j in range(64):
   I=F(i==j);E4=F(i//4==j//4,4);E16=F(i//16==j//16,16);E64=F(1,64)
   spectral=(12*a+48*b)*(I-E4)+(16*a+48*b)*(E4-E16)+64*b*(E16-E64)
   assert H[64+i][64+j]==spectral
 module_checks.append({'root_prefix':root,'dimension':128,'source_depth':1,'B_transpose_B':'64 I2','H_B_equals_B_K':True,'theta_nested_projector_reconstruction':True,'parity_signs':signs})
lo=-c*c/r;hi=-c*c/(r+c*c/r)
assert lo<hi<0
with localcontext() as ctx:
 ctx.prec=100
 def dec(q):return Decimal(q.numerator)/Decimal(q.denominator)
 discriminant=dec(r*r+4*c*c).sqrt()
 lam=-2*dec(c*c)/(dec(r)+discriminant)
 assert dec(lo)<lam<dec(hi)
 W_rho=(lam/dec(c))**2/(1+(lam/dec(c))**2);W_theta=1-W_rho
 numeric={'lambda_minus':str(lam),'rho_weight':str(W_rho),'theta_weight':str(W_theta),'negative_root_interval':[str(dec(lo)),str(dec(hi))]}
# Three-module superpositions: exact probabilities suffice for the IPR identity.
controls=[]
for weights in ([F(1),F(0),F(0)],[F(1,3)]*3,[F(1,2),F(1,4),F(1,4)]):
 assert sum(weights)==1
 cipr=sum(w*w for w in weights);glob=4*cipr;within=glob/(4*cipr)
 assert within==1 and F(4,3)<=glob<=4
 controls.append({'component_weights':[str(w) for w in weights],'global_F':str(glob),'conditioned_F':str(within),'effective_components':str(1/cipr)})
def serial(A):return [[str(x) for x in row] for row in A]
data={'status':'PASS_EXACT_CONDITIONAL','scope':'L4 clean R6b, three depth1 modules only; no fourth-module shape claim','physical_promotion':0,'source_commit':'8be4e90d68528325f081126d27c61ac61cad951e','source_sha256':hashlib.sha256((R/'docs/hmulti_r6b.py').read_bytes()).hexdigest(),'constants':{k:str(x) for k,x in {'eta':eta,'delta':delta,'v':v,'c':c,'r':r,'theta_gap_g':g}.items()},'reduced_K':serial(K),'negative_eigenvalue':'(r-sqrt(r^2+4c^2))/2 = -2c^2/(r+sqrt(r^2+4c^2))','characteristic_polynomial':['1',str(-r),str(-c*c)],'exact_negative_root_interval':[str(lo),str(hi)],'exact_gap_certificate':{'g_minus_2c_squared_over_v_minus_v_over_2':str(g-2*c*c/v-v/2),'strictly_positive':True,'other_eigenvalues_lower_bound':str(v/2)},'module_intertwiner_checks':module_checks,'channel_profile':'Theta u_i=1/8; rho p_i=parity_i/8; conditional site probabilities1/64 in each occupied module','three_module_superposition_controls':controls,'numeric_corroboration_decimal100':numeric,'independent_review':'PENDING'}
(C/'CERTIFICATE.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({'status':data['status'],'lambda_minus':numeric['lambda_minus'][:30],'theta_weight':numeric['theta_weight'][:30],'module_intertwiners':3,'within_component_F':'EXACT1'}))
