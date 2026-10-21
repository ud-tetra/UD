"""Constructor algebra check; never certifies unavailable source-ledger objects."""
import json
from pathlib import Path
from fractions import Fraction

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(k,a): return tuple(k*x for x in a)

def main():
    # Exponents ordered M,L,T. These are explicit hypotheses, not recovered units.
    mass,length,time=(1,0,0),(0,1,0),(0,0,1)
    action=(1,2,-1)
    assert add(add(mass,scale(2,length)),scale(-1,time)) == action
    assert add(action,scale(-1,action)) == (0,0,0)
    # Exact rational probes guard direction in the normalized intake only.
    for a,h in [(Fraction(3,7),Fraction(5,11)),(Fraction(2),Fraction(9))]:
        eta=a/h
        assert eta*h == a
        assert (h/a)*eta == 1
    receipt={
        'status':'PASS_SCOPED_ALGEBRA_ONLY',
        'proof_scope':'Definitional algebra in AUDIT.md; rational probes and dimensional-vector checks here.',
        'dimensions_assumed':{'B0':'M','a0':'L','tau0':'T','hbar':'M L^2 T^-1'},
        'B0_mass_assignment_recovered_in_older_snapshot':True,
        'dimension_assignments_verified_in_v085':False,
        'conditional_pi_substitution_checked':True,
        'trace_map_reproduced':False,
        'ledger_v085_objects_source_verified':0,
        'reported_object_count':723,
        'reported_object_count_verified':False,
        'EXIT-03':'SOURCE_BLOCKED',
        'xi_act_identification':'OPEN',
        'eta_A_numeric':'OPEN',
        'non_constructor_review':'PENDING',
        'physical_promotion':0
    }
    (Path(__file__).parent/'CONSISTENCY_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))

if __name__=='__main__': main()
