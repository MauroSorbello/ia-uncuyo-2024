import random
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

def calc_heu(current):
    h = 0
    size = len(current)
    for i in range (0, size):
        for j in range (i + 1, size):
            # No deberia pasar pero lo dejo por las dudas (current[i] == current[j] )
            if (current[i] == current[j] or (abs(current[i] - current[j]) == abs(i-j))):
                h += 2
    return h
                
def generate_neighbor(current):
    neighbors = []
    len_curr = len(current)
    for i in range (0, len_curr):
        for j in range (0, len_curr):
            if current[i] != j:
                neighbor = current.copy()
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors
    
def best_neighbor(neighbors, current):
    current_heu = calc_heu(current)
    best = current
    best_heu = current_heu
    for neighbor in neighbors:
        neighbor_heu = calc_heu(neighbor)
        if neighbor_heu < best_heu:
            best = neighbor
            best_heu = neighbor_heu
    return best, best_heu 



def hill_climb(current, limit):
    # Conf aleatoria
    # Si n = 5, esc = [1,3,2,4,0] es lo mismo que [-,x,-,-,-; -,-,3,-,-;-,2,-,-,-;-,-,-,-,x;x,-,-,-,-]
    heuristic_values = []
    cost = []
    iterations = 0
    current_heu = calc_heu(current)

    for _ in range(limit):
        
        neighbors = generate_neighbor(current)
        next_solution, next_heu = best_neighbor(neighbors, current)

        heuristic_values.append(current_heu)
        if next_heu >= current_heu:
            break  # Se ha alcanzado un máximo local

        current = next_solution
        current_heu = next_heu
        cost.append(current_heu)
        iterations += 1

    return current, current_heu, iterations, heuristic_values
# Escenario de prueba


def list_to_matrix(queen_positions):
    n = len(queen_positions)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for row in range(n):
        col = queen_positions[row]
        matrix[row][col] = 1  # Colocar la reina
    
    return matrix

# def test_hill_climb(num_queens, limit):
#     solution, heuristic, iterations = hill_climb(num_queens, limit)
#     print(f"Solución encontrada: {solution}")
#     print(f"Conflictos: {heuristic}")
#     print(f"Iteraciones: {iterations}")
#     matrix = list_to_matrix(solution)
#     # Imprimir la matriz
#     for row in matrix:
#         print(row)

# # Parámetros de la prueba
# num_queens = 8 # Número de reinas
# limit = 10000  # Número máximo de iteraciones

# # Ejecutar la prueba
# test_hill_climb(num_queens, limit)

