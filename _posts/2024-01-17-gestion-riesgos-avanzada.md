---
layout: post
title: "Gestión de Riesgos Avanzada: VaR, CVaR y Stress Testing"
use_math: true
published: true
date: 2024-04-18
category: "Gestión de Riesgos"
tags: ["Risk Management", "VaR", "CVaR", "Expected Shortfall", "Stress Testing", "Monte Carlo", "Python"]
thumbnail: "/images/risk-management-advanced.png"
---

La gestión avanzada de riesgos busca responder a una pregunta vital: "¿Qué es lo peor que podría pasar?". Históricamente, las instituciones financieras intentaron resumir el peligro en un solo número, pero pronto descubrieron que los desastres suelen ser más complejos de lo que parece a simple vista.

## Introducción: La Filosofía de la Preparación

Podemos entender estas herramientas comparándolas con la planificación ante inundaciones:

- **Value at Risk (VaR)**: Es como conocer la altura máxima que suele alcanzar el río en un año lluvioso normal. Nos da un límite de "pérdida máxima esperada" en condiciones habituales.
- **CVaR (Expected Shortfall)**: Es el estudio de qué sucede si el dique se rompe. No solo nos dice que el río se desbordó, sino que calcula cuánto daño promedio causará el agua una vez que supere nuestras defensas.
- **Stress Testing**: Es como realizar un simulacro de terremoto o huracán. Probamos cómo resistiría nuestra estructura financiera si ocurriera una catástrofe similar a las grandes crisis del pasado (como la de 2008).

**Idea principal:** Gestionar el riesgo no es evitar el peligro, sino conocer exactamente la profundidad del abismo antes de decidir caminar cerca del borde.

## Value at Risk (VaR) Histórico

El VaR histórico estima la pérdida máxima esperada con un nivel de confianza dado, sin asumir distribución normal. Para un nivel de confianza del 95%, el VaR corresponde al percentil 5 de los retornos históricos:

$ \displaystyle \text{VaR}_{95\%} = \text{percentil}_5(\text{retornos históricos}) $

### Implementación en Python

```python
def calculate_var_cvar_historical(returns, confidence_level=0.95):
    """
    Calcula VaR y CVaR (Expected Shortfall) históricos.
    
    Args:
        returns: Serie de retornos históricos
        confidence_level: Nivel de confianza (por defecto 95%)
    
    Returns:
        Diccionario con 'var' y 'cvar'
    """
    var = np.percentile(returns, (1 - confidence_level) * 100)
    cvar = returns[returns <= var].mean()  # Expected Shortfall
    return {'var': var, 'cvar': cvar}
```

## CVaR (Expected Shortfall)

El CVaR mide la pérdida promedio en los peores escenarios más allá del VaR. Es decir, el valor esperado de los retornos condicionados a que estén por debajo del VaR:

$ \displaystyle \text{CVaR} = E[R \mid R \leq \text{VaR}] $

### Propiedades de Coherencia

El CVaR es una **medida coherente de riesgo** (Artzner et al., 1999), ya que satisface:

- **Subaditividad**: $ \displaystyle \text{CVaR}(X+Y) \leq \text{CVaR}(X) + \text{CVaR}(Y) $
- **Monotonicidad**: Si $ \displaystyle X \leq Y $, entonces $ \displaystyle \text{CVaR}(X) \geq \text{CVaR}(Y) $
- **Homogeneidad positiva**: $ \displaystyle \text{CVaR}(\lambda X) = \lambda \text{CVaR}(X) $ para $ \displaystyle \lambda > 0 $
- **Invarianza traslacional**: $ \displaystyle \text{CVaR}(X + c) = \text{CVaR}(X) - c $

**Nota importante:** El VaR **no es coherente** porque no satisface subaditividad en general.

## VaR por Simulación Monte Carlo

Se asume que los retornos siguen una distribución normal multivariada con la media y covarianza históricas.

### Descomposición de Cholesky

