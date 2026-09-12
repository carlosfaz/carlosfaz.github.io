---
layout: post
title: "Fundamentals: qué significa cada número de tu cartera"
use_math: true
published: true
date: 2026-09-11
category: "Finanzas Cuantitativas"
tags: ["Finanzas Cuantitativas", "Gestión de Riesgos", "Inversión"]
thumbnail: "/images/fundamentals.svg"
---

## 1. Resumen general

*Los conceptos de la pantalla principal: el estado de tu cartera hoy.*

### Dinero y resultado

- **Valor de mercado**: lo que valen hoy todas tus acciones juntas.
- **Invertido**: el dinero que has puesto de tu bolsillo.
- **P&L no realizado**: ganancia o pérdida que llevas sin vender todavía («en papel»). P&L = *profit and loss*, ganancias y pérdidas.

### Riesgo y premio

- **Sharpe**: cuánto te pagan por cada unidad de riesgo que aguantas. Mayor que 1 = bueno; mayor que 2 = muy bueno.
- **Sortino**: igual que el Sharpe, pero solo castiga las caídas, no las subidas.
- **Calmar**: ganancia anual dividida entre la peor caída.
- **Máx. drawdown**: la peor caída del periodo, de pico a valle.
- **Ulcer Index**: cuánto dolor sostenido hubo: pesan más las caídas profundas y largas.
- **VaR 95**: la pérdida que no se supera el 95% de los días; lo que podrías perder en un mal día.
- **CAGR**: crecimiento anual compuesto: el ritmo constante al que crece tu dinero.
- **Volatilidad**: cuánto se mueve tu cartera en un año; más movimiento = más riesgo.

### Comparación con el mercado

- **Benchmark**: índice de referencia para compararte: SPY (S&P 500), QQQ (Nasdaq 100) y DIA (Dow Jones).
- **Base 100**: truco para comparar curvas: todas empiezan en 100.
- **Alpha**: lo que le ganas al índice gracias a tu propia selección de acciones.
- **Beta**: cuánto te mueves respecto al mercado. 1 = igual; 1.35 = un 35% más brusco que él.
- **R²**: qué parte de tus movimientos explica el mercado, de 0 a 1.
- **TWR**: rentabilidad «limpia», quitando el efecto de meter o sacar dinero.

### Diversificación y concentración

- **Ratio de diversificación**: cuánto te protege combinar acciones. 1 = no protege nada; más alto = mejor.
- **N efectivo**: en cuántas acciones «de verdad» está repartido tu dinero. 11.1 de 13 = tus 13 acciones se comportan como 11.
- **Concentración**: el peso de tu posición más grande.
- **Top 3**: lo que suman tus tres posiciones mayores.
- **HHI**: termómetro de concentración: por encima de 0.25 la cartera está muy concentrada.

### Estadísticas del diagnóstico

- **Días ganadores**: porcentaje de días que la cartera cerró en positivo.
- **Profit factor**: dólares ganados por cada dólar perdido. Mayor que 1 = rentable.
- **Correlación media**: si tus acciones se mueven juntas. Cerca de 1 = todas a la vez: diversificación de mentira.
- **Asimetría**: si las sorpresas suelen ser buenas (positiva) o malas (negativa).
- **Curtosis**: si hay más días extremos de los que predice la campana normal.
- **Probabilidad de ganancia**: porcentaje de futuros simulados (Monte Carlo) que acaban el año en ganancia.

## 2. Performance

*Los conceptos sobre cómo ha rendido tu cartera en el tiempo.*

