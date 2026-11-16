import hashlib,json,shutil,tempfile,subprocess
from pathlib import Path
from verify_repository import LEGACY_CAPTURE, LEGACY_EVENT, verify
def write_fixture(root):
 cap=root/'captures/fixture';cap.mkdir(parents=True);(root/'events').mkdir()
 (cap/'artifact.txt').write_text('retained evidence\n')
 path='captures/fixture/artifact.txt';p=root/path
 m={'capture_id':'fixture','physical_promotion':0,'files':[{'path':path,'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}]}
 (cap/'MANIFEST.json').write_text(json.dumps(m));(root/'events/fixture.json').write_text(json.dumps({'capture_id':'fixture'}));return cap,m
def git(root,*args):
 return subprocess.run(['git',*args],cwd=root,check=True,capture_output=True,text=True).stdout.strip()
checks=[]
with tempfile.TemporaryDirectory() as tmp:
 root=Path(tmp);cap,m=write_fixture(root);assert verify(root)['status']=='PASS';checks.append('valid capture passes')
 (cap/'artifact.txt').write_text('changed evidence!\n')
 try:verify(root)
 except AssertionError:checks.append('content tampering rejected')
 else:raise AssertionError('tampering passed')
 (cap/'artifact.txt').write_text('retained evidence\n');git(root,'init','-q');git(root,'add','.');git(root,'-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','fixture')
 base=git(root,'rev-parse','HEAD');p=cap/'artifact.txt';p.write_text('new retained evidence\n');m['files'][0]['size_bytes']=p.stat().st_size;m['files'][0]['sha256']=hashlib.sha256(p.read_bytes()).hexdigest();(cap/'MANIFEST.json').write_text(json.dumps(m))
 git(root,'add','.');git(root,'-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','attempt overwrite')
 try:verify(root,base)
 except AssertionError as e:
  assert 'immutable' in str(e);checks.append('historical overwrite rejected even with renewed hashes')
 else:raise AssertionError('historical overwrite passed')
 (root/'events/fixture.json').unlink()
 try:verify(root)
 except AssertionError:checks.append('missing capture event rejected')
 else:raise AssertionError('missing event passed')
# Check the actual archived bytes and ensure the compatibility branch carries
# the same digest and missing-event guarantees as ordinary captures.
with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    repo = Path(__file__).resolve().parents[1]
    capture = Path("captures") / LEGACY_CAPTURE
    shutil.copytree(repo / capture, root / capture)
    (root / "events").mkdir()
    shutil.copyfile(repo / LEGACY_EVENT, root / LEGACY_EVENT)
    assert verify(root) == {"status": "PASS", "manifests": 1, "checked_files": 3, "events": 1}
    checks.append("pinned legacy manifest and event accepted")
    for relative in (capture / "REPORT.md", capture / "MANIFEST.json", Path(LEGACY_EVENT)):
        p = root / relative
        original = p.read_bytes()
        p.write_bytes(bytes([original[0] ^ 1]) + original[1:])
        try:
            verify(root)
        except AssertionError as e:
            assert "SHA-256" in str(e)
        else:
            raise AssertionError(f"legacy tampering passed for {relative}")
        p.write_bytes(original)
    checks.append("legacy manifest, payload and event tampering rejected")
    (root / LEGACY_EVENT).unlink()
    try:
        verify(root)
    except AssertionError as e:
        assert "missing legacy capture event" in str(e)
        checks.append("missing legacy event rejected")
    else:
        raise AssertionError("missing legacy event passed")
print(json.dumps({'status':'PASS','checks':checks}))
