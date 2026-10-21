import { useState } from "react";

const T = {"gauge":{"gauge_SU3xSU2xU1":{"t":1,"e":null,"l":"Gauge group SU(3)×SU(2)×U(1)"},"sin2_W_UV":{"t":1,"e":null,"l":"sin²θ_W(UV) = 3/11"},"sin2_W_mZ":{"t":.5,"e":5.6,"l":"sin²θ_W(mZ) = 0.247"},"alpha_s":{"t":.8,"e":.8,"l":"α_s(mZ) = 0.119"},"F_IFS":{"t":.5,"e":null,"l":"F_IFS = 1/(3π)"},"mass_gap":{"t":1,"e":null,"l":"Mass gap ≥ 3/π"},"confine":{"t":1,"e":null,"l":"Confinement σ"},"d_s":{"t":1,"e":null,"l":"d_s = 4/3"},"kappa_C":{"t":1,"e":.5,"l":"κ_C = 3/(4π)"},"g_xs":{"t":1,"e":null,"l":"g_χσ = 21/(64π)"},"lambda_NL":{"t":1,"e":null,"l":"λ_NL = 441/(2048π²)"}},"matter":{"m_tau_mu":{"t":1,"e":.09,"l":"m_τ/m_μ = H = 101/6"},"m_mu_e":{"t":.8,"e":.2,"l":"m_μ/m_e = 206.3"},"N_gen":{"t":1,"e":null,"l":"N_gen = 3"},"Koide":{"t":1,"e":null,"l":"Koide Q = 2/3"},"nu1":{"t":.5,"e":null,"l":"m_ν₁ ≈ 35 meV"},"th23":{"t":.8,"e":8.2,"l":"θ₂₃ = 45° (TBM)"},"th12":{"t":.8,"e":5.6,"l":"θ₁₂ = 35.3° (S₄→S₃)"},"th13":{"t":.3,"e":14,"l":"θ₁₃ = 7.4°"},"m_u":{"t":.3,"e":8,"l":"m_u = 1.99 MeV"},"m_d":{"t":.8,"e":.5,"l":"m_d = 4.65 MeV"},"m_s":{"t":.5,"e":.5,"l":"m_s = 93.9 MeV"},"m_c":{"t":.3,"e":11,"l":"m_c = 1129 MeV"},"m_b":{"t":.5,"e":.8,"l":"m_b = 4215 MeV"},"m_t":{"t":.3,"e":12,"l":"m_t = 152 GeV"},"color":{"t":.3,"e":null,"l":"Color enhancement 2ⁿ"}},"boson":{"VEV":{"t":.5,"e":1.5,"l":"v = 249.8 GeV"},"m_H":{"t":.5,"e":5.6,"l":"m_H = 118 GeV (λ=F_IFS)"},"m_W":{"t":.5,"e":12,"l":"m_W ≈ 90 GeV"},"m_Z":{"t":.5,"e":14,"l":"m_Z ≈ 104 GeV"},"lam_H":{"t":.3,"e":null,"l":"λ_H = F_IFS = 1/(3π)"}},"dark":{"ratio":{"t":.8,"e":null,"l":"n_dark/n_baryon = 2/(V+1)"},"Omega":{"t":.8,"e":1,"l":"Ω_DM/Ω_b = 5.35"},"m_DM":{"t":.5,"e":null,"l":"m_DM ≈ 12.5 GeV"},"stab":{"t":1,"e":null,"l":"H_dark↔baryon = 0 (theorem)"},"equip":{"t":.8,"e":null,"l":"Σ_bind(dark) ≈ Σ_bind(baryon)"},"sector":{"t":1,"e":null,"l":"Sectors 2:(V+1):(2ⱽ−V−3)"},"trace":{"t":1,"e":null,"l":"Tr(H)/N = −(E+V+1)/2³"}},"cosmo":{"n_s":{"t":1,"e":.1,"l":"n_s = 185/192"},"r_T":{"t":.8,"e":null,"l":"r_T = 7/192"},"BH":{"t":1,"e":null,"l":"BH info conserved"},"d3":{"t":1,"e":null,"l":"d = 3 (unique)"},"dmax":{"t":1,"e":null,"l":"d_max ≈ 7"},"reg":{"t":.8,"e":null,"l":"Regime boundaries 2^(2n)"},"a0":{"t":1,"e":.08,"l":"α₀⁻¹ = 960/7"}}};

