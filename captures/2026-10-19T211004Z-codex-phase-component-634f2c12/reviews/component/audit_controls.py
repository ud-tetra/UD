"""Small same-team synthetic audit; never calls raw run, opens waveform or fetches data."""
import ast
import cmath
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys
sys.dont_write_bytecode=True
import numpy as np

HERE=Path(__file__).resolve().parent

def require(condition, message):
    if not condition:raise RuntimeError(message)

def digest(path):
    b=path.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}

def main():
    binding=json.loads((HERE/'AUDIT_INPUTS.json').read_text())
    src=Path(binding['source_dir'])
    require(digest(src/binding['source_freeze_path'])==binding['source_freeze'],'source freeze changed')
    freeze=json.loads((src/binding['source_freeze_path']).read_text())
    for row in freeze['files']:
        require(digest(src/row['path'])=={'sha256':row['sha256'],'bytes':row['bytes']},'source member changed:'+row['path'])
    own=json.loads((HERE/'AUDIT_FREEZE.json').read_text())
    for row in own['files']:
        require(digest(HERE/row['path'])=={'sha256':row['sha256'],'bytes':row['bytes']},'review member changed:'+row['path'])
    spec=importlib.util.spec_from_file_location('reviewed_component_checker',src/binding['checker_path'])
    r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
    rows=[[str(r.FS),str(21000+200*i),'0','0','0',str(c)] for i in range(100) for c in range(1,11)]
    out=[]
    def record(name, fn, scope='synthetic implementation check'):
        try:detail=fn();out.append({'id':name,'pass':True,'scope':scope,'detail':detail})
        except Exception as e:out.append({'id':name,'pass':False,'scope':scope,'error':type(e).__name__+':'+str(e)})
    def refusal(fn,reason):
        try:fn()
        except r.Refusal as e:
            require(str(e)==reason,'wrong refusal reason:'+str(e));return reason
        raise RuntimeError('invalid fixture accepted')
    def source_order():
        refusal(lambda:r.identity(r.RAW_BYTES,'0'*64),'SOURCE_IDENTITY_MISMATCH')
        node=next(n for n in ast.parse((src/binding['checker_path']).read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='run')
        calls=[n for n in ast.walk(node) if isinstance(n,ast.Call)]
        identity_line=min(n.lineno for n in calls if isinstance(n.func,ast.Name) and n.func.id=='identity')
        gzip_line=min(n.lineno for n in calls if isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='gzip' and n.func.attr=='open')
        require(identity_line<gzip_line,'gzip before identity')
        return {'wrong_identity':'REFUSED','static_identity_line':identity_line,'static_gzip_line':gzip_line,'raw_entrypoint_invocations':0}
    record('wrong-source-refused-before-gzip',source_order,'scalar identity rejection plus static ordering; raw entrypoint not invoked')
    keys=r.groups(rows)
    def valid_groups():
        require(r.groups(list(reversed(rows)))==keys,'order dependent')
        counts={s:sum(r.split(i)==s for i in range(100)) for s in ('train','validation','test')}
        require(counts=={'train':60,'validation':20,'test':20},'wrong split')
        require(len(keys)==100 and len({k[1] for k in keys})==100,'wrong groups')
        return counts
    record('valid100groups-partition60-20-20',valid_groups)
    record('row-count-refusal',lambda:refusal(lambda:r.groups(rows[:-1]),'ROW_COUNT'))
    dup=[a[:] for a in rows];dup[1]=dup[0][:]
    record('duplicate-group-channel-refusal',lambda:refusal(lambda:r.groups(dup),'DUPLICATE_CHANNEL_GROUP'))
    def bad_meta(col,value,reason):
        a=rows[0][:];a[col]=value;return refusal(lambda:r.metadata(a),reason)
    record('metadata-nonfinite-refusal',lambda:bad_meta(1,'NaN','METADATA_NONFINITE'))
    record('nonzero-drive-metadata-refusal',lambda:bad_meta(2,'0.1','DRIVE_METADATA_MISMATCH'))
    record('channel-schema-refusal',lambda:bad_meta(5,'1.5','CHANNEL_SCHEMA'))
    record('rate-mismatch-refusal',lambda:bad_meta(0,'1953124','RATE_METADATA_MISMATCH'))
    def constant():
        z=r.features(np.full(32,0.1),start=0,fs=32)
        require(z['DC']==0.1 and z['AC_RMS']==0,'constant mean/rms')
        require(all(z[k] is None for k in ('rect_dominant_Hz','rect_centroid_Hz','hann_dominant_Hz','hann_centroid_Hz')),'constant false frequency')
        return {'DC':z['DC'],'AC_RMS':z['AC_RMS'],'spectral_labels':None}
    record('constant-decimal-undefined-spectrum',constant)
    def exact_four():
        a=r.features([3,5,3,1],start=0,fs=4)
        b=r.features([1,-1,1,-1],start=0,fs=4)
        require(a['DC']==3 and abs(a['AC_RMS']-math.sqrt(2))<1e-14,'four point rms/DC')
        require(a['rect_dominant_Hz']==1 and abs(a['rect_positive_power']-2)<1e-14,'four point interior')
        require(b['rect_dominant_Hz']==2 and abs(b['rect_positive_power']-1)<1e-14,'nyquist doubled')
        return {'interior_power':a['rect_positive_power'],'nyquist_power':b['rect_positive_power']}
    record('analytic-four-point-DC-RMS-Nyquist',exact_four)
    def direct_dft():
        a=[3.,1.,-1.,-3.,-3.,-1.,1.,3.];n=len(a);fs=24.;rowsout=[]
        for kind in ('rect','hann'):
            w=[1.]*n if kind=='rect' else [(1-math.cos(2*math.pi*j/(n-1)))/2 for j in range(n)]
            u=[sum(w[t]*a[t]*cmath.exp(-2j*math.pi*k*t/n) for t in range(n)) for k in range(n//2+1)]
            p=[(1 if k in (0,n//2) else 2)*abs(z)**2/(n*sum(q*q for q in w)) for k,z in enumerate(u)]
            total=sum(p[1:]);centroid=sum((k*fs/n)*p[k] for k in range(1,len(p)))/total
            z=r.spectral(np.array(a),fs,kind)
            require(abs(z['positive_power']-total)<1e-12,'power disagrees direct DFT')
            require(abs(z['centroid_Hz']-centroid)<1e-12,'centroid disagrees direct DFT')
            require(z['dominant_Hz']==max(range(1,len(p)),key=lambda k:p[k])*fs/n,'dominant differs')
            rowsout.append({'taper':kind,'direct_positive_power':total,'numpy_positive_power':z['positive_power'],'direct_centroid_label_Hz':centroid})
        return rowsout
    record('independent-small-DFT-rectangular-and-Hann',direct_dft,'8-point cmath direct DFT versus local NumPy checker, approximate formula consistency only')
    def crop_dc():
        z=r.features([99.,99.,99.,99.,3.,5.,3.,1.],start=4,fs=4)
        require(z['DC']==3 and abs(z['AC_RMS']-math.sqrt(2))<1e-14,'crop/mean order')
        return {'retained_samples':4,'DC':z['DC']}
    record('crop-premean-DC',crop_dc)
    record('nonfinite-waveform-refusal',lambda:refusal(lambda:r.features([0.,float('nan'),1.],start=0,fs=3),'TRACE_SCHEMA_OR_NONFINITE'))
    observed={(k,ch):{f:float(i+ch) for f in r.FEATURES} for i,k in enumerate(keys) for ch in range(1,11)}
    def heldout():
        shifted={key:dict(z) for key,z in observed.items()}
        for i,k in enumerate(keys):
            if r.split(i)!='train':
                for ch in range(1,11):
                    for f in r.FEATURES:shifted[(k,ch)][f]+=1000.
        scores=r.compare(keys,shifted)
        require(len(scores)==80,'missing comparison')
        # Training indices are 0,1,2,5,6,7,...,95,96,97. Median is (47+50)/2.
        for z in scores:
            ch=z['channel']
            for e in z['paired_errors']:
                i=e['group_index'];actual=1000.+i+ch
                require(abs(actual-e['median_abs']-(48.5+ch))<1e-12,'heldout changed median fit')
                require(abs(actual-e['linear_abs']-(min(i,97)+ch))<1e-12,'heldout changed interpolator or endpoint')
        return {'heldout_values_shifted_by':1000,'training_unchanged':True,'comparisons':80,'reconstructed_predictions_match_frozen_training_only_rules':True}
    record('fixed-training-baseline-predictions-and-no-heldout-refit',heldout)
    def missing():
        obs={key:dict(z) for key,z in observed.items()};obs[(keys[99],1)]['DC']=None
        got=[z for z in r.compare(keys,obs) if z['channel']==1 and z['feature']=='DC']
        require(len(got)==1 and got[0]['status']=='HOLD_UNDEFINED_FEATURE' and got[0]['dropped_records']==0,'missing silently discarded')
        return got[0]
    record('missing-feature-HOLD-no-deletion',missing)
    plan=json.loads((HERE/'REVIEW_PLAN.json').read_text())
    require({x['id'] for x in out}==set(plan['controls_predeclared']),'plan coverage mismatch')
    result={'artifact_type':'SAME_TEAM_COMPONENT_SYNTHETIC_REVIEW_RESULTS','source_freeze':binding['source_freeze'],'review_freeze':digest(HERE/'AUDIT_FREEZE.json'),'results':out,'controls':len(out),'all_pass':all(x['pass'] for x in out),'runtime':{'python':platform.python_version(),'numpy':np.__version__},'scope':'Separate same-team source/static review and tiny synthetic checks. No waveform/no calibrated numeric interval/no physical or external-review certificate.','raw_record_entrypoint_invocations':0,'experimental_records_evaluated':0,'new_raw_downloads':0,'new_fits':0,'physical_promotion':0,'external_review':'PENDING'}
    print(json.dumps(result,indent=2,allow_nan=False))
    if not result['all_pass']:raise SystemExit(1)
if __name__=='__main__':main()
