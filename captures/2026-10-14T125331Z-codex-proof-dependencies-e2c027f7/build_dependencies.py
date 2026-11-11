"""Build a source-bound, scoped dependency register on top of reading edition 0.2.

Does not execute imported code or replace any scientific source status.
"""
from pathlib import Path
import hashlib,json,re,html,zipfile

ROOT=Path(__file__).parent; D=ROOT/'dist'
catalog=json.loads((D/'assets/sources.json').read_text())
source_map={x['id']:x for x in catalog}
nodes=[];edges=[];snapshots={}

def add(id,branch,title,status,objects,conclusion,source,section,needle,deps=(),ledger=()):
    s=source_map[source];content=s['content'];assert needle in content,(id,source,needle)
    if source not in snapshots:
        raw=content.encode();path=f'/sources/dependency-snapshots-v0.3/{source}.txt'
        (D/path.lstrip('/')).parent.mkdir(parents=True,exist_ok=True)
        (D/path.lstrip('/')).write_bytes(raw)
        snapshots[source]={'id':source,'title':s['title'],'path':path,'sha256':hashlib.sha256(raw).hexdigest(),
          'representation':'atlas source-text snapshot; portal extracted text is not original package bytes',
          'original_local':s.get('local',''),'original_url':s.get('url',''),'original_sha256':s.get('sha256','')}
    citations=[{'source_id':source,'section':section,'anchor_text':needle,'snapshot_sha256':snapshots[source]['sha256']}]
    nodes.append({'id':id,'branch':branch,'title':title,'status':status,'objects':objects,'conclusion':conclusion,
      'citations':citations,'dependencies':[x[0] for x in deps],'ledger_ids':list(ledger)})
    for parent,kind,reason in deps:
        edges.append({'from':parent,'to':id,'kind':kind,'reason':reason,'citations':citations})

