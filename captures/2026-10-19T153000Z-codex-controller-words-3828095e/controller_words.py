"""Exact rational majorants and an explicit fixed-point command implementation.
No archived program is imported or executed. Sources are JSON/Markdown data only.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import ast,copy,hashlib,json,zipfile
R=Path(__file__).resolve().parent
PARAMS=['mu','nu','g','gamma_chi']
OLD_D='2*gamma_chi**2*(3*Q7*(2*Q7+Q8)-3*Q8*(-Q7-2*Q8))+mu'
NEW_D='mu+6*gamma_chi**2*(Q7**2+Q8**2+(Q7+Q8)**2)'
def load_sources():
    inventory=json.loads((R/'SOURCE_INVENTORY.json').read_text());out={}
    with zipfile.ZipFile(R/'SOURCES.zip') as z:
        if set(z.namelist())!={x['member'] for x in inventory}:raise ValueError('source member coverage')
        for x in inventory:
            b=z.read(x['member'])
            if hashlib.sha256(b).hexdigest()!=x['sha256']:raise ValueError('source hash')
            out[x['member']]=json.loads(b) if x['member'].endswith('.json') else b.decode()
    return out

def up(x):
    x=F(x)
    if x<0:raise ValueError('negative majorant')
    if not x:return F(0)
    e=x.numerator.bit_length()-x.denominator.bit_length();v=F(2**e) if e>=0 else F(1,2**(-e))
    return v*2 if v<x else v

def addi(a,b):return (a[0]+b[0],a[1]+b[1])
def negi(a):return (-a[1],-a[0])
def muli(a,b):
    v=[x*y for x in a for y in b];return min(v),max(v)
def sqi(a):return (F(0) if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2))
def mag(a):return max(abs(a[0]),abs(a[1]))
class Rewrite(ast.NodeTransformer):
    def __init__(self):self.count=0;self.old=ast.dump(ast.parse(OLD_D,mode='eval').body)
    def visit(self,node):
        if ast.dump(node)==self.old:
            self.count+=1;return ast.parse(NEW_D,mode='eval').body
        return super().visit(node)
class Graph:
    def __init__(self):self.nodes=[];self.cache={};self.rewrites=0
    def make(self,op,*args):
        key=(op,*args)
        if key not in self.cache:self.cache[key]=len(self.nodes);self.nodes.append(key)
        return self.cache[key]
    def compile(self,text):
        t=Rewrite();node=t.visit(ast.parse(text,mode='eval').body);self.rewrites+=t.count
        def visit(n):
            if isinstance(n,ast.Constant) and type(n.value) is int:return self.make('const',n.value)
            if isinstance(n,ast.Name):return self.make('input',n.id)
            if isinstance(n,ast.UnaryOp):
                if isinstance(n.op,ast.USub):return self.make('neg',visit(n.operand))
                if isinstance(n.op,ast.UAdd):return visit(n.operand)
            if isinstance(n,ast.BinOp):
                if isinstance(n.op,ast.Pow):
                    if not isinstance(n.right,ast.Constant) or type(n.right.value) is not int or not 0<=n.right.value<=8:raise ValueError('exponent')
                    a=visit(n.left);ex=n.right.value
                    if ex==0:return self.make('const',1)
                    if ex==1:return a
                    if ex==2:return self.make('square',a)
                    out=a
                    for _ in range(ex-1):out=self.make('mul',out,a)
                    return out
                op={ast.Add:'add',ast.Sub:'sub',ast.Mult:'mul',ast.Div:'div'}.get(type(n.op))
                if op:return self.make(op,visit(n.left),visit(n.right))
            raise ValueError('non-arithmetic expression')
        return visit(node)
    def analyze(self,env):
        states=[];denominators=[]
        # Entry = exact interval, certified magnitude, four parameter-derivative bounds, rounding K.
        for i,n in enumerate(self.nodes):
            op=n[0]
            if op in ['input','const']:
                iv=env[n[1]] if op=='input' else (F(n[1]),F(n[1]));grad=[F(op=='input' and n[1]==p) for p in PARAMS]
                states.append((iv,up(mag(iv)),grad,F(1)));continue
            a,ba,ga,ka=states[n[1]]
            if op=='neg':states.append((negi(a),ba,ga,ka));continue
            if op=='square':
                iv=sqi(a);gb=[up(2*ba*x) for x in ga];k=up((2*ba+1)*ka+1)
            else:
                b,bb,gb,kb=states[n[2]]
                if op in ['add','sub']:
                    iv=addi(a,b if op=='add' else negi(b));gb=[up(x+y) for x,y in zip(ga,gb)];k=up(ka+kb+1)
                elif op=='mul':
                    iv=muli(a,b);gb=[up(bb*x+ba*y) for x,y in zip(ga,gb)]
                    k=up(min((ba+1)*kb+bb*ka,ba*kb+(bb+1)*ka)+1)
                elif op=='div':
                    if b[0]<=0<=b[1]:raise ValueError('denominator interval crosses0')
                    d=min(abs(b[0]),abs(b[1]));denominators.append((n[2],d))
                    iv=muli(a,(1/b[1],1/b[0]));gb=[up(x/d+ba*y/d**2) for x,y in zip(ga,gb)]
                    k=up(2*ka/d+2*ba*kb/d**2+1)
                else:raise ValueError(op)
            states.append((iv,up(mag(iv)),gb,k))
        return states,denominators
    def exact(self,inputs):
        vals=[]
        for n in self.nodes:
            op=n[0]
            if op=='const':v=F(n[1])
            elif op=='input':v=F(inputs[n[1]])
            elif op=='neg':v=-vals[n[1]]
            elif op=='square':v=vals[n[1]]**2
            else:
                a,b=vals[n[1]],vals[n[2]]
                if op=='add':v=a+b
                elif op=='sub':v=a-b
                elif op=='mul':v=a*b
                else:v=a/b
            vals.append(v)
        return vals
    def fixed(self,inputs,p,width):
        scale=2**p;limit=2**(width-1);temp_limit=2**(2*width+1);vals=[]
        def rounded(x):return round(x) # Fraction.__round__: nearest integer, ties to even.
        for n in self.nodes:
            op=n[0]
            if op=='const':v=n[1]*scale
            elif op=='input':v=rounded(F(inputs[n[1]])*scale)
            elif op=='neg':v=-vals[n[1]]
            else:
                a=vals[n[1]];b=a if op=='square' else vals[n[2]]
                if op=='add':v=a+b
                elif op=='sub':v=a-b
                elif op in ['mul','square']:
                    temp=a*b
                    if abs(temp)>=temp_limit:raise OverflowError('wide multiplication register')
                    v=rounded(F(temp,scale))
                else:
                    if not b:raise ZeroDivisionError('rounded denominator')
                    temp=a*scale
                    if abs(temp)>=temp_limit:raise OverflowError('wide division register')
                    v=rounded(F(temp,b))
            if not -limit<=v<limit:raise OverflowError('word overflow')
            vals.append(v)
        return [F(x,scale) for x in vals]

def build_graph(src):
    alpha=src['UD_COMPONENT_ADMISSIBILITY_RESULT_v0.1.json']['plant_map']['acceleration']
    nn=src['UD_UNITS_CALIBRATION_RESULT_v0.1.json']['mechanical']['N']
    graph=Graph();outs=[];expressions=[]
    for i in range(9):
        damp=lambda j:'(-('+ '+'.join(f'D{j}_{k}*vd{k}' for k in range(9))+'))'
        force=f'2*{damp(i)}' if i<7 else '+'.join(f'({nn[i-7][j-7]})*{damp(j)}' for j in [7,8])
        expr='('+alpha[i][0]+')+('+force+')';expressions.append(expr);outs.append(graph.compile(expr))
    return graph,outs,expressions

def source_envs(src,domain,fixture):
    full=src['UD_FULL_FEEDBACK_RESULT_v0.1.json']['domains'][domain]
    sampled=src['UD_SAMPLED_FEEDBACK_RESULT_v0.1.json']['domains'][domain]
    raw=src['UD_MISMATCH_TIMING_RESULT_v0.1.json']['domains'][domain]
    sf=sampled['fixtures'][fixture];dcap=F(sampled['held_kappa'])+F(sf['matrix_calibration_error']);vd=F(sampled['held_velocity_majorant'])+F(sf['velocity_measurement_error'])
    assert dcap*vd==F(full['fixtures'][fixture]['damping_raw_force'])
    envs={}
    for arm,constants in full['constants'].items():
        qr=F(constants['Q_radius']);vr=F(constants['velocity_radius']);env={}
        env.update({f'Q{i}':(-qr,qr) for i in range(9)});env.update({f'v{i}':(-vr,vr) for i in range(9)});env.update({f'vd{i}':(-vd,vd) for i in range(9)})
        env.update({f'D{i}_{j}':(-dcap,dcap) for i in range(9) for j in range(9)})
        env.update({p:tuple(map(F,v)) for p,v in zip(PARAMS,raw['arm_majorants'][arm]['extended_parameter_box'])})
        if env['mu'][0]<=0:raise ValueError('nonpositive mass box')
        envs[arm]=env
    return envs

def design(graph,outputs,src):
    records=[]
    for di,domain in enumerate(src['UD_FULL_FEEDBACK_RESULT_v0.1.json']['domains']):
        for fixture,old in domain['fixtures'].items():
            zeta=F(old['complete_command_arithmetic_error']);arms={};maximum_l=F(0)
            for arm,env in source_envs(src,di,fixture).items():
                states,dens=graph.analyze(env)
                lip=max(sum(states[i][2]) for i in outputs);maximum_l=max(maximum_l,lip)
                maxk=max(x[3] for x in states);outk=max(states[i][3] for i in outputs);maxb=max(x[1] for x in states)
                p=4
                def bad(p):
                    delta=F(1,2**(p+1));return maxk*delta>1 or outk*delta>zeta/2 or any(states[i][3]*delta>d/2 for i,d in dens)
                while bad(p):p+=1
                assert p==4 or bad(p-1)
                integer_bits=0
                while 2**integer_bits<=maxb+1:integer_bits+=1
                arms[arm]={'parameter_command_L':str(lip),'max_node_magnitude':str(maxb),'max_node_rounding_K':str(maxk),'command_rounding_K':str(outk),'fractional_bits':p,'signed_word_bits':1+integer_bits+p,'wide_temporary_bits':2*(1+integer_bits+p)+2,'integer_magnitude_bits':integer_bits,'rounding_quantum':str(F(1,2**p)),'command_rounding_bound':str(outk*F(1,2**(p+1))),'denominator_nodes':len(dens),'previous_precision_rejected':True}
            k=4
            while maximum_l*F(1,2**k)>zeta/2:k+=1
            rho=F(1,2**k)
            records.append({'domain':di+1,'damping_class':fixture,'target_command_allowance':str(zeta),'coefficient_sup_error_bound':str(rho),'coefficient_dyadic_exponent':k,'coefficient_command_bound':str(maximum_l*rho),'arms':arms})
    return records

def layout_failures(graph,states,dens,outputs,p,width,zeta):
    if type(p) is not int or type(width) is not int or not 4<=p<=4096 or width<=p:return ['invalid layout']
    delta=F(1,2**(p+1));fail=[]
    if any(x[3]*delta>1 for x in states):fail.append('local_error_bootstrap')
    if any(states[i][3]*delta>d/2 for i,d in dens):fail.append('division_separation')
    if max(states[i][3] for i in outputs)*delta>zeta/2:fail.append('command_rounding_budget')
    if F(2**(width-p-1))<=max(x[1] for x in states)+1:fail.append('register_range')
    return fail

def admitted_command(graph,outputs,env,record,arm,inputs,target_parameters,timing):
    if set(inputs)!=set(env):raise ValueError('input fields')
    x={k:F(v) for k,v in inputs.items()}
    if any(not env[k][0]<=v<=env[k][1] for k,v in x.items()):raise ValueError('logical input outside box')
    rho=F(record['coefficient_sup_error_bound'])
    if set(target_parameters)!=set(PARAMS):raise ValueError('target parameter fields')
    if any(not env[k][0]<=F(target_parameters[k])<=env[k][1] or abs(x[k]-F(target_parameters[k]))>rho for k in PARAMS):raise ValueError('coefficient mismatch or box')
    dcap=env['D0_0'][1]
    if any(sum(abs(x[f'D{i}_{j}']) for j in range(9))>dcap for i in range(9)):raise ValueError('damping row norm')
    now,qs,vs,age=map(F,timing)
    if qs!=vs or not 0<=qs<=now or now-qs>age:raise ValueError('same stamp / causal age')
    # age must equal the held v110 bound, not a caller-chosen enlargement.
    original=load_sources()['UD_FULL_FEEDBACK_RESULT_v0.1.json']['domains'][record['domain']-1]['fixtures'][record['damping_class']]
    if age!=F(original['sample_age']):raise ValueError('unfrozen latency allowance')
    a=record['arms'][arm];states,dens=graph.analyze(env)
    if layout_failures(graph,states,dens,outputs,a['fractional_bits'],a['signed_word_bits'],F(record['target_command_allowance'])):raise ValueError('uncertified word layout')
    vals=graph.fixed(x,a['fractional_bits'],a['signed_word_bits'])
    return [vals[i] for i in outputs]

if __name__=='__main__':
    src=load_sources();g,o,e=build_graph(src);records=design(g,o,src)
    print(json.dumps({'classification':'DERIVED_CONDITIONAL_FIXED_POINT_CERTIFICATE','graph_nodes':len(g.nodes),'positive_denominator_rewrites':g.rewrites,'cases':records,'independent_review':False,'physical_promotion':0},indent=2))
