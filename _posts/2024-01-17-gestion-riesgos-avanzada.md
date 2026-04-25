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

**En 2008, muchos portafolios tenían un VaR "seguro". Igual quebraron.**

**Tu modelo dice que perderás como máximo 5%. El problema: ese número es mentira.**

Imagina que saltas de un avión. El **Value at Risk (VaR)** es saber a qué altura se abre tu paracaídas. El **CVaR** es preguntarte: *"Si el paracaídas tiene un agujero, ¿qué tan fuerte me golpearé las piernas al llegar al suelo?"*.

Esta es la esencia de la gestión avanzada de riesgos: no basta con conocer el escenario más probable, hay que entender la **fragilidad humana** frente a lo inesperado. Como escribe Nassim Taleb en *The Black Swan*, el VaR a veces nos da una falsa sensación de seguridad, como el pavo de Acción de Gracias que cree que el carnicero es su mejor amigo... hasta el día de la cena.

## Introducción: La Filosofía de la Preparación

En la vida diaria ya gestionamos riesgos sin darnos cuenta. Cuando calculas que llegas a una cita en 15 minutos el 95% de las veces, eso es VaR. Pero si hoy hay un accidente grave en la autopista, ¿cuánto vas a tardar? ¿Dos horas? Eso es CVaR.

Podemos entender estas herramientas comparándolas con la planificación ante inundaciones:

- **Value at Risk (VaR)**: Es como conocer la altura máxima que suele alcanzar el río en un año lluvioso normal. Nos da un límite de "pérdida máxima esperada" en condiciones habituales.
- **CVaR (Expected Shortfall)**: Es el estudio de qué sucede si el dique se rompe. No solo nos dice que el río se desbordó, sino que calcula cuánto daño promedio causará el agua una vez que supere nuestras defensas.
- **Stress Testing**: Es como realizar un simulacro de terremoto o huracán. Probamos cómo resistiría nuestra estructura financiera si ocurriera una catástrofe similar a las grandes crisis del pasado (como la de 2008).

**Idea principal:** Gestionar el riesgo no es evitar el peligro, sino conocer exactamente la profundidad del abismo antes de decidir caminar cerca del borde.

## Un Caso Real: Cuando el Modelo Falló

> **Octubre de 2008.** Un portafolio diversificado tenía un VaR del 95% de -2% diario. Según el modelo, solo debería perder más de eso 1 de cada 20 días.
>
> El 10 de octubre de 2008, el S&P 500 cayó **-9% en un solo día**.
>
> Ese día no estaba en el modelo. Pero sí en la realidad.

Este es el problema central: **el VaR no distingue entre una caída suave y un precipicio**. Dos portafolios pueden tener el mismo VaR. Uno pierde suavemente. El otro cae por un acantilado. El VaR no ve la diferencia.

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

# Ejemplo práctico
returns = np.random.normal(0, 0.02, 1000)  # 1000 días de retornos
result = calculate_var_cvar_historical(returns)

