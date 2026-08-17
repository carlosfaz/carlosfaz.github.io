---
layout: post
title: "Frontera Eficiente de Markowitz: Optimización Moderna de Portafolios"
use_math: true
published: true
date: 2024-04-16
category: "Finanzas Cuantitativas"
tags: ["Finanzas Cuantitativas", "Portafolios", "Python"]
thumbnail: "/images/markowitz-frontier.svg"
---

En 1952, un joven economista llamado **Harry Markowitz** publicó un artículo de apenas 15 páginas que cambiaría las finanzas para siempre. Su idea, premiada con el Nobel en 1990, puede resumirse en una frase que cualquiera entiende:

> **No pongas todos los huevos en la misma canasta.** Pero ojo: Markowitz no se quedó en el refrán — lo convirtió en una fórmula matemática exacta.

En este artículo vamos a recorrer el camino completo: la intuición detrás de la diversificación, las matemáticas que la sostienen y, finalmente, una implementación en Python que puedes ejecutar tú mismo para encontrar el portafolio óptimo.

## La intuición: por qué diversificar funciona

Imagina que tienes dos negocios posibles: vender **helados** o vender **paraguas**. 

- Si solo vendes helados, un verano lluvioso te arruina.
- Si solo vendes paraguas, un verano soleado te arruina.
- Pero si haces **ambas cosas a la vez**, cuando un negocio sufre, el otro prospera. Tus ingresos totales se vuelven mucho más estables.

Eso es exactamente lo que formalizó Markowitz: el riesgo de un portafolio **no** es simplemente el promedio del riesgo de sus activos. Depende de cómo se mueven *unos con respecto a otros* — la **correlación**. Combinar activos que no se mueven al unísono reduce el riesgo total sin sacrificar retorno. Por eso se dice que la diversificación es *el único "almuerzo gratis" de las finanzas*.

**Los tres ingredientes del modelo:**

- **Retorno** ($\mu$): la ganancia que esperas de cada activo.
- **Riesgo** ($\sigma$): cuánto fluctúa ese retorno; su volatilidad.
- **Correlación** ($\rho$): qué tan parejo se mueven dos activos entre sí.

## El modelo matemático

Sea $ w = (w_1, \dots, w_n) $ el vector de **pesos** (qué fracción del dinero va a cada activo), $ \mu $ el vector de retornos esperados y $ \Sigma $ la matriz de covarianzas.

**El retorno del portafolio** es simplemente el promedio ponderado:

$ \displaystyle E[R_p] = w^T \mu = \sum_{i=1}^{n} w_i \, \mu_i $

**El riesgo del portafolio**, en cambio, contiene toda la magia de la correlación:

$ \displaystyle \sigma_p^2 = w^T \Sigma \, w = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i \, w_j \, \sigma_{ij} $

Fíjate en el doble sumatorio: aparecen los términos cruzados $ \sigma_{ij} $. Si dos activos tienen covarianza baja o negativa, esos términos *restan* riesgo total. Ahí vive el almuerzo gratis.

### El ratio de Sharpe: retorno por unidad de riesgo

¿Cómo comparamos portafolios entre sí? William Sharpe propuso medir el **exceso de retorno por cada unidad de riesgo soportada**:

$ \displaystyle S = \frac{E[R_p] - R_f}{\sigma_p} $

donde $ R_f $ es la **tasa libre de riesgo** (lo que paga, por ejemplo, un bono del Tesoro). Un Sharpe de $0.5$ significa que por cada punto de volatilidad que aguantas, recibes medio punto de retorno por encima de la tasa segura. Cuanto mayor, mejor.

### El problema de optimización

Ya podemos enunciar el objetivo con precisión. De todos los portafolios posibles, buscamos el que maximice su ratio de Sharpe:

$ \displaystyle \max_{w} \; \frac{w^T \mu - R_f}{\sqrt{w^T \Sigma w}} $

sujeto a restricciones de sentido común: invertimos todo el capital y, para no concentrarnos demasiado, ningún activo puede superar el 40% (ni apostar en contra, es decir, nada de ventas en corto):

$ \displaystyle \sum_{i=1}^{n} w_i = 1, \qquad 0 \leq w_i \leq 0.40 $

## De las ecuaciones al código

