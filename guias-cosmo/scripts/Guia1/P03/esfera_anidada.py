import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

def ortho(x, y, z, az, el):
    u = -x*np.sin(az) + y*np.cos(az)
    v = -x*np.sin(el)*np.cos(az) - y*np.sin(el)*np.sin(az) + z*np.cos(el)
    return u, v

fig, axes = plt.subplots(1, 3, figsize=(9.8, 3.4))
az, el = 0.7, 0.35

# Panel 1: S^1 (circulo) -> ds1^2 = dphi^2
ax = axes[0]
th = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(th), np.sin(th), color='#0b6e4f', lw=2.4)
ax.plot([0,0],[-1,1], color='#d1495b', lw=1.6, ls='--')
ax.annotate(r'$ds_1^2=d\phi^2$', (0, 0.2), xytext=(1.15, 0.25), fontsize=11,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.text(0, -1.35, r'1D: circulo $S^1$', ha='center', fontsize=10)
ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.6,2.0); ax.set_ylim(-1.5,1.5)

# Panel 2: S^2 (esfera) con circulos en latitudes (muñeca rusa: cada theta es un S^1)
ax = axes[1]
latitudes = np.linspace(np.pi/14, np.pi-np.pi/14, 6)
for vv_ang in latitudes:
    vv = np.linspace(0, 2*np.pi, 120)
    cx = np.cos(vv)*np.sin(vv_ang); cy = np.sin(vv)*np.sin(vv_ang); cz = np.full_like(vv, np.cos(vv_ang))
    ax.plot(*ortho(cx, cy, cz, az, el), color='#1f77b4', lw=1.4, alpha=0.9)
th = np.linspace(0, 2*np.pi, 200)
ax.plot(*ortho(np.cos(th), np.sin(th), np.zeros_like(th), az, el), color='#d1495b', lw=2.6)
ax.annotate(r'$ds_2^2=d\theta^2+\sin^2\theta\,d\phi^2$', (0.2, 0.9), xytext=(-2.6, 1.5), fontsize=11,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.text(0, -1.75, r'2D: esfera $S^2$ (hecha de c\'irculos $S^1$)', ha='center', fontsize=10)
ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-2.9,2.0); ax.set_ylim(-2.0,2.0)

# Panel 3: S^3 (hiperesfera) vista como esfera de esferas (esquematica)
ax = axes[2]
th = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(th), np.sin(th), color='#999999', lw=1.4)          # contorno 3D
# esfera transversal (el "cascarón" que es una S^2 x S^2 en la carta de Hopf)
for t_chi in np.linspace(0, 1, 5):
    r = np.sqrt(1-t_chi**2)
    tt = np.linspace(0, 2*np.pi, 120)
    # aros de la fibra S^1 sobre la esfera base
    cx = r*np.cos(tt); cy = r*np.sin(tt); cz = np.full_like(tt, t_chi)
    ax.plot(*ortho(cx, cy, cz, az, el), color='#7B85FF', lw=1.2, alpha=0.8)
ax.plot(np.cos(th), -np.sin(th), color='#7B85FF', lw=1.0, ls='--')  # circulo maximo
ax.annotate(r'$ds_3^2=d\chi^2+\sin^2\chi\,ds_2^2$', (0.4, 0.2), xytext=(-2.7, 1.5), fontsize=11,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.text(0, -1.75, r'3D: hiperesfera $S^3$ (cada $\chi$ es una $S^2$)', ha='center', fontsize=10)
ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-2.9,2.0); ax.set_ylim(-2.0,2.0)
fig.tight_layout()
fig.savefig('images/esfera_anidada.svg', bbox_inches='tight')
fig.savefig('images/esfera_anidada.pdf', bbox_inches='tight')
print('OK: esfera_anidada')
