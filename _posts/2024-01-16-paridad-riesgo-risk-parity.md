---
layout: post
title: "Paridad de Riesgo (Risk Parity): El Equilibrio Perfecto de Portafolios"
use_math: true
published: true
date: 2024-04-17
category: "Risk Parity"
tags: ["Risk Parity", "Portfolio Optimization", "Risk Management", "Python", "Diversification"]
thumbnail: "/images/risk-parity-comparison.svg"
---

Aquí va un dato que incomoda a medio mundo financiero: en el clásico portafolio **60/40** (60% acciones, 40% bonos) — el favorito de los asesores durante décadas — las acciones no aportan el 60% del riesgo.

Aportan cerca del **90%**.

Eso significa que el portafolio "equilibrado" más famoso del mundo es, en la práctica, una apuesta a las acciones con un pequeño colchón de bonos. La **Paridad de Riesgo** nació para corregir exactamente eso, y en este artículo vas a entender cómo, con matemáticas claras y código ejecutable.

## La intuición: la mochila desequilibrada

Imagina que preparas una mochila para una expedición. Metes 5 objetos pequeños (brújula, navaja, cantimplora...) y 1 objeto enorme (una tienda de campaña de hierro).

- Tienes 6 objetos distintos: estás *diversificado*... ¿o no?
- Cuando lleves tres horas caminando, tu espalda solo sentirá un objeto: **el grande**.

Con las inversiones pasa igual. Puedes tener muchos activos, pero si uno de ellos es mucho más volátil que los demás, **ese único activo decide el destino de todo tu dinero**. La diversificación por *cantidad de cosas* es una ilusión; lo que importa es la diversificación por *riesgo*.

> **La idea central de Risk Parity:** la estabilidad real se logra cuando cada activo aporta la **misma cantidad de riesgo** al portafolio, sin importar cuánto dinero represente.

Esta filosofía fue popularizada en los años 90 por fondos como Bridgewater (Ray Dalio) y su estrategia *All Weather* — "para todo clima" — diseñada para resistir cualquier tormenta económica.

## El modelo matemático

Partimos del mismo marco del [artículo de Markowitz]({{ site.baseurl }}/frontera-eficiente-markowitz/): pesos $ w $, matriz de covarianzas $ \Sigma $, y riesgo del portafolio $ \sigma_p = \sqrt{w^T \Sigma w} $.

### ¿Cuánto riesgo aporta cada activo?

La pregunta clave necesita una herramienta precisa. Primero, la **Contribución Marginal al Riesgo** (MRC): cuánto aumenta la volatilidad total si aumentamos un poquito el peso del activo $ i $:

$ \displaystyle \text{MRC}_i = \frac{\partial \sigma_p}{\partial w_i} = \frac{(\Sigma w)_i}{\sigma_p} $

Multiplicando por el peso obtenemos la **Contribución Total al Riesgo** (TRC):

$ \displaystyle \text{TRC}_i = w_i \times \text{MRC}_i = \frac{w_i \, (\Sigma w)_i}{\sigma_p} $

Y aquí viene una propiedad preciosa, consecuencia del teorema de Euler para funciones homogéneas: **las contribuciones suman exactamente el riesgo total**:

$ \displaystyle \sum_{i=1}^{n} \text{TRC}_i = \sigma_p $

Es decir, podemos repartir el riesgo del portafolio entre sus activos como quien reparte una cuenta de restaurante — al céntimo. Eso hace posible exigir un reparto *justo*.

### La condición de paridad

Con $ n $ activos, la paridad perfecta exige que cada uno pague exactamente $ 1/n $ de la cuenta:

$ \displaystyle \text{TRC}_i = \frac{\sigma_p}{n}, \qquad \forall \, i $

### El problema de optimización

En la práctica, buscamos los pesos que hagan las contribuciones lo más iguales posible, minimizando las desviaciones cuadráticas respecto al objetivo:

$ \displaystyle \min_{w} \; \sum_{i=1}^{n} \left( \text{TRC}_i - \frac{\sigma_p}{n} \right)^2 $

sujeto a $ \displaystyle \sum_{i=1}^{n} w_i = 1 $ y $ \displaystyle 0.01 \leq w_i \leq 0.30 $ (invertimos todo, con un mínimo del 1% y un máximo del 30% por activo).


## De las ecuaciones al código

