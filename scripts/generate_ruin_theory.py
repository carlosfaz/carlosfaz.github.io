"""
Genera la imagen del artículo sobre Teoría de la Ruina (Cramér-Lundberg).
Panel 1: trayectorias del capital de una aseguradora (rojo = arruinadas).
Panel 2: probabilidad de ruina vs capital inicial: simulación vs fórmula exacta.
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Parámetros del modelo Cramér-Lundberg
lam = 1.0      # Frecuencia de reclamaciones: 1 por unidad de tiempo (Poisson)
mu = 1.0       # Reclamación media: Exp(1)
theta = 0.20   # Carga de seguridad: c = (1 + θ) λμ
c = (1 + theta) * lam * mu   # Prima = 1.2
T = 100        # Horizonte temporal

# Exponente de ajuste de Lundberg: solución de λ(M_X(R) − 1) = cR
# Para X ~ Exp(1): 1/(1−R) − 1 = 1.2R  →  R = 1/6
R_lundberg = 1 - lam * mu / c   # = θ/(1+θ) = 1/6
# Fórmula exacta de la probabilidad de ruina con reclamaciones exponenciales:
def psi_exacta(u):
    return (1 / (1 + theta)) * np.exp(-R_lundberg * u)

# === Simulación por eventos (vectorizada) ===
def simular_ruina(u0, n_sims=5000, max_eventos=200):
    """Simula el capital y estima la probabilidad de ruina antes de T."""
    # Tiempos entre llegadas ~ Exp(λ); tiempos de llegada = suma acumulada
    inter = np.random.exponential(1 / lam, (n_sims, max_eventos))
    tiempos = np.cumsum(inter, axis=1)
    dentro = tiempos <= T                      # solo eventos antes del horizonte

    claims = np.random.exponential(mu, (n_sims, max_eventos)) * dentro
    tiempos_clip = np.minimum(tiempos, T)

    # Capital en cada evento: U(t) = u + c·t − Σ X_i
    capital = u0 + c * tiempos_clip - np.cumsum(claims, axis=1)
    capital[~dentro] = np.inf                  # ignorar eventos fuera de T
    arruinado = np.any(capital < 0, axis=1)
    return arruinado.mean()

# === Panel 1: 60 trayectorias con u = 10 ===
u_demo = 10
n_paths = 60
max_eventos = 200

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

arruinadas = 0
for i in range(n_paths):
    inter = np.random.exponential(1 / lam, max_eventos)
    tiempos = np.cumsum(inter)
    tiempos = tiempos[tiempos <= T]
    claims = np.random.exponential(mu, len(tiempos))
    capital = u_demo + c * tiempos - np.cumsum(claims)

    t_plot = np.concatenate([[0], tiempos])
    u_plot = np.concatenate([[u_demo], capital])
    quebrada = np.any(capital < 0)

    if quebrada:
        arruinadas += 1
        # Recortar en el momento de la quiebra
        idx = np.argmax(capital < 0)
        ax1.step(t_plot[:idx + 1], u_plot[:idx + 1], where='post',
                 color='#d62728', linewidth=2.5, alpha=0.9)
    else:
        ax1.step(t_plot, u_plot, where='post',
                 color='steelblue', linewidth=1, alpha=0.45)

ax1.axhline(y=0, color='black', linewidth=3)
ax1.set_xlabel('Tiempo', fontsize=18)
ax1.set_ylabel('Capital U(t)', fontsize=18)
ax1.set_title(f'60 trayectorias del capital (rojo = ruina, {arruinadas} quebraron)',
              fontsize=20, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.tick_params(labelsize=16)
ax1.set_xlim(0, T)

# === Panel 2: probabilidad de ruina vs capital inicial ===
u_valores = np.array([0, 5, 10, 15, 20, 25, 30])
psi_empirica = np.array([simular_ruina(u) for u in u_valores])

u_fino = np.linspace(0, 30, 200)
ax2.plot(u_fino, psi_exacta(u_fino), 'k--', linewidth=3,
         label=r'Exacta: $\psi(u) = \frac{1}{1.2}\, e^{-u/6}$')
ax2.plot(u_valores, psi_empirica, 'o', color='#d62728', markersize=12,
         markeredgecolor='black', markeredgewidth=1.5, zorder=5,
         label='Simulación Monte Carlo (5,000 por punto)')
ax2.set_xlabel('Capital inicial u', fontsize=18)
ax2.set_ylabel('Probabilidad de ruina $\\psi(u)$', fontsize=18)
ax2.set_title('La teoría acierta: Monte Carlo vs fórmula exacta', fontsize=20, fontweight='bold')
ax2.legend(fontsize=16)
ax2.grid(True, alpha=0.3)
ax2.tick_params(labelsize=16)
ax2.set_ylim(0, 1)

plt.tight_layout()
plt.savefig('images/ruin-theory.svg', format='svg', bbox_inches='tight')
plt.close()

print("Imagen guardada: images/ruin-theory.svg")
print(f"\n=== Teoría de la Ruina (Cramér-Lundberg) ===")
print(f"Prima c = {c}, reclamación media μ = {mu}, frecuencia λ = {lam}")
print(f"Carga de seguridad θ = {theta:.0%}")
print(f"Exponente de ajuste de Lundberg R = {R_lundberg:.4f} (= 1/6)")
print(f"\nψ(10) simulada: {psi_empirica[2]:.3f}  |  ψ(10) exacta: {psi_exacta(10):.3f}")
print(f"ψ(20) simulada: {psi_empirica[4]:.3f}  |  ψ(20) exacta: {psi_exacta(20):.3f}")
