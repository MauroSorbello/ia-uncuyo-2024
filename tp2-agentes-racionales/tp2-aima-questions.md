# AIMA QUESTIONS

## 2.10 

a) ¿Puede un agente simple reflexivo ser perfectamente racional para este entorno? Explicar. 

No puede ser perfectamente racional, dado a que no posee información sobre cuantas celdas sucias quedan, por lo cual siempre ocupara los mil movimientos, aunque estén todas las celdas limpias. 

b) ¿Qué pasa con un agente reflexivo con estado?  

Un agente reflexivo con estado almacenaría las celdas por las que paso, permitiéndole no volver a las anteriores y probablemente sería más eficiente. Pero no sería perfectamente racional en entornos de nxn con n grande porque sigue sin conocer si están todas las celdas limpias. En caso de ser n pequeño probablemente registraría todas las celdas limpias y sería perfectamente racional. 

c) ¿Cómo cambian sus respuestas de a y b si las percepciones del agente le dan la categoría limpia/sucio? 

Allí si se conseguiría perfectamente racional, dado a que los agentes elegirían seguir por el camino donde los casilleros están sucios. Minimizando la cantidad de penalizaciones y maximizando las celdas limpiadas. 

## 2.11 

a) ¿Puede un agente reflexivo simple ser perfectamente racional para este entorno? Explicar. 

No, el agente reflexivo simple solo conoce la información de su estado (celda en la que se encuentra) y sus movimientos luego de limpiar o no, son aleatorios. Por ende, no puede ser perfectamente racional 

b) ¿Puede un agente aleatorio superar a un agente reflexivo simple? 

Un agente aleatorio no puede superar a un agente reflexivo simple, dado a que el agente simple al conocer la información de su estado toma decisiones para perder menos movimientos respecto al agente aleatorio. 

Si el entorno es de nxn, y n es menor a 8, estos tendrán medidas de performance parecidas. Pero al aumentar n, aumentan la cantidad de celdas y se visualizara una amplia diferencia a favor del agente reflexivo simple, con respecto al agente aleatorio. 

c) ¿Puede un agente reflexivo con estado superar a un agente reflexivo simple? Diseñar tal agente 

El agente reflexivo con estado supera al agente reflexivo simple, ya que guarda la anterior celda por la que paso, entonces en el siguiente movimiento no vuelve sobre sus pasos. En comparación con el agente reflexivo simple el cual su movimiento es aleatorio. 