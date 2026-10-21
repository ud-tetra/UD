"""Independent numerical reconstruction; never execute downloaded source code.
Usage: python3 reconstruct.py /path/to/riechert_waveform.gz
"""
import csv,gzip,hashlib,json,sys
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
contract=json.loads((P/'CONTRACT.json').read_text())
def analytic(v):
 n=len(v);h=np.zeros(n);h[0]=1
 if n%2==0:h[n//2]=1;h[1:n//2]=2
 else:h[1:(n+1)//2]=2
 return np.fft.ifft(np.fft.fft(v)*h)
def reconstruct(v,fs,fc,bw):
 v=v-v.mean();z=analytic(v);f=np.fft.fftfreq(len(v),1/fs)
 zf=np.fft.ifft(np.fft.fft(z)*((f>0)&(np.abs(f-fc)<=bw)))
 t=np.arange(len(v))/fs;u=zf*np.exp(-2j*np.pi*fc*t)
 delta=float(np.max(np.abs(z-zf)))
 return v,z,zf,u,delta
# Exact-bin synthetic controls: phase retained; modulation recovered; sign lost under squaring.
n=4096;fs=4096.;t=np.arange(n)/fs;phase=.73
v=(1+.2*np.cos(2*np.pi*7*t))*np.cos(2*np.pi*400*t+phase)
a,z,zf,u,delta=reconstruct(v,fs,400,20)
controls={'signed_roundtrip_max':float(np.max(np.abs(z.real-a))),
 'envelope_complex_error':float(np.max(np.abs(u-(1+.2*np.cos(2*np.pi*7*t))*np.exp(1j*phase)))),
 'opposite_sign_square_error':float(np.max(np.abs(v*v-(-v)**2)))}
_,_,_,_,zero_delta=reconstruct(np.zeros(n),fs,400,20)
controls['zero_phase_points_accepted']=int(np.sum(np.abs(analytic(np.zeros(n)))>10*zero_delta))
v2=np.cos(2*np.pi*400*t)+.3*np.cos(2*np.pi*800*t)
a2,z2,zf2,u2,d2=reconstruct(v2,fs,400,20)
controls['excluded_tone_relative_rms']=float(np.linalg.norm(a2-zf2.real)/np.linalg.norm(a2))
assert controls['signed_roundtrip_max']<1e-12 and controls['envelope_complex_error']<1e-11
assert controls['opposite_sign_square_error']==0 and controls['zero_phase_points_accepted']==0
assert controls['excluded_tone_relative_rms']>.05
path=Path(sys.argv[1]);assert hashlib.sha256(path.read_bytes()).hexdigest()==contract['source_sha256']
with gzip.open(path,'rt') as f:d=np.loadtxt(f)
assert list(d.shape)==contract['source_shape'] and np.isfinite(d).all()
assert np.all(d[:,0]==contract['sample_rate_hz'])
rows=[];carriers={};bounds_ok=True;roundtrip=0.;bound_violation=0.
for ch in contract['channels']:
 channel=d[d[:,5]==ch];assert len(channel)==100
 train=channel[0,206:];f=np.fft.rfftfreq(len(train),1/channel[0,0]);p=np.abs(np.fft.rfft((train-train.mean())*np.hanning(len(train))))**2
 mask=(f>=10000)&(f<=200000);fc=float(f[np.where(mask)[0][np.argmax(p[mask])]]);carriers[str(ch)]=fc
 for ri,row in enumerate(channel[1:],1):
  a,z,zf,u,delta=reconstruct(row[206:],row[0],fc,contract['carrier_half_bandwidth_hz'])
  g=contract['interior_guard_samples'];inter=slice(g,-g);rms=float(np.linalg.norm(a-zf.real)/np.linalg.norm(a))
  accept=np.abs(u[inter])>10*delta;coverage=float(np.mean(accept));phasebound=float(np.arcsin(.1))
  # Reverse triangle inequality and squared-envelope bound, reference = full finite-DFT analytic signal.
  amp_error=np.abs(np.abs(z)-np.abs(zf));energy_error=np.abs(np.abs(z)**2-np.abs(zf)**2)
  tol=1e-11*max(1.,float(np.max(np.abs(z)))**2)
  assert np.max(amp_error)<=delta+tol
  assert np.all(energy_error<=delta*(2*np.abs(zf)+delta)+tol)
  if np.any(accept):
   angle=np.abs(np.angle(z[inter][accept]*np.conj(zf[inter][accept])))
   assert np.max(angle)<=phasebound+1e-10
  roundtrip=max(roundtrip,float(np.max(np.abs(z.real-a))))
  rows.append({'channel':ch,'record':ri,'drive_frequency_metadata':float(row[1]),'carrier_hz':fc,'signed_rms_residual':rms,'max_complex_residual_V':delta,'interior_phase_fraction':coverage,'diagnostic_gate':bool(rms<=.05 and coverage>=.95)})
with (P/'RECORDS.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary={ 'status':'NUMERICAL / EMPIRICAL DESCRIPTIVE; ACTION ANCHOR HOLD', 'physical_promotion':0,
 'contract_sha256':hashlib.sha256((P/'CONTRACT.json').read_bytes()).hexdigest(),
 'records_evaluated':len(rows),'diagnostic_passes':sum(r['diagnostic_gate'] for r in rows),
 'roundtrip_max_abs_V':roundtrip,'conditional_bounds_checked_records':len(rows),
 'phase_bound_at_accepted_points_rad':float(np.arcsin(.1)), 'synthetic_controls':controls,'carriers_hz':carriers,
 'channel_summary':[]}
for ch in contract['channels']:
 rr=[r for r in rows if r['channel']==ch];res=[r['signed_rms_residual'] for r in rr];cov=[r['interior_phase_fraction'] for r in rr]
 summary['channel_summary'].append({'channel':ch,'records':len(rr),'diagnostic_passes':sum(r['diagnostic_gate'] for r in rr),'rms_residual_min_median_max':[float(x) for x in (min(res),np.median(res),max(res))],'phase_fraction_min_median_max':[float(x) for x in (min(cov),np.median(cov),max(cov))]})
(P/'RESULTS.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
