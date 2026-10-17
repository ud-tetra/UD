"""Constructor-team finite reversible-carrier checks; no native realization claim."""
from dataclasses import dataclass, replace, asdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib, importlib.util, json, sys, time

SITE=Path(sys.argv[1] if len(sys.argv)>1 else '/workspace/sites/unified-dynamics-public').resolve()
OUT=Path(sys.argv[2] if len(sys.argv)>2 else '/workspace/scratch/384298a218b5/joint-carrier-parallel-results.json').resolve()
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
input_hashes={name:sha(SITE/name) for name in ['rsp1.py','response_contract.py']}
sys.path.insert(0,str(SITE))
spec=importlib.util.spec_from_file_location('rsp1_joint_actual',SITE/'rsp1.py')
rsp=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rsp;spec.loader.exec_module(rsp)
started=time.monotonic()

@dataclass(frozen=True)
class Payload:
    W:int
    H:tuple
    R:tuple

@dataclass(frozen=True)
class Joint:
    clock:int
    active:Payload
    donors:tuple

def tick(x,F,rho,m,inverse=False):
    N=len(x.active.H);B=len(x.donors);L=(B+1)*(N+1)
    c=(x.clock-1)%L if inverse else x.clock
    j,i=divmod(c,N+1);p=x.active;ds=list(x.donors)
    if i<N:
        hs=list(p.H);rs=list(p.R)
        if inverse:
            old_w=hs[i];old_h=(p.W-F[old_w])%len(F);old_r=(rs[i]-rho[old_w])%m
            w=old_w;hs[i]=old_h;rs[i]=old_r
        else:
            w=(hs[i]+F[p.W])%len(F);hs[i]=p.W;rs[i]=(rs[i]+rho[p.W])%m
        p=Payload(w,tuple(hs),tuple(rs))
    elif j<B:p,ds[j]=ds[j],p
    return Joint(c if inverse else (c+1)%L,p,tuple(ds))

def prepared(F,rho,m,N,B,s0=0):
    fresh=Payload(s0,(0,)*N,(0,)*N)
    return Joint(0,fresh,(fresh,)*B)

def check_prepared(F,rho,m,N,B,s0=0):
    x=prepared(F,rho,m,N,B,s0);states=[x];outgoing=[]
    source=[s0]
    for _ in range(N):source.append(F[source[-1]])
    for j in range(B+1):
        for i in range(N):
            old=x;x=tick(x,F,rho,m)
            assert x.active.W==source[i+1]
            assert x.active.H[i]==source[i]
            assert x.active.R[i]==rho[source[i]]
            assert x.active.H[i+1:]==(0,)*(N-i-1)
            assert x.active.R[i+1:]==(0,)*(N-i-1)
            assert tick(x,F,rho,m,True)==old
            states.append(x)
        outgoing.append(x.active)
        if j<B:
            old=x;x=tick(x,F,rho,m)
            assert x.active==Payload(s0,(0,)*N,(0,)*N)
            assert x.donors[j]==outgoing[j]
            assert tick(x,F,rho,m,True)==old
            states.append(x)
    L=(B+1)*(N+1)
    assert len(states)-1==L-1 and x.clock==L-1
    assert x.donors==tuple(outgoing[:-1])
    wrapped=tick(x,F,rho,m)
    assert wrapped.clock==0 and wrapped.active==x.active and wrapped.donors==x.donors
    assert tick(wrapped,F,rho,m,True)==x
    return states,wrapped

# Exhaustive dirty configurations: 4 clocks *8 active payloads *8 donors.
payloads=[Payload(w,(h,),(r,)) for w,h,r in product(range(2),repeat=3)]
dirty=[Joint(c,p,(d,)) for c,p,d in product(range(4),payloads,payloads)]
assert len(dirty)==256
dirty_checks=prepared_checks=0
for F in product(range(2),repeat=2):
    for rho in product(range(2),repeat=2):
        images=set()
        for x in dirty:
            y=tick(x,F,rho,2);images.add(y)
            assert tick(y,F,rho,2,True)==x
            assert tick(tick(x,F,rho,2,True),F,rho,2)==x
            dirty_checks+=1
        assert set(dirty)==images
        for s0 in range(2):check_prepared(F,rho,2,1,1,s0);prepared_checks+=1

