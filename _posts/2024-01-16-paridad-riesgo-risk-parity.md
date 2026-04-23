---
layout: post
title: "Paridad de Riesgo (Risk Parity): El Equilibrio Perfecto de Portafolios"
use_math: true
published: true
date: 2024-04-17
category: "Risk Parity"
tags: ["Risk Parity", "Portfolio Optimization", "Risk Management", "Python", "Diversification"]
thumbnail: "/images/first-post.png"
---

La Paridad de Riesgo (Risk Parity) es una filosofía de inversión que propone que la verdadera seguridad no viene de tener muchas cosas distintas, sino de asegurar que ninguna de ellas tenga el poder de hundir todo el proyecto por sí sola.

## Introducción: La Filosofía del Equilibrio

Si la Frontera Eficiente de Markowitz nos enseñó a repartir nuestras piezas, la Paridad de Riesgo nos enseña a equilibrar el peso real de esas piezas. Esta filosofía se popularizó en los años 90 y representa un cambio de paradigma en la gestión de portafolios.

**La analogía de la mochila:**

- Puede que lleve 5 objetos pequeños y 1 objeto muy pesado. Aunque tenga 6 objetos (diversidad), el peso que realmente castiga su espalda proviene casi exclusivamente del objeto grande.
- En finanzas, ocurre lo mismo: a veces tenemos muchos tipos de inversión, pero una sola de ellas es tan inestable que domina todo el peligro del grupo.
- La Paridad de Riesgo busca que cada elemento de su mochila aporte exactamente la misma cantidad de peso o esfuerzo, ajustando las cantidades de cada uno hasta lograr un equilibrio perfecto.

**Idea principal:** La estabilidad real se logra cuando cada inversión aporta la misma cantidad de riesgo al conjunto, independientemente de cuánto dinero hayamos puesto en ella.

## Fundamento Matemático

### Contribución Marginal al Riesgo (MRC)

Mide cuánto cambia la volatilidad del portafolio ante un cambio marginal en el peso del activo $ \displaystyle i $:

$ \displaystyle \text{MRC}_i = \frac{\partial \sigma_p}{\partial w_i} = \frac{(\boldsymbol{\Sigma} \boldsymbol{w})_i}{\sigma_p} $

### Contribución Total al Riesgo (TRC)

$ \displaystyle \text{TRC}_i = w_i \times \text{MRC}_i = \frac{w_i (\boldsymbol{\Sigma} \boldsymbol{w})_i}{\sigma_p} $

En Risk Parity, se busca:

$ \displaystyle \text{TRC}_i = \frac{\sigma_p}{n}, \quad \forall i $

es decir, cada activo contribuye con $ \displaystyle 1/n $ del riesgo total.

## Problema de Optimización

Se minimiza la suma de cuadrados de las desviaciones de las contribuciones al riesgo respecto al objetivo de paridad:

$ \displaystyle \min_{\mathbf{w}} \sum_{i=1}^n \left( \text{TRC}_i - \frac{\sigma_p}{n} \right)^2 $

sujeto a $ \displaystyle \sum w_i = 1 $ y $ \displaystyle 0.01 \leq w_i \leq 0.30 $.

## Implementación en Python

### Función Objetivo de Risk Parity

```python
def risk_parity_objective(w, cov):
    """
    Función objetivo para Risk Parity.
    Minimiza la suma de cuadrados de las desviaciones de las contribuciones al riesgo.
    
    Args:
        w: Vector de pesos del portafolio
        cov: Matriz de covarianza anualizada
    
    Returns:
        Suma de cuadrados de las desviaciones de las contribuciones al riesgo
    """
    pv = np.sqrt(w.T @ cov @ w)           # Volatilidad del portafolio
    rc = w * (cov @ w) / pv               # Contribución al riesgo (TRC)
    return np.sum((rc - pv / len(w)) ** 2) # Suma de cuadrados de desviaciones
```

### Optimización con SLSQP

```python
from scipy.optimize import minimize

def optimize_risk_parity(cov_matrix):
    """
    Encuentra los pesos óptimos que logran paridad de riesgo.
    
    Args:
        cov_matrix: Matriz de covarianza anualizada
    
    Returns:
        Vector de pesos que logran paridad de riesgo
    """
    n_assets = len(cov_matrix)
    
    # Restricción: los pesos deben sumar 1
    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
    
    # Límites: peso mínimo 1%, máximo 30% por activo
    bounds = [(0.01, 0.30)] * n_assets
    
    # Pesos iniciales: distribución uniforme
    initial_weights = np.ones(n_assets) / n_assets
    
    # Optimización
    result = minimize(
        risk_parity_objective,
        initial_weights,
        args=(cov_matrix,),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )
    
    return result.x
```

## Cálculo de Métricas Derivadas

### Drawdown

Mide la caída desde el máximo histórico acumulado:

```python
def compute_drawdown(series):
    """
    Calcula el drawdown de una serie de retornos.
    
    Args:
        series: Serie de retornos
    
    Returns:
        Serie de drawdown
    """
    cum = (1 + series).cumprod()
    return (cum - cum.cummax()) / cum.cummax()
```

### Ratio de Sharpe

$ \displaystyle \text{Sharpe} = \frac{\bar{r}_p \times \sqrt{252}}{s_p} $

Implementado como:

```python
def calculate_sharpe_ratio(returns, risk_free_rate=0.05):
    """
    Calcula el ratio de Sharpe anualizado.
    
    Args:
        returns: Serie de retornos diarios
        risk_free_rate: Tasa libre de riesgo anual
    
    Returns:
        Ratio de Sharpe anualizado
    """
    excess_return = returns.mean() * 252 - risk_free_rate
    volatility = returns.std() * np.sqrt(252)
    return excess_return / volatility
```

## Comparación: Markowitz vs Risk Parity

| Característica | Markowitz (Max Sharpe) | Risk Parity |
|---|---|---|
| **Objetivo** | Maximizar retorno por unidad de riesgo | Equalizar contribución al riesgo |
| **Enfoque** | Optimización media-varianza | Balance de riesgo |
| **Diversificación** | Basada en correlaciones | Basada en contribución al riesgo |
| **Sensibilidad** | Sensible a estimación de retornos | Menos sensible a retornos esperados |
| **Resultado típico** | Concentración en activos de alto Sharpe | Distribución más equilibrada |

## Ventajas de la Paridad de Riesgo

1. **Robustez**: No depende de estimaciones precisas de retornos esperados
2. **Diversificación real**: Cada activo contribuye equitativamente al riesgo
3. **Resistencia en crisis**: Mejor comportamiento en períodos de estrés de mercado
4. **Simplicidad conceptual**: Fácil de entender y comunicar

## Limitaciones

1. **Ignora retornos esperados**: No considera el potencial de ganancia de cada activo
2. **Puede sobreponderar activos de bajo riesgo**: Como bonos de larga duración
3. **Requiere rebalanceo frecuente**: Para mantener la paridad de riesgo
4. **Sensible a la estimación de covarianzas**: Como cualquier método basado en volatilidad

## Conclusión

La Paridad de Riesgo representa un enfoque complementario a la optimización tradicional de Markowitz. Mientras que Markowitz busca maximizar el retorno ajustado al riesgo, Risk Parity busca distribuir el riesgo de manera equitativa entre todos los activos.

**Lecciones clave:**
1. **La diversificación por peso no es diversificación real** si un solo activo domina el riesgo
2. **El equilibrio de riesgo** proporciona mayor estabilidad en períodos volátiles
3. **La combinación de ambos enfoques** puede ofrecer beneficios significativos
