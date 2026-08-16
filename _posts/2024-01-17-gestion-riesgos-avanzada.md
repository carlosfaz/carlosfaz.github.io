---
layout: post
title: "Gestión de Riesgos Avanzada: VaR, CVaR y Stress Testing"
use_math: true
published: true
date: 2024-04-18
category: "Gestión de Riesgos"
tags: ["Risk Management", "VaR", "CVaR", "Expected Shortfall", "Stress Testing", "Monte Carlo", "Python"]
thumbnail: "/images/risk-management-advanced.svg"
---

Imagina que saltas de un avión. El **Value at Risk (VaR)** es saber a qué altura se abre tu paracaídas. El **CVaR** es la pregunta mucho más incómoda: *"si el paracaídas falla, ¿qué tan fuerte va a ser el golpe?"*.

En los artículos anteriores medimos el riesgo con un solo número: la volatilidad. Pero la volatilidad trata igual las ganancias que las pérdidas, y no distingue entre un mal día y una catástrofe. Aquí vamos a bajar al sótano del riesgo: las **colas** de la distribución, donde viven los desastres.

## La filosofía de la preparación

En la vida diaria ya gestionas riesgos sin notarlo. Cuando calculas que llegas a una cita en 15 minutos el 95% de las veces, eso es VaR. Y si hoy hubo un accidente en la autopista, ¿cuánto tardarás *de verdad*? ¿Dos horas? Eso es CVaR.

La trilogía completa, explicada con inundaciones:

- **VaR**: la altura máxima que suele alcanzar el río en un año lluvioso normal. Tu muro está justo ahí.
- **CVaR (Expected Shortfall)**: lo que pasa *cuando el agua supera el muro*. No es "si se desborda o no", sino cuánto daño hará en promedio una vez dentro.
- **Stress Testing**: el simulacro de terremoto. Replicar sobre tu portafolio las grandes catástrofes de la historia (2008, COVID-19) para ver si sobrevive.

> **Idea central:** gestionar el riesgo no es evitar el peligro, sino conocer la profundidad exacta del abismo antes de caminar cerca del borde.

## Value at Risk (VaR) histórico

El VaR responde a una pregunta concreta: *"¿cuál es la pérdida máxima que debo esperar en un día normalmente malo?"*. Con un nivel de confianza del 95%, el VaR histórico es simplemente el **percentil 5** de los retornos observados — sin asumir ninguna distribución:

$ \displaystyle \text{VaR}_{95\%} = \text{percentil}_{5}(\text{retornos históricos}) $

Si el VaR 95% diario es $-4.21\%$, la lectura es: *"el 95% de los días perderemos menos del 4.21%... y el 5% restante, algo peor"*.

### Implementación en Python

Dos líneas que resumen toda la idea — nótese que el CVaR viene de regalo en la misma función:

```python
import numpy as np

def calculate_var_cvar_historical(returns, confidence_level=0.95):
    """VaR y CVaR históricos a partir de retornos observados."""
    var = np.percentile(returns, (1 - confidence_level) * 100)
    cvar = returns[returns <= var].mean()   # Promedio de los desastres
    return {'var': var, 'cvar': cvar}
```

## CVaR: lo que hay más allá del umbral

El VaR tiene un punto ciego fatal: te dice *dónde* está el borde del mapa, pero nada de los monstruos que habitan más allá. El **CVaR** (o *Expected Shortfall*) es la pérdida **promedio** condicionada a que ya superamos el VaR:

$ \displaystyle \text{CVaR}_{95\%} = E\left[ R \;\middle|\; R \leq \text{VaR}_{95\%} \right] $

### Por qué el CVaR es una medida "coherente"

Artzner y coautores (1999) definieron qué debe cumplir una medida de riesgo para tener sentido. El CVaR las cumple todas, y cada una tiene una traducción al lenguaje humano:

- **Subaditividad**: $ \displaystyle \text{CVaR}(X+Y) \leq \text{CVaR}(X) + \text{CVaR}(Y) $
  - *Traducción:* "no pongas todos los huevos en la misma canasta". Combinar activos nunca *aumenta* el riesgo medido.
