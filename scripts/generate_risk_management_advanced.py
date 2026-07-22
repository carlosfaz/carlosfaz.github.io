"""
Genera la imagen de Gestión de Riesgos Avanzada.
Muestra: distribución de retornos con VaR/CVaR y simulación Monte Carlo.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import gaussian_kde

# Configuración
np.random.seed(42)
n_simulations = 10000
confidence_level = 0.95

# Generar retornos con distribución t de Student (colas gruesas)
df = 4  # grados de libertad para colas gruesas
returns = np.random.standard_t(df, n_simulations) * 0.02  # escala para ~2% daily vol

# Calcular VaR y CVaR históricos
var_95 = np.percentile(returns, (1 - confidence_level) * 100)
cvar_95 = returns[returns <= var_95].mean()

# Crear figura con 2 subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# === Gráfico 1: Distribución de retornos con VaR y CVaR ===
# Histograma
n_bins = 80
ax1.hist(returns, bins=n_bins, density=True, alpha=0.7, color='steelblue', 
         edgecolor='white', label='Distribución Empírica')

# Línea de VaR
ax1.axvline(x=var_95, color='red', linestyle='--', linewidth=3, 
            label=f'VaR 95% = {var_95:.2%}')

# Línea de CVaR
ax1.axvline(x=cvar_95, color='orange', linestyle='-', linewidth=3, 
            label=f'CVaR 95% = {cvar_95:.2%}')

# Ajustar densidad KDE
kde = gaussian_kde(returns)

# Sombrear la cola izquierda (pérdidas extremas)
x_sorted = np.sort(returns)
tail_mask = x_sorted <= var_95
tail_x = x_sorted[tail_mask]
tail_density = kde(tail_x)
ax1.fill_between(tail_x, 0, tail_density, alpha=0.3, color='red')
x_range = np.linspace(returns.min(), returns.max(), 200)
ax1.plot(x_range, kde(x_range), 'k-', linewidth=2, alpha=0.8, label='Densidad KDE')

ax1.set_xlabel('Retornos Diarios', fontsize=16)
ax1.set_ylabel('Densidad', fontsize=16)
ax1.set_title('Value at Risk (VaR) vs Expected Shortfall (CVaR)', fontsize=18, fontweight='bold')
ax1.legend(fontsize=13)
ax1.grid(True, alpha=0.3)
ax1.tick_params(labelsize=12)

# === Gráfico 2: Simulación Monte Carlo ===
# Simular trayectoria de precios
n_days = 252  # 1 año de trading
initial_price = 100
daily_mean = 0.0003  # ~7.5% anual
daily_vol = 0.015    # ~24% anual

# Generar múltiples trayectorias
n_paths = 100
for i in range(n_paths):
    path_returns = np.random.normal(daily_mean, daily_vol, n_days)
    path = initial_price * np.cumprod(1 + path_returns)
    ax2.plot(path, alpha=0.3, linewidth=0.5, color='steelblue')

# Trayectoria destacada (escenario de stress)
np.random.seed(123)
stress_path_returns = np.random.normal(daily_mean, daily_vol * 1.5, n_days)
stress_path_returns[145:155] -= 0.03
stress_path = initial_price * np.cumprod(1 + stress_path_returns)
ax2.plot(stress_path, 'r-', linewidth=3, alpha=0.8, label='Escenario de Stress')

# Calcular drawdown
cummax = np.maximum.accumulate(stress_path)
drawdown = (stress_path - cummax) / cummax
max_drawdown = drawdown.min()

ax2.annotate(f'Máx Drawdown: {max_drawdown:.1%}',
             xy=(np.argmin(stress_path), stress_path.min()),
             xytext=(100, stress_path.min() + 5),
             arrowprops=dict(arrowstyle='->', color='red', lw=3),
             fontsize=14, color='red', fontweight='bold')

ax2.set_xlabel('Días de Trading', fontsize=16)
ax2.set_ylabel('Precio del Activo ($)', fontsize=16)
ax2.set_title('Simulación Monte Carlo con Escenario de Stress', fontsize=18, fontweight='bold')
ax2.legend(fontsize=13)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, n_days)
ax2.tick_params(labelsize=12)

# Nota explicativa al pie de la figura
fig.text(0.5, -0.02, 
         'El CVaR siempre es mayor (más conservador) que el VaR, ya que mide la pérdida promedio en la cola de la distribución.',
         ha='center', fontsize=12, style='italic', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('images/risk-management-advanced.svg', format='svg', bbox_inches='tight')
plt.close()

print("Imagen guardada: images/risk-management-advanced.svg")
print(f"\n=== Resultados de VaR/CVaR ===")
print(f"VaR Histórico (95%): {var_95:.2%}")
print(f"CVaR (Expected Shortfall): {cvar_95:.2%}")
print(f"Ratio CVaR/VaR: {cvar_95/var_95:.2f}x")