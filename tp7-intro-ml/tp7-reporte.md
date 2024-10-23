1. For each of parts (a) through (d), indicate whether we would generally
expect the performance of a fexible statistical learning method to be
better or worse than an infexible method. Justify your answer.

(a) The sample size n is extremely large, and the number of predictors p is small.

El modelo flexible va a funcionar peor que el inflexible, porque citando el libro "But in general, ftting a more fexible model requires estimating a greater number of parameters." Como en esta muestra hay pocos predictores, el modelo flexible estará demasiado lejos de la verdadera f.

(b) The number of predictors p is extremely large, and the number
of observations n is small.

El modelo flexible puede provocar overfitting "This happens because our statistical learning
procedure is working too hard to fnd patterns in the training data, and
may be picking up some patterns that are just caused by random chance
rather than by true properties of the unknown function f". En cambio el inflexible como el lineal "The bias introduced by inflexibility may be outweighed by the reduction in variance due to overfitting in this case."

(c) The relationship between the predictors and response is highly
non-linear.

very fexible
approaches, such as the splines discussed in Chapter 7 and displayed in
Figures 2.5 and 2.6, and the boosting methods discussed in Chapter 8, can
lead to such complicated estimates of f that it is diffcult to understand
how any individual predictor is associated with the response.

(d) The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely
high

Los métodos inflexibles tendran un mejor desempeño, ya que imponen una estructura en el modelo (como la linealidad), lo que ayuda a reducir la complejidad del modelo y a mitigar el impacto del ruido. Esto permite que los modelos inflexibles sean más robustos y estables, conduciendo a predicciones más confiables en presencia de alta varianza en los errores.
En cambio, los métodos flexibles pueden tener dificultades porque tienden a ajustar no solo la señal (la relación real entre las variables) sino también el ruido presente en los datos.

2. Explain whether each scenario is a classifcation or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

(a) We collect a set of data on the top 500 frms in the US. For each frm we record proft, number of employees, industry and the CEO salary. We are interested in understanding which factors afect CEO salary.

Es un problema de regresión, dado a que la salida es un valor continuo. Además esta interesado en la inferencia, ya que el análisis se centra en identificar y cuantificar relaciones entre variables, lo que es característico de la inferencia estadística. n = 500, p = 3


(b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

Clasificacion y prediccion. n = 20, p = 13

(c) We are interested in predicting the % change in the USD/Euroexchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market

Es un problema de regresión, porque se refiere a una tarea en la que se intenta predecir un valor numérico continuo (% de cambio en USD/Euroeschange) a partir de un conjunto de variables independientes (predictores) (the % change in the US market, the % change in the British market, and the % change in the German market). 
Esta mas interesado en la prediccion.
n = 4.2*12 = 52
p = 3

5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less
flexible approach? When might a less flexible approach be preferred?

Muy Flexibles:
- Desventajas: Menos interpretados, sobreajustes
- Ventajas:

Flexibles:
- Ventajas: Necesita menos datos
- Desventajas: Menos precisos

6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a para metric approach to regression or classification (as opposed to a non parametric approach)? What are its disadvantages?

Parametrico:
- Poco flexible

No Parametrico:
- Flexible

7)

(b) K=1 -> Verde
(c) K=3 -> Rojo
(d) If the Bayes decision boundary in this problem is highly non linear, then would we expect the best value for K to be large or small? Why

K pequeño, para que se pueda hacer un enfoque mas flexible.