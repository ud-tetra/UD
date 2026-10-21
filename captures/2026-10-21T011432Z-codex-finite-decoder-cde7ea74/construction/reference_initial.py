#!/usr/bin/env python3
"""Run the full recurrence on explicit SMALL rational controls, not600cell data."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,importlib.util
from flint import arb,ctx


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--decoder',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 spec=importlib.util.spec_from_file_location('new_reference_decoder',a.decoder);D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D);ctx.prec=192
 s=F(61,27648);C=1/s;U=[[F(5,13),F(-12,13),0,0],[F(12,13),F(5,13),0,0],[0,0,1,0],[0,0,0,1]];V=[[F(3,5),0,0,F(4,5)],[0,1,0,0],[0,0,1,0],[F(-4,5),0,0,F(3,5)]];sv=[s,F(1,2),F(1),F(0)]
 def trans(A):return list(map(list,zip(*A)))
 def mm(A,B):return [[sum((F(x)*y for x,y in zip(row,col)),F(0))for col in zip(*B)]for row in A]
 def mv(A,x):return [sum((F(v)*w for v,w in zip(row,x)),F(0))for row in A]
 def norm2(x):return sum((v*v for v in x),F(0))
 I=[[F(i==j)for j in range(4)]for i in range(4)];assert mm(trans(V),V)==I and mm(trans(U),U)==I
 B=mm([[U[i][j]*sv[j]for j in range(4)]for i in range(4)],trans(V));Bt=trans(B);A=mm(Bt,B);vh=[V[i][3]for i in range(4)];assert mv(A,vh)==[0]*4
 scale=D.STATE_SCALE;cap=F(1,2**67);noise=F(1,2**70)
 def quant(v):return (v.numerator*scale)//v.denominator
 cases=[]
 inputs=[('weak_unit_data',mv(U,[1,0,0,0]),False),('rotated_hidden_and_inconsistent_data',mv(U,[s/4,F(-1,6),F(1,5),F(1,7)]),False),('coherent_hidden_oracle_errors',mv(U,[1,0,0,0]),True)]
 for name,y,perturb in inputs:
  assert norm2(y)<=1
  gtrue=mv(Bt,y);gints=[quant(v+(noise*h if perturb else 0))for v,h in zip(gtrue,vh)];ge2=norm2([F(k,scale)-v for k,v in zip(gints,gtrue)]);assert ge2<=cap**2
  stats={'calls':0,'max_action_error_squared':F(0)}
  def normal(v):
   truth=mv(A,[F(x,scale)for x in v]);out=[quant(x-(noise*h if perturb else 0))for x,h in zip(truth,vh)];err=norm2([F(k,scale)-x for k,x in zip(out,truth)]);assert err<=cap**2;stats['calls']+=1;stats['max_action_error_squared']=max(stats['max_action_error_squared'],err);return out
  got,receipt=D.decode_from_adjoint(gints,normal,steps=8192)
  yi=mv(trans(U),y);exact=mv(V,[yi[i]/sv[i]if sv[i]else F(0)for i in range(4)]);actual=[F(x,scale)for x in got];err2=norm2([v-w for v,w in zip(actual,exact)]);bound=F(1,2**51)*C+F(11,2**46);assert err2<bound**2
  hidden=sum((x*h for x,h in zip(actual,vh)),F(0))
  if perturb:assert hidden!=0
  cases.append({'name':name,'status':'PASS_FULL8192_SMALL_OPERATOR_REFERENCE','dimension':4,'steps':8192,'g_error_squared':str(ge2),'max_normal_action_error_squared':str(stats['max_action_error_squared']),'output_dyadic_integers':got,'reference_minimum_norm_output':[str(x)for x in exact],'final_error_squared':str(err2),'verified_error_bound':str(bound),'computed_hidden_component':str(hidden),'arithmetic_receipt':receipt,'scope':'EXPLICIT_SMALL_RATIONAL_PROXY_NOT_600CELL'})
  print(name,'PASS',stats['calls'],'actions',flush=True)
 # A wrong oracle is detected by the exact control audit; the generic recurrence
 # alone cannot infer an opaque callback's mathematical truth.
 bad_calls=0;bad_rejected=False
 def bad_action(v):
  nonlocal bad_calls
  bad_calls+=1;truth=mv(A,[F(x,scale)for x in v]);out=[quant(x+(F(1,2**60)if bad_calls==17 and i==3 else 0))for i,x in enumerate(truth)];err=norm2([F(k,scale)-x for k,x in zip(out,truth)])
  if err>cap**2:raise ValueError('independent action audit rejects exceeded oracle budget')
  return out
 gints=[quant(v)for v in mv(Bt,inputs[0][1])]
 try:D.decode_from_adjoint(gints,bad_action,steps=20)
 except ValueError as e:bad_rejected='oracle budget'in str(e)
 assert bad_rejected and bad_calls==17
 round_rejected=False
 try:D.checked_quantize(arb('1 +/- 0.000001'))
 except ArithmeticError:round_rejected=True
 assert round_rejected
 # A bad nonzero kernel start would persist with zero g and A h=0; the API
 # deliberately has no initial-state parameter and always uses exact zero.
 assert mv(A,vh)==[0]*4
 result={'status':'PASS_REFERENCE_ARITHMETIC_AND_ADVERSARIAL_CONTROLS','full_8192_cases':cases,'failure_controls':{'bad_oracle_rejected_by_independent_control_audit':True,'bad_oracle_call':17,'wide_arithmetic_ball_rejected':True,'initial_hidden_state_must_be_zero':True},'decoder_source_sha256':hashlib.sha256(a.decoder.read_bytes()).hexdigest(),'actual_600cell_forward_or_adjoint_calls':0,'actual_600cell_decoder_run':False,'physical_promotion':0,'external_promotion_review':'PENDING'}
 (a.out/'REFERENCE_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 (a.out/'SMALL_OPERATOR.json').write_text(json.dumps({'scope':'RATIONAL_PROXY_CONTROL_NOT_600CELL','F':[[str(x)for x in row]for row in B],'normal_A':[[str(x)for x in row]for row in A],'U':[[str(x)for x in row]for row in U],'V':[[str(x)for x in row]for row in V],'singular_values':[str(x)for x in sv]},indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
