"""Finite prepared reversible carrier. Label arithmetic is a coding choice, not native UD."""
from dataclasses import dataclass, asdict
from rsp1 import State, transition, potential, available_stock

@dataclass(frozen=True)
class Payload:
    w: int
    h: tuple
    records: tuple

@dataclass(frozen=True)
class Joint:
    clock: int
    active: Payload
    donors: tuple

class Carrier:
    def __init__(self, successor, receipt, record_dimension, ticks, resets):
        self.f=tuple(successor);self.rho=tuple(receipt);self.d=len(self.f)
        self.m=record_dimension;self.N=ticks;self.B=resets
        if any(type(x) is not int for x in (self.m,self.N,self.B)) or self.d<1 or self.m<1 or self.N<1 or self.B<0:
            raise ValueError('Positive label/record dimensions and window; nonnegative resets required.')
        if len(self.rho)!=self.d or any(type(x) is not int or not 0<=x<self.d for x in self.f) or any(type(x) is not int or not 0<=x<self.m for x in self.rho):
            raise ValueError('Total finite successor and receipt maps required.')
        self.L=(self.B+1)*(self.N+1)

    def blank(self, w=0):return Payload(w,(0,)*self.N,(0,)*self.N)
    def prepared(self):return Joint(0,self.blank(),(self.blank(),)*self.B)

    def validate(self,x):
        if type(x.clock) is not int or not 0<=x.clock<self.L or len(x.donors)!=self.B:raise ValueError('Invalid joint clock/bank.')
        for p in (x.active,)+x.donors:
            if type(p.w) is not int or not 0<=p.w<self.d or len(p.h)!=self.N or len(p.records)!=self.N:raise ValueError('Invalid payload.')
            if any(type(v) is not int or not 0<=v<self.d for v in p.h) or any(type(v) is not int or not 0<=v<self.m for v in p.records):raise ValueError('Invalid memory/record label.')

    def gate(self,p,i,inverse=False):
        h=list(p.h);r=list(p.records)
        if inverse:
            w=h[i];h[i]=(p.w-self.f[w])%self.d;r[i]=(r[i]-self.rho[w])%self.m
        else:
            w=(h[i]+self.f[p.w])%self.d;h[i]=p.w;r[i]=(r[i]+self.rho[p.w])%self.m
        return Payload(w,tuple(h),tuple(r))

    def step(self,x,inverse=False):
        self.validate(x)
        c=(x.clock-1)%self.L if inverse else x.clock
        j,i=divmod(c,self.N+1);a=x.active;donors=list(x.donors)
        if i<self.N:a=self.gate(a,i,inverse)
        elif j<self.B:a,donors[j]=donors[j],a
        y=Joint(c if inverse else (c+1)%self.L,a,tuple(donors));self.validate(y);return y

    def action(self,c):
        j,i=divmod(c,self.N+1)
        return {'kind':'COMPUTE' if i<self.N else ('RESET_EXPORT' if j<self.B else 'WRAP_IDLE'), 'episode':j,'slot':i if i<self.N else None,'donor':j if i==self.N and j<self.B else None}

    def resources(self):
        p=self.d**(self.N+1)*self.m**self.N
        return {'state_labels':self.d,'record_labels':self.m,'ticks_per_episode':self.N,'reset_blocks':self.B,
          'episodes':self.B+1,'clock_addresses':self.L,'certified_transitions':self.L-1,
          'compute_gates':(self.B+1)*self.N,'payload_swaps':self.B,
          'history_cells_total':(self.B+1)*self.N,'record_cells_total':(self.B+1)*self.N,
          'work_cells_total':self.B+1,'payload_dimension':p,'joint_dimension':self.L*p**(self.B+1),
          'allocated_binary_capacity_bits':(self.L-1).bit_length()+(self.B+1)*((self.N+1)*(self.d-1).bit_length()+self.N*(self.m-1).bit_length()),
          'exported_record_cells_final':self.B*self.N,'active_record_cells_final':self.N,
          'unused_reset_blocks_final':0,'master_clock_reset_by_payload_swap':False,
          'complete_restart_fresh_joint_donor_dimension':self.L*p**(self.B+1),
          'physical_promotion':0,'capacity_scope':'Allocated register capacity, not entropy, joules or an optimal memory lower bound.'}