# General-dimensional prepared windows (bounded, not exhaustive arbitrary dimensions).
general_checks=0
for d,m,N,B in [(2,2,2,0),(2,2,2,2),(3,3,3,2),(3,2,2,1)]:
    for F in product(range(d),repeat=d):
        for rho in product(range(m),repeat=d):
            check_prepared(F,rho,m,N,B)
            general_checks+=1

# Noninjective F retains input distinction in history even when W/rho coincide.
F=(0,0);rho=(0,0)
a=prepared(F,rho,2,1,0,0);b=prepared(F,rho,2,1,0,1)
aa=tick(a,F,rho,2);bb=tick(b,F,rho,2)
assert aa.active.W==bb.active.W==0
assert aa.active.H!=bb.active.H
assert aa!=bb

# Fixed work output does not imply a fixed complete carrier: clock advances.
fixed=prepared((0,1),(0,0),2,1,1)
fixed_next=tick(fixed,(0,1),(0,0),2)
assert fixed.active==fixed_next.active and fixed!=fixed_next

# Dirty reuse counterexamples and honest exception.
states,wrapped=check_prepared((1,1),(0,0),2,2,0)
first=tick(wrapped,(1,1),(0,0),2);second=tick(first,(1,1),(0,0),2)
assert first.active.W==1 and second.active.W==0  # clean continuation would stay1
_,receipt_wrap=check_prepared((1,1),(1,1),2,1,1)
receipt_reuse=tick(receipt_wrap,(1,1),(1,1),2)
assert receipt_reuse.active.R[0]==0  # fresh receipt would be1
_,donor_wrap=check_prepared((1,1),(0,0),2,1,1)
donor_after_compute=tick(donor_wrap,(1,1),(0,0),2)
donor_after_swap=tick(donor_after_compute,(1,1),(0,0),2)
assert donor_after_swap.active==donor_wrap.donors[0]
assert donor_after_swap.donors[0]==donor_after_compute.active
assert donor_after_swap.active.W==1  # a fresh episode would restart at0
_,trivial_wrap=check_prepared((0,0),(0,0),2,1,1)
assert trivial_wrap==prepared((0,0),(0,0),2,1,1)

# Exact correlated/superposition whole-payload SWAP; classical basis permutation
# extends unitarily, exports correlation to donor, and leaves fresh active pure.
p0=Payload(0,(0,),(0,));p1=Payload(1,(1,),(1,));fresh=p0
psi={(p0,fresh,0):Fraction(3,5),(p1,fresh,1):Fraction(4,5)}
swapped={(donor,active,ref):amp for (active,donor,ref),amp in psi.items()}
assert sum(a*a for a in psi.values())==sum(a*a for a in swapped.values())==1
assert {active for active,donor,ref in swapped}=={fresh}
assert {(donor,ref) for active,donor,ref in swapped}=={(p0,0),(p1,1)}
restored={(donor,active,ref):amp for (active,donor,ref),amp in swapped.items()}
assert restored==psi

