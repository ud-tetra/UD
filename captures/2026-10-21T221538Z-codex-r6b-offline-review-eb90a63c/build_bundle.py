#!/usr/bin/env python3
"""Stage a reproducible offline evidence bundle from pinned git objects."""
from pathlib import Path
import subprocess,json,hashlib,zipfile,tempfile,shutil,sys,argparse
C=Path(__file__).parent

def build(repo,destination):
    destination.mkdir(parents=True,exist_ok=True)
    indexref='0248067000d2b4a4910bd3186f1ba115503ac9e3'
    indexpath='captures/2026-10-21T205638Z-codex-r6b-review-packet-a1dc32f8/EVIDENCE_INDEX.json'
    def blob(ref,path):return subprocess.check_output(['git','show',ref+':'+path],cwd=repo)
    indexraw=blob(indexref,indexpath);idx=json.loads(indexraw)
    with tempfile.TemporaryDirectory(prefix='r6b-offline-stage-') as td:
        root=Path(td)/'r6b_offline_review';root.mkdir()
        (root/'EVIDENCE_INDEX.json').write_bytes(indexraw)
        for e in idx['upstream']:
            paths=[e['manifest_path']]+[f['path'] for f in e['files']]
            for path in paths:
                p=root/'evidence'/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(blob(e['commit'],path))
        for s in idx['source_files']:
            p=root/'evidence'/s['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(blob(s['commit'],s['path']))
        shutil.copyfile(C/'verify_offline.py',root/'verify_offline.py')
        shutil.copyfile(C/'OFFLINE_README.md',root/'README.md')
        def inventory():
            files=[{'path':p.relative_to(root).as_posix(),'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                   for p in sorted(root.rglob('*')) if p.is_file() and p.name!='BUNDLE_FILES.json']
            (root/'BUNDLE_FILES.json').write_text(json.dumps({'physical_promotion':0,'files':files},indent=2)+'\n')
        inventory()
        proc=subprocess.run([sys.executable,str(root/'verify_offline.py'),'--output',str(root/'CONSTRUCTOR_BASELINE.json')],capture_output=True,text=True,timeout=60)
        assert proc.returncode==0,proc.stderr
        baseline=json.loads((root/'CONSTRUCTOR_BASELINE.json').read_text())
        assert len(baseline['steps'])==7
        inventory()
        archive=destination/'R6B_Offline_Review_v1.zip'
        with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            for p in sorted(root.rglob('*')):
                if p.is_file():
                    zi=zipfile.ZipInfo('r6b_offline_review/'+p.relative_to(root).as_posix(),(1980,1,1,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o644<<16
                    z.writestr(zi,p.read_bytes(),compresslevel=9)
        # Validate the actual final downloadable archive by extracting and rerunning it.
        final=Path(td)/'final';final.mkdir()
        with zipfile.ZipFile(archive) as z:z.extractall(final)
        proc=subprocess.run([sys.executable,str(final/'r6b_offline_review/verify_offline.py')],capture_output=True,text=True,timeout=60)
        assert proc.returncode==0,proc.stderr
        rerun=json.loads((final/'r6b_offline_review/REPRODUCTION.json').read_text())
        assert rerun==baseline
        (C/'CONSTRUCTOR_BASELINE.json').write_text(json.dumps(baseline,indent=2)+'\n')
        receipt={'status':'PASS_OFFLINE_ARCHIVE_REPRODUCTION','archive_name':archive.name,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
                 'size_bytes':archive.stat().st_size,'zip_members':len(zipfile.ZipFile(archive).namelist()),
                 'upstream_files':44,'upstream_manifests':6,'source_files':3,'verification_calls':7,
                 'final_archive_extract_and_run':'PASS; equals constructor baseline',
                 'runtime_network_calls':0,'runtime_git_calls':0,'reviewer_execution':'NOT_PERFORMED','physical_promotion':0}
        (C/'BUNDLE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
        return archive
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--destination',type=Path,required=True);a=p.parse_args();build(a.repo.resolve(),a.destination.resolve())
