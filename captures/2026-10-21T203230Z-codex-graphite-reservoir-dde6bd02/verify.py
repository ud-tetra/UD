from pathlib import Path
import numpy as np,json,hashlib,re
from numpy.polynomial.legendre import leggauss
p=Path(__file__).resolve().parent;f=json.loads((p/'FREEZE.json').read_text());reg=json.loads((p/'SOURCE_REGISTER.json').read_text());r=json.loads((p/'RESULTS.json').read_text());src=p.parent/f['input'];assert hashlib.sha256(src.read_bytes()).hexdigest()==f['input_sha256'];d=np.load(src)
for row in reg['sources']:
 path=p.parent/row['path'];assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256']
inputs=sorted((p/'sources').glob('input-*.txt'));assert len(inputs)==4
for path in inputs:
 commands=[s.split('#')[0].strip() for s in path.read_text().splitlines()];assert any(s.startswith('minimize ') for s in commands);assert not any(re.match(r'run\s',s) for s in commands);assert not any(re.search(r'\b(langevin|nvt|npt|temp/rescale|viscous)\b',s) for s in commands)
ledger=json.loads((p/'sources/prior-1-CURRENT_LEDGER_v0.85.json').read_text());byid={x['id']:x for x in ledger['rows']};assert 'not physical damping rate' in byid['Q163']['status'];assert 'physical clock' in byid['Q162']['next_gate'];assert 'RETIRED' in byid['G05']['exact_form']
nodes,weights=leggauss(128);maximum=0.;max_offdiag=0.
for row in r['rows']:
 key=row['configuration'];A=d[key+'_A'];a=d[key+'_a'];k=float(d[key+'_k']);om=np.sqrt(k);gamma=row['gamma_ratio']*om;nu=row['frequency_ratio']*om;X=np.cos(np.arange(1,len(a)+1));X/=np.linalg.norm(X);c=a@X;T=2*np.pi/nu;t=(nodes+1)*T/2;phase=np.exp(1j*nu*t);zph=-c/(k-nu*nu+1j*gamma*nu);x=X[:,None]*phase.real;v=X[:,None]*(1j*nu*phase).real;z=(zph*phase).real;vz=(1j*nu*zph*phase).real;force=(A-nu*nu*np.eye(len(a)))@x+a[:,None]*z
 W=T/2*(weights@np.sum(force*v,axis=0));Q=T/2*(weights@(gamma*vz*vz));expected=row['mean_power_model_units']*T;err=max(abs(W-expected),abs(Q-expected),abs(W-row['drive_work']),abs(Q-row['export']));maximum=max(maximum,float(err))
 G=np.outer(a,a)*gamma/((k-nu*nu)**2+gamma*gamma*nu*nu);imD=(-np.outer(a,a)/(k-nu*nu+1j*gamma*nu)).imag/nu;max_offdiag=max(max_offdiag,float(np.linalg.norm(G-imD)));assert np.linalg.eigvalsh(G)[0]>-1e-12
assert maximum<1e-9 and max_offdiag<1e-10 and r['status']=='PASS' and len(r['rows'])==432
v={'status':'PASS','constructor_only':True,'nonconstructor_review':'PENDING','source_hashes_matched':len(reg['sources']),'input_hash_match':True,'static_inputs_without_dynamic_loss':4,'current_ledger_gates_checked':['G05','Q162','Q163'],'analytic_quadrature_controls':432,'max_analytic_integral_difference':maximum,'max_transfer_identity_error':max_offdiag,'physical_promotion':0}
(p/'VERIFICATION.json').write_text(json.dumps(v,indent=2)+'\n');summary={k:v for k,v in r.items() if k!='rows'};(p/'RESULTS_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(v,indent=2))
