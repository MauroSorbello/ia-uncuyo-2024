import pandas as pd

# Cargar el conjunto de datos
data = pd.read_csv('../../data/arbolado-mza-dataset.csv')

# Dividir el conjunto de datos en 80% entrenamiento y 20% validación
train_data = data.sample(frac=0.8, random_state=42)  # 80% de los datos
validation_data = data.drop(train_data.index)         # el 20% restante

# Guardar los conjuntos de datos en nuevos archivos CSV
train_data.to_csv('arbolado-mendoza-dataset-train.csv', index=False)
validation_data.to_csv('arbolado-mendoza-dataset-validation.csv', index=False)

print("Los archivos se han creado correctamente.")


