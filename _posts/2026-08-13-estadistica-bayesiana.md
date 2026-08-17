---
layout: post
title: "Estadística Bayesiana: el Arte de Actualizar Creencias"
use_math: true
published: true
date: 2026-08-13
category: "Estadística"
tags: ["Estadística Bayesiana", "Python"]
thumbnail: "/images/bayesian-inference.svg"
---

Te haces un test médico de una enfermedad rara. El resultado sale **positivo**. El laboratorio te asegura que el test acierta el 99% de las veces. Pregunta incómoda: ¿cuál es la probabilidad de que estés enfermo?

Si respondiste "99%", bienvenido al club: la inmensa mayoría de la gente — incluidos médicos — responde eso. La respuesta real es mucho más baja. Con los números que usaremos aquí, es apenas un **17%**.

Entender *por qué* es el corazón de la estadística bayesiana: la probabilidad no es una propiedad del mundo, sino un **grado de creencia que se actualiza con la evidencia**. Y la regla de actualización la escribió un reverendo del siglo XVIII, Thomas Bayes, cuyo trabajo solo se publicó después de su muerte.

## El teorema de Bayes en una línea

$ \displaystyle P(H \mid E) = \frac{P(E \mid H) \, P(H)}{P(E)} $

Cada pieza tiene nombre y apellido:

- $ H $ es tu **hipótesis** ("estoy enfermo") y $ E $ la **evidencia** ("test positivo").
- $ P(H) $ es el **prior**: lo que creías *antes* de ver la evidencia (la prevalencia de la enfermedad: 1%).
- $ P(E \mid H) $ es la **verosimilitud**: qué tan probable es la evidencia *si* la hipótesis es cierta (la sensibilidad: 99%).
- $ P(H \mid E) $ es el **posterior**: lo que debes creer *después*. Es lo que buscamos.

La fórmula, en palabras: **creencia nueva = (creencia previa × qué tan bien explica la evidencia) ÷ qué tan común es la evidencia**.

## La paradoja del test médico, resuelta a mano

Olvida la fórmula un momento y contemos personas. De cada **100,000** personas, con prevalencia del 1%, sensibilidad del 99% y tasa de falsos positivos del 5%:

- **1,000** están enfermas → el test detecta a **990** (verdaderos positivos).
- **99,000** están sanas → el 5% recibe un falso positivo: **4,950** personas.

Tu test salió positivo: estás en el grupo de $ 990 + 4{,}950 = 5{,}940 $ personas con positivo. ¿Cuántas están realmente enfermas?

$ \displaystyle P(\text{enfermo} \mid +) = \frac{990}{990 + 4{,}950} = \frac{990}{5{,}940} \approx 16.7\% $

**El prior lo es todo**: como la enfermedad es rara, los falsos positivos (5% de un grupo *enorme* de sanos) superan en número a los verdaderos positivos (99% de un grupo *diminuto* de enfermos). Este error — confundir $ P(E \mid H) $ con $ P(H \mid E) $ — tiene nombre propio: la **falacia del fiscal**, y ha mandado a gente inocente a la cárcel en juicios con ADN.

## La moneda dudosa: aprendizaje continuo

El segundo superpoder del enfoque bayesiano es que la actualización es una **cadena**: la posterior de hoy es la prior de mañana. 

Imagina una moneda que sospechas que está sesgada hacia cara. Modelas tu creencia inicial sobre $ \theta $ (la probabilidad de cara) con una distribución **Beta(2, 2)**: "creo que ronda el 50%, pero admito bastante duda". 

La distribución Beta es el compañero natural del experimento de Bernoulli — se llaman *conjugadas* — porque si el prior es $ \text{Beta}(a, b) $ y observas $ k $ caras en $ n $ lanzamientos, la posterior es simplemente:

$ \displaystyle \theta \mid \text{datos} \sim \text{Beta}(a + k, \; b + n - k) $

Actualizar la creencia es *sumar*. No hay integral que resolver, no hay simulación: solo contar caras y cruces. La media de la posterior, $ \frac{a+k}{a+b+n} $, es un promedio ponderado entre tu creencia inicial y la frecuencia observada — y con más datos, pesa más la evidencia. Exactamente como debería razonar una mente racional.

## De la teoría al código

