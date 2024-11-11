import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo de entrenamiento
train_data = pd.read_csv('arbolado-mendoza-dataset-train.csv')


print("Distribución de la clase 'inclinacion_peligrosa':")
print(train_data['inclinacion_peligrosa'].value_counts(normalize=True) * 100)

# Graficar la distribución de `inclinacion_peligrosa`
sns.countplot(data=train_data, x='inclinacion_peligrosa')
plt.title('Distribución de la clase inclinacion_peligrosa')
plt.xlabel('Inclinación peligrosa')
plt.ylabel('Frecuencia')
plt.show()


seccion_peligrosa = train_data.groupby('seccion')['inclinacion_peligrosa'].value_counts(normalize=True).unstack()
print("\nPorcentaje de inclinaciones peligrosas por sección:")
print(seccion_peligrosa)

# Graficar la relación entre sección e inclinación peligrosa
sns.countplot(data=train_data, x='seccion', hue='inclinacion_peligrosa')
plt.title('Relación entre Sección e Inclinación Peligrosa')
plt.xlabel('Sección')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.legend(title='Inclinación peligrosa')
plt.show()


especie_peligrosa = train_data.groupby('especie')['inclinacion_peligrosa'].value_counts(normalize=True).unstack()
print("\nPorcentaje de inclinaciones peligrosas por especie:")
print(especie_peligrosa)

# Graficar la relación entre especie e inclinación peligrosa (mostrar solo las especies más comunes)
top_especies = train_data['especie'].value_counts().index[:10]  # Seleccionar las 10 especies más comunes
sns.countplot(data=train_data[train_data['especie'].isin(top_especies)], x='especie', hue='inclinacion_peligrosa')
plt.title('Relación entre Especie e Inclinación Peligrosa (Top 10 Especies)')
plt.xlabel('Especie')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.legend(title='Inclinación peligrosa')
plt.show()
