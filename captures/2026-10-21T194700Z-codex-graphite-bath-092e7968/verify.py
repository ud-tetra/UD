from pathlib import Path
import json,hashlib,numpy as np
p=Path(__file__).resolve().parent;base=p.parent;r=json.loads((p/'RESULTS.json').read_text());a=np.load(p/'CONTROLS.npz');checked=[]
assert hashlib.sha256((p/'CONTROLS.npz').read_bytes()).hexdigest()==r['controls_sha256']
for fn,sha in r['input_sha256'].items():assert hashlib.sha256((base/fn).read_bytes()).hexdigest()==sha
for row in r['rows']:
 key=f"{row['case']}_c{row['cutoff_A']}_w{row['width_A']}";Y=a[key+'_Y'];K=a[key+'_K'];g=a[key+'_g'];n=len(K);rank=row['response_rank'];assert np.linalg.norm(K@Y-g)/np.linalg.norm(g)<1e-12
 # QR reconstructs the dark/bright span independently of the SVD constructor.
 U=np.linalg.qr(Y,mode='reduced')[0];P=U@U.T;ref={'isotropic':np.eye(n)/n,'dark':(np.eye(n)-P)/(n-rank),'bright':P/rank}
 for name,C in ref.items():
  saved=a[key+'_Gamma_'+name];assert np.max(abs(C-saved))<1e-12;assert abs(np.trace(saved)-1)<1e-12;assert np.linalg.eigvalsh(saved)[0]>=-1e-12
  drag=Y.T@saved@Y;assert np.max(abs(drag-a[key+'_drag_'+name]))<1e-12
  assert abs(np.trace(drag)-row['trace_'+name])<1e-12
 assert np.linalg.norm(ref['dark']@Y)/np.linalg.norm(Y)<=1e-12
 assert row['all_pass'] and all(row['checks'].values())
 checked.append(key)
assert len(checked)==36 and len(set(checked))==36
out={'status':'CONSTRUCTOR_VERIFICATION_PASS','checked_configurations':36,'input_hashes':len(r['input_sha256']),'method':'QR span versus SVD construction; saved damping/control traces, PSD, solve and hashes','scope':'Same-constructor linear algebra check, not independent review or material damping test','native_rule':'HOLD_SOURCE_GATE','physical_promotion':0};(p/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