- **Retorno total**: lo ganado (o perdido) en todo el periodo analizado.
- **Mejor y peor día**: tus dos jornadas más extremas, en porcentaje.
- **Omega**: ganancias totales divididas entre pérdidas totales. Mayor que 1 = ganas más de lo que pierdes.
- **Volatilidad bajista**: cuánto se mueve tu cartera solo en las caídas; es el riesgo «malo».
- **Underwater**: en cada fecha, cuánto falta para recuperar el máximo anterior. Todo lo que está bajo cero es una caída sin recuperar.
- **Campana normal**: la referencia teórica de cómo «deberían» repartirse los días. Si tus puntas reales sobresalen, hay más sustos de los esperados.
- **Métricas móviles**: Sharpe, beta y volatilidad recalculados en ventanas deslizantes: sirven para ver si tu ventaja es estable o va y viene.
- **Estacionalidad mensual**: lo ganado cada mes; la última columna es el año completo.
- **Tracking error**: cuánto te separas del índice de referencia.
- **Information ratio (IR)**: el exceso de retorno que consigues por cada unidad de tracking error: premio por separarte acertando.
- **Captura alcista**: porcentaje de las subidas del índice que logras aprovechar. Ideal: por encima de 100.
- **Captura bajista**: porcentaje de las bajadas del índice que sufres. Ideal: por debajo de 100.
- **Episodio de drawdown**: una caída concreta: cuándo empezó, su fondo, cuánto duró y cuánto tardó en recuperarse. «En curso» = aún no se ha recuperado.

## 3. Riesgo

*Los conceptos sobre cuánto puedes perder y de dónde viene el peligro.*

### Riesgo de cola (los malos días)

- **VaR**: la pérdida máxima esperada en un día malo, con un nivel de confianza: al 95% es un día malo normal (1 de cada 20); al 99%, uno extremo (1 de cada 100). Se da en porcentaje y en dólares.
- **CVaR (Expected Shortfall)**: cuando el día sí rompe el VaR, esta es la pérdida media. Responde a «y si pasa, ¿cuánto duele?».
- **VaR Cornish-Fisher**: el VaR corregido por asimetría y colas gruesas, porque la bolsa da más sustos de los que dice la campana normal.

### Correlación y estructura

- **Matriz de correlación**: mapa de calor entre pares de acciones: rojo = se mueven juntas; cian = independientes.
- **PCA (descomposición factorial)**: en cuántos «sabores» se reparte tu riesgo. Si el factor 1 explica demasiado, casi todo tu riesgo es uno solo: el mercado.
- **Cargas del factor 1**: qué acciones siguen más ese riesgo dominante.

### Atribución (quién aporta el riesgo)

- **Contribución al riesgo**: porcentaje de la volatilidad total que aporta cada acción.
- **Component VaR**: el VaR total repartido entre las acciones: quién es el culpable del riesgo.
- **Δ Riesgo − Peso**: si una acción aporta más riesgo del que representa en dinero, domina tus sustos: es candidata natural a recortar.
- **Beta vs cartera**: cuánto se mueve una acción respecto a tu propia cartera.

### Monte Carlo

- **Simulación Monte Carlo**: 4,000 futuros posibles a 12 meses, construidos remuestreando el comportamiento real de tu cartera (*bootstrap*).
- **Escenario mediano**: el valor en el centro de todos los futuros simulados.
- **P5 (escenario adverso)**: el 5% peor de los futuros: el mal final razonable.
- **P95 (escenario favorable)**: el 5% mejor de los futuros: el buen final razonable.

## 4. Optimización

*Los conceptos de las «recetas» automáticas para mejorar la cartera. Son una referencia, no una predicción.*

- **Frontera eficiente (Markowitz)**: las mejores combinaciones posibles de riesgo y retorno: para cada nivel de riesgo, la cartera que más gana.
- **Portafolio de máximo Sharpe**: el mejor punto de la frontera: la combinación que más paga por cada unidad de riesgo.
- **CML (Capital Market Line)**: la línea que une el interés sin riesgo con el portafolio de máximo Sharpe; marca el límite teórico de lo alcanzable.
- **GMV (mínima varianza)**: la combinación más tranquila posible: la de menor volatilidad.
- **Tasa libre de riesgo**: lo que paga el dinero «seguro» (aquí 5%): el punto de partida para exigir premio al riesgo.
- **Retorno esperado**: lo que sugiere el histórico para cada acción; es una referencia, no una promesa.
- **Risk Parity (paridad de riesgo)**: repartir el *riesgo* en partes iguales entre las acciones, no el dinero: a las nerviosas les toca menos peso y a las tranquilas, más. Suele suavizar las caídas a costa de ganar un poco menos.
- **Reasignación sugerida**: para cada acción, la acción indicada por el optimizador: **Aumentar**, **Reducir** o **Mantener**.

## 5. Posiciones

*Los conceptos del detalle operativo, acción por acción.*

