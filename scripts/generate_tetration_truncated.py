"""
Genera la imagen de Tetración Truncada.
Muestra: la función piso(n) para diferentes valores de n,
y una visualización de la torre de potencias.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.patches as patches

# Configuración
x_range = np.linspace(0.1, 2.0, 500)

# Función de tetración truncada (piso)
def tetration_truncated(x, n):
    """
    Calcula la tetración truncada de orden n: x^x^...^x (n veces)
    piso(1) = x
    piso(2) = x^x
    piso(3) = x^(x^x)
    """
    if n == 1:
        return x
    else:
        return x ** tetration_truncated(x, n - 1)

# Calcular valores para diferentes órdenes
orders = [1, 2, 3, 4]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
labels = [f'$^{{{n}}}x$ (orden {n})' for n in orders]

# Crear figura con 2 subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# === Gráfico 1: Funciones de tetración truncada ===
for i, n in enumerate(orders):
    try:
        y_values = []
        for x in x_range:
            try:
                val = tetration_truncated(x, n)
                # Limitar valores extremos para visualización
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

# Añadir nota sobre convergencia debajo del título
note_text = (
    "Nota: Para $x \\in (e^{-e}, e^{1/e}) \\approx (0.066, 1.44)$, \n"
    "la tetración infinita converge. Fuera de este intervalo, \n"
    "los valores crecen extremadamente rápido o divergen."
)
ax1.text(0.5, 0.92, note_text, transform=ax1.transAxes, ha='left', va='top',
         fontsize=10, style='italic',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# === Gráfico 2: Diagrama de la estructura recursiva ===
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

# Dibujar la torre de potencias para n=4
tower_text = [
    (5, 8.5, r'$x$', 'Orden 4: $x^{x^{x^x}}$'),
    (5, 7.0, r'$x^x$', 'Orden 3: $x^{x^x}$'),
    (5, 5.5, r'$x^{x^x}$', 'Orden 2: $x^x$'),
    (5, 4.0, r'$x^{x^{x^x}}$', 'Orden 1: $x$'),
]

# Caja de definición recursiva
def_box = FancyBboxPatch((1.5, 2.0), 7, 1.5,
                         boxstyle="round,pad=0.1,rounding_size=0.2",
                         linewidth=2, edgecolor='navy', facecolor='lightblue', alpha=0.5)
ax2.add_patch(def_box)
ax2.text(5, 2.75, r'piso(n) = x^piso(n-1)', 
         fontsize=16, ha='center', va='center', fontweight='bold', color='navy')
ax2.text(5, 2.3, r'con piso(1) = x', 
         fontsize=14, ha='center', va='center', style='italic', color='navy')

# Flechas de recursión
for i in range(len(tower_text) - 1):
    ax2.annotate('', xy=(5, tower_text[i+1][1] + 0.4), 
                 xytext=(5, tower_text[i][1] - 0.3),
                 arrowprops=dict(arrowstyle='->', color='red', lw=3))
    ax2.text(5.5, (tower_text[i][1] + tower_text[i+1][1]) / 2,
             f'$x^{{(\\cdot)}}$', fontsize=14, color='red', 
             va='center', fontweight='bold')

# Dibujar nodos de la torre
for i, (x, y, text, label) in enumerate(tower_text):
    # Caja para cada nivel
    box = FancyBboxPatch((x - 1.5, y - 0.4), 3, 0.8,
                         boxstyle="round,pad=0.1,rounding_size=0.1",
                         linewidth=2, edgecolor=colors[i % len(colors)], 
                         facecolor='white', alpha=0.9)
    ax2.add_patch(box)
    ax2.text(x, y, text, fontsize=16, ha='center', va='center', 
             color=colors[i % len(colors)], fontweight='bold')
    ax2.text(x, y - 0.7, label, fontsize=12, ha='center', va='center', 
             color='gray', style='italic')

ax2.set_title('Estructura Recursiva de la Tetración Truncada', 
              fontsize=20, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('images/tetration-truncated.svg', format='svg', bbox_inches='tight')
plt.close()

print("Imagen guardada: images/tetration-truncated.svg")

# Imprimir algunos valores de ejemplo
print("\n=== Valores de ejemplo de la tetración truncada ===")
x_test = 1.5
for n in orders:
    try:
        val = tetration_truncated(x_test, n)
        print(f"piso({n}) en x={x_test}: {val:.4f}")
    except:
        print(f"piso({n}) en x={x_test}: Overflow")