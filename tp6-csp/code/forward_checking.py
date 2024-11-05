import random
from backtracking import calc_heu
from escenario import *

def es_seguro(colocaciones, fila, columna):
    for f in range(fila):
        c = colocaciones[f]
        if c == columna or abs(f - fila) == abs(c - columna):
            return False
    return True

def obtener_dominios(colocaciones, fila, n):
    dominio = []
    for columna in range(n):
        if es_seguro(colocaciones, fila, columna):
            dominio.append(columna)
    return dominio

def forward_checking(colocaciones, fila, n, contador):
    if fila == n:
        return True

    # Obtener dominios para la fila actual
    dominios_fila = obtener_dominios(colocaciones, fila, n)
    
    for columna in dominios_fila:
        contador[0] += 1  # Incrementar contador al evaluar una posición
        colocaciones[fila] = columna
        
        if forward_checking(colocaciones, fila + 1, n, contador):
            return True
        
        colocaciones[fila] = -1
    
    return False

def resolver_reinas_f(n):
    colocaciones = [-1] * n  # Inicializar un escenario sin reinas
    contador = [0]  # Contador para estados visitados
    if forward_checking(colocaciones, 0, n, contador):
        return colocaciones, calc_heu(colocaciones), contador[0]  # Devolver también el número de estados visitados
    else:
        return None, contador[0]  # Devolver el número de estados visitados aunque no haya solución



for i in range (0, 10):
    print(resolver_reinas_f(4))


