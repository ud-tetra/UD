import subprocess,json,sys,time
from bindings import P,freeze,sha
if __name__=='__main__':
 freeze();runs=[]
 def go(stage,args):
  t=time.monotonic()
  with (P/(stage+'.log')).open('x') as out:r=subprocess.run([sys.executable,*args],cwd=P,stdout=out,stderr=subprocess.STDOUT)
  runs.append({'stage':stage,'returncode':r.returncode,'seconds':time.monotonic()-t});(P/'RUN_EXECUTIONS.json').write_text(json.dumps(runs,indent=2));assert r.returncode==0
 go('baseline',['baseline.py']);go('uniform',['uniform.py']);go('raw_baseline_replay',['baseline.py','--raw-replay']);go('raw_noise',['make_record.py']);go('raw_noise_regeneration',['make_record.py','--regenerate',str(P.parent/'uniform-two-noise-regenerated/cyclic_unit.i64le')])
 go('order',['source_order.py','cyclic_unit'])
 for mode in ['original','instrumented']:
  out=P/('results/original-cyclic_unit' if mode=='original' else 'results/new-cyclic_unit');go(mode,['propose.py',str(P/'records/cyclic_unit.i64le'),str(out),*(['--instrument'] if mode=='instrumented' else [])])
  if mode=='instrumented':
   for x in out.iterdir():assert not (P/'results/cyclic_unit'/x.name).exists();x.rename(P/'results/cyclic_unit'/x.name)
   out.rmdir()
 for stage,args in [('source_witness',['propose_reference.py','cyclic_unit']),('actual_certificate',['certify.py','cyclic_unit']),('actual_replay',['certify.py','cyclic_unit','--replay']),('direct_error',['direct_error_v2.py','cyclic_unit']),('order_replay',['source_order.py','cyclic_unit','--replay']),('uniform_replay',['uniform.py','--replay']),('validate',['validate.py'])]:go(stage,args)
