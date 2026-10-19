"""Separate same-team streamed descriptive replay. No acquisition, fit, import of constructor code or tuning."""
import argparse,bisect,cmath,gzip,hashlib,json,math,platform,sys,time
from collections import Counter
from decimal import Decimal
from pathlib import Path
sys.dont_write_bytecode=True
import numpy as np
import scipy
from scipy.fft import rfft
HERE=Path(__file__).resolve().parent
RAW_SHA='7966700a6208e2bd2b5829a32b38cce7016f0c3460ace2708c85bac8577c282c'
RAW_BYTES=30941478
N=16184
FS=1953125
FEATURES=('DC','AC_RMS','rect_dominant_Hz','rect_centroid_Hz')
TOL={'voltage':1e-12,'power':1e-11,'frequency':1e-6,'direct_normalized_complex':1e-10}

def need(ok,msg):
    if not ok:raise ValueError(msg)

def fingerprint(p):
    h=hashlib.sha256();n=0
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b);n+=len(b)
    return {'bytes':n,'sha256':h.hexdigest()}

def lane(i):return 'train' if i%5<3 else 'validation' if i%5==3 else 'test'
def tolerance(feature):return TOL['frequency'] if 'Hz' in feature else TOL['power'] if 'power' in feature else TOL['voltage']

