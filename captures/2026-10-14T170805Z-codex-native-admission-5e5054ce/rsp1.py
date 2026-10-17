"""RSP-1: an explicitly prepared finite source-interface candidate, not native UD."""
from dataclasses import dataclass,replace,asdict
from response_contract import bits,transport,readout

ZERO=(0,0,0)
def stock(v):
    if not isinstance(v,(list,tuple)) or len(v)!=3 or any(type(x) is not int or x<0 for x in v):
        raise ValueError('Stock must contain three nonnegative integers.')
    return tuple(v)

@dataclass(frozen=True)
class State:
    T: tuple
    L: tuple
    q: tuple
    r: tuple
    bank: tuple=()
    cursor: int=0
    branch: str='C'

    def __post_init__(self):
        for field in ['T','L','q']:object.__setattr__(self,field,bits(getattr(self,field)))
        object.__setattr__(self,'r',stock(self.r))
        if not isinstance(self.bank,(list,tuple)):raise ValueError('A finite bank queue is required.')
        object.__setattr__(self,'bank',tuple(stock(v) for v in self.bank))
        if type(self.cursor) is not int or not 0<=self.cursor<=len(self.bank):raise ValueError('Invalid bank cursor.')
        if self.branch not in ['C','H']:raise ValueError('Freeze branch C or H.')
        if any(t*l>q or q>t for t,l,q in zip(self.T,self.L,self.q)):raise ValueError('Prior response violates omega≤q≤T.')
        if any(v and not t for row in (self.r,)+self.bank for v,t in zip(row,self.T)):
            raise ValueError('Prepared stock outside fixed integrity domain.')

def available_stock(s):return sum(s.r)+sum(sum(v) for v in s.bank[s.cursor:])
def potential(s):return 4*available_stock(s)+2*sum(s.q)+sum(s.L)+len(s.bank)-s.cursor
def relabel(s,p):
    # Same old→current convention as the source-contract algebra; works for integer stock too.
    def vector(v):
        transport(ZERO,p);out=[0]*3
        for old,current in enumerate(p):out[current]=v[old]
        return tuple(out)
    return State(vector(s.T),vector(s.L),vector(s.q),vector(s.r),tuple(vector(v) for v in s.bank),s.cursor,s.branch)

def transition(s):
    if s.r==ZERO and s.q==ZERO and s.L==ZERO and s.cursor<len(s.bank):
        nxt=replace(s,r=s.bank[s.cursor],cursor=s.cursor+1);kind='RENEWAL_ONLY';L=ZERO;h=ZERO
    else:
        L=tuple(t*int(r>0)*(1-q) for t,r,q in zip(s.T,s.r,s.q))
        omega=tuple(t*l for t,l in zip(s.T,L));I=tuple(t*(1-l) for t,l in zip(s.T,L))
        h=ZERO if s.branch=='C' else tuple(i*q for i,q in zip(I,s.q))
        q=tuple(w+idle for w,idle in zip(omega,h));r=tuple(v-w for v,w in zip(s.r,omega))
        nxt=replace(s,L=L,q=q,r=r);kind='INSPECTION'
    oldomega=tuple(t*l for t,l in zip(s.T,s.L))
    event=readout(tuple(1-v for v in s.q),oldomega,s.T,L,h)
    changed=nxt!=s
    response_tag='BIT_EVENT' if event['gross_pair_toggles'] else 'RESPONSE_NULL'
    if not changed:
        kind='HALT'
        halt='EXHAUSTED_QUIESCENT' if available_stock(s)==0 and s.cursor==len(s.bank) and s.q==ZERO and s.L==ZERO else 'LATCHED_OR_STRANDED'
    else:halt=None
    consumed=sum(s.r)-sum(nxt.r) if kind!='RENEWAL_ONLY' else 0
    assert available_stock(s)-available_stock(nxt)==consumed
    if changed:assert potential(nxt)<potential(s)
    return {'state':nxt,'transition_kind':kind,'response_tag':response_tag,'changed':changed,
      'halt_reason':halt,'consumed_tokens':consumed,'event':event,
      'potential_before':potential(s),'potential_after':potential(nxt)}

def close_duration(s):
    if s.branch!='C':raise ValueError('Exact pulse duration applies to branch C.')
    broken=int(any(l and not t for l,t in zip(s.L,s.T)))
    d0=max(max(2*r+q for r,q in zip(s.r,s.q)),broken)
    return d0+(len(s.bank)-s.cursor)+2*sum(max(v) for v in s.bank[s.cursor:])

def run(initial):
    # The strictly decreasing integer potential bounds the entire prepared episode.
    s=initial;trace=[]
    for attempt in range(potential(initial)+1):
        row=transition(s);out={k:v for k,v in row.items() if k!='state'}
        out.update(attempt=attempt,pre_state=asdict(s),post_state=asdict(row['state']),available_stock_before=available_stock(s),available_stock_after=available_stock(row['state']))
        if not row['changed']:
            return {'program':'RSP-1 v0.1','branch':initial.branch,'trace':trace,'terminal':out,
              'committed_updates':len(trace),'opening_toggles':sum(sum(x['event']['reopen_mask']) for x in trace),
              'closure_toggles':sum(sum(x['event']['close_mask']) for x in trace),
              'initial_stock':available_stock(initial),'remaining_stock':available_stock(s),
              'physical_promotion':0,'scope':'Finite prepared-register candidate. HALT is a model control status, not a physical no-event verdict.'}
        trace.append(out);s=row['state']
    raise AssertionError('Strict potential bound violated.')

if __name__=='__main__':
    import argparse,json
    from pathlib import Path
    p=argparse.ArgumentParser();p.add_argument('state_json');a=p.parse_args()
    print(json.dumps(run(State(**json.loads(Path(a.state_json).read_text()))),indent=2))
