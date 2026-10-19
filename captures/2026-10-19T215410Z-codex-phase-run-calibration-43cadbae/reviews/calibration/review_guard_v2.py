"""Post-known synthetic capture-layout guard checks only. No real capture/evidence is mutated."""
import ast,hashlib,importlib.util,json,sys,tempfile
from pathlib import Path
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent

def need(ok,msg):
    if not ok:raise RuntimeError(msg)

def digest(p):
    b=p.read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def main():
    bind=json.loads((HERE/'GUARD_INPUT_BINDINGS_v0.2.json').read_text());src=Path(bind['source_dir'])
    need(digest(src/'PROTOCOL_FREEZE_v0.2.json')==bind['source_freeze'],'v2sourcefreezechanged')
    for row in json.loads((src/'PROTOCOL_FREEZE_v0.2.json').read_text())['files']:
        need(digest(src/row['path'])=={'bytes':row['bytes'],'sha256':row['sha256']},'sourcechanged:'+row['path'])
    for row in json.loads((HERE/'GUARD_REVIEW_FREEZE_v0.2.json').read_text())['files']:
        need(digest(HERE/row['path'])=={'bytes':row['bytes'],'sha256':row['sha256']},'reviewchanged:'+row['path'])
    def without_guard(p):
        tree=ast.parse(p.read_text());tree.body=[n for n in tree.body if not (isinstance(n,ast.FunctionDef) and n.name=='output_path')]
        return ast.dump(tree,include_attributes=False)
    need(without_guard(src/'validate_request.py')==without_guard(src/'validate_request_v2.py'),'scientific/schema/metadata semantics changed')
    spec=importlib.util.spec_from_file_location('reviewed_guard_v2',src/'validate_request_v2.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
    results=[]
    def refused(name,candidate,request):
        try:r.output_path(candidate,request)
        except ValueError as e:
            need('MANIFEST_ANCESTOR' in str(e),'wrong guard reason:'+str(e))
            need(not candidate.exists(),'unexpected output created')
            results.append({'id':name,'pass':True,'reason':str(e)});return
        raise RuntimeError('protected layout accepted:'+name)
    with tempfile.TemporaryDirectory(prefix='ud-calibration-guard-review-') as td:
        root=Path(td);outer=root/'outer';inner=outer/'inner';packet=inner/'packet';sibling=outer/'sibling';external=root/'external'
        for p in (packet,sibling,external):p.mkdir(parents=True,exist_ok=True)
        (outer/'MANIFEST.json').write_text('{}\n');(inner/'MANIFEST.json').write_text('{}\n')
        old=r.HERE;r.HERE=packet
        try:
            refused('capture-sibling-output-refused',sibling/'new.json',external/'request.json')
            (external/'to_capture').symlink_to(sibling,target_is_directory=True)
            refused('external-symlink-into-capture-refused',external/'to_capture'/'new.json',external/'request.json')
            (outer/'to_external').symlink_to(external,target_is_directory=True)
            refused('capture-symlink-outside-refused',outer/'to_external'/'new.json',external/'request.json')
        finally:r.HERE=old
    plan=json.loads((HERE/'GUARD_REVIEW_PLAN_v0.2.json').read_text());need(set(x['id'] for x in results)==set(plan['controls']),'plan coverage')
    out={'artifact_type':'POST_V1_SAME_TEAM_CAPTURE_GUARD_REVIEW_RESULTS','all_pass':True,'controls':3,'results':results,'two_nested_manifest_roots_exercised':True,'sibling_outside_nearest_manifest_root_protected':True,'ast_unchanged_outside_output_path':True,'constructor_source_freeze':bind['source_freeze'],'review_freeze':digest(HERE/'GUARD_REVIEW_FREEZE_v0.2.json'),'v1_review_evidence_retained':True,'scope':'Post-known metadata path-safety tests under trusted nonconcurrent host. Temporary synthetic layouts only; no actualcapturewrite, evidenceURI,raw/model/calibration evaluation or signatures.','physical_promotion':0,'external_review':'PENDING'}
    print(json.dumps(out,indent=2)+'\n',end='')
if __name__=='__main__':main()
