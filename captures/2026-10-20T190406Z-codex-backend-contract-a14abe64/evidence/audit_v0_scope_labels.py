"""Bounded content audit; no numerical estimator, archive code or hardware execution."""
from pathlib import Path
import json,hashlib,subprocess,collections,argparse,datetime
P=Path(__file__).resolve().parent
PIN='065f44b7a9b432efb94fc7cb4d274abb6ecd461d'
OLD='f24550979dba3251c95ea52a10e18e006a0bf2a6'
CAND='captures/2026-10-20T140000Z-codex-finite-calibration-f4b96720'
PRIOR='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d/evidence_return'
J1='captures/2026-10-20T183614Z-codex-j1-upper-central-e9ee47d7'
CANON='captures/2026-10-20T133000Z-codex-canonical-diamond-6d82a19f'
sha=lambda b:hashlib.sha256(b).hexdigest()
def js(b):return json.loads(b)
def git(repo,*args):return subprocess.check_output(['git',*args],cwd=repo)
def source(repo,path):return git(repo,'show',PIN+':'+path)
def planning_disclosures(doc):
    return {
        'explicit_open_return':doc.get('status')=='OPEN_APPARATUS_RETURN',
        'explicit_illustrative_no_measurements':doc.get('design_inputs_kind')=='Illustrative supplied mathematical bounds; no measurements',
        'explicit_no_execution':doc.get('experimental_execution')=='NONE',
        'review_pending':doc.get('independent_review')=='PENDING',
        'all_required_groups_open':bool(doc.get('required_records'))and all(x.get('status')=='OPEN'for x in doc['required_records'])
    }
def classify(doc):
    facts=planning_disclosures(doc)
    # It can reject a purported empirical return on explicit disclosures. It never
    # promotes unknown or self-asserted metadata into qualified empirical content.
    if facts['explicit_illustrative_no_measurements']or facts['explicit_no_execution']:
        return 'PLANNING_ONLY_NOT_AN_ACQUIRED_RETURN'
    return 'UNVERIFIED_CANDIDATE_REQUIRES_CONTENT_AND_AUTHORITY_REVIEW'
def controls(doc):
    rows=[]
    def ck(name,value):
        assert value,name;rows.append({'id':name,'pass':True})
    ck('original_design_is_not_acquired_return',classify(doc)=='PLANNING_ONLY_NOT_AN_ACQUIRED_RETURN')
    altered=dict(doc,status='PASS')
    ck('success_label_cannot_override_no_measurements',classify(altered)=='PLANNING_ONLY_NOT_AN_ACQUIRED_RETURN')
    altered=dict(doc,experimental_execution='DONE',independent_review='PASSED')
    ck('self_asserted_execution_does_not_override_design_kind',classify(altered)=='PLANNING_ONLY_NOT_AN_ACQUIRED_RETURN')
    ck('empty_unknown_document_not_qualified',classify({})=='UNVERIFIED_CANDIDATE_REQUIRES_CONTENT_AND_AUTHORITY_REVIEW')
    altered={'status':'PASS','experimental_execution':'DONE','independent_review':'PASSED'}
    ck('complete_labels_alone_not_qualified',classify(altered)=='UNVERIFIED_CANDIDATE_REQUIRES_CONTENT_AND_AUTHORITY_REVIEW')
    return rows