Manos a la obra. Construiremos un mercado de juguete con 5 activos y dejaremos que `scipy` encuentre el portafolio óptimo. El script completo está en [`scripts/generate_markowitz_frontier.py`](https://github.com/carlosfaz/carlosfaz.github.io/blob/main/scripts/generate_markowitz_frontier.py); aquí lo analizamos bloque por bloque.

### 1. Un mercado de juguete con 5 activos

Definimos retornos esperados, volatilidades y la matriz de correlaciones. Nótese el detalle elegante: la matriz de covarianzas se construye como $ \Sigma_{ij} = \sigma_i \, \sigma_j \, \rho_{ij} $, es decir, el producto externo de volatilidades por la matriz de correlación:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

np.random.seed(42)          # Reproducibilidad ante todo
risk_free_rate = 0.05       # Tasa libre de riesgo: 5% anual

# Retornos esperados anualizados: 10%, 12%, 8%, 15%, 6%
expected_returns = np.array([0.10, 0.12, 0.08, 0.15, 0.06])

# Volatilidades anualizadas: 15%, 20%, 10%, 25%, 8%
volatilities = np.array([0.15, 0.20, 0.10, 0.25, 0.08])

# Matriz de correlación (sím las relaciones entre activos)
correlation_matrix = np.array([
    [1.00, 0.30, 0.20, 0.10, 0.05],
    [0.30, 1.00, 0.40, 0.20, 0.10],
    [0.20, 0.40, 1.00, 0.15, 0.05],
    [0.10, 0.20, 0.15, 1.00, 0.20],
    [0.05, 0.10, 0.05, 0.20, 1.00]
])

# Matriz de covarianza: Σ = σ σᵀ ⊙ ρ
cov_matrix = np.outer(volatilities, volatilities) * correlation_matrix
```

### 2. La función objetivo

Los optimizadores de `scipy` **minimizan**, así que para maximizar el Sharpe minimizamos su negativo. El código traduce literalmente las fórmulas de arriba:

```python
def neg_sharpe_ratio(weights, expected_returns, cov_matrix, risk_free_rate):
    """Retorna el Sharpe con signo negativo (para minimizar)."""
    portfolio_return = np.sum(expected_returns * weights)        # E[R_p] = wᵀμ
    portfolio_vol = np.sqrt(weights.T @ cov_matrix @ weights)    # σ_p = √(wᵀΣw)
    sharpe = (portfolio_return - risk_free_rate) / portfolio_vol
    return -sharpe
```

### 3. La optimización

Usamos **SLSQP** (*Sequential Least Squares Programming*), ideal para problemas con restricciones de igualdad y cotas:

```python
n_assets = len(expected_returns)

# Restricción: los pesos suman exactamente 1
constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}

# Cotas: sin ventas en corto, máximo 40% por activo
bounds = tuple((0.0, 0.40) for _ in range(n_assets))

# Punto de partida: reparto uniforme (20% a cada activo)
initial_weights = np.ones(n_assets) / n_assets

result = minimize(
    neg_sharpe_ratio,
    initial_weights,
    args=(expected_returns, cov_matrix, risk_free_rate),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)

optimal_weights = result.x
```

### 4. Explorando el universo de portafolios

Para *ver* la frontera, generamos 500 portafolios aleatorios con la **distribución de Dirichlet** — la forma elegante de muestrear vectores que suman 1:

```python
n_portfolios = 500

# Pesos aleatorios que suman 1, cortesía de Dirichlet
w_mat = np.random.dirichlet(np.ones(n_assets), size=n_portfolios)

# Retorno, volatilidad y Sharpe de los 500 portafolios, vectorizado
frontier_returns = w_mat @ expected_returns
frontier_vols = np.sqrt(np.einsum("ij,jk,ik->i", w_mat, cov_matrix, w_mat))
sharpe_ratios = (frontier_returns - risk_free_rate) / frontier_vols
```

El `einsum` merece un aplauso: calcula las 500 varianzas $ w^T \Sigma w $ en una sola línea, sin bucles.


### 5. La visualización

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Nube de portafolios aleatorios, coloreados por su Sharpe
scatter = ax1.scatter(frontier_vols, frontier_returns, c=sharpe_ratios,
                      cmap='viridis', alpha=0.6, s=60, edgecolors='none')

# El campeón: portafolio de máximo Sharpe (estrella roja)
ax1.scatter(optimal_vol, optimal_return, color='red', s=300,
            marker='*', edgecolors='black', linewidth=3, zorder=5,
            label='Máximo Sharpe')

# Capital Allocation Line: combinar el óptimo con la tasa libre de riesgo
vol_range = np.linspace(0, 0.25, 100)
cal = risk_free_rate + optimal_sharpe * vol_range
ax1.plot(vol_range, cal, 'r-', alpha=0.5, linewidth=2,
         label='Capital Allocation Line')
ax1.axhline(y=risk_free_rate, color='gray', linestyle='--', alpha=0.7,
            label=f'Tasa Libre de Riesgo ({risk_free_rate:.0%})')

# Panel derecho: pesos del portafolio óptimo
asset_labels = [f'Activo {i+1}' for i in range(n_assets)]
ax2.bar(asset_labels, optimal_weights,
        color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

plt.tight_layout()
plt.savefig('images/markowitz-frontier.svg', format='svg', bbox_inches='tight')
```

