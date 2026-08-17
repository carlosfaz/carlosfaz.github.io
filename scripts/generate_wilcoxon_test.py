"""
Genera la imagen del artículo sobre la prueba de rangos con signo de Wilcoxon.
Panel 1: puntuaciones antes/después por participante (slope graph).
Panel 2: diferencias ordenadas por magnitud con su rango (verde = positiva, roja = negativa).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rankdata, wilcoxon, norm

np.random.seed(42)

# 12 participantes: puntuación antes y después de un programa de entrenamiento
n = 12
antes = np.array([68, 74, 71, 65, 80, 77, 69, 73, 66, 78, 72, 70], dtype=float)
# Mejoras mayormente positivas, con una mejora atípica enorme (rompe la normalidad)
mejoras = np.array([5, 8, 3, 6, -2, 7, 4, 25, 6, -1, 9, 5], dtype=float)
despues = antes + mejoras

diferencias = despues - antes

# === Cálculo MANUAL de Wilcoxon (para mostrar el procedimiento) ===
no_cero = diferencias[diferencias != 0]
abs_dif = np.abs(no_cero)
rangos = rankdata(abs_dif)              # rangos de las magnitudes
signos = np.sign(no_cero)
W_pos = np.sum(rangos[signos > 0])      # suma de rangos positivos
W_neg = np.sum(rangos[signos < 0])      # suma de rangos negativos
W_stat = min(W_pos, W_neg)

# Aproximación normal
m = len(no_cero)
mu_W = m * (m + 1) / 4
sigma_W = np.sqrt(m * (m + 1) * (2 * m + 1) / 24)
z = (W_stat - mu_W) / sigma_W
p_aprox = 2 * norm.cdf(z)

# === Verificación con scipy ===
result = wilcoxon(despues, antes)
p_scipy = result.pvalue

# ================= FIGURA =================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Panel 1: slope graph antes -> después
x = [0, 1]
for i in range(n):
    color = '#2ca02c' if mejoras[i] > 0 else '#d62728'
    ax1.plot(x, [antes[i], despues[i]], marker='o', markersize=8,
             linewidth=2, color=color, alpha=0.75)
ax1.set_xlim(-0.3, 1.3)
ax1.set_xticks(x)
ax1.set_xticklabels(['Antes', 'Después'], fontsize=18)
ax1.set_ylabel('Puntuación', fontsize=18)
ax1.set_title('Cada línea es un participante', fontsize=20, fontweight='bold')
ax1.grid(True, alpha=0.3, axis='y')
ax1.tick_params(labelsize=16)

# Panel 2: diferencias ordenadas por magnitud con rangos
orden = np.argsort(abs_dif)
dif_ord = no_cero[orden]
rangos_ord = np.arange(1, m + 1)
colores = ['#2ca02c' if d > 0 else '#d62728' for d in dif_ord]

bars = ax2.bar(rangos_ord, dif_ord, color=colores, alpha=0.85,
               edgecolor='black', linewidth=1.2)
ax2.axhline(y=0, color='black', linewidth=1)
ax2.set_xlabel('Rango (orden por magnitud |d|)', fontsize=18)
ax2.set_ylabel('Diferencia (después − antes)', fontsize=18)
ax2.set_title('Los rangos llevan el signo de la diferencia', fontsize=20, fontweight='bold')
ax2.set_xticks(rangos_ord)
ax2.grid(True, alpha=0.3, axis='y')
ax2.tick_params(labelsize=14)

# Etiqueta del outlier
idx_max = np.argmax(abs_dif)
ax2.annotate('¡El outlier!\n(magnitud 25, rango máximo)',
             xy=(rangos_ord[-1], dif_ord[-1]),
             xytext=(rangos_ord[-1] - 4.5, dif_ord[-1] - 3),
             arrowprops=dict(arrowstyle='->', color='black', lw=2),
             fontsize=15, fontweight='bold')

plt.tight_layout()
plt.savefig('images/wilcoxon-signed-rank.svg', format='svg', bbox_inches='tight')
plt.close()

print("Imagen guardada: images/wilcoxon-signed-rank.svg")
print(f"\n=== Wilcoxon (cálculo manual) ===")
print(f"Diferencias: {diferencias.astype(int).tolist()}")
print(f"W+ (rangos positivos) = {W_pos}")
print(f"W− (rangos negativos) = {W_neg}")
print(f"W = min(W+, W−) = {W_stat}")
print(f"Aproximación normal: z = {z:.3f}, p ≈ {p_aprox:.4f}")
print(f"\n=== Verificación scipy ===")
print(f"scipy.stats.wilcoxon: W = {result.statistic}, p-valor = {p_scipy:.4f}")
print(f"Mediana antes: {np.median(antes):.1f} | Mediana después: {np.median(despues):.1f}")
