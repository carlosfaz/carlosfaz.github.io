---
layout: post
title: "El precio de romper la simetría: por qué existe más materia que antimateria"
use_math: true
published: true
date: 2026-08-28
category: "Cosmología"
tags: ["Cosmología", "Física Estadística", "Termodinámica"]
thumbnail: "/images/symmetry-breaking.svg"
---

En los primeros instantes del Universo, materia y antimateria formaban un plasma extremadamente caliente y denso. Partículas y antipartículas — regidas por leyes casi perfectamente simétricas — aparecían y desaparecían en cantidades prácticamente idénticas. *Prácticamente.*

> Si la física trata la materia y la antimateria con el mismo respeto... **¿por qué quedó algo en lugar de nada?**

Esa casi simetría es lo único que separa nuestro cosmos de un desierto de radiación enfriándose para siempre. La física estadística permite describir el misterio con precisión quirúrgica: toda la materia visible puede codificarse en un único número — la razón adimensional entre el potencial químico y la temperatura del plasma primordial. En este artículo reconstruimos esa cuenta paso a paso, sin dar nada por sabido.

## El plasma primordial: un caldo donde la masa no importa

Imaginemos el Universo cuando era extremadamente joven: un espacio lleno de partículas, antipartículas y radiación, a temperaturas tan elevadas que las colisiones entre ellas ocurrían continuamente.

En este régimen, la energía térmica típica de las partículas es mucho mayor que sus masas:

$ \displaystyle T \gg m $

por lo que podemos trabajar en el régimen **ultrarrelativista**, donde la relación entre energía y momento se aproxima por

$ \displaystyle E = \sqrt{p^2 + m^2} \simeq p $

No estamos diciendo que las partículas carezcan de masa: simplemente, su energía térmica es tan grande comparada con su masa que esta puede despreciarse en primera aproximación.

En este caldo primordial conviven fermiones y sus correspondientes antipartículas. Para describirlos estadísticamente usaremos la distribución de **Fermi–Dirac**, y trabajaremos en unidades naturales,

$ \displaystyle c = \hbar = k_B = 1 $

de modo que temperatura, energía, masa y momento se expresan en las mismas unidades.

## El potencial químico: el precio de preferir la materia

Supongamos que $ n $ es la densidad numérica de partículas y $ \bar{n} $ la de antipartículas. Si el Universo fuese perfectamente simétrico entre materia y antimateria, esperaríamos

$ \displaystyle n = \bar{n} $

Pero podemos permitir una pequeña diferencia introduciendo un **potencial químico** $ \mu $. La intuición es directa: $ \mu $ mide cuánto favorece el sistema la presencia de partículas frente a la de antipartículas. Para las antipartículas, el potencial aparece con signo contrario — penalizar a una especie es exactamente lo mismo que favorecer a su espejo.

La distribución de Fermi–Dirac nos da entonces

$ \displaystyle n = \frac{g}{2\pi^2} \int_0^\infty \frac{p^2\, dp}{e^{(p-\mu)/T} + 1} $

mientras que para las antipartículas tenemos

$ \displaystyle \bar{n} = \frac{g}{2\pi^2} \int_0^\infty \frac{p^2\, dp}{e^{(p+\mu)/T} + 1} $

Aquí $ g $ representa el número de **grados de libertad internos** de la partícula, como los asociados al espín. Fíjate en el detalle decisivo: en el integrando de $ n $ aparece $ -\mu $ y en el de $ \bar{n} $, $ +\mu $.

## La integral que nadie quiere resolver (y el truco para esquivarla)

Restando ambas expresiones obtenemos la asimetría neta:

$ \displaystyle n - \bar{n} = \frac{g}{2\pi^2} \int_0^\infty p^2 \left[ \frac{1}{e^{(p-\mu)/T}+1} - \frac{1}{e^{(p+\mu)/T}+1} \right] dp $

Para simplificar, separamos la temperatura del resto introduciendo variables adimensionales:

$ \displaystyle x = \frac{p}{T}, \qquad \xi = \frac{\mu}{T} $

La variable $ \xi $ será la protagonista del artículo: mide el potencial químico en unidades de temperatura. Como $ p = xT $ y $ dp = T\, dx $, obtenemos