print(f"VaR 95%: {result['var']:.2%}")
print(f"CVaR 95%: {result['cvar']:.2%}")
```

**Interpretación:** Si obtienes `VaR = -3%` y `CVaR = -7%`, significa que cuando las cosas salen mal (más allá del VaR), salen **más del doble de mal** de lo que el VaR sugería. Ese es el verdadero riesgo.

## CVaR (Expected Shortfall)

El CVaR mide la pérdida promedio en los peores escenarios más allá del VaR. Es decir, el valor esperado de los retornos condicionados a que estén por debajo del VaR:

$ \displaystyle \text{CVaR} = E[R \mid R \leq \text{VaR}] $

### Propiedades de Coherencia

El CVaR es una **medida coherente de riesgo** (Artzner et al., 1999), ya que satisface propiedades que podemos "traducir para humanos":

- **Subaditividad**: $ \displaystyle \text{CVaR}(X+Y) \leq \text{CVaR}(X) + \text{CVaR}(Y) $
  - *Traducción:* "No pongas todos los huevos en la misma canasta". El CVaR premia la diversificación, mientras que el VaR es "testarudo" y a veces te dice que dos riesgos juntos son peores que por separado, lo cual desafía la lógica de la naturaleza.

- **Monotonicidad**: Si $ \displaystyle X \leq Y $, entonces $ \displaystyle \text{CVaR}(X) \geq \text{CVaR}(Y) $
  - *Traducción:* Si un activo siempre pierde más que otro, su riesgo debe ser mayor. Simple sentido común.

- **Homogeneidad positiva**: $ \displaystyle \text{CVaR}(\lambda X) = \lambda \text{CVaR}(X) $ para $ \displaystyle \lambda > 0 $
  - *Traducción:* Si duplicas tu apuesta, duplicas tu riesgo. Proporcionalidad pura.

- **Invarianza traslacional**: $ \displaystyle \text{CVaR}(X + c) = \text{CVaR}(X) - c $
  - *Traducción:* "El colchón de efectivo". Si guardas un billete de $100 bajo el colchón, tu riesgo disminuye exactamente en esa cantidad. Es la lógica de la honestidad financiera.

**Nota importante:** El VaR **no es coherente** porque no satisface subaditividad en general. Es como un amigo que a veces te dice que juntar dos caminos es más peligroso que tomarlos por separado, lo cual no tiene sentido cuando buscas seguridad en números.

---

⚠️ **Insight clave**

> El VaR no mide pérdidas extremas. **Mide dónde empiezan.**
>
> El CVaR describe lo que viene después.

---

## El VaR como "Mentira Piadosa"

David Einhorn comparó el VaR con *"un airbag que funciona perfectamente, excepto cuando tienes un accidente de coche"*.

Frases que duelen pero son ciertas:

- **"El VaR funciona… hasta que importa."**
- **"El VaR ignora exactamente lo que te destruye."**
- **"El VaR no falla. Está diseñado para ignorar el desastre."**

El VaR es un **umbral de ignorancia**: nos dice dónde termina el mapa que conocemos. El CVaR, en cambio, es la descripción del territorio de los monstruos que hay más allá del borde.

Como advierte Benoit Mandelbrot en *The (Mis)behavior of Markets*, la "normalidad" que asume el VaR paramétrico es un mito peligroso. Los mercados tienen colas gruesas, fractales y comportamientos que una campana de Gauss nunca capturará.

## Los Tres Personajes del Riesgo

Piensa en estos modelos como personajes con personalidad:

| Modelo | Personalidad | Lo que te dice |
|--------|-------------|----------------|
| **VaR** | Optimista ingenuo | "Todo está bien" |
| **CVaR** | Pesimista realista | "Sí… hasta que deja de estarlo" |
| **Stress Testing** | Paranoico útil | "¿Y si TODO sale mal?" |

El VaR te dice: *"Con 95% de confianza, no perderás más de X"*.  
El CVaR responde: *"Pero cuando pierdas más de X, prepárate para el infierno"*.  
El Stress Testing añade: *"¿Y si el infierno es peor de lo que imaginas?"*.

## VaR por Simulación Monte Carlo

Se asume que los retornos siguen una distribución normal multivariada con la media y covarianza históricas.

### Descomposición de Cholesky

Para generar retornos correlacionados, se descompone la matriz de covarianza:

$ \displaystyle \Sigma = L L^T $

donde $ \displaystyle L $ es una matriz triangular inferior.

Si $ \displaystyle Z \sim N(0, I) $, entonces $ \displaystyle LZ \sim N(0, \Sigma) $.

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

## Stress Testing: El Simulador de Vuelo en Tormenta

El Stress Testing no es un cálculo frío, es un **simulador de vuelo en tormenta**. Nos permite preguntar: *"Si todo sale mal al mismo tiempo, ¿sobrevivimos?"*.

No hacemos Stress Testing para predecir el futuro, sino para no olvidar las cicatrices del pasado. Como sugiere Taleb en *Antifragile*, el objetivo no es solo sobrevivir al estrés, sino diseñar portafolios que puedan **beneficiarse** de él.

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

### El Efecto "Imán" en las Crisis (Correlación Dinámica)

Imagina una discoteca. En una noche normal, cada quien baila a su ritmo (activos descorrelacionados). Pero si alguien grita **"¡FUEGO!"**, todos corren hacia la misma puerta al mismo tiempo. En las crisis, la libertad de movimiento desaparece y todo se vuelve un solo bloque de pánico.

Las correlaciones convergen a 1 en las crisis. Este fenómeno se modela mediante una combinación convexa entre la matriz base y la matriz de correlación perfecta:

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

# Ejemplo: ¿Qué pasa en una crisis tipo 2008?
# Si tienes 60% acciones, 40% bonos:
weights = [0.6, 0.4]
tickers = ['SPY', 'TLT']
scenarios = define_stress_scenarios(tickers)
resultados = run_stress_test(weights, None, scenarios)

print(f"Pérdida en Crisis 2008: {resultados['Crisis 2008']['portfolio_loss']:.2%}")
# Resultado típico: -32% (más grave que el VaR diario sugeriría)
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

---

⚠️ **Errores Comunes al Usar VaR**

1. **Creer que es la pérdida máxima** → No lo es. Solo es un percentil.
2. **Usarlo sin CVaR** → Es como saber que hay un acantilado, pero no cuán profundo es.
3. **Confiar en datos históricos tranquilos** → El pasado no predice las crisis.
4. **Ignorar correlaciones en crisis** → Todo se correlaciona cuando hay pánico.
5. **No hacer backtesting** → Un modelo no validado es una opinión disfrazada de ciencia.

---

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

---

### Para Profundizar

Si este tema te intriga, estas lecturas cambiarán tu forma de ver el riesgo:

- **Nassim Nicholas Taleb**: *Antifragile* y *The Black Swan* - Por qué el estrés es necesario y cómo los eventos raros dominan la historia.
- **Benoit Mandelbrot**: *The (Mis)behavior of Markets* - Por qué los mercados son fractales y la normalidad es un mito.
- **Artzner, Delbaen, Eber & Heath (1999)**: *Coherent Measures of Risk* - El Génesis de la gestión de riesgos moderna.
- **Daniel Kahneman**: *Thinking, Fast and Slow* - Cómo nuestros sesgos cognitivos nos hacen subestimar el riesgo.

### Una Pregunta Incómoda

> *"Si tu modelo nunca ha visto una crisis real… ¿estás gestionando riesgo o solo midiendo tranquilidad?"*

Esta pregunta transforma un ejercicio técnico en una meditación sobre la incertidumbre. Al final, gestionar riesgos no es sobre controlar el futuro, sino sobre respetar lo desconocido.