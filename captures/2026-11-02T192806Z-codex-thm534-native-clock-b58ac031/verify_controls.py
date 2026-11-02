"""Reject altered preparation and a spurious direct core/clock contact."""
from pathlib import Path
import json, subprocess, sys, tempfile, shutil, hashlib
root=Path(__file__).resolve().parent
records=[]
for label in ("altered_mode","extra_contact"):
    with tempfile.TemporaryDirectory() as tmp:
        p=Path(tmp)
        for name in ("native_model.py","verify_clock.py"):
            shutil.copyfile(root/name,p/name)
        if label=="altered_mode":
            f=p/"verify_clock.py"
            old="w=lin(1,unit(3),-1,unit(4))"
            text=f.read_text();assert old in text
            f.write_text(text.replace(old,"w=lin(1,unit(3),0,unit(4))"))
        else:
            f=p/"native_model.py"
            text=f.read_text();assert "    return a\n" in text
            # Change only native(), not boundary().
            before,tail=text.split("def native(h):",1)
            f.write_text(before+"def native(h):"+tail.replace(
                "    return a\n",
                "    a[3][22]=Q(1);a[22][3]=Q(-1)\n    return a\n",1))
        r=subprocess.run([sys.executable,str(p/"verify_clock.py")],capture_output=True,text=True)
        assert r.returncode!=0 and "AssertionError" in r.stderr,label
        records.append({"control":label,"rejected":True,"returncode":r.returncode})
with tempfile.TemporaryDirectory() as tmp:
    p=Path(tmp)
    for name in ("native_model.py","verify_clock.py"):shutil.copyfile(root/name,p/name)
    r=subprocess.run([sys.executable,str(p/"verify_clock.py")],capture_output=True,text=True,check=True)
    assert (p/"RESULTS.json").read_bytes()==(root/"RESULTS.json").read_bytes()
    assert r.stdout==(root/"RESULTS.json").read_text()
    replay=hashlib.sha256((p/"RESULTS.json").read_bytes()).hexdigest()
result={"status":"PASS","mutations":records,"fresh_replay_sha256":replay}
(root/"CONTROLS.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps(result,indent=2,sort_keys=True))