$ \displaystyle n - \bar{n} = \frac{g\, T^3}{2\pi^2}\, I(\xi), \qquad I(\xi) = \int_0^\infty x^2 \left[ \frac{1}{e^{x-\xi}+1} - \frac{1}{e^{x+\xi}+1} \right] dx $

A primera vista, resolver directamente esta integral no parece especialmente agradable. Pero hay una estrategia sencilla: en lugar de atacarla de frente, estudiamos **cómo cambia cuando modificamos $ \xi $**. Las derivadas respecto de $ \xi $ simplifican progresivamente la estructura de las distribuciones de Fermi–Dirac; después de dos derivadas, la potencia $ x^2 $ puede eliminarse mediante integración por partes. El resultado es

$ \displaystyle \frac{d^2 I}{d\xi^2} = 2 \int_0^\infty \left[ \frac{1}{e^{x-\xi}+1} - \frac{1}{e^{x+\xi}+1} \right] dx $

Las integrales que quedan son elementales:

$ \displaystyle \int_0^\infty \frac{dx}{e^{x-\xi}+1} = \ln\!\left(1+e^{\xi}\right), \qquad \int_0^\infty \frac{dx}{e^{x+\xi}+1} = \ln\!\left(1+e^{-\xi}\right) $

Y la diferencia de logaritmos colapsa en algo casi cómico:

$ \displaystyle \ln\!\left(1+e^{\xi}\right) - \ln\!\left(1+e^{-\xi}\right) = \xi $

Reuniendo todo queda una ecuación de lo más inofensiva:

$ \displaystyle \frac{d^2 I}{d\xi^2} = 2\,\xi $

Ahora solo hay que integrar dos veces. La primera integración da

$ \displaystyle \frac{dI}{d\xi} = \xi^2 + C_1 $

Para determinar $ C_1 $ evaluamos la expresión en $ \xi = 0 $, el caso en que partículas y antipartículas tienen exactamente la misma distribución. El cálculo usa la integral clásica $ \int_0^\infty \frac{x\,dx}{e^x+1} = \left(1-2^{-1}\right)\Gamma(2)\,\zeta(2) = \frac{\pi^2}{12} $ y el factor 2 que introduce la simetría entre ambas poblaciones. El resultado es

$ \displaystyle I'(0) = 2 \cdot \frac{\pi^2}{12} = \frac{\pi^2}{3} \quad\Longrightarrow\quad C_1 = \frac{\pi^2}{3} $

Integrando una segunda vez:

$ \displaystyle I(\xi) = \frac{\xi^3}{3} + \frac{\pi^2}{3}\, \xi + C_2 $

La constante $ C_2 $ sale de una condición de frontera muy sencilla: si $ \xi = 0 $, los dos sumandos del integrando se cancelan uno a uno y por tanto

$ \displaystyle I(0) = 0 \quad\Longrightarrow\quad C_2 = 0 $

El resultado final, en su forma más elegante:

$ \displaystyle I(\xi) = \frac{\pi^2}{3}\, \xi \left[ 1 + \left( \frac{\xi}{\pi} \right)^2 \right] $

Recordando que $ \xi = \mu/T $:

$ \displaystyle n - \bar{n} = \frac{g\, T^2\, \mu}{6} \left[ 1 + \left( \frac{\mu}{\pi T} \right)^2 \right] $

Este resultado tiene una interpretación física sencilla. Si $ \mu = 0 $, entonces $ n - \bar{n} = 0 $, como debe ocurrir en un sistema perfectamente simétrico. Para un potencial químico pequeño, $ |\mu| \ll T $, podemos despreciar los términos de orden superior:

$ \displaystyle n - \bar{n} \simeq \frac{g}{6}\, \mu\, T^2 $

**La asimetría es lineal en el potencial químico** cuando este es pequeño, y la primera corrección relativa es proporcional a $ (\mu/\pi T)^2 $. La razón $ \mu / T $ es, por tanto, la medida natural de cuán importante es la asimetría química frente a la energía térmica del plasma.

## La entropía: el caos compartido

La asimetría $ n - \bar{n} $ sola no basta para la cosmología, porque el Universo se expande: las densidades se diluyen y los volúmenes cambian. Necesitamos un recipiente que no se desvanezca con el tiempo, y ese recipiente es la **entropía**. En un universo en expansión, la entropía por volumen comóvil se conserva: es el número que el paso del tiempo no borra.

