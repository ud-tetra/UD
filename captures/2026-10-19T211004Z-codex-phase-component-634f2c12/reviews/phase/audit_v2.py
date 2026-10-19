"""Independent finite phase-list audit; no estimator, SVD or new proposals."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import math,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,acb,fmpq,fmpz_mat,ctx
ctx.prec=512
ROOT=Path('/workspace/scratch/f3d1c2f040c9');OUT=Path(__file__).resolve().parent
SOURCE=ROOT/'directional-admission-work-20261019'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
fr=lambda x:F(int(x[0]),int(x[1]));pair=lambda x:[str(x.numerator),str(x.denominator)]
ar=lambda x:arb(fmpq(x.numerator,x.denominator))
def up(x):
    n=(x.upper()*(1<<180)).ceil().unique_fmpz();assert n is not None;return [int(n),1<<180]
def down(x):
    n=(x.lower()*(1<<180)).floor().unique_fmpz();assert n is not None;return [int(n),1<<180]
def enc(x):
    assert x.dtype==np.float64 and np.isfinite(x).all()
    pairs=[float(v).as_integer_ratio() for v in x.flat];b=max(d.bit_length()-1 for n,d in pairs)
    return np.array([n<<(b-(d.bit_length()-1)) for n,d in pairs],dtype=object).reshape(x.shape),b
def cenc(z):
    assert z.dtype==np.complex128 and np.isfinite(z).all();r,br=enc(z.real);i,bi=enc(z.imag);b=max(br,bi)
    return r*(1<<(b-br)),i*(1<<(b-bi)),b
fm=lambda x:fmpz_mat(np.asarray(x,dtype=object).tolist())
ss=lambda m:sum(int(v)**2 for row in m.tolist() for v in row)

def complex_metrics(meta):
    T,ev,V,H=meta['shift'],meta['eigenvalues'],meta['eigenvectors'],meta['inverse']
    assert T.shape==V.shape==H.shape==(209,209) and ev.shape==(209,)
    t,bt=enc(T);vr,vi,bv=cenc(V);hr,hi,bh=cenc(H);lr,li,bl=cenc(ev)
    VR,VI,HR,HI=map(fm,[vr,vi,hr,hi]);I=fmpz_mat(np.eye(209,dtype=object).tolist())
    ir=VR*HR-VI*HI-I*(1<<(bv+bh));ii=VR*HI+VI*HR
    inverse2=F(ss(ir)+ss(ii),1<<(2*(bv+bh)))
    b=max(bt+bv,bv+bl);TM=fm(t)
    er=(TM*VR)*(1<<(b-bt-bv))-fm(vr*lr[None,:]-vi*li[None,:])*(1<<(b-bv-bl))
    ei=(TM*VI)*(1<<(b-bt-bv))-fm(vr*li[None,:]+vi*lr[None,:])*(1<<(b-bv-bl))
    eigen2=F(ss(er)+ss(ei),1<<(2*b))
    # Hermitian Gram row-sum bound independently implemented with integer sums.
    gr=HR.transpose()*HR+HI.transpose()*HI;gi=HR.transpose()*HI-HI.transpose()*HR
    trace=sum(int(gr[j,j]) for j in range(209))
    row=max(sum(abs(int(gr[j,k]))+abs(int(gi[j,k])) for k in range(209)) for j in range(209))
    norm2=F(min(trace,row),1<<(2*bh))
    return inverse2,eigen2,norm2

def audit():
    frozen=load(OUT/'AUDIT_V2_FREEZE.json');assert sha(Path(__file__))==frozen['script_sha256']
    for path,h in frozen['source_files'].items():assert sha(ROOT/path)==h,path
    source=load(ROOT/frozen['source_phase_path']);policy=load(ROOT/frozen['policy_path'])['gates']
    targets=source['target_matches'];assert len(targets)==209
    omega=[ar(fr(t['omega'])) for t in targets];sep=ar(fr(source['metrics']['minimum_target_chord_lower']));assert 0<sep<1
    # New expression: all target separation chords directly from frequency differences.
    chord_lowers=[]
    for i in range(209):
        for j in range(i):
            d=2*abs((omega[i]-omega[j]).sin());assert d>=sep
            chord_lowers.append(d.lower())
    min_chord_lower=down(arb(min(chord_lowers)))
    rows=[]
    for amp in [0,1,2,4]:
        case=SOURCE/'results'/f'directional_amp_{amp}';run=load(case/'RUN.json')
        assert run['case']==f'directional_amp_{amp}' and run['learned_order']==209 and run['execution_status']=='COMPLETED'
        for n in ['PHASE_META.npz','PHASE_PROPOSAL.npz']:assert sha(case/n)==run['numeric_witnesses'][n]
        with np.load(case/'PHASE_META.npz',allow_pickle=False) as z:meta={k:z[k] for k in z.files}
        emission=np.load(case/'PHASE_PROPOSAL.npz',allow_pickle=False)['two_step_phase'];angles=meta['angles'];ev=meta['eigenvalues']
        assert emission.shape==angles.shape==ev.shape==(209,) and emission.dtype==np.int64 and angles.dtype==np.float64
        matched=[];argmax=arb(0);error_max=arb(0);all_ties=True
        for i,n in enumerate(emission):
            an,ad=float(angles[i]).as_integer_ratio();q,r=divmod(an*(1<<60),ad)
            wanted=q+int(2*r>ad or(2*r==ad and q%2));all_ties=all_ties and int(n)==wanted
            th=arb(int(n))/(1<<60);assert abs(th)<arb.pi()+arb(1)/(1<<59)
            # Floating selection is merely a proposal; strict certified half-separation
            # and globally verified target separation establish the unique matching.
            rough=[abs((float(th-2*w)+math.pi)%(2*math.pi)-math.pi) for w in omega]
            j=min(range(209),key=rough.__getitem__)
            err=2*abs(((th-2*omega[j])/2).sin()).asin();assert err<sep/2
            error_max=arb(max(error_max.upper(),err.upper()))
            zr,zi=float(ev[i].real).as_integer_ratio(),float(ev[i].imag).as_integer_ratio()
            zz=acb(ar(F(*zr)),ar(F(*zi)));assert abs(zz)>0
            ae=2*abs(((zz.arg()-th)/2).sin()).asin();argmax=arb(max(argmax.upper(),ae.upper()))
            matched.append({'emitted_index':i,'target_index':j,'target_label':targets[j]['label'],'circular_error_upper':up(err),'source_omega':targets[j]['omega']})
        bijection=len({r['target_index'] for r in matched})==209
        inverse2,eigen2,hnorm2=complex_metrics(meta)
        gates={'ties_even':all_ties,'bijection':bijection,'strict_half_fixed_separation':True,'inverse_residual':inverse2<=fr(policy['inverse_residual'])**2,'proposed_inverse_norm':hnorm2<=fr(policy['proposed_inverse_norm'])**2,'eigenpair_residual':eigen2<=fr(policy['eigenpair_residual'])**2,'emitted_argument_error':bool(argmax<=ar(fr(policy['emitted_argument_error'])))}
        assert all(gates.values()),gates
        rho=ar(inverse2).sqrt();hn=ar(hnorm2).sqrt();assert rho<1
        rows.append({'case':run['case'],'amplitude':amp,'status':'CERTIFIED_FINITE_EMISSION_LIST_AND_SAVED_COMPLEX_DIAGNOSTICS','record_sha256':run['record_sha256'],'phase_meta_sha256':sha(case/'PHASE_META.npz'),'phase_proposal_sha256':sha(case/'PHASE_PROPOSAL.npz'),'gates':gates,'maximum_circular_error_upper':up(error_max),'maximum_argument_error_upper':up(argmax),'exact_inverse_residual_squared':pair(inverse2),'exact_eigenpair_residual_squared':pair(eigen2),'proposed_inverse_norm_bound_squared':pair(hnorm2),'validated_actual_eigenvector_inverse_norm_upper':up(hn/(1-rho)),'matching':matched})
    result={'status':'SAME_TEAM_FOUR_PHASE_LIST_AUDIT_PASS','utc':datetime.now(timezone.utc).isoformat(),'audit_freeze_sha256':sha(OUT/'AUDIT_V2_FREEZE.json'),'source_target_count':209,'target_pairwise_chords_checked':209*208//2,'minimum_target_chord_lower':min_chord_lower,'fixed_source_chord_lower':source['metrics']['minimum_target_chord_lower'],'rows':rows,'emissions_checked':836,'new_estimator_calls':0,'new_SVD_calls':0,'new_alignment_or_inverse_proposals':0,'scope':'Finite dyadic TWO-STEP emitted lists, exact saved complex residuals and inverse diagnostics. Does not identify exact spectrum(T), SI frequencies, unique one-step alias branches, or any uniform noise-ball guarantee. Old frame refusals unchanged.','external_review':'PENDING','physical_promotion':0}
    out=OUT/'AUDIT_V2_RECEIPT.json';assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'receipt_sha256':sha(out),'emissions_checked':836}))

if __name__=='__main__':audit()
