"""Reject legal native programmes that miss the certified target operator."""
from pathlib import Path
import tempfile,subprocess,shutil,json,os
ROOT=Path(__file__).resolve().parent
def main():
    tests=[
      ('parameter_changed',lambda d:d['programs'][0]['parameter_numerators'].__setitem__(0,d['programs'][0]['parameter_numerators'][0]+10**10)),
      ('mask_changed',lambda d:d['programs'][0]['masks'][0].__setitem__(0,1-d['programs'][0]['masks'][0][0])),
      ('target_sign_changed',lambda d:d['programs'][0].__setitem__('u','-1/2'))]
    controls=[]
    for label,change in tests:
        with tempfile.TemporaryDirectory() as tmp:
            dst=Path(tmp)
            for f in ['native_model.py','verify_writer.py','WRITER_SCHEDULES.json']:shutil.copyfile(ROOT/f,dst/f)
            d=json.loads((dst/'WRITER_SCHEDULES.json').read_text());change(d)
            (dst/'WRITER_SCHEDULES.json').write_text(json.dumps(d))
            r=subprocess.run(['python3',str(dst/'verify_writer.py')],capture_output=True,text=True,
                env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
            assert r.returncode!=0 and 'AssertionError' in r.stderr
            controls.append({'control':label,'rejected':True,'returncode':r.returncode})
    (ROOT/'CERTIFICATE_CONTROLS.json').write_text(json.dumps(controls,indent=2)+'\n')
    print(json.dumps(controls))
if __name__=='__main__':main()
