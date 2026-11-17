# C06 quadratic phase receipt v0.16

**EXACT / CONDITIONAL** for odd-stock sensing and post-event isolation in the audited exchange. **CANDIDATE (agile)** for the guard and switch. **OPEN** for native actuation, persistent completion storage, Stage 2, and deficit allocation. Physical Promotion = 0.

## 1. Source and typed observable

Use C06 v0.11, *Boundary action coefficient*, for the unweighted Whitney flag metric and v0.12, *Declared switched interaction*, for its exchange and sector alignment. Let \(X=E\oplus T_2\) with its ordinary-edge Euclidean metric. Let \(Y\) be the flag record space with the declared action metric. Write \(P\) for the odd orthogonal projector in \(X\) and \(R\) for the orthogonal projector in \(Y\) onto \(G(T_2)\), where the direct port \(G:X\to Y\) has \(G^*G=\omega_E^2(I-P)+\omega_-^2P\). The adjoint uses the declared carrier metrics. The specialization to the unweighted unit cell gives \(\omega_E^2=4/3\) and \(\omega_-^2=106/9\). The port fact \(G|_{T_2}/\omega_-\) gives an isometry, so raw record stock computed in the declared metric agrees with stock computed in aligned odd coordinates.

With odd preparation \(u_0=Px_0\ne0\) and empty records, define \(Q_x=\|Px\|^2\), \(Q_y=\|Ry\|_Y^2\), \(N=Q_x+Q_y>0\), \(B=Q_y-Q_x\), and \(f=Q_y/N\). The identity \(Q_x/Q_y=(1-f)/f\) holds for \(Q_y>0\). For control use \(B=0\) with \(N>0\). This avoids division by zero and excludes the absent odd sector. The v0.15 fractions \(1/50,1/2,49/50\) yield ratios \(49,1,1/49\), respectively. This is exact discrimination with the quantitative port stock. The prior finite receipts contain no such stock field in the audited interface.

## 2. Select the first balance and preserve the metric

The v0.12 active odd block in aligned coordinates \((u,v)\) has \(u=u_0\cos(\omega_-t)\), \(v=u_0\sin(\omega_-t)\), and \(\dot B=4\omega_-\langle u,v\rangle\). The ratio is unity at \(\omega_-t=\pi/4+k\pi/2\) for integers \(k\ge0\). A positive incoming derivative selects the ascending occurrences, with \(\dot B=2\omega_-N\) there. The **first** occurrence follows from zero-record preparation and first-event selection. In particular, an ascending balance repeats after phase advances by \(\pi\). The prescribed absorbing Hold state below prevents the active guard from firing again. A sampled sign change would only bracket the first root unless the sampling or within-step event location is exact.

Metric changes affect equality. If on a shared direction the readouts are \(a Q_x\) and \(b Q_y\), for \(a,b>0\), equality moves to \(f=a/(a+b)\). For instance, applying the squared odd port gain \(106/9\) to an already normalized record without a matching carrier factor would select \(9/115\). For direction-dependent quadratic forms on aligned source and record coordinates, equality at \(f=1/2\) for every direction requires the forms agree, by polarization. The declared stock uses the common aligned metric.

## 3. Stock-preserving selective update

The active flow is \((\dot x,\dot y)=(-G^*y,Gx)\). Declare a Ready state and an absorbing Hold state until a separately defined handoff. From a nonzero odd preparation, transition once at the first directed \(B=0\), with positive incoming \(\dot B\). The transition leaves both amplitude registers unchanged and sets
\[
G_{\rm hold}=G(I-P),\qquad
(\dot x,\dot y)=(-G_{\rm hold}^*y,G_{\rm hold}x).
\]
Stock \(\|x\|^2+\|y\|_Y^2\) is conserved by the skew flow on each branch and by the identity amplitude reset. The odd source freezes since \(PG_{\rm hold}^*=0\). Its flag record freezes because \(RG_{\rm hold}=0\). On the v0.12 port, \(G(E)\perp G(T_2)\), so the even block and its record keep exactly their original dynamics. The Ready/Hold memory and actuator are declared choices.

The condition \(RG(I-P)=0\) is equivalent to \(PG^*G(I-P)=0\). This follows by testing whether \(G(E)\) is orthogonal to all \(G(T_2)\). Thus source gating by \(I-P\) alone can fail to freeze the odd record if the port Gram mixes parity. For example with one even and one odd unit coordinate and a scalar record \(G=(1,1)\), the odd record range is the entire record. Cutting the odd source coupling leaves \(G_{\rm hold}=(1,0)\), which still drives the record. An admissible source law must justify the relevant block separation as well as the switch.

## 4. Scope and replay

The source identifies a metric in the declared Whitney port and supports this detector calculation. It leaves open which native mechanism supplies the directed comparison and a persistent operator update. The v0.15 reciprocal comparator solves for \(z=v/u\) on the incoming orbit. The separate scalar balance ODE can give the same arrival time \(2/\omega\) while having a different intermediate trajectory. For example at \(t=1/\omega\), the reciprocal comparator has \(z=3/4\) and \(B/N=-7/25\), whereas the scalar balance ODE gives \(-1/4\). The stock detector and the held exchange are dimensionless mathematical constructions.

Run python3 replay_c06_quadratic_phase.py for exact rational ratio, recurrence direction, metric bias, and two-way isolation controls. The time result follows analytically from the declared oscillator.
