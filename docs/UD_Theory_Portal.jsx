import { useState, useEffect } from "react";

const SF = "'Crimson Pro','Georgia',serif";
const MF = "'JetBrains Mono','Menlo',monospace";
const EF = "'Crimson Pro','Times New Roman',serif";

const ES = [
  { id:"V1", label:"V₁", dim:1, lam:1, energy:"0", color:"#5CE0D2", role:"FREE", phys:"Vacuum / Gravity", spin:"P₊", corr:"Invariant" },
  { id:"V12", label:"V₁/₂", dim:2, lam:0.5, energy:"½", color:"#F2C744", role:"BROKEN", phys:"Weak / Flavor", spin:"P₊", corr:"Rotated" },
  { id:"V13", label:"V₁/₃", dim:3, lam:1/3, energy:"⅔", color:"#E8565C", role:"CONFINED", phys:"Color / Strong", spin:"P₋", corr:"Invariant" },
];

const LS = [
  {id:"LS1",c:"Retention",d:"R(ψ, n) = cos²(ψ, Tⁿψ)"},
  {id:"LS2",c:"Repair",d:"B = ∑(1−μ) ‖Pμ δψ‖²"},
  {id:"LS3",c:"Free repair",d:"B = 0 in degenerate sectors"},
  {id:"LS4",c:"Projector",d:"Pλ unique from spectral theorem"},
  {id:"LS5",c:"Totality",d:"All T eigenvalues > 0"},
  {id:"LS6",c:"Gap",d:"Δλ_min = 1/6"},
  {id:"LS7",c:"Cost order",d:"C(λ → μ) = 1 − μ"},
  {id:"LS8",c:"Decay",d:"|R(n) − R(∞)| ~ (λ₂/λ₁)ⁿ"},
  {id:"LS9",c:"S₄ irreps",d:"C⁶ = 1 ⊕ 2 ⊕ 3"},
  {id:"LS10",c:"Convergence",d:"‖Tⁿ − P₁‖ = (½)ⁿ"},
  {id:"LS11",c:"Additivity",d:"B(δψ₁ + δψ₂) = B₁ + B₂"},
  {id:"LS12",c:"Harmonic",d:"λ_k = 1/k with dim = k"},
];

const PR = [
  {p:"Spatial dimensions",v:"3",x:"3",e:0,ex:true,cat:"str"},
  {p:"Generations",v:"3",x:"3",e:0,ex:true,cat:"str"},
  {p:"Colors",v:"3",x:"3",e:0,ex:true,cat:"str"},
  {p:"Gluons",v:"8",x:"8",e:0,ex:true,cat:"str"},
  {p:"Graviton pol.",v:"2",x:"2",e:0,ex:true,cat:"str"},
  {p:"Fine structure α",v:"1/137",x:"1/137.036",e:0.026,cat:"cpl"},
  {p:"Spectral tilt",v:"185/192",x:"0.9649",e:0.14,cat:"cos"},
  {p:"Muon mass",v:"105.9 MeV",x:"105.66",e:0.2,cat:"mas"},
  {p:"Tau mass",v:"1762 MeV",x:"1776.9",e:0.8,cat:"mas"},
  {p:"Cabibbo angle",v:"sin 12°",x:"0.225",e:7.6,cat:"mix"},
  {p:"V_cb",v:"λ² = 0.043",x:"0.041",e:5.4,cat:"mix"},
  {p:"sin²θ_W bare",v:"1/4",x:"0.231",e:8.1,cat:"cpl"},
  {p:"Mass ratio",v:"√3",x:"~2.13",e:19,cat:"mas"},
  {p:"Z_max",v:"118–120",x:"118",e:0,ex:false,cat:"str",nt:"consistent"},
  {p:"Proton lifetime",v:">10⁴⁵ yr",x:">10³⁴ yr",e:0,ex:false,cat:"str",nt:"consistent"},
  {p:"Higgs ratio",v:"3.9",x:"1.56",e:-1,cat:"mas"},
  {p:"V_ub",v:"λ³ ≈ 0.009",x:"0.0036",e:-2,cat:"mix"},
];

const ORB = [
  {nm:"Stars",ct:4,ed:3,v1:"½",v12:"0",v13:"½",cl:"#E8565C",nt:"Pure color + vacuum. V₁/₂ vanishes exactly."},
  {nm:"4-Cycles",ct:3,ed:4,v1:"⅔",v12:"⅓",v13:"0",cl:"#F2C744",nt:"Pure weak + vacuum. V₁/₃ vanishes exactly."},
  {nm:"K₄ − 1",ct:6,ed:5,v1:"5/6",v12:"1/15",v13:"1/10",cl:"#888",nt:"All three sectors present."},
];

