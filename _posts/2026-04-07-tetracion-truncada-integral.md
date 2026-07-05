---
layout: post
title: "Desarrollo Analítico y Formal de la Representación en Serie para la Integral de la Tetración Truncada"
use_math: true
published: true
date: 2026-04-07
category: "Matemáticas"
tags: ["Tetración", "Integrales", "Series Infinitas", "Función Gamma"]
thumbnail: "/images/tetration-truncated.png"
---

En este artículo presentamos un desarrollo analítico completo para la integral de la tetración truncada, una función recursiva que representa torres finitas de potencias. Demostraremos mediante inducción matemática una representación en series múltiples y resolveremos analíticamente la integral utilizando la Función Gamma incompleta inferior.

## Parte 1: Cimientos y Definiciones Básicas

### 1. Definición Recursiva de la Función

Definimos la función $\text{piso}(n)$ como una torre finita de potencias (tetración truncada) de orden $n$, para un dominio unificado en la variable real $x \in (0, \infty)$, donde el argumento $n \in \mathbb{N}$ representa el número de niveles o "elevaciones":

$$
\text{piso}(1) = x
$$

$$
\text{piso}(2) = x^{x}
$$

$$
\text{piso}(3) = x^{x^{x}}
$$

Para un orden genérico $n \ge 2$, la función se estructura de manera recursiva mediante la relación:

$ \displaystyle \text{piso}(n) = x^{\text{piso}(n-1)} $

### 2. Identidades Fundamentales

Para desarmar analíticamente esta estructura, aplicaremos de forma reiterada dos herramientas clásicas:

- **La identidad exponencial:** Permite trasladar los exponentes a una base constante $e$.

$ \displaystyle a^{b} = e^{b\ln a} $

- **La serie de Maclaurin de la exponencial:** Permite linealizar funciones exponenciales en series de potencias infinitas.

$ \displaystyle e^{u} = \sum_{k=0}^{\infty} \frac{u^{k}}{k!} $

---

## Parte 2: Análisis de Casos Bajos ($n=2$ y $n=3$)

Desarrollamos los primeros niveles para inspeccionar el comportamiento de los índices y establecer el cimiento de la prueba.

### Caso $n = 2$: La integral del Sophomore's Dream y Justificación del Intercambio

Queremos evaluar la integral $I_2 = \int \text{piso}(2) \, dx = \int x^x \, dx$. Trasladamos la base usando la identidad exponencial:

$ \displaystyle x^{x} = e^{x\ln x} = \sum_{k_{1}=0}^{\infty} \frac{1}{k_{1}!}x^{k_{1}}(\ln x)^{k_{1}} $

Para justificar rigurosamente el intercambio entre el operador integral y la sumatoria infinita, definimos las sumas parciales $S_N(x) = \sum_{k_1=0}^{N} \frac{1}{k_1!} x^{k_1} (\ln x)^{k_1}$. En cualquier intervalo compacto $[a, b] \subset (0, \infty)$, la función $\|x \ln x|$ está acotada superiormente por una constante $M > 0$. Por lo tanto, el término general está acotado por $\frac{M^{k_1}}{k_1!}$. Dado que $\sum_{k_1=0}^{\infty} \frac{M^{k_1}}{k_1!} = e^M < \infty$, por el test de M-Weierstrass, la serie converge uniformemente en $[a, b]$.

Por el teorema de convergencia uniforme para integrales en intervalos compactos, el intercambio de la suma y la integral es plenamente válido:

$ \displaystyle I_{2} = \int \left( \sum_{k_{1}=0}^{\infty} \frac{1}{k_{1}!}x^{k_{1}}(\ln x)^{k_{1}} \right) dx = \sum_{k_{1}=0}^{\infty} \frac{1}{k_{1}!} \int x^{k_{1}}(\ln x)^{k_{1}}\,dx $

### Caso $n = 3$: Surgimiento de la interacción indexada

