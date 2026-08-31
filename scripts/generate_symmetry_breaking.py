#!/usr/bin/env python3
"""Figura para el post 'El precio de romper la simetría'.

Muestra el cociente cosmológico eta = (n - nbar)/(s + sbar) como función
de xi = mu/T: su forma exacta, la aproximación lineal (15/7*pi^2)*xi y la
posición del Universo observado (asimetría de ~6e-10 sobre fotones).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
})
plt.rcParams["mathtext.fontset"] = "dejavusans"

PI = np.pi


def eta_exact(xi):
    """Cociente exacto: (n-nbar)/(s+sbar) = (1/6)(xi+xi^3/pi^2)/(7pi^2/90+xi^2/6)."""
    num = (xi + xi**3 / PI**2) / 6.0
    den = (7.0 * PI**2 / 90.0) + xi**2 / 6.0
    return num / den


def eta_lin(xi):
    """Aproximacion lineal valida para |xi| << 1."""
    return 15.0 * xi / (7.0 * PI**2)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 3.7))

# ---- Panel izquierdo: escala lineal -------------------------------------
xi = np.linspace(0.0, 3.0, 500)
ax1.plot(xi, eta_lin(xi), ls="--", color="#d1495b", lw=1.8,
         label=r"$\eta \simeq \dfrac{15}{7\pi^2}\,\xi$")
ax1.plot(xi, eta_exact(xi), color="#0b6e4f", lw=2.5,
         label=r"$\eta = \dfrac{\frac{1}{6}\left(\xi+\xi^3/\pi^2\right)}"
               r"{\frac{7\pi^2}{90}+\frac{\xi^2}{6}}$")
ax1.axvspan(0.0, 1.0, color="#0b6e4f", alpha=0.07)
ax1.axvline(1.0, color="#0b6e4f", lw=0.8, ls=":", alpha=0.7)
ax1.text(0.5, 0.42, "regimen\nlineal\n$\\xi \\ll 1$", ha="center",
         va="center", fontsize=8, color="#444444")
ax1.set_xlabel(r"$\xi = \mu/T$  (asimetria quimica en unidades de temperatura)")
ax1.set_ylabel(r"$(n-\bar{n})/(s+\bar{s})$")
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 1.05)
ax1.legend(loc="upper left", fontsize=8.5)
ax1.set_title("El cociente exacto y su aproximacion lineal", fontsize=10)

# ---- Panel derecho: escala log-log --------------------------------------
xi2 = np.logspace(-10, 1, 800)
ax2.loglog(xi2, eta_lin(xi2), ls="--", color="#d1495b", lw=1.8,
           label=r"$\eta \simeq (15/7\pi^2)\,\xi$  (pendiente 1)")
ax2.loglog(xi2, eta_exact(xi2), color="#0b6e4f", lw=2.5, label="exacta")

# Posicion del Universo observado: xi ~ 4e-10, eta ~ 8.7e-11
xi_u, eta_u = 4.0e-10, eta_lin(4.0e-10)
ax2.plot([xi_u], [eta_u], marker="*", ms=17, color="#111111", ls="none", zorder=6)
ax2.annotate("asimetria observada hoy:\n$\\xi \\approx 4\\times10^{-10}$",
             xy=(xi_u, eta_u), xytext=(4e-8, 1e-9), fontsize=8, zorder=7,
             arrowprops=dict(arrowstyle="->", lw=0.9, color="#111111"))
ax2.text(4e-4, 0.05, "la correccion cubica\nse nota a partir de\n$\\xi\\sim 1$",
         fontsize=8, color="#444444", ha="left")
ax2.set_xlabel(r"$\xi = \mu/T$")
ax2.set_ylabel(r"$(n-\bar{n})/(s+\bar{s})$")
ax2.set_xlim(1e-10, 10)
ax2.set_ylim(1e-11, 2.0)
ax2.legend(loc="upper left", fontsize=8.5)
ax2.set_title("El Universo real vive en el regimen lineal", fontsize=10)

fig.tight_layout()
fig.savefig("images/symmetry-breaking.svg", bbox_inches="tight")
print("OK: images/symmetry-breaking.svg")