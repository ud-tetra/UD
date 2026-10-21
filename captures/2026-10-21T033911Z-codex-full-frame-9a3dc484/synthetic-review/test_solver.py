"""Independent SYNTHETIC-only actual-CLI tests; never a UD source admission."""
from pathlib import Path
from fractions import Fraction
import gzip, hashlib, json, os, subprocess, sys, time

HERE = Path(__file__).absolute().parent
SOLVER = HERE.parent / 'c33_solve.py'
H = lambda b: hashlib.sha256(b).hexdigest()
dump = lambda x: (json.dumps(x, indent=2, sort_keys=True)+'\n').encode()

def guarded(p):
    p = Path(p).absolute()
    assert p.is_relative_to(HERE) and p != HERE
    for a in [p, *p.parents]:
        assert not a.is_symlink(), 'symlink output ancestor rejected'
        if a == HERE: break
    assert p.resolve().is_relative_to(HERE.resolve())
    return p

def write(p, b):
    p=guarded(p); p.parent.mkdir(exist_ok=True, parents=True)
    with p.open('xb') as f: f.write(b)

def invoke(name, frame, args):
    od=guarded(HERE/'runs'/name)
    cmd=[sys.executable,str(SOLVER),'--frame',str(frame),'--out',str(od),*args]
    cpus=tuple(sorted(os.sched_getaffinity(0))[:2])
    env=dict(os.environ,OPENBLAS_NUM_THREADS='2',OMP_NUM_THREADS='2',MKL_NUM_THREADS='2')
    t=time.monotonic()
    proc=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env,
       preexec_fn=lambda:os.sched_setaffinity(0,cpus),timeout=600)
    rec={'argv':cmd,'returncode':proc.returncode,'elapsed_seconds':time.monotonic()-t,
         'cpu_affinity':cpus,'output_exists':od.exists(),
         'certificate_exists':(od/'FULL_SOLVE.json').exists()}
    write(HERE/'logs'/(name+'.stdout'),proc.stdout)
    write(HERE/'logs'/(name+'.stderr'),proc.stderr)
    write(HERE/'logs'/(name+'.json'),dump(rec))
    return rec,od

