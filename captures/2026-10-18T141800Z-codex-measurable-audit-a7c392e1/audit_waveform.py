"""Read-only content audit of one published circuit acquisition; no imported code execution."""
import gzip, hashlib, json, sys
from pathlib import Path
import numpy as np

p=Path(sys.argv[1]); raw=p.read_bytes()
d=np.loadtxt(gzip.open(p,'rt'))
assert d.shape==(1000,16390)
assert np.isfinite(d).all()
assert np.unique(d[:,0]).tolist()==[1953125.0]
channels, counts=np.unique(d[:,5],return_counts=True)
assert channels.tolist()==list(range(1,11)) and (counts==100).all()
blocks=[]
for c in channels:
    z=d[d[:,5]==c]
    blocks.append(z)
assert all(np.array_equal(z[:,:5],blocks[0][:,:5]) for z in blocks)
assert np.all(d[:,2:5]==0)
sha=hashlib.sha256(raw).hexdigest()
md5=hashlib.md5(raw).hexdigest()
out={'status':'PASS_CONTENT_AUDIT_NOT_PHYSICAL_CERTIFICATE',
 'source_commit':'265b6671dde799d7c73f32247fa3ee93ae70e0f2',
 'path':p.name,'bytes':len(raw),'sha256':sha,'md5':md5,
 'rows':1000,'metadata_columns':6,'samples_per_trace':16384,
 'channels':channels.astype(int).tolist(),'records_per_channel':100,
 'sample_rate_hz':1953125.0,'sample_interval_s':1/1953125,
 'record_length_s':16384/1953125,'fft_bin_hz':1953125/16384,
 'trigger_sample_documented':200,'all_values_finite':True,
 'metadata_equal_across_channels':True,
 'frequency_metadata_range_hz':[float(d[:,1].min()),float(d[:,1].max())],
 'frequency_metadata_unique_count':int(np.unique(d[:,1]).size),
 'drive_amplitude_phase_delay_all_zero':True,
 'voltage_min_max':[float(d[:,6:].min()),float(d[:,6:].max())],
 'max_abs_below_notebook_15V_guard':bool(np.max(np.abs(d[:,6:]))<15),
 'channel10_empty_by_filename_only':True,
 'limits':['100 records are not automatically 100 repeated preparations at one setting',
 'Equal metadata does not certify inter-device timing skew',
 '15 V software guard is not an independently calibrated ADC clipping test',
 'No full calibration covariance, simultaneous coverage or UD state/energy/source reconstruction certified',
 'No waveform fit, Gauss-conservation significance test or GUT inference performed'],
 'physical_promotion':0}
print(json.dumps(out,indent=2))