Trabajaremos con un mercado de 4 activos (retornos 10%, 12%, 8% y 15%; volatilidades 15%, 20%, 10% y 25%). El script completo está en [`scripts/generate_risk_parity_comparison.py`](https://github.com/carlosfaz/carlosfaz.github.io/blob/main/scripts/generate_risk_parity_comparison.py); lo diseccionamos por bloques.

### 1. La función objetivo: medir el desequilibrio

El código traduce directamente la fórmula de mínimos cuadrados. Tres líneas de NumPy que valen un tratado:

```python
import numpy as np
from scipy.optimize import minimize

def risk_parity_objective(w, cov):
    """Suma de cuadrados de las desviaciones respecto a la paridad."""
    pv = np.sqrt(w.T @ cov @ w)            # σ_p: volatilidad del portafolio
    rc = w * (cov @ w) / pv                # TRC: contribución de cada activo
    return np.sum((rc - pv / len(w)) ** 2) # Distancia al reparto ideal
```

### 2. La optimización

Mismo motor que en Markowitz (SLSQP), distinto destino:

```python
n_assets = len(cov_matrix)

# Los pesos suman 1; cada activo entre 1% y 30%
constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
bounds = [(0.01, 0.30)] * n_assets
initial_weights = np.ones(n_assets) / n_assets

result = minimize(
    risk_parity_objective,
    initial_weights,
    args=(cov_matrix,),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)

rp_weights = result.x
```

### 3. El duelo: Markowitz vs Risk Parity

Para comparar ambos enfoques sobre el mismo mercado, calculamos también el portafolio de máximo Sharpe y las contribuciones al riesgo de cada uno:

```python
def calculate_trc(weights, cov):
    """Descompone la volatilidad total en contribuciones por activo."""
    pv = np.sqrt(weights.T @ cov @ weights)
    trc = weights * (cov @ weights) / pv
    return trc, pv

mw_trc, mw_vol = calculate_trc(mw_weights, cov_matrix)  # Markowitz
rp_trc, rp_vol = calculate_trc(rp_weights, cov_matrix)  # Risk Parity
```

## El resultado

![Comparación entre Markowitz y Risk Parity: frontera eficiente con ambos portafolios marcados, y distribución de pesos por activo]({{ site.baseurl }}/images/risk-parity-comparison.svg)

Y los números exactos que producen esa figura:

```text
=== Markowitz (Max Sharpe) ===
Retorno: 11.05%, Volatilidad: 10.98%, Sharpe: 0.551
Pesos:            [29.8%, 16.1%, 28.3%, 25.8%]
% Riesgo aportado: [24.6%, 18.6%, 14.1%, 42.7%]   <- desequilibrio

=== Risk Parity ===
Retorno: 10.77%, Volatilidad: 10.62%
Pesos:            [30.0%, 20.9%, 30.0%, 19.1%]
% Riesgo aportado: [27.2%, 28.4%, 16.7%, 27.6%]   <- equilibrio
```

**Cómo interpretar esto:**

- En el portafolio de **Markowitz**, el Activo 4 (el más volátil, σ=25%) acapara el **42.7% del riesgo total** con apenas el 25.8% del dinero. Es la tienda de campaña de hierro en la mochila: un solo activo decide casi la mitad de tu destino.
- En el portafolio de **Risk Parity**, las contribuciones rondan el 25% ideal (con 4 activos). El reparto es casi perfecto.
- ¿Y por qué el Activo 3 se queda en 16.7%? Detalle hermoso del mundo real: es el activo *más estable* (σ=10%), y para que aportara más riesgo necesitaría un peso mayor... pero choca contra la cota del 30% que impusimos. **Las restricciones realistas tienen consecuencias visibles.**

Risk Parity sacrifica un poco de retorno (10.77% vs 11.05%) a cambio de que **ningún activo pueda hundir el barco él solo**.

## Comparación de filosofías

| Característica | Markowitz (Max Sharpe) | Risk Parity |
|---|---|---|
| **Objetivo** | Maximizar retorno por unidad de riesgo | Igualar la contribución al riesgo |
| **¿Qué optimiza?** | Usa retornos esperados y covarianzas | Solo usa covarianzas |
| **Diversificación** | Basada en correlaciones | Basada en aporte de riesgo |
| **Sensibilidad** | Muy sensible a errores en $ \mu $ | Robusta: no necesita estimar retornos |
| **Resultado típico** | Concentrado en activos de alto Sharpe | Reparto equilibrado del riesgo |

## Ventajas y limitaciones

**Fortalezas:**

1. **Robustez**: estimar retornos futuros es notoriamente difícil (casi adivinación); Risk Parity simplemente no los necesita.
2. **Diversificación real**: ningún activo domina el riesgo del conjunto.
3. **Comportamiento en crisis**: históricamente más estable en mercados turbulentos.
4. **Comunicable**: se le explica a cualquiera con la analogía de la mochila.

**Debilidades:**

1. **Ignora los retornos esperados**: trata igual a un gran activo que a uno mediocre si su volatilidad es similar.
2. **Sobrepondera activos tranquilos**: puede cargar mucho peso en bonos (y sufrir si suben las tasas).
3. **Requiere rebalanceo**: la paridad se rompe cuando las volatilidades cambian.
4. **Sigue dependiendo de $ \Sigma $**: estimar covarianzas también tiene su incertidumbre.

## Conclusión

Markowitz pregunta: *"¿qué portafolio me da más retorno por mi riesgo?"* Risk Parity pregunta algo distinto: *"¿qué portafolio no depende de ningún activo en particular?"*

No son rivales: son respuestas a preguntas diferentes, y los gestores profesionales combinan ambas. Lo que sí debes llevarte de este artículo:

1. **Diversificar por pesos no es diversificar**: un portafolio 60/40 es una apuesta a las acciones disfrazada de equilibrio.
2. **El riesgo se puede repartir al céntimo** gracias a la descomposición TRC.
3. **La robustez tiene precio**: un poco menos de retorno esperado a cambio de mucha más estabilidad estructural.

## Sigue la serie

- **[Frontera Eficiente de Markowitz]({{ site.baseurl }}/frontera-eficiente-markowitz/)**: el punto de partida — maximizar el Sharpe.
- **[Gestión de Riesgos Avanzada]({{ site.baseurl }}/gestion-riesgos-avanzada/)**: VaR, CVaR y stress testing — qué hacer cuando la volatilidad no cuenta toda la historia.
