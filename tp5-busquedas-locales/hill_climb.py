# 1) Estado inicial: Generas una configuración aleatoria de las n reinas. 
# Asegúrate de que haya una sola reina por columna.
# 2) Evaluar el estado: Mides cuántas reinas están en conflicto entre sí. 
# Dos reinas están en conflicto si están en la misma fila o en una diagonal.
# 3) Búsqueda local: Examina los vecinos del estado actual. 
# Un vecino es una configuración donde una sola reina cambia de fila en su columna.
# 4) Seleccionar el mejor vecino: Evalúa los vecinos según cuántos conflictos tienen y 
# selecciona el vecino que tenga menos conflictos. 
# Si uno de ellos tiene menos conflictos que el estado actual, lo adoptas como nuevo estado.
# 5)Iterar: Repite el proceso de búsqueda y actualización hasta que llegues a una configuración 
# sin conflictos (solución óptima) o hasta que no encuentres un vecino mejor que el actual 
# (máximo local).
# 6) Detenerse: Si alcanzas un máximo local (ningún vecino es mejor), puedes reiniciar con una 
# nueva configuración aleatoria para intentar salir del máximo local.

import random
def hill_climb(num_queens):
    # Conf aleatoria
    # Si n = 5, esc = [1,3,2,4,0] es lo mismo que [-,x,-,-,-; -,-,3,-,-;-,2,-,-,-;-,-,-,-,x;x,-,-,-,-]
    esc = []
    for i in range (0, num_queens):
        check = False
        while not check:
            pos = random.randint(0,num_queens - 1)
            if (pos not in esc):
                esc[i] = pos
                check = True
        