Para un gas relativista en equilibrio, la relación

$ \displaystyle s = \frac{\rho + p - \mu\, n}{T} $

conecta la densidad de entropía con la densidad de energía, la presión, el potencial químico y la densidad de partículas. Para las antipartículas, el potencial químico cambia de signo:

$ \displaystyle \bar{s} = \frac{\bar{\rho} + \bar{p} + \mu\, \bar{n}}{T} $

Sumando ambas expresiones y usando la ecuación de estado ultrarrelativista $ p = \rho/3 $ (y su análoga $ \bar{p} = \bar{\rho}/3 $):

$ \displaystyle s + \bar{s} = \frac{4}{3T}(\rho + \bar{\rho}) - \frac{\mu}{T}(n - \bar{n}) $

Necesitamos, pues, la densidad de energía del plasma. Repitiendo el mismo tipo de cálculo con las integrales de Fermi–Dirac — y con la ayuda de $ \zeta(4) = \pi^4/90 $ — se obtiene

$ \displaystyle \rho + \bar{\rho} = g\, T^4 \left[ \frac{7\pi^2}{120} + \frac{\xi^2}{4} + \frac{\xi^4}{8\pi^2} \right] $

Combinando las piezas aparece una de las cancelaciones más elegantes de la física: los términos de cuarto orden en $ \xi $, presentes en $ \frac{4}{3T}(\rho+\bar{\rho}) $ y en $ \frac{\mu}{T}(n - \bar{n}) $, se anulan entre sí **exactamente**. El resultado:

$ \displaystyle s + \bar{s} = g\, T^3 \left[ \frac{7\pi^2}{90} + \frac{\xi^2}{6} \right] $

Dos lecturas. Primera: en ausencia de asimetría, $ s + \bar{s} = \frac{7\pi^2}{90}\, g\, T^3 $ — la dependencia $ T^3 $ es característica de un gas relativista: al subir la temperatura, explota el número de estados térmicamente accesibles y, con ellos, el desorden por unidad de volumen. Segunda: la entropía **no cambia de signo** cuando invertimos $ \mu $ — aparece $ \xi^2 $, no $ \xi $. Tiene todo el sentido: intercambiar cuál de las dos poblaciones es ligeramente mayor no debería alterar la cantidad total de desorden térmico. El caos no toma partido.

## El cociente que sobrevive al Universo

Ya tenemos las dos piezas. La combinación que realmente importa en cosmología es

$ \displaystyle \frac{n - \bar{n}}{s + \bar{s}} $

¿Por qué esta y no otra? Porque tanto $ n - \bar{n} $ como $ s + \bar{s} $ dependen fuertemente de la temperatura y de $ g $, pero al dividirlas los factores $ g\, T^3 $ se cancelan. Obtenemos una **magnitud adimensional** que caracteriza la asimetría de materia frente al desorden total y que no se diluye con la expansión del Universo.

Usando nuestros resultados:

$ \displaystyle \frac{n - \bar{n}}{s + \bar{s}} = \frac{ \frac{1}{6}\left( \xi + \frac{\xi^3}{\pi^2} \right) }{ \frac{7\pi^2}{90} + \frac{\xi^2}{6} } $

Para una asimetría pequeña, $ |\xi| \ll 1 $, podemos quedarnos con los términos dominantes:

$ \displaystyle n - \bar{n} \simeq \frac{g\, T^3}{6}\,\xi, \qquad s + \bar{s} \simeq \frac{7\pi^2}{90}\, g\, T^3 $

de donde resulta

$ \displaystyle \boxed{ \frac{n - \bar{n}}{s + \bar{s}} \simeq \frac{15}{7\pi^2}\, \frac{\mu}{T} \approx 0{,}217\, \frac{\mu}{T} } $

Ahí está la conclusión central del artículo: **los factores $ gT^3 $ se cancelan, y la asimetría relativa deja de depender directamente de la temperatura para quedar controlada — en primera aproximación — por la razón adimensional $ \mu / T $.**

![Cociente (n−n̄)/(s+s̄) frente a ξ = μ/T. Izquierda: curva exacta vs aproximación lineal. Derecha: escala log-log, con la posición del Universo observado marcada con una estrella.]({{ site.baseurl }}/images/symmetry-breaking.svg)

