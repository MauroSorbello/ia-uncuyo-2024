library(randomForest)
library(dplyr)

# Cargo los datos
data <- read.csv("C:/Users/Martinotebook/Documents/nacho (podes borrar tranqui)/2° año/Paradigmas/lab/ia-uncuyo-2024/tp7-ml/data/arbolado-mza-dataset.csv")
data_test <- read.csv("C:/Users/Martinotebook/Documents/nacho (podes borrar tranqui)/2° año/Paradigmas/lab/ia-uncuyo-2024/tp7-ml/data/arbolado-mza-dataset-test.csv")

# Filtrar todos los árboles con inclinación peligrosa
muestra_inclinacion_peligrosa <- data[data$inclinacion_peligrosa == 1, ]

# Filtrar algunos árboles con inclinación no peligrosa (la misma cantidad que exista de inclinación peligrosa para balancear)
muestra_inclinacion_no_peligrosa <- data %>% filter(inclinacion_peligrosa == 0) %>% sample_n(3500)

# Unir los dos conjuntos de datos
data_filtrado <- rbind(muestra_inclinacion_peligrosa, muestra_inclinacion_no_peligrosa)

# Establecer predictores y respuesta para randomForest
# Excluir columnas como "inclinacion_peligrosa", "id", "nombre_seccion", "area_seccion", "ultima_modificacion", "lat" y "long"
predictores <- data_filtrado[, !(colnames(data_filtrado) %in% c("inclinacion_peligrosa", "id", "nombre_seccion", "area_seccion","seccion", "ultima_modificacion","circ_tronco_cm"))]

# Asegúrate de que la variable de respuesta sea un factor
respuesta <- factor(data_filtrado$inclinacion_peligrosa)

# Entrenamiento del modelo Random Forest
modelo <- randomForest(x = predictores, y = respuesta, ntree = 3900, mtry = 3)

# Realizar predicciones
predictions <- predict(modelo, newdata = data_test)

# Ver las primeras 30 predicciones
head(predictions, 30)
summary(predictions)

# Convertir las predicciones a 1 o 0
predicciones_transformadas <- as.numeric(predictions) - 1  # Convierte 'No' a 0 y 'Sí' a 1

# Imprimir el modelo
print(modelo)

# Crear un dataframe de resultados
resultado <- data.frame(ID = data_test$id, inclinacion_peligrosa = predicciones_transformadas)

# Ver las primeras filas del resultado
head(resultado)

# Guardar el resultado en un archivo CSV
write.csv(resultado, file = "resultados.csv", row.names = FALSE)
