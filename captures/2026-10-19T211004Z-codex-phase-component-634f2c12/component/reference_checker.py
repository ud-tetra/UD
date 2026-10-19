"""Frozen descriptive reference. No acquisition commands, downloads, fits or calibration.
Actual source execution is deferred; this turn runs only tiny synthetic controls.
"""
import argparse
from decimal import Decimal, InvalidOperation
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np

RAW_SHA='7966700a6208e2bd2b5829a32b38cce7016f0c3460ace2708c85bac8577c282c'
RAW_BYTES=30941478
FS=1953125
NRAW=16384
START=200
FEATURES=('DC','AC_RMS','rect_dominant_Hz','rect_centroid_Hz')

class Refusal(ValueError):
    pass

def need(c, reason):
    if not c:
        raise Refusal(reason)

def fingerprint(path):
    h=hashlib.sha256(); count=0
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            count+=len(b);h.update(b)
    return count,h.hexdigest()

def identity(size,sha):
    need(size==RAW_BYTES and sha==RAW_SHA,'SOURCE_IDENTITY_MISMATCH')

def metadata(fields):
    need(len(fields)==6,'METADATA_WIDTH')
    try:
        z=tuple(Decimal(str(t)) for t in fields)
    except (InvalidOperation,ValueError):
        raise Refusal('METADATA_DECIMAL')
    need(all(t.is_finite() for t in z),'METADATA_NONFINITE')
    need(z[0]==FS,'RATE_METADATA_MISMATCH')
    need(21000<=z[1]<=41000,'FREQUENCY_LABEL_RANGE')
    need(all(t==0 for t in z[2:5]),'DRIVE_METADATA_MISMATCH')
    need(z[5]==int(z[5]) and 1<=z[5]<=10,'CHANNEL_SCHEMA')
    return z

def groups(rows):
    need(len(rows)==1000,'ROW_COUNT')
    d={}
    for r in rows:
        z=metadata(r);key=z[:5];ch=int(z[5])
        g=d.setdefault(key,{})
        need(ch not in g,'DUPLICATE_CHANNEL_GROUP')
        g[ch]=True
    need(len(d)==100,'GROUP_COUNT')
    need(all(set(g)==set(range(1,11)) for g in d.values()),'MISSING_CHANNEL_GROUP')
    keys=sorted(d,key=lambda k:k[1])
    need(len({k[1] for k in keys})==100,'DISTINCT_FREQUENCY_LABEL_COUNT')
    return keys

def split(index):
    return ('train' if index%5 in (0,1,2) else 'validation' if index%5==3 else 'test')

def spectral(ac,fs,kind):
    n=len(ac)
    need(n>=3 and np.isfinite(ac).all(),'SPECTRAL_INPUT')
    if kind=='rect':
        w=np.ones(n)
    elif kind=='hann':
        w=(1-np.cos(2*np.pi*np.arange(n)/(n-1)))/2
    else:
        raise Refusal('UNKNOWN_TAPER')
    u=np.fft.rfft(w*ac)
    d=np.full(len(u),2.0);d[0]=1
    if n%2==0:d[-1]=1
    power=d*np.abs(u)**2/(n*np.sum(w*w))
    need(np.isfinite(power).all(),'ARITHMETIC_NONFINITE')
    pos=power[1:];labels=np.arange(1,len(power))*fs/n
    total=float(np.sum(pos))
    if total==0:
        return {'dominant_Hz':None,'centroid_Hz':None,'positive_power':0.0,'zero_ac':True}
    centroid=float(np.sum(labels*pos)/total)
    need(np.isfinite(total) and np.isfinite(centroid),'ARITHMETIC_NONFINITE')
    return {'dominant_Hz':float(labels[int(np.argmax(pos))]),
            'centroid_Hz':centroid,
            'positive_power':total,'zero_ac':False}

