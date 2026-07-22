import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw

x_range = np.linspace(0.1, 2.0, 500)

def tetration_truncated(x, n):
    if n == 1:
        return x
    else:
        return x ** tetration_truncated(x, n - 1)

orders = [1, 2, 3, 4]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
labels = [f'$^{{{n}}}x$ (orden {n})' for n in orders]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

for i, n in enumerate(orders):
    try:
        y_values = []
        for x in x_range:
            try:
                val = tetration_truncated(x, n)
                if np.isfinite(val) and val < 100:
                    y_values.append(val)
                else:
                    y_values.append(np.nan)
            except (OverflowError, ValueError):
                y_values.append(np.nan)
        
        ax1.plot(x_range, y_values, color=colors[i], linewidth=3, 
                 alpha=0.8, label=labels[i], zorder=5-i)
    except Exception as e:
        print(f"Error calculando orden {n}: {e}")

ax1.set_xlabel('$x$', fontsize=18)
ax1.set_ylabel('piso(n)', fontsize=18)
ax1.set_title('Tetración Truncada: $x^{x^{\\cdot^{\\cdot^x}}}$', fontsize=20, fontweight='bold')
ax1.legend(fontsize=15, loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0.1, 2.0)
ax1.set_ylim(0, 50)
ax1.tick_params(labelsize=13)

note_text = (
    "Nota: Para $x \\in (e^{-e}, e^{1/e}) \\approx (0.066, 1.44)$,\n"
    "la tetración infinita converge. Fuera de este intervalo,\n"
    "los valores crecen extremadamente rápido o divergen."
)
ax1.text(0.98, 0.50, note_text, transform=ax1.transAxes, ha='right', va='center',
         fontsize=13, style='italic',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='wheat', alpha=0.6, edgecolor='orange'))

x_conv = np.linspace(np.exp(-np.e) + 1e-5, np.exp(1/np.e), 400)
h_x = -lambertw(-np.log(x_conv)).real / np.log(x_conv)

ax2.plot(x_conv, h_x, color='purple', linewidth=3.5, label=r'Límite $n \to \infty$ ($h(x)$)')

x_lower, x_upper = np.exp(-np.e), np.exp(1/np.e)
ax2.axvline(x_lower, color='darkred', linestyle='--', linewidth=2, label=f'Límite inf. ($e^{{-e}} \\approx 0.066$)')
ax2.axvline(x_upper, color='darkgreen', linestyle='--', linewidth=2, label=f'Límite sup. ($e^{{1/e}} \\approx 1.445$)')

ax2.axvspan(x_lower, x_upper, color='green', alpha=0.1)

ax2.set_xlabel('$x$', fontsize=18)
ax2.set_ylabel(r'$h(x) = x^{x^{x^{\cdot^{\cdot^{\cdot}}}}}$', fontsize=18)
ax2.set_title('Límite Infinito de la Torre de Potencias', fontsize=20, fontweight='bold')
ax2.legend(fontsize=13, loc='upper left')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0.0, 2.0)
ax2.set_ylim(0, 4)
ax2.tick_params(labelsize=13)

plt.tight_layout()
plt.savefig('images/tetration-truncated.svg', format='svg', bbox_inches='tight')
plt.close()

print("Imagen guardada: images/tetration-truncated.svg")