# Integrate actual RSP trajectories: one finite trajectory plus its terminal
# state is a closed source carrier, relabeled so the prepared state is0.
rsp_cases={}
for branch in 'CH':
    start=rsp.State((1,0,0),(0,0,0),(0,0,0),(1,0,0),((0,0,0),(1,0,0)),0,branch)
    source=[start]
    while True:
        row=rsp.transition(source[-1])
        if not row['changed']:break
        source.append(row['state'])
    F=tuple(min(i+1,len(source)-1) for i in range(len(source)))
    rho=tuple(rsp.transition(s)['event']['mu_theta']+3 for s in source)
    N=len(source)-1;B=1;m=7;d=len(source)
    window,wrapped=check_prepared(F,rho,m,N,B)
    assert len(window)-1==(B+1)*(N+1)-1
    P=d**(N+1)*m**N;L=(B+1)*(N+1)
    rsp_cases[branch]={'source_carrier_labels':d,'source_committed_updates':N,'rho_encoding':'mu_theta+3 in alphabet0..6','episodes':B+1,'prepared_donors':B,'payload_dimension':P,'joint_dimension':L*P**(B+1),'master_period_labels':L,'valid_window_transitions':L-1,'rsp_initial_stock':rsp.available_stock(start),'rsp_final_stock':rsp.available_stock(source[-1]),'scope':'Finite closed trajectory carrier relabeled with s0=0; tokens remain typed RSP registers, not native carrier energy.'}

assert all(sha(SITE/name)==digest for name,digest in input_hashes.items())
report={
 'status':'PASS','physical_promotion':0,
 'scope':'Constructor-team AI mathematical verification; no native Hodge Hamiltonian, local gate synthesis, independent physical review, actual quantum-device execution or physical clock identified.',
 'input_hashes':input_hashes,'checker_sha256':sha(__file__),
 'exhaustive_dirty_domain':{'d':2,'m':2,'N':1,'B':1,'states_per_rule':256,'F_rho_rule_pairs':16,'bijection_and_inverse_checks':dirty_checks,'prepared_windows':prepared_checks},
 'general_prepared_window_checks':general_checks,
 'formulas':{'payload_dimension':'P=d^(N+1)*m^N','joint_dimension':'L*P^(B+1), L=(B+1)(N+1)','inverse_gate':'w=h_i_prime; h_i=w_prime-F(w) mod d; r_i=r_i_prime-rho(w) mod m','valid_window':'First L-1 transitions; Lth tick only wraps the master clock. Fresh supply is B donor payloads, not regenerated blank memory.'},
 'adversarial_checks':{'noninjective_F_history_retains_distinction':'PASS','fixed_W_still_has_clock_transition':'PASS','dirty_carry_N2_constant_F':'second reused gate gives W0 versus clean continuationW1','dirty_receipt_N1':'first reused receipt gives0 versus fresh receipt1','exported_donor_reuse':'For constant F1, reused donor returns W1 rather than prepared W0; both payloads are swapped intact, so no fresh reset occurs.','trivial_reuse_exception':'F0=0,rho0=0 leaves prepared payloads unchanged, so clock wrap can reuse this special orbit','correlated_superposition_SWAP':'Exact rational amplitudes3/5,4/5; norm and reference correlation preserved; old active information exported to donor, never erased.'},
 'RSP_integration':rsp_cases,
 'weaknesses_and_repairs':['Dirty reuse failure is possible, not universal or necessarily immediate. State explicit finite-window validity and supply debt.','Initial labels should identify a fixed source state s0; encode s0=0 once, before defining the source table.','The global permutation is not an all-time state-only factor of dissipative F. Intertwining is asserted only at prepared compute prefixes.','Whole-payload SWAP requires export capacity and a gate/clock implementation; it does not reset the joint carrier or produce fresh environmental resources.','Master-clock identity at the final payload tick leaves payload untouched, but increment/wrap still changes the full clock state.','For superpositions, logical records retain coherence; they are not independently classical receipts or authenticated measurements without an additional readout model.','Source-register labels and modular history/receipt arithmetic have no proved equality with Hodge amplitudes, conserved support, energy or physical time.'],
 'elapsed_seconds':round(time.monotonic()-started,3)
}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','dirty_checks':dirty_checks,'prepared_small_windows':prepared_checks,'general_prepared_windows':general_checks,'RSP_branches':list(rsp_cases),'checker_sha256':sha(__file__),'results_sha256':sha(OUT)},indent=2))