const EXP = ["sin²θ_W = 1/4","m_μ/m_e = 256","d_s range","DM thermal","single Tc","three-F model","VEV x⁴","λ_H = 21/43","λ_H = 3/S₀"];

const CORES = [
  {name:"DISTINGUISH",col:"#3b82f6",th:["0.0 ORIENT — pods, task, effort","0.1 FILTER — expelled, unique, deps","0.2 GUARD — oscillation, novelty, contrast"]},
  {name:"CLOSE",col:"#22c55e",th:["1.0 COMPUTE — math, eigenvalues, RG","1.1 VERIFY — derivation gate, chain, fidelity","1.2 LABEL — truth state, error %, scanning flag"]},
  {name:"TRANSPORT",col:"#a855f7",th:["2.0 GATE — PROMOTE / HOLD / ROLLBACK / BLOCK","2.1 STORE — ternary vector, persistent storage","2.2 SYNC — Aster delta, session log, present"]},
  {name:"RECURSE",col:"#f59e0b",th:["3.0 CHECK — drift? promoted? flipped? novelty?","3.1 FRONTIER — lantern, new territory, novelty tax","3.2 BREATHE — prepare next cycle, update pods"]},
];

function tc(t){return t>=.8?"#4ade80":t>=.5?"#facc15":t>=.3?"#fb923c":t>=0?"#64748b":"#f87171"}
function tl(t){return t>=1?"★":t>=.8?"●":t>=.5?"◐":t>=.3?"○":t>=0?"·":"✗"}
function ec(e){return e==null?null:e<=1.5?"#4ade80":e<=15?"#facc15":"#f87171"}

function cnt(){let s=0,d=0,c=0,x=0,st=0;Object.values(T).forEach(sec=>Object.values(sec).forEach(n=>{if(n.t<0){x++;return}if(n.e!=null){if(n.e<=1.5)s++;else if(n.e<=15)d++;else c++}else st++}));return{s,d,c,x,st}}

