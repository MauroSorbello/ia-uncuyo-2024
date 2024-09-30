import random
import math

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
    for i in range(size):
        for j in range(i + 1, size):
            if current[i] == current[j] or abs(current[i] - current[j]) == abs(i - j):
                h += 1
    return h


def generate_neighbor(current):
    neighbour = current.copy()
    i = random.randint(0, len(current) - 1)
    j = random.randint(0, len(current) - 1)
    check = False
    while not check:
        if j != current[i]:
            neighbour[i] = j
            check = True
        else:
            j = random.randint(0, len(current) - 1)
    return neighbour


def simulate_annealing(current, limit, temp_initial, cooling_rate):
    heuristic_values = []

    current_heu = calc_heu(current)

    temperature = temp_initial

    for t in range(1, limit + 1):
        heuristic_values.append(current_heu)
        neighbor = generate_neighbor(current)
        neighbor_heu = calc_heu(neighbor)

        # Si el vecino es mejor, lo aceptamos
        if neighbor_heu < current_heu:
            current = neighbor
            current_heu = neighbor_heu
        else:
            # Aceptar soluciones peores con probabilidad que depende de la temperatura
            acceptance = math.exp((current_heu - neighbor_heu) / temperature)
            if random.random() < acceptance:
                current = neighbor
                current_heu = neighbor_heu
        
        # Enfriar la temperatura de forma más lenta para permitir exploración
        temperature *= cooling_rate

        # Detener si se alcanza la solución óptima
        if current_heu == 0:
            break

    return current, current_heu, t, heuristic_values

def list_to_matrix(queen_positions):
    n = len(queen_positions)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for row in range(n):
        col = queen_positions[row]
        matrix[row][col] = 1  # Colocar la reina
    
    return matrix

# def test_simulated_annealing():
#     num_queens = 8
#     limit = 1000
#     temp_initial = 100  # Ajuste de temperatura inicial
#     cooling_rate = 0.995  # Más lenta para permitir más exploración

#     # Recocido simulado
#     solution, heuristic, iteracion = simulate_annealing(num_queens, limit, temp_initial, cooling_rate)
#     heuristic = calc_heu(solution)
#     matrix = list_to_matrix(solution)
#     # Imprimir la matriz
#     for row in matrix:
#         print(row)
#     print(f"Solución encontrada: {solution}")
#     print(f"Heurística de la solución: {heuristic}")
#     print(f"Cantidad de iteraciones: {iteracion}")
#     # assert heuristic == 0, f"La solución tiene conflictos: {finish_heu} conflictos encontrados."

# # Correr el test
# test_simulated_annealing()