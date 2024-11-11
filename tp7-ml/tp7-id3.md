## Árbol de Decisión para "play"

- **outlook**
  - **sunny**
    - **humidity**
      - high: no
      - normal: yes
  - **overcast**: yes
  - **rainy**
    - **windy**
      - false: yes
      - true: no

## Estrategias de los Árboles de Decisión para Datos de Tipo Real

Los árboles de decisión enfrentan desafíos al trabajar con datos de tipo real (variables numéricas continuas) debido a la necesidad de crear divisiones o "umbrales" adecuados en el proceso de particionamiento. Las estrategias clave para manejar este tipo de datos incluyen:

1. **División en puntos de umbral**: Para una variable continua, el árbol de decisión selecciona un punto de corte (o umbral) que maximice alguna medida de pureza, como la ganancia de información o la reducción de la varianza, dividiendo los datos en dos subconjuntos. Por ejemplo, una variable de temperatura podría dividirse en "temperatura <= 25" y "temperatura > 25" para optimizar la separación de clases.

2. **Binning o discretización**: Otra estrategia es discretizar la variable continua, dividiéndola en intervalos (o "bins") y tratándola como categorías. Aunque esto puede simplificar el modelo y reducir la variabilidad, puede resultar en pérdida de información si no se realiza con cuidado.

3. **Ajuste de profundidad del árbol y poda**: Para evitar el sobreajuste en árboles de decisión que manejan datos continuos, se pueden aplicar técnicas de poda y limitar la profundidad del árbol. Esto controla el sobreajuste que puede surgir debido a múltiples divisiones en datos continuos.

4. **Selección automática de umbrales**: Algunos algoritmos avanzados, como los árboles de decisión en bibliotecas de Python como `scikit-learn`, implementan métodos automáticos para evaluar puntos de división óptimos para cada variable continua, mejorando el rendimiento sin necesidad de discretizar manualmente.

