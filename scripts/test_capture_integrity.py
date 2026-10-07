import hashlib,json,tempfile,subprocess
from pathlib import Path
from verify_repository import verify
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
print(json.dumps({'status':'PASS','checks':checks}))