def summaries(v,direct=False):
    # Python compensated reductions independently of NumPy mean/RMS reductions.
    constant=all(x==v[0] for x in v)
    m=v[0] if constant else math.fsum(v)/N
    a=[0.]*N if constant else [x-m for x in v]
    rms=math.sqrt(math.fsum(x*x for x in a)/N)
    out={'DC':m,'AC_RMS':rms};direct_checks=[]
    for name in ('rect','hann'):
        w=[1.]*N if name=='rect' else [(1-math.cos(2*math.pi*j/(N-1)))/2 for j in range(N)]
        wa=[x*y for x,y in zip(w,a)];s2=math.fsum(x*x for x in w)
        u=rfft(wa,workers=1)
        # Scalar one-sided weighting, independent summation and bin selection.
        p=[(1. if k in (0,N//2) else 2.)*(float(z.real)**2+float(z.imag)**2)/(N*s2) for k,z in enumerate(u)]
        need(all(math.isfinite(x) for x in p),'nonfinite own spectrum')
        total=math.fsum(p[1:])
        k=None if total==0 else max(range(1,len(p)),key=lambda j:p[j])
        out[name+'_positive_power']=total
        out[name+'_dominant_Hz']=None if k is None else k*FS/N
        out[name+'_centroid_Hz']=None if k is None else math.fsum(j*FS/N*p[j] for j in range(1,len(p)))/total
        if direct and k is not None:
            bins=sorted({1,N//2,*[j for j in (k-1,k,k+1) if 1<=j<=N//2]})
            denom=math.sqrt(N*s2)
            for j in bins:
                re=math.fsum(wa[t]*math.cos(2*math.pi*j*t/N) for t in range(N))
                im=-math.fsum(wa[t]*math.sin(2*math.pi*j*t/N) for t in range(N))
                delta=abs(complex(re,im)-complex(u[j]))/denom
                need(delta<=TOL['direct_normalized_complex'],'direct selected DFT mismatch')
                direct_checks.append({'taper':name,'bin':j,'normalized_complex_delta':delta})
    for f in ('dominant_Hz','centroid_Hz'):
        out['sensitivity_hann_minus_rect_'+f]=None if out['rect_'+f] is None or out['hann_'+f] is None else out['hann_'+f]-out['rect_'+f]
    return out,direct_checks

def baseline(keys,values):
    training=[i for i in range(100) if lane(i)=='train'];xs=[float(keys[i][1]) for i in training];out=[]
    for ch in range(1,11):
        for f in FEATURES:
            ys=[values[(key,ch)][f] for key in keys]
            if any(y is None for y in ys):
                out.append({'channel':ch,'feature':f,'status':'HOLD_UNDEFINED_FEATURE','dropped_records':0});continue
            ty=[ys[i] for i in training];sorty=sorted(ty);med=(sorty[29]+sorty[30])/2
            for split in ('validation','test'):
                pairs=[]
                for i,key in enumerate(keys):
                    if lane(i)!=split:continue
                    x=float(key[1]);j=bisect.bisect_left(xs,x)
                    pred=ty[0] if j==0 else ty[-1] if j==len(xs) else ty[j-1]+(ty[j]-ty[j-1])*(x-xs[j-1])/(xs[j]-xs[j-1])
                    pairs.append({'group_index':i,'median_abs':abs(ys[i]-med),'linear_abs':abs(ys[i]-pred)})
                ec=[z['median_abs'] for z in pairs];el=[z['linear_abs'] for z in pairs]
                out.append({'channel':ch,'feature':f,'split':split,'groups':len(pairs),'status':'DESCRIPTIVE_ONLY','median_MAE':math.fsum(ec)/len(ec),'median_max_abs':max(ec),'linear_MAE':math.fsum(el)/len(el),'linear_max_abs':max(el),'linear_minus_median_MAE':math.fsum(el)/len(el)-math.fsum(ec)/len(ec),'paired_errors':pairs})
    return out

def run(raw,result,resultsha):
    start=time.monotonic();before=fingerprint(raw)
    need(before=={'bytes':RAW_BYTES,'sha256':RAW_SHA},'raw identity mismatch before decode')
    primary_before=fingerprint(result);need(primary_before['sha256']==resultsha,'caller result hash mismatch')
    rows={};groups={};direct_rows=[];count=0
    with gzip.open(raw,'rt',encoding='ascii') as f:
        for line in f:
            fields=line.partition('#')[0].split()
            if not fields:continue
            need(len(fields)==16390,'row width')
            z=tuple(Decimal(x) for x in fields[:6]);need(all(x.is_finite() for x in z),'metadata nonfinite')
            need(z[0]==FS and 21000<=z[1]<=41000 and all(x==0 for x in z[2:5]),'metadata value')
            need(z[5] in range(1,11),'channel value');ch=int(z[5]);key=z[:5]
            need((key,ch) not in rows,'duplicate group/channel')
            values=[float(x) for x in fields[6:]];need(all(math.isfinite(x) for x in values),'sample nonfinite')
            direct=z[1] in (Decimal(21000),Decimal(41000)) and ch in (1,2,10)
            val,checks=summaries(values[200:],direct)
            rows[(key,ch)]=val;groups.setdefault(key,set()).add(ch);count+=1
            need(count<=1000,'too many rows')
            if direct:direct_rows.append({'frequency_label':str(z[1]),'channel':ch,'checks':checks})
    need(count==1000 and len(groups)==100,'record/group count')
    need(all(ch==set(range(1,11)) for ch in groups.values()),'group channel completeness')
    keys=sorted(groups,key=lambda k:k[1]);need(len({k[1] for k in keys})==100,'frequency uniqueness')
    need(len(direct_rows)==6,'predeclared endpoint rows missing')
    need(fingerprint(raw)==before,'raw changed during read')
    # First exposure to newly generated primary results occurs only after own recomputation.
    primary=json.loads(Path(result).read_text())
    need(primary['status']=='DESCRIPTIVE_COMPONENT_OUTPUT_NOT_PHYSICAL_CERTIFICATE','primary status')
    need(primary['raw_sha256']==RAW_SHA and primary['raw_bytes']==RAW_BYTES and primary['groups']==100 and primary['crop_N']==N,'primary identity/shape')
    need(primary['split_counts']=={'train':60,'validation':20,'test':20},'primary split counts')
    need(len(primary['records'])==1000,'primary output count')
    maxima={};seen=set();feature_checks=0
    def compare_value(name,actual,expected,tol):
        nonlocal feature_checks
        feature_checks+=1
        if expected is None:need(actual is None,'expected undefined:'+name);return
        need(isinstance(actual,(int,float)) and math.isfinite(actual),'nonfinite primary:'+name)
        delta=abs(actual-expected);maxima[name]=max(maxima.get(name,0.),delta)
        need(delta<=tol,'comparison mismatch:'+name+':'+repr(delta))
    for rec in primary['records']:
        i=rec['group_index'];ch=rec['channel'];need(type(i)==int and 0<=i<100 and type(ch)==int and ch in range(1,11),'result index')
        need((i,ch) not in seen,'duplicate primary row');seen.add((i,ch));key=keys[i]
        need(tuple(Decimal(v) for v in rec['metadata'])==key and rec['split']==lane(i),'primary group metadata/split')
        for f,expected in rows[(key,ch)].items():
            compare_value('record.'+f,rec[f],expected,0. if 'dominant_Hz' in f else tolerance(f))
    ownmodels=baseline(keys,rows);actualmodels=primary['descriptive_comparisons']
    need(len(actualmodels)==len(ownmodels),'comparison report count')
    actualidx={ (r['channel'],r['feature'],r.get('split')):r for r in actualmodels }
    need(len(actualidx)==len(actualmodels),'duplicate model row')
    for expected in ownmodels:
        actual=actualidx[(expected['channel'],expected['feature'],expected.get('split'))]
        need(actual['status']==expected['status'],'model status')
        if expected['status'].startswith('HOLD'):
            need(actual['dropped_records']==0,'missing deletion');continue
        need(actual['groups']==20 and len(actual['paired_errors'])==20,'model group count')
        tol=4*tolerance(expected['feature'])
        for f in ('median_MAE','median_max_abs','linear_MAE','linear_max_abs','linear_minus_median_MAE'):
            compare_value('model.'+expected['feature']+'.'+f,actual[f],expected[f],tol)
        for a,e in zip(actual['paired_errors'],expected['paired_errors']):
            need(a['group_index']==e['group_index'],'paired error group')
            for f in ('median_abs','linear_abs'):compare_value('paired.'+expected['feature'],a[f],e[f],tol)
    need(primary['physical_promotion']==0 and primary['confidence_intervals'] is None and primary['phase_or_gauss_claim'] is False,'primary physical scope')
    need(primary['calibration'].startswith('HOLD') and primary['physical_model_comparison'].startswith('HOLD') and primary['native_apparatus'].startswith('HOLD'),'physical HOLD removed')
    need(fingerprint(result)==primary_before,'primary changed during review')
    return {'artifact_type':'SAME_TEAM_STREAMED_COMPONENT_EXECUTION_REVIEW','status':'PASS_DESCRIPTIVE_NUMERICAL_CONSISTENCY_PHYSICAL_HOLD','raw':before,'primary_result':primary_before,'rows':count,'groups':100,'records_per_channel':100,'split_counts':dict(Counter(lane(i) for i in range(100))),'crop_N':N,'own_feature_and_model_scalar_comparisons':feature_checks,'maximum_absolute_differences':maxima,'selected_direct_DFT_rows':direct_rows,'independence_scope':'No constructor imports; Python compensated mean/RMS and list/bisect models. SciPy FFT may share algorithm/backend ancestry with NumPy; direct selected cosine/sine sums strengthen limited coefficient checks, not interval proof. Same-team review is not external review.','numerical_tolerances':TOL,'numeric_tolerance_scope':'Frozen engineering consistency thresholds, not outward rounding enclosures or instrument uncertainty','runtime':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'elapsed_seconds':time.monotonic()-start,'calibration':'HOLD','physical_model_test':'HOLD','gauss_significance':'HOLD','native62_channel_admission':'HOLD','physical_promotion':0,'external_review':'PENDING','new_fits':0,'source_downloads_by_reviewer':0}

def main():
    p=argparse.ArgumentParser();p.add_argument('--raw',required=True,type=Path);p.add_argument('--result',required=True,type=Path);p.add_argument('--result-sha256',required=True);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    freeze=json.loads((HERE/'PRE_RESULT_FREEZE.json').read_text())
    for member in freeze['files']:
        need(fingerprint(HERE/member['path'])=={k:member[k] for k in ('bytes','sha256')},'review source changed:'+member['path'])
    need(not a.output.exists() and not a.output.is_symlink() and a.output.resolve() not in (a.raw.resolve(),a.result.resolve()),'output must be fresh')
    output=run(a.raw,a.result,a.result_sha256)
    output['pre_result_freeze']=fingerprint(HERE/'PRE_RESULT_FREEZE.json')
    with a.output.open('x') as f:json.dump(output,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps({'status':output['status'],'rows':output['rows'],'groups':output['groups'],'output':str(a.output),'physical_promotion':0,'external_review':'PENDING'}))
if __name__=='__main__':main()
