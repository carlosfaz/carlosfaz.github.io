"""
Genera la imagen del artículo sobre "Memory Scarcity, Open Models, and the
Restructuring of the AI Industry, 2026-2030" (Satoshi Matsuoka, RIKEN,
arXiv:2607.07207).
Panel 1: brecha de costo entrante vs incumbente en $/PB de ancho de banda
         entregado (la "cinta transportadora de la depreciación").
Panel 2: probabilidades de los cinco escenarios 2026-2030.
"""

import numpy as np
import matplotlib.pyplot as plt

# === Datos ancla del paper (secciones 3 y 8) ===
# Brecha de costo entrante/incumbente medida en $/PB de ancho de banda:
#   3.2× en 2026, 1.9× en 2027, y se RE-ABRE hacia 2029-30:
#   ~3× si el precio del HBM se normaliza en 2028, >4× si la escasez persiste.
anios = np.array([2026, 2027, 2028, 2029, 2030])
# Nota: 2028 es interpolación ilustrativa entre los anclas del paper
gap_normaliza = np.array([3.2, 1.9, 2.3, 2.8, 3.0])   # HBM normalizado en 2028
gap_escasez = np.array([3.2, 1.9, 2.6, 3.4, 4.2])     # Escasez hasta 2030

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# === Panel 1: la brecha que nunca se cierra ===
ax1.plot(anios, gap_normaliza, 'o-', color='steelblue', linewidth=3,
         markersize=11, markeredgecolor='black',
         label='HBM se normaliza en 2028 → ~3×')
ax1.plot(anios, gap_escasez, 's--', color='#d62728', linewidth=3,
         markersize=11, markeredgecolor='black',
         label='Escasez hasta 2030 → >4×')
ax1.axhline(y=1.0, color='green', linewidth=2.5, linestyle=':',
            label='Paridad de costos (nunca se alcanza)')

# Anotar los anclas del paper
ax1.annotate('3.2×', (2026, 3.2), textcoords='offset points', xytext=(0, 14),
             fontsize=16, fontweight='bold', ha='center')
ax1.annotate('1.9×', (2027, 1.9), textcoords='offset points', xytext=(0, -26),
             fontsize=16, fontweight='bold', ha='center')
ax1.annotate('~3×', (2030, 3.0), textcoords='offset points', xytext=(-8, 14),
             fontsize=16, fontweight='bold', ha='center', color='steelblue')
ax1.annotate('>4×', (2030, 4.2), textcoords='offset points', xytext=(-8, 14),
             fontsize=16, fontweight='bold', ha='center', color='#d62728')

ax1.set_xlabel('Año', fontsize=18)
ax1.set_ylabel('Brecha de costo (× vs flota incumbente)', fontsize=18)
ax1.set_title('La brecha entrante–incumbente nunca se cierra\n'
              '(costo en $/PB de ancho de banda entregado)',
              fontsize=20, fontweight='bold')
ax1.legend(fontsize=15, loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.tick_params(labelsize=16)
ax1.set_xticks(anios)
ax1.set_ylim(0, 5)

# === Panel 2: los cinco escenarios 2026-2030 ===
escenarios = [
    ('Bifurcación geopolítica', 12),
    ('Re-diferenciación por capa de sistema', 18),
    ('Absorción de Jevons', 20),
    ('Crash de commoditización', 25),
    ('Oligopolio de caseros rotativos', 25),
]
nombres = [e[0] for e in escenarios]
probs = [e[1] for e in escenarios]
colores = ['#7b3294', '#c2a5cf', '#a6dba0', '#fdae61', '#d62728']

barras = ax2.barh(nombres, probs, color=colores, edgecolor='black',
                  linewidth=1.2, height=0.62)
ax2.bar_label(barras, fmt='%d%%', padding=6, fontsize=17, fontweight='bold')
ax2.set_xlabel('Probabilidad asignada por el paper', fontsize=18)
ax2.set_title('Cinco escenarios para 2026–2030\n(ninguno supera el 25%)',
              fontsize=20, fontweight='bold')
ax2.grid(True, axis='x', alpha=0.3)
ax2.tick_params(labelsize=15)
ax2.set_xlim(0, 30)

plt.tight_layout()
plt.savefig('images/memory-scarcity-ai.svg', format='svg', bbox_inches='tight')
plt.close()

print("Imagen guardada: images/memory-scarcity-ai.svg")

# === Las cuentas del paper, reproducidas ===
print("\n=== Escasez de memoria y reestructuración de la IA (arXiv:2607.07207) ===")
print(f"Brecha entrante/incumbente: {gap_normaliza[0]}× (2026) → "
      f"{gap_normaliza[1]}× (2027) → ~3× o >4× (2029-30)")

print("\n--- Corredor de solvencia ---")
crec_tokens = 2.0      # la demanda de tokens debe duplicarse cada año
eficiencia = 0.70      # -30%/año en bytes por token
anios_corr = 4
print(f"Demanda de tokens: {crec_tokens}×/año × {anios_corr} años = "
      f"{crec_tokens**anios_corr:.0f}× acumulado")
print(f"Bytes por token: {eficiencia}×/año → {eficiencia**anios_corr:.2f}× "
      f"en {anios_corr} años")
print(f"Ancho de banda entregado requerido: (2 × 0.7)^4 = "
      f"{(crec_tokens * eficiencia)**anios_corr:.1f}× en {anios_corr} años")

print("\n--- Divergencia del costo de entrenamiento (2030) ---")
lujo = (18e9, 38e9)    # $18B-$38B por corrida frontera
masa = 5e6             # ~$5M paridad con la frontera previa (RL/destilación)
print(f"Nivel lujo:  ${lujo[0]/1e9:.0f}B-${lujo[1]/1e9:.0f}B por corrida frontera")
print(f"Nivel masa:  ~${masa/1e6:.0f}M (paridad con frontera previa)")
print(f"Ratio: {lujo[0]/masa:,.0f}× - {lujo[1]/masa:,.0f}× "
      f"(3-4 órdenes de magnitud; hoy ~40×)")
