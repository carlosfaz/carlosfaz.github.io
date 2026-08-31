import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

# Universos de Friedmann (dominados por materia, Lambda=0) normalizados a max a=1
eta_c = np.linspace(0, 2*np.pi, 400)
a_c = 0.5*(1-np.cos(eta_c)); t_c = 0.5*(eta_c-np.sin(eta_c))     # cerrado k=+1
eta_a = np.linspace(0.01, 6, 400)
a_a = 0.5*(np.cosh(eta_a)-1); t_a = 0.5*(np.sinh(eta_a)-eta_a)  # abierto k=-1
t_f = np.linspace(0, 2.5, 400)
a_f = 1.31*t_f**(2/3)                                            # plano k=0, cte ajustada

fig, ax = plt.subplots(figsize=(6.4, 3.4))
ax.plot(t_c, a_c, color='#d1495b', lw=2.4, label=r'cerrado $k=+1$: nace y recolapsa')
ax.plot(t_a[t_a<=8], a_a[t_a<=8], color='#7B85FF', lw=2.2, label=r'abierto $k=-1$')
ax.plot(t_f, a_f, color='#0b6e4f', lw=2.2, ls='--', label=r'plano $k=0$')
ax.axhline(1, color='#999999', lw=0.8, ls=':')
ax.annotate('cerrado:\nla curvatura lo frena\ny lo hace colapsar', (t_c[-2]-0.4, a_c[-2]), xytext=(1.6, 1.15),
            fontsize=8.5, arrowprops=dict(arrowstyle='->', lw=0.8))
ax.set_xlabel(r'tiempo $t$'); ax.set_ylabel(r'factor de escala $a(t)$')
ax.set_title('Las tres curvaturas, tres destinos', fontsize=10)
ax.legend(loc='lower right', fontsize=8.5)
ax.set_xlim(0, 8); ax.set_ylim(0, 1.6)
fig.tight_layout()
fig.savefig('images/friedmann_curvaturas.svg', bbox_inches='tight')
fig.savefig('images/friedmann_curvaturas.pdf', bbox_inches='tight')
print('OK: friedmann_curvaturas')
