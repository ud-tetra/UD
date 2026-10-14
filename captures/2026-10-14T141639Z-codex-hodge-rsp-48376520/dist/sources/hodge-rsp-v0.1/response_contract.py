"""Finite response algebra and structural admission; no native or empirical authority."""
from itertools import product
from pathlib import Path
from datetime import datetime
import hashlib,json

def bits(x):
    if not isinstance(x,(list,tuple)) or len(x)!=3 or any(type(v) is not int or v not in (0,1) for v in x):
        raise ValueError('Expected three integer binary coordinates.')
    return tuple(x)

def transport(mask,permutation):
    mask=bits(mask)
    if not isinstance(permutation,(list,tuple)) or len(permutation)!=3 or any(type(v) is not int for v in permutation) or set(permutation)!={0,1,2}:
        raise ValueError('Permutation must list the current address of each old address.')
    out=[0]*3
    for old,current in enumerate(permutation):out[current]=mask[old]
    return tuple(out)

def response_fiber(T,L):
    T,L=bits(T),bits(L);omega=tuple(t*l for t,l in zip(T,L));idle=tuple(t*(1-l) for t,l in zip(T,L))
    result=[]
    for h in product((0,1),repeat=3):
        if all(a<=b for a,b in zip(h,idle)):
            q=tuple(a+b for a,b in zip(omega,h));theta=tuple(1-v for v in q)
            result.append({'h':h,'q':q,'theta':theta,'idle_count':sum(h)})
    return {'T':T,'L':L,'omega':omega,'I':idle,'i':sum(idle),'responses':result}

def readout(theta_old,omega_old,T,L,h,permutation=(0,1,2)):
    theta=transport(theta_old,permutation);omega0=transport(omega_old,permutation);q0=tuple(1-v for v in theta)
    if any(w>q for w,q in zip(omega0,q0)):raise ValueError('Prior viable obligation exceeds prior response.')
    fiber=response_fiber(T,L);h=bits(h)
    matches=[r for r in fiber['responses'] if r['h']==h]
    if not matches:raise ValueError('Idle response lies outside intact-null addresses.')
    out=matches[0];index=sum(omega0)-sum(fiber['omega']);h0=tuple(q-w for q,w in zip(q0,omega0))
    mu=sum(out['theta'])-sum(theta)
    assert mu==index+sum(h0)-sum(h)
    closes=tuple((1-a)*b for a,b in zip(theta,out['theta']));opens=tuple(a*(1-b) for a,b in zip(theta,out['theta']))
    return {'theta_prior_aligned':theta,'omega_prior_aligned':omega0,'h_prior_aligned':h0,
      'theta_output':out['theta'],'q_output':out['q'],'omega_output':fiber['omega'],'h_output':h,
      'viable_index':index,'mu_theta':mu,'closure_capacity_change':-2*mu,
      'close_mask':closes,'reopen_mask':opens,'gross_pair_toggles':sum(closes)+sum(opens),
      'physical_promotion':0,'scope':'Conditional finite readout; supplied receipts are not a native source law.'}

def validate_receipt(packet,artifact_root):
    """Check syntax, binding, chronology and algebra. Does not establish causal truth."""
    failures=[];root=Path(artifact_root).resolve()
    def require(test,msg):
        if not test:failures.append(msg)
    try:
        require(packet['schema_version']=='1.0','Unknown schema version.')
        require(packet['domain']=='three_opposite_pairs','Wrong carrier domain.')
        require(packet['source_class'] in ['synthetic','native_candidate'],'Unknown source class.')
        require(packet['target_exposed'] is False,'Endpoint exposure invalidates pre-event admission.')
        require(packet['null_event_policy'] in ['hold','source_defined'],'Missing event/no-event semantics.')
        require(packet['tie_policy'] in ['hold','source_defined'],'Missing collision/tie semantics.')
        require(packet['time_semantics']=='ordinal_update_index','This contract does not calibrate physical seconds.')
        require(type(packet['update_index']) is int and packet['update_index']>=0,'Invalid ordinal index.')
        times=[datetime.fromisoformat(packet[k].replace('Z','+00:00')) for k in ['input_sealed_at','prediction_frozen_at','endpoint_release_at']]
        require(all(t.tzinfo is not None for t in times),'Custody times require explicit timezones.')
        require(times[0]<=times[1]<times[2],'Freeze must follow input seal and precede endpoint release.')
        # Hashes bind the actual input values to a declared source artifact; they do not authenticate its scientific truth.
        binding=None;construction_count=0
        for artifact in packet['artifacts']:
            p=Path(artifact['path'])
            require(not p.is_absolute() and '..' not in p.parts,'Unsafe artifact path.')
            f=(root/p).resolve();require(f.is_relative_to(root),'Artifact escapes declared root.')
            require(f.is_file(),'Source artifact missing.')
            if not f.is_file() or not f.is_relative_to(root):continue
            require(hashlib.sha256(f.read_bytes()).hexdigest()==artifact['sha256'],'Source artifact hash mismatch.')
            if artifact['role']=='pre_event_construction':
                construction_count+=1;binding=json.loads(f.read_text())
        require(binding is not None,'Pre-event construction artifact absent.')
        require(construction_count==1,'Exactly one pre-event construction artifact is required.')
        keys=['prior_theta','prior_T','prior_L','frame_old_to_current','prospective_T','prospective_L','idle_h','source_class','update_index']
        if binding is not None:
            require(all(binding.get(k)==packet.get(k) for k in keys),'Receipt values do not match source artifact.')
            require(bool(binding.get('construction_rule')),'Construction rule not declared.')
            require(binding.get('uses_endpoint') is False,'Construction artifact declares endpoint-derived input.')
        oldT,oldL,oldTheta=bits(packet['prior_T']),bits(packet['prior_L']),bits(packet['prior_theta'])
        oldOmega=tuple(t*l for t,l in zip(oldT,oldL));oldQ=tuple(1-v for v in oldTheta)
        require(all(w<=q<=t for w,q,t in zip(oldOmega,oldQ,oldT)),'Prior state violates admitted response domain.')
        outcome=readout(oldTheta,oldOmega,packet['prospective_T'],packet['prospective_L'],packet['idle_h'],packet['frame_old_to_current'])
        if packet['source_class']=='native_candidate':
            required=['complete_state','viability_update','idle_response','event_and_null_rule','frame_rule','state_feedback','renewal_rule','collision_ties']
            require(all(packet.get('source_program',{}).get(k) for k in required),'Native source-program declarations incomplete.')
    except (KeyError,TypeError,ValueError,OSError,json.JSONDecodeError) as e:
        failures.append('Invalid/missing receipt field or artifact: '+str(e));outcome=None
    return {'status':'SOURCE_INVALID__NO_SCORE' if failures else ('STRUCTURE_PASS__SYNTHETIC_ONLY' if packet['source_class']=='synthetic' else 'STRUCTURE_PASS__NATIVE_VALIDATION_PENDING__NO_SCORE'),
      'failures':failures,'conditional_readout':None if failures else outcome,'physical_promotion':0,
      'authority_limit':'Hash and timestamp checks bind declared inputs; they do not prove pre-event acquisition, native law correctness, independent custody or empirical eligibility.'}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('receipt');p.add_argument('--artifact-root',required=True);a=p.parse_args()
    r=validate_receipt(json.loads(Path(a.receipt).read_text()),a.artifact_root);print(json.dumps(r,indent=2));raise SystemExit(1 if r['failures'] else 0)
