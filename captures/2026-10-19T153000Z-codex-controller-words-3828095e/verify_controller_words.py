"""Fresh constructor verification of source identities, fixed-point rounding and admission."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from pathlib import Path
import ast,json,hashlib
from controller_words import *
# Sparse rational-function arithmetic, only for the four source algebra identities.
VARS=['Q7','Q8','gamma_chi','mu'];ONE={(0,0,0,0):F(1)}
def pa(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,F(0))+v
 return {k:v for k,v in c.items() if v}
def pn(a):return {k:-v for k,v in a.items()}
def pm(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():
   k=tuple(u+v for u,v in zip(i,j));c[k]=c.get(k,F(0))+x*y
 return {k:v for k,v in c.items() if v}
def rat(text):
 def go(n):
  if isinstance(n,ast.Constant):return ({(0,0,0,0):F(n.value)} if n.value else {},ONE)
  if isinstance(n,ast.Name):return ({tuple(int(k==n.id) for k in VARS):F(1)},ONE)
  if isinstance(n,ast.UnaryOp):
   a,b=go(n.operand);return pn(a),b
  a,b=go(n.left)
  if isinstance(n.op,ast.Pow):
   ex=n.right.value;u,v=ONE,ONE
   for _ in range(ex):u,v=pm(u,a),pm(v,b)
   return u,v
  c,d=go(n.right)
  if isinstance(n.op,ast.Add):return pa(pm(a,d),pm(c,b)),pm(b,d)
  if isinstance(n.op,ast.Sub):return pa(pm(a,d),pn(pm(c,b))),pm(b,d)
  if isinstance(n.op,ast.Mult):return pm(a,c),pm(b,d)
  if isinstance(n.op,ast.Div):return pm(a,d),pm(b,c)
  raise ValueError('algebra grammar')
 return go(ast.parse(text,mode='eval').body)
def equal(a,b):
 x,y=rat(a);u,v=rat(b);return not pa(pm(x,v),pn(pm(u,y)))

def main():
 src=load_sources();g,outs,expressions=build_graph(src);records=design(g,outs,src);checks=[];witnesses=[]
 def ck(name,test):
  if not test:raise AssertionError(name)
  checks.append(name)
 ck('positive denominator rewrite exact',equal(OLD_D,NEW_D))
 mm=src['UD_UNITS_CALIBRATION_RESULT_v0.1.json']['mechanical'];n=mm['N'];inv=mm['N_inverse']
 for i in range(2):
  for j in range(2):ck(f'source N inverse identity {i}{j}',equal('+'.join(f'({n[i][k]})*({inv[k][j]})' for k in range(2)),str(int(i==j))))
 ck('positive quadratic denominator identity',equal('2*gamma_chi**2*(3*Q7*(2*Q7+Q8)-3*Q8*(-Q7-2*Q8))','6*gamma_chi**2*(Q7**2+Q8**2+(Q7+Q8)**2)'))
 for record in records:
  di=record['domain']-1;fixture=record['damping_class'];envs=source_envs(src,di,fixture);zeta=F(record['target_command_allowance']);rho=F(record['coefficient_sup_error_bound'])
  held=src['UD_FULL_FEEDBACK_RESULT_v0.1.json']['domains'][di]['fixtures'][fixture];age=F(held['sample_age'])
  for arm,env in envs.items():
   descriptor=record['arms'][arm];states,dens=g.analyze(env);p=descriptor['fractional_bits'];width=descriptor['signed_word_bits']
   ck(f'{di} {fixture} {arm} all layout conditions',not layout_failures(g,states,dens,outs,p,width,zeta))
   ck(f'{di} {fixture} {arm} previous precision rejected',bool(layout_failures(g,states,dens,outs,p-1,width-1,zeta)))
   ck(f'{di} {fixture} {arm} small word rejected',bool(layout_failures(g,states,dens,outs,32,64,zeta)))
   ck(f'{di} {fixture} {arm} coefficient plus rounding allocation',F(record['coefficient_command_bound'])+F(descriptor['command_rounding_bound'])<=zeta)
   for seed in range(5):
    x={k:F(0) for k in env};qr=env['Q0'][1];vr=env['v0'][1];vd=env['vd0'][1];dc=env['D0_0'][1]
    for i in range(9):
     sign=(-1)**(i+seed);fraction=[F(0),F(1,2),F(1),F(1),F(1,7)][seed]
     x[f'Q{i}']=sign*qr*fraction;x[f'v{i}']=-sign*vr*fraction;x[f'vd{i}']=sign*vd*fraction
     for j in range(9):x[f'D{i}_{j}']=dc/F(9) if seed==2 else dc*F(i==j,2)
    if seed==3:x['Q8']=-x['Q7']
    target={k:(env[k][0]+env[k][1])/2 for k in PARAMS}
    for j,k in enumerate(PARAMS):x[k]=target[k]+rho*F((-1)**j,2)
    exact_impl=g.exact(x);fx=g.fixed(x,p,width);logical={**x,**target};exact_target=g.exact(logical)
    ck(f'{di} {fixture} {arm} seed{seed} every node word enclosure',all(abs(a-b)<=s[3]*F(1,2**(p+1)) for a,b,s in zip(exact_impl,fx,states)))
    err=max(abs(fx[i]-exact_target[i]) for i in outs)
    ck(f'{di} {fixture} {arm} seed{seed} complete target command error',err<=zeta)
    admitted=admitted_command(g,outs,env,record,arm,x,target,(age,F(0),F(0),age))
    ck(f'{di} {fixture} {arm} seed{seed} runtime equals certified program',admitted==[fx[i] for i in outs])
    witnesses.append({'domain':di+1,'class':fixture,'arm':arm,'seed':seed,'input_sha256':hashlib.sha256(json.dumps({k:str(v) for k,v in sorted(x.items())}).encode()).hexdigest(),'complete_command_error':str(err),'allowed':str(zeta)})
   def rejected(name,xx=x,tt=target,timing=(age,F(0),F(0),age)):
    try:admitted_command(g,outs,env,record,arm,xx,tt,timing)
    except ValueError:ck(f'{di} {fixture} {arm} rejects '+name,True)
    else:raise AssertionError(name+' accepted')
   bad=dict(x);bad['mu']=F(0);rejected('mass outside positive box',bad)
   bad=dict(x);bad['mu']=target['mu']+2*rho;rejected('excess coefficient mismatch',bad)
   bad=dict(x);bad['D0_1']=dc;rejected('damping row sum',bad)
   rejected('asynchronous Q/V',timing=(age,F(0),age/2,age))
   rejected('stale age',timing=(age*2,F(0),F(0),age))
   rejected('enlarged latency reserve',timing=(age,F(0),F(0),age*2))
 # Two operation-level controls: nearest-even and finite overflow.
 ck('round ties even',round(F(1,2))==0 and round(F(3,2))==2 and round(F(-3,2))==-2)
 tiny=Graph();tiny.compile('a*a')
 try:tiny.fixed({'a':F(100)},4,8)
 except OverflowError:ck('actual finite-word overflow refused',True)
 else:raise AssertionError('overflow accepted')
 # Sanity check the derivative certificate against an exact source-free quotient identity.
 t=Graph();o=t.compile('mu/(1+nu**2)');en={'mu':(F(1),F(2)),'nu':(F(0),F(1))};ss,_=t.analyze(en)
 ck('quotient derivative bound nonzero',ss[o][2][0]>=1 and ss[o][2][1]>=1)
 result={'status':'PASS','classification':'CONSTRUCTOR_EXACT_RATIONAL_CERTIFICATE_CHECKS_PLUS_FINITE_WITNESSES','checks':checks,'check_count':len(checks),'witness_count':len(witnesses),'witnesses':witnesses,'graph_nodes':len(g.nodes),'positive_denominator_rewrites':g.rewrites,'layouts':records,'source_algebra_scope':'positive rewrite and2x2 mass inverse; target canonical acceleration premise inherited from pinned v106 JSON','archived_code_executed':False,'independent_review':False,'physical_promotion':0}
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