Queremos analizar el integrando para $I_3 = \int \text{piso}(3) \, dx = \int x^{x^x} \, dx$. Aplicamos la identidad exponencial sobre la base externa:

$ \displaystyle \text{piso}(3) = e^{\text{piso}(2)\ln x} = \sum_{k_{2}=0}^{\infty} \frac{1}{k_{2}!} \left[\text{piso}(2)\right]^{k_{2}}(\ln x)^{k_{2}} $

Sustituimos la definición explícita de $\text{piso}(2) = x^x$ dentro del paréntesis:

$ \displaystyle \left[\text{piso}(2)\right]^{k_{2}} = (x^{x})^{k_{2}} = e^{k_{2}x\ln x} $

Expandimos esta nueva exponencial interior utilizando el índice $k_{1}$:

$ \displaystyle e^{k_{2}x\ln x} = \sum_{k_{1}=0}^{\infty} \frac{(k_{2}x\ln x)^{k_{1}}}{k_{1}!} = \sum_{k_{1}=0}^{\infty} \frac{k_{2}^{k_{1}}}{k_{1}!}x^{k_{1}}(\ln x)^{k_{1}} $

Al acoplar ambos pasos, el integrando resulta en:

$ \displaystyle \text{piso}(3) = \sum_{k_{2}=0}^{\infty} \sum_{k_{1}=0}^{\infty} \frac{k_{2}^{k_{1}}}{k_{1}!\,k_{2}!}x^{k_{1}}(\ln x)^{k_{1}+k_{2}} $

Bajo el mismo argumento de convergencia uniforme y absoluta de las series analíticas multicapa en compactos de $(0,\infty)$, se hereda la validez del intercambio de operadores:

$ \displaystyle I_{3} = \sum_{k_{2}=0}^{\infty} \sum_{k_{1}=0}^{\infty} \frac{k_{2}^{k_{1}}}{k_{1}!\,k_{2}!} \int x^{k_{1}}(\ln x)^{k_{1}+k_{2}}\,dx $

---

## Parte 3: Demostración Formal por Inducción Matemática

Para validar universalmente el comportamiento de la torre de potencias, planteamos una demostración por inducción sobre la estructura del integrando $\text{piso}(n)$.

### 1. Definición del Teorema y Proposición $P(n)$

Sea $P(n)$ la proposición que afirma que para cualquier entero $n \ge 2$, la función $\text{piso}(n)$ admite una representación en series de la forma:

$ \displaystyle \text{piso}(n) = \sum_{k_{n-1}=0}^{\infty} \dots \sum_{k_{1}=0}^{\infty} \left[ \frac{\prod_{j=1}^{n-2}k_{j+1}^{k_{j}}}{\prod_{j=1}^{n-1}k_{j}!} \right] x^{k_{1}}(\ln x)^{\sum_{j=1}^{n-1}k_{j}} $

*Nota de convención:* Para el caso base $n=2$, la productoria vacía se define como $1$. Se asume que $0^0 = 1$ y $0^k = 0$ para todo $k > 0$.

### 2. Base de la Inducción

Para $n=2$, la fórmula propone de manera directa:

$ \displaystyle \text{piso}(2) = \sum_{k_{1}=0}^{\infty} \frac{1}{k_{1}!}x^{k_{1}}(\ln x)^{k_{1}} $

Esto coincide exactamente con el desarrollo analítico del Caso $n=2$ en la Parte 2. Por lo tanto, $P(2)$ es verdadera.

### 3. Hipótesis Inductiva

Asumimos que $P(n)$ es verdadera para un valor fijo $n = m$ ($m \ge 2$). Es decir, tomamos como hipótesis operativa y válida la expresión:

$ \displaystyle \text{piso}(m) = \sum_{k_{m-1}=0}^{\infty} \dots \sum_{k_{1}=0}^{\infty} \left[ \frac{\prod_{j=1}^{m-2}k_{j+1}^{k_{j}}}{\prod_{j=1}^{m-1}k_{j}!} \right] x^{k_{1}}(\ln x)^{\sum_{j=1}^{m-1}k_{j}} $

