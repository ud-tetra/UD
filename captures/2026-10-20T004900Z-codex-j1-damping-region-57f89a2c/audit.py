"""Exact rational rectangle and rounding proofs; native two-input oracle controls."""
import sys
sys.dont_write_bytecode=True
import ast,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import evaluator as ev
from rounding import bits,frombits,round64,pow2
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
U=F(1,2**53);TINY=F(1,2**1075);GRID=2**120
OPS=[('dw','sub','omega','OMEGA0'),('sw','add','omega','OMEGA0'),('s','mul','dw','sw'),('dg','sub','gamma','GAMMA0'),('p','mul','gamma','dw'),('q','mul','OMEGA0','dg'),('v','add','p','q'),('t','mul','TWO','v'),('pr','mul','s','M_R'),('qr','mul','t','M_I'),('cr','add','pr','qr'),('real','add','J_R','cr'),('pi','mul','s','M_I'),('qi','mul','t','M_R'),('ci','sub','pi','qi'),('imag','add','J_I','ci')]

def sqrtup(x):
 assert x>=0
 s=10**30;n=isqrt(x.numerator*s*s//x.denominator)
 if F(n*n,s*s)<x:n+=1
 y=F(n,s);assert y*y>=x
 return y

def ceilgrid(x):
 assert x>=0
 return F(-((-x.numerator*GRID)//x.denominator),GRID)

def op(a,b,kind):return a+b if kind=='add' else a-b if kind=='sub' else a*b

def interval(a,b,kind):
 l,h,ea=a;ll,hh,eb=b;ma=max(abs(l),abs(h));mb=max(abs(ll),abs(hh))
 if kind=='mul':
  products=[l*ll,l*hh,h*ll,h*hh];lo,hi=min(products),max(products);prop=ma*eb+mb*ea+ea*eb
 else:
  lo,hi=(l+ll,h+hh) if kind=='add' else (l-hh,h-ll);prop=ea+eb
 mag=max(abs(lo),abs(hi));assert mag+prop<16
 error=ceilgrid(prop+U*(mag+prop)+TINY)
 assert error>=prop+U*(mag+prop)+TINY
 return lo,hi,error

def check_program():
 tree=ast.parse((HERE/'evaluator.py').read_text())
 fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='trace');tail=fn.body[-17:]
 assert len(tail)==17
 for stmt,(name,kind,a,b) in zip(tail[:-1],OPS):
  assert isinstance(stmt,ast.Assign) and len(stmt.targets)==1 and isinstance(stmt.targets[0],ast.Name) and stmt.targets[0].id==name
  assert isinstance(stmt.value,ast.BinOp) and isinstance(stmt.value.left,ast.Name) and stmt.value.left.id==a and isinstance(stmt.value.right,ast.Name) and stmt.value.right.id==b
  assert type(stmt.value.op)=={'add':ast.Add,'sub':ast.Sub,'mul':ast.Mult}[kind]
 assert isinstance(tail[-1],ast.Return) and isinstance(tail[-1].value,ast.List) and [x.id for x in tail[-1].value.elts]==[x[0] for x in OPS]
 fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='evaluate')
 expected=ast.parse('def evaluate(omega,gamma):\n nodes=trace(branch(omega,gamma),omega,gamma)\n return complex(nodes[11],nodes[15])').body[0]
 assert ast.dump(fn,include_attributes=False)==ast.dump(expected,include_attributes=False)
 fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='branch')
 expected=ast.parse("def branch(omega,gamma):\n w,g=validated(omega,gamma)\n return 'original' if w<=SWITCH else 'neighbor'").body[0]
 assert ast.dump(fn,include_attributes=False)==ast.dump(expected,include_attributes=False)