const SMP = [
  {n:2,nm:"Triangle",dm:"1, 2",ed:3},
  {n:3,nm:"Tetrahedron",dm:"1, 2, 3",ed:6,ok:true},
  {n:4,nm:"Pentachoron",dm:"1, 4, 5",ed:10},
  {n:5,nm:"5-simplex",dm:"1, 5, 9",ed:15},
  {n:6,nm:"6-simplex",dm:"1, 6, 14",ed:21},
  {n:7,nm:"7-simplex",dm:"1, 7, 20",ed:28},
];

const CK = [
  {el:"V_us",pr:"sin(12°) = 0.208",xp:"0.225",er:"7.6%",ok:true},
  {el:"V_cb",pr:"λ² = 0.043",xp:"0.041",er:"5.4%",ok:true},
  {el:"V_ub",pr:"λ³ ≈ 0.009",xp:"0.0036",er:"2.5×",ok:false},
];

const TABS = ["◇ Architecture","∞ Loop Spine","◎ Predictions","⊕ Selection","⬡ Orbits","△ Uniqueness","↻ CKM","✎ Review"];

function Pill({children,color="#555"}){return <span style={{display:"inline-block",fontSize:10,padding:"2px 9px",borderRadius:10,background:color+"18",color,fontWeight:600,fontFamily:MF,lineHeight:1.6}}>{children}</span>;}
function Hd({children,sub}){return <div style={{marginBottom:16}}><h2 style={{fontSize:20,fontWeight:300,letterSpacing:1,color:"#fff"}}>{children}</h2>{sub&&<p style={{fontSize:11,color:"#555",marginTop:4,fontFamily:MF}}>{sub}</p>}<div style={{width:40,height:1,background:"linear-gradient(90deg,#F2C744,transparent)",marginTop:10}}/></div>;}
function Cd({children,accent,sx}){return <div style={{padding:"14px 16px",borderRadius:10,marginBottom:10,background:"rgba(255,255,255,0.02)",borderLeft:accent?"3px solid "+accent:"3px solid #222",...sx}}>{children}</div>;}

function Tet({size=120}){
  const [t,setT]=useState(0);
  useEffect(()=>{const id=setInterval(()=>setT(p=>p+0.015),40);return()=>clearInterval(id);},[]);
  const cx=size/2,cy=size/2,r=size*0.36,w=Math.sin(t*0.7)*3;
  const pts=[{x:cx+w,y:cy-r},{x:cx-r*0.87-w*0.5,y:cy+r*0.5},{x:cx+r*0.87+w*0.5,y:cy+r*0.5},{x:cx-w*0.3,y:cy+r*0.12}];
  const E=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
  const C=["#E8565C","#F2C744","#5CE0D2","#E8565C","#F2C744","#5CE0D2"];
  return <svg width={size} height={size} viewBox={"0 0 "+size+" "+size}><defs><filter id="glow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>{E.map(([a,b],i)=><line key={i} x1={pts[a].x} y1={pts[a].y} x2={pts[b].x} y2={pts[b].y} stroke={C[i]} strokeWidth={2.2} opacity={0.35+0.35*Math.sin(t*0.8+i)} filter="url(#glow)"/>)}{pts.map((p,i)=><circle key={i} cx={p.x} cy={p.y} r={4} fill="#fff" opacity={0.85}/>)}</svg>;
}

function Bar({e}){
  const ls=e.id==="V13"?"1/3":String(e.lam);
  return <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:10}}>
    <span style={{width:50,fontFamily:EF,fontSize:16,color:e.color,fontWeight:700}}>{e.label}</span>
    <div style={{flex:1,height:30,background:"rgba(255,255,255,0.03)",borderRadius:6,overflow:"hidden"}}>
      <div style={{height:"100%",width:(e.lam*100)+"%",borderRadius:6,background:"linear-gradient(90deg,"+e.color+"33,"+e.color+"cc)",display:"flex",alignItems:"center",justifyContent:"flex-end",paddingRight:10}}>
        <span style={{fontSize:12,color:"#000",fontWeight:700,fontFamily:MF}}>{"λ = "+ls}</span>
      </div>
    </div>
    <div style={{textAlign:"right",minWidth:60}}>
      <div style={{fontSize:11,color:"#999",fontFamily:MF}}>dim {e.dim}</div>
      <Pill color={e.color}>{e.role}</Pill>
    </div>
  </div>;
}