El script completo está en [`scripts/generate_bayesian_inference.py`](https://github.com/carlosfaz/carlosfaz.github.io/blob/main/scripts/generate_bayesian_inference.py). Actualizar la cadena prior → posterior son dos líneas:

```python
import numpy as np
from scipy.stats import beta

# Prior: Beta(2, 2) — "probablemente justa, pero no seguro"
a0, b0 = 2, 2

# Tras observar k caras en n lanzamientos, la posterior ES otra Beta
def actualizar(a, b, n, k):
    """Beta-Binomial: la posterior se obtiene sumando los datos."""
    return a + k, b + (n - k)

a_post, b_post = actualizar(a0, b0, n=50, k=35)
media_posterior = a_post / (a_post + b_post)
```

Y la paradoja del test médico, sin fórmulas: solo contar:

```python
poblacion = 100_000
enfermos = int(poblacion * 0.01)          # prevalencia: 1%
sanos = poblacion - enfermos

verdaderos_pos = int(enfermos * 0.99)     # sensibilidad: 99%
falsos_pos = int(sanos * 0.05)            # tasa de falsos positivos: 5%

p_enfermo_si_positivo = verdaderos_pos / (verdaderos_pos + falsos_pos)
```

## El resultado

![A la izquierda: la distribución posterior se concentra alrededor del sesgo verdadero conforme aumentan los lanzamientos. A la derecha: verdaderos vs falsos positivos en la paradoja del test médico]({{ site.baseurl }}/images/bayesian-inference.svg)

Cómo leer la figura:

- **Panel izquierdo**: la creencia sobre el sesgo de la moneda. La curva gris punteada es el prior Beta(2,2), casi plano: "no sé mucho". Con 10, 50 y 200 lanzamientos, la posterior se va **afinando y centrando** sobre el sesgo verdadero (línea roja, $ p = 0.7 $). Más datos = menos incertidumbre. Eso *es* aprender.
- **Panel derecho**: la paradoja del test médico en una imagen. La barra roja aplasta a la verde: hay **5 veces más** falsos positivos que verdaderos. Por eso un positivo en una enfermedad rara no es (todavía) una sentencia.

La salida del programa:

```text
=== Paradoja del test médico ===
Prevalencia 1%, sensibilidad 99%, tasa de falsos positivos 5%
Verdaderos positivos: 990
Falsos positivos: 4,950
P(enfermo | test positivo) = 990/5940 = 16.7%

=== Beta-Binomial ===
Tras 10 lanzamientos (7 caras):  posterior Beta(9,5),   media = 0.643
Tras 50 lanzamientos (35 caras): posterior Beta(37,17),  media = 0.685
Tras 200 lanzamientos (140 caras): posterior Beta(142,62), media = 0.696
```

Observa la elegancia de la cadena: la media posterior (0.643 → 0.685 → 0.696) se acerca paso a paso al sesgo verdadero (0.70), y la curva se estrecha a su alrededor. La incertidumbre inicial del prior se disuelve en los datos.

## ¿Bayesiano o frecuentista?

El debate clásico de la estadística, en una tabla honesta:

| | Frecuentista | Bayesiano |
|---|---|---|
| **La probabilidad es...** | Frecuencia en largas series | Grado de creencia |
| **Los parámetros son...** | Fijos pero desconocidos | Variables con distribución |
| **Los datos previos...** | No entran en el cálculo | Entran vía el prior |
| **Fortaleza** | Objetividad aparente | Actualización natural y coherente |
| **Debilidad** | No responde "¿qué creo ahora?" | El prior puede ser subjetivo |

En la práctica moderna no hay que elegir bando: el machine learning bayesiano, los filtros de spam, la búsqueda del Higgs y los tests A/B usan esta maquinaria todos los días.

## Conclusión

1. **$ P(E \mid H) \neq P(H \mid E) $**: confundirlas es la falacia del fiscal; el prior lo cambia todo.
2. **Creer es un verbo dinámico**: la posterior de hoy es la prior de mañana.
3. **Los conjugados son un regalo**: con Beta-Binomial, aprender es literalmente *sumar*.
4. **Ante un resultado sorprendente, pregunta por la tasa base**: es el hábito mental más barato y más poderoso que te llevas hoy.

## Sigue explorando

- **[Gestión de Riesgos Avanzada]({{ site.baseurl }}/gestion-riesgos-avanzada/)**: otra forma de cuantificar lo inesperado, esta vez en los mercados.
- **[Prueba de Wilcoxon]({{ site.baseurl }}/wilcoxon-rangos-signo/)**: cuando no puedes asumir normalidad, la estadística no paramétrica al rescate.

