import os
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)

# Configuracion de la figura y fondo oscuro
fig = plt.figure(figsize=(8, 8))
fig.patch.set_facecolor('#808080')  # Fondo gris exterior
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('#808080')         # Fondo gris interior

# 1. Parametrizacion de la pseudoesfera (tractricoide)
t = np.linspace(0.01, 3.5, 60)
theta = np.linspace(0, 2 * np.pi, 60)
T, Theta = np.meshgrid(t, theta)

X = np.cos(Theta) / np.cosh(T)
Y = np.sin(Theta) / np.cosh(T)
Z = T - np.tanh(T)
Z = -Z

ax.plot_surface(X, Y, Z, color='#7B85FF', alpha=0.9, edgecolor='white', lw=0.3, antialiased=True)

# 2. Linea verde (geodesica aproximada entre a y b)
t_line = np.linspace(0.1, 3.2, 100)
theta_line = 0.5 * t_line + np.pi/2

x_line = np.cos(theta_line) / np.cosh(t_line)
y_line = np.sin(theta_line) / np.cosh(t_line)
z_line = -(t_line - np.tanh(t_line))

ax.plot(x_line, y_line, z_line, color='#32CD32', linewidth=3, zorder=5)

# 3. Etiquetas 'a' y 'b'
ax.text(x_line[-1]*1.2, y_line[-1]*1.2, z_line[-1], 'a', color='white', fontsize=14, fontweight='bold', zorder=6)
ax.text(x_line[0]*1.1, y_line[0]*1.1, z_line[0] - 0.1, 'b', color='white', fontsize=14, fontweight='bold', zorder=6)

# 4. Ajustes visuales
ax.view_init(elev=15, azim=60)
ax.set_axis_off()
ax.set_box_aspect([1, 1, 1.5])

plt.tight_layout()
plt.savefig("images/pseudoesfera_lobachevsky.png", dpi=300, bbox_inches='tight', facecolor='#808080')
print("OK: images/pseudoesfera_lobachevsky.png")
