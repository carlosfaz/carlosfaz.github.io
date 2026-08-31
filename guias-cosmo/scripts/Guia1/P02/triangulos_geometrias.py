import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

def ortho(x, y, z, az, el):
    u = -x*np.sin(az) + y*np.cos(az)
    v = -x*np.sin(el)*np.cos(az) - y*np.sin(el)*np.sin(az) + z*np.cos(el)
    return u, v

fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.4))
# Plano
ax = axes[0]
T = np.array([[0,0],[1,0],[0,1]])
ax.fill(T[:,0], T[:,1], color='#0b6e4f', alpha=0.15)
ax.plot(*np.vstack([T, T[0]]).T, color='#0b6e4f', lw=2.2)
for (x,y), a in zip(T, ['90','45','45']):
    ax.annotate(a+'°', (x,y), xytext=(x+0.05, y+0.05), fontsize=9)
ax.set_title(r'Plano: $k=0$, suma = 180°', fontsize=10)
ax.set_aspect('equal'); ax.axis('off')
# Esfera
ax = axes[1]
az, el = 0.55, 0.45
th = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(th), np.sin(th), color='#999999', lw=1.2)
A, B, C = np.array([1.,0,0]), np.array([0,1.,0]), np.array([0,0,1.])
def gc(P, Q):
    t = np.linspace(0, np.pi/2, 60)
    pts = np.outer(np.cos(t), P) + np.outer(np.sin(t), Q)
    return ortho(pts[:,0], pts[:,1], pts[:,2], az, el)
edges = [gc(A,B), gc(B,C), gc(C,A)]
for u, v in edges:
    ax.plot(u, v, color='#d1495b', lw=2.2)
ax.fill(np.concatenate([e[0] for e in edges]), np.concatenate([e[1] for e in edges]), color='#d1495b', alpha=0.15)
for P in [A,B,C]:
    u, v = ortho(P[0], P[1], P[2], az, el)
    ax.annotate('90°', (u, v), xytext=(u+0.05, v+0.08), fontsize=9)
ax.set_title(r'Esfera: $k=+1$, suma = 270°', fontsize=10)
ax.set_aspect('equal'); ax.axis('off')
# Lobachevsky (disco de Poincare)
ax = axes[2]
ax.add_patch(plt.Circle((0,0), 1, fill=False, color='#999999', lw=1.2))
verts = [0.9*np.array([np.cos(a), np.sin(a)]) for a in np.deg2rad([90, 210, 330])]
def geo_arc(p, q):
    A_ = np.array([p, q]); b = np.array([(p@p+1)/2, (q@q+1)/2])
    c = np.linalg.solve(A_, b); R = np.hypot(*(p-c))
    a1 = np.arctan2(p[1]-c[1], p[0]-c[0]); a2 = np.arctan2(q[1]-c[1], q[0]-c[0])
    A1 = np.c_[c[0]+R*np.cos(np.linspace(a1, a2, 120)), c[1]+R*np.sin(np.linspace(a1, a2, 120))]
    A2 = np.c_[c[0]+R*np.cos(np.linspace(a2, a1+2*np.pi, 120)), c[1]+R*np.sin(np.linspace(a2, a1+2*np.pi, 120))]
    if np.hypot(*(A1[60])) <= 1: return A1, c
    return A2, c
arcs, cents = [], []
for i in range(3):
    arc, c = geo_arc(verts[i], verts[(i+1)%3])
    arcs.append(arc); cents.append(c)
for arc in arcs:
    ax.plot(arc[:,0], arc[:,1], color='#7B85FF', lw=2.2)
ax.fill(np.concatenate([a[:,0] for a in arcs]), np.concatenate([a[:,1] for a in arcs]), color='#7B85FF', alpha=0.15)
angs = []
for i in range(3):
    v = verts[i]; c1, c2 = cents[(i-1)%3], cents[i]
    d1, d2 = v-c1, v-c2
    ang = np.degrees(np.arccos(np.clip(d1@d2/np.hypot(*d1)/np.hypot(*d2), -1, 1)))
    angs.append(min(ang, 180-ang))
for v, a in zip(verts, angs):
    ax.annotate(f'{a:.0f}°', v, xytext=v*0.9, fontsize=9, ha='center')
ax.set_title(r'Lobachevsky: $k=-1$, suma = '+str(int(sum(angs)))+'°<180°', fontsize=10)
ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.15,1.15); ax.set_ylim(-1.15,1.15)
fig.tight_layout()
fig.savefig('images/triangulos_geometrias.svg', bbox_inches='tight')
fig.savefig('images/triangulos_geometrias.pdf', bbox_inches='tight')
print('OK: triangulos_geometrias (suma hiperbolica = %d)' % int(sum(angs)))
