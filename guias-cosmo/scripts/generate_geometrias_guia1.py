import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,
    "axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"

def ortho(x, y, z, az, el):
    """Proyeccion ortografica con azimut az y elevacion el."""
    u = -x*np.sin(az) + y*np.cos(az)
    v = -x*np.sin(el)*np.cos(az) - y*np.sin(el)*np.sin(az) + z*np.cos(el)
    return u, v

# ============ FIG 1: triangulos en las tres geometrias (Problema 2) ============
fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.4))

# --- Plano ---
ax = axes[0]
T = np.array([[0,0],[1,0],[0,1]])
ax.fill(T[:,0], T[:,1], color='#0b6e4f', alpha=0.15)
ax.plot(*np.vstack([T, T[0]]).T, color='#0b6e4f', lw=2.2)
for (x,y), a in zip(T, ['90','45','45']):
    ax.annotate(a+'°', (x,y), xytext=(x+0.05, y+0.05), fontsize=9)
ax.set_title(r'Plano: $k=0$, suma = 180°', fontsize=10)
ax.set_aspect('equal'); ax.axis('off')

# --- Esfera ---
ax = axes[1]
az, el = 0.55, 0.45
th = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(th), np.sin(th), color='#999999', lw=1.2)  # contorno
A, B, C = np.array([1.,0,0]), np.array([0,1.,0]), np.array([0,0,1.])
def gc(P, Q):
    t = np.linspace(0, np.pi/2, 60)
    pts = np.outer(np.cos(t), P) + np.outer(np.sin(t), Q)
    return ortho(pts[:,0], pts[:,1], pts[:,2], az, el)
edges = [gc(A,B), gc(B,C), gc(C,A)]
for u, v in edges:
    ax.plot(u, v, color='#d1495b', lw=2.2)
ax.fill(np.concatenate([e[0] for e in edges]), np.concatenate([e[1] for e in edges]), color='#d1495b', alpha=0.15)
for P, t in zip([A,B,C], ['90','90','90']):
    u, v = ortho(P[0], P[1], P[2], az, el)
    ax.annotate(t+'°', (u, v), xytext=(u+0.05, v+0.08), fontsize=9)
ax.set_title(r'Esfera: $k=+1$, suma = 270°', fontsize=10)
ax.set_aspect('equal'); ax.axis('off')

# --- Lobachevsky (disco de Poincare) ---
ax = axes[2]
ax.add_patch(plt.Circle((0,0), 1, fill=False, color='#999999', lw=1.2))
verts = [0.9*np.array([np.cos(a), np.sin(a)]) for a in np.deg2rad([90, 210, 330])]
def geo_arc(p, q):
    A = np.array([p, q]); b = np.array([(p@p+1)/2, (q@q+1)/2])
    c = np.linalg.solve(A, b); R = np.hypot(*(p-c))
    a1, a2 = np.arctan2(p[1]-c[1], p[0]-c[0]), np.arctan2(q[1]-c[1], q[0]-c[0])
    def arc(aa, bb):
        ts = np.linspace(aa, bb, 120)
        return np.c_[c[0]+R*np.cos(ts), c[1]+R*np.sin(ts)], c
    A1, _ = arc(a1, a2); A2, _ = arc(a2, a1+2*np.pi)
    m1, m2 = A1[60], A2[60]
    return (A1, c) if np.hypot(*m1) <= 1 else (A2, c)
arcs, cents = [], []
for i in range(3):
    arc, c = geo_arc(verts[i], verts[(i+1)%3])
    arcs.append(arc); cents.append(c)
for arc in arcs:
    ax.plot(arc[:,0], arc[:,1], color='#7B85FF', lw=2.2)
ax.fill(np.concatenate(arcs), np.concatenate([a[:,1] for a in arcs]), color='#7B85FF', alpha=0.15)
angs = []
for i in range(3):
    v = verts[i]; c1, c2 = cents[(i-1)%3], cents[i]
    d1, d2 = v-c1, v-c2
    ang = np.degrees(np.arccos(np.clip(d1@d2/np.hypot(*d1)/np.hypot(*d2), -1, 1)))
    angs.append(min(ang, 180-ang))
