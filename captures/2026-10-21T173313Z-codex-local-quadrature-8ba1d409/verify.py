from pathlib import Path
import csv,hashlib,json
import numpy as np
P=Path(__file__).resolve().parent;c=json.loads((P/'CONTRACT.json').read_text());fs=c['sample_rate_hz'];n=c['record_samples'];m=c['half_window'];k=np.arange(-m,m+1);s=k/fs;t=np.arange(n)/fs;fc=257*fs/n;omega=2*np.pi*fc
D=np.column_stack([np.cos(omega*s),-np.sin(omega*s),np.ones(len(k))]);w=np.hanning(len(k));G=D.T@(w[:,None]*D);dual=np.linalg.solve(G,D.T*w);h=dual[0]+1j*dual[1]
def estimate(v):return np.convolve(v,h[::-1],mode='valid')
sl=slice(m,-m);moment=h@D;moment_error=float(np.max(np.abs(moment-np.array([1,1j,0]))));assert moment_error<1e-12
l1=float(np.abs(h).sum());moment1=float(np.sum(np.abs(h)*np.abs(s)))
fc_off=fc+.37*fs/n;phase=.73

def z(a,f=fc,p=0):return a*np.exp(1j*(2*np.pi*f*t+phase+p))
base=z(np.ones(n));off=z(np.ones(n),fc_off)
cases={'exact_bin':(base,base),'off_bin':(off,off),'smooth_AM_PM':(z(1+.2*np.cos(2*np.pi*600*t),fc_off,.15*np.sin(2*np.pi*200*t)),None),'smooth_turnon':(z(.1+.45*(1+np.tanh((t-.001)/.0002)),fc_off),None),'narrow_pulse':(z(.05+np.exp(-((t-.004)/.00012)**2),fc_off),None),'omitted_sideband':(off+.3*z(np.ones(n),fc_off+12000),off)}
rows=[]
for name,(truth,fundamental) in cases.items():
 q=estimate(truth.real);ref=truth[sl];eligible=np.abs(ref)>=.2;r=float(np.linalg.norm(q-ref)/np.linalg.norm(ref));p=float(np.max(np.abs(np.angle(q[eligible]*np.conj(ref[eligible])))))
 rows.append({'case':name,'complex_relative_rms':r,'max_phase_rad':p,'max_amplitude_error_V':float(np.max(np.abs(np.abs(q)-np.abs(ref)))),'eligible_phase_points':int(eligible.sum()),'synthetic_gate':bool(r<=.01 and p<=.02),'fundamental_relative_rms':None if fundamental is None else float(np.linalg.norm(q-fundamental[sl])/np.linalg.norm(fundamental[sl]))})
# Exact transfer identity for any constant-amplitude tone, including carrier mismatch and image leakage.
transfer=[];transfer_error=0.
for df in c['transfer_offsets_hz']:
 A=.5*np.sum(h*np.exp(2j*np.pi*(fc+df)*s));B=.5*np.sum(h*np.exp(-2j*np.pi*(fc+df)*s));truth=z(np.ones(n),fc+df);pred=A*truth[sl]+B*np.conj(truth[sl]);err=float(np.max(np.abs(estimate(truth.real)-pred)));assert err<1e-11;transfer_error=max(transfer_error,err)
 transfer.append({'offset_hz':df,'A_real':float(A.real),'A_imag':float(A.imag),'image_abs_B':float(abs(B)),'relative_error_bound_abs_Aminus1_plus_abs_B':float(abs(A-1)+abs(B))})
# Local source-regularity bound with exact analytic Lipschitz upper bounds per generator.
L={'exact_bin':0.,'off_bin':2*np.pi*(fc_off-fc),'smooth_AM_PM':.2*2*np.pi*600+1.2*(2*np.pi*(fc_off-fc)+.15*2*np.pi*200),'smooth_turnon':.45/.0002+2*np.pi*(fc_off-fc),'narrow_pulse':np.sqrt(2/np.e)/.00012+1.05*2*np.pi*(fc_off-fc),'omitted_sideband':2*np.pi*(fc_off-fc)+.3*2*np.pi*(fc_off-fc+12000)}
bounds=[]
for name,(truth,_) in cases.items():
 actual=float(np.max(np.abs(estimate(truth.real)-truth[sl])));bound=float(L[name]*moment1);assert actual<=bound+1e-11
 bounds.append({'case':name,'envelope_L_V_per_s':float(L[name]),'conditional_complex_error_bound_V':bound,'observed_max_complex_error_V':actual})
noise=.005*np.sin(2*np.pi*250000*t);noisy=estimate(base.real+noise+2.7);noise_error=float(np.max(np.abs(noisy-base[sl])));assert noise_error<=.005*l1+1e-11
phase_errors=[]
for ph in [0,.73,1.9,3.14]:
 truth=np.exp(1j*(omega*t+ph));phase_errors.append(float(np.max(np.abs(estimate(truth.real+2.7)-truth[sl]))))
assert max(phase_errors)<1e-11
assert next(x for x in rows if x['case']=='omitted_sideband')['complex_relative_rms']>.1
summary={'status':'DERIVED CONDITIONAL / NUMERICAL SYNTHETIC','physical_promotion':0,'contract_sha256':hashlib.sha256((P/'CONTRACT.json').read_bytes()).hexdigest(),'valid_outputs':len(estimate(base.real)),'half_window_samples':m,'availability_delay_seconds':m/fs,'gram_eigenvalues':np.linalg.eigvalsh(G).tolist(),'gram_condition':float(np.linalg.cond(G)),'moment_error':moment_error,'noise_l1_gain':l1,'envelope_moment_seconds':moment1,'synthetic_passes':sum(r['synthetic_gate'] for r in rows),'rows':rows,'transfer':transfer,'transfer_identity_max_error':transfer_error,'conditional_bounds':bounds,'controls':{'constant_baseline_and_four_phases_max_error_V':max(phase_errors),'bounded_noise_max_error_V':noise_error,'bounded_noise_error_limit_V':.005*l1,'wrong_carrier_1000Hz_error_bound':next(x for x in transfer if x['offset_hz']==1000)['relative_error_bound_abs_Aminus1_plus_abs_B']},'empirical_status':'NOT RUN; prior0/891 preserved; no calibrated source regularity or physical phase bound.'}
(P/'RESULTS.json').write_text(json.dumps(summary,indent=2)+'\n')
with (P/'METRICS.csv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
with (P/'KERNEL.csv').open('w') as f:
 writer=csv.writer(f);writer.writerow(['sample_offset','real_h','imag_h']);writer.writerows(zip(k,h.real,h.imag))
print(json.dumps(summary,indent=2))
