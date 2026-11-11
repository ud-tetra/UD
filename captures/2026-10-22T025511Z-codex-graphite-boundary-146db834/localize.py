from pathlib import Path
import json,numpy as np
p=Path(__file__).resolve().parent;f=json.loads((p/'FREEZE.json').read_text());rows=[]
for c in f['cases']:
 a=np.load(p/c/'ESTIMATES.npz');Q=a['one_sided'];avg=a['averaged'];diff=Q[:,:,0]-Q[:,:,1];j,k,i=np.unravel_index(np.argmax(abs(diff)),diff.shape);ladder=[dict(h_A=h,max_side_difference=float(np.max(abs(diff[:,kk]))),worst_fixed_component=float(diff[j,kk,i]),worst_fixed_Qplus=float(Q[j,kk,0,i]),worst_fixed_Qminus=float(Q[j,kk,1,i])) for kk,h in enumerate(f['steps_A'])];flags=[]
 for jj in range(len(Q)):
  sa=np.max(abs(diff[jj]));sr=max(np.linalg.norm(diff[jj,kk])/np.linalg.norm(avg[jj,kk]) for kk in range(3));st=np.max(abs(np.diff(Q[jj],axis=0)));strr=max(np.linalg.norm(Q[jj,kk+1,s]-Q[jj,kk,s])/np.linalg.norm(avg[jj,kk+1]) for kk in range(2) for s in range(2));aa=np.max(abs(np.diff(avg[jj],axis=0)));ar=max(np.linalg.norm(avg[jj,kk+1]-avg[jj,kk])/np.linalg.norm(avg[jj,kk+1]) for kk in range(2));bad=[key for key,v in dict(side_abs=sa>=1e-6,side_rel=sr>=1e-5,step_abs=st>=1e-6,step_rel=strr>=1e-5,average_abs=aa>=1e-6,average_rel=ar>=1e-5).items() if v]
  if bad:flags.append(dict(probe=jj,kind='column' if jj<81 else 'direction',failed=bad,side_max=float(sa),side_relative=float(sr),step_max=float(st),average_step_max=float(aa)))
 rows.append(dict(case=c,worst_probe=int(j),worst_component=int(i),worst_step_index=int(k),ladder=ladder,complete_failed_probe_register=flags))
(p/'LOCALIZATION.json').write_text(json.dumps(dict(cases=rows,interpretation='Measured fixed-step behavior only. Bitwise repeatability does not distinguish deterministic floating-point cancellation from truncation or another branch effect. No unique source attribution is inferred.'),indent=2)+'\n');print(json.dumps([{k:r[k] for k in ['case','worst_probe','worst_component','ladder']} for r in rows],indent=2))
