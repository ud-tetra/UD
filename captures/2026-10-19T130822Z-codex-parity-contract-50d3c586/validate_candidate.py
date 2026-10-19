"""Prospective numeric admission only. No archived runner execution."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import hashlib, importlib.util, json, math
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
CONTRACT=json.loads((ROOT/'CONTRACT.json').read_text())
def source():
    for pin in CONTRACT['source_pins']:
        if hashlib.sha256((REPO/pin['path']).read_bytes()).hexdigest()!=pin['sha256']:
            raise ValueError('source_hashes')
    pin=next(x for x in CONTRACT['source_pins'] if x['path'].endswith('exact_selector_check.py'))
    spec=importlib.util.spec_from_file_location('pinned_selector',REPO/pin['path'])
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    _,(a,p0,p1)=mod.verify() # fresh constructor exact reconstruction, not imported runner
    a=[[float(x) for x in r] for r in a]
    p=[[float(x)+math.sqrt(8065)*float(y) for x,y in zip(r,s)] for r,s in zip(p0,p1)]
    return a,p

def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def scale(a,k):return [[k*x for x in r] for r in a]
def eye(n):return [[float(i==j) for j in range(n)] for i in range(n)]
def norm(a):return max(sum(abs(x) for x in r) for r in a)
def close(a,b):
    if not all(math.isfinite(x) for m in (a,b) for r in m for x in r):return False
    error=norm([[x-y for x,y in zip(r,s)] for r,s in zip(a,b)])
    left,right=norm(a),norm(b)
    if not all(math.isfinite(v) for v in (error,left,right)):return False
    return error <= CONTRACT['numeric']['atol']+CONTRACT['numeric']['rtol']*max(left,right)
def matrix(a,shape):
    return isinstance(a,list) and len(a)==shape[0] and all(isinstance(r,list) and len(r)==shape[1] and all(type(x) in (int,float) and math.isfinite(x) for x in r) for r in a)
def canonical(a,p,c=2.0):
    u=[[0.0]*3 for _ in range(30)]
    for j,(seed,den) in enumerate(zip(([1,-1,0,0],[1,1,-2,0],[1,1,1,-3]),(2,6,12))):
        for i,x in enumerate(seed):u[i][j]=x/math.sqrt(den)
    q=scale(mm(p,u),1/math.sqrt((1+89/math.sqrt(8065))/2))
    momentum=scale(mm(a,q),1/math.sqrt(5));w=[r+s for r,s in zip(q,momentum)]
    r=[[float((1 if i<3 else -1) if i==j else 0) for j in range(6)] for i in range(6)]
    ic=[[float((c if i<3 else 1/c) if i==j else 0) for j in range(6)] for i in range(6)]
    return {'W':w,'T':tr(w),'Theta':mm(mm(w,r),tr(w)),'Ic':ic,'c':c}
def validate(case,a,p):
    # a,p are rebuilt once by source(), never accepted from candidate payload.
    if set(case)!={'W','T','Theta','Ic','c'}:return {'status':'INELIGIBLE','reason':'fields'}
    c=case['c']
    if type(c) not in (int,float) or not math.isfinite(c) or not 0.001<=c<=1000:
        return {'status':'INELIGIBLE','reason':'types_finite_positive_c'}
    for k,shape in CONTRACT['types'].items():
        if k!='c' and not matrix(case[k],shape):return {'status':'INELIGIBLE','reason':'types_finite_positive_c'}
    w,t,h,ic=(case[k] for k in ('W','T','Theta','Ic'))
    r=[[float((1 if i<3 else -1) if i==j else 0) for j in range(6)] for i in range(6)]
    j=[[float(-1 if col==row+3 else 1 if row==col+3 else 0) for col in range(6)] for row in range(6)]
    s=[[float(col==(row+3)%6) for col in range(6)] for row in range(6)]
    expected_ic=[[float((c if i<3 else 1/c) if i==j else 0) for j in range(6)] for i in range(6)]
    f=mm(w,ic)
    pairs={
      'W_orthonormal':(mm(tr(w),w),eye(6)),
      'selected_membership':(mm(p,w),w),
      'native_generator':(mm(a,w),scale(mm(w,j),math.sqrt(5))),
      'Darboux_pullback':(scale(mm(mm(tr(w),a),w),1/math.sqrt(5)),j),
      'T_definition':(t,tr(w)), 'Theta_definition':(h,mm(mm(w,r),tr(w))),
      'Ic_definition':(ic,expected_ic),
      'event_intertwining':(mm(t,h),mm(r,t)),
      'Ic_intertwining':(mm(r,ic),mm(ic,r)),
      'Theta_F':(mm(h,f),mm(f,r)),
      'full_typed_composite':(mm(mm(mm(t,h),w),ic),mm(ic,r)),
      'ambient_square':(mm(h,h),p),
      'event_antisymplectic':(mm(mm(r,j),r),scale(j,-1)),
      'copy_swap':(mm(mm(s,r),tr(s)),scale(r,-1))}
    gates={k:close(*v) for k,v in pairs.items()}
    return {'status':'NUMERICAL_SOURCE_ADMITTED' if all(gates.values()) else 'REJECTED','gates':gates}
if __name__=='__main__':
    try:
        a,p=source()
        result=validate(json.loads(Path(sys.argv[1]).read_text()),a,p)
    except (ValueError,OverflowError,TypeError):result={'status':'INELIGIBLE','reason':'invalid_input'}
    print(json.dumps(result,indent=2))