function P0(){return <div>
  <Hd sub="One 6×6 matrix. Three eigenspaces.">The Spectral Architecture</Hd>
  <div style={{textAlign:"center",marginBottom:12}}><Tet size={130}/></div>
  <p style={{fontSize:14,lineHeight:1.75,color:"#999",marginBottom:20}}>The tetrahedron has 6 edges carrying transport matrix T with eigenvalues 1, ½, ⅓ and eigenspace dimensions 1, 2, 3 — matching U(1) × SU(2) × SU(3).</p>
  {ES.map(e=><Bar key={e.id} e={e}/>)}
  <Cd accent="#222" sx={{marginTop:16}}>
    <div style={{display:"grid",gridTemplateColumns:"1fr",gap:14}}>
      {[{l:"Transport",q:"T = ½I + off-diag",n:"Doubly stochastic"},{l:"Hamiltonian",q:"H = I − T",n:"Energy = gap"},{l:"Spin",q:"S : σ ↔ σ̄",n:"[T,S] = [S,*] = 0"},{l:"Hodge",q:"*² = I",n:"Signs (+, −, +)"}].map((x,i)=><div key={i}><div style={{fontSize:10,color:"#F2C744",fontWeight:600,fontFamily:MF}}>{x.l}</div><div style={{fontSize:14,color:"#ddd",marginTop:3,fontFamily:EF,fontStyle:"italic"}}>{x.q}</div><div style={{fontSize:9,color:"#555",marginTop:2}}>{x.n}</div></div>)}
    </div>
  </Cd>
</div>;}

function P1(){return <div>
  <Hd sub="12 locked results. Pure spectral algebra.">The Loop Spine</Hd>
  <div style={{display:"flex",gap:6,marginBottom:14,flexWrap:"wrap"}}><Pill color="#5CE0D2">L_R → L_C → L_T</Pill><Pill color="#F2C744">Layer A exact</Pill></div>
  {LS.map((ls,i)=><div key={i} style={{marginBottom:4,padding:"10px 12px",borderRadius:8,background:i%2===0?"rgba(255,255,255,0.015)":"transparent"}}>
    <div style={{display:"flex",gap:8,alignItems:"center"}}>
      <span style={{fontSize:10,color:"#444",fontFamily:MF,minWidth:32}}>{ls.id}</span>
      <span style={{fontSize:14,fontWeight:600,color:"#ddd"}}>{ls.c}</span>
    </div>
    <div style={{marginLeft:40,marginTop:4,fontSize:13,color:"#999",fontFamily:EF,fontStyle:"italic",lineHeight:1.5,wordBreak:"break-word"}}>{ls.d}</div>
  </div>)}
  <Cd accent="#F2C744" sx={{marginTop:14}}><p style={{fontSize:12,color:"#888",lineHeight:1.6}}><strong style={{color:"#F2C744"}}>THM-566:</strong> Mass ratio = √3. <strong style={{color:"#F2C744"}}>THM-567:</strong> Coupling angle ∈ [60°, 120°]. Zero parameters.</p></Cd>
</div>;}

