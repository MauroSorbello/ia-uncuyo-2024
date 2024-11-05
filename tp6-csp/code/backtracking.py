import random
from escenario import *

def calc_heu(current):
    h = 0
    size = len(current)
    for i in range(size):
        for j in range(i + 1, size):
            if current[i] == current[j] or abs(current[i] - current[j]) == abs(i - j):
                h += 1
    return h

def esSeguro(esc, fila, columna):
    for i in range(fila):
        if esc[i] == columna or abs(fila - i) == abs(columna - esc[i]):
            return False
    return True

def colocarReina(esc, fila, contador):
    if fila >= len(esc):
        return True  

    for columna in range(len(esc)):
        contador[0] += 1  # Incrementar contador al evaluar una posición
        if esSeguro(esc, fila, columna):
            esc[fila] = columna
            if colocarReina(esc, fila + 1, contador):  
                return True
            esc[fila] = -1  # Deshacer el movimiento
    return False 

def resolverReinas(n):
    esc = [-1] * n  # Inicializar un escenario sin reinas
    contador = [0]  # Contador para estados visitados
    if colocarReina(esc, 0, contador):
        return esc, calc_heu(esc), contador[0]  # Devolver también el número de estados visitados
    else:
        return False, contador[0]  # Devolver el número de estados visitados aunque no haya solución

    
for i in range (0, 10):
    print(resolverReinas(4))


