import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo de entrenamiento
train_data = pd.read_csv('arbolado-mendoza-dataset-train.csv')

# b) Histograma de frecuencia para la variable `circ_tronco_cm` con diferentes números de bins
plt.figure(figsize=(12, 6))
train_data['circ_tronco_cm'].plot(kind='hist', bins=20, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Histograma de circ_tronco_cm (20 bins)')
plt.xlabel('circ_tronco_cm')
plt.ylabel('Frecuencia')
plt.savefig('histograma_circ_tronco_cm_20_bins.png')  # Guardar la gráfica
plt.close()

plt.figure(figsize=(12, 6))
train_data['circ_tronco_cm'].plot(kind='hist', bins=50, alpha=0.7, color='orange', edgecolor='black')
plt.title('Histograma de circ_tronco_cm (50 bins)')
plt.xlabel('circ_tronco_cm')
plt.ylabel('Frecuencia')
plt.savefig('histograma_circ_tronco_cm_50_bins.png')  # Guardar la gráfica
plt.close()

# c) Histograma de `circ_tronco_cm` separado por `inclinacion_peligrosa`
plt.figure(figsize=(12, 6))
sns.histplot(data=train_data, x='circ_tronco_cm', hue='inclinacion_peligrosa', bins=20, kde=False, edgecolor='black')
plt.title('Histograma de circ_tronco_cm separado por inclinacion_peligrosa')
plt.xlabel('circ_tronco_cm')
plt.ylabel('Frecuencia')
plt.savefig('histograma_circ_tronco_cm_inclinacion_peligrosa.png')  # Guardar la gráfica
plt.close()

# d) Crear una nueva variable categórica `circ_tronco_cm_cat` basada en circ_tronco_cm

# Usar los percentiles de circ_tronco_cm para definir los puntos de corte
q1 = train_data['circ_tronco_cm'].quantile(0.25)
q2 = train_data['circ_tronco_cm'].quantile(0.5)
q3 = train_data['circ_tronco_cm'].quantile(0.75)

# Crear la nueva variable categórica
train_data['circ_tronco_cm_cat'] = pd.cut(
    train_data['circ_tronco_cm'],
    bins=[-float('inf'), q1, q2, q3, float('inf')],
    labels=['bajo', 'medio', 'alto', 'muy alto']
)

# Guardar el nuevo DataFrame con la variable categórica en un archivo CSV
train_data.to_csv('arbolado-mendoza-dataset-circ_tronco_cm-train.csv', index=False)

print("Archivo con la nueva variable 'circ_tronco_cm_cat' guardado correctamente.")
print("Las gráficas han sido guardadas en la carpeta 'data'.")