def compile_rsp(initial):
    """Compile a declared prepared trace into a forward-invariant finite state set."""
    states=[];receipts=[];s=initial
    for _ in range(potential(initial)+1):
        states.append(s);row=transition(s)
        receipts.append({k:v for k,v in row.items() if k!='state'})
        if row['state']==s:break
        s=row['state']
    else:raise AssertionError('RSP bound failed.')
    return {'states':[asdict(s) for s in states], 'successor':list(range(1,len(states)))+[len(states)-1],
      'receipt':list(range(1,len(states)+1)),'record_dimension':len(states)+1,
      'record_dictionary':[{'id':0,'meaning':'BLANK'}]+[{'id':i+1,'pre_state_label':i,'post_state_label':min(i+1,len(states)-1),**r} for i,r in enumerate(receipts)],
      'scope':'Prepared RSP trajectory closure only; source state, integrity, stock, queue and branch are encoded completely. No native selection or source calibration.'}

def witness(branch='C',ticks=4,resets=1):
    spec=compile_rsp(State((1,0,0),(0,0,0),(0,0,0),(1,0,0),branch=branch))
    c=Carrier(spec['successor'],spec['receipt'],spec['record_dimension'],ticks,resets)
    stocks=[available_stock(State(**s)) for s in spec['states']]
    def stock_ledger(x,used):
        return {'active':stocks[x.active.w], 'unspent_donors':sum(stocks[p.w] for p in x.donors[used:]),
          'outgoing_remaining':sum(stocks[p.w] for p in x.donors[:used]),
          'total_work_register_stock':stocks[x.active.w]+sum(stocks[p.w] for p in x.donors),
          'scope':'Encoded RSP token ledger on work registers only; history and receipt copies are nonspendable snapshots, not extra resource.'}
    x=c.prepared();rows=[];used=0
    for k in range(c.L-1):
        old=x;x=c.step(x);j,i=divmod(old.clock,c.N+1)
        expected=0
        if i<c.N:
            for _ in range(i+1):expected=c.f[expected]
        before=stock_ledger(old,used)
        if i==c.N:used+=1
        after=stock_ledger(x,used)
        consumed=spec['record_dictionary'][old.active.w+1]['consumed_tokens'] if i<c.N else 0
        assert before['total_work_register_stock']-after['total_work_register_stock']==consumed
        row={'transition':k+1,'action':c.action(old.clock),'clock_before':old.clock,'clock_after':x.clock,
          'active':asdict(x.active),'donors':list(map(asdict,x.donors)),'expected_work_label':expected,
          'within_declared_window':True,'work_matches':x.active.w==expected,
          'stock_before':before,'stock_after':after,'consumed_tokens':consumed}
        assert row['work_matches'];rows.append(row)
    final=x;post=[]
    for k in range(c.N+1):
        old=x;x=c.step(x);post.append({'action':c.action(old.clock),'clock_after':x.clock,'active':asdict(x.active),'within_declared_window':False})
    return {'branch':branch,'specification':spec,'resources':c.resources(),'initial':asdict(c.prepared()),
      'trace':rows,'initial_stock':stock_ledger(c.prepared(),0),'final_stock':stock_ledger(final,c.B),
      'final':asdict(final),'post_window_negative_control':post,
      'status':'EXACT CONDITIONAL PREPARED WINDOW / CANDIDATE JOINT OPERATOR',
      'independent_human_review':'PENDING','physical_promotion':0}

if __name__=='__main__':
    import json
    from pathlib import Path
    p=Path(__file__).parent/'dist/sources/joint-carrier-v0.1';p.mkdir(parents=True,exist_ok=True)
    (p/'JOINT_CARRIER_WITNESS_v0.1.json').write_text(json.dumps({'version':'0.1','branches':{b:witness(b) for b in ['C','H']}},indent=2)+'\n')