function P2(){
  const [fil,setFil]=useState("all");
  const cm={str:"Structure",cpl:"Couplings",mas:"Masses",mix:"Mixing",cos:"Cosmo"};
  const list=fil==="all"?PR:PR.filter(p=>p.cat===fil);
  const bs=(a)=>({padding:"5px 11px",border:"1px solid",borderRadius:12,borderColor:fil===a?"#F2C744":"#1e1e1e",background:fil===a?"#F2C74410":"transparent",color:fil===a?"#F2C744":"#555",fontSize:10,fontFamily:MF,cursor:"pointer"});
  return <div>
    <Hd sub="Zero free parameters.">Falsifiable Predictions</Hd>
    <div style={{display:"flex",gap:4,marginBottom:12,flexWrap:"wrap"}}>
      <button onClick={()=>setFil("all")} style={bs("all")}>All</button>
      {Object.entries(cm).map(([k,v])=><button key={k} onClick={()=>setFil(k)} style={bs(k)}>{v}</button>)}
    </div>
    {list.map((r,i)=>{const fail=r.e<0;const dc=fail?"#E8565C":r.ex?"#5CE0D2":r.nt?"#888":r.e<=1?"#5CE0D2":r.e<=10?"#F2C744":"#F2C744";const et=r.ex?"exact":r.nt?r.nt:fail?(r.e===-1?"FAILS":"2.5× open"):r.e+"%";
    return <div key={i} style={{display:"flex",alignItems:"center",gap:7,padding:"7px 10px",marginBottom:3,borderRadius:5,background:fail?"rgba(232,86,92,0.04)":"rgba(255,255,255,0.012)"}}>
      <span style={{width:8,height:8,borderRadius:"50%",background:dc,flexShrink:0}}/><span style={{flex:1,fontSize:13,color:"#ccc"}}>{r.p}</span><span style={{fontSize:11,color:"#666",fontFamily:MF,minWidth:70,textAlign:"right"}}>{r.v}</span><span style={{fontSize:11,color:dc,fontFamily:MF,minWidth:55,textAlign:"right",fontWeight:600}}>{et}</span>
    </div>;})}
    <div style={{display:"flex",gap:20,marginTop:14,justifyContent:"center"}}>{[{n:5,l:"exact",c:"#5CE0D2"},{n:6,l:"≤10%",c:"#F2C744"},{n:2,l:"fails",c:"#E8565C"}].map((s,i)=><div key={i} style={{textAlign:"center"}}><div style={{fontSize:24,fontWeight:700,color:s.c,fontFamily:MF}}>{s.n}</div><div style={{fontSize:9,color:"#555"}}>{s.l}</div></div>)}</div>
  </div>;
}