def word_domain(lo,hi):
 first,last=bits(round64(lo)),bits(round64(hi))
 while F.from_float(frombits(first))<lo:first+=1
 while F.from_float(frombits(last))>hi:last-=1
 assert F.from_float(frombits(first-1))<lo<=F.from_float(frombits(first))
 assert F.from_float(frombits(last))<=hi<F.from_float(frombits(last+1))
 assert first>>52==last>>52 and first<=last
 spacing=F.from_float(frombits(first+1))-F.from_float(frombits(first))
 assert spacing==pow2((first>>52)-1023-52)
 return {'first_word':first,'last_word':last,'first_hex':frombits(first).hex(),'last_hex':frombits(last).hex(),'count':last-first+1,'spacing':str(spacing),'rational_endpoints':[str(lo),str(hi)]}

def certify(leaf,exact,gmax):
 wc=exact['OMEGA0'];gc=exact['GAMMA0'];rho=ev.RHO;lo,hi=wc-rho,wc+rho
 assert ev.GAMMA_LOWER==gc and gmax>=gc and lo>0
 nodes={k:(x,x,abs(F.from_float(ev.CONSTANTS[leaf][k])-x)) for k,x in exact.items()}
 nodes['omega']=(lo,hi,F(0));nodes['gamma']=(gc,gmax,F(0));details=[]
 for name,kind,a,b in OPS:
  nodes[name]=interval(nodes[a],nodes[b],kind)
  l,h,e=nodes[name];details.append({'node':name,'op':kind,'args':[a,b],'ideal_interval':[str(l),str(h)],'uniform_absolute_error':str(e)})
 ee=sqrtup(nodes['real'][2]**2+nodes['imag'][2]**2)
 wit=json.loads((HERE/'EVALUATOR_WITNESS.json').read_text())
 d=json.loads((REPO/wit['source_upper_results'][leaf]).read_text())
 mass=sum(F(x) for x in d['full_state_mass'][:2]);d2=F(d['defect_squared']);nu2=F(d['local_lift_budget_squared'])
 res=sqrtup(d2)+sqrtup(nu2)
 realmax=rho*(2*wc+rho);imagmax=2*(gmax*hi-gc*wc)
 # Bounds attained simultaneously at upper corner. Negative lower-corner magnitudes are smaller.
 assert realmax==hi*hi-wc*wc>=wc*wc-lo*lo>=0
 assert imagmax>=2*gc*rho>=0
 dz2=realmax**2+imagmax**2
 for w in [lo,hi]:
  for g in [gc,gmax]:assert (w*w-wc*wc)**2+4*(g*w-gc*wc)**2<=dz2
 kappa=sqrtup(1+(hi/(2*gc))**2)
 shifted=res+sqrtup(dz2)*sqrtup(mass)/2
 model=kappa*shifted**2
 return {'leaf':leaf,'omega_interval':[str(lo),str(hi)],'gamma_interval':[str(gc),str(gmax)],'halfwidth':str(rho),'frozen_center':[str(wc),str(gc)],'defect_squared':str(d2),'local_lift_squared':str(nu2),'full_state_L2_squared':str(mass),'center_residual_Vprime_upper':str(res),'delta_z_components_upper':[str(realmax),str(imagmax)],'delta_z_squared_upper':str(dz2),'kappa_upper':str(kappa),'shifted_residual_Vprime_upper':str(shifted),'nodes':details,'component_evaluation_bounds':[str(nodes['real'][2]),str(nodes['imag'][2])],'complex_evaluation_bound':str(ee),'exact_model_continuum_radius':str(model),'total_actual_floating_continuum_radius':str(model+ee),'target':'1/10','precision_passed':model+ee<=F(1,10)}

