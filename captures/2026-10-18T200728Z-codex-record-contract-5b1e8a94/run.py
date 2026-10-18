import json,subprocess,time,sys
from bindings import P,freeze
if __name__=='__main__':
 freeze();runs=[]
 for name,args in [('project',['project.py']),('verify',['verify.py']),('raw_replay',['project.py','--raw-replay']),('proof_replay',['verify.py','--replay']),('validate',['validate.py'])]:
  t=time.monotonic()
  with (P/(name+'.log')).open('x') as out:r=subprocess.run([sys.executable,*args],cwd=P,stdout=out,stderr=subprocess.STDOUT)
  runs.append({'stage':name,'returncode':r.returncode,'seconds':time.monotonic()-t});(P/'RUN_EXECUTIONS.json').write_text(json.dumps(runs,indent=2));assert r.returncode==0