function P3(){return <div>
  <Hd sub="The corridor rotation selects physics.">The Selection Law</Hd>
  <p style={{fontSize:13,lineHeight:1.7,color:"#999",marginBottom:14}}>The corridor rotation U(θ) respects spin S. Since V₁/₂ lives in P₊ and V₁/₃ = P₋, the rotation acts on V₁/₂ only.</p>
  {ES.map(e=><Cd key={e.id} accent={e.color}><div style={{display:"flex",alignItems:"center",gap:12}}>
    <span style={{fontSize:18,fontWeight:700,color:e.color,fontFamily:EF,minWidth:50}}>{e.label}</span>
    <div style={{flex:1}}>
      <div style={{fontSize:13,color:"#bbb"}}>{e.corr} · {e.spin} · E = {e.energy}{e.dim>1?" · Degenerate":" · Singleton"}</div>
      <div style={{fontSize:12,color:"#777",marginTop:4}}>{"→ "+e.phys+" "}<Pill color={e.color}>{e.role}</Pill></div>
    </div>
  </div></Cd>)}
  <div style={{display:"flex",alignItems:"center",justifyContent:"center",gap:8,padding:"18px 0"}}>
    {[{g:"n = 4",eps:"30°",c:"#E8565C"},{g:"n = 5",eps:"12°",c:"#F2C744"},{g:"n = 6",eps:"0°",c:"#5CE0D2"}].map((g,i)=><div key={i} style={{display:"flex",alignItems:"center",gap:8}}>
      <div style={{width:70,height:70,borderRadius:"50%",border:"2px solid "+g.c,display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center",background:g.c+"0a"}}><span style={{fontSize:11,fontWeight:700,color:g.c}}>{g.g}</span><span style={{fontSize:9,color:"#666"}}>{"ε = "+g.eps}</span></div>
      {i<2&&<div style={{textAlign:"center",minWidth:36}}><div style={{fontSize:16,color:"#444"}}>{"→"}</div><div style={{fontSize:9,color:"#F2C744",fontFamily:MF}}>{"Δε = "+["18°","12°"][i]}</div></div>}
    </div>)}
  </div>
  <Cd accent="#F2C744"><p style={{fontSize:12,color:"#888",lineHeight:1.65,textAlign:"center"}}>Color confines: P₋ invisible to corridor.<br/>Weak breaks: V₁/₂ rotated at each boundary.<br/>Gravity free: V₁ trivially invariant.</p></Cd>
</div>;}

function P4(){return <div>
  <Hd sub="13 configs. 3 orbits. Exact eigenspace generation.">Binary Orbits</Hd>
  {ORB.map((o,i)=><Cd key={i} accent={o.cl}>
    <div style={{display:"flex",justifyContent:"space-between",marginBottom:6}}><span style={{fontSize:15,fontWeight:700,color:o.cl}}>{o.nm}</span><span style={{fontSize:10,color:"#555",fontFamily:MF}}>{o.ct} configs · {o.ed} edges</span></div>
    <div style={{display:"flex",gap:14,marginBottom:6}}><span style={{fontSize:12,color:"#5CE0D2"}}>V₁ : {o.v1}</span><span style={{fontSize:12,color:"#F2C744"}}>V₁/₂ : {o.v12}</span><span style={{fontSize:12,color:"#E8565C"}}>V₁/₃ : {o.v13}</span></div>
    <p style={{fontSize:11,color:"#666"}}>{o.nt}</p>
  </Cd>)}
  <Cd accent="#5CE0D2"><p style={{fontSize:12,color:"#888",lineHeight:1.65}}><strong style={{color:"#5CE0D2"}}>Stars − V₁ = V₁/₃</strong> (rank 3). <strong style={{color:"#F2C744"}}>4-Cycles − V₁ = V₁/₂</strong> (rank 2). Discrete generates continuous.</p></Cd>
</div>;}

function P5(){return <div>
  <Hd sub="THM-568: Why the tetrahedron.">Uniqueness</Hd>
  <p style={{fontSize:13,lineHeight:1.7,color:"#999",marginBottom:14}}>The n-simplex edge rep under S(n+1) has irrep dims <strong style={{color:"#F2C744"}}>1, n, n(n−1)/2 − 1</strong>. Only n = 3 gives 1, 2, 3.</p>
  <div style={{borderRadius:8,overflow:"hidden",marginBottom:14}}>
    <div style={{display:"grid",gridTemplateColumns:"1fr 35px 85px 30px",padding:"7px 12px",background:"rgba(255,255,255,0.04)",fontSize:10,fontFamily:MF,color:"#666"}}><span>Simplex</span><span style={{textAlign:"center"}}>E</span><span style={{textAlign:"center"}}>Irrep dims</span><span></span></div>
    {SMP.map((s,i)=><div key={i} style={{display:"grid",gridTemplateColumns:"1fr 35px 85px 30px",padding:"8px 12px",fontSize:13,background:s.ok?"rgba(242,199,68,0.06)":"transparent",borderLeft:s.ok?"3px solid #F2C744":"3px solid transparent"}}>
      <span style={{color:s.ok?"#fff":"#777"}}>{s.nm}</span><span style={{textAlign:"center",color:"#555",fontFamily:MF}}>{s.ed}</span><span style={{textAlign:"center",color:s.ok?"#F2C744":"#444",fontFamily:MF,fontWeight:s.ok?700:400}}>{s.dm}</span><span style={{textAlign:"center",color:s.ok?"#5CE0D2":"#222",fontSize:16}}>{s.ok?"★":"—"}</span>
    </div>)}
  </div>
  <Cd accent="#F2C744"><p style={{fontSize:12,color:"#888",lineHeight:1.6}}>No other simplex, Platonic solid, or symmetric graph matches 1, 2, 3. The tetrahedron uniquely encodes U(1) × SU(2) × SU(3).</p></Cd>
</div>;}

function P6(){return <div>
  <Hd sub="Partially recovered.">CKM Recovery</Hd>
  <Cd accent="#F2C744" sx={{marginBottom:14}}><p style={{fontSize:12,color:"#999",lineHeight:1.65}}>The 60° floor is intra-generation. CKM is inter-generation. The floor does not constrain CKM.</p></Cd>
  {CK.map((c,i)=><div key={i} style={{display:"flex",alignItems:"center",gap:10,padding:"10px 12px",marginBottom:6,borderRadius:6,background:"rgba(255,255,255,0.02)",borderLeft:"3px solid "+(c.ok?"#F2C744":"#E8565C")}}>
    <span style={{fontSize:14,fontWeight:700,color:"#ccc",fontFamily:MF,minWidth:40}}>{c.el}</span>
    <div style={{flex:1}}><div style={{fontSize:12,color:"#999"}}>{c.pr}</div><div style={{fontSize:10,color:"#555"}}>exp: {c.xp}</div></div>
    <Pill color={c.ok?"#F2C744":"#E8565C"}>{c.er}</Pill>
  </div>)}
  <Cd accent="#888" sx={{marginTop:10}}><p style={{fontSize:12,color:"#777",lineHeight:1.6}}>CP phase: δ = π/30 = 6°. Structural, not fitted.</p></Cd>
</div>;}

function P7(){return <div>
  <Hd sub="Proof-state boundaries preserved.">Review Posture</Hd>
  {[{l:"Exact Structural",n:31,c:"#5CE0D2",d:"Complete proofs. No physical identification."},{l:"Supported Bridge",n:18,c:"#F2C744",d:"Numerical matches with bridges."},{l:"Working Structural",n:6,c:"#888",d:"Intermediate with dependencies."},{l:"Open Failures",n:2,c:"#E8565C",d:"Higgs ratio and V_ub."}].map((x,i)=><Cd key={i} accent={x.c}>
    <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:3}}><span style={{fontSize:13,fontWeight:600,color:x.c}}>{x.l}</span><span style={{fontSize:20,fontWeight:700,color:x.c,fontFamily:MF}}>{x.n}</span></div>
    <p style={{fontSize:10,color:"#555"}}>{x.d}</p>
  </Cd>)}
  <div style={{marginTop:14,padding:14,background:"#0b0b12",borderRadius:8,border:"1px solid #181828"}}><p style={{fontSize:12,color:"#888",lineHeight:1.7}}>UD develops a structural core from a recursive tetrahedral substrate, from which gauge algebra, mass splitting, quark-lepton decomposition, and chirality are derived or supported at different proof-state levels.</p></div>
</div>;}