- **Monotonicidad**: si $ X \leq Y $ siempre, entonces $ \text{CVaR}(X) \geq \text{CVaR}(Y) $
  - *Traducción:* si un activo pierde más que otro en *todo* escenario, debe medirse como más riesgoso. Puro sentido común.
- **Homogeneidad positiva**: $ \displaystyle \text{CVaR}(\lambda X) = \lambda \, \text{CVaR}(X) $ para $ \lambda > 0 $
  - *Traducción:* si duplicas la apuesta, duplicas el riesgo. Ni más, ni menos.
- **Invarianza traslacional**: $ \displaystyle \text{CVaR}(X + c) = \text{CVaR}(X) - c $
  - *Traducción:* el colchón de efectivo. Guardar \$100 en efectivo reduce tu riesgo en exactamente \$100.

**Dato clave:** el VaR **no es coherente** — puede violar la subaditividad. Es como un amigo que a veces te dice que juntar dos inversiones es *más* peligroso que tenerlas por separado, justo cuando la intuición (y la diversificación) dicen lo contrario.

### El VaR como "mentira piadosa"

David Einhorn lo dijo mejor que nadie: el VaR es *"un airbag que funciona perfectamente, excepto cuando tienes un accidente"*. Y Benoit Mandelbrot pasó media carrera advirtiendo que la campana de Gauss — la base del VaR paramétrico — es un mito peligroso: los mercados reales tienen **colas gruesas**, y los días catastróficos son mucho más frecuentes de lo que la normalidad predice.

Nassim Taleb lo ilustra con el pavo de Acción de Gracias: mil días de datos le "prueban" al pavo que el granjero es su amigo. El VaR calculado con esos mil días no contiene ninguna pista sobre el día 1001.

## VaR por simulación Monte Carlo

¿Y si no tenemos suficiente historia, o queremos probar escenarios que *nunca* han ocurrido? Generamos miles de futuros sintéticos. El supuesto: los retornos siguen una normal multivariada con la media y covarianza históricas.

### El truco de Cholesky: fabricar correlación

Aquí hay una joya de álgebra lineal. Si queremos generar retornos aleatorios **correlacionados** (porque los activos no se mueven independientes), descomponemos la matriz de covarianzas:

$ \displaystyle \Sigma = L \, L^T $

donde $ L $ es triangular inferior. Entonces, si $ Z \sim N(0, I) $ son choques *independientes*:

$ \displaystyle L Z \sim N(0, \Sigma) $

Multiplicar por $ L $ "inyecta" la correlación exacta del mercado en nuestros números aleatorios. Con esto, simular un portafolio correlacionado son 5 líneas:

```python
import numpy as np

def monte_carlo_var(weights, mean_returns, cov_matrix,
                    n_simulations=10000, horizon=10):
    """VaR y CVaR por Monte Carlo con descomposición de Cholesky."""
    # L tal que Σ = L·Lᵀ (con regularización si Σ no es definida positiva)
    try:
        L = np.linalg.cholesky(cov_matrix)
    except np.linalg.LinAlgError:
        cov_matrix += np.eye(len(weights)) * 1e-6
        L = np.linalg.cholesky(cov_matrix)

    # Choques independientes que se vuelven correlacionados al aplicar L
    z = np.random.normal(0, 1, (n_simulations, len(weights)))
    correlated = z @ L.T + mean_returns.values

    # Retorno del portafolio escalado al horizonte de 10 días
    portfolio_returns = correlated @ weights * np.sqrt(horizon)

    var_95 = np.percentile(portfolio_returns, 5)
    cvar_95 = portfolio_returns[portfolio_returns <= var_95].mean()
    return var_95, cvar_95
```

## Stress Testing: el simulador de vuelo en tormenta

El stress testing no es un cálculo frío: es un **simulador de vuelo en tormenta**. No preguntamos "¿qué pasará?", sino *"si todo sale mal al mismo tiempo — como ya ha pasado —, ¿sobrevivimos?"*.