- **Precio medio**: lo que pagaste de media por cada acción de ese valor.
- **Coste total**: lo que pagaste en total: unidades por precio medio.
- **Valor actual**: lo que vale hoy esa posición: unidades por último precio.
- **P&L y rentabilidad**: valor actual menos coste, en dólares y en porcentaje sobre lo pagado.
- **Peso**: qué porcentaje de tu dinero está en esa acción.
- **Rango de 120 días**: el mínimo y el máximo de precio de los últimos 120 días de mercado.
- **vs Máx**: cuánto le falta al precio actual para alcanzar su máximo de 120 días.
- **Mapa de exposición (treemap)**: cada cuadro es una acción: el tamaño es el dinero invertido y el color dice si gana (verde) o pierde (rojo).

## 6. Histórico

*Los conceptos del diario real de tu cartera, con tus aportes de dinero incluidos.*

- **Retorno TWR**: tu rentabilidad quitando el efecto de meter o sacar dinero: mide la calidad de la gestión, no el momento de los aportes.
- **TWR anualizado**: ese mismo rendimiento llevado a ritmo anual.
- **Drawdown realizado**: las caídas reales que ha sufrido tu cartera tal y como las viviste.
- **Brecha capital–valor**: la distancia entre lo que has metido y lo que vale: tu ganancia acumulada.

## 7. Indicadores de la ficha de cada activo

*Los conceptos técnicos que ves al abrir cualquier acción (V, TSM, MU, GOOGL, BRK-B, AMZN, GE, LLY, VSTS, JPM…).*

- **RSI 14**: termómetro de 0 a 100 sobre las últimas 14 sesiones. Por encima de 70 = *sobrecompra* (quizá caro); por debajo de 30 = *sobreventa* (quizá barato); en medio = rango neutro.
- **Medias móviles (SMA 20 y 50)**: el promedio del precio de los últimos 20 y 50 días: marcan la tendencia. Precio por encima = tendencia sana; por debajo = débil.
- **Volumen**: cuántas acciones cambiaron de manos en el día. Verde = día de subida; rojo = día de bajada.
- **Perfil de volumen**: a qué precios se negoció más la acción en el periodo.
- **POC (punto de control)**: el precio más negociado de todos (la barra ámbar): suele actuar de imán para el precio.
- **Drawdown del activo**: las caídas de esa acción desde su propio máximo.
- **Contribución al riesgo**: cuánto del riesgo total de tu cartera pone esa acción.

## 8. Fundamentales de empresa

*Los datos de la compañía que aparecen al final de cada ficha (fuente: Yahoo Finance).*

### Valoración (si está cara o barata)

- **P/E (Trailing)**: cuántos dólares pagas por cada dólar de beneficio anual de la empresa. Alto = el mercado espera mucho de ella.
- **PEG Ratio**: el P/E ajustado por su crecimiento. Por debajo de 1 suele considerarse barata para lo que crece.
- **Price/Sales**: lo que pagas por cada dólar de ventas.
- **Price/Book**: lo que pagas frente a lo que vale la empresa «en libros» (sus activos menos sus deudas).

### Calidad del negocio

- **ROE**: beneficio que genera por cada 100 dólares de patrimonio. Cuanto mayor, mejor negocio.
- **ROA**: beneficio que genera por cada 100 dólares de activos.
- **Rev. Growth**: cuánto crecen las ventas al año.
- **Profit Margin**: de cada 100 dólares que vende, cuántos le quedan de beneficio.
- **Operating Margin**: lo mismo, pero contando solo el negocio (sin intereses ni impuestos).

### Salud financiera

- **Debt/Equity**: deuda por cada dólar propio. Alto = muy apalancada.
- **Current Ratio**: si puede pagar sus deudas de corto plazo con lo que tiene a mano. Mayor que 1 = puede.
- **Quick Ratio**: lo mismo pero sin contar inventarios: el examen más exigente de liquidez.

### Para el accionista

- **Div. Yield**: porcentaje anual que paga en dividendos sobre el precio actual.
- **Div. Rate**: dólares de dividendo que paga al año por acción.
- **EPS**: beneficio por acción: lo que «gana» cada título.
- **Book Value**: valor en libros por acción: lo que valdría cada título si la empresa se liquidara en papel.
- **Beta (de la empresa)**: cuánto se mueve la acción frente al mercado: 1 = igual que él.

