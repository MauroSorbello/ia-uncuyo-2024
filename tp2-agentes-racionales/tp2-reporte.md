# Reporte ejercicios 3 y 4
## Introducción
Se realizaron experimentos para simular y comparar la medida de rendimiento, de dos agentes diferentes (agente reflexivo simple y agente con comportamiento totalmente aleatorio), para el conocido entorno del mundo de la aspiradora. 
## Marco Teórico
**Entorno**
El entorno es una grilla de nxn casilleros, parcialmente observable, donde cada casillero puede estar sucio (1) o limpio (0). 
**Agentes**
Los agentes, construidos utilizando PEAS, tendrán una medida de performance. 
Esta medida será tomada según cuantos casilleros fueron limpiados por los agentes. 
Las acciones permitidas a los agentes son: 
- Arriba
- Abajo
- Izquierda
- Derecha
- Limpiar (aspirar)
- NoHacerNada
La diferencia de los agentes es que el agente reflexivo evalúa el casillero en el que se encuentra, para decidir limpiar o no hacer nada, ahorrando pasos cuando escoge no hacer nada. Mientras que, el agente con comportamiento totalmente aleatorio, no observa el entorno en ningún momento, y como lo indica su nombre, su comportamiento es aleatorio. 
## Diseño experimental
El experimento consta de evaluar y comparar el desempeño de los agentes diseñados anteriormente, con combinaciones de parametros de porcentaje de suciedad y cantidad de celdas nxn del entorno, para los dos agentes. 
Cada entorno, junto con la posicion inicial del agente, se genera con una semilla, obteniendo asi, el mismo entorno a probar con los dos agentes y posibilitando la replicacion del experimento.
Para cada combinacion de porcentaje de suciedad y cantidad de celdas nxn, se generan 10 entornos diferentes y se evalua el desempeño de ambos agentes.

**Parametros utilizados**
- Entornos de: 2 × 2, 4 × 4, 8 × 8, 16 × 16, 32 × 32, 64 × 64, 128 × 128.
- Porcentaje de suciedad en el ambiente: 0.1, 0.2, 0.4, 0.8