def features(trace,start=START,fs=FS):
    a=np.asarray(trace,dtype=np.float64)
    need(a.ndim==1 and 0<=start<len(a) and np.isfinite(a).all(),'TRACE_SCHEMA_OR_NONFINITE')
    a=a[start:]
    constant=bool(np.all(a==a[0]))
    dc=float(a[0] if constant else np.mean(a));ac=np.zeros_like(a) if constant else a-dc
    rms=float(np.sqrt(np.mean(ac*ac)))
    need(np.isfinite(dc) and np.isfinite(rms),'ARITHMETIC_NONFINITE')
    r=spectral(ac,fs,'rect');h=spectral(ac,fs,'hann')
    return {'DC':dc,'AC_RMS':rms,'rect_dominant_Hz':r['dominant_Hz'],
            'rect_centroid_Hz':r['centroid_Hz'],'rect_positive_power':r['positive_power'],
            'hann_dominant_Hz':h['dominant_Hz'],'hann_centroid_Hz':h['centroid_Hz'],
            'hann_positive_power':h['positive_power'],
            'sensitivity_hann_minus_rect_dominant_Hz':None if r['dominant_Hz'] is None or h['dominant_Hz'] is None else h['dominant_Hz']-r['dominant_Hz'],
            'sensitivity_hann_minus_rect_centroid_Hz':None if r['centroid_Hz'] is None or h['centroid_Hz'] is None else h['centroid_Hz']-r['centroid_Hz']}

def compare(keys,observed):
    x=np.array([float(k[1]) for k in keys])
    need(len(x)==100 and np.isfinite(x).all() and np.all(np.diff(x)>0),'FLOAT_LABEL_ORDER_COLLAPSE')
    tr=[i for i in range(100) if split(i)=='train']
    out=[]
    for ch in range(1,11):
        for f in FEATURES:
            y=[observed[(k,ch)][f] for k in keys]
            if any(t is None or not np.isfinite(t) for t in y):
                out.append({'channel':ch,'feature':f,'status':'HOLD_UNDEFINED_FEATURE','dropped_records':0});continue
            y=np.array(y);med=float(np.median(y[tr]));linear=np.interp(x,x[tr],y[tr])
            for lane in ('validation','test'):
                ix=[i for i in range(100) if split(i)==lane]
                ec=np.abs(y[ix]-med);el=np.abs(y[ix]-linear[ix])
                out.append({'channel':ch,'feature':f,'split':lane,'groups':len(ix),
                    'status':'DESCRIPTIVE_ONLY','median_MAE':float(np.mean(ec)),
                    'median_max_abs':float(np.max(ec)),'linear_MAE':float(np.mean(el)),
                    'linear_max_abs':float(np.max(el)),
                    'linear_minus_median_MAE':float(np.mean(el)-np.mean(ec)),
                    'paired_errors':[{'group_index':i,'median_abs':float(ec[j]),'linear_abs':float(el[j])} for j,i in enumerate(ix)]})
    return out

def run(path):
    before=fingerprint(path);identity(*before)
    metas=[];observed={}
    with gzip.open(path,'rt',encoding='ascii') as f:
        for line in f:
            line=line.split('#',1)[0].strip()
            if not line:continue
            fields=line.split();need(len(fields)==6+NRAW,'ROW_WIDTH')
            z=metadata(fields[:6]);metas.append(z)
            need(len(metas)<=1000,'ROW_COUNT')
            key=(z[:5],int(z[5]));need(key not in observed,'DUPLICATE_CHANNEL_GROUP')
            try:a=np.array(fields[6:],dtype=np.float64)
            except ValueError:raise Refusal('SAMPLE_NUMBER_SCHEMA')
            observed[key]=features(a)
    keys=groups(metas)
    need(fingerprint(path)==before,'SOURCE_CHANGED_DURING_READ')
    return {'status':'DESCRIPTIVE_COMPONENT_OUTPUT_NOT_PHYSICAL_CERTIFICATE',
        'raw_sha256':before[1],'raw_bytes':before[0],'groups':100,
        'crop_N':NRAW-START,'crop_metadata_bin_Hz':FS/(NRAW-START),
        'split_counts':{'train':60,'validation':20,'test':20},
        'records':[{'group_index':i,'split':split(i),'metadata':[str(v) for v in k],
                    'channel':ch,**observed[(k,ch)]} for i,k in enumerate(keys) for ch in range(1,11)],
        'descriptive_comparisons':compare(keys,observed),
        'calibration':'HOLD_MISSING_INDEPENDENT_CALIBRATION_TIMING_COVARIANCE',
        'physical_model_comparison':'HOLD_MISSING_CALIBRATED_MODEL_AND_ACQUISITION_CONFIGURATION',
        'native_apparatus':'HOLD_INCOMPATIBLE_OBSERVER_AND_CALIBRATION','physical_promotion':0,
        'confidence_intervals':None,'phase_or_gauss_claim':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--raw',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    try:out=run(a.raw)
    except (Refusal,OSError,UnicodeError,ValueError,OverflowError) as e:
        out={'status':'HOLD_REFERENCE_INPUT_OR_ARITHMETIC','reason':str(e),'physical_promotion':0,'partial_results_admitted':False}
    a.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
