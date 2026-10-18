import subprocess,sys,time,json
from bindings import P,check
check();rows=[]
for script,args in [('propose_inverse.py',[]),('certify_budgets.py',[]),('controls.py',[]),('certify_budgets.py',['--replay']),('validate.py',[])]:
 start=time.monotonic();name=script.replace('.py','')+('-replay' if args else '')
 with (P/f'{name}.log').open('x') as log:r=subprocess.run([sys.executable,script,*args],cwd=P,stdout=log,stderr=subprocess.STDOUT)
 rows.append({'script':script,'args':args,'returncode':r.returncode,'seconds':time.monotonic()-start});(P/'RUN_EXECUTIONS.json').write_text(json.dumps(rows,indent=2));assert r.returncode==0
print(json.dumps(rows,indent=2))