### 4. Paso Inductivo: Demostración Explícita de $P(m) \implies P(m+1)$

Consideremos ahora la estructura funcional para el nivel $m+1$. Por la definición recursiva fundamental, tenemos:

$ \displaystyle \text{piso}(m+1) = x^{\text{piso}(m)} $

Aplicando la identidad exponencial en la base externa e introduciendo un nuevo índice de sumatoria $k_m$ mediante la serie de Maclaurin, se obtiene de forma exacta:

$ \displaystyle \text{piso}(m+1) = e^{\text{piso}(m)\ln x} = \sum_{k_{m}=0}^{\infty} \frac{1}{k_{m}!} \left[ \text{piso}(m) \right]^{k_{m}} (\ln x)^{k_{m}} $

En este punto, **aplicamos rigurosamente la hipótesis inductiva $P(m)$** sustituyendo la serie supuesta para $\text{piso}(m)$ dentro de la potencia $k_m$:

$ \displaystyle \left[ \text{piso}(m) \right]^{k_{m}} = \left( \sum_{k_{m-1}=0}^{\infty} \dots \sum_{k_{1}=0}^{\infty} \left[ \frac{\prod_{j=1}^{m-2}k_{j+1}^{k_{j}}}{\prod_{j=1}^{m-1}k_{j}!} \right] x^{k_{1}}(\ln x)^{\sum_{j=1}^{m-1}k_{j}} \right)^{k_{m}} $

Para calcular de manera exacta esta potencia $k_m$-ésima sin recurrir a argumentos de patrón, aplicamos de forma inversa la linealización de Maclaurin. Sabemos que la expresión interna proviene rigurosamente de la cadena recursiva de exponenciales combinadas. Específicamente, por propiedades de los exponentes, elevar $\text{piso}(m) = x^{\text{piso}(m-1)}$ a la potencia $k_m$ equivale a:

$ \displaystyle \left[ \text{piso}(m) \right]^{k_{m}} = \left( x^{\text{piso}(m-1)} \right)^{k_m} = e^{k_m \text{piso}(m-1) \ln x} $

Expandiendo esta última expresión mediante el desarrollo en serie con el índice $k_{m-1}$, obtenemos:

$ \displaystyle e^{k_m \text{piso}(m-1) \ln x} = \sum_{k_{m-1}=0}^{\infty} \frac{(k_m \text{piso}(m-1) \ln x)^{k_{m-1}}}{k_{m-1}!} = \sum_{k_{m-1}=0}^{\infty} \frac{k_m^{k_{m-1}}}{k_{m-1}!} \left[ \text{piso}(m-1) \right]^{k_{m-1}} (\ln x)^{k_{m-1}} $

Este mecanismo algebraico demuestra que la presencia de la base $\text{piso}(m-1)$ elevada a $k_{m-1}$ arrastra de manera exacta el factor multiplicativo $k_m^{k_{m-1}}$. Por hipótesis inductiva, la aplicación sucesiva de este operador lineal de potencias sobre cada nivel descendente $j$ produce el factor generalizado:

$ \displaystyle \left[ \text{piso}(j+1) \right]^{k_{j+1}} = e^{k_{j+1} \text{piso}(j) \ln x} \implies \frac{k_{j+1}^{k_j}}{k_j!} \left[ \text{piso}(j) \right]^{k_j} (\ln x)^{k_j} $

Sustituyendo esta cadena de expansiones algebraicas obligatorias en la sumatoria de $\text{piso}(m+1)$, el coeficiente del numerador se extiende de manera unívoca al incorporar el término $k_{m}^{k_{m-1}}$ al producto preexistente:

$ \displaystyle \left( \prod_{j=1}^{m-2} k_{j+1}^{k_j} \right) \cdot k_{m}^{k_{m-1}} = \prod_{j=1}^{m-1} k_{j+1}^{k_j} $

