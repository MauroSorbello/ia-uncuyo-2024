library(dplyr)
library(ggplot2)

#___1)___ Creacion de train_data y validation_data

# data <- read.csv("arbolado-mza-dataset.csv")
# 
# set.seed(123)  # Puedes cambiar el número de la semilla
# 
# validation_indices <- sample(nrow(data), size = 0.2 * nrow(data))
# validation_data <- data[validation_indices, ]
# 
# train_data <- data[-validation_indices, ]
# 
# write.csv(validation_data, "arbolado-mendoza-dataset-validation.csv", row.names = FALSE)
# write.csv(train_data, "arbolado-mendoza-dataset-train.csv", row.names = FALSE)
# 
# cat("Los archivos de validación y entrenamiento se han guardado correctamente.")
# 
#------------------------------------------------------------------
#___2)___ 

# #--a. Distribución de la clase `inclinacion_peligrosa`
# #Crear una tabla de frecuencias y calcular la proporción de cada categoría
# inclinacion_distribucion <- table(train_data$inclinacion_peligrosa)
# inclinacion_porcentaje <- prop.table(inclinacion_distribucion) * 100
# 
# print("Distribución de la inclinación peligrosa:")
# print(inclinacion_distribucion)
# print("Porcentaje de inclinación peligrosa:")
# print(inclinacion_porcentaje)
# 
# # Gráfico de barras para la distribución
# grafico <- ggplot(train_data, aes(x = factor(inclinacion_peligrosa))) +
#   geom_bar() +
#   labs(title = "Distribución de Inclinación Peligrosa",
#        x = "Inclinación Peligrosa",
#        y = "Número de Árboles") +
#   theme_bw()
# 
# ggsave("Distribucion_Inclinacion_Peligrosa.png", plot = grafico, width = 8, height = 6, dpi = 300)
# 
# #------------------------------------------------------------------
# #--b)¿Se puede considerar alguna sección más peligrosa que otra?
# # Calcular la cantidad de árboles con inclinación peligrosa por sección
# seccion_peligrosa <- train_data %>%
#   group_by(seccion) %>%
#   summarise(total_arboles = n(),
#             arboles_peligrosos = sum(inclinacion_peligrosa == 1, na.rm = TRUE),
#             porcentaje_peligrosos = (arboles_peligrosos / total_arboles) * 100)
# 
# print("Análisis de inclinación peligrosa por sección:")
# print(seccion_peligrosa)
# 
# # Gráfico de barras para mostrar las secciones más peligrosas
# grafico2 <- ggplot(seccion_peligrosa, aes(x = factor(seccion, levels = seccion_peligrosa$seccion[order(-seccion_peligrosa$porcentaje_peligrosos)]), 
#                                           y = porcentaje_peligrosos)) +
#   geom_bar(stat = "identity") +
#   labs(title = "Porcentaje de Árboles con Inclinación Peligrosa por Sección",
#        x = "Sección",
#        y = "Porcentaje de Árboles Peligrosos") +
#   theme_bw() +
#   coord_flip()
# 
# ggsave("Porcentaje_peligrosos_por_secc.png", plot = grafico2, width = 8, height = 6, dpi = 300)
# 
# #------------------------------------------------------------------
# #--c) # Calcular la cantidad de árboles con inclinación peligrosa por especie
# especie_peligrosa <- train_data %>%
#   group_by(especie) %>%
#   summarise(total_arboles = n(),
#             arboles_peligrosos = sum(inclinacion_peligrosa == 1, na.rm = TRUE),
#             porcentaje_peligrosos = (arboles_peligrosos / total_arboles) * 100)
# 
# print("Análisis de inclinación peligrosa por especie:")
# print(especie_peligrosa)
# 
# # Gráfico de barras para mostrar el porcentaje de árboles peligrosos por especie
# grafico3 <- ggplot(especie_peligrosa, aes(x = reorder(especie, -porcentaje_peligrosos), 
#                                           y = porcentaje_peligrosos)) +
#   geom_bar(stat = "identity") +
#   labs(title = "Porcentaje de Árboles con Inclinación Peligrosa por Especie",
#        x = "Especie",
#        y = "Porcentaje de Árboles Peligrosos") +
#   theme_bw() +  
#   coord_flip()
# 
# ggsave("Porcentaje_peligrosos_por_especie.png", plot = grafico3, width = 8, height = 6, dpi = 300)


