import json,subprocess,sys,time
from bindings import P,freeze,sha
if __name__=='__main__':
 f=freeze();data=json.loads((P/'DATA_FREEZE.json').read_text());assert data['noise_freeze_sha256']==sha(P/'NOISE_FREEZE.json');runs=[]
 def execute(stage,args):
  t=time.monotonic()
  with (P/f'{stage}.log').open('x') as log:r=subprocess.run([sys.executable,*args],cwd=P,stdout=log,stderr=subprocess.STDOUT)
  runs.append({'stage':stage,'returncode':r.returncode,'seconds':time.monotonic()-t});(P/'RUN_EXECUTIONS.json').write_text(json.dumps(runs,indent=2));assert r.returncode==0
 execute('uniform',['uniform.py'])
 for e,r in zip(f['cases'],data['records']):
  n=e['case'];record=P/f'records/{n}.i64le';assert sha(record)==r['record_sha256'];execute('source_order-'+n,['source_order.py',n])
  for mode in ['original','instrumented']:
   out=P/f'results/original-{n}' if mode=='original' else P/f'results/new-{n}';execute(mode+'-'+n,['propose.py',str(record),str(out),*(['--instrument'] if mode=='instrumented' else [])])
   if mode=='instrumented':
    target=P/f'results/{n}'
    for x in out.iterdir():assert not (target/x.name).exists();x.rename(target/x.name)
    out.rmdir()
  o=P/f'results/{n}';audit=json.loads((o/'DISCOVERY.json').read_text())
  if not (o/'REPORT.json').exists() or audit['learned_order_float']!=209:
   (o/'ADAPTER_HOLD.json').write_text(json.dumps({'case':n,'status':'HOLD_SOURCE_ORDER_APPLICABILITY','reason':'Unchanged precision-cutoff floating order is not209; no forced truncation','learned_order':audit['learned_order_float']},indent=2));execute('order_replay-'+n,['source_order.py',n,'--replay']);continue
  assert sha(o/'PHASE_PROPOSAL.npz')==sha(P/f'results/original-{n}/PHASE_PROPOSAL.npz')
  for stage,args in [('source_witness',['propose_reference.py',n]),('certify',['certify.py',n]),('direct_error',['direct_error.py',n]),('order_replay',['source_order.py',n,'--replay']),('phase_replay',['certify.py',n,'--replay'])]:execute(stage+'-'+n,args)
 execute('validate',['validate.py'])
