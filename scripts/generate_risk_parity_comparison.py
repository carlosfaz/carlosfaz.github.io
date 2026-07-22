"""
Genera la imagen de comparación entre Markowitz (Max Sharpe) y Risk Parity.
Muestra dos gráficos lado a lado: la frontera eficiente y la comparación
de contribución al riesgo entre ambos enfoques.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Configuración
np.random.seed(42)

# Parámetros del mercado (4 activos para claridad visual)
n_assets = 4
risk_free_rate = 0.05

# Retornos esperados anualizados
expected_returns = np.array([0.10, 0.12, 0.08, 0.15])

# Volatilidades anualizadas
volatilities = np.array([0.15, 0.20, 0.10, 0.25])

# Matriz de correlación
correlation_matrix = np.array([
    [1.00, 0.30, 0.20, 0.10],
    [0.30, 1.00, 0.40, 0.20],
    [0.20, 0.40, 1.00, 0.15],
    [0.10, 0.20, 0.15, 1.00]
])

# Matriz de covarianza
cov_matrix = np.outer(volatilities, volatilities) * correlation_matrix

# Función objetivo de Risk Parity
def risk_parity_objective(w, cov):
    pv = np.sqrt(w.T @ cov @ w)
    rc = w * (cov @ w) / pv
    return np.sum((rc - pv / len(w)) ** 2)

# Optimizar Risk Parity
constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
bounds_rp = [(0.01, 0.30)] * n_assets
initial_weights = np.ones(n_assets) / n_assets

result_rp = minimize(
    risk_parity_objective,
    initial_weights,
    args=(cov_matrix,),
    method='SLSQP',
    bounds=bounds_rp,
    constraints=constraints
)

rp_weights = result_rp.x
rp_vol = np.sqrt(rp_weights.T @ cov_matrix @ rp_weights)
rp_return = np.sum(expected_returns * rp_weights)

# Optimizar Markowitz (Max Sharpe)
def neg_sharpe_ratio(weights, expected_returns, cov_matrix, risk_free_rate):
    portfolio_return = np.sum(expected_returns * weights)
    portfolio_vol = np.sqrt(weights.T @ cov_matrix @ weights)
    sharpe = (portfolio_return - risk_free_rate) / (portfolio_vol + 1e-10)
    return -sharpe

bounds_mw = [(0.0, 0.40)] * n_assets
constraints_mw = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}

result_mw = minimize(
    neg_sharpe_ratio,
    initial_weights,
    args=(expected_returns, cov_matrix, risk_free_rate),
    method='SLSQP',
    bounds=bounds_mw,
    constraints=constraints_mw
)

mw_weights = result_mw.x
mw_vol = np.sqrt(mw_weights.T @ cov_matrix @ mw_weights)
mw_return = np.sum(expected_returns * mw_weights)
mw_sharpe = (mw_return - risk_free_rate) / mw_vol

# Calcular contribución al riesgo (TRC) para cada portafolio
def calculate_trc(weights, cov):
    pv = np.sqrt(weights.T @ cov @ weights)
    trc = weights * (cov @ weights) / pv
    return trc, pv

mw_trc, mw_total_vol = calculate_trc(mw_weights, cov_matrix)
rp_trc, rp_total_vol = calculate_trc(rp_weights, cov_matrix)

# Crear figura con 2 subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Gráfico 1: Frontera eficiente con ambos portafolios
n_portfolios = 400
w_mat = np.random.dirichlet(np.ones(n_assets), size=n_portfolios)
frontier_returns = w_mat @ expected_returns
frontier_vols = np.sqrt(np.einsum("ij,jk,ik->i", w_mat, cov_matrix, w_mat))
sharpe_ratios = (frontier_returns - risk_free_rate) / frontier_vols

ax1.scatter(frontier_vols, frontier_returns, c=sharpe_ratios, cmap='viridis', 
            alpha=0.5, s=60, edgecolors='none')
ax1.scatter(mw_vol, mw_return, color='red', s=350, marker='*', 
            edgecolors='black', linewidth=3, zorder=5, label='Markowitz (Max Sharpe)')
ax1.scatter(rp_vol, rp_return, color='blue', s=300, marker='D', 
            edgecolors='black', linewidth=3, zorder=5, label='Risk Parity')
ax1.axhline(y=risk_free_rate, color='gray', linestyle='--', alpha=0.5, label='Tasa Libre de Riesgo')

ax1.set_xlabel('Volatilidad Anualizada ($\sigma_p$)', fontsize=16)
ax1.set_ylabel('Retorno Esperado Anualizado ($E[R_p]$', fontsize=16)
ax1.set_title('Frontera Eficiente: Markowitz vs Risk Parity', fontsize=18, fontweight='bold')
ax1.legend(fontsize=13)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 0.22)
ax1.set_ylim(0.04, 0.15)

# Gráfico 2: Comparación de pesos y contribución al riesgo
x_pos = np.arange(n_assets)
width = 0.35

# Barras de pesos
ax2.bar(x_pos - width/2, mw_weights, width, label='Markowitz Pesos', alpha=0.8, color='red', edgecolor='black', linewidth=1.5)
ax2.bar(x_pos + width/2, rp_weights, width, label='Risk Parity Pesos', alpha=0.8, color='blue', edgecolor='black', linewidth=1.5)

# Líneas de contribución al riesgo objetivo
ax2.axhline(y=rp_total_vol/n_assets, color='blue', linestyle=':', alpha=0.7, 
            label=f'Risk Parity TRC Objetivo ({rp_total_vol/n_assets:.2%})')

ax2.set_xlabel('Activos', fontsize=16)
ax2.set_ylabel('Peso / Contribución al Riesgo', fontsize=16)
ax2.set_title('Distribución de Pesos y Riesgo', fontsize=18, fontweight='bold')
ax2.set_xticks(x_pos)
ax2.set_xticklabels([f'Activo {i+1}\n(σ={v:.0%})' for i, v in enumerate(volatilities)], fontsize=13)
ax2.legend(fontsize=13)
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('images/risk-parity-comparison.svg', format='svg', bbox_inches='tight')
plt.close()

print("Imagen guardada: images/risk-parity-comparison.svg")
print("\n=== Markowitz (Max Sharpe) ===")
print(f"Pesos: {mw_weights}")
print(f"Retorno: {mw_return:.2%}, Volatilidad: {mw_vol:.2%}, Sharpe: {mw_sharpe:.3f}")
print(f"TRC: {mw_trc}")
print(f"% Riesgo por activo: {mw_trc/mw_total_vol*100}")

print("\n=== Risk Parity ===")
print(f"Pesos: {rp_weights}")
print(f"Retorno: {rp_return:.2%}, Volatilidad: {rp_total_vol:.2%}")
print(f"TRC: {rp_trc}")
print(f"Riesgo objetivo por activo: {rp_total_vol/n_assets:.4f}")
print(f"% Riesgo por activo: {rp_trc/rp_total_vol*100}")