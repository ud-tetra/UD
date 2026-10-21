# UD amplitude, readiness and binary-interface audit v0.1

Date: 2026-10-02 UTC. Development lane. Constructor: Codex. Non-constructor review: none. Physical promotion: 0.

## Result

The inspected UD support laws retain signed face–cell coherence, but they do not yet select a conversion from continuous amplitudes to integer credits, four readiness flags, or committed binary events. The collective four-face update remains a conditional mathematical extension. Conserved support and the binary interface do not uniquely select it or the cubic/BCC geometry.

This audit advances the previous [collective four-face history lift](https://chatgpt.com/space/page_9e041497b47881919ce1e0fc05fb70a7). It does not modify that release or any source ledger, action, registry rung or earlier hash-locked artifact.

## Inspected source boundary

| Source | Relevant statement | What remains open |
|---|---|---|
| Provenance ledger v0.86, Q169–Q170 | Global real skew chain generator on uniquely owned simplices; quadratic support balance across incidence cuts | Recursive ownership and open-system semantics |
| Q171 | Cell stock u²; native derivative 2u sum_f B3(f,t)f_f | Coarse/open-system support |
| Q172 | Face stock f_f²; derivative includes edge–face and face–cell currents | Reservoir elimination requires a controlled approximation |
| Q173 | Gated current 2h_f B3(f,t)f_f u | Explicit next gate: “gate-transition receipt” |
| Glued local clocks and credit reuse v0.4, sections 5–6 | Consumption has a finite budget; an explicitly separate reserve/release branch can repeat commits | Reuse, bank attachment, crossing processing and release are new assumptions |
| State-cone living audit revision0.5, preserving revision0.4 | A harmonic reference and selected quadratic boards can retain two quadratures; stock fractions alone lose predictive coherences | Actual preparation, access and detector semantics remain unadmitted |
| Spacetime manuscript, current version9, around line4391 | Q173 is conditional on a gate and does not specify four-face accumulation/reset | Gate-transition law |
| Time-source dossier v0.12 and migration audit v0.1 | Readiness and retention motivation do not supply the selected event mechanism | No silent promotion of a historical branch |

Q169–Q173 were checked directly in the retrieved v0.86 ledger, rather than attributed solely to the historical v0.39 baseline. This is a bounded source audit, not a claim to have searched every possible UD document.

Source identities:

- Ledger: libfile_fe0eb09831148191a4879de0ab2b7295, current version0; file title UD_COEFFICIENT_PROVENANCE_LEDGER_v0.86_QUIX_CORRELATED_COVARIANCE.json. Q169–Q173 occur in retrieved text lines2751–2810.

- Manuscript: libfile_fc7d5213e3488191a7005e84afd4bec2, current version9.

- Local clocks: libfile_a5a4b2ec718c81918640f4cb8813cf55, current version0.

- State-cone living audit: libfile_b93d9787b18881919e301eefadd669bf, current version0, content revision0.5.

- Time dossier: libfile_54fda59d4c8c819197274218227fbddc, current version0.

- Migration audit: libfile_466ca1dc88b48191b785f1f3e8fb7791, current version0.

## Exact phase-versus-stock discriminator

Use one tetrahedron's oriented boundary column b=(1,−1,1,−1), real face vector f and cell amplitude u. Define g=bᵀf. The previously proposed collective update at epsilon=1/8 is

```text
alpha = 8/65
beta  = 1/130
r     = 63/65
f'    = f − alpha b u − beta b g
u'    = r u + alpha g
```

It preserves the original Euclidean support S=||f||²+u². It is a candidate discrete update, not a ledger-selected event law.

| Quantity | State + | State − |
|---|---:|---:|
| Faces f | 2b | −2b |
| Cell u | 1 | 1 |
| Four face stocks | 4,4,4,4 | 4,4,4,4 |
| Cell stock | 1 | 1 |
| Total support | 17 | 17 |
| Signed contraction g | 8 | −8 |
| Native cell-stock derivative 2ug | 16 | −16 |
| Cell after candidate update | 127/65 | −1/65 |
| Faces after candidate update | (118/65)b | (−134/65)b |
| Four positive-stock flags before and after | 1111 → 1111 | 1111 → 1111 |

Thus identical individual stocks do not determine even the direction of native support transfer. They also do not determine the candidate next cell sign. A proposed binary interface based only on these stocks cannot predict both cases.

This does not exclude all quadratic readouts. The cross products b_f f_f u appearing in Q171/Q173 distinguish the two states. The newer harmonic-reference audit already shows how selected quadratic readouts can retain phase. The excluded proposal is the stock-only projection.

For the isolated collective face–cell update, the two active quadratures are v=g/2 and u:

```text
(v',u') = (r v − 2alpha u, 2alpha v + r u).
```

These determine the next cell amplitude. The full f is still required to retain the transverse face state or evaluate other cells after gluing. A global amplitude sign convention is additionally required if a bit is to mean the absolute sign of u; support currents are invariant under simultaneous global sign reversal.

## Readiness reset discriminator

If readiness is defined statically as R_f=1 when f_f²>0, both states above remain ready on every face after the update. That conflicts with the existing candidate event model's reset to an empty readiness set after a commit.

This excludes the simple positivity mapping, not every possible amplitude-driven gate. A threshold law, a crossing latch, a history register, or an explicitly different amplitude update could change the result. None is supplied merely by the definition of face stock. Q173 explicitly leaves the gate transition open.

Similarly, holding amplitudes fixed between commits and setting readiness only as a function of their current value cannot turn a false readiness predicate true by waiting. An independent continuous flow, preparation update or retained event state is needed for such a trigger.

## Real support does not automatically yield integer credits

There are two separate exact obstructions, each with stated assumptions.

1. Any continuous map from the connected support domain S>0 to the discrete nonnegative integers is constant. A changing integer credit assignment therefore needs a discontinuity, restricted allowed supports, additional state or history.

2. More strongly, let q map every nonnegative real support to a nonnegative integer and suppose q is additive under support combination. For any S, write m=q(S) and choose integer n>m. Additivity gives m=n q(S/n). Since q(S/n) is a nonnegative integer, it must be zero; hence m=0. Therefore the only such everywhere-defined additive map is q=0.

This is not an objection to quantized or nonadditive credits. It identifies the extra rule needed to obtain them from unrestricted real support. No identification of credits with physical energy is made.

If a proposed consumptive credit count depends only on conserved total support, q=q(S), then every norm-preserving collective commit leaves q unchanged. It cannot simultaneously implement q' = q−1. A separate reservoir, changed amplitude law, or independent credit register is required.

For the existing consumptive branch, source bookkeeping remains E≤N_initial+R_injected. Internal redistribution alone does not replenish consumed credits. The separate reusable branch preserves sum(q+r), and can sustain conditional commits, but it expressly introduces reserve/release semantics. It is not selected by support conservation or tetrahedral geometry.

## A binary flip does not select the amplitude operator

At the half-return limit epsilon→infinity, the collective update becomes

```text
R(f,u) = (f − (1/2)b(bᵀf), −u).
```

This is an orthogonal involution and flips every nonzero cell amplitude sign. The different operator V(f,u)=(f,−u) also preserves support and gives the same cell sign flip, while leaving every face unchanged.

Hence even an exact sign-flip interface cannot choose the collective face transport from those constraints alone. These are discriminators, not proposed replacements for the current finite-step propagation law. A chosen native half-return could supply R conditionally; its event convention and interface still need source admission. For ordinary epsilon=1/8, a pure positive cell amplitude remains positive after a step, so the prior finite-step candidate already fails a universal “commit equals sign flip” identification.

## What this adds to the cubic interpretation

The cube/BCC macrocell can organize adjacency and collective propagation once a gluing and update contract is declared. This audit finds no new internal selection of that geometry.

The source gives a more concrete link than a shape analogy: signed incidence currents carry information that stock-only descriptions discard. To connect the macrocell to physical reality, the remaining issue is an admitted operational event/readout mechanism and independently tested physical correspondence. Geometric regularity, internal exactness and resource accounting are insufficient by themselves.

## Next bounded target: the gate-transition receipt

Attempt a source-compatible phase-aware transition contract using the existing signed incidence currents. Require it to state:

- The typed input and output registers: real amplitudes, gate mask h, readiness R, credits and reservations, cell bit and retained event record.

- The acquisition, cancellation, completion and reset rules for each readiness flag, including zero support and reversed currents.

- Which continuous port or event convention supplies opportunities, and how duplicate or blind crossings are handled.

- Whether credits are consumed or reserved, with an explicit balance law.

- How shared-face ownership and causal ordering preserve local compatibility after gluing.

The decisive comparison is stock-only readiness versus phase-aware current-driven latches under the same source amplitudes. Admission requires the declared rule to survive the two-state discriminator, reset test, resource balance, zero/blind preparations and shared-face ordering. Until such a source law is supplied, a constructive latch example would remain a candidate.

## Verification and limits

146 exact named checks passed in the JavaScript orchestration runtime using BigInt rational arithmetic. They cover all16 sign orientations of a four-face boundary column, three rational step sizes, orthogonality and inverse identities, half-return involutions, the discriminator, scaling, readiness failure, the two-quadrature predictor and operator nonuniqueness.

The analytic credit obstructions are proved above; they are not inferred from a finite simulation. This is constructor verification, not independent review or empirical evidence.

The command-line workspace disconnected during this turn. A local executable file and downloadable release ZIP could not be created. The complete standalone JavaScript replay and its exact result are preserved below; the report's Page text is read back for content verification. Visual layout is not verified.

## Exact result

```json
{
  "status": "PASS",
  "exact_named_checks": 146,
  "physical_promotion": 0,
  "epsilon": "1/8",
  "input_stocks": [
    "4",
    "4",
    "4",
    "4",
    "1"
  ],
  "plus": {
    "g": "8",
    "native_cell_stock_derivative": "16",
    "post": [
      "118/65",
      "-118/65",
      "118/65",
      "-118/65",
      "127/65"
    ]
  },
  "minus": {
    "g": "-8",
    "native_cell_stock_derivative": "-16",
    "post": [
      "-134/65",
      "134/65",
      "-134/65",
      "134/65",
      "-1/65"
    ]
  },
  "preserved_total": "17",
  "positivity_masks_before_after": "1111 -> 1111",
  "active_pair": {
    "before": [
      "4",
      "1"
    ],
    "after": [
      "236/65",
      "127/65"
    ]
  },
  "scope": "Candidate collective update; exact rational identities. Proofs about all real support and integer credits are separate analytic arguments, not inferred from these fixtures."
}
```

## Standalone replay

Save the following as verify_ud_amplitude_readiness_v0_1.js and run node verify_ud_amplitude_readiness_v0_1.js. It uses only JavaScript built-ins.

```javascript
// UD amplitude-to-readiness audit v0.1. Standalone JavaScript; no dependencies.
// Run with Node.js, or paste into a JavaScript console.
(() => {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
  const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];};
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>Q(-a[0],a[1]), sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
  const sum=a=>a.reduce(add,Q(0));
  const dot=(a,b)=>sum(a.map((x,i)=>mul(x,b[i])));
  const sq=a=>mul(a,a);
  const stock=v=>v.map(sq), norm=v=>sum(stock(v));
  const text=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);
  let checks=0;const check=(ok,label)=>{if(!ok)throw Error(label);checks++;};
  const same=(a,b)=>a.length===b.length&&a.every((x,i)=>eq(x,b[i]));
  const U=(v,b,e)=>{
    const f=v.slice(0,4),u=v[4],g=dot(b,f),den=add(Q(1),sq(e));
    const alpha=div(e,den),beta=div(sq(e),mul(Q(2),den));
    const r=div(sub(Q(1),sq(e)),den);
    return [...f.map((x,i)=>sub(sub(x,mul(alpha,mul(b[i],u))),mul(beta,mul(b[i],g)))),
      add(mul(r,u),mul(alpha,g))];
  };
  const R=(v,b)=>{const g=dot(b,v.slice(0,4));return [...v.slice(0,4).map((x,i)=>sub(x,mul(Q(1,2),mul(b[i],g)))),neg(v[4])];};
  const basis=Array.from({length:5},(_,j)=>Array.from({length:5},(_,i)=>Q(i===j?1:0)));
  const b=[1,-1,1,-1].map(x=>Q(x)),e=Q(1,8);
  for(let mask=0;mask<16;mask++){
    const oriented=Array.from({length:4},(_,i)=>Q(mask&(1<<i)?1:-1));
    for(const step of [Q(1,8),Q(1,3),Q(1)]){
      const cols=basis.map(v=>U(v,oriented,step));
      check(cols.every((a,j)=>cols.every((c,k)=>eq(dot(a,c),Q(j===k?1:0)))),"U orthogonal");
      check(basis.every(v=>same(U(U(v,oriented,step),oriented,neg(step)),v)),"U inverse");
    }
    check(basis.every(v=>same(R(R(v,oriented),oriented),v)),"half-return involution");
    const cols=basis.map(v=>R(v,oriented));
    check(cols.every((a,j)=>cols.every((c,k)=>eq(dot(a,c),Q(j===k?1:0)))),"half-return orthogonal");
  }
  const plus=[...b.map(x=>mul(Q(2),x)),Q(1)];
  const minus=[...b.map(x=>mul(Q(-2),x)),Q(1)];
  const up=U(plus,b,e),um=U(minus,b,e);
  check(same(stock(plus),stock(minus)),"identical five input stocks");
  check(eq(norm(plus),Q(17))&&eq(norm(minus),Q(17)),"input total17");
  check(eq(up[4],Q(127,65))&&eq(um[4],Q(-1,65)),"opposite post-cell signs");
  check(eq(norm(up),Q(17))&&eq(norm(um),Q(17)),"post total17");
  const ready=v=>v.slice(0,4).map(x=>x[0]!==0n);
  check(ready(plus).every(Boolean)&&ready(minus).every(Boolean),"four faces initially positive stock");
  check(ready(up).every(Boolean)&&ready(um).every(Boolean),"positivity fails commit reset");
  check(eq(mul(Q(2),mul(plus[4],dot(b,plus.slice(0,4)))),Q(16)),"positive native cell flux");
  check(eq(mul(Q(2),mul(minus[4],dot(b,minus.slice(0,4)))),Q(-16)),"negative native cell flux");
  const g=dot(b,plus.slice(0,4)),alpha=Q(8,65),r=Q(63,65);
  const pair=[div(g,Q(2)),plus[4]];
  const pairNext=[sub(mul(r,pair[0]),mul(Q(2),mul(alpha,pair[1]))),
                  add(mul(Q(2),mul(alpha,pair[0])),mul(r,pair[1]))];
  check(eq(pairNext[0],div(dot(b,up.slice(0,4)),Q(2)))&&eq(pairNext[1],up[4]),"two-quadrature predictor");
  check(eq(norm(pair),norm(pairNext)),"active pair support preserved");
  const V=v=>[...v.slice(0,4),neg(v[4])];
  check(eq(R(plus,b)[4],V(plus)[4]),"two distinct sign-flip laws agree on cell readout");
  check(!same(R(plus,b),V(plus)),"cell bit fails operator selection");
  check(eq(norm(R(plus,b)),Q(17))&&eq(norm(V(plus)),Q(17)),"both sign-flip laws preserve support");
  check(same(U(Array(5).fill(Q(0)),b,e),Array(5).fill(Q(0))),"zero amplitude fixed");
  const posCell=[Q(0),Q(0),Q(0),Q(0),Q(1)];
  check(U(posCell,b,e)[4][0]>0n,"ordinary small step does not force bit flip");
  for(const scale of [Q(1,5),Q(1),Q(3)]){
    const a=plus.map(x=>mul(scale,x)),c=minus.map(x=>mul(scale,x));
    check(same(stock(a),stock(c))&&U(a,b,e)[4][0]>0n&&U(c,b,e)[4][0]<0n,"scaled stock ambiguity");
  }
  const results={
    status:"PASS",exact_named_checks:checks,physical_promotion:0,
    epsilon:text(e),input_stocks:stock(plus).map(text),
    plus:{g:text(g),native_cell_stock_derivative:"16",post:up.map(text)},
    minus:{g:text(dot(b,minus.slice(0,4))),native_cell_stock_derivative:"-16",post:um.map(text)},
    preserved_total:"17",positivity_masks_before_after:"1111 -> 1111",
    active_pair:{before:pair.map(text),after:pairNext.map(text)},
    scope:"Candidate collective update; exact rational identities. Proofs about all real support and integer credits are separate analytic arguments, not inferred from these fixtures."
  };
  return results;
})()
```