## El resultado

![Frontera Eficiente de Markowitz: 500 portafolios aleatorios coloreados por su ratio de Sharpe, el portafolio óptimo marcado con una estrella roja, la Capital Allocation Line, y la distribución de pesos óptimos]({{ site.baseurl }}/images/markowitz-frontier.svg)

Cómo leer la figura:

- **Cada punto** es un portafolio posible; su color indica su ratio de Sharpe (amarillo = mejor).
- **La estrella roja ★** es el portafolio que encontró el optimizador: el punto donde la nube "empuja" más hacia arriba a la izquierda (más retorno, menos riesgo).
- **La línea roja** es la *Capital Allocation Line*: si combinas el portafolio óptimo con el activo libre de riesgo, puedes moverte sobre esa recta según tu tolerancia al riesgo. Es la mejor recta que se puede trazar — es tangente a la frontera.
- **El borde superior izquierdo** de la nube es la **frontera eficiente** propiamente dicha: por debajo de ella solo hay portafolios dominados (mismo riesgo con menos retorno).

Y esta es la salida del programa:

```text
Portafolio óptimo de máximo Sharpe:
  Retorno: 10.71%
  Volatilidad: 10.35%
  Sharpe: 0.551
  Pesos: [28.0%, 15.0%, 26.7%, 23.9%, 6.4%]
```

Observa la sabiduría del resultado: el Activo 4 tiene el mayor retorno (15%) pero también la mayor volatilidad (25%), así que el optimizador le asigna un respetable 24% sin llegar al límite. El Activo 3, modesto en retorno (8%) pero muy estable (10%) y poco correlacionado, recibe casi el 27%. **El óptimo no persigue el mayor retorno, sino la mejor combinación.**

## La solución exacta (para los curiosos)

Sin la restricción del 40%, el problema admite solución en forma cerrada. Planteando el Lagrangiano:

$ \displaystyle \mathcal{L}(w, \lambda) = \frac{w^T \mu - R_f}{\sqrt{w^T \Sigma w}} - \lambda \left( \sum_{i=1}^{n} w_i - 1 \right) $

e igualando su gradiente a cero se llega al portafolio tangente:

$ \displaystyle w^{*} = \frac{\Sigma^{-1} (\mu - R_f \mathbf{1})}{\mathbf{1}^T \Sigma^{-1} (\mu - R_f \mathbf{1})} $

donde $ \mathbf{1} $ es un vector de unos. Con las restricciones de caja (los límites del 40%), la solución ya no tiene forma cerrada y por eso recurrimos a optimización numérica como SLSQP.

## Apéndice: de datos diarios a anuales

Si trabajas con retornos diarios (lo habitual al descargar precios), la conversión anual es directa — con $252$ días hábiles bursátiles al año:

$ \displaystyle \mu_{\text{anual}} = \bar{r}_{\text{diario}} \times 252, \qquad \Sigma_{\text{anual}} = \Sigma_{\text{diario}} \times 252 $

y como la desviación estándar es la raíz de la varianza:

$ \displaystyle \sigma_{\text{anual}} = \sigma_{\text{diario}} \times \sqrt{252} $

## Conclusión

Markowitz nos enseñó que invertir no es elegir el mejor activo, sino la **mejor combinación** de activos. En este artículo viste el ciclo completo:

1. **La intuición**: la correlación imperfecta entre activos reduce el riesgo total.
2. **Las matemáticas**: retorno $ w^T \mu $, riesgo $ \sqrt{w^T \Sigma w} $ y el Sharpe como brújula.
3. **La práctica**: 40 líneas de Python que encuentran el portafolio óptimo y dibujan la frontera.

## Sigue la serie

Este artículo es el primero de una serie sobre gestión cuantitativa de portafolios:

- **[Paridad de Riesgo (Risk Parity)]({{ site.baseurl }}/paridad-riesgo-risk-parity/)**: ¿y si en lugar de repartir el dinero en partes iguales, repartiéramos el *riesgo* en partes iguales?
- **[Gestión de Riesgos Avanzada]({{ site.baseurl }}/gestion-riesgos-avanzada/)**: VaR, CVaR, stress testing y simulaciones Monte Carlo para cuando la volatilidad no basta.

