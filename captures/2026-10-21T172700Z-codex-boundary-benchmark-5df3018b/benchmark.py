"""Constructor benchmark of fixed boundary treatments; generates no experimental claim."""
from pathlib import Path
import csv,hashlib,json
import numpy as np
P=Path(__file__).resolve().parent;c=json.loads((P/'CONTRACT.json').read_text())
n=c['samples'];fs=c['sample_rate_hz'];g=c['guard_samples'];t=np.arange(n)/fs
fc=c['carrier_bin']*fs/n;f_off=fc+c['noninteger_offset_bins']*fs/n;phi=c['phase_rad'];bw=c['half_bandwidth_hz'];sl=slice(g,-g)
def phasor(a,f=fc,extra=0):return a*np.exp(1j*(2*np.pi*f*t+phi+extra))
base=phasor(np.ones(n));off=phasor(np.ones(n),f_off)
cases={'exact_bin':(base,base), 'off_bin':(off,off),
 'smooth_AM_PM':(phasor(1+.2*np.cos(2*np.pi*600*t),f_off,.15*np.sin(2*np.pi*200*t)),None),
 'smooth_turnon':(phasor(.1+.45*(1+np.tanh((t-.001)/.0002)),f_off),None),
 'narrow_pulse':(phasor(.05+np.exp(-((t-.004)/.00012)**2),f_off),None),
 'omitted_sideband':(off+.3*phasor(np.ones(n),f_off+12000),off)}
def filt(v,method):
 v=v-v.mean();weights=np.ones(n)
 if method=='zero_pad':x=np.pad(v,(n,n));crop=slice(n,2*n)
 elif method=='reflect_pad':x=np.pad(v,(n,n),mode='reflect');crop=slice(n,2*n)
 elif method=='hann_divide':weights=np.hanning(n);x=v*weights;crop=slice(0,n)
 else:x=v;crop=slice(0,n)
 f=np.fft.fftfreq(len(x),1/fs);mult=2*((f>0)&(np.abs(f-fc)<=bw));z=np.fft.ifft(np.fft.fft(x)*mult)[crop]
 if method=='hann_divide':
  # No extrapolation or division at zero endpoint weights; metrics use the fixed interior.
  out=np.full(n,np.nan+1j*np.nan);np.divide(z,weights,out=out,where=weights>0);z=out
 return z
rows=[]
for name,(truth,fundamental) in cases.items():
 for method in c['methods']:
  z=filt(truth.real,method);q=z[sl];ref=truth[sl];eligible=np.abs(ref)>=.2
  rel=float(np.linalg.norm(q-ref)/np.linalg.norm(ref));phase=float(np.max(np.abs(np.angle(q[eligible]*np.conj(ref[eligible])))))
  amp=float(np.max(np.abs(np.abs(q)-np.abs(ref))))
  row={'case':name,'method':method,'complex_relative_rms':rel,'max_amplitude_error_V':amp,'max_phase_error_rad':phase,'phase_eligible_points':int(eligible.sum()),'synthetic_gate':bool(rel<=.01 and phase<=.02),'fundamental_relative_rms':None}
  if fundamental is not None:row['fundamental_relative_rms']=float(np.linalg.norm(q-fundamental[sl])/np.linalg.norm(fundamental[sl]))
  rows.append(row)
# Finite-band boundary influence. One outside impulse, explicit kernel identity and norm bounds.
L=3*n;f=np.fft.fftfreq(L,1/fs);mask=(f>0)&(np.abs(f-fc)<=bw);kernel=np.fft.ifft(2*mask.astype(float));outside=np.ones(L);outside[n:2*n]=0
row_l1=np.fft.ifft(np.fft.fft(np.abs(kernel))*np.fft.fft(outside)).real[n+g:2*n-g]
impulse=np.zeros(L);impulse[n-1]=1;effect=np.fft.ifft(np.fft.fft(impulse)*(2*mask))
expected=np.roll(kernel,n-1);assert np.max(np.abs(effect-expected))<1e-14
norm_bound=2*np.sqrt(mask.sum()/L);assert np.max(np.abs(effect))<=norm_bound+1e-14
influence=float(np.max(np.abs(effect[n+g:2*n-g])));assert influence>1e-8
assert next(r for r in rows if r['case']=='exact_bin' and r['method']=='periodic')['complex_relative_rms']<1e-12
# A carrier-band estimator must not call removal of injected out-of-band content full recovery.
assert all(r['complex_relative_rms']>.1 for r in rows if r['case']=='omitted_sideband')
summary={'status':'NUMERICAL_SYNTHETIC_BOUNDARY_COMPARISON','physical_promotion':0,'contract_sha256':hashlib.sha256((P/'CONTRACT.json').read_bytes()).hexdigest(),'carrier_hz':fc,'off_bin_carrier_hz':f_off,'rows':rows,'method_pass_counts':{m:sum(r['synthetic_gate'] for r in rows if r['method']==m) for m in c['methods']},'boundary_kernel':{'L':L,'retained_positive_bins':int(mask.sum()),'row_l2':float(norm_bound),'outside_row_l1_min_max':[float(row_l1.min()),float(row_l1.max())],'single_outside_unit_impulse_max_interior_effect':influence,'kernel_identity_error':float(np.max(np.abs(effect-expected))),'scope':'A finite guard does not erase boundary influence; missing continuation-amplitude bound cannot be inferred from agreement of padding methods.'},'empirical_reanalysis':'NOT_RUN; v0.1 0/891 gate result preserved'}
(P/'RESULTS.json').write_text(json.dumps(summary,indent=2)+'\n')
with (P/'METRICS.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(json.dumps(summary,indent=2))