P='polarity';A='action-scale'
proof=lambda id,why:(id,'proof_premise',why)
choice=lambda id,why:(id,'constitutive_assumption',why)
gate=lambda id,why:(id,'evaluation_requirement',why)
add('P-DEF',P,'Typed pair variables','SOURCE_DECLARED','Theta,q,T,L,omega on three pair addresses','q=1−Theta; omega=T AND L. These binary response and viability masks are different objects.','E04','§2','omega')
add('P-ADM',P,'Admissible response domain','SOURCE_DECLARED','Binary masks','omega ≤ q ≤ T coordinatewise; five admissible triples per address.','E04','§2','admissible',[proof('P-DEF','Defines the masks in the inequalities.')])
add('P-IDLE',P,'Idle-response decomposition','EXACT_CONDITIONAL','h=q−omega','h is binary, nonnegative and supported on intact-null addresses; q=omega+h with disjoint support.','C0963','declared_source_variables / exact_response_form','q = omega OR h',[proof('P-ADM','The inequalities make h an admissible residual mask.')])
add('P-RANK',P,'Finite continuation spaces','SOURCE_DECLARED','F: L− → L+','Declare finite spaces with dimensions |omega−| and |omega+|. No causal source is inferred from their dimensions.','C0884','§2','finite-dimensional continuation map')
add('P-INDEX',P,'Rank-nullity index','EXACT_CONDITIONAL','ind Fomega','ind Fomega=|omega−|−|omega+| for any linear map on the declared spaces. The rank cancels.','C0884','§2','Rank-nullity',[proof('P-RANK','Finite domain and codomain dimensions determine the index.')])
add('P-BUDGET',P,'Full Hamming budget','EXACT_CONDITIONAL','muTheta','muTheta=|Theta+|−|Theta−|=|q−|−|q+|. Cardinalities are invariant under pair-frame permutations.','C0957','Theorem','Hamming event budget',[proof('P-DEF','Uses Theta=1−q on both three-seat states.')])
add('P-CORRECT',P,'Idle-corrected identity','EXACT_CONDITIONAL','muTheta,ind Fomega,nu_h','muTheta=ind Fomega+|h−|−|h+|. This is an identity on ordered admissible states, not an endpoint predictor.','C0957','Theorem','residual idle-response index',[proof('P-IDLE','Separates viable and idle counts.'),proof('P-INDEX','Supplies the viable count difference.'),proof('P-BUDGET','Identifies the full response count difference.')])
add('P-EQUAL',P,'Index equals full budget iff idle totals match','EXACT_CONDITIONAL','Equal idle cardinalities','muTheta=ind Fomega iff |h−|=|h+|. Equal idle totals need not mean either mask is zero.','C0957','Theorem / decomposition','mu_\\Theta=\\operatorname{ind}F_\\omega+\\nu_h',[proof('P-CORRECT','The difference equals the idle count difference.')])
add('P-PRIOR',P,'Saturated prior premise','CONSTITUTIVE_PREMISE','h−=000','This is an additional premise for the saturated-prior corollary, not a consequence of rank-nullity.','C0957','Saturated-prior corollary','h^-=0')
add('P-SAT',P,'Saturated-prior corollary','EXACT_CONDITIONAL','muTheta=ind Fomega−|h+|','With h−=0, index-only equality holds iff h+=0. Using that equality to prove no-idle response is circular.','C0957','Saturated-prior corollary','circularity firewall',[proof('P-CORRECT','Starts from the corrected identity.'),choice('P-PRIOR','Sets only the previous idle mask to zero.')])
add('P-NOIDLE',P,'POC-1 no-idle response','CANDIDATE','h+=000; q+=omega+','A candidate constitutive law needing an independent source; it is not proved by demanding index-only equality.','C0963','minimum_missing_object / admissible_reopen_routes','h=000')
add('P-ADDRESS',P,'Binding no-idle address','EXACT_CONDITIONAL','Theta+=1−omega+','If POC-1 binds the response, the final address is fixed. A competing burden minimizer cannot freely choose a different final address.','E04','§3','address-selector',[proof('P-DEF','Relates the response and Theta masks.'),choice('P-NOIDLE','Supplies the no-idle final response law.')])
add('P-BURDEN',P,'Burden and integrity inputs','SOURCE_DECLARED','T,W,k','A supplied burden selector optimizes a target Hamming shell subject to integrity; it must also respect the chosen viability/idle-response contract.','C0884','§5','three-pair address selector')
add('P-SHELL',P,'Conditional shell optimizer','EXACT_CONDITIONAL','argmin on a declared finite shell','An empty admissible shell returns infeasible; a tied optimum holds unresolved symmetry. The historical integrity-only shell is not automatically compatible with binding POC-1.','C0884','§5','HOLD_UNRESOLVED_SYMMETRY',[proof('P-BURDEN','Requires supplied weights, integrity and shell count.')])
add('P-CONFLICT',P,'Two final selectors can conflict','EXACT_NO_GO','T=111,L=100,W=(2,8,10)','POC-1 gives Theta=011 (cost 18); integrity-only k=2 minimization gives 110 (cost 10), violating omega≤q. Adding viability fixes this example.','E04','§3','18',[proof('P-ADM','Defines viability admissibility.'),proof('P-ADDRESS','Supplies the binding no-idle response.'),proof('P-SHELL','Supplies the alternative historical optimization.')])
add('P-FRAME',P,'Frame-alignment receipt','OPEN','Oriented C1 transport; old Theta and omega','A native address prediction requires an independently obtained relative-frame receipt and aligned prior address masks. Count identities alone do not provide this receipt.','E04','§5','frame')
add('P-SOURCE',P,'Native pre-event viability source','OPEN','L−,L+,T from target-hidden pre-state','Finite rank-nullity does not construct independently sourced obligation spaces from native evolution.','C0884','§9','native pre-event mechanism')
add('P-HSOURCE',P,'Independent idle-response source','OPEN','h before endpoint release','Supply typed gate dynamics, an independent silence theorem, an authenticated pre-event receipt or blinded response discrimination. Endpoint-inferred h is forbidden.','C0963','minimum_missing_object','before endpoint release')
add('P-PREDICT',P,'Native address/polarity prediction','OPEN','Declared complete pre-event packet','A predictive model needs independently generated viable and idle response data, the address-frame receipt, and a consistent final selector. Exact endpoint identities do not close these gates.','E04','§§2–5','pre-event',[gate('P-SOURCE','Native viability inputs must precede the endpoint.'),gate('P-HSOURCE','The residual budget requires an independent response law/receipt.'),gate('P-FRAME','Address comparison requires relative-frame alignment.'),proof('P-CORRECT','The full budget must include the idle term.'),proof('P-SHELL','An optimizer used by the model must declare admissibility and tie behavior.')])
add('P-SCORE',P,'Eligible independent score','SOURCE_BLOCKED','Frozen scorer + target-hidden native episode','No new empirical score is issued by this graph. Original scorer custody, source admission and eligible target-hidden episodes remain required.','R35','Object and scope / scoring gate','SOURCE_INCOMPLETE_NO_SCORE',[gate('P-PREDICT','The tested model must supply lawful pre-event outputs.')])
add('P-FLUX',P,'Fixed-K flux witness','SOURCE_DECLARED','s_a=pi/12,s_b=pi/6','Unchanged viable obligation gives zero index/budget; edge support rises by 3/8 (one pair 1/8).','E04','§4','EXACT fixed-K counterexample')
add('P-FLUX-NOGO',P,'Universal flux-index equality fails','EXACT_NO_GO','signed support diagnostic versus integer index','The witness disproves universal equality on this admitted domain. A diagnostic under a new restricted contract remains a separate possibility.','E04','§4','counterexample',[proof('P-FLUX','Nonzero signed flux coexists with zero index.')])
add('A-UNIT',A,'Typed action unit','SOURCE_DECLARED','B0 masslike; a0 length; tau0 time','A0=B0 a0²/tau0 has action dimensions. This definition supplies no measured value.','E11','§2','B_0')
add('A-METRIC',A,'Unit chain metric and active sector','SOURCE_DECLARED','Filled K4, Euclidean norm, P2','Fix the declared unit metric and active nonharmonic sector. Changing this carrier or metric requires rederiving its generator and action geometry.','C0579','Theorem / source anchors','Euclidean chain norm')
add('A-CARRIER',A,'Single-cell spectral identity','SOURCE_DECLARED','A^T=−A; A²=−4P2','The active frequency is 2 in native parameter s; the harmonic component is static. This source-supplied finite identity is not independently reproofed here.','C0906','§1','Exact carrier',[proof('A-METRIC','The carrier and norm fix the declared spectral identity.')])
add('A-J',A,'Active complex structure','EXACT_CONDITIONAL','J=A/2; J²=−I','The active restriction is an orthogonal complex structure; the induced symplectic convention is fixed by this norm.','C0579','Theorem','orthogonal complex structure',[proof('A-CARRIER','Skewness and A²=−4I imply J²=−I and orthogonality.')])
add('A-PHASE',A,'Lifted phase history','SOURCE_DECLARED','a=||x||²; Delta phi tilde','Retain winding in lifted phase, with phase rate 2 in native parameter. Endpoint phase modulo 2pi discards this history.','C0906','§§1,3','Endpoint phase alone')
add('A-ACTION',A,'Single-sector lifted action','EXACT_CONDITIONAL','I_Hodge=(a/2) Delta phi tilde','With the declared symplectic normalization, accumulated native action is S=A0(a/2)Delta phi tilde. It varies continuously with support a.','C0906','§1','lifted Hodge action',[proof('A-J','Provides the source symplectic normalization.'),proof('A-PHASE','Provides support and accumulated phase.'),proof('A-UNIT','Dimensionalizes the internal action.')],['O09'])
add('A-SCALE',A,'Specific action-phase scale','EXACT_CONDITIONAL','S/(a Delta phi tilde)=A0/2','For a>0 and nonzero lifted phase, the ratio is independent of amplitude. It is not yet physical hbar.','C0906','§2','amplitude-independent',[proof('A-ACTION','Cancel the nonzero support and lifted phase.')])
add('A-NORM',A,'Normalized representative','CONVENTION','a=1 on an explicitly normalized ray','Normalizing a representative does not prove native support quantization or physical quantum identity.','C0906','§5','normalized representative')
add('A-REC',A,'Normalized recurrence action','EXACT_CONDITIONAL','Delta phi tilde=2pi; S=pi A0','One single-cell recurrence has native interval pi; its normalized circulation is pi A0. This is not a universal glued-carrier recurrence.','C0906','§§3,5','One recurrence',[proof('A-ACTION','Integrates the lifted phase over the recurrence.'),choice('A-NORM','Uses the normalized representative.'),proof('A-CARRIER','Fixes native frequency 2 and recurrence pi.')])
add('A-END',A,'Endpoint versus history comparison','SOURCE_DECLARED','Same endpoint: zero winding and one winding','Admit both a zero-duration history and a nonzero full-cycle active orbit at the same endpoint with a>0.','C0906','§3','2\\pi n\\equiv0')
add('A-END-NOGO',A,'Endpoint-only accumulated action no-go','EXACT_NO_GO','Endpoint defect delta(U) versus lifted action','Zero winding has action 0; one full active winding has pi a A0 at the same endpoint. An endpoint-only scalar cannot encode both.','C0906','§3','generally nonzero',[proof('A-END','The domain contains histories sharing the endpoint.'),proof('A-ACTION','Their accumulated actions differ.')],['G05','O09'])
add('A-G05',A,'Universal scalar alias retired','RETIRED','kappa_loop^master','The ledger retires a universal scalar alias. A restricted alias needs a new sufficiency/proportionality and carrier-stability certificate.','L65','G05','RETIRED FROM MAINLINE AS UNIVERSAL SCALAR',ledger=['G05'])
add('A-ALG',A,'Conditional scalar-family algebra','PRESERVED_CONDITIONAL','Supplied scalar on a declared operator family','Retiring a universal native alias does not invalidate algebra conditional on a supplied scalar. No specific scalar-family operator is reproofed in this graph.','REC02','ARA01','Conditional scalar-family algebra survives')
add('A-CERT',A,'Restricted scalar sufficiency certificate','OPEN','Sufficient history compression; stable proportionality','A declared compression must retain O09 history and have carrier-stable proportionality before any restricted native scalar identification.','L65','G05 next_gate','sufficient for O09',ledger=['G05','O09'])
add('A-ALIAS',A,'Restricted native scalar identification','OPEN','Declared restricted domain only','This conditional reopening route needs both valid scalar-family algebra and the separate sufficiency certificate. It does not revive the universal alias.','L65','G05','restricted scalar aliases',[proof('A-ALG','Keeps any supplied scalar-family calculation conditional.'),gate('A-CERT','Native identification requires independent sufficiency/proportionality.')],['G05'])
add('A-ETA',A,'Unambiguous current ratio','SOURCE_DECLARED','eta_A=A0/hbar','Current ratio direction is A0/hbar. Historical bare xi_hbar used reciprocal conventions and must remain typed.','L65','G06','current canonical ratio is eta_A=A0/hbar',[proof('A-UNIT','Declares the native dimensional numerator.')],['G06'])
add('A-QPB',A,'QPB-1 physical correspondence candidate','CANDIDATE','Physical hbar=A0/2; eta_A=2','Identifying the specific native action-phase scale with physical hbar is a candidate correspondence, not a theorem from internal geometry.','C0883','Frozen prediction','Frozen prediction',[proof('A-SCALE','The exact internal ratio motivates, but does not prove, the correspondence.'),proof('A-ETA','Fixes the ratio convention.')])
add('A-ANCHOR',A,'Independent physical A0 anchor','OPEN','Physical A0, source-derived uncertainty','Freeze an independently constructed action anchor excluding hbar, h, Planck units, known action targets and fitting to 2. No such data is supplied here.','C0883','Lawful future test','independently constructed physical')
add('A-QPB-TEST',A,'Prospective QPB-1 comparison','OPEN','eta_obs=A0_indep/hbar','Only after freezing the independent anchor compare with 2 under source-derived uncertainty; PASS, FAIL, indeterminate and invalid-source are distinct verdicts.','C0883','Verdicts','QPB1_FAIL',[choice('A-QPB','Freezes the candidate prediction before comparison.'),gate('A-ANCHOR','The independent physical numerator is required.')])
add('A-SPEED',A,'Speed/action identities','EXACT_CONDITIONAL','c_speed=a0/tau0; A0=B0 c_speed² tau0','Even fixed A0 and c_speed determine B0 tau0, not B0 and tau0 separately.','E11','§2','c',[proof('A-UNIT','Substitute a0=c_speed tau0 into the action unit.')])
add('A-GAUGE',A,'Physical clock scale gauge','EXACT_CONDITIONAL','lambda>0','(a0,tau0,B0)→(lambda a0,lambda tau0,B0/lambda) fixes speed and action, while physical frequency scales as 1/lambda and G_SI as lambda².','E11','§§3–4','Scale-gauge theorem',[proof('A-SPEED','Defines the invariants of the transformation.')])
add('A-ANCHOR-NOGO',A,'Action anchor alone cannot set seconds','EXACT_NO_GO','A0 invariant under lambda','An independent action anchor can test eta_A but is invariant under the residual clock gauge. It cannot alone identify absolute tau0. This is an explicit algebraic consequence of E11.','E11','§§3,9','What can break the scale gauge?',[proof('A-GAUGE','The gauge leaves A0 unchanged for every lambda.')])
add('A-CLOCK-ANCHOR',A,'Independent scale-sensitive anchor','OPEN','Identified mass, length or time observable','Supply a lawful physical observable that changes under lambda, an independently identified carrier and a unique map to native units. Merely supplying A0 or a dimensionless ratio is insufficient.','E11','§9','What can break the scale gauge?')
add('A-CLOCK',A,'Absolute physical clock','OPEN','tau0 in seconds','Absolute seconds require a source-complete, scale-sensitive physical correspondence. Native period pi or event coordinate 3/4 is not that anchor.','E11','§§5,8–9','Strongest lawful clock bridge',[gate('A-CLOCK-ANCHOR','A gauge-breaking measurement and correspondence is necessary.'),proof('A-GAUGE','The current unit identities otherwise admit a free positive lambda.')])
add('G-HISTORY',A,'Same local canonical history','CONSTITUTIVE_PREMISE','Genesis and Hodge active local plane','Assume the typed GH-1 balanced coordinate map represents the same local canonical history. c_bridge is a coordinate normalization, distinct from c_speed.','E13','§§4–5','same local canonical history')
add('G-STATIONARY',A,'Stationary Genesis local carrier','CONSTITUTIVE_PREMISE','omega_G constant locally','Use a locally stationary harmonic Genesis mode and its declared historical action/time units hbar_d,tau_d; neither is identified with physical hbar or seconds.','E13','§§1–3','locally stationary Genesis')
add('G-EVENT',A,'GH-2 active event geometry','SOURCE_DECLARED','delta_H²=(3/4)c_bridge² Delta a_G²','The active event length is a typed source object, not an independently fixed physical length.','E13','§6','exact GH-2 event geometry')
add('G-LOCAL',A,'Conditional Genesis–Hodge ratios','EXACT_CONDITIONAL','A0/hbar_d=3omega_G/(4delta_H²); tau0/tau_d=2/omega_G','The product is 3/(2delta_H²). Local harmonic action areas and recurrence periods match under the same-history canonical intertwiner. No absolute units follow.','E13','§§5–11','Conditional canonical identity theorem',[choice('G-HISTORY','Requires equality of local canonical histories.'),choice('G-STATIONARY','Requires the stationary harmonic symplectic form and frequency.'),proof('G-EVENT','Eliminates the balanced coordinate normalization.'),proof('A-J','Supplies the Hodge local canonical plane.'),proof('A-UNIT','Supplies the native dimensional action scale.')])
add('G-VARY',A,'Nonstationary history domain','DOMAIN_PREMISE','omega_G(t) assumes unequal values','The no-go is conditional on a history with varying local frequency; it does not assert every Genesis history is nonstationary.','E13','§12','omega_G(t)')
add('G-CONST',A,'Constant unit-ratio requirement','DOMAIN_PREMISE','One constant tau0/tau_d across the whole history','A proposed global identification uses one constant ratio rather than a newly supplied varying clock law.','E13','§12','single constant ratio')
add('G-GLOBAL-NOGO',A,'Nonstationary global clock no-go','EXACT_NO_GO','omega_G(t) varying; constant unit ratio','One constant tau0/tau_d cannot equal 2/omega_G(t) at all times if the historical frequency varies. A new stationary/effective-clock theorem would be needed.','E13','§12','single constant ratio',[proof('G-VARY','Requires at least two distinct local frequencies.'),choice('G-CONST','Requires one unchanged ratio over the history.')])

