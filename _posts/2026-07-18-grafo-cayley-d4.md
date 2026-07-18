---
layout: post
title: "Análisis Formal del Grafo de Cayley del Grupo Dihédrico $D_4$"
use_math: true
published: true
date: 2026-07-18
category: "Matemáticas"
tags: ["Teoría de Grupos", "Grafos de Cayley", "Grupo Dihédrico", "Simetrías"]
---

El grafo de Cayley presentado para el grupo diédrico $D_4$ es matemáticamente correcto y modela con total precisión la estructura del grupo de simetrías de un cuadrado (de orden 8). A continuación se desglosa la verificación formal de cada uno de sus componentes basados en la presentación algebraica:

$$
D_4 = \langle r, f \mid r^4 = e, \, f^2 = e, \, fr = r^{-1}f \rangle
$$

## Definición de los Generadores y Relaciones

- **Rotación ($r^4 = e$):** Representa una rotación de $90^\circ$ en sentido horario. Aplicarla cuatro veces consecutivas regresa el sistema al estado de identidad ($e$).
- **Reflexión ($f^2 = e$):** Representa una simetría axial. Al ser un operador involutivo, aplicarlo dos veces consecutivas anula su efecto ($f \cdot f = e$).
- **Relación no abeliana ($fr = r^{-1}f$ o $fr = r^3f$):** Esta relación define la interacción no conmutativa entre rotaciones y reflexiones. Como el orden de $r$ es 4, se tiene que $r^{-1} = r^3$.

## Análisis de las Órbitas en el Grafo

### El Ciclo Exterior (Rotaciones Puras, Camino Verde-Azul)

La acción de la rotación se define multiplicando por la derecha por el generador $r$ (es decir, la transición es de la forma $x \xrightarrow{\cdot r} xr$). 

Para los elementos sin reflexión (ciclo exterior), el avance sigue un sentido horario estándar:

$$
e \xrightarrow{\cdot r} r \xrightarrow{\cdot r} r^2 \xrightarrow{\cdot r} r^3 \xrightarrow{\cdot r} e
$$

Esto coincide perfectamente con las flechas exteriores continuas de color azul-verde.

### El Ciclo Interior (Elementos Reflejados)

Al multiplicar por la derecha por $r$ a un elemento que ya posee una componente de reflexión ($xf \xrightarrow{\cdot r} xfr$), la relación $fr = r^3f$ altera el sentido de la rotación:

- **Partiendo de $f$:** 
$$ f \cdot r = r^3f $$
La flecha dirigida va desde el nodo $f$ hasta el nodo $r^3f$.

- **Partiendo de $r^3f$:** 
$$ r^3f \cdot r = r^3(fr) = r^3(r^3f) = r^6f = r^2f $$
La flecha va desde $r^3f$ hasta $r^2f$ (ya que $r^4 = e$, por lo que $r^6 = r^2$).

- **Partiendo de $r^2f$:** 
$$ r^2f \cdot r = r^2(fr) = r^2(r^3f) = r^5f = rf $$
La flecha va desde $r^2f$ hasta $rf$ (dado que $r^5 = r$).

- **Partiendo de $rf$:** 
$$ rf \cdot r = r(fr) = r(r^3f) = r^4f = f $$
La flecha va desde $rf$ hasta $f$.

Esta secuencia matemática genera el ciclo interno:

$$
f \xrightarrow{\cdot r} r^3f \xrightarrow{\cdot r} r^2f \xrightarrow{\cdot r} rf \xrightarrow{\cdot r} f
$$

El cual se desplaza de forma **antihoraria**, ilustrando visualmente cómo la reflexión invierte la orientación del plano.

### Los Puentes de Reflexión (Camino Naranja Punteado)

Las aristas punteadas representan la multiplicación por la derecha por el generador $f$ ($x \xrightarrow{\cdot f} xf$). Dado que $f$ es una involución ($f^2 = e$), estas conexiones son bidireccionales, actuando como puentes de doble sentido entre los ciclos interior y exterior:

