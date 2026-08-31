import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

tau = np.linspace(0.01, 4, 300)
fig, ax = plt.subplots(figsize=(6.2, 4.2))
# lineas de mundo de Milne: rho = r*tau (rectas desde el origen = Minkowski)
for r in [0.1, 0.3, 0.5, 0.7, 0.9, 0.99]:
    ax.plot(tau, r*tau, color='#1f77b4', lw=1.8, alpha=0.85,
            label=None if r<0.9 else r'partículas: $\rho = r\,\tau$')
# cono de luz
ax.plot(tau, tau, color='#d1495b', lw=2.4, label='luz')
ax.plot(tau, -tau, color='#d1495b', lw=2.4)
ax.fill_between([0,4], 0, 4, color='#999999', alpha=0.06)
ax.annotate('rectas desde el origen:\nvelocidad constante\nen Minkowski', (3.0, 2.1), xytext=(0.4, 3.4), fontsize=9,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.set_xlabel(r'tiempo $\tau$'); ax.set_ylabel(r'radio $\rho$')
ax.set_title('El universo de Milne es Minkowski disfrazado', fontsize=10)
ax.set_xlim(0, 4); ax.set_ylim(0, 4)
ax.legend(loc='lower right', fontsize=8.5)
fig.tight_layout()
fig.savefig('images/milne_worldlines.svg', bbox_inches='tight')
fig.savefig('images/milne_worldlines.pdf', bbox_inches='tight')
print('OK: milne_worldlines')
