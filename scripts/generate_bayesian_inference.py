"""
Genera la imagen del artículo sobre Estadística Bayesiana.
Panel 1: prior y posteriors Beta-Binomial conforme llegan datos (moneda sesgada).
Panel 2: la paradoja del test médico (falacia del fiscal) en una población de 100,000.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

np.random.seed(42)

# ================= Panel 1: Beta-Binomial =================
# Moneda con sesgo verdadero p = 0.70 hacia cara
p_true = 0.70
theta = np.linspace(0, 1, 500)

# Prior: Beta(2, 2) — "creo que es justa, pero no estoy seguro"
a0, b0 = 2, 2

# Datos acumulados (70% caras): (lanzamientos, caras)
observations = [(10, 7), (50, 35), (200, 140)]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

ax1.plot(theta, beta.pdf(theta, a0, b0), linewidth=3, color='#7f7f7f',
         linestyle='--', label=f'Prior: Beta({a0}, {b0})')

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for (n, k), color in zip(observations, colors):
    a_post, b_post = a0 + k, b0 + (n - k)
    ax1.plot(theta, beta.pdf(theta, a_post, b_post), linewidth=3, color=color,
             label=f'Posterior: Beta({a_post}, {b_post})  ({k}/{n} caras)')

ax1.axvline(x=p_true, color='red', linestyle='-', linewidth=2.5, alpha=0.8,
            label=f'Sesgo verdadero p = {p_true}')
ax1.set_xlabel('Probabilidad de cara ($\\theta$)', fontsize=18)
ax1.set_ylabel('Densidad', fontsize=18)
ax1.set_title('La posterior se concentra con más datos', fontsize=20, fontweight='bold')
ax1.legend(fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.tick_params(labelsize=16)
ax1.set_xlim(0, 1)

# ================= Panel 2: la paradoja del test médico =================
# Enfermedad: prevalencia 1%; test: sensibilidad 99%, falsos positivos 5%
poblacion = 100_000
enfermos = int(poblacion * 0.01)              # 1,000
sanos = poblacion - enfermos                  # 99,000
verdaderos_pos = int(enfermos * 0.99)         # 990
falsos_pos = int(sanos * 0.05)                # 4,950
p_enfermo_dado_pos = verdaderos_pos / (verdaderos_pos + falsos_pos)

categorias = ['Verdaderos\npositivos', 'Falsos\npositivos']
valores = [verdaderos_pos, falsos_pos]
bars = ax2.bar(categorias, valores, color=['#2ca02c', '#d62728'],
               alpha=0.85, edgecolor='black', linewidth=1.5, width=0.5)

for bar, val in zip(bars, valores):
    ax2.text(bar.get_x() + bar.get_width() / 2, val + 120,
             f'{val:,}', ha='center', fontsize=20, fontweight='bold')

ax2.set_ylabel('Personas (de cada 100,000)', fontsize=18)
ax2.set_title(f'¡Test positivo! P(enfermo | +) = {p_enfermo_dado_pos:.1%}',
              fontsize=20, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')
ax2.tick_params(labelsize=16)
ax2.set_ylim(0, max(valores) * 1.18)

plt.tight_layout()
plt.savefig('images/bayesian-inference.svg', format='svg', bbox_inches='tight')
plt.close()

print("Imagen guardada: images/bayesian-inference.svg")
print(f"\n=== Paradoja del test médico ===")
print(f"Prevalencia 1%, sensibilidad 99%, tasa de falsos positivos 5%")
print(f"Verdaderos positivos: {verdaderos_pos:,}")
print(f"Falsos positivos: {falsos_pos:,}")
print(f"P(enfermo | test positivo) = {verdaderos_pos}/{verdaderos_pos + falsos_pos} = {p_enfermo_dado_pos:.1%}")
print(f"\n=== Beta-Binomial ===")
for (n, k) in observations:
    a_post, b_post = a0 + k, b0 + (n - k)
    print(f"Tras {n} lanzamientos ({k} caras): posterior Beta({a_post},{b_post}), media = {a_post/(a_post+b_post):.3f}")
