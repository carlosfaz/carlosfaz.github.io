---
layout: post
title: "Frontera Eficiente de Markowitz: Optimización Moderna de Portafolios"
use_math: true
published: true
date: 2024-01-15
category: "Finanzas Cuantitativas"
tags: ["Markowitz", "Portfolio Optimization", "Risk Management", "Python"]
thumbnail: "/images/first-post.png"
---

La teoría moderna de portafolios, desarrollada por Harry Markowitz en 1952, revolucionó la forma en que entendemos la inversión y el riesgo. En este artículo exploraremos los fundamentos matemáticos y su implementación práctica.

## Introducción: La Filosofía de la Diversificación

Imagine que está preparando una receta culinaria compleja. No busca que un solo ingrediente sea el protagonista absoluto, sino que la combinación de sabores cree un plato equilibrado. Markowitz transformó el mundo de las finanzas al aplicar esta misma lógica a las inversiones.

**Conceptos fundamentales:**
- **Portafolio**: Su "bolsa" de inversiones; el conjunto total de activos que posee
- **Retorno**: El beneficio o ganancia que espera obtener de su dinero
- **Riesgo**: La posibilidad de que los resultados reales sean diferentes a lo esperado

## El Ratio de Sharpe

El ratio de Sharpe mide el exceso de retorno por unidad de riesgo:

$ \displaystyle \frac{E[R_{p}] - R_{f}}{\sigma_{p}} $

donde:
- $E[R_p]$ es el retorno esperado del portafolio
- $R_f$ es la tasa libre de riesgo (típicamente 5% anual)
- $\sigma_p$ es la volatilidad anualizada del portafolio

## Fundamento Matemático

Sea $w = (w_1, ..., w_n)$ el vector de pesos, $\mu$ el vector de retornos esperados anualizados, y $\Sigma$ la matriz de covarianza anualizada.

### Retorno del Portafolio

$\displaystyle E[R_p] = w^T \mu = \sum_{i=1}^{n} w_i \mu_i$

### Varianza del Portafolio

$\displaystyle \sigma_p^2 = w^T \Sigma w = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma_{ij}$

### Problema de Optimización

$\displaystyle \max_{w} \frac{w^T \mu - R_f}{\sqrt{w^T \Sigma w}}$

sujeto a:
$\displaystyle \sum_{i=1}^{n} w_i = 1, \quad 0 \leq w_i \leq 0.40$

## Solución Analítica

El Lagrangiano del problema es:

$\displaystyle \mathcal{L}(w, \lambda) = \frac{w^T \mu - R_f}{\sqrt{w^T \Sigma w}} - \lambda \left(\sum_{i=1}^{n} w_i - 1\right)$

La solución analítica (sin restricciones de caja) es:

$\displaystyle w^* = \frac{\Sigma^{-1}(\mu - R_f \mathbf{1})}{\mathbf{1}^T \Sigma^{-1}(\mu - R_f \mathbf{1})}$

## Implementación en Python

### Función Objetivo

```python
def neg_sharpe_ratio(weights, expected_returns, cov_matrix, risk_free_rate):
    """
    Calcula el negativo del ratio de Sharpe para minimización.
    
    Args:
        weights: Vector de pesos del portafolio
        expected_returns: Vector de retornos esperados anualizados
        cov_matrix: Matriz de covarianza anualizada
        risk_free_rate: Tasa libre de riesgo anual
    
    Returns:
        Negativo del ratio de Sharpe
    """
    portfolio_return = np.sum(expected_returns * weights)
    portfolio_vol = np.sqrt(weights.T @ cov_matrix @ weights)
    sharpe = (portfolio_return - risk_free_rate) / (portfolio_vol + 1e-10)
    return -sharpe  # Se minimiza el negativo
```

### Optimización con SLSQP

```python
from scipy.optimize import minimize

def optimize_maximum_sharpe(expected_returns, cov_matrix, risk_free_rate=0.05):
    """
    Encuentra los pesos óptimos que maximizan el ratio de Sharpe.
    """
    n_assets = len(expected_returns)
    
    # Restricciones
    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
    
    # Límites: sin short selling, máximo 40% por activo
    bounds = tuple((0.0, 0.40) for _ in range(n_assets))
    
    # Pesos iniciales: distribución uniforme
    initial_weights = np.ones(n_assets) / n_assets
    
    # Optimización
    result = minimize(
        neg_sharpe_ratio,
        initial_weights,
        args=(expected_returns, cov_matrix, risk_free_rate),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )
    
    return result.x
```

## Generación de la Frontera Eficiente

Para visualizar la frontera, generamos múltiples portafolios aleatorios:

```python
def generate_efficient_frontier(expected_returns, cov_matrix, n_portfolios=200):
    """
    Genera la frontera eficiente usando la distribución Dirichlet.
    """
    np.random.seed(42)
    
    # Generar pesos aleatorios que sumen 1
    w_mat = np.random.dirichlet(np.ones(len(expected_returns)), size=n_portfolios)
    
    # Calcular retornos y volatilidades
    frontier_returns = w_mat @ expected_returns.values
    frontier_vols = np.sqrt(np.einsum("ij,jk,ik->i", w_mat, cov_matrix.values, w_mat))
    
    # Calcular ratios de Sharpe
    sharpe_ratios = (frontier_returns - risk_free_rate) / frontier_vols
    
    return w_mat, frontier_returns, frontier_vols, sharpe_ratios
```

## Anualización de Datos

Los retornos diarios se anualizan multiplicando por 252 (días hábiles):

$\displaystyle \mu_{anual} = \bar{r}_{diario} \times 252$

$\displaystyle \Sigma_{anual} = \Sigma_{diario} \times 252$

La volatilidad se anualiza como:

$\displaystyle \sigma_{anual} = \sigma_{diario} \times \sqrt{252}$

## Temas Relacionados

Este artículo forma parte de una serie sobre optimización moderna de portafolios:

- **[Paridad de Riesgo (Risk Parity)](/paridad-riesgo-risk-parity/)**: Descubre cómo equilibrar el riesgo de manera equitativa entre todos los activos.
- **[Gestión de Riesgos Avanzada](/gestion-riesgos-avanzada/)**: Profundiza en VaR, CVaR, Stress Testing y simulaciones Monte Carlo.

## Conclusión

La optimización moderna de portafolios combina teoría matemática rigurosa con implementación práctica. Las técnicas presentadas - desde la frontera eficiente de Markowitz hasta la paridad de riesgo y las simulaciones Monte Carlo - proporcionan herramientas poderosas para la gestión profesional de inversiones.

La clave del éxito está en entender que:
1. **La diversificación es el único "almuerzo gratis"** en finanzas
2. **El riesgo debe medirse y gestionarse sistemáticamente**
3. **Las restricciones realistas mejoran la robustez** de las soluciones
4. **El rebalanceo periódico** mantiene la asignación objetivo

¿Te interesa implementar estas técnicas en tus propias inversiones? ¡Explora el código completo en mi repositorio de GitHub!