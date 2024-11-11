# Cargar librerías necesarias
library(dplyr)

# Función para generar la columna 'prediction_prob' con valores aleatorios
generate_prediction_prob <- function(df) {
  df %>%
    mutate(prediction_prob = runif(nrow(df), min = 0, max = 1))  # Genera números aleatorios entre 0 y 1
}

# Función random_classifier para generar la columna 'prediction_class'
random_classifier <- function(df) {
  df %>%
    mutate(prediction_class = ifelse(prediction_prob > 0.5, 1, 0))  # Asigna clase 1 si prediction_prob > 0.5, sino 0
}

# Cargar el archivo 'arbolado-mendoza-dataset-validation.csv'
df <- read.csv("C:/Users/Martinotebook/Documents/nacho (podes borrar tranqui)/2° año/Paradigmas/lab/ia-uncuyo-2024/tp7-ml/code/intro/arbolado-mendoza-dataset-validation.csv")

# Aplicar las funciones
df <- df %>%
  generate_prediction_prob() %>%  # Generar la columna 'prediction_prob'
  random_classifier()  # Generar la columna 'prediction_class'

# Calcular la matriz de confusión utilizando dplyr
confusion_matrix <- df %>%
  summarise(
    true_positive = sum(prediction_class == 1 & inclinacion_peligrosa == 1),  # True Positives
    true_negative = sum(prediction_class == 0 & inclinacion_peligrosa == 0),  # True Negatives
    false_positive = sum(prediction_class == 1 & inclinacion_peligrosa == 0), # False Positives
    false_negative = sum(prediction_class == 0 & inclinacion_peligrosa == 1)  # False Negatives
  )

# Mostrar la matriz de confusión
print(confusion_matrix)