scenarios=[
 {'id':'idle-law','title':'Withdraw binding POC-1','changes':['P-NOIDLE'],'must_affect':['P-ADDRESS','P-CONFLICT'],'must_preserve':['P-CORRECT','P-EQUAL','P-INDEX','P-SAT'],'note':'The saturated-prior conditional theorem survives with its stated h−=0 premise. The binding final-address application needs rederivation.'},
 {'id':'prior','title':'Remove the saturated prior premise','changes':['P-PRIOR'],'must_affect':['P-SAT'],'must_preserve':['P-CORRECT','P-EQUAL','P-INDEX']},
 {'id':'frame','title':'Change the address-frame receipt','changes':['P-FRAME'],'must_affect':['P-PREDICT','P-SCORE'],'must_preserve':['P-BUDGET','P-CORRECT','P-INDEX'],'note':'Permutation-invariant cardinality identities survive; address predictions require rechecking.'},
 {'id':'g05','title':'Revisit the retired universal scalar','changes':['A-G05'],'must_affect':[],'must_preserve':['A-ALG','A-ACTION','A-ALIAS'],'note':'No proof edge from a retired universal alias to conditional supplied-scalar algebra is licensed.'},
 {'id':'metric','title':'Change the single-cell chain metric','changes':['A-METRIC'],'must_affect':['A-CARRIER','A-ACTION','A-SCALE','A-REC','G-LOCAL'],'must_preserve':['A-GAUGE','P-CORRECT']},
 {'id':'action-anchor','title':'Withdraw the independent A0 anchor','changes':['A-ANCHOR'],'must_affect':['A-QPB-TEST'],'must_preserve':['A-ACTION','A-SCALE','A-GAUGE','A-CLOCK'],'note':'An action anchor is not a clock anchor. The clock remains open under its separate scale-sensitive gate.'},
 {'id':'clock-anchor','title':'Withdraw the scale-sensitive clock anchor','changes':['A-CLOCK-ANCHOR'],'must_affect':['A-CLOCK'],'must_preserve':['A-QPB-TEST','A-GAUGE','A-SCALE']},
 {'id':'same-history','title':'Withdraw same-history identification','changes':['G-HISTORY'],'must_affect':['G-LOCAL'],'must_preserve':['A-ACTION','A-GAUGE','G-GLOBAL-NOGO']}
]
excluded=[
 {'from':'P-INDEX','to':'P-NOIDLE','reason':'Index-only equality cannot independently prove no-idle response; the idle correction must be sourced.'},
 {'from':'P-INDEX','to':'P-SOURCE','reason':'Rank-nullity does not generate target-hidden obligation spaces.'},
 {'from':'P-FLUX','to':'P-PREDICT','reason':'Signed support is a diagnostic; universal flux-index equality has a counterexample.'},
 {'from':'A-G05','to':'A-ALG','reason':'Retiring a universal native alias does not retract supplied-scalar conditional algebra.'},
 {'from':'A-SCALE','to':'A-ETA','reason':'An exact internal factor 1/2 does not supply a measured physical action correspondence.'},
 {'from':'A-ANCHOR','to':'A-CLOCK','reason':'A0 is invariant under lambda. A separate scale-sensitive anchor is needed.'},
 {'from':'G-LOCAL','to':'A-CLOCK','reason':'A local ratio of historically typed units gives no absolute seconds.'},
 {'from':'A-REC','to':'A-NORM','reason':'A normalized recurrence does not prove support quantization.'}
]
graph={'edition':'0.3','date':'2026-10-14','status':'SCOPED_DEPENDENCY_REGISTER_COMPLETE__GLOBAL_PROOF_DAG_OPEN',
 'physical_promotion':0,'review':'Constructor source audit; independent human proof review pending',
 'scope':'Explicit premises and evaluation gates for the displayed polarity and single-cell action/clock targets. Completeness is by target declaration, not the full 448-row research ledger.',
 'propagation_policy':'Hypothetical premise-change drill. Descendants are PENDING_REDERIVATION for reuse; stored scientific statuses are unchanged. Conditional theorem statements retain their explicitly declared premises.',
 'source_baseline_site_commit':'72b74c201d5b86794a0569442a4990f3f3f1768e',
 'repository_freshness_commit':'4b9c1f7ba03f76324b792f389517161d2bc47e05',
 'nodes':nodes,'edges':edges,'sources':list(snapshots.values()),'scenarios':scenarios,'excluded_inferences':excluded,
 'target_closure':[{'target':n['id'],'direct_premises':n['dependencies'],'completeness':'Declared finite target only; external source identities remain source premises.'} for n in nodes if n['status'] in ['EXACT_CONDITIONAL','EXACT_NO_GO']]}