Para generar retornos correlacionados, se descompone la matriz de covarianza:

$ \displaystyle \boldsymbol{\Sigma} = \boldsymbol{L} \boldsymbol{L}^T $

donde $ \displaystyle \boldsymbol{L} $ es una matriz triangular inferior.

Si $ \displaystyle \boldsymbol{Z} \sim N(\boldsymbol{0}, \boldsymbol{I}) $, entonces $ \displaystyle \boldsymbol{L}\boldsymbol{Z} \sim N(\boldsymbol{0}, \boldsymbol{\Sigma}) $.

### Implementación en Python

```python
def monte_carlo_var(weights, mean_returns, cov_matrix, n_simulations=10000, horizon=10):
    """
    Calcula VaR usando simulación Monte Carlo con descomposición de Cholesky.
    
    Args:
        weights: Vector de pesos del portafolio
        mean_returns: Vector de retornos esperados diarios
        cov_matrix: Matriz de covarianza diaria
        n_simulations: Número de simulaciones
        horizon: Horizonte de tiempo en días
    
    Returns:
        Tuple (VaR_95, CVaR_95)
    """
    # Descomposición de Cholesky
    try:
        L = np.linalg.cholesky(cov_matrix)
    except np.linalg.LinAlgError:
        # Regularización si no es definida positiva
        cov_matrix += np.eye(len(weights)) * 1e-6
        L = np.linalg.cholesky(cov_matrix)
    
    # Generar retornos correlacionados
    random_returns = np.random.normal(0, 1, (n_simulations, len(weights)))
    correlated_returns = random_returns @ L.T + mean_returns.values
    
    # Retornos del portafolio para el horizonte deseado
    portfolio_returns = correlated_returns @ weights * np.sqrt(horizon)
    
    # Calcular VaR y CVaR
    var_95 = np.percentile(portfolio_returns, 5)
    cvar_95 = portfolio_returns[portfolio_returns <= var_95].mean()
    
    return var_95, cvar_95
```

## Stress Testing

Se simulan escenarios de crisis aplicando shocks a los precios y ajustando las correlaciones:

### Definición de Escenarios

```python
def define_stress_scenarios(tickers):
    """
    Define escenarios de stress para testing.
    
    Returns:
        Diccionario con diferentes escenarios de crisis
    """
    scenarios = {
        'Crisis 2008': {
            'shocks': {t: -0.40 for t in tickers},
            'correlation_adjustment': 0.8,
            'description': 'Crisis financiera global'
        },
        'Pandemia 2020': {
            'shocks': {t: -0.34 for t in tickers},
            'correlation_adjustment': 0.7,
            'description': 'Crash COVID-19'
        },
        'Caída Tecnológico': {
            'shocks': {t: -0.50 if 'tech' in t.lower() else -0.20 for t in tickers},
            'correlation_adjustment': 0.6,
            'description': 'Burst burbuja tecnológica'
        },
        'Volatilidad Extrema': {
            'volatility_multiplier': 3.0,
            'correlation_adjustment': 0.9,
            'description': 'Período de alta volatilidad'
        }
    }
    return scenarios
```

### Ajuste de Correlación en Crisis

El ajuste de correlación se aplica mediante una combinación convexa entre la matriz base y la matriz de correlación perfecta:

$ \displaystyle C_{\text{ajustada}} = \alpha \cdot C_{\text{base}} + (1 - \alpha) \cdot J $

donde $ \displaystyle J $ es la matriz de unos (correlación perfecta), modelando el fenómeno de que en crisis las correlaciones convergen a 1.

### Pérdida del Portafolio bajo Escenarios

$ \displaystyle \text{Pérdida} = \sum_{i=1}^n w_i \times \text{shock}_i $

### Implementación del Stress Testing

