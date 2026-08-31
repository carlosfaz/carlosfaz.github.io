import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

GM = 1.0
r = np.linspace(0.6, 5, 500)
f = 1 - 2*GM/r
fig, ax = plt.subplots(figsize=(6.6, 3.6))
ax.plot(r, f, color='#0b6e4f', lw=2.5, label=r'$-g_{tt}=g^{rr}=1-2GM/r$')
ax.plot(r, 1/f, color='#d1495b', lw=2.2, label=r'$g_{rr}=1/(1-2GM/r)$')
ax.axvline(2, color='k', ls='--', lw=1.4)
ax.axhline(0, color='k', lw=0.8)
ax.axvspan(0.6, 2, color='#d1495b', alpha=0.08)
ax.annotate('horizonte $r=2GM$\nlos papeles se intercambian', (2, 1.5), xytext=(2.6, 2.1), fontsize=8.5,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.annotate('interior\n($r$ es tiempo)', (1.3, 3.4), fontsize=9, ha='center', color='#d1495b')
ax.text(4.6, 2.0, 'exterior\n($t$ es tiempo)', fontsize=9, ha='center', color='#0b6e4f')
ax.set_xlabel(r'radio $r$'); ax.set_ylabel(r'coeficientes')
ax.set_title('Dentro del agujero negro, tiempo y espacio se dan la mano', fontsize=10)
ax.legend(loc='lower right', fontsize=8.5)
ax.set_xlim(0.6, 5); ax.set_ylim(-3, 5)
fig.tight_layout()
fig.savefig('images/schwarzschild_swap.svg', bbox_inches='tight')
fig.savefig('images/schwarzschild_swap.pdf', bbox_inches='tight')
print('OK: schwarzschild_swap')