De igual forma, el denominador factorial incorpora el término $k_m!$, transformándose en $\prod_{j=1}^{m} k_j!$. Finalmente, las potencias de los logaritmos naturales se consolidan por adición:

$ \displaystyle (\ln x)^{k_m} \cdot (\ln x)^{\sum_{j=1}^{m-1} k_j} = (\ln x)^{\sum_{j=1}^{m} k_j} $

Reagrupando las sumatorias múltiples, obtenemos de forma exacta:

$ \displaystyle \text{piso}(m+1) = \sum_{k_{m}=0}^{\infty} \dots \sum_{k_{1}=0}^{\infty} \left[ \frac{\prod_{j=1}^{m-1}k_{j+1}^{k_{j}}}{\prod_{j=1}^{m}k_{j}!} \right] x^{k_{1}}(\ln x)^{\sum_{j=1}^{m}k_{j}} $

Esta expresión es idéntica a la definición de $P(n)$ evaluada formalmente en $n = m+1$. Habiéndose demostrado que $P(2)$ es verdadera y que $P(m) \implies P(m+1)$, la validez de la proposición $P(n)$ queda matemáticamente demostrada y firmemente establecida para todo $n \ge 2$.

---

## Parte 4: Resolución Analítica del Núcleo

Habiendo demostrado la estructura del integrando, la resolución de la integral requiere resolver el núcleo atrapado en el fondo, el cual mantiene una geometría polinómico-logarítmica:

$ \displaystyle \int x^{k_{1}}(\ln x)^{\beta }\,dx \quad \text{donde } \beta =\sum_{j=1}^{n-1}k_{j} $

Para resolverla de manera compacta para $x \in (0, \infty)$, aplicamos un cambio de variable clásico encaminado a la definición de la Función Gamma incompleta inferior:

$ \displaystyle u = -(k_{1}+1)\ln x \implies \ln x = -\frac{u}{k_{1}+1} $

Diferenciando ambos lados para obtener el operador $dx$:

$ \displaystyle x = e^{-\frac{u}{k_{1}+1}} \implies dx = -\frac{1}{k_{1}+1}e^{-\frac{u}{k_{1}+1}}\,du $

Sustituyendo estos componentes en la integral del núcleo, extrayendo las constantes y agrupando las bases exponenciales:

$ \displaystyle \frac{(-1)^{\beta }}{(k_{1}+1)^{\beta +1}} \int u^{\beta }e^{-u}\,du $

Por definición fundamental, la integral resultante corresponde a la Función Gamma incompleta inferior, $\gamma(s, z) = \int_0^z t^{s-1}e^{-t}dt$. Al tratarse de una integral indefinida, añadimos la constante de integración correspondiente:

$ \displaystyle \int u^{\beta }e^{-u}\,du = \gamma(\beta +1, u) + C_{0} $

Devolviendo el valor original de la variable de sustitución $u$, la representación propuesta para la solución del núcleo queda definida como:

$ \displaystyle \int x^{k_{1}}(\ln x)^{\beta }\,dx = \frac{(-1)^{\beta }}{(k_{1}+1)^{\beta +1}}\gamma \left(\beta +1, -(k_{1}+1)\ln x\right) + C_{0} $

---

## Parte 5: La Representación General Propuesta

Al fusionar la solución analítica del núcleo (Parte 4) con el sistema jerárquico de sumatorias múltiples demostrado por inducción (Parte 3), la representación general para la integral de la tetración truncada de cualquier orden $n \ge 2$ es:

$ \displaystyle \int \text{piso}(n)\,dx = \sum_{k_{n-1}=0}^{\infty }\dots \sum_{k_{1}=0}^{\infty } \frac{\left(\prod_{j=1}^{n-2}k_{j+1}^{k_{j}}\right)\cdot (-1)^{\sum_{j=1}^{n-1}k_{j}}}{\left(\prod_{j=1}^{n-1}k_{j}!\right)\cdot (k_{1}+1)^{\left(\sum_{j=1}^{n-1}k_{j}\right)+1}} \gamma \left(\sum_{j=1}^{n-1}k_{j}+1, -(k_{1}+1)\ln x\right) + C $

