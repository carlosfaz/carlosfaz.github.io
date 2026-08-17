"""
Genera la imagen del artículo sobre Black-Scholes.
Panel 1: payoffs al vencimiento de una call y una put.
Panel 2: precio Black-Scholes de una call vs el subyacente para distintas volatilidades.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(42)

# Parámetros del contrato y del mercado
K = 100.0        # Precio de ejercicio (strike)
T = 1.0          # Vencimiento: 1 año
r = 0.05         # Tasa libre de riesgo: 5%
sigma = 0.20     # Volatilidad: 20%

def black_scholes_call(S, K, T, r, sigma):
    """Precio de una opción call europea según Black-Scholes."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def black_scholes_put(S, K, T, r, sigma):
    """Precio de una opción put europea según Black-Scholes."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# --- Precios con S = 100 (at the money) ---
S0 = 100.0
d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
call_price = black_scholes_call(S0, K, T, r, sigma)
put_price = black_scholes_put(S0, K, T, r, sigma)

# --- Verificación Monte Carlo del precio de la call ---
n_sims = 200_000
Z = np.random.normal(0, 1, n_sims)
S_T = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
call_mc = np.exp(-r * T) * np.mean(np.maximum(S_T - K, 0))

# ================= FIGURA =================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Panel 1: payoffs al vencimiento
S_range = np.linspace(50, 150, 300)
payoff_call = np.maximum(S_range - K, 0)
payoff_put = np.maximum(K - S_range, 0)

ax1.plot(S_range, payoff_call, color='#2ca02c', linewidth=3.5, label='Payoff Call: max(S − K, 0)')
ax1.plot(S_range, payoff_put, color='#d62728', linewidth=3.5, label='Payoff Put: max(K − S, 0)')
ax1.axvline(x=K, color='gray', linestyle='--', alpha=0.6, label=f'Strike K = {K:.0f}')
ax1.axhline(y=0, color='black', linewidth=1)
ax1.set_xlabel('Precio del subyacente al vencimiento ($S_T$)', fontsize=18)
ax1.set_ylabel('Payoff ($)', fontsize=18)
ax1.set_title('Payoffs al vencimiento', fontsize=20, fontweight='bold')
ax1.legend(fontsize=15)
ax1.grid(True, alpha=0.3)
ax1.tick_params(labelsize=16)

# Panel 2: precio de la call hoy, para distintas volatilidades
for sig, color in [(0.10, '#1f77b4'), (0.20, '#ff7f0e'), (0.35, '#9467bd')]:
    prices = black_scholes_call(S_range, K, T, r, sig)
    ax2.plot(S_range, prices, linewidth=3, color=color, label=f'σ = {sig:.0%}')

ax2.plot(S_range, payoff_call, 'k--', linewidth=2, alpha=0.5, label='Payoff al vencimiento')
ax2.axvline(x=K, color='gray', linestyle=':', alpha=0.6)
ax2.set_xlabel('Precio del subyacente hoy ($S_0$)', fontsize=18)
ax2.set_ylabel('Precio de la call ($)', fontsize=18)
ax2.set_title('Precio Black-Scholes: la volatilidad vale dinero', fontsize=20, fontweight='bold')
ax2.legend(fontsize=15)
ax2.grid(True, alpha=0.3)
ax2.tick_params(labelsize=16)

plt.tight_layout()
plt.savefig('images/black-scholes.svg', format='svg', bbox_inches='tight')
plt.close()

print("Imagen guardada: images/black-scholes.svg")
print(f"\n=== Black-Scholes (S=100, K=100, T=1, r=5%, σ=20%) ===")
print(f"d1 = {d1:.4f},  d2 = {d2:.4f}")
print(f"Precio Call: ${call_price:.2f}")
print(f"Precio Put:  ${put_price:.2f}")
print(f"Verificación Monte Carlo de la call ({n_sims:,} sims): ${call_mc:.2f}")
