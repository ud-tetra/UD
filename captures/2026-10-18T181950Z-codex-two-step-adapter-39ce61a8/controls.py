"""Frozen actual-array corruption refusals, isolated from retained originals."""
import json,shutil,tempfile,subprocess,sys,os
from pathlib import Path
import numpy as np
from bindings import P,freeze,sha
if __name__=='__main__':
 rows=[];f=freeze();case='ramp_clock_stress';o=P/'results'/case
 if not (o/'SOURCE_WITNESS.npz').exists():
  (P/'CONTROL_RESULTS.json').write_text(json.dumps({'status':'HOLD_NO_APPLICABLE_ACTUAL_WITNESS','controls':[]},indent=2));sys.exit(0)
 before={p.name:sha(p) for p in o.glob('*.npz')}
 for mode in ['zero_source_inverse','tampered_emitted_phase']:
  with tempfile.TemporaryDirectory(prefix='ud-two-step-control-') as tmp:
   out=Path(tmp)/'work';shutil.copytree(P,out,ignore=shutil.ignore_patterns('__pycache__','CERTIFICATE.json','REPLAY_CERTIFICATE.json','controls.log'))
   c=out/'results'/case
   if mode=='zero_source_inverse':
    zpath=c/'SOURCE_WITNESS.npz'
    with np.load(zpath,allow_pickle=False) as z:d={k:z[k] for k in z.files}
    d['inverse'][:]=0;np.savez_compressed(zpath,**d)
   else:
    zpath=c/'PHASE_PROPOSAL.npz'
    with np.load(zpath,allow_pickle=False) as z:d={k:z[k] for k in z.files}
    d['two_step_phase'][0]+=1;np.savez_compressed(zpath,**d)
    # Preserve the original comparison and report binding so the emission test,
    # not a trivially stale external hash, sees the altered candidate.
    shutil.copyfile(zpath,out/f'results/original-{case}/PHASE_PROPOSAL.npz');rp=c/'REPORT.json';r=json.loads(rp.read_text());r['proposal_sha256']=sha(zpath);rp.write_text(json.dumps(r))
   r=subprocess.run([sys.executable,'certify.py',case],cwd=out,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'},capture_output=True,text=True)
   cert=c/'CERTIFICATE.json';status=json.loads(cert.read_text())['status'] if cert.exists() else None
   assert r.returncode!=0 or status!='CERTIFIED_ACTUAL_TWO_STEP_PHASE_MATCHING';rows.append({'control':mode,'returncode':r.returncode,'certificate_status':status,'rejected':True,'stderr_tail':r.stderr[-500:]})
 assert all(sha(o/n)==h for n,h in before.items());(P/'CONTROL_RESULTS.json').write_text(json.dumps({'status':'PASS','controls':rows,'original_arrays_unchanged':True,'physical_promotion':0},indent=2));print(json.dumps(rows,indent=2))
