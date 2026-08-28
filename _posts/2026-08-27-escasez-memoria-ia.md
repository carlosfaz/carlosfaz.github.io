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

Todo el mundo habla de la burbuja de la IA mirando a las tarjetas gráficas y a las valoraciones de las empresas. Un paper publicado en julio de 2026 dice que estamos mirando al sitio equivocado. El cuello de botella que va a decidir quién gana y quién quiebra no es la potencia de cálculo. Es algo mucho más aburrido y mucho más caro: **la memoria**.

> Si el costo que manda ya no es *pensar rápido* sino *mover datos*... **¿quién gana y quién pierde cuando la memoria se vuelve un artículo de lujo?**

El autor no es un analista de bolsa cualquiera: **Satoshi Matsuoka** dirige el RIKEN Center for Computational Science de Japón, el centro que construyó el superordenador Fugaku. Su trabajo *"Memory Scarcity, Open Models, and the Restructuring of the AI Industry, 2026–2030"* ([arXiv:2607.07207](https://arxiv.org/abs/2607.07207)) llega a una conclusión incómoda: el mayor plan de construcción de infraestructura de la historia solo sale a cuenta si se cumplen a la vez dos condiciones bastante improbables.

Vamos a desmontarlo pieza a pieza, sin dar nada por sabido.

## Primero, lo básico: ¿por qué manda la memoria?

Un modelo de lenguaje es, en el fondo, una tabla gigantesca de números — los llamados *pesos*. Para escribir **una sola palabra** de su respuesta, el ordenador tiene que leer esa tabla **entera**. No una parte: entera. Y luego repetirlo para la siguiente palabra. Y para la siguiente.

La consecuencia es contraintuitiva: el chip no está pensando, está **esperando datos**. Es como un chef rapidísimo al que obligan a bajar a la despensa a por cada ingrediente. Da igual lo rápido que corte: el tiempo se lo come el trayecto.

Por eso la velocidad de un modelo no la marca su potencia de cálculo, sino cuánta información puede transportar por segundo — lo que se llama **ancho de banda**:

$ \displaystyle \text{palabras por segundo} \; \approx \; \frac{\text{datos que puedes mover por segundo}}{\text{datos que hay que leer por palabra}} $

### Un ejemplo con números redondos

Imagina un modelo mediano que ocupa **70 gigabytes**. Un acelerador moderno mueve unos **3 terabytes por segundo** (3.000 gigabytes). Divides:

$ \displaystyle \frac{3{,}000\ \text{GB/s}}{70\ \text{GB por palabra}} \approx 43\ \text{palabras por segundo} $

Ahí está el techo. Y lo importante: **un procesador más potente no lo sube ni un milímetro**. Solo hay dos formas de mejorarlo — mover más datos por segundo (memoria más cara) o necesitar menos datos por palabra (mejor software).

De ahí sale la unidad que propone el paper para medirlo todo: **dólares por petabyte movido** (un petabyte es un millón de gigabytes). Es una medida honesta porque **da igual qué modelo uses**: al final todos pagan por lo mismo, mover datos. Y convierte la pregunta de moda — *"¿qué modelo es mejor?"* — en otra mucho más cruda: **¿a qué precio compraste tú la memoria?**

## Las cuatro fuerzas que chocan a la vez

El paper identifica cuatro cosas que están pasando **al mismo tiempo**, y que juntas cambian las reglas del juego:

1. **La memoria se ha disparado de precio.** Una crisis de suministro histórica ha encarecido brutalmente el componente más crítico. Todo hardware nuevo nace caro.
2. **Los modelos abiertos alcanzaron a los cerrados.** Modelos que cualquiera puede descargar y ejecutar (el paper cita GLM-5.2) llegaron al nivel de los mejores modelos privados. La capacidad puntera dejó de ser un secreto comercial.
3. **El software aprendió a gastar menos.** Nuevas técnicas de compresión reducen los datos necesarios por palabra alrededor de un **30% cada año**. Cada año hace falta menos hardware para lo mismo.
4. **Los laboratorios de IA se han hecho caseros.** Meta y xAI empezaron a **alquilar** su capacidad de cómputo a terceros. ¿La clave? Compraron sus equipos *antes* de que la memoria se encareciera.

Ese cuarto punto parece menor. Es el que lo decide todo.

## La trampa: por qué el que llega tarde nunca alcanza

Aquí viene la idea más original del paper, y merece una analogía.

Imagina dos dueños de pisos de alquiler. El primero compró su edificio hace años y ya terminó de pagar la hipoteca: cada euro que cobra es beneficio. El segundo acaba de comprar, en el pico del mercado, y tiene que cubrir la letra todos los meses. ¿Quién puede bajar el precio del alquiler sin arruinarse?

La intuición dice que con el tiempo esto se empareja: los precios se normalizan y el recién llegado alcanza al veterano. **El paper demuestra que no.** La diferencia de costos entre quien ya tiene el equipo pagado y quien entra nuevo evoluciona así:

- **3.2 veces más caro** para el que entra en 2026
- **1.9 veces** en 2027 — el momento en que parece que casi se empareja
- y luego **vuelve a abrirse**: unas 3 veces si la memoria se abarata en 2028, o **más de 4 veces** si la escasez dura hasta 2030

¿Por qué no se cierra nunca? Por lo que el paper llama la **cinta transportadora de la depreciación**. Cada año, otra tanda de equipos termina de amortizarse en manos de los grandes y pasa a producir prácticamente gratis. Esa cinta va **más rápido** de lo que bajan los precios del hardware nuevo. Es una escalera mecánica que baja mientras tú intentas subirla corriendo.

Y el detalle demoledor: la ventaja **rota entre los grandes**, pero **nunca cruza** hacia los nuevos. Hoy le toca a uno, mañana a otro, pero siempre dentro del mismo club.

¿Y si te fabricas tus propios chips para saltarte al intermediario? El paper lo calcula: te ahorras el margen del fabricante, **pero no el precio de la memoria**, que es el problema de fondo. Resultado esperado: **25% de probabilidad de éxito, 34% de quedarte a medias y 41% de perder dinero**. Se puede mejorar, pero solo troceando la inversión en fases con puntos de salida, en vez de apostarlo todo de una vez.

## Entrenar modelos: se parte en dos mundos

Hasta ahora hablamos de *usar* modelos. Crearlos desde cero es otra historia, y también se rompe en dos:

- **La liga de lujo**: entrenar un modelo puntero costará entre **18.000 y 38.000 millones de dólares** en 2030. Eso lo pagan tres o cuatro empresas en el mundo entero.
- **La liga popular**: copiar la capacidad del modelo puntero *del año pasado*, partiendo de uno abierto y refinándolo, caerá hasta unos **5 millones de dólares**.

Hoy esa diferencia es de unas 40 veces. En 2030 será de **tres o cuatro órdenes de magnitud** — es decir, entre mil y diez mil veces.

La consecuencia es paradójica y bastante esperanzadora: **casi nadie podrá entrenar el mejor modelo del mundo, pero casi cualquiera podrá permitirse el mejor modelo de hace año y medio.** Lo puntero se convierte en un artículo de lujo; lo *suficientemente bueno* se convierte en algo tan barato como la electricidad.

## El corredor de solvencia: la cuenta que no sale

Llegamos al corazón del asunto. Se han anunciado inversiones colosales en centros de datos. ¿Salen las cuentas? Solo si se cumplen **dos condiciones a la vez**:

1. El uso mundial de IA debe **duplicarse cada año durante cuatro años seguidos** (multiplicarse por 16 en total).
2. Los modelos premium deben **seguir cobrando lo mismo** — sin guerras de precios.

El problema es que hay un tercer factor jugando en contra: el software mejora y cada año necesita un **30% menos de datos** para hacer lo mismo. Eso destruye demanda de hardware exactamente igual de rápido que la crea el crecimiento de usuarios.

Hagamos la cuenta despacio. Si $ T $ es el uso anual y $ b $ los datos que hay que mover por palabra, el ancho de banda que necesitas instalado es $ B = T \cdot b $. Como ambas cosas cambian de forma multiplicativa, **sus tasas de crecimiento se multiplican entre sí**:

$ \displaystyle g\_B \; = \; g\_T \cdot g\_b \; = \; \underbrace{2.0}\_{\text{el uso se duplica}} \times \underbrace{0.7}\_{\text{gasta un 30\% menos}} \; = \; 1.4 $

O sea: la demanda **real de hardware** crece un 40% al año, no un 100%. Y compuesta a lo largo de los cuatro años:

$ \displaystyle \frac{B\_{2030}}{B\_{2026}} \; = \; g\_B^{\,4} \; = \; 1.4^{4} \; \approx \; 3.84 $

**Traducción:** aunque el uso de la IA se multiplique por 16, la eficiencia se come casi todo el crecimiento y la capacidad que realmente hay que **vender** solo se multiplica por **3.8**. Y ese 3.8 es lo que tiene que pagar todo lo que se está construyendo ahora mismo.

Salirse del corredor por cualquiera de los dos lados hunde a alguien. ¿A quién? Depende de **cuándo** compró — igual que las cosechas de vino, hay añadas buenas y malas. El análisis del paper es tajante: las compras de **2026** y las de **2028–29** quedan gravemente expuestas, cada una a un escenario de precios distinto. Solo la añada **2027** aguanta las dos. Y el escalofrío final: **los contratos de la añada 2028–29, la más expuesta, se están firmando ahora mismo.**

### Dos avisos que valen oro

Antes de creerse cualquier gráfico de crecimiento, el paper deja dos advertencias:

- **Los contadores públicos de uso engañan.** Miden palabras generadas, pero muchas no las paga nadie — pruebas gratuitas, experimentos, reintentos. La demanda que **factura** es bastante menor que la que se publica.
- **Cualquier previsión anterior a mediados de 2026 está caducada.** La industria dio un giro de 180 grados: pasó de *generar todas las palabras posibles* a *gastar las mínimas*. El ahorro se convirtió en un objetivo de negocio, y eso invalida las proyecciones hechas antes.

Y de fondo, una tela de araña financiera: más de **800.000 millones de dólares** en acuerdos cruzados entre un puñado de empresas que se compran y se venden entre sí — NVIDIA invierte en OpenAI y a la vez le vende chips; OpenAI arrastra compromisos del orden de **1,15 billones** repartidos con Oracle, AMD, AWS y otros. Si las cuentas fallan, el contagio ya está cableado.

## China: jugar a otro juego

Entre abril y junio de 2026 pasó algo que el paper considera decisivo. El sistema **LineShine**, en Shenzhen, se puso primero del mundo en la lista TOP500 con casi **40.960 procesadores** de diseño propio — la primera vez que China lidera desde 2019.

En potencia bruta para IA todavía va por detrás, y el paper lo dice sin maquillaje: rinde menos que los sistemas estadounidenses equivalentes y su memoria es de una generación anterior. **Pero eso no es lo importante.**

Lo importante es que esa memoria **la fabrican ellos**. Mientras Occidente paga la crisis mundial de precios, China está fuera de esa crisis. Su curva de costos vive en otro planeta.

Es exactamente lo que pasó con los coches eléctricos: unos años por detrás en la gama alta, estructuralmente más baratos en la gama de volumen, y mejorando más rápido. **Lo que hay que mirar no es la posición en la tabla, es la pendiente.**

## Los cinco futuros posibles

El paper termina dibujando cinco escenarios para 2026–2030. Fijate en un detalle: **ninguno pasa del 25%**. Esa dispersión *es* el mensaje — nadie sabe cómo acaba esto.

| Escenario | Prob. | En una frase |
|---|---|---|
| **El oligopolio rotatorio** | 25% | Los grandes se reparten la ventaja por turnos; los nuevos nunca entran |
| **El batacazo de precios** | 25% | La eficiencia acelera, la demanda toca techo en 2027 y el desplome llega en 2028 |
| **La paradoja de Jevons** | 20% | Abaratar la IA dispara tanto su uso que absorbe toda la capacidad construida |
| **El valor se muda de sitio** | 18% | Lo que se paga deja de ser el modelo y pasa a ser el sistema que lo orquesta |
| **Dos mundos separados** | 12% | Un bloque occidental con memoria cara y otro chino desacoplado |

## Las cuentas, en código

Lo mejor de este análisis es que sus números centrales caben en unas pocas líneas. El script completo que genera la figura está en [`scripts/generate_memory_scarcity.py`](https://github.com/carlosfaz/carlosfaz.github.io/blob/main/scripts/generate_memory_scarcity.py):

```python
# El corredor: el uso se duplica cada año, pero cada palabra gasta un 30% menos
crec_uso, eficiencia, anios = 2.0, 0.70, 4

uso_acumulado = crec_uso ** anios                  # 16× más uso...
hardware_necesario = (crec_uso * eficiencia) ** anios   # ...pero solo 3.8× más hardware

# Entrenar en 2030: la liga de lujo contra la liga popular
lujo, popular = 18e9, 5e6
ratio = lujo / popular                             # 3,600 veces más caro
```

## El resultado

![A la izquierda: la diferencia de costo entre quien entra nuevo y quien ya tiene el equipo pagado, que se estrecha en 2027 y vuelve a abrirse hacia 2030 sin llegar nunca a igualarse. A la derecha: los cinco escenarios posibles con sus probabilidades]({{ site.baseurl }}/images/memory-scarcity-ai.svg)

Cómo leer la figura:

- **Panel izquierdo**: cuántas veces más caro le sale producir a quien entra nuevo frente a quien ya tiene el equipo amortizado. Se estrecha hasta 1,9 veces en 2027 — el espejismo del *"ya casi los alcanzo"* — y luego **vuelve a abrirse**. La línea verde marca el empate: nunca se toca.
- **Panel derecho**: los cinco futuros posibles. Que el más probable apenas llegue al 25% es la forma numérica de admitir que esto puede acabar de muchas maneras distintas.

Lo que imprime el programa:

```text
=== Escasez de memoria y reestructuración de la IA (arXiv:2607.07207) ===
Desventaja del que entra nuevo: 3.2× (2026) → 1.9× (2027) → ~3× o >4× (2029-30)

--- Corredor de solvencia ---
Uso de IA: se duplica cada año × 4 años = 16× acumulado
Gasto por palabra: -30% cada año → queda en 0.24× tras 4 años
Hardware realmente necesario: (2 × 0.7)^4 = 3.8× en 4 años

--- Entrenar un modelo en 2030 ---
Liga de lujo:    18.000-38.000 millones por modelo puntero
Liga popular:    ~5 millones (nivel del puntero anterior)
Diferencia: 3.600× - 7.600× (hoy es de solo ~40×)
```

## ¿Y esto a mí en qué me afecta?

El análisis es global, pero aterriza en decisiones muy concretas según dónde estés:

- **Si construyes centros de datos**: importa más *cuándo* compras que *qué* compras. Firmar hoy capacidad para 2028–29 al precio actual de la memoria es apostar a un escenario muy concreto. Mejor trocear la inversión en fases con puntos de salida.
- **Si vendes IA como servicio**: tu margen no depende de lo bueno que sea tu modelo, sino de la **fecha de la factura de tus equipos**. Competir contra alguien con el hardware ya pagado es competir contra un coste que tiende a ser solo la luz.
- **Si desarrollas productos con IA**: la división lujo–popular te regala una opción. Hoy un modelo abierto y afinado cubre casos que hace año y medio exigían lo más caro del mercado. **Diseñar tu producto para poder cambiar de modelo vale más que acertar con el modelo.**
- **Si inviertes**: la pregunta útil no es *"¿crecerá la IA?"* — casi seguro que sí — sino *"¿crecerá el uso que alguien **paga** lo suficiente para llenar lo que se está construyendo?"*. Son preguntas distintas, y solo la segunda paga las facturas.
- **Si solo lo miras desde fuera**: prepárate para que la IA capaz sea cada vez más barata y más local, mientras la IA puntera se encarece hasta ser cosa de tres empresas. Las dos cosas van a pasar a la vez.

## Lo que este análisis no promete

Un estudio de escenarios no es una bola de cristal, y conviene leerlo con las mismas reservas que pone su autor:

- **Esas probabilidades son un juicio experto, no una ley de la naturaleza.** El 25/25/20/18/12 refleja la información disponible en julio de 2026. Lo valioso es la estructura del razonamiento, no el segundo decimal.
- **La paradoja de Jevons puede ganar la partida.** Si abaratar la IA multiplica sus usos más rápido de lo que baja el precio, las cuentas salen solas. El paper le da un 20% — no es un escenario de consuelo.
- **Los "agentes" pueden romper la aritmética en cualquier dirección.** Una IA que trabaja sola en una tarea consume muchísimo más que un chat. Eso puede disparar la demanda... o acelerar la carrera por gastar menos. La misma tecnología empuja hacia los dos lados.
- **La luz y las redes no entran en la cuenta.** El análisis aísla el coste de mover datos, pero la electricidad contratada y la refrigeración son límites reales que pueden aparecer antes que la memoria.
- **La cifra de 1,15 billones mezcla peras y manzanas.** El propio autor avisa de que junta compromisos con validez legal muy distinta. Titular fácil, dato frágil.

Con todo, la idea central aguanta todas estas objeciones: **medir la IA por lo que cuesta mover datos, y no por lo rápido que calcula, cambia por completo quién parece competitivo.** Eso es lo que se queda.

## Conclusión

1. **El cuello de botella es la memoria, no la potencia.** Un modelo no piensa despacio: espera datos. Y los datos se pagan por byte movido.
2. **El que llega tarde no alcanza.** La cinta transportadora de la depreciación entrega equipos ya pagados a los grandes más rápido de lo que bajan los precios. La ventaja rota entre ellos; nunca sale del club.
3. **Entrenar se parte en dos ligas.** Lo puntero se vuelve un artículo de lujo de miles de millones; lo "suficientemente bueno" se vuelve casi gratis.
4. **Las cuentas solo salen en un pasillo muy estrecho.** El uso debe duplicarse cada año durante cuatro *y* los precios premium aguantar. La eficiencia juega en contra de quien construye.
5. **Mira la pendiente, no la foto.** China no lidera en IA, pero fabrica su propia memoria y eso la saca de la crisis que encarece a todos los demás. A veces importa más de dónde vienes que dónde estás.

Y si te quedas con una sola frase: **en la era de la IA, la pregunta que decide quién gana dinero no es qué modelo tienes, sino a qué precio compraste la memoria.**

## Referencia y más lectura

- **El paper**: Satoshi Matsuoka, *"Memory Scarcity, Open Models, and the Restructuring of the AI Industry, 2026–2030"*, [arXiv:2607.07207](https://arxiv.org/abs/2607.07207) [econ.GN], julio de 2026.
- **[Teoría de la Ruina]({{ site.baseurl }}/teoria-ruina/)**: cómo una empresa rentable *en promedio* puede quebrar igualmente. Es el mismo problema del corredor de solvencia, contado con aseguradoras.
- **[Gestión de Riesgos Avanzada]({{ site.baseurl }}/gestion-riesgos-avanzada/)**: escenarios extremos y pruebas de estrés, la misma lógica aplicada a los mercados en lugar de a los centros de datos.
