from fractions import Fraction as Q
from pathlib import Path
import json
P=Path(__file__).resolve().parent
M=lambda a:[[Q(x)for x in row]for row in a]
def T(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum(x*y for x,y in zip(row,col))for col in T(b)]for row in a]
def sub(a,b):return [[x-y for x,y in zip(r,s)]for r,s in zip(a,b)]
def inv(a):
 n=len(a);w=[row[:]+[Q(i==j)for j in range(n)]for i,row in enumerate(a)]
 for j in range(n):
  k=next((i for i in range(j,n)if w[i][j]),None)
  if k is None:raise ValueError('singular')
  w[j],w[k]=w[k],w[j];d=w[j][j];w[j]=[x/d for x in w[j]]
  for i in range(n):
   if i!=j:
    d=w[i][j];w[i]=[x-d*y for x,y in zip(w[i],w[j])]
 return [r[n:]for r in w]
def pinv_fullrow(a):return mul(T(a),inv(mul(a,T(a))))
def norm2col(a):return sum(row[0]**2 for row in a)
F=M([[1,0],[0,0]]);Y=M([[Q(3,5)],[Q(4,5)]]);C=mul(T(Y),F);B=mul(pinv_fullrow(C),T(Y));Proj=M([[1,0],[0,0]])
assert mul(B,F)==Proj and B==M([[1,Q(4,3)],[0,0]])
scaled=[[2*x for x in row]for row in Y];assert mul(pinv_fullrow(mul(T(scaled),F)),T(scaled))==B
angle={'BF_equals_full_projection':True,'gain_squared':str(sum(x*x for x in B[0])),'omitting_angle_bound_fails':sum(x*x for x in B[0])>1,'nonzero_trial_scaling_changes_no_decoder':True}
d=Q(1,16);F=M([[1,0,0],[0,1,0]]);Y=M([[1,0],[0,1]]);C=F;D=M([[0,0,d],[d,0,0]]);G=[[x+y for x,y in zip(a,b)]for a,b in zip(C,D)]
assert mul(D,T(D))==M([[d*d,0],[0,d*d]])
Bg=mul(pinv_fullrow(G),T(Y));P3=M([[1,0,0],[0,1,0],[0,0,0]]);defect=sub(mul(Bg,F),P3);e=mul(defect,M([[1],[0],[0]]));e2=norm2col(e)
assert e2>(d/(1-d))**2 and e2<d*d+(d/(1-d))**2
assert e[2][0]!=0 and mul(mul(Bg,F),M([[0],[0],[1]]))==M([[0],[0],[0]])
approx={'D_operator_error_exact':str(d),'visible_input_error_squared':str(e2),'single_debit_bound_fails':True,'orthogonal_combination_bound_covers':True,'visible_input_can_have_spurious_nominal_hidden_output':True,'nominal_hidden_input_still_gives_zero_exact_data':True}
try:pinv_fullrow(M([[0,0]]));raise AssertionError('rank loss not detected')
except ValueError:pass
C=M([[1,0]]);Bbad=mul(pinv_fullrow(C),M([[2]]));assert mul(Bbad,M([[1,0]]))==M([[2,0],[0,0]])
# Nonzero finite solve/RHS/lift residuals, checked against the supplied-record rule.
H=mul(G,T(G));z=M([[Q(1,3)],[Q(-2,5)]]);a=mul(inv(H),z);ahat=[[a[0][0]+Q(1,1024)],[a[1][0]-Q(1,512)]];zhat=[[z[0][0]+Q(1,4096)],[z[1][0]+Q(1,4096)]]
lift=M([[Q(1,8192)],[Q(-1,8192)],[Q(1,8192)]]);xhat=[[u[0]+v[0]]for u,v in zip(mul(T(G),ahat),lift)];exact=mul(pinv_fullrow(G),z)
ez=sum(abs(v[0])for v in sub(zhat,z));er=sum(abs(v[0])for v in sub(mul(H,ahat),zhat));el=sum(abs(v[0])for v in lift);budget=(ez+er)/(1-d)+el;error2=norm2col(sub(xhat,exact));assert error2<budget*budget
result={'status':'PASS','fixtures':{'range_angle_and_scale':angle,'q2_cross_rotation':approx,'rank_loss_at_error_equal_floor_rejected':True,'compression_rhs_mismatch_at_zero_C_error_produces_defect_one':True,'nonzero_solve_residual':{'error_squared':str(error2),'budget':str(budget),'RHS_error_l1_cap':str(ez),'solve_residual_l1_cap':str(er),'lift_error_l1_cap':str(el)}},'scope':'independent exact rational small matrices; no full source compression or actual inverse computed','physical_promotion':0}
(P/'EXACT_FIXTURE_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print('PASS exact range-angle, scale, cross-rotation, rank-loss, RHS and solve fixtures')
