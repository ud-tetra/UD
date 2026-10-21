"""Finite malformed and out-of-domain probes, with no universal intake claim."""
from pathlib import Path
import subprocess,json,hashlib,argparse
P=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--executable',type=Path,required=True);ap.add_argument('--source',type=Path,required=True);ap.add_argument('--operator',type=Path,required=True);a=ap.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();pins={k:sha(v) for k,v in vars(a).items()}
work=P/'work_rejections';work.mkdir(exist_ok=False)
zero=['0']*2640
fixtures=[]
for name,value in [('positive_parse_cap',(1<<112)+1),('negative_parse_cap',-((1<<112)+1)),('positive_signed128_boundary',1<<127),('negative_signed128_boundary',-(1<<127)),('domain_one_grid_excess',2048*(1<<96)+1),('malformed_double_sign','--1')]:
 entries=zero[:];entries[13]=str(value);fixtures.append((name,entries,a.operator))
fixtures.append(('truncated_input',zero[:-1],a.operator))
fixtures.append(('extra_input',zero+['0'],a.operator))
ops=work/'truncated_ne.txt';tokens=a.operator.read_text().split();ops.write_text(' '.join(tokens[:67])+'\n')
fixtures.append(('truncated_operator_before_ne',zero,ops))
results=[]
for name,entries,op in fixtures:
 inp=work/(name+'.txt');out=work/(name+'_OUT.txt');inp.write_text('\n'.join(entries)+'\n')
 run=subprocess.run([str(a.executable.resolve()),str(op.resolve()),'step+',str(inp),str(out)],text=True,capture_output=True)
 assert run.returncode!=0 and not out.exists(),(name,run.returncode,run.stdout,run.stderr)
 results.append({'name':name,'exit_code':run.returncode,'no_output':True,'stderr':run.stderr.strip()})
assert pins=={k:sha(v) for k,v in vars(a).items()}
(P/'REJECTION_CHECKS.json').write_text(json.dumps({'status':'PASS','cases':results,'source_bindings':pins,'scope':'finite negative probes only, not universal malformed-input proof','physical_promotion':0},indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','negative_cases':len(results)}))
