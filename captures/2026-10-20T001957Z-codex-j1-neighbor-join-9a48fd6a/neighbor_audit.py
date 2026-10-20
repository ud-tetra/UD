"""Uniform operation-level floating certificate plus software-oracle trace controls."""
import sys
sys.dont_write_bytecode=True
import ast,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import neighbor_evaluator as ev
from rounding import bits,frombits,round64,pow2
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
SOURCE=HERE
P2=HERE
U=F(1,2**53);TINY=F(1,2**1075);GRID=2**120
OPS=[('dw','sub','omega','OMEGA0'),('sw','add','omega','OMEGA0'),('s','mul','dw','sw'),('t','mul','TWO_GAMMA','dw'),('pr','mul','s','M_R'),('qr','mul','t','M_I'),('cr','add','pr','qr'),('real','add','J_R','cr'),('pi','mul','s','M_I'),('qi','mul','t','M_R'),('ci','sub','pi','qi'),('imag','add','J_I','ci')]

def sqrtup(x):
 assert x>=0
 s=10**30;n=isqrt(x.numerator*s*s//x.denominator)
 if F(n*n,s*s)<x:n+=1
 y=F(n,s);assert y*y>=x
 return y

def ceilgrid(x):
 assert x>=0
 return F(-((-x.numerator*GRID)//x.denominator),GRID)

def op(x,y,name):return x+y if name=='add' else x-y if name=='sub' else x*y

def interval(a,b,name):
 l,h,ea=a;ll,hh,eb=b;ma=max(abs(l),abs(h));mb=max(abs(ll),abs(hh))
 if name=='mul':
  products=[l*ll,l*hh,h*ll,h*hh];lo,hi=min(products),max(products);prop=ma*eb+mb*ea+ea*eb
 else:
  lo,hi=(l+ll,h+hh) if name=='add' else (l-hh,h-ll);prop=ea+eb
 mag=max(abs(lo),abs(hi));assert mag+prop<16,'overflow exclusion bound failed'
 error=ceilgrid(prop+U*(mag+prop)+TINY)
 assert error>=prop+U*(mag+prop)+TINY
 return lo,hi,error

def check_program():
 tree=ast.parse((HERE/'neighbor_evaluator.py').read_text());fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='trace');tail=fn.body[-13:]
 assert len(tail)==13
 for stmt,(name,kind,a,b) in zip(tail[:-1],OPS):
  assert isinstance(stmt,ast.Assign) and len(stmt.targets)==1 and isinstance(stmt.targets[0],ast.Name) and stmt.targets[0].id==name
  assert isinstance(stmt.value,ast.BinOp) and isinstance(stmt.value.left,ast.Name) and stmt.value.left.id==a and isinstance(stmt.value.right,ast.Name) and stmt.value.right.id==b
  assert type(stmt.value.op)=={'add':ast.Add,'sub':ast.Sub,'mul':ast.Mult}[kind]
 assert isinstance(tail[-1],ast.Return) and isinstance(tail[-1].value,ast.List) and [x.id for x in tail[-1].value.elts]==[x[0] for x in OPS]
 return True

def certify(rho,exact):
 w0=F(289,64);lo,hi=w0-rho,w0+rho
 nodes={k:(x,x,abs(F.from_float(getattr(ev,k))-x)) for k,x in exact.items()};nodes['omega']=(lo,hi,F(0));details=[]
 for name,kind,a,b in OPS:
  nodes[name]=interval(nodes[a],nodes[b],kind);l,h,e=nodes[name];details.append({'node':name,'op':kind,'args':[a,b],'exact_interval':[str(l),str(h)],'uniform_absolute_error':str(e)})
 ee=sqrtup(nodes['real'][2]**2+nodes['imag'][2]**2)
 raw=(SOURCE/'UPPER_RESULTS.json').read_bytes();d=json.loads(raw);mass=sum(F(x) for x in d['full_state_mass'][:2]);res=sqrtup(F(d['defect_squared']))+sqrtup(F(d['local_lift_budget_squared']))
 dz2=(rho*(2*w0+rho))**2+(rho/5)**2;kappa=sqrtup(1+((w0+rho)*5)**2);model=kappa*(res+sqrtup(dz2)*sqrtup(mass)/2)**2
 return {'halfwidth':str(rho),'omega_interval':[str(lo),str(hi)],'gamma':'1/10','nodes':details,'component_evaluation_bounds':[str(nodes['real'][2]),str(nodes['imag'][2])],'complex_evaluation_bound':str(ee),'exact_model_continuum_radius':str(model),'total_actual_floating_continuum_radius':str(model+ee),'target':'1/10','precision_passed':model+ee<=F(1,10)}

def main():
 assert sys.float_info.radix==2 and sys.float_info.mant_dig==53 and sys.float_info.max_exp==1024 and sys.float_info.min_exp==-1021 and sys.float_info.rounds==1
 assert check_program()
 wit=json.loads((HERE/'EVALUATOR_WITNESS.json').read_text());d=json.loads((SOURCE/'UPPER_RESULTS.json').read_text());mr,mi,mc=map(F,d['full_state_mass']);exact={'J_R':F(d['J'][0]),'J_I':F(d['J'][1]),'M_R':mr-mi,'M_I':2*mc,'TWO_GAMMA':F(1,5),'OMEGA0':F(289,64)}
 assert wit['exact_constants']=={k:str(v) for k,v in exact.items()}
 for k,x in exact.items():assert getattr(ev,k).hex()==wit['constant_hex'][k] and bits(round64(x))==bits(getattr(ev,k))
 records=[certify(F(r),exact) for r in ['1/1000','1/500','1/200','1/125','17/2000']];cert=records[-1];assert cert['precision_passed'] and records[2]['precision_passed'];assert list(map(F,cert['omega_interval']))==[ev.LOWER,ev.UPPER]
 # All positive binary64 frequencies in this binade have uniform spacing 2^-50.
 first=bits(round64(ev.LOWER));last=bits(round64(ev.UPPER))
 while F.from_float(frombits(first))<ev.LOWER:first+=1
 while F.from_float(frombits(last))>ev.UPPER:last-=1
 assert F.from_float(frombits(first-1))<ev.LOWER<=F.from_float(frombits(first)) and F.from_float(frombits(last))<=ev.UPPER<F.from_float(frombits(last+1))
 assert F.from_float(frombits(first+1))-F.from_float(frombits(first))==F(1,2**50)
 count=last-first+1;samples={first+i for i in range(32)}|{last-i for i in range(32)}|{bits(ev.OMEGA0)+i for i in range(-32,33)}|{first+(last-first)*i//1024 for i in range(1025)}
 seed=0x4a315032
 for i in range(512):seed=(1664525*seed+1013904223)%(2**32);samples.add(first+(last-first)*seed//(2**32))
 max_error=[F(0)]*12;max_output=F(0);sample_rows=[];envelope=[F(x['uniform_absolute_error']) for x in cert['nodes']]
 for word in sorted(samples):
  w=frombits(word);native=ev.trace(w);ref={k:F.from_float(getattr(ev,k)) for k in exact};ref['omega']=F.from_float(w);ideal=dict(exact);ideal['omega']=F.from_float(w)
  for i,(name,kind,a,b) in enumerate(OPS):
   rn=round64(op(ref[a],ref[b],kind));assert bits(rn)==bits(native[i]),'native/software oracle mismatch';ref[name]=F.from_float(rn);ideal[name]=op(ideal[a],ideal[b],kind);err=abs(ref[name]-ideal[name]);assert err<=envelope[i];max_error[i]=max(max_error[i],err)
  wq=F.from_float(w);dzr=-(wq*wq-F(289,64)**2);dzi=wq/5-F(289,320)
  closed=[exact['J_R']-dzr*exact['M_R']+dzi*exact['M_I'],exact['J_I']-dzr*exact['M_I']-dzi*exact['M_R']]
  assert closed==[ideal['real'],ideal['imag']],'operation family differs from exact J0-(z-z0) mass identity'
  got=ev.evaluate(w);assert bits(got.real)==bits(native[7]) and bits(got.imag)==bits(native[11]);out_err=(F.from_float(got.real)-ideal['real'])**2+(F.from_float(got.imag)-ideal['imag'])**2;assert out_err<=F(cert['complex_evaluation_bound'])**2;max_output=max(max_output,out_err)
  if word in [first,last,bits(ev.OMEGA0),bits(ev.OMEGA0)-1,bits(ev.OMEGA0)+1]:sample_rows.append({'input_hex':w.hex(),'output_hex':[got.real.hex(),got.imag.hex()],'exact_error_squared':str(out_err),'native_oracle_trace_equal':True})
 # Oracle controls exercise tie-even, both sides of ties and subnormal rounding independently of this program's scale.
 oracle_cases=[(F(1)+pow2(-53),1.0),(F(1)+3*pow2(-53),frombits(bits(1.0)+2)),(pow2(-1075),0.0),(3*pow2(-1075),frombits(2)),(pow2(-1022)-pow2(-1075),frombits(1<<52)),(-(F(1)+pow2(-53)),-1.0)]
 for x,want in oracle_cases:assert bits(round64(x))==bits(want)
 controls=[]
 for name,x in [('below lower boundary',frombits(first-1)),('above upper boundary',frombits(last+1)),('NaN',float('nan')),('positive infinity',float('inf')),('negative infinity',-float('inf')),('integer input',4),('string input','4.5')]:
  try:ev.evaluate(x)
  except ValueError:controls.append(name)
  else:raise AssertionError(name+' accepted')
 bad=ev.trace(ev.OMEGA0);bad[7]=frombits(bits(bad[7])+1);assert bits(bad[7])!=bits(ev.evaluate(ev.OMEGA0).real);controls.append('one-ULP corrupted output differs from frozen oracle')
 center_actual=ev.evaluate(ev.OMEGA0);assert F.from_float(center_actual.real)!=exact['J_R'] or F.from_float(center_actual.imag)!=exact['J_I'];controls.append('omitting constant quantization gives a false zero center budget')
 sourcep2=json.loads((P2/'P2_WITNESS.json').read_text());old=[F.from_float(float.fromhex(x)) for x in sourcep2['reported_corrected_hex']];new=ev.evaluate(ev.OMEGA0);change=sqrtup((F.from_float(new.real)-old[0])**2+(F.from_float(new.imag)-old[1])**2)
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_NEIGHBOR_UNIFORM_ACTUAL_BINARY64_BAND','source_upper_results_sha256':hashlib.sha256((SOURCE/'UPPER_RESULTS.json').read_bytes()).hexdigest(),'source_evaluator_sha256':hashlib.sha256((HERE/'neighbor_evaluator.py').read_bytes()).hexdigest(),'source_witness_sha256':hashlib.sha256((HERE/'EVALUATOR_WITNESS.json').read_bytes()).hexdigest(),'IEEE_model':{'rounding':'binary64 round-to-nearest ties-to-even, one rounded operation per explicit AST node; no contraction/FMA','unit_roundoff':str(U),'absolute_underflow_term':str(TINY),'rounding_lemma':'|RN(x)-x|<=2^-53 |x|+2^-1075; derived from binary64 spacing; exact-operation magnitudes plus propagated error <16 exclude overflow','error_rounding_grid':'2^-120 upward; does not model arithmetic, only compresses rational upper bounds','runtime_binary64_preconditions_checked':True,'native_operation_sequence_AST_matched':True,'status':'CONDITIONAL ON DECLARED IEEE OPERATION MODEL; native/software trace controls are constructor checks, not proof of every runtime/platform'},'constant_quantization_errors':{k:str(abs(F.from_float(getattr(ev,k))-x)) for k,x in exact.items()},'records':records,'accepted_float_domain':{'rational_endpoints':[str(ev.LOWER),str(ev.UPPER)],'first_hex':frombits(first).hex(),'last_hex':frombits(last).hex(),'spacing':'1/1125899906842624','number_of_binary64_inputs':count,'proof_scope':'Uniform bound covers every accepted binary64 input by interval/error propagation; sampled oracle traces are supplemental runtime controls.'},'native_trace_controls':{'inputs_checked':len(samples),'operations_per_input':len(OPS),'total_node_comparisons':len(samples)*len(OPS),'closed_exact_estimator_identity_checks':len(samples),'per_node_max_observed_errors':[str(x) for x in max_error],'max_observed_complex_evaluation_error_upper':str(sqrtup(max_output)),'boundary_and_center_records':sample_rows,'independent_oracle_rounding_cases':len(oracle_cases),'controls':controls},'center_output_change_from_original_sparse_reported_J_upper':str(change),'lineage_scope':'Same frozen P2 state/exact corrected family; new compact evaluator with newly rounded constants, not the original sparse-matrix output pipeline or a new Galerkin solve.','limitations':'Input frequency denotes its exact represented binary64 value; no decimal parsing, measurement uncertainty or physical Hertz calibration guarantee. No full [0,6]x[0.1,1] band, global IEEE implementation verification, independent review, finite mesh termination or native UD action claim.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0}
 p=HERE/'FLOATING_BAND_RESULTS.json'
 if p.exists():assert json.loads(p.read_text())==result;print('read-only uniform floating-band replay matches results',flush=True)
 else:p.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS inputs='+str(count)+' sampled traces='+str(len(samples))+' eval bound='+str(float(F(cert['complex_evaluation_bound'])))+' model+float band radius='+str(float(F(cert['total_actual_floating_continuum_radius']))),flush=True)
if __name__=='__main__':main()
