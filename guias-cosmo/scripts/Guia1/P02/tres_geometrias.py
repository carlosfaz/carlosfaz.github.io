import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

r = np.linspace(0, 1.6, 400)
fig, ax = plt.subplots(figsize=(6.2, 3.2))
ax.axhline(1.0, ls='--', color='#888888', lw=1.2, label=r'Plano: $g_{rr}=1$')
rs = np.linspace(0, 0.999, 400)
ax.plot(rs, 1/(1-rs**2), color='#d1495b', lw=2.4, label=r'Esfera: $g_{rr}=1/(1-r^2)$')
ax.plot(r, 1/(1+r**2), color='#0b6e4f', lw=2.4, label=r'Lobachevsky: $g_{rr}=1/(1+r^2)$')
ax.set_xlabel(r'$r$'); ax.set_ylabel(r'$g_{rr}$')
ax.set_title('Cómo \"pesa\" el radio en cada geometría', fontsize=10)
ax.set_ylim(0, 5)
ax.legend(loc='upper left', fontsize=8.5)
fig.tight_layout()
fig.savefig('images/tres_geometrias.svg', bbox_inches='tight')
fig.savefig('images/tres_geometrias.pdf', bbox_inches='tight')
print('OK: tres_geometrias')
