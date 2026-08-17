---
layout: post
title: "Teoría de la Ruina: la Probabilidad de Quebrar"
use_math: true
published: true
date: 2026-08-15
category: "Gestión de Riesgos"
tags: ["Gestión de Riesgos", "Monte Carlo", "Python"]
thumbnail: "/images/ruin-theory.svg"
---

Una aseguradora cobra primas todos los días y paga siniestros de vez en cuando. Los números cuadran: cobra más de lo que paga *en promedio*. Pregunta incómoda:

> Si el negocio es rentable en promedio... **¿puede quebrar igual?**

La respuesta — que los actuarios conocen desde Filip Lundberg (1903) y Harald Cramér (1930) — es un **sí** rotundo. La rentabilidad promedio no te salva de una mala racha. La pregunta correcta no es *"¿gano en promedio?"* sino *"¿cuánto capital necesito para que una mala racha casi nunca me hunda?"*. Bienvenido a la **teoría de la ruina**.

## El modelo: el capital como un caminante con trampas

El capital de la aseguradora en el tiempo $ t $ sigue el **proceso de Cramér-Lundberg**:

$ \displaystyle U(t) = u + c\,t - \sum_{i=1}^{N(t)} X_i $

Cada pieza cuenta una historia:

- $ u $: el **capital inicial** — tu escudo.
- $ c $: la **prima** que entra continuamente — tu ingreso constante.
- $ N(t) $: el número de siniestros hasta $ t $, un **proceso de Poisson** con tasa $ \lambda $ — los desastres llegan sin avisar, a intervalos exponenciales.
- $ X_i $: el **monto de cada siniestro**, que modelamos con una exponencial de media $ \mu $ — la mayoría son golpes pequeños, algunos son catástrofes.

El capital sube en línea recta (las primas) y cae en saltos bruscos (los siniestros). La **ruina** es el momento en que $ U(t) < 0 $: el día en que no puedes pagar.

## La carga de seguridad y el exponente de Lundberg

Para que el negocio tenga sentido, la prima debe superar al costo esperado de los siniestros. Esa diferencia relativa es la **carga de seguridad** $ \theta $:

$ \displaystyle c = (1 + \theta)\,\lambda\,\mu $

Con $ \lambda = \mu = 1 $ y $ \theta = 20\% $, la prima es $ c = 1.2 $. Ahora bien, la pieza maestra de la teoría: la probabilidad de ruina $ \psi(u) $ decae **exponencialmente** con el capital inicial, y la velocidad de ese decaimiento la marca el **exponente de ajuste de Lundberg** $ R $, la única solución positiva de:

$ \displaystyle \lambda \left( M_X(R) - 1 \right) = c\,R $

donde $ M_X $ es la función generatriz de momentos del siniestro. Para siniestros exponenciales con media 1, la ecuación se puede resolver *en la servilleta*:

$ \displaystyle \frac{1}{1-R} - 1 = 1.2\,R \quad \Longrightarrow \quad R = \frac{1}{6} $

Y en este caso la probabilidad de ruina tiene forma exacta y cerrada:

$ \displaystyle \psi(u) = \frac{1}{1 + \theta}\, e^{-R\,u} = \frac{1}{1.2}\, e^{-u/6} $

Detente a apreciarla un segundo: dice que **duplicar tu capital no divide a la mitad tu riesgo de quiebra — lo eleva a otra potencia**. Pasar de $ u=10 $ a $ u=20 $ no mejora tu situación un 50%: la mejora es de $ e^{10/6} \approx 5.3 $ veces. El capital es el mejor seguro, y su efecto es exponencial.

## De la teoría al código

