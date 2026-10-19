"""Public constructor fixtures; no blinding or independent review claimed."""
import sys
sys.dont_write_bytecode=True
import copy, hashlib,json
from validate_candidate import source,canonical,validate,norm,ROOT,CONTRACT

def main():
    a,p=source();good=canonical(a,p);results={}
    pin=CONTRACT['source_pins'][0];saved=pin['sha256'];pin['sha256']='0'*64
    try:
        source()
        raise AssertionError('hash mismatch accepted')
    except ValueError as err:
        assert str(err)=='source_hashes'
    finally:pin['sha256']=saved
    results['source_hash_mismatch']='rejected before reconstruction'
    def run(name,case,status,failed=None):
        out=validate(case,a,p)
        assert out['status']==status,(name,out)
        if failed:assert out['gates'][failed] is False,(name,out)
        results[name]=out
    run('native_positive',good,'NUMERICAL_SOURCE_ADMITTED')
    for name,c in [('zero',0),('negative',-2),('nan',float('nan')),('infinity',float('inf')),('bool',True),('outside_numeric_domain',1001)]:
        q=copy.deepcopy(good);q['c']=c;run(name,q,'INELIGIBLE')
    q=copy.deepcopy(good);q['W']=[[float(i==j) for j in range(6)] for i in range(30)]
    q['T']=[list(x) for x in zip(*q['W'])]
    q['Theta']=[[float((1 if i<3 else -1) if i==j and i<6 else 0) for j in range(30)] for i in range(30)]
    run('coordinate_carrier',q,'REJECTED','selected_membership')
    q=copy.deepcopy(good);q['Ic']=[[float((2 if i<3 else 3) if i==j else 0) for j in range(6)] for i in range(6)]
    run('commuting_nonreciprocal',q,'REJECTED','Ic_definition')
    q=copy.deepcopy(good);q['T']=q['W'];run('wrong_typed_shape',q,'INELIGIBLE')
    q=copy.deepcopy(good);q['W'][0][0]=float('nan');run('matrix_nan',q,'INELIGIBLE')
    q=copy.deepcopy(good);q['Theta'][0][0]+=0.01;run('tampered_theta',q,'REJECTED','full_typed_composite')
    # All 6 entries accumulate under row-sum norm; max-entry would incorrectly pass.
    from validate_candidate import close
    assert norm([[2e-11]*6])==1.2e-10
    assert not close([[2e-11]*6],[[0.0]*6])
    results['row_sum_boundary']='rejected as required'
    assert not close([[1e308]*6],[[1e308]*6])
    results['overflowed_norm']='rejected despite finite entries'
    # Missing embedding is dimensionally invalid: T(6x30) Theta(30x30) Ic(6x6).
    assert CONTRACT['types']['Theta'][1]!=CONTRACT['types']['Ic'][0]
    results['omitted_embedding']='dimension mismatch; W(30x6) mandatory'
    # Every required numerical gate is reported and cannot be bypassed by fields.
    expected=set(CONTRACT['required_gates'])-{'source_hashes','types_finite_positive_c'}
    assert set(results['native_positive']['gates'])==expected
    results['contract_sha256']=hashlib.sha256((ROOT/'CONTRACT.json').read_bytes()).hexdigest()
    results['classification']='CONSTRUCTOR_SELF_TEST_ONLY'
    results['physical_promotion']=0
    print(json.dumps(results,indent=2))
if __name__=='__main__':main()
