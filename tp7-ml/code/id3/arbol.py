import pandas as pd
import numpy as np

# Método para calcular el valor mayoritario
def Valor_mayoria(ejemplos, class_name):
    return ejemplos[class_name].mode()[0]  # Devuelve el valor más frecuente en la clase

# Método para calcular la entropía de un conjunto de datos
def calcular_entropia(ejemplos, class_name):
    frecuencia = ejemplos[class_name].value_counts(normalize=True)
    entropia = -sum(frecuencia * np.log2(frecuencia))
    return entropia

# Método para elegir el mejor atributo usando la ganancia de información
def Elegir_atributo(atribs, ejemplos, class_name):
    entropia_inicial = calcular_entropia(ejemplos, class_name)
    mejor_ganancia = -1
    mejor_atributo = None

    for atributo in atribs:
        # Calcula la entropía condicional para cada valor del atributo
        entropia_atributo = 0
        for valor in ejemplos[atributo].unique():
            subset = ejemplos[ejemplos[atributo] == valor]
            probabilidad = len(subset) / len(ejemplos)
            entropia_atributo += probabilidad * calcular_entropia(subset, class_name)

        # Calcula la ganancia de información
        ganancia = entropia_inicial - entropia_atributo

        if ganancia > mejor_ganancia:
            mejor_ganancia = ganancia
            mejor_atributo = atributo

    return mejor_atributo


def Aprendizaje_arbol_decision(ejemplos, atribs, default, class_name):
    if len(ejemplos) == 0:
        return default
    elif len(ejemplos[class_name].unique()) == 1:
        return ejemplos[class_name].iloc[0]
    elif len(atribs) == 0:
        return Valor_mayoria(ejemplos, class_name)
    else:
        mejor = Elegir_atributo(atribs, ejemplos, class_name)
        arbol = {mejor: {}}
        m = Valor_mayoria(ejemplos, class_name)
        for value in ejemplos[mejor].unique():
            subset = ejemplos[ejemplos[mejor] == value]
            subArbol = Aprendizaje_arbol_decision(subset, atribs.drop([mejor]), m, class_name)
            arbol[mejor][value] = subArbol
        return arbol

# Cargar los datos desde el archivo CSV
# Asegúrate de reemplazar esta ruta con la ruta correcta donde esté guardado "tennis.csv"
ejemplos = pd.read_csv("C:/Users/Martinotebook/Documents/nacho (podes borrar tranqui)/2° año/Paradigmas/lab/ia-uncuyo-2024/tp7-ml/data/tennis.csv")


# Lista de atributos (excluyendo la clase objetivo)
atribs = ejemplos.columns.drop("play")

# Llamar a la función de aprendizaje del árbol de decisión
arbol = Aprendizaje_arbol_decision(ejemplos, atribs, Valor_mayoria(ejemplos, "play"), "play")

# Mostrar el árbol de decisión generado
print(arbol)
