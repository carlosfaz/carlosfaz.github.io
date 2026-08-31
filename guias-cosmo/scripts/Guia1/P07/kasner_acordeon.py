import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9.5,"axes.spines.top":False,"axes.spines.right":False})
plt.rcParams["mathtext.fontset"]="dejavusans"
os.makedirs("images", exist_ok=True)

t = np.linspace(0.5, 4, 300)
# caso conocido: (2/3, 2/3, -1/3)
ax_x = t**(2/3); ax_z = t**(-1/3); vol = t
fig, ax = plt.subplots(figsize=(6.4, 3.4))
ax.plot(t, ax_x, color='#0b6e4f', lw=2.4, label=r'$a_x=a_y=t^{2/3}$ (se expanden)')
ax.plot(t, ax_z, color='#d1495b', lw=2.4, label=r'$a_z=t^{-1/3}$ (se contrae)')
ax.plot(t, vol, color='#7B85FF', lw=2.2, ls='--', label=r'volumen $V=a_x a_y a_z=t$')
ax.set_xlabel(r'tiempo $t$'); ax.set_ylabel(r'escalas')
ax.set_title('El \"acordeón\" de Kasner: dos ejes crecen, uno colapsa', fontsize=10)
ax.legend(loc='upper left', fontsize=8.5)
ax.set_xlim(0.5, 4)
fig.tight_layout()
fig.savefig('images/kasner_acordeon.svg', bbox_inches='tight')
fig.savefig('images/kasner_acordeon.pdf', bbox_inches='tight')
print('OK: kasner_acordeon')
