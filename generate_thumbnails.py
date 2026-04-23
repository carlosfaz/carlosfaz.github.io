#!/usr/bin/env python3
"""
Script para generar thumbnails temáticos para los posts del blog.
Crea gráficos relacionados con el contenido de cada post.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
from matplotlib.lines import Line2D
import matplotlib.patches as patches
from scipy import stats
import os

# Crear directorio de imágenes si no existe
os.makedirs('images', exist_ok=True)

# Configuración de estilo
plt.style.use('default')
COLORS = {
    'primary': '#2c3e50',
    'secondary': '#3498db',
    'accent': '#e74c3c',
    'success': '#27ae60',
    'warning': '#f39c12',
    'bg': '#ecf0f1',
    'dark': '#1a252f'
}

def generate_markowitz_thumbnail():
    """
    Genera thumbnail para el post de Frontera Eficiente de Markowitz.
    Muestra la clásica gráfica de frontera eficiente con portafolios.
    """
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
    
    # Generar datos para la frontera eficiente
    np.random.seed(42)
    n_assets = 5
    
    # Retornos y volatilidades simuladas
    returns = np.array([0.08, 0.12, 0.15, 0.10, 0.18])
    vols = np.array([0.10, 0.15, 0.20, 0.12, 0.25])
    correlation = 0.3
    cov_matrix = np.outer(vols, vols) * correlation
    np.fill_diagonal(cov_matrix, vols**2)
    
    # Generar portafolios aleatorios
    n_portfolios = 500
    weights = np.random.dirichlet(np.ones(n_assets), n_portfolios)
    
    portfolio_returns = weights @ returns
    portfolio_vols = np.sqrt(np.einsum('ij,jk,ik->i', weights, cov_matrix, weights))
    
    # Scatter de portafolios aleatorios
    ax.scatter(portfolio_vols, portfolio_returns, c='lightblue', alpha=0.3, s=20, zorder=1)
    
    # Encontrar y destacar la frontera eficiente
    for i in range(len(portfolio_vols)):
        is_efficient = True
        for j in range(len(portfolio_vols)):
            if portfolio_vols[j] <= portfolio_vols[i] and portfolio_returns[j] > portfolio_returns[i]:
                is_efficient = False
                break
        if is_efficient:
            ax.scatter(portfolio_vols[i], portfolio_returns[i], c='#e74c3c', s=30, alpha=0.8, zorder=2)
    
    # Destacar el portafolio de máximo Sharpe
    risk_free_rate = 0.05
    sharpe_ratios = (portfolio_returns - risk_free_rate) / portfolio_vols
    max_sharpe_idx = np.argmax(sharpe_ratios)
    ax.scatter(portfolio_vols[max_sharpe_idx], portfolio_returns[max_sharpe_idx], 
              c='#27ae60', s=150, marker='*', edgecolors='black', linewidth=1.5, 
              zorder=3, label='Max Sharpe')
    
    # Dibujar línea de tasa libre de riesgo
    ax.axhline(y=risk_free_rate, color='gray', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(0.005, risk_free_rate + 0.005, 'Rf', fontsize=10, color='gray')
    
    # Línea de asignación de capital (CAL)
    x_line = np.array([0, 0.35])
    y_line = risk_free_rate + sharpe_ratios[max_sharpe_idx] * x_line
    ax.plot(x_line, y_line, 'g--', alpha=0.6, linewidth=2)
    
    # Configuración de ejes
    ax.set_xlabel('Riesgo (Volatilidad σ)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Retorno Esperado E[R]', fontsize=11, fontweight='bold')
    ax.set_title('Frontera Eficiente de Markowitz', fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 0.25)
    ax.set_ylim(0.04, 0.20)
    
    plt.tight_layout()
    plt.savefig('images/markowitz-frontier.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Generada: images/markowitz-frontier.png")


def generate_riskparity_thumbnail():
    """
    Genera thumbnail para el post de Paridad de Riesgo (Risk Parity).
    Muestra un gráfico de barras comparando contribución al riesgo.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), dpi=150)
    
    np.random.seed(42)
    n_assets = 6
    asset_labels = ['Acciones\nEEUU', 'Acciones\nIntl', 'Bonos\nGob', 'Bonos\nCorp', 'Commodities', 'Real Estate']
    
    # Simular contribuciones al riesgo - Markowitz (desequilibrado)
    markowitz_risk_contrib = np.array([0.45, 0.25, 0.08, 0.10, 0.07, 0.05])
    
    # Simular contribuciones al riesgo - Risk Parity (equilibrado)
    risk_parity_risk_contrib = np.array([0.167, 0.167, 0.167, 0.167, 0.166, 0.166])
    
    # Colores
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']
    x_pos = np.arange(n_assets)
    
    # Gráfico 1: Markowitz (desequilibrado)
    ax1 = axes[0]
    bars1 = ax1.bar(x_pos, markowitz_risk_contrib * 100, color=colors, edgecolor='white', linewidth=1.5)
    ax1.axhline(y=100/n_assets, color='red', linestyle='--', alpha=0.5, linewidth=1.5, label=f'Objetivo ({100/n_assets:.1f}%)')
    ax1.set_title('Markowitz: Riesgo Desequilibrado', fontsize=12, fontweight='bold', pad=10)
    ax1.set_ylabel('Contribución al Riesgo (%)', fontsize=10)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(asset_labels, fontsize=8)
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.set_ylim(0, 55)
    
    # Añadir etiquetas de porcentaje
    for bar, val in zip(bars1, markowitz_risk_contrib):
        ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                f'{val*100:.0f}%', ha='center', va='bottom', fontsize=8, fontweight='bold')
    
    # Gráfico 2: Risk Parity (equilibrado)
    ax2 = axes[1]
    bars2 = ax2.bar(x_pos, risk_parity_risk_contrib * 100, color=colors, edgecolor='white', linewidth=1.5)
    ax2.axhline(y=100/n_assets, color='red', linestyle='--', alpha=0.5, linewidth=1.5, label=f'Objetivo ({100/n_assets:.1f}%)')
    ax2.set_title('Risk Parity: Riesgo Equilibrado', fontsize=12, fontweight='bold', pad=10)
    ax2.set_ylabel('Contribución al Riesgo (%)', fontsize=10)
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(asset_labels, fontsize=8)
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.set_ylim(0, 55)
    
    # Añadir etiquetas de porcentaje
    for bar, val in zip(bars2, risk_parity_risk_contrib):
        ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                f'{val*100:.0f}%', ha='center', va='bottom', fontsize=8, fontweight='bold')
    
    plt.suptitle('Comparación: Distribución de Contribución al Riesgo', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('images/risk-parity-comparison.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Generada: images/risk-parity-comparison.png")


def generate_riskmanagement_thumbnail():
    """
    Genera thumbnail para el post de Gestión de Riesgos Avanzada.
    Muestra distribución de retornos con VaR y CVaR.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), dpi=150)
    
    np.random.seed(42)
    
    # Generar distribución de retornos (con colas pesadas)
    n_samples = 10000
    returns = np.random.normal(0.0005, 0.02, n_samples)
    # Añadir algunas colas pesadas
    returns[np.random.random(n_samples) < 0.02] *= 3
    
    # Calcular VaR y CVaR
    confidence_level = 0.95
    var_level = (1 - confidence_level) * 100
    var_value = np.percentile(returns, var_level)
    cvar_value = returns[returns <= var_value].mean()
    
    # Gráfico 1: Distribución con VaR y CVaR
    ax1 = axes[0]
    n, bins, patches = ax1.hist(returns, bins=100, density=True, alpha=0.7, 
                                 color='#3498db', edgecolor='none', label='Distribución de Retornos')
    
    # Línea VaR
    ax1.axvline(x=var_value, color='#e74c3c', linestyle='-', linewidth=2.5, 
                label=f'VaR ({confidence_level*100:.0f}%): {var_value:.2%}')
    
    # Línea CVaR
    ax1.axvline(x=cvar_value, color='#27ae60', linestyle='--', linewidth=2.5, 
                label=f'CVaR: {cvar_value:.2%}')
    
    # Sombrear región de cola
    x_fill = np.linspace(var_value - 0.02, var_value, 50)
    y_fill = np.interp(x_fill, bins[:-1], n)
    ax1.fill_between(x_fill, 0, y_fill, alpha=0.3, color='#e74c3c')
    
    ax1.set_xlabel('Retorno', fontsize=11)
    ax1.set_ylabel('Densidad de Probabilidad', fontsize=11)
    ax1.set_title('Value at Risk (VaR) y Expected Shortfall (CVaR)', fontsize=12, fontweight='bold', pad=10)
    ax1.legend(fontsize=9, loc='upper right')
    ax1.grid(True, alpha=0.3)
    
    # Gráfico 2: Stress Testing - Escenarios
    ax2 = axes[1]
    
    scenarios = {
        'Normal': -0.05,
        'Crisis 2008': -0.40,
        'Pandemia 2020': -0.34,
        'Tech Crash': -0.50,
        'Volatilidad Extrema': -0.25
    }
    
    scenario_names = list(scenarios.keys())
    scenario_values = list(scenarios.values())
    colors_scenarios = ['#2ecc71', '#e74c3c', '#e67e22', '#9b59b6', '#f39c12']
    
    bars = ax2.barh(scenario_names, [abs(v) for v in scenario_values], 
                    color=colors_scenarios, edgecolor='white', linewidth=1.5)
    
    # Añadir etiquetas
    for bar, val in zip(bars, scenario_values):
        ax2.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
                f'{abs(val)*100:.0f}%', ha='left', va='center', fontsize=10, fontweight='bold')
    
    ax2.set_xlabel('Pérdida del Portafolio (%)', fontsize=11)
    ax2.set_title('Stress Testing: Escenarios de Crisis', fontsize=12, fontweight='bold', pad=10)
    ax2.grid(True, alpha=0.3, axis='x')
    ax2.invert_xaxis()  # Las pérdidas van a la izquierda
    
    plt.suptitle('Gestión Avanzada de Riesgos', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('images/risk-management-advanced.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Generada: images/risk-management-advanced.png")


if __name__ == '__main__':
    print("Generando thumbnails para posts del blog...")
    print("-" * 50)
    
    generate_markowitz_thumbnail()
    generate_riskparity_thumbnail()
    generate_riskmanagement_thumbnail()
    
    print("-" * 50)
    print("¡Todos los thumbnails generados exitosamente!")