No lo hacemos para predecir el futuro, sino para no olvidar las cicatrices del pasado. Y como sugiere Taleb en *Antifragile*, el objetivo final ni siquiera es sobrevivir al estrés: es diseñar portafolios que puedan **beneficiarse** de él.

### El efecto "¡FUEGO!": la correlación en las crisis

Imagina una discoteca. En una noche normal, cada quien baila a su ritmo: eso son los activos descorrelacionados. Pero si alguien grita **"¡FUEGO!"**, todos corren hacia la misma puerta a la vez. En las crisis, la diversificación se evapora justo cuando más la necesitas: **las correlaciones convergen a 1**.

Se modela como una combinación convexa entre la matriz de correlación normal y la matriz de unos $ J $ (correlación perfecta):

$ \displaystyle C_{\text{ajustada}} = \alpha \cdot C_{\text{base}} + (1 - \alpha) \cdot J $

### Escenarios históricos y pérdida del portafolio

Definimos los grandes desastres como shocks directos sobre cada activo, y la pérdida es la suma ponderada:

$ \displaystyle \text{Pérdida} = \sum_{i=1}^{n} w_i \times \text{shock}_i $

```python
def define_stress_scenarios(tickers):
    """Catálogo de catástrofes históricas para probar el portafolio."""
    return {
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
        'Caída Tecnológica': {
            'shocks': {t: -0.50 if 'tech' in t.lower() else -0.20
                       for t in tickers},
            'correlation_adjustment': 0.6,
            'description': 'Burst de la burbuja tecnológica'
        },
        'Volatilidad Extrema': {
            'volatility_multiplier': 3.0,
            'correlation_adjustment': 0.9,
            'description': 'Período de alta volatilidad'
        }
    }
```

### Ejecutar el simulacro

```python
def run_stress_test(weights, scenarios):
    """Aplica cada escenario de crisis y reporta la pérdida del portafolio."""
    results = {}
    for name, scenario in scenarios.items():
        shocks = scenario['shocks']
        portfolio_loss = sum(weights[i] * shocks[t]
                             for i, t in enumerate(shocks.keys()))
        results[name] = {
            'portfolio_loss': portfolio_loss,
            'description': scenario.get('description', '')
        }
    return results
```

### Vigilando la correlación en tiempo real

Como la correlación es el ingrediente que se evapora en las crisis, conviene monitorearla con ventanas móviles:

```python
def analyze_dynamic_correlation(returns, windows=[30, 90, 180]):
    """Correlación promedio entre activos en distintas ventanas temporales."""
    analysis = {}
    for window in windows:
        latest_corr = returns.tail(window).corr()
        # Máscara triangular superior: solo pares únicos, sin la diagonal
        mask = np.triu(np.ones(latest_corr.shape, dtype=bool), k=1)
        analysis[f'{window}d'] = {
            'average_correlation': latest_corr.values[mask].mean()
        }
    return analysis
```

Si la correlación de 30 días empieza a separarse mucho de la de 180 días, el mercado te está susurrando que la discoteca se está poniendo nerviosa.


## El resultado en imágenes

