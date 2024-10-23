
dataset <- read.csv("FACULTAD/3 AÑO/Inteligencia Artificial 1/ia-uncuyo-2024/tp7/arbolado-mendoza.csv")


set.seed(123)  
n <- nrow(dataset)
validation_size <- floor(0.20 * n)
validation_indices <- sample(seq_len(n), size = validation_size)


validation_set <- dataset[validation_indices, ]
train_set <- dataset[-validation_indices, ]


write.csv(validation_set, "FACULTAD/3 AÑO/Inteligencia Artificial 1/ia-uncuyo-2024/tp7/arbolado-mendoza-dataset-validation.csv", row.names = FALSE)
write.csv(train_set, "FACULTAD/3 AÑO/Inteligencia Artificial 1/ia-uncuyo-2024/tp7/arbolado-mendoza-dataset-train.csv", row.names = FALSE)

