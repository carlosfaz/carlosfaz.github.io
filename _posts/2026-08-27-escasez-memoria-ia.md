---
layout: post
title: "Escasez de Memoria y Modelos Abiertos: la Reestructuración de la Industria de la IA"
use_math: true
published: true
date: 2026-08-27
category: "Economía de la IA"
tags: ["Inteligencia Artificial", "Economía", "Python"]
thumbnail: "/images/memory-scarcity-ai.svg"
---

El debate público sobre la "burbuja de la IA" se fija en las GPUs y en las valoraciones de las empresas. Un paper publicado en julio de 2026 sugiere que todos miran al sitio equivocado: el cuello de botella que reordenará la industria no es el cómputo, es **la memoria**.

> Si el costo que manda en la inferencia ya no son los FLOPs sino los *bytes movidos*... **¿quién gana y quién pierde cuando el precio de la memoria se dispara?**

El autor no es un analista cualquiera: **Satoshi Matsuoka** dirige el RIKEN Center for Computational Science, el centro japonés detrás del superordenador Fugaku. En *"Memory Scarcity, Open Models, and the Restructuring of the AI Industry, 2026–2030"* ([arXiv:2607.07207](https://arxiv.org/abs/2607.07207)) construye un análisis cuantitativo de escenarios con una conclusión incómoda: la solvencia del mayor buildout de infraestructura de la historia depende de un corredor estrechísimo de demanda y precios.

## Las cuatro fuerzas que chocan a la vez

El paper analiza cómo cuatro fuerzas simultáneas reestructuran la industria entre 2026 y 2030:

1. **La subida histórica del DRAM/HBM**: la memoria de alto ancho de banda se revaloriza y pone una prima enorme sobre todo el hardware nuevo.
2. **Modelos abiertos de nivel frontera** (ejemplificados por GLM-5.2): la capacidad puntera deja de ser exclusiva de los laboratorios cerrados.
3. **La eficiencia de inferencia acelera**: compresión de KV-cache cerca del límite de Shannon (TurboQuant) y runtimes locales ligeros (DwarfStar 4, hardware clase DGX Spark) reducen los bytes necesarios por token ~30% al año.
4. **Los "antiguos laboratorios de IA" se vuelven caseros**: Meta y xAI entran al mercado de reventa de cómputo con flotas compradas *antes* de la revalorización de la memoria.

## La unidad correcta: dólares por petabyte de ancho de banda

Generar un token con un LLM exige leer *todos* los pesos del modelo desde la memoria HBM. La fase de decodificación está limitada por **ancho de banda**, no por cómputo:

$ \displaystyle \text{tokens/s} \; \approx \; \frac{\text{ancho de banda (bytes/s)}}{\text{bytes por token}} $

Por eso el paper formula la economía de la inferencia en **\\$/PB**: dólares por petabyte de ancho de banda entregado. Es una métrica *agnóstica al modelo* — da igual si sirves un gigante cerrado o un abierto destilado, el costo por token se reduce a cuánto te cuesta mover bytes:

$ \displaystyle \text{costo/token} \; = \; \frac{\text{USD/PB} \; \times \; \text{bytes leídos por token}}{10^{15}\ \text{bytes/PB}} $

Con esta regla de tres, toda la discusión de "qué modelo gana" se convierte en una pregunta mucho más incómoda: **¿a cuánto compraste tú la memoria?**

### Un ejemplo con números redondos

Sirve un modelo denso de 70B parámetros en 8 bits: son **70 GB** de pesos que hay que leer *enteros* por cada token generado, más la KV-cache. Un acelerador con 3 TB/s de ancho de banda te da:

$ \displaystyle \frac{3{,}000\ \text{GB/s}}{70\ \text{GB/token}} \approx 43\ \text{tokens/s} $

Ese techo **no lo mueve un procesador más rápido**: lo mueve más ancho de banda o menos bytes por token. Por eso la cuarta fuerza del paper — la compresión de KV-cache cerca del límite de Shannon — no es un detalle técnico: cada 30% de bytes que ahorras es un 30% de capacidad que *no* necesitas comprar. Y ahí está la trampa para quien construye: **la eficiencia de inferencia destruye demanda de hardware exactamente igual de rápido que la crea el crecimiento de usuarios.**

## La cinta transportadora de la depreciación

La intuición dice que con el tiempo los precios del hardware se normalizan y la brecha entre el que ya tiene flota y el que entra nuevo se cierra. El paper demuestra lo contrario: medida en \\$/PB, la brecha entrante–incumbente es **estructural y no se cierra dentro del horizonte**:

- **3.2×** en 2026
- **1.9×** en 2027 (el punto más estrecho)
- se **re-abre** a ~3× si el HBM se normaliza en 2028, o **por encima de 4×** si la escasez persiste hasta 2030

¿Por qué? Por la **cinta transportadora de la depreciación**: cada año, una nueva hornada de flotas termina de amortizarse en manos de los incumbentes y pasa a producir a coste marginal casi nulo — *más rápido de lo que los precios del hardware nuevo se normalizan*. La ventaja **rota entre incumbentes, pero nunca se transfiere a los entrantes**. Montar un datacenter nuevo hoy es comprar la memoria en el pico para vender cómputo al precio de mañana.

¿Y si construyes tu propio silicio para saltarte el margen del fabricante? El análisis de entrada *greenfield* con silicio custom es frío: eliminas el margen del comerciante, **pero no la prima de la memoria**. Resultado central: **25% de éxito, 34% mediocre, 41% de pérdida** — mejorable solo con puertas de decisión escalonadas (go/no-go) en lugar de una apuesta única.

## Entrenamiento: la bifurcación lujo–masa

El costo de entrenar se parte en dos mundos que se alejan a toda velocidad:

- **Nivel lujo**: una corrida de clase frontera costará **\\$18B–\\$38B en 2030**. Solo un puñado de actores podrá sentarse a esa mesa.
- **Nivel masa**: replicar la capacidad de la frontera *previa* mediante aprendizaje por refuerzo y destilación sobre bases abiertas cae hacia **~\\$5M**.

La divergencia pasa de ~40× hoy a **tres o cuatro órdenes de magnitud**. La consecuencia es paradójica y optimista a la vez: casi nadie entrenará la frontera, pero *casi todo el mundo* podrá permitirse el modelo de hace 18 meses. La frontera se convierte en un bien de lujo; la capacidad "suficiente", en una commodity.

## El corredor de solvencia

Aquí está el corazón del paper. La solvencia del buildout anunciado está confinada a un **corredor** con dos condiciones simultáneas:

1. La demanda agregada de tokens debe crecer **~2× al año durante cuatro años seguidos** (16× acumulado).
2. Los precios *premium* (modelos cerrados) deben mantenerse **rígidos en términos absolutos**.

Y eso contra el viento de la eficiencia: cada token cuesta ~30% menos bytes al año. Las cuentas del ancho de banda que hay que *vender de verdad*:

Si $ T $ son los tokens servidos al año y $ b $ los bytes que hay que mover por token, el ancho de banda que debes tener instalado es $ B = T \cdot b $. Como ambos factores crecen (o decrecen) de forma multiplicativa, sus **tasas anuales se multiplican**:

$ \displaystyle g\_B \; = \; g\_T \cdot g\_b \; = \; \underbrace{2.0}\_{\text{tokens}} \times \underbrace{0.7}\_{\text{bytes/token}} \; = \; 1.4 $

Es decir, el ancho de banda **vendible** crece un 40% al año, no un 100%. Compuesto durante los cuatro años del corredor:

$ \displaystyle \frac{B\_{2030}}{B\_{2026}} \; = \; g\_B^{\,4} \; = \; 1.4^{4} \; \approx \; 3.84 $

Aunque los tokens se multipliquen por $ 2^4 = 16 $, la eficiencia los divide por $ (1/0.7)^4 \approx 4.2 $, y el ancho de banda que realmente hay que *vender* solo se multiplica por **~3.8**. Ese factor 3.8 es el que tiene que pagar toda la capacidad que se está construyendo hoy.

Salirse del corredor por cualquiera de los dos ejes concentra los deterioros en la capacidad de las cosechas pico. El análisis de **punto de equilibrio por cosecha** (*vintage breakeven*) es demoledor: la capacidad de **2026** y la de **2028–29** quedan fatalmente expuestas, cada una a un régimen de precios distinto; solo la cosecha **2027** es robusta. Y el detalle que eriza la piel: las decisiones finales de inversión de la ventana 2028–29 — la tranche más expuesta — **se están firmando ahora**.

Dos avisos metodológicos que valen oro:

- Los *trackers* públicos de tokens **sobreestiman la demanda monetizable** (cuentan tokens que nadie paga).
- Toda proyección anterior al Q2-2026 pertenece a otra época: la industria giró de **maximizar tokens a minimizar tokens** — la eficiencia se volvió un KPI empresarial.

Como telón de fondo, la telaraña financiera: más de **\\$800 mil millones** en acuerdos circulares entre un puñado de actores (NVIDIA invierte en y provee a OpenAI; OpenAI arrastra compromisos del orden de **\\$1.15 billones**: ~\\$300B con Oracle, ~\\$90B con AMD, ~\\$38B con AWS...). Si el corredor se rompe, la transmisión ya está cableada.


## LineShine LX2: el desacoplamiento chino

Entre abril y junio de 2026, el sistema **LineShine** de Shenzhen tomó el puesto #1 del TOP500 con **2.198 EFLOPS sostenidos** — la primera sumisión china verificada desde 2019. Sus **40,960 procesadores Armv9 LX2** (diseño Huawei) combinan HBM *de producción doméstica* en el mismo paquete (~32 GB a 4 TB/s) con 256 GB de DDR5, unidades matriciales SME/SVE e interconexión propia.

El paper es honesto con las métricas de IA: va por detrás. Uplift de precisión mixta de 3.6× frente a 9–11× de los sistemas con GPU de EE.UU.; 52 GFLOPS/W por debajo de El Capitan; HBM generaciones por detrás de HBM4. Pero lo estratégicamente decisivo no es la posición, es el **desacoplamiento**: con HBM propia, la curva de costos china queda *fuera* de la crisis global de memoria que infla el capex de todos los demás. El patrón es el de los vehículos eléctricos: unos años atrás en el nivel premium, estructuralmente adelante en costo por unidad de capacidad de masas, y mejorando con una pendiente más pronunciada. **La lectura correcta de LineShine no es el benchmark, es la pendiente.**

Y hay poesía arquitectónica: el LX2 — un CPU de propósito general con unidades matriciales alimentado por una jerarquía HBM+DDR, en linaje directo del A64FX de Fugaku — es exactamente la dirección defendida en la serie *"¿Todavía necesitamos GPUs?"* de Dongarra, Hoefler y el propio Matsuoka. La ruta sin GPUs deja de ser hipotética justo cuando la economía del GPU carga con la prima de la memoria.

## Los cinco escenarios (con probabilidades)

El paper cierra con cinco escenarios para 2026–2030. Ninguno supera el 25%: la incertidumbre *es* el mensaje.

| Escenario | Prob. | En una frase |
|---|---|---|
| **Oligopolio de caseros rotativos** | 25% | La ventaja rota entre incumbentes con flotas amortizadas; los entrantes nunca la alcanzan |
| **Crash de commoditización** | 25% | La eficiencia acelera a 40%/año, la demanda toca techo en 2027 y el crash llega en 2028: el clásico busto del DRAM con acelerante de IA |
| **Absorción de Jevons** | 20% | La paradoja de Jevons salva el buildout: abaratar la inferencia dispara el consumo total |
| **Re-diferenciación por capa de sistema** | 18% | El valor migra del modelo a la capa de sistema y orquestación |
| **Bifurcación geopolítica** | 12% | Dos stacks separados: el occidental con prima de memoria y el chino desacoplado |

## De la teoría al código

Las cuentas centrales del paper caben en unas líneas. El script completo que genera la figura está en [`scripts/generate_memory_scarcity.py`](https://github.com/carlosfaz/carlosfaz.github.io/blob/main/scripts/generate_memory_scarcity.py):

```python
# Corredor de solvencia: tokens 2×/año, eficiencia -30%/año en bytes/token
crec_tokens, eficiencia, anios = 2.0, 0.70, 4
tokens_acum = crec_tokens ** anios                    # 16×
bandwidth_req = (crec_tokens * eficiencia) ** anios   # ≈ 3.8×

# Divergencia de entrenamiento en 2030
lujo, masa = (18e9, 38e9), 5e6
ratio = (lujo[0] / masa, lujo[1] / masa)              # 3,600× – 7,600×
```

## El resultado

![A la izquierda: la brecha de costo entrante-incumbente en dólares por petabyte, que se estrecha en 2027 y se reabre hacia 2030 sin tocar nunca la paridad. A la derecha: los cinco escenarios 2026-2030 con sus probabilidades]({{ site.baseurl }}/images/memory-scarcity-ai.svg)

Cómo leer la figura:

- **Panel izquierdo**: la brecha de costo entre un entrante con hardware nuevo y un incumbente con flota amortizada, medida en \\$/PB. Se estrecha hasta 1.9× en 2027 — el espejismo de que "ya casi" — y luego se **re-abre** por la cinta transportadora de la depreciación. La línea verde de paridad (1×) nunca se toca: entrar nuevo nunca deja de ser desventaja.
- **Panel derecho**: los cinco escenarios con las probabilidades del paper. Que el más probable tenga apenas 25% es la forma cuantitativa de decir *"nadie sabe, y estos son los mundos posibles"*.

La salida del programa:

```text
=== Escasez de memoria y reestructuración de la IA (arXiv:2607.07207) ===
Brecha entrante/incumbente: 3.2× (2026) → 1.9× (2027) → ~3× o >4× (2029-30)

--- Corredor de solvencia ---
Demanda de tokens: 2.0×/año × 4 años = 16× acumulado
Bytes por token: 0.7×/año → 0.24× en 4 años
Ancho de banda entregado requerido: (2 × 0.7)^4 = 3.8× en 4 años

--- Divergencia del costo de entrenamiento (2030) ---
Nivel lujo:  $18B-$38B por corrida frontera
Nivel masa:  ~$5M (paridad con la frontera previa)
Ratio: 3,600× - 7,600× (3-4 órdenes de magnitud; hoy ~40×)
```

## Qué significa esto según dónde estés sentado

El paper es macro, pero sus consecuencias son muy concretas:

- **Si construyes infraestructura**: la cosecha importa más que la tecnología. Firmar capacidad para 2028–29 al precio de la memoria de hoy es apostar a un régimen de precios concreto — el paper sugiere puertas de decisión escalonadas en vez de un compromiso único.
- **Si vendes inferencia**: tu margen no depende de tu modelo, depende de la fecha en que compraste tus aceleradores. Competir contra una flota amortizada es competir contra un costo marginal que tiende a la electricidad.
- **Si construyes producto sobre APIs**: la bifurcación lujo–masa te regala una opción. Un modelo abierto destilado, servido local o en hardware barato, cubre hoy casos que hace 18 meses exigían la frontera cerrada. Diseñar para poder *cambiar de modelo* vale más que elegir bien el modelo.
- **Si inviertes**: la pregunta útil no es "¿crecerá la IA?" — casi seguro sí — sino "¿crecerá la **demanda monetizable de ancho de banda** un 3.8× en cuatro años?". Son preguntas distintas y solo la segunda paga las facturas.

## Lo que el paper no promete

Un análisis de escenarios no es una bola de cristal, y conviene leerlo con las mismas reservas que su autor:

- **Son probabilidades subjetivas, no frecuencias.** El 25%/25%/20%/18%/12% es un juicio experto calibrado con los datos disponibles a julio de 2026, no la salida de un modelo estimado sobre historia. La virtud está en la estructura del argumento, no en el segundo decimal.
- **La paradoja de Jevons puede ganar.** Si abaratar la inferencia multiplica los usos más rápido de lo que cae el costo por token, el corredor se ensancha solo. El paper le asigna un 20% honesto — no es un escenario marginal.
- **Los "agentes" cambian la aritmética.** Un flujo de trabajo agéntico consume decenas de miles de tokens por tarea. Si ese patrón se generaliza, el 2× anual de demanda puede quedarse corto... o el giro a *minimizar* tokens puede acelerarse. La misma tecnología empuja en las dos direcciones.
- **La energía y la red no entran en el \\$/PB.** El modelo aísla el costo de mover bytes; la potencia contratada, el enfriamiento y la interconexión son restricciones reales que pueden morder antes que la memoria.
- **La cifra de \\$1.15 billones es un agregado heterogéneo.** El propio paper advierte que mezcla compromisos de fuerza legal muy distinta. Titular fácil, dato frágil.

Con todo, la contribución central sobrevive a estas objeciones: **medir la inferencia en dólares por byte movido, y no en FLOPs, cambia quién parece competitivo.** Esa es la parte que se queda.

## Conclusión

1. **El cuello de botella es la memoria, no el cómputo**: en decodificación mandan los bytes movidos, y la unidad honesta es el \\$/PB.
2. **La ventaja incumbente es estructural**: la cinta transportadora de la depreciación entrega flotas amortizadas más rápido de lo que se normalizan los precios. La brecha rota entre gigantes; nunca llega al entrante.
3. **El entrenamiento se bifurca**: frontera como bien de lujo (\\$18B–\\$38B) y capacidad previa como commodity (~\\$5M).
4. **La solvencia vive en un corredor estrecho**: 2× de demanda de tokens al año durante cuatro años *y* precios premium rígidos — con solo la cosecha 2027 robusta a ambos regímenes.
5. **Mira la pendiente, no la posición**: LineShine no gana el benchmark de IA, pero desacopla a China de la crisis de memoria. En un mundo de escasez, tener tu propia HBM vale más que liderar el TOP500.

## Referencia y más lectura

- **Paper**: Satoshi Matsuoka, *"Memory Scarcity, Open Models, and the Restructuring of the AI Industry, 2026–2030"*, [arXiv:2607.07207](https://arxiv.org/abs/2607.07207) [econ.GN], julio 2026.
- **[Teoría de la Ruina]({{ site.baseurl }}/teoria-ruina/)**: la solvencia bajo incertidumbre en versión aseguradora — el corredor de solvencia del paper es el mismo problema con otro nombre.
- **[Gestión de Riesgos Avanzada]({{ site.baseurl }}/gestion-riesgos-avanzada/)**: stress testing y escenarios extremos, la misma lógica aplicada a mercados en lugar de datacenters.