La simulación Monte Carlo es sorprendentemente directa: la ruina solo puede ocurrir *justo después de un siniestro*, así que basta evaluar el capital en los tiempos de llegada. El script completo está en [`scripts/generate_ruin_theory.py`](https://github.com/carlosfaz/carlosfaz.github.io/blob/main/scripts/generate_ruin_theory.py):

```python
import numpy as np

lam, mu, theta, T = 1.0, 1.0, 0.20, 100
c = (1 + theta) * lam * mu          # Prima con 20% de carga de seguridad

def simular_ruina(u0, n_sims=5000, max_eventos=200):
    """Estima ψ(u): fracción de simulaciones donde el capital cae bajo cero."""
    # Tiempos entre siniestros ~ Exp(λ); llegadas = suma acumulada
    inter = np.random.exponential(1 / lam, (n_sims, max_eventos))
    tiempos = np.cumsum(inter, axis=1)
    dentro = tiempos <= T

    # Montos ~ Exp(μ); el capital solo se evalúa en tiempos de siniestro
    claims = np.random.exponential(mu, (n_sims, max_eventos)) * dentro
    tiempos_clip = np.minimum(tiempos, T)
    capital = u0 + c * tiempos_clip - np.cumsum(claims, axis=1)
    capital[~dentro] = np.inf

    return np.any(capital < 0, axis=1).mean()
```

Y la fórmula exacta contra la que la contrastaremos:

```python
R = 1 - lam * mu / c                         # Exponente de Lundberg: 1/6
psi_exacta = lambda u: (1 / (1 + theta)) * np.exp(-R * u)
```

## El resultado

![A la izquierda: 60 trayectorias del capital, con las arruinadas en rojo. A la derecha: la probabilidad de ruina simulada contra la fórmula exacta]({{ site.baseurl }}/images/ruin-theory.svg)

Cómo leer la figura:

- **Panel izquierdo**: 60 aseguradoras idénticas, cada una con capital inicial $ u = 10 $. Todas suben por las primas y tropiezan con los siniestros (escalones). La mayoría sobrevive los 100 periodos (azul), pero las trayectorias **rojas** muestran la ruina en vivo: el salto que cruza la línea negra y no tiene vuelta atrás.
- **Panel derecho**: la joya del artículo. Los puntos rojos son la simulación Monte Carlo (5,000 mundos por cada capital inicial) y la línea punteada es la fórmula exacta $ \psi(u) = \frac{1}{1.2} e^{-u/6} $. Que coincidan casi punto por punto es el momento *"la teoría funciona"*.

La salida del programa:

```text
=== Teoría de la Ruina (Cramér-Lundberg) ===
Prima c = 1.2, reclamación media μ = 1.0, frecuencia λ = 1.0
Carga de seguridad θ = 20%
Exponente de ajuste de Lundberg R = 0.1667 (= 1/6)

ψ(10) simulada: 0.140  |  ψ(10) exacta: 0.157
ψ(20) simulada: 0.020  |  ψ(20) exacta: 0.030
```

Un matiz honesto y didáctico: la simulación queda *ligeramente por debajo* de la fórmula, y tiene sentido — el Monte Carlo solo vigila 100 periodos, mientras que la fórmula exacta contempla la ruina en un horizonte **infinito**. Las quiebras que ocurrirían en el año 101 no están en nuestra simulación, pero sí en $ \psi(u) $.

Y mira lo que dice la tabla de números: duplicar el capital de 10 a 20 reduce la probabilidad de quiebra de ~16% a ~3%. **Siete veces menos riesgo por el doble de capital.** El decaimiento exponencial $ e^{-u/6} $ no es una abstracción: es la razón por la que los reguladores exigen niveles mínimos de capital a las aseguradoras (hola, Solvencia II).

## Conclusión

1. **Rentable en promedio ≠ inmune a la quiebra**: la varianza también cobra facturas.
2. **La prima necesita colchón**: la carga de seguridad $ \theta $ es lo que separa un negocio de una ruleta.
3. **El capital inicial protege exponencialmente**: cada unidad adicional de $ u $ multiplica tu seguridad, no la suma.
4. **Teoría y simulación se necesitan**: la fórmula da la respuesta instantánea; Monte Carlo la verifica y llega donde la fórmula no puede (siniestros no exponenciales, primas variables, reaseguro...).

## Sigue la serie

- **[Gestión de Riesgos Avanzada]({{ site.baseurl }}/gestion-riesgos-avanzada/)**: VaR, CVaR y stress testing — el hermano moderno de la teoría de la ruina.
- **[Paridad de Riesgo (Risk Parity)]({{ site.baseurl }}/paridad-riesgo-risk-parity/)**: otra respuesta estructural al mismo miedo — que ningún riesgo domine tu destino.