def run(repo):
    reads={}
    def read(path,scope='Content inspected'):
        b=source(repo,path);reads[path]={'path':path,'sha256':sha(b),'size_bytes':len(b),'inspection_scope':scope};return b
    profile=js(read(PRIOR+'/RETURN_PROFILE.json'));cross=js(read(PRIOR+'/BLOCKER_RETURN_CROSSWALK.json'));read(PRIOR+'/RETURN_REVIEW_GUIDE.md')
    assert len(profile['artifacts'])==14 and {x['id']for x in profile['artifacts']}=={'R%02d'%i for i in range(1,15)}
    assert len(cross['entries'])==128
    assert all(x['content_review_status']=='UNSUPPLIED_UNVERIFIED'and x['qualification_closed']is False for x in cross['entries'])
    assert profile['outreach_sent']is False and profile['qualification_blockers_closed']==0
    doc=js(read(CAND+'/FINITE_CALIBRATION_RETURN_v0.1.json'));prov=js(read(CAND+'/PROVENANCE_v0.1.json'));manifest=js(read(CAND+'/MANIFEST.json'));rat=js(read(CAND+'/RATIONAL_CERTIFICATE_v0.1.json'));tex=read(CAND+'/UD_FINITE_CALIBRATION_FAULT_CERTIFICATE_v0.1.tex').decode()
    assert all(planning_disclosures(doc).values()) and len(doc['required_records'])==7
    assert prov['constructor']=='Codex' and prov['reviewers']==[] and prov['physical_promotion']==0
    assert rat['certificate']['status']=='PASS_CONDITIONAL_DESIGN'
    assert rat['certificate']['input_kind']=='illustrative certified-bound inputs; no apparatus data'
    assert 'No experiment has been performed by this workstream.'in tex
    # Hash identity of every candidate manifest payload is checked; this is not
    # re-execution or semantic inspection of its opaque PDF/ZIP/image artifacts.
    candidate_inventory=[]
    for x in manifest['files']:
        b=read(x['path'],'Manifest payload identity checked; opaque payloads not executed or interpreted')
        assert sha(b)==x['sha256'] and len(b)==x['size_bytes'];candidate_inventory.append(x['path'])
    for dep in prov['dependencies']:
        b=read(dep['path'],'Provenance dependency identity checked; no physical claim admitted')
        assert sha(b)==dep['sha256']
    canon=js(read(CANON+'/MANIFEST.json'))
    assert canon['physical_promotion']==0 and canon['provenance']['reviewers']==[]
    delta=git(repo,'diff','--name-only',OLD,PIN).decode().splitlines();assert len(delta)==38
    assert all(x.startswith(J1+'/')or x=='events/'+J1.split('/')[-1]+'.json'for x in delta)
    jm=js(read(J1+'/MANIFEST.json'));jr=read(J1+'/REPORT.md').decode();read(J1+'/SOURCE_CONTEXT.json');read('events/'+J1.split('/')[-1]+'.json')
    assert jm['independent_review']is False and jm['physical_promotion']==0 and jm['scientific_status']=='OPEN'
    assert 'Measurement uncertainty, decimal parsing uncertainty and physical time/frequency calibration are outside this contract.'in jr
    # Inventory all newly added payload bytes, without interpreting binary witnesses.
    delta_inventory=[]
    for name in delta:
        b=read(name,'Complete delta payload identity inventoried; semantic inspection limited to manifest/report/context/event')
        delta_inventory.append({'path':name,'sha256':sha(b),'size_bytes':len(b)})
    allpaths=git(repo,'ls-tree','-r','--name-only',PIN).decode().splitlines()
    requested_paths=[x for x in allpaths if '/returned/'in x or x.startswith('returned/')]
    assert requested_paths==[]
    issue_summaries=[]
    for n in [241,270,130]:
        path=P/'sources'/f'ISSUE_{n}_SNAPSHOT.json';b=path.read_bytes();s=js(b);issue=s['issue'];comments=s['comments_tool_result']['structuredContent']['comments']
        assert issue['issue_number']==n and issue['state']=='open' and comments==[]
        assert 'UNSENT'in issue['body'] and 'Physical Promotion=0'in issue['body']
        issue_summaries.append({'issue_number':n,'url':issue['url'],'body_updated_at':issue['updated_at'],'body_bytes':len(issue['body'].encode()),'snapshot_sha256':sha(b),'all_page_comments_count':0,'retrieved_utc':s['retrieved_utc'],'interpretation':'Status/progress narrative and unresolved/UNSENT snapshot; no attributable acquired-return packet in body or comments'})
    group_map={
        'port_design':['R02','R08','R09','R10'],
        'canonical_scale':['R03','R04','R08','R09'],
        'finite_calibration':['R03','R05','R06'],
        'control_timing':['R04','R10'],
        'metrology':['R02','R03','R04','R05','R06','R09'],
        'blinded_controls':['R11','R12','R13'],
        'review':['R01','R14']}
    candidate_mapping=[]
    for x in doc['required_records']:
        candidate_mapping.append({'candidate_group':x['type'],'candidate_status':x['status'],'conceptually_related_roles':group_map[x['type']],'actual_records_disclosed':False,'requirements':x['records'],'mapping_status':'Content-topic crosswalk only; source/lane/domain identity not established'})
    roles=[]
    counts=collections.Counter(x['requested_artifact_id']for x in cross['entries'])
    for x in profile['artifacts']:
        roles.append({'id':x['id'],'title':x['title'],'requested_path':x['requested_path'],'required_content':x['required_content'],'required_sections':x['required_sections'],'conditional_sections':x.get('conditional_sections'), 'original_128_lineage_path_count':counts[x['id']], 'candidate_contribution':'Planning or conditional-mathematics context only; no actual accepted return for this role','newly_qualified_in_audited_scope':False,'qualification_status':'NOT_CLOSED_BY_THIS_AUDIT'})
    return {
      'status':'BOUNDED_EVIDENCE_AUDIT_COMPLETE_NO_QUALIFIED_ACQUISITION_RETURN_IN_SCOPE',
      'audit_created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'pinned_repository':'ud-tetra/UD','pinned_commit':PIN,'delta_base':OLD,
      'scope':{'candidate':CAND,'candidate_payloads_hash_checked':len(candidate_inventory),'candidate_semantic_sources':['FINITE_CALIBRATION_RETURN_v0.1.json','PROVENANCE_v0.1.json','MANIFEST.json','RATIONAL_CERTIFICATE_v0.1.json','UD_FINITE_CALIBRATION_FAULT_CERTIFICATE_v0.1.tex'],'delta_files':len(delta),'delta_capture':J1,'delta_semantic_sources':['MANIFEST.json','REPORT.md','SOURCE_CONTEXT.json','event'],'requested_return_path_inventory':{'matches':requested_paths,'interpretation':'No conventional returned/ paths in pinned tree; not proof that every possible external return under another name is absent'},'issues':issue_summaries,'excluded':['Other issue/mail/chat surfaces','Any unexported material','Broad public dataset search','Full semantic re-audit of every prior capture','Re-execution of conditional CD-1 mathematics or J1 numerics']},
      'candidate':{'classification':classify(doc),'explicit_disclosures':planning_disclosures(doc),'required_groups':candidate_mapping,'rational_design_certificate':'PASS_CONDITIONAL_DESIGN with explicitly illustrative inputs; this remains a valid conditional claim within its own stated scope','own_declared_lane':'Short-window CD-1 Gauss discriminator, not full campaign/endpoint admission','independent_review':'PENDING','experimental_execution':'NONE','physical_promotion':0,'role_R07_note':'Constructor conditional computation may inform a future design. It does not supply source-specific validated numerical/calibration evidence for an actual acquired record.'},
      'delta_finding':{'classification':'CONDITIONAL_COMPUTATIONAL_J1_STATE_NOT_EMPIRICAL_ACQUISITION','independent_review':False,'scientific_status':'OPEN','physical_promotion':0,'does_not_close_R01_R14':True},
      'role_requirements':roles,
      'historical_request_snapshot':{'original_path_count':128,'count_is_not_independent_gate_count':True,'counts_by_role':dict(sorted(counts.items())),'outreach_sent':False,'interpretation':'Preserved original ten-channel request lineage only. New CD-1/native/fresh-source domains need independent source-specific maps and counts. This audit does not globally re-prove absence of all128 requested facts.'},
      'new_qualified_R01_R14_returns_in_audited_scope':0,'physical_qualification_blockers_closed':0,
      'next_gate':{'priority':'Supply attributable acquisition/source identity and source-specific physical-unit/readout map, then actual calibration/time/transfer/joint-coverage records, prospective model/comparator/holdout freeze and attributable external content review.','minimal_first_bundle':['R01 actual authority/independence decision','R02 actual acquisition/custody/domain identity','R08/R09 independently supported physical model/state/readout/unit map','R13 fresh selection/exposure/pre-outcome lineage','R14 attributable external review and separate custodian ruling'],'warning_on_order':'This lists content dependencies, not permission to operate hardware, obtain private records, or send outreach. No authorization is granted by this audit.'},
      'controls':controls(doc),'source_files':sorted(reads.values(),key=lambda x:x['path']),
      'new_estimator_calls':0,'new_raw_records':0,'archive_code_executed':False,'external_outreach_sent':False,'hardware_operation':False,'public_site_or_project_board_updated':False,
      'lane':'Development — no registry entry','same_team_implementation_review':True,'external_promotion_review':'PENDING','physical_promotion':0,
      'audit_code_sha256':sha(Path(__file__).read_bytes())}
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--repo',required=True);a.add_argument('--out',required=True);q=a.parse_args();out=Path(q.out);assert not out.exists();d=run(Path(q.repo));out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'status':d['status'],'candidate_classification':d['candidate']['classification'],'delta_files':d['scope']['delta_files'],'new_qualified_returns':0,'source_files':len(d['source_files']),'controls':len(d['controls'])}))
