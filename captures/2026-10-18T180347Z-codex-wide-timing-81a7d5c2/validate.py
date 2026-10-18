import json,subprocess,sys
from bindings import P,freeze,sha
from model import rules,source_tail
from fractions import Fraction as F

def run():
 f=freeze();cases=[]
 for e in f['cases']:
  o=P/'results'/e['case'];a=json.loads((o/'CERTIFICATE.json').read_text());b=json.loads((o/'REPLAY_CERTIFICATE.json').read_text())
  clean=lambda x:{k:v for k,v in x.items() if k not in ['replay'] and k!='rows'}
  assert clean(a)==clean(b);assert not a['replay'] and b['replay'];counts=[]
  for x,y in zip(a['rows'],b['rows']):
   assert {k:v for k,v in x.items() if k!='seconds'}=={k:v for k,v in y.items() if k!='seconds'}
   m=x['width'];assert x['rules']=={k:[v.numerator,v.denominator] for k,v in rules(m).items()};assert x['Gram_sha256']==sha(o/'GRAM.npz')
   r=x['counts']['common'];counts.append(r['above_count_lower'])
   for rule in ['common','scaled']:
    c=x['counts'][rule]
    if c['all_values_classified']:assert c['above_count_lower']==c['above_count_upper'] and c['above_count_upper']<=209
   assert F(*x['comparison_rank209_tail']['bound_squared'])==source_tail(m)
  assert all(a<=b for a,b in zip(counts,counts[1:]));cases.append({'case':e['case'],'rows':[{'width':r['width'],'counts':r['counts']} for r in a['rows']]})
 t=subprocess.run([sys.executable,'-m','unittest','discover','-v','-p','test_*.py'],cwd=P,capture_output=True,text=True);assert t.returncode==0,t.stderr;(P/'TEST_RESULTS.txt').write_text(t.stdout+t.stderr)
 return {'status':'PASS','cases':cases,'tests':5,'physical_promotion':0,'independent_review':'pending','phase_certificate_extended':False,'full_Hankel_certified':False,'exact_encoded_rank209_claimed':False}
if __name__=='__main__':
 r=run();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
