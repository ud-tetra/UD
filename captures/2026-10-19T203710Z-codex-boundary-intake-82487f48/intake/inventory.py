"""Repository DIRECT JSON inventory. No archive opening, scripts or raw fetches."""
import argparse,json,hashlib,subprocess
from pathlib import Path
from datetime import datetime,timezone
def inventory(repo):
    repo=Path(repo).resolve()
    paths=subprocess.run(['rg','--files',str(repo),'-g','*.json'],check=True,capture_output=True,text=True).stdout.splitlines()
    head=subprocess.run(['git','-C',str(repo),'rev-parse','HEAD'],check=True,capture_output=True,text=True).stdout.strip()
    rows=[];skips=[];parse_errors=[];examined=0
    def facts(value,path='$'):
        out=[]
        if isinstance(value,dict):
            if value.get('provenance_kind') in ['apparatus_submission','synthetic_fixture']:out.append({'json_path':path,'field':'provenance_kind','value':value['provenance_kind']})
            if value.get('version') in ['UD_TRUST_POLICY_v1','UD_ANALYTIC_ADMISSION_v1','ADC_RECORD_CONTRACT_v0.1']:out.append({'json_path':path,'field':'version','value':value['version'],'scope':value.get('scope'),'keys_count':len(value['keys']) if isinstance(value.get('keys'),dict) else None})
            if value.get('physical_verdict')=='HOLD_UNQUALIFIED':out.append({'json_path':path,'field':'physical_verdict','value':'HOLD_UNQUALIFIED'})
            if isinstance(value.get('status'),str) and ('CONTENT_AUDIT' in value['status'] or 'APPARATUS' in value['status'] or 'AUTHENTICATION' in value['status']):out.append({'json_path':path,'field':'status','value':value['status']})
            for k,x in value.items():out+=facts(x,path+'.'+str(k))
        elif isinstance(value,list):
            for i,x in enumerate(value):out+=facts(x,path+'['+str(i)+']')
        return out
    for name in sorted(paths):
        p=Path(name)
        if p.is_symlink() or p.stat().st_size>32*1024*1024:skips.append(str(p.relative_to(repo)));continue
        raw=p.read_bytes();examined+=1
        try:value=json.loads(raw)
        except (ValueError,RecursionError):parse_errors.append(str(p.relative_to(repo)));continue
        fs=facts(value)
        if fs:rows.append({'path':str(p.relative_to(repo)),'sha256':hashlib.sha256(raw).hexdigest(),'size_bytes':len(raw),'facts':fs,'classification':'Typed claims/metadata only; not independently qualified evidence'})
    return {'status':'DIRECT_JSON_ONLY_SCOPED_INVENTORY','observed_utc':datetime.now(timezone.utc).isoformat(),'repository_HEAD':head,'direct_JSON_paths_discovered':len(paths),'direct_JSON_files_examined':examined,'skipped_paths':skips,'parse_error_paths':parse_errors,'relevant_rows':rows,'archive_contents_examined':False,'raw_measurements_reanalyzed':0,'new_fits':0,'actual_current_real_record_intakes':0,'scope':'Repository working-tree DIRECT JSON metadata only. Nested archives/raw contents and Library files are not examined. Metadata includes historical experimental audit receipts and synthetic controls/templates; this inventory does not prove absence of past experiments or of unexamined archive evidence. No independently caller-pinned current REAL bundle was supplied to this task.','physical_promotion':0,'external_review':'PENDING'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);x=ap.parse_args()
    with Path(x.out).open('x') as f:json.dump(inventory(x.repo),f,indent=2);f.write('\n')
