---
layout: post
title: "Análisis Formal del Grafo de Cayley del Grupo Dihédrico $D_4$"
use_math: true
published: true
date: 2026-07-18
category: "Matemáticas"
tags: ["Teoría de Grupos", "Grafos de Cayley", "Grupo Dihédrico", "Simetrías"]
---

El siguiente grafo de Cayley representa el grupo diédrico

$$
D_4=\langle r,f\mid r^4=e,\;f^2=e,\;fr=r^{-1}f\rangle,
$$

tomando como conjunto de generadores

$$
S=\{r,f\},
$$

y considerando que cada arista corresponde a **multiplicación por la derecha**.

Los ocho elementos del grupo son

$$
\{e,r,r^2,r^3,f,rf,r^2f,r^3f\}.
$$

---

## Generadores

### Rotación

El generador

$$
r
$$

representa una rotación de \(90^\circ\).

Como

$$
r^4=e,
$$

las rotaciones forman un ciclo de longitud cuatro.

---

### Reflexión

El generador

$$
f
$$

representa una reflexión.

Al satisfacer

$$
f^2=e,
$$

es una involución.

---

### Relación no conmutativa

La relación fundamental del grupo es

$$
fr=r^{-1}f=r^3f,
$$

que expresa que una reflexión invierte el sentido de las rotaciones.

---

# Acción del generador \(r\)

Como las aristas representan multiplicación por la derecha,

$$
x\longrightarrow xr.
$$

## Ciclo exterior

Sobre las rotaciones puras se obtiene

$$
e
\longrightarrow
r
\longrightarrow
r^2
\longrightarrow
r^3
\longrightarrow
e.
$$

Este es el ciclo exterior del grafo.

---

## Ciclo interior

Para los elementos con reflexión,

$$
\begin{aligned}
f\cdot r
&=r^3f,\\
r^3f\cdot r
&=r^2f,\\
r^2f\cdot r
&=rf,\\
rf\cdot r
&=f.
\end{aligned}
$$

Por tanto,

$$
f
\longrightarrow
r^3f
\longrightarrow
r^2f
\longrightarrow
rf
\longrightarrow
f.
$$

Obsérvese que el orden del ciclo interior es el inverso del exterior. Esto es una consecuencia directa de la relación

$$
fr=r^{-1}f,
$$

que invierte la orientación de la rotación cuando aparece una reflexión.

---

# Acción del generador \(f\)

Las aristas punteadas representan

$$
x\longrightarrow xf.
$$

Dado que

$$
f^2=e,
$$

cada una de ellas puede recorrerse en ambos sentidos.

Con el etiquetado utilizado en la figura se obtienen las parejas

$$
\begin{aligned}
e &\longleftrightarrow f,\\
r &\longleftrightarrow r^3f,\\
r^2 &\longleftrightarrow r^2f,\\
r^3 &\longleftrightarrow rf.
\end{aligned}
$$

Estas conexiones enlazan el ciclo exterior con el interior y representan la acción involutiva del generador \(f\).

---

# Representación Visual del Grafo de Cayley

<figure style="text-align:center;margin:2em 0;">
<img
src="/images/cayley-graph-d4.svg"
alt="Grafo de Cayley del grupo diédrico D4"
style="max-width:100%;height:auto;border-radius:8px;box-shadow:0 4px 8px rgba(0,0,0,.12);">

<figcaption style="margin-top:0.8em;font-style:italic;color:#666">

Grafo de Cayley del grupo

$$
D_4=\langle r,f\mid r^4=e,\;f^2=e,\;fr=r^{-1}f\rangle.
$$

Las aristas continuas representan la acción del generador \(r\) mediante multiplicación por la derecha.

El ciclo exterior corresponde a las rotaciones puras

$$
e,r,r^2,r^3,
$$

mientras que el ciclo interior

$$
f,r^3f,r^2f,rf
$$

aparece con orientación opuesta debido a la relación

$$
fr=r^{-1}f.
$$

Las aristas punteadas representan la acción involutiva del generador \(f\).

</figcaption>
</figure>

---

# Conclusión

El grafo de Cayley reproduce fielmente la estructura algebraica del grupo diédrico \(D_4\).

En particular,

- el ciclo exterior representa las rotaciones;
- el ciclo interior muestra cómo la relación \(fr=r^{-1}f\) invierte el sentido de la acción de \(r\);
- las aristas punteadas representan la acción involutiva de \(f\).

De este modo, la representación gráfica refleja de forma inmediata tanto la estructura cíclica de las rotaciones como el carácter no conmutativo del grupo.
