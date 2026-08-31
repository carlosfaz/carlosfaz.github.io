import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

t = np.linspace(0.001, 3.0, 500)
fig, ax = plt.subplots(figsize=(6.2, 3.2))
ax.plot(t, np.exp(t)-1, color='#d1495b', lw=2.4, label=r'de Sitter: $d_p=e^t-1$')
ax.plot(t, t/0.5, color='#0b6e4f', lw=2.2, label=r'polvo, $\alpha=1/2$: $d_p=2t$')
ax.plot(t, t*np.log(t/0.001), color='#555555', lw=2.2, ls='--', label=r'$\alpha=1$: $d_p=t\ln t$')
ax.set_xlabel(r'$t$'); ax.set_ylabel(r'$d_p(t)$')
ax.set_title('El horizonte: quien se deja alcanzar por la luz', fontsize=10)
ax.legend(loc='upper left', fontsize=8.5)
ax.set_xlim(0, 3)
fig.tight_layout()
fig.savefig('images/horizonte_de_sitter.svg', bbox_inches='tight')
fig.savefig('images/horizonte_de_sitter.pdf', bbox_inches='tight')
print('OK: horizonte_de_sitter')
