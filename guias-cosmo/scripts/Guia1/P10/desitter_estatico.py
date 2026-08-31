import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

H = 1.0
r = np.linspace(0.01, 2.2, 500)
f = 1-H**2*r**2
fig, ax = plt.subplots(figsize=(6.6, 3.6))
ax.plot(r, -f, color='#0b6e4f', lw=2.5, label=r'$-g_{tt}=1-H^2r^2$')
ax.plot(r, 1/f, color='#d1495b', lw=2.2, label=r'$g_{rr}=1/(1-H^2r^2)$')
ax.axvline(1, color='k', ls='--', lw=1.4)
ax.axhline(0, color='k', lw=0.8)
ax.axvspan(1, 2.2, color='#d1495b', alpha=0.08)
ax.annotate('horizonte $r=\\sqrt{3/\\Lambda}$\nla luz se congela', (1, 2.5), xytext=(0.25, 3.4), fontsize=8.5,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.text(0.5, 3.6, 'accesible', fontsize=9, ha='center', color='#0b6e4f')
ax.text(1.75, 3.6, 'perdida', fontsize=9, ha='center', color='#d1495b')
ax.set_xlabel(r'radio $r$'); ax.set_ylabel(r'coeficientes')
ax.set_title('de Sitter estático: la \"prisión de luz\" según la constante cosmológica', fontsize=10)
ax.legend(loc='lower center', fontsize=8.5)
ax.set_xlim(0, 2.2); ax.set_ylim(-3, 5)
fig.tight_layout()
fig.savefig('images/desitter_estatico.svg', bbox_inches='tight')
fig.savefig('images/desitter_estatico.pdf', bbox_inches='tight')
print('OK: desitter_estatico')
