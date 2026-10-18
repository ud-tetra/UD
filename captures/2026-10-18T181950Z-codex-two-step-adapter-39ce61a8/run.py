import json,subprocess,sys,time
from bindings import P,freeze,sha
if __name__=='__main__':
 runs=[]
 def execute(stage,args):
  t=time.monotonic()
  with (P/f'{stage}.log').open('x') as log:r=subprocess.run([sys.executable,*args],cwd=P,stdout=log,stderr=subprocess.STDOUT)
  runs.append({'stage':stage,'returncode':r.returncode,'seconds':time.monotonic()-t});(P/'RUN_EXECUTIONS.json').write_text(json.dumps(runs,indent=2));assert r.returncode==0
 for e in freeze()['cases']:
  n=e['case'];record=P.parent/f'floating-timing-work/records/{n}.i64le';execute('source_order-'+n,['source_order.py',n,'--records',str(record.parent)])
  for mode in ['original','instrumented']:
   out=P/f'results/{n}' if mode=='instrumented' else P/f'results/original-{n}'
   # Source order receipts already occupy results/case. Run adapter in a fresh
   # directory then move its new outputs into that case without replacing files.
   if mode=='instrumented':out=P/f'results/actual-new-{n}'
   execute(mode+'-'+n,['propose.py',str(record),str(out),*(['--instrument'] if mode=='instrumented' else [])])
   if mode=='instrumented':
    target=P/f'results/{n}'
    for x in out.iterdir():assert not (target/x.name).exists();x.rename(target/x.name)
    out.rmdir()
  o=P/f'results/{n}';q=1+104*len(e['classes']);report=json.loads((o/'REPORT.json').read_text()) if (o/'REPORT.json').exists() else None
  if report is None or report['learned_order']!=q:
   (o/'ADAPTER_HOLD.json').write_text(json.dumps({'case':n,'status':'HOLD_SOURCE_ORDER_APPLICABILITY','actual_order':None if report is None else report['learned_order'],'expected_target_order':q},indent=2));execute('order_replay-'+n,['source_order.py',n,'--replay']);continue
  assert sha(o/'PHASE_PROPOSAL.npz')==sha(P/f'results/original-{n}/PHASE_PROPOSAL.npz')
  for stage,args in [('source_witness',['propose_reference.py',n]),('certify',['certify.py',n]),('order_replay',['source_order.py',n,'--replay']),('phase_replay',['certify.py',n,'--replay'])]:execute(stage+'-'+n,args)
 execute('controls',['controls.py']);execute('validate',['validate.py'])
