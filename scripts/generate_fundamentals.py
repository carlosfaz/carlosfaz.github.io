"""
Genera la imagen del artículo "Fundamentals: qué significa cada número de tu cartera".
Cuatro mini-paneles tipo dashboard:
  1. Curva base 100 de la cartera vs benchmark, con la zona underwater sombreada.
  2. Frontera eficiente de Markowitz con la CML, el portafolio de máximo Sharpe y el GMV.
  3. Matriz de correlación entre activos.
  4. Abanico Monte Carlo a 12 meses con bandas P5-P95 y mediana.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(11)

# Paleta del reporte Proventus
ACCENT = "#2563EB"
POS = "#16A34A"
NEG = "#DC2626"
WARN = "#D97706"
MUTED = "#64748B"

fig, axes = plt.subplots(2, 2, figsize=(16, 9))
fig.patch.set_facecolor("white")

# ---------------------------------------------------------------- Panel 1: Base 100 + underwater
ax = axes[0, 0]
n = 252
r_cartera = np.random.normal(0.0009, 0.012, n)
r_bench = np.random.normal(0.0005, 0.011, n)
cartera = 100 * np.cumprod(1 + r_cartera)
bench = 100 * np.cumprod(1 + r_bench)
dias = np.arange(n)

ax.plot(dias, cartera, color=ACCENT, lw=2, label="Cartera")
ax.plot(dias, bench, color=MUTED, lw=1.5, label="Benchmark (SPY)")
pico = np.maximum.accumulate(cartera)
ax.fill_between(dias, cartera, pico, color=NEG, alpha=0.25, label="Underwater")
ax.set_title("Base 100 vs benchmark y underwater", fontsize=14, fontweight="bold")
ax.set_xlabel("Días")
ax.set_ylabel("Base 100")
ax.legend(fontsize=9, loc="upper left", frameon=False)

# ------------------------------------------------- Panel 2: Frontera eficiente, CML, máx. Sharpe
ax = axes[0, 1]
rf = 0.05
sig = np.linspace(0.10, 0.30, 200)
ret = 0.03 + 0.60 * sig - 0.85 * sig**2
sharpe = (ret - rf) / sig
i_max = int(np.argmax(sharpe))

ax.plot(sig * 100, ret * 100, color=ACCENT, lw=2, label="Frontera eficiente")
x_cml = np.linspace(0, 32, 50)
ax.plot(x_cml, (rf + sharpe[i_max] * x_cml / 100) * 100, color=MUTED, lw=1.5,
        ls="--", label="CML")
ax.scatter(sig[i_max] * 100, ret[i_max] * 100, marker="*", s=260, color=WARN,
           zorder=5, label="Máx. Sharpe")
ax.scatter(sig[0] * 100, ret[0] * 100, marker="o", s=70, color=POS,
           zorder=5, label="GMV (mínima varianza)")

# Acciones individuales (no alcanzan la frontera)
sig_a = np.random.uniform(0.13, 0.34, 12)
ret_a = 0.03 + 0.60 * sig_a - 0.85 * sig_a**2 - np.random.uniform(0.01, 0.05, 12)
ax.scatter(sig_a * 100, ret_a * 100, s=28, color=MUTED, alpha=0.7, label="Acciones")
ax.set_title("Frontera eficiente y CML", fontsize=14, fontweight="bold")
ax.set_xlabel("Volatilidad anual (%)")
ax.set_ylabel("Retorno esperado (%)")
ax.legend(fontsize=9, loc="lower right", frameon=False)

# ---------------------------------------------------------- Panel 3: Matriz de correlación
ax = axes[1, 0]
tickers = ["V", "TSM", "MU", "GOOGL", "AMZN", "JPM"]
k = len(tickers)
base = 0.15 + 0.65 * np.random.rand(k, k)
corr = (base + base.T) / 2
np.fill_diagonal(corr, 1.0)

im = ax.imshow(corr, cmap="coolwarm", vmin=-0.2, vmax=1.0)
ax.set_xticks(range(k), tickers)
ax.set_yticks(range(k), tickers)
for i in range(k):
    for j in range(k):
        ax.text(j, i, f"{corr[i, j]:.2f}", ha="center", va="center",
                fontsize=9, color="black")
fig.colorbar(im, ax=ax, shrink=0.85)
ax.set_title("Matriz de correlación", fontsize=14, fontweight="bold")

# ---------------------------------------------------------- Panel 4: Abanico Monte Carlo
ax = axes[1, 1]
n_sims, pasos = 2000, 252
retornos = np.random.normal(0.0007, 0.013, (n_sims, pasos))
trayectorias = 100 * np.cumprod(1 + retornos, axis=1)
trayectorias = np.column_stack([np.full(n_sims, 100.0), trayectorias])
meses = np.arange(pasos + 1) / 21

p5 = np.percentile(trayectorias, 5, axis=0)
p25 = np.percentile(trayectorias, 25, axis=0)
p50 = np.percentile(trayectorias, 50, axis=0)
p75 = np.percentile(trayectorias, 75, axis=0)
p95 = np.percentile(trayectorias, 95, axis=0)

ax.fill_between(meses, p5, p95, color=ACCENT, alpha=0.18, label="P5 – P95")
ax.fill_between(meses, p25, p75, color=ACCENT, alpha=0.35, label="P25 – P75")
ax.plot(meses, p50, color=ACCENT, lw=2, label="Mediana")
ax.axhline(100, color=MUTED, lw=1, ls=":")
ax.set_title("Abanico Monte Carlo (12 meses)", fontsize=14, fontweight="bold")
ax.set_xlabel("Meses")
ax.set_ylabel("Valor de la cartera")
ax.legend(fontsize=9, loc="upper left", frameon=False)

fig.suptitle("Anatomía de un reporte de cartera", fontsize=18, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("/home/carlos/Escritorio/Prod/carlosfaz.github.io/images/fundamentals.svg",
            bbox_inches="tight")
print("OK: images/fundamentals.svg")
