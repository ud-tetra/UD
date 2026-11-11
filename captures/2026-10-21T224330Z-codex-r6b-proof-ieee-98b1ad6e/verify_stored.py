#!/usr/bin/env python3
"""Audit immutable replay bytes. All bounds use exact rational arithmetic."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import argparse,hashlib,json,runpy
import numpy as np
C=Path(__file__).parent
SCALE=10**65

def interval(lo,hi):
    assert lo<=hi
    lo=F((lo*SCALE).__floor__(),SCALE); hi=F((hi*SCALE).__ceil__(),SCALE)
    with localcontext() as ctx:
        ctx.prec=65
        ds=[str(Decimal(x.numerator)/Decimal(x.denominator)) for x in (lo,hi)]
    return {'lower':str(lo),'upper':str(hi),'decimal_display':ds}
def endpoints(x):return F(x['lower']),F(x['upper'])
def subtract(x,y):
    a,b=endpoints(x);c,d=endpoints(y);return interval(a-d,b-c)
def asf(x):return F.from_float(float(x))
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main(args):
    assert digest(args.payload)=='fa6f6c4fa3dc9d1c13d0a9d0418cef93d1fd6d03cdfa0370055796164767fd3f'
    settings={'residual_tol':5e-12}
    anchor=json.loads((C/'EXACT_CERTIFICATE.json').read_bytes())
    assert runpy.run_path(str(C/'verify_exact.py'))['run']()==anchor
    z=np.load(args.payload,allow_pickle=False);A=z['full'];assert A.shape==(512,512)
    assert np.array_equal(A,A.T)
    # Check every cross-module entry, rather than assuming graph decomposition survives assembly.
    modules=[list(range(64*j,64*(j+1)))+list(range(256+64*j,256+64*(j+1))) for j in range(4)]
    labels=np.array([(i%256)//64 for i in range(512)])
    assert np.all(A[labels[:,None]!=labels[None,:]]==0)
    eta=F(185,192);delta=1-eta;a,b=eta**4,eta**6;g0=12*a+48*b
    # Constant-depth source negative root, independently bisected rationally.
    v1=delta**2;c1=eta**3*delta**3;r1=4*eta**2+v1
    lo=-c1**2/r1;hi=F(0)
    for _ in range(160):
        mid=(lo+hi)/2
        if mid**2-r1*mid-c1**2>0:lo=mid
        else:hi=mid
    depth1=interval(lo,hi)
    source=[interval(*endpoints(anchor['intervals_exact']['lambda']))]+[depth1]*3
    certificates=[];stored=[]
    for root,ids in enumerate(modules):
        H=[[F(0)]*128 for _ in range(128)];depth=[];parity=[]
        for i in range(64):
            ds=[root,i//16,(i//4)%4,i%4]
            depth.append(next((j+1 for j,d in enumerate(ds) if d),4));parity.append((-1)**sum(ds))
        vs=[delta*(1-eta**h) for h in depth]
        cs=[eta**2*delta*(1-eta**h)*(eta**h-eta**(2*h)) for h in depth]
        for i in range(64):
            H[i][i]+=vs[i];H[i][64+i]=H[64+i][i]=parity[i]*cs[i]
            for j in range(i+1,64):
                off,w=(0,eta**2) if i//4==j//4 else (64,a if i//16==j//16 else b)
                H[off+i][off+i]+=w;H[off+j][off+j]+=w
                H[off+i][off+j]-=w;H[off+j][off+i]-=w
        B=[[asf(A[i,j]) for j in ids] for i in ids];stored.append(B)
        E=max(sum(abs(B[i][j]-H[i][j]) for j in range(128)) for i in range(128))
        # Codimension-one form bound with Theta orthogonal to uniform gives source lambda_2>=vmin/2.
        alpha=min(vs)/2
        assert g0-2*max(cs)**2/min(vs)>alpha>0
        beta=alpha-E;assert beta>0
        l,u=endpoints(source[root]);lam=(l+u)/2
        if root==0:
            ys={h:sum(endpoints(anchor['intervals_exact']['Theta_amplitude_h'+str(h)]),F(0))/2 for h in (2,3,4)}
            y=[ys[h] for h in depth]
        else:y=[F(1)]*64
        x=[-parity[i]*cs[i]*y[i]/(4*eta**2+vs[i]-lam) for i in range(64)]
        vec=x+y;n=sum(q*q for q in vec)
        mv=[sum(B[i][j]*vec[j] for j in range(128)) for i in range(128)]
        mu=sum(vec[i]*mv[i] for i in range(128))/n
        variance=sum((mv[i]-mu*vec[i])**2 for i in range(128))/n
        assert mu<0<beta
        # Temple: second stored eigenvalue >= beta, so lambda1 in [mu-var/(beta-mu),mu].
        fl=interval(mu-variance/(beta-mu),mu)
        assert F(fl['upper'])-F(fl['lower'])<F(1,10**23)
        certificates.append({'module_first_digit':root,'source_ground_interval':source[root],
            'stored_IEEE_ground_interval':fl,'assembly_shift_interval':subtract(fl,source[root]),
            'assembly_max_absolute_row_sum_bound':interval(E,E),
            'source_second_eigenvalue_lower':str(alpha),'stored_second_eigenvalue_lower':str(beta),
            'trial_Rayleigh':interval(mu,mu),'trial_residual_variance':interval(variance,variance),
            'method':'exact rational source trial + exact stored-byte Rayleigh and variance; Weyl and Temple'})
    assert certificates[1]['stored_IEEE_ground_interval']==certificates[2]['stored_IEEE_ground_interval']==certificates[3]['stored_IEEE_ground_interval']
    # Exact sign gauge proves that the three stored depth1 blocks share their spectrum.
    for root in (2,3):
        gauge=[(-1)**(root-1)]*64+[1]*64
        assert all(stored[root][i][j]==gauge[i]*gauge[j]*stored[1][i][j] for i in range(128) for j in range(128))
    stored_norm_inf=max(sum(abs(q) for q in row) for block in stored for row in block)
    # Compare all stored solver returns in the negative low-mode sector.
    rows=[]
    for name in ['coupled','blockwise','probe0','probe1']:
        vals=z[name+'_eigenvalues'];vecs=z[name+'_eigenvectors'];negative=np.flatnonzero(vals<0)
        for k in negative:
            assert len(negative)<=4
            ev=asf(vals[k]);v=vecs[:,k]
            weights=[sum(asf(v[i])**2 for i in ids) for ids in modules]
            root=max(range(4),key=lambda j:weights[j])
            family_weight=weights[0] if root==0 else sum(weights[1:])
            assert family_weight>F(99,100)*sum(weights)
            # Exact residual in its dominant module. Nonzero tails elsewhere remain captured as weight.
            w=[asf(v[i]) for i in modules[root]];norm=sum(q*q for q in w)
            residual_sq=sum((sum(stored[root][i][j]*w[j] for j in range(128))-ev*w[i])**2 for i in range(128))/norm
            bound=certificates[root]['stored_IEEE_ground_interval']
            reported=interval(ev,ev)
            solver=subtract(reported,bound);total=subtract(reported,source[root])
            # Recheck the original residual criterion on all 512 stored coordinates.
            raw_residual_sq=F(0)
            for j,ids in enumerate(modules):
                vv=[asf(v[i]) for i in ids]
                if not any(vv):continue
                raw_residual_sq+=sum((sum(stored[j][i][k]*vv[k] for k in range(128))-ev*vv[i])**2 for i in range(128))
            scaled_residual_sq=raw_residual_sq/max(F(1),stored_norm_inf+abs(ev))**2
            assert scaled_residual_sq<=F(str(settings['residual_tol']))**2
            rows.append({'solver':name,'index':int(k),'dominant_module_first_digit':root,
                         'reported_eigenvalue_exact':str(ev),'reported_decimal':repr(float(vals[k])),
                         'solver_error_interval':solver,'total_source_error_interval':total,
                         'dominant_module_residual_squared_per_norm_exact':str(residual_sq),
                         'full_512_scaled_residual_squared_exact':str(scaled_residual_sq),
                         'original_residual_tolerance_pass_exact':True,
                         'weight_outside_dominant_module_display':float(1-weights[root]/sum(weights))})
    coverage={name:sum(x['solver']==name for x in rows) for name in ['coupled','blockwise','probe0','probe1']}
    assert coverage=={'coupled':4,'blockwise':4,'probe0':0,'probe1':4}
    assert stored_norm_inf==F(28105596915389682213,288230376151711744)
    return {'status':'PASS_EXACT_STORED_MATRIX_AUDIT','stored_norm_inf_exact':str(stored_norm_inf),'model':'clean rational R6b; archived binary64 payload',
            'input_hashes':{'payload':digest(args.payload),'anchor':digest(C/'EXACT_CERTIFICATE.json'),'anchor_verifier':digest(C/'verify_exact.py')},
            'module_certificates':certificates,'solver_returns':rows,'coverage':coverage,
            'interpretation':'source-to-IEEE assembly shift separated from stored-eigenvalue reporting error; old thresholds unchanged',
            'limitations':['Temple intervals enclose true stored-byte eigenvalues, not exact new eigensolver runs',
                           'residuals rechecked on full512 coordinates; no new orthogonality or projector audit',
                           'no eigenvector, channel-weight or empirical physical certification is added']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--payload',default=str(C/'NUMERICAL_PAYLOAD.npz'))
    result=main(p.parse_args());(C/'STORED_MATRIX_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'coverage':result['coverage'],'modules':[
        {'root':x['module_first_digit'],'assembly_shift':x['assembly_shift_interval']['decimal_display'],
         'stored_ground':x['stored_IEEE_ground_interval']['decimal_display']} for x in result['module_certificates']]},indent=2))