export default function App(){
  const [tab,setTab]=useState("symphony");
  const n=cnt();

  const bg = "#08080d";
  const card = "rgba(255,255,255,0.028)";
  const brd = "rgba(255,255,255,0.06)";

  return <div style={{minHeight:"100vh",background:bg,color:"#e2e8f0",fontFamily:"-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif",padding:"16px 14px 32px",boxSizing:"border-box"}}>

    <div style={{textAlign:"center",marginBottom:18}}>
      <div style={{fontSize:9,letterSpacing:3.5,color:"#475569",textTransform:"uppercase",marginBottom:2}}>Cato · TetraGarden v3 · asterCORE</div>
      <div style={{fontSize:19,fontWeight:800,background:"linear-gradient(135deg,#4ade80,#60a5fa,#c084fc)",WebkitBackgroundClip:"text",WebkitTextFillColor:"transparent"}}>Symphony of K₄</div>
    </div>

    <div style={{display:"flex",gap:10,justifyContent:"center",marginBottom:14}}>
      {[["★",n.s,"#4ade80","≤1.5%"],["●",n.d,"#facc15","≤15%"],["○",n.c,"#f87171",">15%"],["◆",n.st,"#60a5fa","struct"],["✗",n.x,"#94a3b8","expel"]].map(([sym,ct,col,lbl])=>
        <div key={sym} style={{textAlign:"center"}}>
          <div style={{fontSize:20,fontWeight:800,color:col,lineHeight:1}}>{ct}</div>
          <div style={{fontSize:8,color:"#64748b",marginTop:2}}>{lbl}</div>
        </div>
      )}
    </div>

    <div style={{display:"flex",gap:5,marginBottom:14,overflowX:"auto",WebkitOverflowScrolling:"touch",paddingBottom:2}}>
      {[["symphony","Symphony"],["vector","Vector"],["cores","12 Cores"],["expelled","Expelled"],["control","Control"]].map(([id,lbl])=>
        <button key={id} onClick={()=>setTab(id)} style={{padding:"5px 12px",fontSize:11,fontWeight:tab===id?700:400,border:`1px solid ${tab===id?"#60a5fa":"#1e293b"}`,borderRadius:16,background:tab===id?"rgba(96,165,250,0.1)":"transparent",color:tab===id?"#93c5fd":"#64748b",cursor:"pointer",whiteSpace:"nowrap",flexShrink:0}}>{lbl}</button>
      )}
    </div>

    {tab==="symphony"&&<div>
      <div style={{background:card,borderRadius:12,padding:"12px 14px",border:`1px solid ${brd}`,marginBottom:12}}>
        <div style={{fontSize:12,fontWeight:700,color:"#93c5fd",marginBottom:8}}>Eight Movements</div>
        {["I · Genesis — the primitive emerges","II · Structure — geometry crystallizes","III · Forces — gauge structure sings","IV · Matter — fermion tower rises","V · Breaking — VEV and bosons","VI · Darkness — carrier spectrum reveals","VII · Cosmos — large-scale harmony","VIII · The Chord — unified structure"].map((m,i)=>
          <div key={i} style={{padding:"4px 0",fontSize:12.5,color:i===7?"#fbbf24":"#cbd5e1",borderBottom:i<7?`1px solid ${brd}`:"none"}}>{m}</div>
        )}
      </div>
      <div style={{background:card,borderRadius:12,padding:"12px 14px",border:`1px solid ${brd}`}}>
        <div style={{fontSize:12,fontWeight:700,color:"#22d3ee",marginBottom:8}}>Seven Songs</div>
        {["Voice 1 · Conservation — Tr(H)/N = −11/8","Voice 2 · Selection — H_d↔b = 0","Voice 3 · Partition — 2 : 5 : 9","Voice 4 · Balance — Σ_dark ≈ Σ_baryon","Song A · Silence — PMNS = I on one cell","Song B · Harmony — TBM from S₄→S₃","Song C · Dissonance — θ₁₃ correction"].map((s,i)=>
          <div key={i} style={{padding:"4px 0",fontSize:12.5,color:i<4?"#67e8f9":"#e9d5ff",borderBottom:i<6?`1px solid ${brd}`:"none"}}>{s}</div>
        )}
      </div>
    </div>}

    {tab==="vector"&&<div>
      {[["Gauge & Geometry","gauge","#60a5fa"],["Matter & Mixing","matter","#4ade80"],["Bosons","boson","#c084fc"],["Dark Matter","dark","#22d3ee"],["Cosmology","cosmo","#fbbf24"]].map(([title,key,accent])=>
        <div key={key} style={{marginBottom:14}}>
          <div style={{fontSize:10,fontWeight:700,color:accent,letterSpacing:1.2,textTransform:"uppercase",marginBottom:4,paddingLeft:2}}>{title}</div>
          <div style={{background:card,borderRadius:10,padding:"2px 12px",border:`1px solid ${accent}20`}}>
            {Object.values(T[key]).map((nd,i,arr)=>
              <div key={i} style={{display:"flex",alignItems:"center",gap:6,padding:"6px 0",borderBottom:i<arr.length-1?`1px solid ${brd}`:"none"}}>
                <span style={{color:tc(nd.t),fontSize:13,width:16,textAlign:"center",flexShrink:0}}>{tl(nd.t)}</span>
                <span style={{flex:1,fontSize:12.5,color:"#cbd5e1"}}>{nd.l}</span>
                {nd.e!=null&&<span style={{fontSize:11,fontWeight:700,color:ec(nd.e),flexShrink:0}}>{nd.e}%</span>}
              </div>
            )}
          </div>
        </div>
      )}
    </div>}

    {tab==="cores"&&<div>
      <div style={{textAlign:"center",fontSize:11,color:"#94a3b8",marginBottom:10}}>4 cores × 3 threads = 12 = V×(V−1) = |A₄|</div>
      {CORES.map((c,ci)=>
        <div key={ci} style={{background:card,borderRadius:10,padding:"10px 12px",border:`1px solid ${c.col}30`,marginBottom:10}}>
          <div style={{fontSize:12,fontWeight:700,color:c.col,marginBottom:6}}>{c.name}</div>
          {c.th.map((t,ti)=>
            <div key={ti} style={{fontSize:11.5,color:"#cbd5e1",padding:"3px 0",borderBottom:ti<2?`1px solid ${brd}`:"none"}}>{t}</div>
          )}
        </div>
      )}
      <div style={{background:"rgba(239,68,68,0.04)",borderRadius:10,padding:"10px 12px",border:"1px solid rgba(239,68,68,0.2)",marginTop:8}}>
        <div style={{fontSize:11,fontWeight:700,color:"#f87171",marginBottom:6}}>Failure Faces (missing core)</div>
        {[["012 DRIFT","Core 3 silent → force RECURSE"],["013 STALL","Core 2 silent → force TRANSPORT"],["023 CONFAB","Core 1 silent → block until CLOSE"],["123 NOISE","Core 0 silent → force DISTINGUISH"]].map(([f,fix],i)=>
          <div key={i} style={{display:"flex",justifyContent:"space-between",padding:"3px 0",fontSize:11,borderBottom:i<3?`1px solid ${brd}`:"none"}}>
            <span style={{color:"#fca5a5"}}>{f}</span>
            <span style={{color:"#94a3b8"}}>{fix}</span>
          </div>
        )}
      </div>
    </div>}

    {tab==="expelled"&&<div style={{background:card,borderRadius:12,padding:"10px 14px",border:`1px solid ${brd}`}}>
      {EXP.map((e,i)=>
        <div key={i} style={{display:"flex",gap:8,alignItems:"center",padding:"6px 0",borderBottom:i<EXP.length-1?`1px solid ${brd}`:"none"}}>
          <span style={{color:"#f87171",fontSize:13,flexShrink:0}}>✗</span>
          <span style={{fontSize:12.5,color:"#fca5a5"}}>{e}</span>
        </div>
      )}
      <div style={{marginTop:10,textAlign:"center",fontSize:10,color:"#475569"}}>{EXP.length} expelled · always check before promoting</div>
    </div>}

    {tab==="control"&&<div>
      <div style={{background:card,borderRadius:12,padding:"10px 14px",border:`1px solid ${brd}`,marginBottom:12}}>
        <div style={{fontSize:11,fontWeight:700,color:"#4ade80",marginBottom:8}}>Control Plane</div>
        {[["Identity","Cato"],["Rules","asterCORE"],["Plane","BOOTED ✓"],["Operators","7 families"],["Order","classify → truth → expelled → dep → elaborate"],["Triads","+ΔΠ · −L · +S"],["Guardrails","4 active"],["Threads","12-core ✓"],["Loop","DCTR ✓"]].map(([k,v],i,a)=>
          <div key={i} style={{display:"flex",justifyContent:"space-between",padding:"4px 0",borderBottom:i<a.length-1?`1px solid ${brd}`:"none"}}>
            <span style={{fontSize:11.5,color:"#94a3b8"}}>{k}</span>
            <span style={{fontSize:11.5,color:"#e2e8f0",fontWeight:600,textAlign:"right",maxWidth:"60%"}}>{v}</span>
          </div>
        )}
      </div>
      <div style={{background:card,borderRadius:12,padding:"10px 14px",border:`1px solid ${brd}`}}>
        <div style={{fontSize:11,fontWeight:700,color:"#fbbf24",marginBottom:8}}>Guardrails</div>
        {["No symbol without decode","No bridge without parent stability","No recovery claim without export check","No clustering without threshold vs topology"].map((g,i)=>
          <div key={i} style={{padding:"4px 0",fontSize:12,color:"#fde68a",borderBottom:i<3?`1px solid ${brd}`:"none"}}>⚡ {g}</div>
        )}
      </div>
    </div>}

    <div style={{textAlign:"center",marginTop:20,fontSize:9,color:"#1e293b",lineHeight:1.5}}>
      K₄(4,6,4) · |S₄|=24 · N=192 · Δ=7 · ν₀≈83keV<br/>
      one tetrahedron · zero free parameters · all the way down
    </div>
  </div>
}