```python
def run_stress_test(weights, current_prices, scenarios):
    """
    Ejecuta stress testing bajo diferentes escenarios.
    
    Args:
        weights: Vector de pesos del portafolio
        current_prices: Diccionario con precios actuales
        scenarios: Diccionario con escenarios de stress
    
    Returns:
        Diccionario con resultados del stress test
    """
    results = {}
    
    for scenario_name, scenario_data in scenarios.items():
        shocks = scenario_data['shocks']
        corr_adjustment = scenario_data.get('correlation_adjustment', 1.0)
        
        # Calcular pérdida del portafolio
        portfolio_loss = sum(weights[i] * shocks[ticker] 
                           for i, ticker in enumerate(shocks.keys()))
        
        results[scenario_name] = {
            'portfolio_loss': portfolio_loss,
            'correlation_adjustment': corr_adjustment,
            'description': scenario_data.get('description', '')
        }
    
    return results
```

## Correlación Dinámica

Se calculan matrices de correlación para diferentes ventanas temporales (30, 90, 180 días):

```python
def analyze_dynamic_correlation(returns, windows=[30, 90, 180]):
    """
    Analiza la evolución de las correlaciones en diferentes ventanas temporales.
    
    Args:
        returns: DataFrame con retornos de los activos
        windows: Lista de ventanas temporales en días
    
    Returns:
        Diccionario con correlaciones promedio por ventana
    """
    correlation_analysis = {}
    
    for window in windows:
        latest_corr = returns.tail(window).corr()
        
        # Extraer correlaciones únicas (triángulo superior)
        mask = np.triu(np.ones(latest_corr.shape, dtype=bool), k=1)
        avg_corr = latest_corr.values[mask].mean()
        
        correlation_analysis[f'{window}d'] = {
            'average_correlation': avg_corr,
            'correlation_matrix': latest_corr
        }
    
    return correlation_analysis
```

La máscara triangular superior extrae solo los elementos por encima de la diagonal (pares únicos de correlaciones).

## Comparación de Métodos de VaR

| Método | Ventajas | Limitaciones |
|---|---|---|
| **VaR Histórico** | No asume distribución, simple | Depende del período histórico |
| **VaR Paramétrico** | Rápido, analítico | Asume normalidad (irreal) |
| **Monte Carlo** | Flexible, modela no-linealidades | Computacionalmente intensivo |
| **CVaR** | Medida coherente, captura colas | Más complejo de calcular |

## Backtesting del VaR

Es crucial validar que el VaR calculado es preciso mediante backtesting:

```python
def backtest_var(var_predictions, actual_returns, confidence_level=0.95):
    """
    Realiza backtesting del VaR.
    
    Args:
        var_predictions: Serie con predicciones de VaR
        actual_returns: Serie con retornos reales
        confidence_level: Nivel de confianza del VaR
    
    Returns:
        Diccionario con estadísticas del backtest
    """
    # Contar violaciones (cuando la pérdida excede el VaR)
    violations = actual_returns < var_predictions
    n_violations = violations.sum()
    n_observations = len(actual_returns)
    
    # Frecuencia esperada de violaciones
    expected_violations = (1 - confidence_level) * n_observations
    
    # Test de proporción de Kupiec
    actual_frequency = n_violations / n_observations
    expected_frequency = 1 - confidence_level
    
    return {
        'total_observations': n_observations,
        'violations': n_violations,
        'actual_frequency': actual_frequency,
        'expected_frequency': expected_frequency,
        'frequency_ratio': actual_frequency / expected_frequency
    }
```

## Conclusión

La gestión avanzada de riesgos proporciona herramientas esenciales para entender y prepararse para escenarios adversos:

**Lecciones clave:**
1. **El VaR es solo el comienzo** - el CVaR proporciona información más completa sobre las colas
2. **Las crisis correlacionan todo** - el stress testing debe considerar este fenómeno
3. **La validación es crucial** - el backtesting asegura que los modelos son confiables
4. **Múltiples métodos** - usar diferentes enfoques proporciona una visión más robusta

**Advertencia importante:** Ningún modelo de riesgo es perfecto. La clave está en entender las limitaciones de cada método y usarlos de manera complementaria.