def sample_pairs(wd,gd,wc):
 wf,wl=wd['first_word'],wd['last_word'];gf,gl=gd['first_word'],gd['last_word']
 pairs={(wf+(wl-wf)*i//32,gf+(gl-gf)*j//32) for i in range(33) for j in range(33)}
 pairs|={(w,g) for w in [wf,wl,bits(float(wc)),bits(float(ev.SWITCH))] for g in [gf,gl,(gf+gl)//2] if wf<=w<=wl}
 pairs|={(bits(float(wc))+i,g) for i in range(-32,33) for g in [gf,gl]}
 seed=0x4a315032
 for i in range(1024):
  seed=(1664525*seed+1013904223)%(2**32);w=wf+(wl-wf)*seed//(2**32)
  seed=(1664525*seed+1013904223)%(2**32);g=gf+(gl-gf)*seed//(2**32)
  pairs.add((w,g))
 return pairs

def trace_audit(leaf,exact,cert,wd,gd):
 envelope=[F(x['uniform_absolute_error']) for x in cert['nodes']];max_error=[F(0)]*len(OPS);max_output=F(0)
 pairs=sample_pairs(wd,gd,exact['OMEGA0'])
 for ww,gg in sorted(pairs):
  w,g=frombits(ww),frombits(gg);native=ev.trace(leaf,w,g)
  ref={k:F.from_float(ev.CONSTANTS[leaf][k]) for k in exact};ideal=dict(exact)
  for d in [ref,ideal]:d['omega']=F.from_float(w);d['gamma']=F.from_float(g)
  for i,(name,kind,a,b) in enumerate(OPS):
   rn=round64(op(ref[a],ref[b],kind));assert bits(rn)==bits(native[i]),'native/software oracle mismatch'
   ref[name]=F.from_float(rn);ideal[name]=op(ideal[a],ideal[b],kind)
   err=abs(ref[name]-ideal[name]);assert err<=envelope[i];max_error[i]=max(max_error[i],err)
  wq,gq=F.from_float(w),F.from_float(g);dzr=-(wq*wq-exact['OMEGA0']**2);dzi=2*(gq*wq-exact['GAMMA0']*exact['OMEGA0'])
  closed=[exact['J_R']-dzr*exact['M_R']+dzi*exact['M_I'],exact['J_I']-dzr*exact['M_I']-dzi*exact['M_R']]
  assert closed==[ideal['real'],ideal['imag']]
  err2=(F.from_float(native[11])-closed[0])**2+(F.from_float(native[15])-closed[1])**2
  assert err2<=F(cert['complex_evaluation_bound'])**2;max_output=max(max_output,err2)
  if ev.branch(w,g)==leaf:
   got=ev.evaluate(w,g);assert bits(got.real)==bits(native[11]) and bits(got.imag)==bits(native[15])
 return {'sampled_input_pairs':len(pairs),'operations_per_pair':len(OPS),'native_oracle_node_comparisons':len(pairs)*len(OPS),'exact_closed_estimator_identity_checks':len(pairs),'per_node_max_observed_errors':[str(e) for e in max_error],'max_observed_complex_evaluation_error_upper':str(sqrtup(max_output))}

def main():
 assert (sys.float_info.radix,sys.float_info.mant_dig,sys.float_info.max_exp,sys.float_info.min_exp,sys.float_info.rounds)==(2,53,1024,-1021,1)
 check_program()
 contract=json.loads((HERE/'CONTRACT.json').read_text())
 for x in contract['source_dependencies']:
  p=REPO/x['path'];assert p.stat().st_size==x['size_bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256']
 wit=json.loads((HERE/'EVALUATOR_WITNESS.json').read_text());records={};domains={};traces={};controls=[]
 gd=word_domain(ev.GAMMA_LOWER,ev.GAMMA_UPPER)
 assert gd['spacing']==str(F(1,2**56))
 for leaf,c in wit['exact_constants'].items():
  exact={k:F(v) for k,v in c.items()};d=json.loads((REPO/wit['source_upper_results'][leaf]).read_text());mr,mi,mc=map(F,d['full_state_mass'])
  assert exact==dict(J_R=F(d['J'][0]),J_I=F(d['J'][1]),M_R=mr-mi,M_I=2*mc,OMEGA0=ev.CENTERS[leaf],GAMMA0=F(1,10),TWO=F(2))
  for k,x in exact.items():assert ev.CONSTANTS[leaf][k].hex()==wit['constant_hex'][leaf][k] and bits(round64(x))==bits(ev.CONSTANTS[leaf][k])
  cert=certify(leaf,exact,ev.GAMMA_UPPER);assert cert['precision_passed'];records[leaf]=cert
  wd=word_domain(*map(F,cert['omega_interval']));domains[leaf]=wd
  traces[leaf]=trace_audit(leaf,exact,cert,wd,gd)
 # A wider box does not inherit this certificate: same conservative envelope exceeds target.
 rejected=certify('original',{k:F(v) for k,v in wit['exact_constants']['original'].items()},F(101,1000))
 assert not rejected['precision_passed'];controls.append('gamma upper 0.101 fails the declared conservative 0.1 certificate; not a physical impossibility claim')
 overlap_lo=max(F(x['omega_interval'][0]) for x in records.values());overlap_hi=min(F(x['omega_interval'][1]) for x in records.values())
 assert overlap_lo<ev.SWITCH<overlap_hi and ev.SWITCH==F(577,128)
 union=word_domain(ev.LOWER,ev.UPPER);overlap=word_domain(overlap_lo,overlap_hi)
 assert union['count']==sum(d['count'] for d in domains.values())-overlap['count']
 cut=bits(float(ev.SWITCH));assert F.from_float(frombits(cut))==ev.SWITCH
 assert domains['original']['first_word']==union['first_word']<=cut<=domains['original']['last_word']
 assert domains['neighbor']['first_word']<=cut+1<=union['last_word']==domains['neighbor']['last_word']
 selected_counts={'original':cut-union['first_word']+1,'neighbor':union['last_word']-cut};assert sum(selected_counts.values())==union['count']
 selector_checks=0
 for ww in [union['first_word'],cut-1,cut,cut+1,union['last_word']]:
  for gg in [gd['first_word'],gd['last_word'],(gd['first_word']+gd['last_word'])//2]:
   w,g=frombits(ww),frombits(gg);leaf=ev.branch(w,g);assert leaf==('original' if ww<=cut else 'neighbor')
   n=ev.trace(leaf,w,g);out=ev.evaluate(w,g);assert bits(out.real)==bits(n[11]) and bits(out.imag)==bits(n[15]);selector_checks+=1
 bad_switch=overlap_lo-ev.RHO;assert not overlap_lo<=bad_switch<=overlap_hi;controls.append('selector outside overlap fails rectangle containment')
 goodw,goodg=frombits(cut),frombits(gd['first_word'])
 bads=[('frequency below union',frombits(union['first_word']-1),goodg),('frequency above union',frombits(union['last_word']+1),goodg),('gamma below rectangle',goodw,frombits(gd['first_word']-1)),('gamma above rectangle',goodw,frombits(gd['last_word']+1))]
 for arg in ['omega','gamma']:
  for label,x in [('NaN',float('nan')),('positive infinity',float('inf')),('negative infinity',-float('inf')),('integer',1),('boolean',True),('string','0.1')]:bads.append((arg+' '+label,x if arg=='omega' else goodw,x if arg=='gamma' else goodg))
 for name,w,g in bads:
  try:ev.evaluate(w,g)
  except ValueError:controls.append(name+' rejected')
  else:raise AssertionError(name+' accepted')
 for leaf in records:
  other='neighbor' if leaf=='original' else 'original';w=frombits(domains[other]['first_word'] if other=='original' else domains[other]['last_word'])
  try:ev.trace(leaf,w,goodg)
  except ValueError:controls.append('out-of-leaf '+leaf+' rejected')
  else:raise AssertionError('out-of-leaf accepted')
 assert F.from_float(float(0.1))>F(1,10) and F.from_float(frombits(gd['first_word']))==F.from_float(float(0.1))
 assert all(F.from_float(ev.CONSTANTS[n]['GAMMA0'])!=F(1,10) for n in records)
 controls.append('gamma0 constant quantization explicitly nonzero; float 0.1 differs from exact fixed gamma 1/10')
 for x,want in [(F(1)+pow2(-53),1.0),(F(1)+3*pow2(-53),frombits(bits(1.0)+2)),(pow2(-1075),0.0),(3*pow2(-1075),frombits(2)),(pow2(-1022)-pow2(-1075),frombits(1<<52)),(-(F(1)+pow2(-53)),-1.0)]:assert bits(round64(x))==bits(want)
 bad=ev.evaluate(goodw,goodg);assert bits(frombits(bits(bad.real)+1))!=bits(bad.real);controls.append('one-ULP output corruption differs from frozen native trace')
 radius=max(F(c['total_actual_floating_continuum_radius']) for c in records.values());assert radius<F(1,10)
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_TWO_INPUT_JOINED_BINARY64_RECTANGLE','source_evaluator_sha256':hashlib.sha256((HERE/'evaluator.py').read_bytes()).hexdigest(),'source_witness_sha256':hashlib.sha256((HERE/'EVALUATOR_WITNESS.json').read_bytes()).hexdigest(),'source_contract_sha256':hashlib.sha256((HERE/'CONTRACT.json').read_bytes()).hexdigest(),'dependency_hash_checks':len(contract['source_dependencies']),'IEEE_model':{'rounding':'binary64 RN ties-to-even, one operation per 16 AST nodes; no contraction/FMA','unit_roundoff':str(U),'absolute_underflow_term':str(TINY),'error_upward_grid':'2^-120','lemma':'|RN(x)-x|<=2^-53*|x|+2^-1075; propagated magnitudes<16 exclude overflow','runtime_shape_and_AST_checked':True,'scope':'Conditional semantics; supplemental native/software traces are constructor checks, not every-platform proof'},'constant_quantization_errors':{n:{k:str(abs(F.from_float(ev.CONSTANTS[n][k])-F(x))) for k,x in c.items()} for n,c in wit['exact_constants'].items()},'leaf_certificates':records,'accepted_input_domains':{'gamma':gd,'leaf_frequencies':domains,'joined_frequency':union,'overlap_frequency':overlap,'selected_frequency_word_counts':selected_counts,'joined_binary64_input_pair_count':union['count']*gd['count'],'uniform_proof_scope':'Every accepted pair covered by rational interval/error propagation; no enumeration of all pairs claimed.'},'join':{'frequency_interval':[str(ev.LOWER),str(ev.UPPER)],'gamma_interval':[str(ev.GAMMA_LOWER),str(ev.GAMMA_UPPER)],'switch':str(ev.SWITCH),'overlap_interval':[str(overlap_lo),str(overlap_hi)],'overlap_width':str(overlap_hi-overlap_lo),'no_uncovered_binary64_pair':True,'selector_checks':selector_checks,'uniform_total_radius':str(radius),'maximum_uniform_evaluation_radius':str(max(F(c['complex_evaluation_bound']) for c in records.values())),'target':'1/10','precision_passed':True,'output_semantics':'Exact parameter selector, no interpolation. Continuity/differentiability of selected approximate output not asserted.'},'native_trace_controls':traces,'controls':controls,'rejected_wider_box':{'gamma_upper':'101/1000','original_leaf_total_radius':rejected['total_actual_floating_continuum_radius'],'precision_passed':False,'meaning':'Failure of this sufficient envelope only, not NO-GO for continuum/state/other certificates.'},'parameter_semantics':contract['parameter_semantics'],'lineage':'Reuse original and neighbor P2/flux witnesses without modification. New scalar evaluator/rounding proof; no new solve or physical calibration.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0}
 p=HERE/'RECTANGLE_RESULTS.json'
 if p.exists():assert json.loads(p.read_text())==result;print('read-only rectangle replay matches saved results',flush=True)
 else:p.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS pair count='+str(union['count']*gd['count'])+' traces='+str(sum(t['sampled_input_pairs'] for t in traces.values()))+' nodes='+str(sum(t['native_oracle_node_comparisons'] for t in traces.values()))+' uniform radius='+str(float(radius))+' eval='+str(float(F(result['join']['maximum_uniform_evaluation_radius']))),flush=True)

if __name__=='__main__':main()