$$
\begin{aligned}
    e \cdot f = f &\iff f \cdot f = e \\
    r \cdot f = rf &\iff rf \cdot f = r \\
    r^2 \cdot f = r^2f &\iff r^2f \cdot f = r^2 \\
    r^3 \cdot f = r^3f &\iff r^3f \cdot f = r^3
\end{aligned}
$$

El grafo plasma con absoluta fidelidad estos pares de conexiones simétricas mediante los puentes naranjas.

## Representación Visual del Grafo de Cayley

A continuación se presenta la representación gráfica del grafo de Cayley para $D_4$:

<figure style="text-align: center; margin: 2em 0;">
  <svg width="400" height="400" viewBox="-2.5 -2.5 5 5" style="max-width: 100%; height: auto; background: #fafafa; border-radius: 8px;">
    <!-- Estilos -->
    <defs>
      <marker id="arrowhead-teal" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
        <polygon points="0 0, 10 3.5, 0 7" fill="#008080"/>
      </marker>
      <marker id="arrowhead-orange" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
        <polygon points="0 0, 10 3.5, 0 7" fill="#FF8C00"/>
      </marker>
    </defs>
    
    <!-- Aristas de rotación (ciclo exterior) -->
    <path d="M 0.99,-0.99 Q 0.71,0 0.99,0.99" stroke="#008080" stroke-width="0.03" fill="none" marker-end="url(#arrowhead-teal)"/>
    <path d="M 0.99,0.99 Q 0,1.4  -0.99,0.99" stroke="#008080" stroke-width="0.03" fill="none" marker-end="url(#arrowhead-teal)"/>
    <path d="M -0.99,0.99 Q -0.71,0 -0.99,-0.99" stroke="#008080" stroke-width="0.03" fill="none" marker-end="url(#arrowhead-teal)"/>
    <path d="M -0.99,-0.99 Q 0,-1.4 0.99,-0.99" stroke="#008080" stroke-width="0.03" fill="none" marker-end="url(#arrowhead-teal)"/>
    
    <!-- Aristas de rotación (ciclo interior) -->
    <path d="M -0.5,0.5 Q -0.35,0.71 -0.71,0.35" stroke="#008080" stroke-width="0.03" fill="none" marker-end="url(#arrowhead-teal)"/>
    <path d="M -0.71,0.35 Q -0.5,0 -0.35,-0.35" stroke="#008080" stroke-width="0.03" fill="none" marker-end="url(#arrowhead-teal)"/>
    <path d="M -0.35,-0.35 Q 0,-0.5 0.5,-0.5" stroke="#008080" stroke-width="0.03" fill="none" marker-end="url(#arrowhead-teal)"/>
    <path d="M 0.5,-0.5 Q 0.71,-0.35 0.35,0.35" stroke="#008080" stroke-width="0.03" fill="none" marker-end="url(#arrowhead-teal)"/>
    <path d="M 0.35,0.35 Q 0.5,0.5 -0.5,0.5" stroke="#008080" stroke-width="0.03" fill="none" marker-end="url(#arrowhead-teal)"/>
    
    <!-- Aristas de reflexión (punteadas) -->
    <line x1="0.71" y1="-0.71" x2="-0.35" y2="0.35" stroke="#FF8C00" stroke-width="0.025" stroke-dasharray="0.1,0.05"/>
    <line x1="0.99" y1="0" x2="-0.5" y2="0" stroke="#FF8C00" stroke-width="0.025" stroke-dasharray="0.1,0.05"/>
    <line x1="0.71" y1="0.71" x2="-0.35" y2="-0.35" stroke="#FF8C00" stroke-width="0.025" stroke-dasharray="0.1,0.05"/>
    <line x1="0" y1="1.4" x2="0" y2="-0.5" stroke="#FF8C00" stroke-width="0.025" stroke-dasharray="0.1,0.05"/>
    
    <!-- Nodos (círculo exterior) -->
    <circle cx="0" cy="1.4" r="0.12" fill="white" stroke="black" stroke-width="0.02"/>
    <circle cx="0.99" cy="0.71" r="0.12" fill="white" stroke="black" stroke-width="0.02"/>
    <circle cx="0.99" cy="-0.71" r="0.12" fill="white" stroke="black" stroke-width="0.02"/>
    <circle cx="0" cy="-1.4" r="0.12" fill="white" stroke="black" stroke-width="0.02"/>
    
    <!-- Nodos (círculo interior) -->
    <circle cx="-0.5" cy="0.5" r="0.1" fill="white" stroke="black" stroke-width="0.02"/>
    <circle cx="-0.71" cy="0.35" r="0.1" fill="white" stroke="black" stroke-width="0.02"/>
    <circle cx="-0.35" cy="-0.35" r="0.1" fill="white" stroke="black" stroke-width="0.02"/>
    <circle cx="0.5" cy="-0.5" r="0.1" fill="white" stroke="black" stroke-width="0.02"/>
    
    <!-- Etiquetas -->
    <text x="0" y="1.55" text-anchor="middle" font-size="0.25" font-family="serif">$e$</text>
    <text x="1.15" y="0.71" text-anchor="middle" font-size="0.25" font-family="serif">$r$</text>
    <text x="1.15" y="-0.71" text-anchor="middle" font-size="0.25" font-family="serif">$r^2$</text>
    <text x="0" y="-1.55" text-anchor="middle" font-size="0.25" font-family="serif">$r^3$</text>
    
    <text x="-0.65" y="0.65" text-anchor="middle" font-size="0.2" font-family="serif">$f$</text>
    <text x="-0.85" y="0.35" text-anchor="middle" font-size="0.2" font-family="serif">$rf$</text>
    <text x="-0.2" y="-0.5" text-anchor="middle" font-size="0.2" font-family="serif">$r^2f$</text>
    <text x="0.65" y="-0.65" text-anchor="middle" font-size="0.2" font-family="serif">$r^3f$</text>
    
    <!-- Leyenda -->
    <rect x="-1.8" y="1.2" width="1.2" height="0.6" fill="white" stroke="gray" stroke-width="0.02" stroke-dasharray="0.05,0.02"/>
    <line x1="-1.7" y1="1.5" x2="-1.3" y2="1.5" stroke="#008080" stroke-width="0.03" marker-end="url(#arrowhead-teal)"/>
    <text x="-1.05" y="1.55" font-size="0.15" font-family="serif">Rotación $r$</text>
    <line x1="-1.7" y1="1.35" x2="-1.3" y2="1.35" stroke="#FF8C00" stroke-width="0.025" stroke-dasharray="0.1,0.05"/>
    <text x="-1.05" y="1.4" font-size="0.15" font-family="serif">Reflexión $f$</text>
  </svg>
  <figcaption style="margin-top: 0.5em; font-style: italic; color: #666; font-size: 0.9em;">
    Grafo de Cayley del grupo diédrico $D_4 = \langle r, f \mid r^4 = e, f^2 = e, fr = r^{-1}f \rangle$. 
    El ciclo exterior azul-verde representa las rotaciones puras del cuadrado, mientras que el ciclo interior refleja 
    la inversión inducida por la relación no abeliana $fr=r^{-1}f$. Los puentes naranjas representan la acción involutiva de la reflexión.
  </figcaption>
</figure>

## Conclusión

El grafo de Cayley para $D_4$ cumple de manera rigurosa con la estructura del grupo algebraico. Representa tanto el carácter no abeliano como las propiedades geométricas de simetría de forma clara y formal.

Este análisis demuestra cómo la estructura algebraica abstracta se manifiesta visualmente en el grafo, donde:

1. **El ciclo exterior** representa las rotaciones puras del cuadrado
2. **El ciclo interior** ilustra cómo la reflexión invierte la orientación
3. **Los puentes de reflexión** muestran la naturaleza involutiva de $f$

La representación gráfica no es solo una ilustración, sino una herramienta poderosa para comprender la estructura del grupo y sus relaciones fundamentales.