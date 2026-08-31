import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

eta = np.linspace(0, 4, 200)
fig, ax = plt.subplots(figsize=(6.0, 4.2))
ax.plot(eta, eta, color='#d1495b', lw=2.2, label='rayo de luz')
ax.plot(eta, -eta, color='#d1495b', lw=2.2)
ax.fill_between([-4, 4], 0, 4, color='#999999', alpha=0.06)
ax.axvline(0, color='k', lw=1.0)
ax.plot([3.0,3.0],[0,3.0], color='#0b6e4f', ls='--', lw=2.0)
ax.plot([-3.0,-3.0],[0,3.0], color='#0b6e4f', ls='--', lw=2.0)
ax.annotate('horizonte de\npartículas\n$\\psi=\\eta$', (3.0, 2.2), xytext=(1.7, 3.2), fontsize=8.5,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.annotate('Big Bang\n$\\eta=0$', (0, 0.05), xytext=(-1.5, 0.6), fontsize=8.5,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.annotate('luz a 45°', (2.4, 2.4), xytext=(2.6, 1.4), fontsize=9, color='#d1495b',
            arrowprops=dict(arrowstyle='->', lw=0.8, color='#d1495b'))
ax.set_xlabel(r'distancia comóvil $\psi$')
ax.set_ylabel(r'tiempo conforme $\eta$')
ax.set_title('La luz viaja a 45° en el mapa conforme', fontsize=10)
ax.set_xlim(-4, 4); ax.set_ylim(0, 4)
ax.legend(loc='lower center', fontsize=8.5)
fig.tight_layout()
fig.savefig('images/cono_conforme.svg', bbox_inches='tight')
fig.savefig('images/cono_conforme.pdf', bbox_inches='tight')
print('OK: cono_conforme')