outfile=D/'assets/dependencies-v0.3.json';outfile.write_text(json.dumps(graph,indent=2,ensure_ascii=False)+'\n')

report='''# UD scoped proof-dependency register v0.3

14 October 2026 UTC. Presentation / source audit. Physical promotion: 0.

The new public dependency explorer binds every displayed object and dependency edge to a source-text snapshot, section locator and SHA-256. Proof premises, constitutive assumptions and evaluation requirements are distinct edge types. Excluded inferences are recorded separately and never propagated as proof edges.

The register is complete for its explicitly declared finite targets, not the full 448-row UD research DAG. Imported spectral identities remain source premises; no assertion of independent source reproof is made. Source status, ledger bytes and prior reconciliation records remain unchanged. The general O09 multimode action formula is retained in the ledger, but this new proof expansion audits the source-complete single-cell active-sector specialization. Glued-carrier and open-system action extensions remain open.

## Polarity boundary

The exact full budget is muTheta = ind Fomega + |h−| − |h+|. Index-only equality requires equal idle totals, not universal saturation. With a saturated prior it holds iff the new response is saturated. This cannot independently prove POC-1. If POC-1 binds the final response, a competing shell-only burden optimizer cannot select a different final address. Native target-hidden viability and idle-response sources, frame receipt and eligible empirical scorer custody remain open.

## Action and clock boundary

The declared unit-metric active K4 carrier yields S=A0(a/2)Delta phi tilde and the exact specific scale A0/2. One normalized recurrence has action pi A0; normalization is not physical support quantization. Same endpoints at zero and one winding have different accumulated actions, ruling out an endpoint-only scalar on that history domain. The retired universal G05 alias has no proof edge to valid supplied-scalar conditional algebra.

QPB-1 eta_A=2 remains a candidate physical correspondence, requiring an independently frozen physical A0 anchor. The E11 scale gauge leaves both speed and A0 fixed while changing tau0. Thus an action anchor alone cannot set absolute seconds: a separately identified lambda-sensitive physical observable is necessary. The local Genesis–Hodge ratios remain conditional on a stationary same-history canonical intertwiner and give no absolute units.

## Change propagation

The explorer runs a hypothetical change audit. It marks reachable uses PENDING_REDERIVATION and distinguishes first-edge reasons. It never modifies the scientific ledger or constitutes a real promotion/demotion receipt. The eight supplied scenarios check both affected and preserved conclusions. Removing frame alignment flags address prediction, while permutation-invariant count identities survive. Removing a physical anchor does not retract internal geometry.

## Source freshness and recovery

The GitHub main snapshot is 4b9c1f7ba03f76324b792f389517161d2bc47e05, including the newer July residue recovery. That result retains missing original Base44 custody and supplies only conditional reconstructed/exchange models; it does not fill the native event-source or absolute-scale gates above. Earlier captures and presentation versions are preserved. Portal snapshots in this release are normalized extracted source text, not recovered original package bytes. Gap2_FINAL_Finite_Genesis.png remains unavailable. Existing substantive former-placeholder guides remain reading crosswalks, not fabricated recovered derivations.

## Verification and remaining review

Fresh verification checks source hashes/locators, DAG acyclicity, exact target premise declarations, excluded-edge absence, all change scenarios, exhaustive 15,625 admissible polarity pairs, selector/flux boundary witnesses, rational scale-gauge identities and Genesis ratio/product identities. These are constructor checks; independent human review remains pending. Static page/link and JavaScript syntax checks accompany publication; browser rendering QA is unavailable in this runtime.

Next recommended work: independently review the scoped graph, then supply a versioned pre-event idle-response/viability source contract. Priority: high; it attacks the upstream prediction gate rather than adding more endpoint identities.
'''
rp='/sources/UD_SCOPED_PROOF_DEPENDENCIES_v0.3.md';(D/rp.lstrip('/')).write_text(report)
entry={'id':'DEP03','title':'Scoped polarity and action proof dependencies v0.3','group':'Reconciliation evidence','status':'SCOPED REGISTER / GLOBAL DAG OPEN','note':graph['scope'],'url':'/dependencies/','local':rp,'sha256':hashlib.sha256(report.encode()).hexdigest(),'size_bytes':len(report.encode()),'content':report}
catalog=[x for x in catalog if x['id']!='DEP03']+[entry];(D/'assets/sources.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2))

base=(D/'reconciliation/index.html').read_text();body='''<div class="page-intro"><div class="eyebrow">Source-bound dependencies · reading edition 0.3</div><h1>What depends on what?</h1><p class="lede">Trace a polarity or action claim to its premises. Change an assumption to see which uses need rederivation.</p></div>
<aside class="callout"><strong>Scoped completeness, open physical correspondence</strong><p>This register enumerates the displayed finite targets. The full research proof DAG and independent human review remain open. Imported spectral identities are source premises. Physical promotion: 0.</p></aside>
<div class="inventory-banner"><div><b>'''+str(len(nodes))+'''</b><span>typed objects and gates</span></div><div><b>'''+str(len(edges))+'''</b><span>explicit dependencies</span></div><div><b>8</b><span>change scenarios</span></div></div>
<div class="search-tools"><label>Research branch<select id="dependency-branch"><option value="polarity">Polarity and response</option><option value="action-scale">Action scale and clocks</option></select></label><label>Claim or premise<select id="dependency-node"></select></label></div>
<div id="dependency-message" class="muted" role="status">Loading the source-bound graph…</div><div id="dependency-detail"></div><section class="chapter"><div class="chapter-label">02</div><div><h2>Change a premise</h2><p>Run a hypothetical reuse audit. This leaves stored research statuses unchanged. Conditional theorem statements keep their declared premises.</p><label class="dependency-label">Saved change scenario<select id="dependency-scenario"></select></label><button class="button secondary" id="dependency-audit">Audit selected object instead</button><div id="dependency-impact" aria-live="polite"></div></div></section>
<section class="chapter"><div class="chapter-label">03</div><div><h2>Inference boundaries</h2><p>These tempting shortcuts are excluded from the proof graph.</p><div id="dependency-exclusions"></div></div></section>
<noscript><p>The interactive explorer requires JavaScript. The complete graph and readable report are available below.</p></noscript><div class="actions"><a class="button" href="/releases/UD_SCOPED_DEPENDENCIES_v0.3.zip" download>Download verified release ↓</a><a class="text-link" href="/sources/UD_SCOPED_PROOF_DEPENDENCIES_v0.3.md">Read audit report</a><a class="text-link" href="/assets/dependencies-v0.3.json">Full graph JSON</a><a class="text-link" href="/sources/UD_DEPENDENCY_VERIFICATION_v0.3.json">Verification receipt</a></div>'''
page=re.sub(r'<main id="main">.*?</main>','<main id="main">'+body+'</main>',base,flags=re.S).replace('Reconciliation · Unified Dynamics','Dependencies · Unified Dynamics').replace('data-page="reconciliation"','data-page="dependencies"').replace(' aria-current="page"','')
page=page.replace('</head>','<script src="/assets/dependencies-v0.3.js" defer></script></head>')
(D/'dependencies').mkdir(exist_ok=True);(D/'dependencies/index.html').write_text(page)
nav='<a href="/dependencies/"'+('')+'><span>12</span>Dependencies</a>'
for p in D.rglob('*.html'):
    t=p.read_text().replace('Public reading edition 0.2','Public reading edition 0.3')
    if 'href="/dependencies/"' not in t.split('</nav>')[0]:t=t.replace('</nav>',nav+'</nav>')
    if p.parent.name=='dependencies':t=t.replace('href="/dependencies/">','href="/dependencies/" aria-current="page">')
    if p.parent.name=='reconciliation':t=t.replace('The full proof DAG and independent reproof remain OPEN_GATED.','<a href="/dependencies/">Scoped polarity/action dependencies are now explicit.</a> The full proof DAG and independent reproof remain OPEN_GATED.')
    p.write_text(t)
up=D/'updates/index.html';t=up.read_text()
if 'dependency-update-v03' not in t:
    article='<article class="claim" id="dependency-update-v03"><div class="eyebrow">14 October 2026 · Reading edition 0.3</div><h2>Polarity and action dependencies</h2><p>Source-bound premises, constitutive choices and evaluation gates now have an explicit scoped graph. Eight change scenarios identify affected uses while retaining conditional mathematics. Absolute clock and native event-source gates remain open.</p><a class="text-link" href="/dependencies/">Explore the dependencies →</a></article>'
    t=t.replace('</div><section', '</div>'+article+'<section',1) if '</div><section' in t else t.replace('</main>',article+'</main>')
    up.write_text(t)
print(json.dumps({'nodes':len(nodes),'edges':len(edges),'snapshots':len(snapshots),'target_declarations':len(graph['target_closure'])}))

cov=json.loads((D/'assets/coverage.json').read_text());cov['edition']='0.3';cov['source_registry_entries']=len(catalog);cov['scoped_dependency_register']={'edition':'0.3','nodes':len(nodes),'edges':len(edges),'source_snapshots':len(snapshots),'target_declarations':len(graph['target_closure']),'full_research_DAG':'OPEN_GATED','source_baseline_site_commit':graph['source_baseline_site_commit'],'freshness_repository_commit':graph['repository_freshness_commit']};(D/'assets/coverage.json').write_text(json.dumps(cov,indent=2)+'\n')