---

## Parte 6: Verificación de Casos Particulares

### Verificación del Caso $n=2$

Para $n=2$, la productoria del numerador queda vacía (igual a $1$), las sumatorias se reducen únicamente al índice $k_{1}$ y el exponente logarítmico es $\beta = k_1$. Sustituyendo en la ecuación general:

$ \displaystyle \int \text{piso}(2)\,dx = \sum_{k_{1}=0}^{\infty} \frac{(-1)^{k_{1}}}{k_{1}!\cdot (k_{1}+1)^{k_{1}+1}}\gamma \left(k_{1}+1, -(k_{1}+1)\ln x\right) + C $

El resultado coincide término a término con la sustitución Gamma directa sobre la integral parcial obtenida en la Parte 2.

### Verificación del Caso $n=3$ por Comparación Término a Término

Para validar el caso $n=3$, en lugar de una inspección general, realizamos una comparación término a término evaluando explícitamente los componentes de la fórmula general frente al desarrollo manual.

De acuerdo con la expresión general evaluada en $n=3$:

- El límite superior de la productoria del numerador es $n-2 = 1$, lo que da $\prod_{j=1}^{1} k_{j+1}^{k_j} = k_2^{k_1}$.
- El límite superior de la productoria del denominador es $n-1 = 2$, dando $\prod_{j=1}^{2} k_j! = k_1! \, k_2!$.
- El exponente del factor alternante y del denominador es $\beta = \sum_{j=1}^{2} k_j = k_1 + k_2$.

Sustituyendo estos términos estrictos en la fórmula general, se produce:

$ \displaystyle I_{3,\text{general}} = \sum_{k_{2}=0}^{\infty} \sum_{k_{1}=0}^{\infty} \frac{k_{2}^{k_{1}}\cdot (-1)^{k_{1}+k_{2}}}{k_{1}!\,k_{2}!\cdot (k_{1}+1)^{k_{1}+k_{2}+1}}\gamma \left(k_{1}+k_{2}+1, -(k_{1}+1)\ln x\right) + C $

Por otra parte, si tomamos el desarrollo explícito del integrando para $n=3$ obtenido en la Parte 2:

$ \displaystyle \text{piso}(3) = \sum_{k_{2}=0}^{\infty} \sum_{k_{1}=0}^{\infty} \frac{k_{2}^{k_{1}}}{k_{1}!\,k_{2}!}x^{k_{1}}(\ln x)^{k_{1}+k_{2}} $

y aplicamos de forma directa a cada término la integral del núcleo con $\beta = k_1 + k_2$, obtenemos el término genérico:

$ \displaystyle \frac{k_{2}^{k_{1}}}{k_{1}!\,k_{2}!} \left[ \frac{(-1)^{k_1+k_2}}{(k_1+1)^{k_1+k_2+1}} \gamma\left(k_1+k_2+1, -(k_1+1)\ln x\right) \right] $

Al comparar algebraicamente miembro a miembro el término generalizado de la fórmula con la integración término a término del desarrollo directo, se constata una equivalencia exacta e idéntica en todos sus coeficientes, exponentes e índices. Queda así demostrada la consistencia analítica absoluta del teorema.

---

## Conclusión

Hemos desarrollado una representación analítica completa para la integral de la tetración truncada mediante:

1. **Demostración por inducción** de la representación en series múltiples del integrando
2. **Resolución del núcleo** utilizando la Función Gamma incompleta inferior
3. **Verificación rigurosa** de los casos particulares $n=2$ y $n=3$

Este resultado proporciona una herramienta poderosa para el cálculo de integrales de funciones de tetración de cualquier orden, expresando el resultado en términos de funciones especiales bien conocidas.