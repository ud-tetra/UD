import json,sys,subprocess,time
from bindings import P,freeze
if __name__=='__main__':
 f=freeze();rows=[]
 for e in f['cases']:
  n=e['case']
  for stage,args in [('project',['project.py',n,'--records',str(P.parent/'floating-timing-work/records')]),('certify',['certify.py',n]),('project_replay',['project.py',n,'--records',str(P.parent/'floating-timing-work/records'),'--replay']),('certify_replay',['certify.py',n,'--replay'])]:
   t=time.monotonic()
   with (P/f'{stage}-{n}.log').open('x') as log:r=subprocess.run([sys.executable,*args],cwd=P,stdout=log,stderr=subprocess.STDOUT)
   rows.append({'case':n,'stage':stage,'returncode':r.returncode,'seconds':time.monotonic()-t});(P/'RUN_EXECUTIONS.json').write_text(json.dumps(rows,indent=2));assert r.returncode==0
 r=subprocess.run([sys.executable,'validate.py'],cwd=P);assert r.returncode==0