El script completo ([`scripts/generate_risk_management_advanced.py`](https://github.com/carlosfaz/carlosfaz.github.io/blob/main/scripts/generate_risk_management_advanced.py)) simula 10,000 retornos diarios con **colas gruesas** (distribución t de Student, como los mercados reales) y 100 trayectorias de precio con un escenario de stress incrustado:

![Distribución de retornos con VaR y CVaR marcados en la cola izquierda, y simulación Monte Carlo de trayectorias de precio con un escenario de stress]({{ site.baseurl }}/images/risk-management-advanced.svg)

Cómo leer la figura:

- **Panel izquierdo**: el histograma de retornos. La línea **roja punteada** es el VaR 95%: el borde del mapa. La línea **naranja** es el CVaR: el promedio de todo lo que está en la zona sombreada de desastre.
- **Panel derecho**: 100 futuros posibles del precio de un activo (azul), y en **rojo** un escenario de stress con un crash incrustado a mitad del año, donde se anota el *máximo drawdown* — la caída desde la cima hasta el fondo del valle.

Y la salida exacta del programa:

```text
=== Resultados de VaR/CVaR ===
VaR Histórico (95%): -4.21%
CVaR (Expected Shortfall): -6.38%
Ratio CVaR/VaR: 1.52x
```

La lectura en una frase: *"En un día malo (1 de cada 20) pierdes más del 4.21%... y cuando eso pasa, la pérdida típica es del 6.38%"*. **El abismo resulta ser 1.5 veces más profundo de lo que sugiere el borde.** Esa distancia entre VaR y CVaR es exactamente la fragilidad de la que habla Taleb.

## Backtesting: no confíes, verifica

Un modelo de riesgo que nunca se valida es decoración. El *backtesting* cuenta cuántas veces la realidad superó al VaR (esas violaciones deberían ocurrir aproximadamente el 5% de los días, ni muchas más ni muchas menos), y el **test de Kupiec** formaliza esa comparación:

```python
def backtest_var(var_predictions, actual_returns, confidence_level=0.95):
    """Valida el VaR contando violaciones vs las esperadas teóricamente."""
    violations = actual_returns < var_predictions
    n_violations = violations.sum()
    n_observations = len(actual_returns)

    expected_violations = (1 - confidence_level) * n_observations

    return {
        'total_observations': n_observations,
        'violations': n_violations,
        'actual_frequency': n_violations / n_observations,
        'expected_frequency': 1 - confidence_level,
        'frequency_ratio': (n_violations / n_observations) / (1 - confidence_level)
    }
```

Si el `frequency_ratio` es muy mayor que 1, tu VaR es ingenuamente optimista; si es muy menor, estás sobrestimando el peligro (y probablemente dejando dinero sobre la mesa).

## Comparación de métodos

| Método | Fortaleza | Debilidad |
|---|---|---|
| **VaR histórico** | Sin supuestos de distribución; directo | Prisionero del pasado reciente |
| **VaR paramétrico** | Rápido y analítico | Asume normalidad: colas irreales |
| **Monte Carlo** | Flexible; modela correlaciones y escenarios | Computacionalmente intensivo |
| **CVaR** | Coherente; mide la profundidad del desastre | Algo más complejo de calcular |

## Conclusión

1. **El VaR es solo el principio de la conversación**: el CVaR cuenta lo que pasa cuando el VaR falla.
2. **En las crisis, todo se correlaciona**: la diversificación se evapora justo cuando más se necesita; por eso el stress testing asume correlación casi perfecta.
3. **Valida siempre**: un modelo sin backtesting es una opinión disfrazada de número.
4. **Ningún modelo es el territorio**: úsalos en conjunto, y respeta lo que no pueden ver.

---

### Para profundizar

Si este tema te intriga, estas lecturas cambiarán tu forma de ver el riesgo:

- **Nassim Nicholas Taleb** — *The Black Swan* y *Antifragile*: por qué los eventos raros dominan la historia y cómo beneficiarse de ellos.
- **Benoit Mandelbrot** — *The (Mis)behavior of Markets*: por qué los mercados son fractales y la normalidad, un mito.
- **Artzner, Delbaen, Eber & Heath (1999)** — *Coherent Measures of Risk*: el génesis de la gestión de riesgos moderna.
- **Daniel Kahneman** — *Thinking, Fast and Slow*: cómo nuestros sesgos nos hacen subestimar el riesgo.

### Una pregunta para llevar

> *"Si pudieras saber el minuto exacto en que tu fortuna se reducirá a la mitad, ¿cambiarías tu estrategia hoy o confiarías en que eres el único que sabe dónde está la salida de emergencia?"*

Al final, gestionar riesgos no consiste en controlar el futuro, sino en **respetar lo desconocido**.

## Sigue la serie

- **[Frontera Eficiente de Markowitz]({{ site.baseurl }}/frontera-eficiente-markowitz/)**: maximizar el retorno por unidad de riesgo.
- **[Paridad de Riesgo (Risk Parity)]({{ site.baseurl }}/paridad-riesgo-risk-parity/)**: repartir el riesgo en partes iguales entre los activos.

