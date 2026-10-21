#!/usr/bin/env python3
"""Fresh stdlib counterexample checks for a submitted review, not an independent review."""
from fractions import Fraction as F
from pathlib import Path
import subprocess,json,hashlib
C=Path(__file__).parent;R=C.parents[1]

def blob(ref,path):return subprocess.check_output(['git','show',ref+':'+path],cwd=R)
def main():
    eta=F(185,192);d=1-eta;a,b=eta**4,eta**6;v=d*d;c=eta**3*d**3
    spectrum=[64*b,16*a+48*b,12*a+48*b]
    assert spectrum==[F(40089475140625,782757789696),F(54483031620625,1043677052928),F(50884642500625,1043677052928)]
    # Enumerate the exact declared Theta address rules. No archived program is run.
    components=[]
    for L in (3,4,5):
        N=4**L;adj=[[] for _ in range(N)]
        for i in range(N):
            for j in range(i+1,N):
                if i//64==j//64 and i//4!=j//4:
                    adj[i].append(j);adj[j].append(i)
        seen=set();sizes=[]
        for i in range(N):
            if i in seen:continue
            seen.add(i);stack=[i];size=0
            while stack:
                q=stack.pop();size+=1
                for k in adj[q]:
                    if k not in seen:seen.add(k);stack.append(k)
            sizes.append(size)
        assert sizes==[64]*(N//64)
        components.append({'L':L,'N':N,'components':len(sizes),'component_size':64})
    # In a depth1 module q=(ones/8,0) is unit, orthogonal to the two-column ground sector.
    parity=[(-1)**(1+i//16+(i//4)%4+i%4) for i in range(64)]
    q=[F(1,8)]*64
    assert sum(x*x for x in q)==1 and sum(q[i]*parity[i]/8 for i in range(64))==0
    # Sibling Laplacian annihilates q; cross energy vanishes because Theta=0.
    rho_rayleigh=sum(v*x*x for x in q)
    assert rho_rayleigh==F(49,36864)<F(1,100)<48
    # Frozen F uses the factor64. The review's displayed formula omits it.
    unscaled=sum(x**4 for x in q)/sum(x*x for x in q)**2
    assert unscaled==F(1,64) and 64*unscaled==1
    # Weighted variance identity for n=(1,3,12), total16.
    n=[1,3,12];x=[F(0),F(1),F(2)];mean=sum(n[i]*x[i] for i in range(3))/sum(n)
    pair=sum(n[i]*n[j]*(x[i]-x[j])**2 for i in range(3) for j in range(i+1,3))
    var=sum(n[i]*(x[i]-mean)**2 for i in range(3))
    assert pair==sum(n)*var and pair!=var/2
    # Positive sigma does not exclude negative eigenvalues: transformed magnitude can be largest.
    sigma=F(1,10);eig=[F(-1),F(10)];transformed=[1/(z-sigma) for z in eig]
    assert abs(transformed[0])>abs(transformed[1])
    ref='524f180d3f903267925d48599add52acb9301d6b';cap='captures/2026-10-21T201221Z-codex-r6b-numerical-replay-2dbd851a/'
    raw=blob(ref,cap+'RESULTS.json');old=json.loads(raw)
    coverage=[{'sigma':p['sigma'],'negative_return_count':sum(m['eigenvalue']<0 for m in p['modes'])} for p in old['probes']]
    assert coverage==[{'sigma':0.00133,'negative_return_count':0},{'sigma':1e-8,'negative_return_count':4}]
    ar='98d084191b2c6471b1e73aae2985abefc8bc80ff';ac='captures/2026-10-21T204744Z-codex-r6b-error-budget-bc7134a9/AUDIT.json'
    auditraw=blob(ar,ac);audit=json.loads(auditraw)
    bounds=[]
    for m in audit['module_certificates']:
        E=F(m['assembly_max_absolute_row_sum_bound']['lower'])
        beta=F(m['stored_second_eigenvalue_lower'])
        assert E>F('4.4e-14') and 0<beta<F(1,100)
        bounds.append({'module':m['module_first_digit'],'row_sum_error_lower':str(E),'actual_certified_second_eigenvalue_lower':str(beta)})
    return {'status':'PASS_OBJECTION_CHECKS','meaning':'Review inaccuracies identified; not a non-constructor review or a retraction of source claims',
            'physical_promotion':0,'review_acceptance':'REVISION_REQUIRED','reviewer_provenance':'UNVERIFIED',
            'source_spectrum_correct':list(map(str,spectrum)),'component_controls':components,
            'complement_Rayleigh_counterexample':str(rho_rayleigh),
            'unscaled_uniform_IPR':str(unscaled),'frozen_uniform_F':'1',
            'weighted_variance_control':{'pair_sum':str(pair),'weighted_variance':str(var),'total_weight':sum(n)},
            'positive_shift_counterexample':{'sigma':str(sigma),'eigenvalues':list(map(str,eig)),'transformed':list(map(str,transformed))},
            'actual_replay_coverage':coverage,'audit_gap_and_error_controls':bounds,
            'input_hashes':{'submitted_review':hashlib.sha256((C/'SUBMITTED_REVIEW.txt').read_bytes()).hexdigest(),
                            'PR352_RESULTS':hashlib.sha256(raw).hexdigest(),'PR358_AUDIT':hashlib.sha256(auditraw).hexdigest()}}
if __name__=='__main__':
    result=main();(C/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