for v, a in zip(verts, angs):
    ax.annotate(f'{a:.0f}°', v, xytext=v*0.9, fontsize=9, ha='center')
ax.set_title(r'Lobachevsky: $k=-1$, suma '+f'$={sum(angs):.0f}°<180°$', fontsize=10)
ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.15,1.15); ax.set_ylim(-1.15,1.15)
fig.tight_layout()
fig.savefig('images/triangulos_geometrias.svg', bbox_inches='tight')
fig.savefig('images/triangulos_geometrias.pdf', bbox_inches='tight')
print('OK: triangulos_geometrias (suma hiperbolica = %.0f)' % sum(angs))

# ============ FIG 2: el factor de volumen r^2 sin(th) (Problema 1) ============
fig, ax = plt.subplots(figsize=(6.4, 3.1))
th = np.linspace(0, np.pi, 400)
ax.plot(np.degrees(th), np.sin(th), color='#0b6e4f', lw=2.4)
ax.fill_between(np.degrees(th), np.sin(th), color='#0b6e4f', alpha=0.10)
ax.axvline(90, color='#d1495b', ls='--', lw=1.1)
ax.axvline(15, color='#d1495b', ls='--', lw=1.1)
ax.annotate('ecuador: celdas grandes\n(sin θ = 1)', (90, 0.5), xytext=(100, 0.62), fontsize=8.5,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.annotate('polos: celdas encogidas\n(sin θ → 0)', (15, 0.26), xytext=(30, 0.12), fontsize=8.5,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.set_xlabel(r'ángulo polar $\theta$ (grados)')
ax.set_ylabel(r'$\sin\theta$')
ax.set_title(r'El corrector de volumen $\sqrt{|\det\eta|}=r^2\sin\theta$ sobre la esfera', fontsize=10)
ax.set_xlim(0, 180); ax.set_ylim(0, 1.1)
fig.tight_layout()
fig.savefig('images/factor_volumen.svg', bbox_inches='tight')
fig.savefig('images/factor_volumen.pdf', bbox_inches='tight')
print('OK: factor_volumen')

# ============ FIG 3: cono de luz en tiempo conforme (Problema 4) ============
fig, ax = plt.subplots(figsize=(6.0, 4.2))
eta = np.linspace(0, 4, 200)
# lineas de luz a 45 grados: psi = +- eta
ax.plot(eta, eta, color='#d1495b', lw=2.2, label='rayo de luz')
ax.plot(eta, -eta, color='#d1495b', lw=2.2)
ax.fill_between([-4, 4], 0, 4, color='#999999', alpha=0.06)
ax.axvline(0, color='k', lw=1.0)
# horizonte de particulas: psi_max = eta
ax.plot([3.0, 3.0], [0, 3.0], color='#0b6e4f', ls='--', lw=2.0)
ax.plot([-3.0, -3.0], [0, 3.0], color='#0b6e4f', ls='--', lw=2.0)
ax.annotate('horizonte de\npartículas\n$\\psi=\\eta$', (3.0, 2.2), xytext=(1.7, 3.2), fontsize=8.5,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.annotate('Big Bang\n$\\eta=0$', (0, 0.05), xytext=(-1.5, 0.6), fontsize=8.5,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.annotate('luz a 45°', (2.4, 2.4), xytext=(2.6, 1.4), fontsize=9, color='#d1495b',
            arrowprops=dict(arrowstyle='->', lw=0.8, color='#d1495b'))
ax.set_xlabel(r'distancia comóvil $\psi$')
ax.set_ylabel(r'tiempo conforme $\eta$')
ax.set_title('La luz viaja en línea recta a 45° en el mapa conforme', fontsize=10)
ax.set_xlim(-4, 4); ax.set_ylim(0, 4)
ax.legend(loc='lower center', fontsize=8.5)
fig.tight_layout()
fig.savefig('images/cono_conforme.svg', bbox_inches='tight')
fig.savefig('images/cono_conforme.pdf', bbox_inches='tight')
print('OK: cono_conforme')
