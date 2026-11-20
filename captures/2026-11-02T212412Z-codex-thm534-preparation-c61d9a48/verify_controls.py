"""Rejected changes and fresh deterministic replay; standard library only."""
from pathlib import Path
import subprocess,sys,shutil,tempfile,hashlib,json
root=Path(__file__).resolve().parent
names=("native_model.py","interval_exact.py","verify_preparation.py")
changes=[
 ("zero_clock","R=Q(1,1000);EPS=Q(1,10**6)","R=Q(0);EPS=Q(1,10**6)"),
 ("unsupported_large_ball","R=Q(1,1000);EPS=Q(1,10**6)","R=Q(1,1000);EPS=Q(1,1000)"),
 ("reopened_output_gate","H=m.native([0,1,0,1,0,1,0])","H=m.native([1,1,0,1,0,1,0])")]
controls=[]
for label,old,new in changes:
    with tempfile.TemporaryDirectory() as tmp:
        p=Path(tmp)
        for name in names:shutil.copyfile(root/name,p/name)
        f=p/"verify_preparation.py";text=f.read_text();assert old in text
        f.write_text(text.replace(old,new,1))
        r=subprocess.run([sys.executable,str(f)],capture_output=True,text=True)
        assert r.returncode!=0 and "AssertionError" in r.stderr,label
        controls.append({"control":label,"rejected":True,"returncode":r.returncode})
with tempfile.TemporaryDirectory() as tmp:
    p=Path(tmp)
    for name in names:shutil.copyfile(root/name,p/name)
    r=subprocess.run([sys.executable,str(p/"verify_preparation.py")],capture_output=True,text=True,check=True)
    hashes={}
    for name in ("RESULTS.json","SIGNED_CELL_RECEIPTS.json"):
        a=(p/name).read_bytes();assert a==(root/name).read_bytes()
        hashes[name]=hashlib.sha256(a).hexdigest()
    assert r.stdout==(root/"verification_stdout.txt").read_text()
result={"status":"PASS","mutations":controls,"fresh_replay_sha256":hashes,"stdout_byte_match":True}
(root/"CONTROLS.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps(result,indent=2,sort_keys=True))