#------------------------------------------------------------------
#___3)___ 
#---b) Generar pictogramas de para circ_tromo_Cm, con distintos bins

# Histograma de la variable circ_tronco_cm con diferentes números de bins
# Histograma con 10 bins
histograma_10_bins <- ggplot(train_data, aes(x = circ_tronco_cm)) +
  geom_histogram(bins = 10, fill = "blue", color = "black", alpha = 0.7) +
  labs(title = "Histograma de circ_tronco_cm con 10 Bins",
       x = "Circunferencia del Tronco (cm)",
       y = "Frecuencia") +
  theme_bw()

# Histograma con 30 bins
histograma_30_bins <- ggplot(train_data, aes(x = circ_tronco_cm)) +
  geom_histogram(bins = 30, fill = "green", color = "black", alpha = 0.7) +
  labs(title = "Histograma de circ_tronco_cm con 30 Bins",
       x = "Circunferencia del Tronco (cm)",
       y = "Frecuencia") +
  theme_bw()

# Histograma con 50 bins
histograma_50_bins <- ggplot(train_data, aes(x = circ_tronco_cm)) +
  geom_histogram(bins = 50, fill = "red", color = "black", alpha = 0.7) +
  labs(title = "Histograma de circ_tronco_cm con 50 Bins",
       x = "Circunferencia del Tronco (cm)",
       y = "Frecuencia") +
  theme_bw()

# Histograma con 150 bins
histograma_150_bins <- ggplot(train_data, aes(x = circ_tronco_cm)) +
  geom_histogram(bins = 150, fill = "red", color = "black", alpha = 0.7) +
  labs(title = "Histograma de circ_tronco_cm con 50 Bins",
       x = "Circunferencia del Tronco (cm)",
       y = "Frecuencia") +
  theme_bw()

print(histograma_10_bins)
print(histograma_30_bins)
print(histograma_50_bins)
print(histograma_150_bins)

# Guardar los gráficos
ggsave("histograma_10_bins.png", plot = histograma_10_bins, width = 8, height = 6, dpi = 300)
ggsave("histograma_30_bins.png", plot = histograma_30_bins, width = 10, height = 6, dpi = 300)
ggsave("histograma_50_bins.png", plot = histograma_50_bins, width = 12, height = 6, dpi = 300)
ggsave("histograma_150_bins.png", plot = histograma_50_bins, width = 12, height = 6, dpi = 300)

#------------------------------------------------------------------
#---c) Repetir el punto b) pero separando por la clase de la variable inclinación_peligrosa?
# Crear el histograma de circ_tronco_cm separado por inclinacion_peligrosa, bin50
ggplot(train_data, aes(x = circ_tronco_cm, fill = factor(inclinacion_peligrosa))) +
  geom_histogram(bins = 50, alpha = 0.8, position = "identity", color = "black") + # Ajusta el número de bins si es necesario
  labs(title = "Histograma de Circunferencia de Tronco Separado por Inclinación Peligrosa",
       x = "Circunferencia del Tronco (cm)",
       y = "Frecuencia") +
  facet_wrap(~inclinacion_peligrosa, scales = "free_y", ncol = 1, 
             labeller = labeller(inclinacion_peligrosa = c("0" = "Inclinación No Peligrosa", "1" = "Inclinación Peligrosa"))) + 
  theme_bw() +
  scale_fill_manual(values = c("blue", "red")) + 
  scale_x_continuous(breaks = seq(min(train_data$circ_tronco_cm), max(train_data$circ_tronco_cm), by = 50)) +
  ggsave("histogramas_inclinacion_peligrosa.png", width = 8, height = 6, dpi = 300)

#------------------------------------------------------------------
