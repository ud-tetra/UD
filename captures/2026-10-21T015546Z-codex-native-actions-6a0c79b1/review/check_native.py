#!/usr/bin/env python3
"""Independent signed integer104-grid reference, not producer code."""
from pathlib import Path
import argparse,subprocess,json,hashlib
P=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--executable',type=Path,required=True);ap.add_argument('--source',type=Path,required=True);ap.add_argument('--operator',type=Path,required=True);args=ap.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
initial={k:sha(v) for k,v in vars(args).items()}
assert initial['operator']=='cca3ed7e671b8397c3940921d9845399425fd2558cc62708941c00fc4b899950'
nums=list(map(int,args.operator.read_text().split()));assert nums[:5]==[2640,62,4096,40,128]
rows=[[] for _ in range(2640)]
assert nums[67]==14880
for at in range(68,len(nums),3):
 i,j,w=nums[at:at+3];rows[i].append((j,w))
def trunc(x,d):return (1 if x>=0 else -1)*(abs(x)//d)
def reference(inp,sign):
 term=[x*256 for x in inp];out=term[:];maxterm=maxacc=maxout=0
 for k in range(1,41):
  nextterm=[]
  for row in rows:
   accum=0
   for j,w in row:
    product=sign*w*term[j];assert abs(product)<2**127
    accum+=product;maxacc=max(maxacc,abs(accum));assert abs(accum)<2**123
   nextterm.append(trunc(accum,4*k))
  term=nextterm;maxterm=max(maxterm,max(map(abs,term)));out=[x+y for x,y in zip(out,term)];maxout=max(maxout,max(map(abs,out)));assert maxout<2**121
 return [trunc(x,256) for x in out],{'max_partial_row_abs':maxacc,'max_term_abs':maxterm,'max_partial_output_abs':maxout}
scale=2**96
zero=[0]*2640
dense=[(((i*i*97+31*i+11)%257)-128)*2**83 for i in range(2640)]
pos=[0]*2640;pos[2040]=2048*scale
neg=[0]*2640;neg[2049]=-2048*scale
work=P/'work_native';work.mkdir(exist_ok=False)
cases=[]
for name,seed in [('zero',zero),('mixed_signed',dense),('positive_boundary_top',pos),('negative_boundary_top',neg)]:
 assert sum(x*x for x in seed)<=(2048*scale)**2
 inp=work/(name+'.txt');inp.write_text(''.join(str(x)+'\n' for x in seed))
 for sign,mode in [(1,'step+'),(-1,'step-')]:
  out=work/(name+mode+'.txt')
  run=subprocess.run([str(args.executable.resolve()),str(args.operator.resolve()),mode,str(inp),str(out)],text=True,capture_output=True)
  assert run.returncode==0,(run.returncode,run.stdout,run.stderr)
  actual=list(map(int,out.read_text().split()));expected,extrema=reference(seed,sign)
  assert actual==expected and len(actual)==2640
  cases.append({'name':name,'mode':mode,'all_components_match':True,'components':2640,'input_sha256':sha(inp),'output_sha256':sha(out),'reference_extrema':extrema,'backend_stderr':run.stderr.strip()})
assert initial=={k:sha(v) for k,v in vars(args).items()}
result={'status':'PASS','source_bindings':initial,'cases':cases,'delivered_output_coordinates_compared':len(cases)*2640,'independent_reference_term_coordinate_divisions':len(cases)*2640*40,'scope':{'producer_scripts_not_executed':True,'compiled_backend_intermediate_terms_not_claimed_exported_or_compared':True,'finite_probes_not_universal_runtime_proof':True,'no_full8192_run':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'NATIVE_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','coordinates':len(cases)*2640}))
