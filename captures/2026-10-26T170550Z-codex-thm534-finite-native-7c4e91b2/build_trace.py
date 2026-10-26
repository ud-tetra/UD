"""Numerical trace proposal; all claims are rechecked by verify_schedule.py."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from scipy.linalg import solve
from pathlib import Path
import json
import native_model as m
D=10**14
data=json.loads(Path('schedule_search.json').read_text())
cur=np.array(m.checkpoints()[0],dtype=float)
steps=[]
for stage,s in enumerate(data['stages'],1):
    for h,num in zip(s['masks'],s['steps_numerator']):
        dt=num/s['step_denominator'];a=np.array(m.native(h),dtype=float)
        cur=solve(np.eye(23)-dt*a/2,(np.eye(23)+dt*a/2)@cur,check_finite=False)
        ints=[int(round(v*D)) for v in cur]
        steps.append({'stage':stage,'mask':h,'t':str(m.Q(num,s['step_denominator'])),'q_numerators':ints})
        cur=np.array(ints,dtype=float)/D
Path('SCHEDULE_CERTIFICATE.json').write_text(json.dumps({'format':'native-cayley-rational-trace-v1','trace_denominator':D,'steps':steps},separators=(',',':'))+'\n')
