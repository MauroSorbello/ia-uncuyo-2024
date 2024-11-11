# Cargar las librerías necesarias
library(dplyr)

# Cargar el archivo de validación
data <- read.csv("C:/Users/Martinotebook/Documents/nacho (podes borrar tranqui)/2° año/Paradigmas/lab/ia-uncuyo-2024/tp7-ml/code/intro/arbolado-mendoza-dataset-validation.csv")

# Determinar la clase mayoritaria en la columna 'inclinacion_peligrosa'
majority_class <- data %>%
  count(inclinacion_peligrosa) %>%
  arrange(desc(n)) %>%
  slice(1) %>%
  pull(inclinacion_peligrosa)

# Implementar la función biggerclass_classifier
biggerclass_classifier <- function(df) {
  df <- df %>%
    mutate(prediction_class = majority_class)
  return(df)
}

# Aplicar la función biggerclass_classifier al dataframe cargado
data <- biggerclass_classifier(data)

# Calcular la matriz de confusión
confusion_matrix <- data %>%
  summarise(
    True_Positive = sum(inclinacion_peligrosa == 1 & prediction_class == 1),
    True_Negative = sum(inclinacion_peligrosa == 0 & prediction_class == 0),
    False_Positive = sum(inclinacion_peligrosa == 0 & prediction_class == 1),
    False_Negative = sum(inclinacion_peligrosa == 1 & prediction_class == 0)
  )

# Mostrar la matriz de confusión
print(confusion_matrix)
