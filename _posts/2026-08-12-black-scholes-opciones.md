---
layout: post
title: "Black-Scholes: la Ecuación que Mueve Wall Street"
use_math: true
published: true
date: 2026-08-12
category: "Finanzas Cuantitativas"
tags: ["Finanzas Cuantitativas", "Derivados", "Monte Carlo", "Python"]
thumbnail: "/images/black-scholes.svg"
---

En 1973, Fischer Black y Myron Scholes publicaron una fórmula que transformó un mercado artesanal — las opciones se negociaban casi a ojo — en una industria de billones de dólares. Robert Merton la perfeccionó ese mismo año, y en 1997 Scholes y Merton recibieron el Nobel por ella (Black había fallecido dos años antes).

La pregunta que resuelve es de una simplicidad engañosa:

> **¿Cuánto vale hoy el derecho a comprar algo mañana a un precio fijado?**

## La intuición: una opción es un seguro con trampa a favor

Piensa en el seguro de tu coche. Pagas una prima, y si chocas, la aseguradora cubre el desastre; si no chocas, pierdes la prima. Una **opción call** es exactamente eso, pero al revés y con el mercado de valores: pagas una prima y, si la acción sube mucho, ganas la diferencia; si cae, solo pierdes la prima. **Tu peor escenario está acotado, tu mejor escenario no tiene techo.**

Esa asimetría es la clave de todo lo que sigue. Una acción es una apuesta simétrica (sube o baja, ganas o pierdes). Una opción es una apuesta *con protección*: te quedas con el lado bueno del azar y le vendes el lado malo a alguien más.

Los personajes del contrato:

- **Subyacente ($ S $)**: la acción sobre la que se escribe la opción.
- **Strike ($ K $)**: el precio pactado al que podrás comprar.
- **Vencimiento ($ T $)**: la fecha límite para ejercer el derecho.
- **Prima**: lo que cuesta la opción hoy — eso es lo que queremos calcular.

## La idea genial: eliminar el riesgo en lugar de adivinarlo

Aquí está el truco que hizo famosa a esta ecuación. Antes de Black-Scholes, valorar una opción parecía requerir *adivinar* cuánto subiría la acción. Black y Scholes demostraron algo sorprendente: si en cada instante combinas la opción con la cantidad exacta de acciones (la famosa **cobertura delta**), el riesgo se cancela por completo.

Y un portafolio sin riesgo debe rendir exactamente la tasa libre de riesgo $ r $ — si no, habría arbitraje (dinero gratis, y el mercado no regala dinero por mucho tiempo). De ahí la consecuencia contraintuitiva y hermosa:

> El precio de la opción **no depende de cuánto esperas que suba la acción**. Depende de cuánto *se mueve*: la volatilidad $ \sigma $.

## La fórmula

Para una call europea (que solo puede ejercerse al vencimiento), el valor es:

$ \displaystyle C = S \, N(d_1) - K \, e^{-rT} \, N(d_2) $

donde $ N(\cdot) $ es la función de distribución acumulada de la normal estándar, y:

$ \displaystyle d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)\, T}{\sigma \sqrt{T}}, \qquad d_2 = d_1 - \sigma \sqrt{T} $

No dejes que los símbolos te intimiden; la estructura es legible:

- $ S \, N(d_1) $: lo que esperas *recibir* (la acción), ponderado por cuánto participa la opción en ella.
- $ K e^{-rT} N(d_2) $: lo que esperas *pagar* (el strike), traído a valor presente y ponderado por la probabilidad de que ejerzas.
- $ N(d_2) $ admite otra lectura deliciosa: es la probabilidad (en el "mundo libre de riesgo") de que la opción termine *in the money*.
- $ N(d_1) $ es el **delta**: cuántas acciones necesitas para la cobertura perfecta.

## De la fórmula al código

La implementación cabe en tres líneas útiles. El script completo está en [`scripts/generate_black_scholes.py`](https://github.com/carlosfaz/carlosfaz.github.io/blob/main/scripts/generate_black_scholes.py):

```python
import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """Precio de una opción call europea según Black-Scholes."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
```

¿Y si no confiamos en la fórmula cerrada? Podemos *simular* el futuro: bajo la medida libre de riesgo, el precio al vencimiento sigue una lognormal:

$ \displaystyle S_T = S_0 \, \exp\left( \left( r - \tfrac{\sigma^2}{2} \right) T + \sigma \sqrt{T} \, Z \right), \quad Z \sim N(0,1) $

El precio de la call es entonces el valor presente del payoff promedio sobre 200,000 futuros simulados:

```python
np.random.seed(42)
n_sims = 200_000

Z = np.random.normal(0, 1, n_sims)
S_T = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

# El precio es el valor presente del payoff esperado
call_mc = np.exp(-r * T) * np.mean(np.maximum(S_T - K, 0))
```

## El resultado

![Payoffs de una call y una put al vencimiento, y precio Black-Scholes de la call en función del subyacente para tres niveles de volatilidad]({{ site.baseurl }}/images/black-scholes.svg)

Cómo leer la figura:

- **Panel izquierdo**: los *payoffs* al vencimiento — la famosa forma de "palos de hockey". La call gana cuando la acción supera el strike; la put, cuando cae por debajo. Antes del strike, el payoff es cero: **solo pierdes la prima**.
- **Panel derecho**: el precio *hoy* de la call según Black-Scholes, para tres volatilidades. Aquí está la lección más profunda del artículo: **a mayor volatilidad, más cara la opción**. ¿Por qué? Porque la volatilidad solo te beneficia: si la acción se dispara, ganas mucho; si se desploma, tu pérdida sigue limitada a la prima. La incertidumbre, con una opción en la mano, juega a tu favor.

La salida exacta del programa:

```text
=== Black-Scholes (S=100, K=100, T=1, r=5%, σ=20%) ===
d1 = 0.3500,  d2 = 0.1500
Precio Call: $10.45
Precio Put:  $5.57
Verificación Monte Carlo de la call (200,000 sims): $10.46
```

La fórmula cerrada dice \$10.45 y doscientos mil futuros simulados dicen \$10.46. Cuando dos caminos tan distintos — el cálculo exacto y el azar domesticado — coinciden al centavo, sabes que entendiste el modelo.

**Bonus de coherencia**: la *paridad put-call* exige $ C - P = S - K e^{-rT} $. Comprobamos: $ 10.45 - 5.57 = 4.88 $ y $ 100 - 100 e^{-0.05} = 4.88 $. ✓

## Conclusión

1. **Una opción es asimetría embotellada**: te quedas con el lado bueno del azar y acotas el malo.
2. **El genio de Black-Scholes** no fue adivinar el mercado, sino eliminarlo: la cobertura delta convierte la dirección del precio en irrelevante; solo importa la volatilidad.
3. **La volatilidad vale dinero**: es el ingrediente que le da valor al tiempo y a la incertidumbre.
4. **Verifica tus modelos**: Monte Carlo y la fórmula cerrada se confirman mutuamente al centavo.

## Sigue la serie

- **[Frontera Eficiente de Markowitz]({{ site.baseurl }}/frontera-eficiente-markowitz/)**: dónde nace la idea de medir el riesgo con la volatilidad.
- **[Gestión de Riesgos Avanzada]({{ site.baseurl }}/gestion-riesgos-avanzada/)**: qué pasa cuando las colas son más gruesas de lo que la normalidad admite — la crítica de Mandelbrot que también pesa sobre Black-Scholes.