Cómo leer la figura:

- **Panel izquierdo**: el cociente exacto (curva verde) contra su aproximación lineal (curva roja discontinua). Son indistinguibles en el régimen $ \xi \ll 1 $; a partir de $ \xi \sim 1 $ la corrección cúbica las separa.
- **Panel derecho**: la misma historia en escala log-log. La pendiente 1 de la zona izquierda es el régimen lineal; la desviación empieza cerca de $ \xi \sim 1 $. La estrella marca dónde vive el Universo real: una asimetría diminuta que aterriza exactamente en el régimen lineal.

¿Y cuánto vale ese número en el mundo real? Las observaciones cosmológicas fijan la asimetría bariónica en torno a

$ \displaystyle \frac{n - \bar{n}}{s + \bar{s}} \sim 10^{-10} \quad\Longrightarrow\quad \xi = \frac{\mu}{T} \sim 4 \times 10^{-10} $

Es decir: todo el desequilibrio que explica la existencia de la materia visible cabe en una razón de **una parte en diez mil millones**.

## Una pequeña asimetría con consecuencias enormes

El Universo temprano podía estar compuesto por cantidades enormes de materia y antimateria, casi perfectamente equilibradas — pero no necesariamente de manera exacta.

Si existía una pequeñísima preferencia por la materia, entonces

$ \displaystyle n > \bar{n} $

A medida que el Universo se expandía y se enfriaba, materia y antimateria podían aniquilarse mutuamente. Si la simetría hubiese sido perfecta, al final apenas quedaría materia: un cosmos de radiación enfriándose para siempre. Pero si existía una pequeña asimetría inicial, después de las aniquilaciones podía sobrevivir un exceso residual de materia.

En este sentido, una diferencia microscópica entre $ n $ y $ \bar{n} $ acaba determinando la existencia de toda la materia ordinaria que observamos hoy: estrellas, planetas, carbón y nosotros. La física estadística muestra cómo esa pequeña diferencia se conecta con cantidades tan fundamentales como la temperatura del Universo y el potencial químico de las partículas:

$ \displaystyle \boxed{ \text{asimetría materia–antimateria} \quad\longleftrightarrow\quad \frac{\mu}{T} } $

Y detrás de una diferencia aparentemente diminuta se esconde una de las preguntas más profundas de la cosmología:

> **¿Por qué existe más materia que antimateria en el Universo?**

La respuesta completa requiere física adicional — en particular, procesos capaces de *generar* y *preservar* una asimetría de materia sobre antimateria. Pero las ecuaciones de este artículo muestran algo valioso: cómo puede describirse cuantitativamente esa asimetría **una vez que existe**. La termodinámica del plasma primordial es el molde; el motivo por el que la simetría se rompió sigue siendo un misterio — y su precio, medido hoy, es una parte en diez mil millones.

## Conclusiones

1. **Todo depende de una sola razón adimensional**: $ \mu / T $ — el potencial químico medido en unidades de temperatura.
2. **La asimetría es lineal en $ \mu $; la entropía, cuadrática**: preferir un bando tiene un coste neto, pero el desorden total no se entera de quién gana.
3. **El cociente $ (n-\bar{n})/(s+\bar{s}) $ sobrevive a la expansión**: los $ gT^3 $ se cancelan, y por eso los cosmólogos miden asimetrías relativas a la entropía y no densidades absolutas.
4. **Una asimetría microscópica produce un Universo entero**: $ \mu/T \sim 10^{-10} $ separa el vacío absoluto de todo lo que existe.
5. Explicar *por qué* existe esa asimetría es el problema abierto; describirla *una vez que existe* se reduce a una cuenta limpia de física estadística.

La próxima vez que mires el cielo estrellado, recuerda la operación aritmética que lo sostiene: una parte en diez mil millones. Ese fue el precio de romper la simetría — y el Universo entero es el interés compuesto.

## Sigue la serie

- **[Tetración Truncada]({{ site.baseurl }}/tetracion-truncada-integral/)**: otro ejemplo de cómo un truco matemático evita una integral imposible.
- **[Teoría de la Ruina]({{ site.baseurl }}/teoria-ruina/)**: cuando un desequilibrio diminuto decide, también en finanzas, quién sobrevive en el largo plazo.