def main():
    freeze=json.loads((HERE/'FREEZE.json').read_bytes())
    assert H(SOLVER.read_bytes())==freeze['solver_sha256']
    assert H(Path(__file__).read_bytes())==freeze['test_source_sha256']
    assert H((HERE/'PLAN.json').read_bytes())==freeze['plan_sha256']
    assert not (HERE/'runs').exists() and not (HERE/'synthetic_frame').exists()
    frame=HERE/'synthetic_frame'; frame.mkdir()
    rows=[]; diag=[]; z=[]
    for i in range(1999):
        d=1<<(96-i%13); rhs=(1 if i%2==0 else -1)*(d*d//3)
        diag.append(d); z.append(rhs)
        raw=bytearray(2640*16); raw[16*i:16*(i+1)]=d.to_bytes(16,'little',signed=True)
        packed=gzip.compress(raw,compresslevel=9,mtime=0); fn=f'row_{i:04d}.i128.gz'
        write(frame/fn,packed)
        rows.append({'column':i,'output_row_file':fn,'output_row_sha256':H(packed),
          'output_decoded_sha256':H(raw),'state_integer_scale_bits':96,
          'rhs_dot_denominator_power2':192,'rhs_dot_integer':str(rhs)})
    meta={'status':'PASS_FULL1999_SOURCE_FRAME_CONSTRUCTION',
      'synthetic_source_excluded':True,'scope':'SYNTHETIC DIAGONAL FIXTURE ONLY; status is required CLI schema, not independently admitted UD source',
      'actual_rows_constructed_or_authenticated':1999,'data_scale_bits':96,'rows':rows}
    fb=dump(meta); write(frame/'FULL_FRAME.json',fb); fh=H(fb)
    inv=[]
    for name,args in [('missing_trusted_hash',[]),('wrong_trusted_hash',['--frame-sha256','0'*64])]:
        r,o=invoke(name,frame,args); assert r['returncode']!=0 and not r['certificate_exists']; inv.append(r)
    bad=HERE/'missing_coverage'; bad.mkdir(); mm=dict(meta,rows=rows[:-1]); mb=dump(mm)
    write(bad/'FULL_FRAME.json',mb)
    r,o=invoke('missing_coverage',bad,['--frame-sha256',H(mb)])
    assert r['returncode']!=0 and not r['certificate_exists']; inv.append(r)
    bad=HERE/'corrupt_row'; bad.mkdir(); write(bad/'FULL_FRAME.json',fb)
    packed=bytearray((frame/rows[0]['output_row_file']).read_bytes()); packed[-1]^=1
    write(bad/rows[0]['output_row_file'],packed)
    r,o=invoke('corrupt_row',bad,['--frame-sha256',fh])
    assert r['returncode']!=0 and not r['certificate_exists']; inv.append(r)
    r,out=invoke('synthetic_refinement',frame,['--frame-sha256',fh]); inv.append(r)
    assert r['returncode']==0 and r['certificate_exists']
    cert=json.loads((out/'FULL_SOLVE.json').read_bytes())
    cb=gzip.decompress((out/'COEFFICIENTS.json.gz').read_bytes()); c=json.loads(cb)
    raw=gzip.decompress((out/'LIFT.i128.gz').read_bytes())
    aa=list(map(int,c['coefficient_integers'])); assert len(aa)==1999
    q=[int.from_bytes(raw[i:i+16],'little',signed=True)for i in range(0,len(raw),16)]
    assert len(q)==2640 and c['coefficient_denominator_power2']==160
    scale=1<<160; rr=[d*d*a-rhs*scale for d,a,rhs in zip(diag,aa,z)]
    r2=sum(v*v for v in rr); li=[d*a for d,a in zip(diag,aa)]+[0]*641
    assert q==[v//scale for v in li]
    err=sum((qi*scale-l)**2 for qi,l in zip(q,li))
    assert r2==int(cert['normal_equation_residual_squared_integer'])
    assert cert['normal_equation_residual_denominator_power2']==352
    assert Fraction(cert['normal_equation_residual_squared'])==Fraction(r2,1<<704)
    assert err==int(cert['finite_lift_error_squared_integer'])
    assert cert['finite_lift_error_denominator_power2']==256
    assert Fraction(cert['finite_lift_error_squared'])==Fraction(err,1<<512)
    assert r2 < 1<<(704-128) and err < 1<<(512-88)
    assert H(cb)==cert['coefficient_decoded_sha256'] and H(raw)==cert['lift_decoded_sha256']
    assert H((out/'COEFFICIENTS.json.gz').read_bytes())==cert['coefficient_packed_sha256']
    assert H((out/'LIFT.i128.gz').read_bytes())==cert['lift_packed_sha256']
    assert c['frame_receipt_sha256']==fh==cert['frame_receipt_sha256']
    hist=cert['refinement_history']
    assert hist[0]['iteration']==0 and hist[0]['residual_gate_pass'] is False
    assert len(hist)>=2 and hist[-1]['residual_gate_pass'] is True
    assert int(hist[-1]['residual_squared_integer'])==r2
    # Rational oracle for the exact diagonal Gram solve, independent of FLINT/BLAS.
    oracle_errors=[Fraction(qi,1<<96)-Fraction(rhs,d*(1<<96))
       for qi,rhs,d in zip(q,z,diag)]+[Fraction(v,1<<96)for v in q[1999:]]
    oracle2=sum((x*x for x in oracle_errors),Fraction(0))
    coeff_lift2=sum((Fraction(d*a,1<<256)-Fraction(rhs,d*(1<<96)))**2
       for d,a,rhs in zip(diag,aa,z))
    # Componentwise triangle bound squared, without floating square roots.
    conservative2=2*(Fraction(err,1<<512)+coeff_lift2)
    assert oracle2<=conservative2
    # Deliberate one-unit coefficient/lift mutations must disagree with exact oracle checks.
    assert (diag[0]**2*(aa[0]+1)-z[0]*scale)!=rr[0]
    assert [q[0]+1,*q[1:]] != [v//scale for v in li]
    assert cert['physical_promotion']==0 and cert['physical_input_status']=='UNSUPPLIED_HOLD'
    assert H(SOLVER.read_bytes())==freeze['solver_sha256']
    res={'status':'PASS_SYNTHETIC_ACTUAL_CLI_INDEPENDENT_INTEGER_RATIONAL_AUDIT',
      'scope':'SYNTHETIC/source-excluded acceptance proves a record residual and finite lift certificate only; no UD source admission, physical accuracy, or external promotion',
      'solver_sha256':freeze['solver_sha256'],'frame_sha256':fh,'fixture_dimensions':[1999,2640],
      'initial_residual_gate':False,'final_residual_gate':True,'refinement_iterations':len(hist)-1,
      'exact_residual_squared':str(Fraction(r2,1<<704)),
      'exact_finite_lift_quantization_squared':str(Fraction(err,1<<512)),
      'exact_ideal_diagonal_solution_lift_error_squared':str(oracle2),
      'exact_coefficient_lift_error_squared':str(coeff_lift2),
      'exact_oracle_triangle_squared_upper':str(conservative2),
      'rejection_controls':4,'one_unit_oracle_corruption_controls':2,
      'invocations':inv,'physical_promotion':0,'external_promotion_review':'PENDING',
      'safe_input_allowlist':[str(SOLVER),str(frame)],
      'actual_UD_frames_read':False,'actual_UD_solves_executed':0,
      'stable_input_premise':'Exclusive synthetic fixture; hashes checked before/after; no universal concurrent snapshot claim'}
    write(HERE/'REVIEW_RECEIPT.json',dump(res))
    manifest={str(p.relative_to(HERE)):H(p.read_bytes()) for p in sorted(HERE.rglob('*')) if p.is_file()}
    write(HERE/'REVIEW_MANIFEST.json',dump(manifest))
    print(json.dumps({'status':res['status'],'refinement_iterations':len(hist)-1,'oracle_error_squared_float':float(oracle2)}))

if __name__=='__main__': main()
