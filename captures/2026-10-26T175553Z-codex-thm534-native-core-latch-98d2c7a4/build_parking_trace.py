"""Extend the certified v2.20 prefix without resetting at pulse 192."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
import json
import numpy as np
from scipy.linalg import solve
import native_model as m
prior=json.loads(Path('SCHEDULE_CERTIFICATE.json').read_text())
prior['steps']=prior['steps'][:192]
parking=json.loads(Path('parking_search.json').read_text())['stages'][0]
den=prior['trace_denominator']
cur=np.array(prior['steps'][-1]['q_numerators'],dtype=float)/den
steps=prior['steps'].copy()
for h,num in zip(parking['masks'],parking['steps_numerator']):
    t=num/parking['step_denominator'];a=np.array(m.native(h),dtype=float)
    cur=solve(np.eye(23)-t*a/2,(np.eye(23)+t*a/2)@cur,check_finite=False)
    ints=[int(round(v*den)) for v in cur]
    steps.append({'stage':4,'mask':h,'t':str(m.Q(num,parking['step_denominator'])),'q_numerators':ints})
    cur=np.array(ints,dtype=float)/den
Path('SCHEDULE_CERTIFICATE.json').write_text(json.dumps({'format':'native-cayley-rational-trace-v2-parking','trace_denominator':den,'steps':steps},separators=(',',':'))+'\n')
