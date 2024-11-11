### A. Las funciones create_folds() y cross_validation()

```R
# Cargar los paquetes necesarios
library(rpart)
library(dplyr)

# Función para crear los folds
create_folds <- function(data, num_folds) {
  set.seed(123)  # Fijamos una semilla para reproducibilidad
  indices <- sample(1:nrow(data))  # Barajamos los índices
  fold_size <- floor(nrow(data) / num_folds)  # Tamaño de cada fold
  folds <- vector("list", num_folds)  # Lista vacía para guardar los folds
  
  for (i in 1:num_folds) {
    start_idx <- (i - 1) * fold_size + 1
    end_idx <- min(i * fold_size, nrow(data))
    folds[[i]] <- indices[start_idx:end_idx]  # Asignamos los índices al fold
  }
  
  return(folds)
}

# Función para realizar cross-validation
cross_validation <- function(data, num_folds) {
  # Convertir la columna de respuesta a factor
  data$inclinacion_peligrosa <- as.factor(data$inclinacion_peligrosa)
  
  folds <- create_folds(data, num_folds)  # Crear los folds
  accuracy <- numeric(num_folds)  # Vector para guardar las métricas
  precision <- numeric(num_folds)
  sensitivity <- numeric(num_folds)
  specificity <- numeric(num_folds)
  
  # Fórmula del modelo (ajustar con los nombres correctos de las variables)
  train_formula <- formula(inclinacion_peligrosa ~ altura + circ_tronco_cm + lat + long + seccion + especie)
  
  # Loop para entrenar y evaluar el modelo en cada fold
  for (i in 1:num_folds) {
    # Dividir el dataframe en entrenamiento y prueba
    test_indices <- folds[[i]]
    train_data <- data[-test_indices, ]
    test_data <- data[test_indices, ]
    
    # Entrenar el modelo de árbol de decisión
    tree_model <- rpart(train_formula, data=train_data)
    
    # Realizar las predicciones sobre el conjunto de prueba
    predictions <- predict(tree_model, test_data, type='class')
    
    # Calcular la matriz de confusión
    cm <- table(predictions, test_data$inclinacion_peligrosa)
    
    # Extraer los valores de la matriz de confusión
    TP <- cm[2, 2]
    TN <- cm[1, 1]
    FP <- cm[1, 2]
    FN <- cm[2, 1]
    
    # Calcular las métricas
    accuracy[i] <- (TP + TN) / (TP + TN + FP + FN)
    precision[i] <- TP / (TP + FP)
    sensitivity[i] <- TP / (TP + FN)
    specificity[i] <- TN / (TN + FP)
  }
  
  # Devolver las métricas medias y desviación estándar
  metrics <- data.frame(
    Metric = c("Accuracy", "Precision", "Sensitivity", "Specificity"),
    Mean = c(mean(accuracy), mean(precision), mean(sensitivity), mean(specificity)),
    Std_Dev = c(sd(accuracy), sd(precision), sd(sensitivity), sd(specificity))
  )
  
  return(metrics)
}

```
## Tabla con los resultados
| Metric      | Mean     | Std_Dev   |
|-------------|----------|-----------|
| Accuracy    | 0.8884013 | 0.01646887 |
| Precision   | 0.0000000 | 0.00000000 |
| Sensitivity | NaN      | NA        |
| Specificity | 0.8884013 | 0.01646887 |