export default function UDPortal(){
  const [tab,setTab]=useState(0);
  const [cnt,setCnt]=useState(0);
  useEffect(()=>{let n=0;const id=setInterval(()=>{n+=Math.ceil((581-n)*0.12);if(n>=581){n=581;clearInterval(id);}setCnt(n);},50);return()=>clearInterval(id);},[]);
  const pages=[<P0 key={0}/>,<P1 key={1}/>,<P2 key={2}/>,<P3 key={3}/>,<P4 key={4}/>,<P5 key={5}/>,<P6 key={6}/>,<P7 key={7}/>];
  return <div style={{minHeight:"100vh",background:"radial-gradient(ellipse at 50% 0%,#12121a 0%,#08080c 70%)",color:"#e0e0e0",fontFamily:SF,padding:"0 14px"}}>
    <style>{"@import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');*{box-sizing:border-box;margin:0;padding:0}::selection{background:#F2C74433}button{border:none;outline:none}"}</style>
    <header style={{textAlign:"center",paddingTop:28,paddingBottom:4}}>
      <Tet size={110}/>
      <h1 style={{fontSize:24,fontWeight:300,letterSpacing:4,color:"#fff",marginTop:2}}>UNIFIED DYNAMICS</h1>
      <p style={{fontSize:10,color:"#3a3a3a",letterSpacing:3,fontFamily:MF,marginTop:1}}>DISTINCTION THEORY</p>
      <div style={{display:"flex",justifyContent:"center",gap:28,marginTop:14}}>
        {[{v:cnt,l:"THEOREMS",c:"#5CE0D2"},{v:"0",l:"FREE PARAMS",c:"#F2C744"},{v:"1",l:"GEOMETRY",c:"#E8565C"}].map((s,i)=><div key={i} style={{textAlign:"center"}}><div style={{fontSize:26,fontWeight:700,fontFamily:MF,color:s.c}}>{s.v}</div><div style={{fontSize:8,color:"#3a3a3a",letterSpacing:1.5}}>{s.l}</div></div>)}
      </div>
    </header>
    <nav style={{display:"flex",justifyContent:"center",gap:3,margin:"14px auto 12px",maxWidth:500,flexWrap:"wrap"}}>
      {TABS.map((t,i)=><button key={i} onClick={()=>setTab(i)} style={{padding:"6px 11px",border:"1px solid",borderColor:tab===i?"#F2C744":"#1a1a1a",borderRadius:14,background:tab===i?"#F2C74412":"transparent",color:tab===i?"#F2C744":"#4a4a4a",fontSize:10,fontFamily:MF,cursor:"pointer"}}>{t}</button>)}
    </nav>
    <main style={{maxWidth:500,margin:"0 auto",paddingBottom:40}}>{pages[tab]}</main>
    <footer style={{textAlign:"center",padding:"16px 0 24px",borderTop:"1px solid #111"}}><p style={{fontSize:8,color:"#222",fontFamily:MF,letterSpacing:1}}>UNIFIED DYNAMICS · 581 LOCKED · APRIL 2026</p></footer>
  </div>;
}
