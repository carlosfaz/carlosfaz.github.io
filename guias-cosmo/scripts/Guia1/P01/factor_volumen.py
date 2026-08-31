import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

theta = np.linspace(0, np.pi, 400)
fig, ax = plt.subplots(figsize=(6.4, 3.1))
ax.plot(np.degrees(theta), np.sin(theta), color='#0b6e4f', lw=2.4)
ax.fill_between(np.degrees(theta), np.sin(theta), color='#0b6e4f', alpha=0.10)
ax.axvline(90, color='#d1495b', ls='--', lw=1.1)
ax.axvline(15, color='#d1495b', ls='--', lw=1.1)
ax.annotate('ecuador: celdas grandes\n(sin θ = 1)', (90, 0.5), xytext=(100, 0.62), fontsize=8.5,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.annotate('polos: celdas encogidas\n(sin θ -> 0)', (15, 0.26), xytext=(30, 0.12), fontsize=8.5,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.set_xlabel(r'ángulo polar $\theta$ (grados)')
ax.set_ylabel(r'$\sin\theta$')
ax.set_title(r'El corrector de volumen $\sqrt{|\det\eta|}=r^2 \sin\theta$', fontsize=10)
ax.set_xlim(0, 180); ax.set_ylim(0, 1.1)
fig.tight_layout()
fig.savefig('images/factor_volumen.svg', bbox_inches='tight')
fig.savefig('images/factor_volumen.pdf', bbox_inches='tight')
print('OK: factor_volumen')
