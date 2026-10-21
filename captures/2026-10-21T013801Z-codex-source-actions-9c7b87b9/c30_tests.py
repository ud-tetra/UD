from pathlib import Path
from fractions import Fraction as F
import argparse,subprocess,json,hashlib,importlib.util
ap=argparse.ArgumentParser();ap.add_argument('--workspace',type=Path,required=True);ap.add_argument('--operator',type=Path,required=True);ap.add_argument('--executable',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();P=a.workspace;a.out.mkdir(parents=True,exist_ok=False);H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();read=lambda n:list(map(int,(P/n).read_text().split()));S=2**96
lines=a.operator.read_text().splitlines();n,c,m,L,b=map(int,lines[0].split());obs=list(map(int,lines[1].split()));edges=[tuple(map(int,l.split()))for l in lines[3:]];assert len(edges)==int(lines[2])
x=read('c30_x.txt');xb=read('c30_x_boundary.txt');y=read('c30_y.txt');fx=read('c30_Fx.txt');fxb=read('c30_Fxb.txt');fty=read('c30_Fty.txt');assert len(x)==len(xb)==len(fty)==n and len(y)==len(fx)==len(fxb)==c*m
const=json.loads((P/'c30_math/ACTION_CONSTANTS.json').read_text());ef=F(const['forward_error_upper']);et=F(const['adjoint_error_upper']);norm2=lambda v:sum(t*t for t in v)
assert norm2(x)<(16*S)**2 and norm2(xb)<(2048*S)**2 and norm2(y)<(2049*S)**2
# Full-size duality is a consistency check, not the source of the universal action proof.
dual=F(sum(v*w for v,w in zip(fx,y))-sum(v*w for v,w in zip(x,fty)),S*S);dualcap=ef*2049+et*16;assert abs(dual)<dualcap
# The rounded action is not exactly linear; scale discrepancy must stay within rounding/action bounds.
linear=F(sum((u-128*v)**2 for u,v in zip(fxb,fx)),S*S);assert linear<(129*ef)**2
# Independently reproduce EVERY coordinate/term of each actual2640-state half-step.
controls=[]
def trunc(v,d):return (1 if v>=0 else -1)*(abs(v)//d)
for sign,mode in [(1,'step+'),(-1,'step-')]:
 out=a.out/(mode+'.txt');r=subprocess.run([str(a.executable),str(a.operator),mode,str(P/'c30_x_boundary.txt'),str(out)],capture_output=True,text=True);assert r.returncode==0,r.stderr
 term=[v*2**32 for v in xb];exact=term.copy()
 for k in range(1,41):
  acc=[0]*n
  for i,j,w in edges:acc[i]+=sign*w*term[j]
  term=[trunc(v,4*k)for v in acc];exact=[v+w for v,w in zip(exact,term)]
 exact=[trunc(v,2**32)for v in exact];got=list(map(int,out.read_text().split()));assert got==exact
 controls.append({'mode':mode,'status':'PASS_ALL2640_COMPILED_OUTPUTS_FROM40_TERM_REFERENCE','reference_term_coordinates_evaluated':2640*40,'compiled_output_coordinates_compared':2640,'output_sha256':H(out)})
# Invalid actual-domain inputs must be rejected before a trajectory is emitted.
bad=a.out/'bad_input.txt';bad.write_text(str(2049*S)+'\n'+'0\n'*(n-1));badout=a.out/'bad_output.txt';r=subprocess.run([str(a.executable),str(a.operator),'forward',str(bad),str(badout)],capture_output=True,text=True);assert r.returncode==1 and 'domain'in r.stderr and not badout.exists()
# Adapter hash binding rejects changed source bytes before any executable call.
spec=importlib.util.spec_from_file_location('new_oracles',P/'c30_oracles.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);expected=H(a.executable);mod.SourceActions(a.operator,a.executable,expected);changed=a.out/'changed_operator.txt';changed.write_bytes(a.operator.read_bytes()+b'\n');rejected=False
try:mod.SourceActions(changed,a.executable,expected)
except ValueError:rejected=True
assert rejected
bad_build_rejected=False
try:mod.SourceActions(a.operator,a.executable,'0'*64)
except ValueError:bad_build_rejected=True
assert bad_build_rejected
# Exact arithmetic backend controls exercise large positive/negative integer divisions and shifts
# through the independently reproduced full halfsteps, without accessing GMP internals.
result={'status':'PASS_ACTUAL_SOURCE_FORWARD_ADJOINT_AND_INTEGER_CONTROLS','actual_full_actions':[{'mode':'forward','input_dimension':n,'output_dimension':c*m,'input_sha256':H(P/'c30_x.txt'),'output_sha256':H(P/'c30_Fx.txt'),'input_norm_squared':str(F(norm2(x),S*S))},{'mode':'forward_boundary','input_dimension':n,'output_dimension':c*m,'input_sha256':H(P/'c30_x_boundary.txt'),'output_sha256':H(P/'c30_Fxb.txt'),'input_norm_squared':str(F(norm2(xb),S*S))},{'mode':'adjoint','input_dimension':c*m,'output_dimension':n,'input_sha256':H(P/'c30_y.txt'),'output_sha256':H(P/'c30_Fty.txt'),'input_norm_squared':str(F(norm2(y),S*S))}],'duality_residual':str(dual),'duality_absolute_upper':str(dualcap),'scale128_discrepancy_squared':str(linear),'halfstep_controls':controls,'failure_controls':{'outside_forward_domain_rejected':True,'changed_operator_adapter_rejected':True,'wrong_expected_executable_hash_rejected':True},'operator_sha256':H(a.operator),'source_sha256':H(P/'c30_action.cpp'),'adapter_sha256':H(P/'c30_oracles.py'),'actual_full8192_decoder_run':False,'actual_floating_estimator_calls':0,'physical_promotion':0,'external_promotion_review':'PENDING'}
(a.out/'ACTION_TESTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'full_actions':3,'reference_term_coordinates_evaluated':211200,'compiled_output_coordinates_compared':5280,'full_decoder':False},indent=2))
