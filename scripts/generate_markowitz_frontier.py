"""
Genera la imagen de la Frontera Eficiente de Markowitz.
Esta imagen muestra la frontera eficiente con portafolios aleatorios,
el portafolio de máximo Sharpe y la tasa libre de riesgo.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Configuración de semillas para reproducibilidad
np.random.seed(42)

# Parámetros del mercado (5 activos)
n_assets = 5
risk_free_rate = 0.05

# Retornos esperados anualizados (10%, 12%, 8%, 15%, 6%)
expected_returns = np.array([0.10, 0.12, 0.08, 0.15, 0.06])

# Volatilidades anualizadas (15%, 20%, 10%, 25%, 8%)
volatilities = np.array([0.15, 0.20, 0.10, 0.25, 0.08])

# Matriz de correlación
correlation_matrix = np.array([
    [1.00, 0.30, 0.20, 0.10, 0.05],
    [0.30, 1.00, 0.40, 0.20, 0.10],
    [0.20, 0.40, 1.00, 0.15, 0.05],
    [0.10, 0.20, 0.15, 1.00, 0.20],
    [0.05, 0.10, 0.05, 0.20, 1.00]
])

# Matriz de covarianza anualizada
cov_matrix = np.outer(volatilities, volatilities) * correlation_matrix

# Función para calcular el ratio de Sharpe negativo
def neg_sharpe_ratio(weights, expected_returns, cov_matrix, risk_free_rate):
    portfolio_return = np.sum(expected_returns * weights)
    portfolio_vol = np.sqrt(weights.T @ cov_matrix @ weights)
    sharpe = (portfolio_return - risk_free_rate) / (portfolio_vol + 1e-10)
    return -sharpe

# Optimizar portafolio de máximo Sharpe
n_assets = len(expected_returns)
constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
bounds = tuple((0.0, 0.40) for _ in range(n_assets))
initial_weights = np.ones(n_assets) / n_assets

result = minimize(
    neg_sharpe_ratio,
    initial_weights,
    args=(expected_returns, cov_matrix, risk_free_rate),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)

optimal_weights = result.x
optimal_return = np.sum(expected_returns * optimal_weights)
optimal_vol = np.sqrt(optimal_weights.T @ cov_matrix @ optimal_weights)
optimal_sharpe = (optimal_return - risk_free_rate) / optimal_vol

# Generar portafolios aleatorios para la frontera
n_portfolios = 500
w_mat = np.random.dirichlet(np.ones(n_assets), size=n_portfolios)
frontier_returns = w_mat @ expected_returns
frontier_vols = np.sqrt(np.einsum("ij,jk,ik->i", w_mat, cov_matrix, w_mat))
sharpe_ratios = (frontier_returns - risk_free_rate) / frontier_vols

# Crear la figura
fig, ax = plt.subplots(figsize=(14, 10))

# Scatter de portafolios aleatorios coloreados por Sharpe
scatter = ax.scatter(frontier_vols, frontier_returns, c=sharpe_ratios,
                     cmap='viridis', alpha=0.6, s=80, edgecolors='none')

# Portafolio de máximo Sharpe
ax.scatter(optimal_vol, optimal_return, color='red', s=400, 
           marker='*', edgecolors='black', linewidth=3, zorder=5, label='Máximo Sharpe')

# Línea de la tasa libre de riesgo
ax.axhline(y=risk_free_rate, color='gray', linestyle='--', alpha=0.7, label=f'Tasa Libre de Riesgo ({risk_free_rate*100}%)')

# Línea del Capital Allocation Line (CAL)
vol_range = np.linspace(0, 0.25, 100)
cal = risk_free_rate + optimal_sharpe * vol_range
ax.plot(vol_range, cal, 'r-', alpha=0.5, linewidth=2, label='Capital Allocation Line')

# Configurar el gráfico
ax.set_xlabel('Volatilidad Anualizada ($\sigma_p$)', fontsize=18)
ax.set_ylabel('Retorno Esperado Anualizado ($E[R_p]$)', fontsize=18)
ax.set_title('Frontera Eficiente de Markowitz\nOptimización Moderna de Portafolios', fontsize=22, fontweight='bold')
ax.legend(fontsize=16, loc='upper left')
ax.grid(True, alpha=0.3)

# Agregar barra de color
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Ratio de Sharpe', fontsize=16)
cbar.ax.tick_params(labelsize=14)

# Límites
ax.set_xlim(0, 0.25)
ax.set_ylim(0.02, 0.16)

plt.tight_layout()
plt.savefig('images/markowitz-frontier.svg', format='svg', bbox_inches='tight')
plt.close()

print("Imagen guardada: images/markowitz-frontier.svg")
print(f"Portafolio óptimo de máximo Sharpe:")
print(f"  Retorno: {optimal_return:.2%}")
print(f"  Volatilidad: {optimal_vol:.2%}")
print(f"  Sharpe: {optimal_sharpe:.3f}")
print(f"  Pesos: {optimal_weights}")