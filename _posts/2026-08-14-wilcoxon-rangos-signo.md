---
layout: post
title: "No Paramétrica: la Prueba de los Rangos con Signo de Wilcoxon"
use_math: true
published: true
date: 2026-08-14
category: "Estadística"
tags: ["Estadística No Paramétrica", "Pruebas de Hipótesis", "Python"]
thumbnail: "/images/wilcoxon-signed-rank.svg"
---

La prueba *t* de Student — la estrella de cualquier curso de estadística — esconde una letra pequeña: **asume que los datos siguen una distribución normal**. Con muestras grandes, el teorema central del límite te salva. Pero con 12 observaciones y un valor atípico enorme, esa suposición se convierte en un castillo de naipes.

¿Y si te dijera que existe una prueba que no necesita la normalidad, que es inmune a los outliers y que aun así conserva casi toda la potencia de la *t*? Frank Wilcoxon la publicó en 1945, en un artículo de apenas 3 páginas: la **prueba de los rangos con signo**.

> La idea en una frase: **no uses los valores brutos de los datos, usa su *orden*.** Un outlier deja de ser un monstruo y se convierte simplemente en "el más grande".

## El problema: comparar "antes" y "después"

Doce participantes toman una prueba de habilidad, siguen un programa de entrenamiento y repiten la prueba. Queremos saber si el programa *funciona*, es decir, si la mediana de las diferencias es distinta de cero:

$ \displaystyle H_0: \; \text{mediana}(D) = 0 \qquad \text{vs} \qquad H_1: \; \text{mediana}(D) \neq 0 $

donde $ D_i = \text{después}_i - \text{antes}_i $. Nuestros datos tienen trampa incluida: una mejora atípica de **25 puntos** (¿un genio? ¿un error de captura?) que inflaría la varianza y maltrataría a la prueba *t*.

## El procedimiento en 5 pasos

Wilcoxon transforma los datos en rangos con una receta elegante:

1. **Calcula las diferencias** $ D_i $ por pareja y descarta las que sean cero.
2. **Toma los valores absolutos** $ |D_i| $.
3. **Asigna rangos** del 1 al $ m $ según su magnitud (el más pequeño recibe el 1).
4. **Devuelve el signo** a cada rango y suma por separado: $ W^+ $ (rangos de las diferencias positivas) y $ W^- $ (el de las negativas).
5. El estadístico es $ W = \min(W^+, W^-) $. Si $ H_0 $ fuera cierta, ambos deberían andar parejos; un $ W $ muy pequeño delata el desequilibrio.

Fíjate en lo astuto del paso 3: el outlier de 25 puntos recibe simplemente *el rango más alto*. Su magnitud exagerada queda **domada** — vale lo mismo que si hubiera sido un 12.

### ¿Cuándo es "demasiado pequeño"?

Bajo $ H_0 $, con $ m $ diferencias no nulas, $ W $ se comporta aproximadamente como una normal con:

$ \displaystyle \mu_W = \frac{m(m+1)}{4}, \qquad \sigma_W = \sqrt{\frac{m(m+1)(2m+1)}{24}} $

lo que permite calcular un $ z $ y un p-valor sin tablas exóticas: $ \displaystyle z = \frac{W - \mu_W}{\sigma_W} $.

## De la receta al código

Primero, el cálculo **manual** — porque entender es poder. El script completo está en [`scripts/generate_wilcoxon_test.py`](https://github.com/carlosfaz/carlosfaz.github.io/blob/main/scripts/generate_wilcoxon_test.py):

```python
import numpy as np
from scipy.stats import rankdata, wilcoxon

diferencias = despues - antes

# 1) Descartar ceros, 2) magnitudes, 3) rangos, 4) signos
no_cero = diferencias[diferencias != 0]
rangos = rankdata(np.abs(no_cero))
signos = np.sign(no_cero)

W_pos = np.sum(rangos[signos > 0])   # Suma de rangos positivos
W_neg = np.sum(rangos[signos < 0])   # Suma de rangos negativos
W = min(W_pos, W_neg)                # Estadístico de Wilcoxon
```

Y la verificación profesional con `scipy`, en una sola línea:

```python
result = wilcoxon(despues, antes)   # W y p-valor exacto
print(result.statistic, result.pvalue)
```

## El resultado

![A la izquierda: puntuaciones antes y después por participante. A la derecha: las diferencias ordenadas por magnitud, con el rango asignado y su signo]({{ site.baseurl }}/images/wilcoxon-signed-rank.svg)

Cómo leer la figura:

- **Panel izquierdo**: cada línea conecta el "antes" y el "después" de un participante. Casi todas suben (verde); solo dos bajan ligeramente (rojo). A simple vista ya sospechas que el programa funciona.
- **Panel derecho**: el corazón de la prueba. Las diferencias ordenadas por magnitud reciben su rango (1 al 12), y el color conserva el signo. Fíjate en el **outlier de 25 puntos**: en una prueba *t* ese valor inflaría la varianza y distorsionaría todo; aquí es simplemente "el rango 12". Domado.

La salida del programa:

```text
=== Wilcoxon (cálculo manual) ===
Diferencias: [5, 8, 3, 6, -2, 7, 4, 25, 6, -1, 9, 5]
W+ (rangos positivos) = 75.0
W− (rangos negativos) = 3.0
W = min(W+, W−) = 3.0
Aproximación normal: z = -2.824, p ≈ 0.0047

=== Verificación scipy ===
scipy.stats.wilcoxon: W = 3.0, p-valor = 0.0024
Mediana antes: 71.5 | Mediana después: 76.0
```

**Interpretación**: de los 78 puntos de rango disponibles, las mejoras acaparan 75 y los retrocesos apenas 3. Con un p-valor de **0.0024** (scipy, exacto) — y 0.0047 con la aproximación normal — rechazamos $ H_0 $ con total comodidad: **el programa de entrenamiento sí mejora las puntuaciones** (mediana: de 71.5 a 76.0). Y lo demostramos sin haber asumido normalidad en ningún paso.

## ¿Wilcoxon o la prueba t?

| | Prueba *t* pareada | Wilcoxon |
|---|---|---|
| **Supuesto clave** | Diferencias normales | Solo simetría en las diferencias |
| **Sensibilidad a outliers** | Alta (usan medias y varianzas) | Casi nula (usan rangos) |
| **¿Qué contrasta?** | La media | La mediana (rangos) |
| **Potencia con normalidad** | Óptima | ~95% de la *t* (¡casi nada que perder!) |
| **Muestras pequeñas** | Riesgosa | Recomendada |

## Conclusión

1. **Los rangos domesticen a los outliers**: el valor más grande es solo "el rango más alto".
2. **Menos supuestos, misma fuerza**: Wilcoxon conserva ~95% de la potencia de la *t* incluso cuando la normalidad sí se cumple.
3. **El procedimiento es transparente**: cinco pasos que puedes hacer a mano con lápiz y papel — y verificar con una línea de `scipy`.
4. **Regla práctica**: muestra pequeña, distribución dudosa u outliers presentes → Wilcoxon.

## Sigue explorando

- **[Estadística Bayesiana]({{ site.baseurl }}/estadistica-bayesiana/)**: otra forma de pensar la inferencia — actualizando creencias en lugar de contrastar hipótesis.
- **[Gestión de Riesgos Avanzada]({{ site.baseurl }}/gestion-riesgos-avanzada/)**: donde los outliers no se doman, se estudian — son las colas de la distribución.

