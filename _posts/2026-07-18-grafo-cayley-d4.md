---
layout: post
title: "Análisis Formal del Grafo de Cayley del Grupo Dihédrico $D_4$"
use_math: true
published: true
date: 2026-07-18
category: "Matemáticas"
tags: ["Teoría de Grupos", "Grafos de Cayley", "Grupo Dihédrico"]
thumbnails: 
  - "/svg-inkscape/cayley-graph-d4.svg"
  - "/svg-inkscape/cayley-graph-d4_2.svg"
---

<div style="
width:100vw;
margin-left:calc(50% - 50vw);
display:flex;
justify-content:center;
align-items:flex-start;
gap:2rem;
">

    <img src="/svg-inkscape/cayley-graph-d4.svg"
         alt="Grafo de Cayley del grupo diédrico D4 - Versión 1"
         style="width:350px;height:auto;">

    <img src="/svg-inkscape/cayley-graph-d4_2.svg"
         alt="Grafo de Cayley del grupo diédrico D4 - Versión 2"
         style="width:400px;height:auto;">

</div>

El grafo de Cayley presentado para el grupo diédrico $D_4$ es matemáticamente correcto y modela con total precisión la estructura del grupo de simetrías de un cuadrado (de orden 8). A continuación se desglosa la verificación formal de cada uno de sus componentes basados en la presentación algebraica:

$D_4 = \langle r, f \mid r^4 = e,  f^2 = e, fr = r^{-1}f \rangle$

## Definición de los Generadores y Relaciones

- **Rotación ($r^4 = e$):** Representa una rotación de $90^\circ$ en sentido horario. Aplicarla cuatro veces consecutivas regresa el sistema al estado de identidad ($e$).
- **Reflexión ($f^2 = e$):** Representa una simetría axial. Al ser un operador involutivo, aplicarlo dos veces consecutivas anula su efecto ($f \cdot f = e$).
- **Relación no abeliana ($fr = r^{-1}f$ o $fr = r^3f$):** Esta relación define la interacción no conmutativa entre rotaciones y reflexiones. Como el orden de $r$ es 4, se tiene que $r^{-1} = r^3$.

## Análisis de las Órbitas en el Grafo

### El Ciclo Exterior (Rotaciones Puras, Camino Verde-Azul)

La acción de la rotación se define multiplicando por la derecha por el generador $r$ (es decir, la transición es de la forma $x \xrightarrow{\cdot r} xr$). 

Para los elementos sin reflexión (ciclo exterior), el avance sigue un sentido horario estándar:

$e \xrightarrow{\cdot r} r \xrightarrow{\cdot r} r^2 \xrightarrow{\cdot r} r^3 \xrightarrow{\cdot r} e$

Esto coincide perfectamente con las flechas exteriores continuas de color azul-verde.

### El Ciclo Interior (Elementos Reflejados)

Al multiplicar por la derecha por $r$ a un elemento que ya posee una componente de reflexión ($xf \xrightarrow{\cdot r} xfr$), la relación $fr = r^3f$ altera el sentido de la rotación:

- **Partiendo de $f$:** $f \cdot r = r^3f$. La flecha dirigida va desde el nodo $f$ hasta el nodo $r^3f$.

- **Partiendo de $r^3f$:** $r^3f \cdot r = r^3(fr) = r^3(r^3f) = r^6f = r^2f$. La flecha va desde $r^3f$ hasta $r^2f$ (ya que $r^4 = e$, por lo que $r^6 = r^2$).

- **Partiendo de $r^2f$:** $r^2f \cdot r = r^2(fr) = r^2(r^3f) = r^5f = rf$. La flecha va desde $r^2f$ hasta $rf$ (dado que $r^5 = r$).

- **Partiendo de $rf$:** $rf \cdot r = r(fr) = r(r^3f) = r^4f = f$. La flecha va desde $rf$ hasta $f$.

Esta secuencia matemática genera el ciclo interno:

$f \xrightarrow{\cdot r} r^3f \xrightarrow{\cdot r} r^2f \xrightarrow{\cdot r} rf \xrightarrow{\cdot r} f$

El cual se desplaza de forma **antihoraria**, ilustrando visualmente cómo la reflexión invierte la orientación del plano.

### Los Puentes de Reflexión (Camino Naranja Punteado)

Las aristas punteadas representan la multiplicación por la derecha por el generador $f$ ($x \xrightarrow{\cdot f} xf$). Dado que $f$ es una involución ($f^2 = e$), estas conexiones son bidireccionales, actuando como puentes de doble sentido entre los ciclos interior y exterior:

$e \cdot f = f \iff f \cdot f = e$, $r \cdot f = rf \iff rf \cdot f = r$, $r^2 \cdot f = r^2f \iff r^2f \cdot f = r^2$, $r^3 \cdot f = r^3f \iff r^3f \cdot f = r^3$

El grafo plasma con absoluta fidelidad estos pares de conexiones simétricas mediante los puentes naranjas.

## Conclusión

El grafo de Cayley para $D_4$ cumple de manera rigurosa con la estructura del grupo algebraico. Representa tanto el carácter no abeliano como las propiedades geométricas de simetría de forma clara y formal.

Este análisis demuestra cómo la estructura algebraica abstracta se manifiesta visualmente en el grafo, donde:

1. **El ciclo exterior** representa las rotaciones puras del cuadrado
2. **El ciclo interior** ilustra cómo la reflexión invierte la orientación
3. **Los puentes de reflexión** muestran la naturaleza involutiva de $f$

La representación gráfica no es solo una ilustración, sino una herramienta poderosa para comprender la estructura del grupo y sus relaciones fundamentales.