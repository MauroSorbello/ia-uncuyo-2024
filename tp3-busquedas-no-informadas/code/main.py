import time
import numpy as np
import matplotlib.pyplot as plt
import copy
import csv
from statistics import mean, stdev
from generate_random_map_custom import generate_random_map_custom
from busquedas import bfs, dfs, dls, a_star, uniform_cost, aleatorio

# Configuración de la simulación
n_experiments = 30
map_size = 100
hole_prob = 0.08
slippery = False
def calc_cost(actions):
    move_cost = 0
    for act in actions:
            # Asignar un costo diferente basado en la dirección (act)
        if act == 0:  # Arriba
            move_cost += 2
        elif act == 1:  # Abajo
            move_cost += 1
        elif act == 2:  # Izquierda
            move_cost += 3
        elif act == 3:  # Derecha
            move_cost += 1
    return move_cost
# Resultados de cada algoritmo
results = {
    'bfs': {'explored': [], 'cost_e1': [], 'cost_e2': [], 'time': [], 'solution_found': []},
    'dfs': {'explored': [], 'cost_e1': [], 'cost_e2': [], 'time': [], 'solution_found': []},
    'dls': {'explored': [], 'cost_e1': [], 'cost_e2': [], 'time': [], 'solution_found': []},
    'uniform_cost_e1': {'explored': [], 'cost_e1': [], 'time': [], 'solution_found': []},
    'uniform_cost_e2': {'explored': [], 'cost_e2': [], 'time': [], 'solution_found': []},
    'a_star': {'explored': [], 'cost_e1': [], 'cost_e2': [], 'time': [], 'solution_found': []},
    'a_star_e2': {'explored': [], 'cost_e1': [], 'cost_e2': [], 'time': [], 'solution_found': []},
    'aleat': {'explored': [], 'cost_e1': [], 'cost_e2': [], 'time': [], 'solution_found': []},
}

# Guardar los resultados en un archivo CSV
with open('no-informada-results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["algorithm_name", "env_n", "states_n", "cost_e1", "cost_e2", "time", "solution_found"])

    # Ejecutar los experimentos
    for i in range(n_experiments):
        print(f"Experimento {i+1} / {n_experiments}")
        
        # Generar un nuevo entorno aleatorio de 100x100
        env, desc = generate_random_map_custom(map_size, hole_prob, seed=i, slippery=slippery)

        # Crear copias del entorno antes de ejecutar cada algoritmo
        env_bfs = copy.deepcopy(env)
        env_dfs = copy.deepcopy(env)
        env_dls = copy.deepcopy(env)
        env_uniform_cost_e1 = copy.deepcopy(env)
        env_uniform_cost_e2 = copy.deepcopy(env)
        env_a_star_e1 = copy.deepcopy(env)
        env_a_star_e2 = copy.deepcopy(env)
        env_aleat = copy.deepcopy(env)

        # Ejecutar BFS
        start_time = time.time()
        result_bfs = bfs(env_bfs)
        end_time = time.time()
        solution_found = result_bfs is not None
        states_explored = len(result_bfs[1]) if solution_found else 0
        cost_e1 = len(result_bfs[1]) if solution_found else 0
        cost_e2 = calc_cost(result_bfs[2]) if solution_found else 0
        results['bfs']['explored'].append(states_explored)
        results['bfs']['cost_e1'].append(cost_e1)
        results['bfs']['cost_e2'].append(cost_e2)
        results['bfs']['time'].append(end_time - start_time)
        results['bfs']['solution_found'].append(solution_found)
        writer.writerow(["BFS", i + 1, states_explored, cost_e1, cost_e2, end_time - start_time, solution_found])

        # Ejecutar DFS
        start_time = time.time()
        result_dfs = dfs(env_dfs)
        end_time = time.time()
        solution_found = result_dfs is not None
        states_explored = len(result_dfs[1]) if solution_found else 0
        cost_e1 = len(result_dfs[1]) if solution_found else 0
        cost_e2 = calc_cost(result_dfs[2]) if solution_found else 0
        results['dfs']['explored'].append(states_explored)
        results['dfs']['cost_e1'].append(cost_e1)
        results['dfs']['cost_e2'].append(cost_e2)
        results['dfs']['time'].append(end_time - start_time)
        results['dfs']['solution_found'].append(solution_found)
        writer.writerow(["DFS", i + 1, states_explored, cost_e1, cost_e2, end_time - start_time, solution_found])

        # Ejecutar DLS
        start_time = time.time()
        result_dls = dls(env_dls, 10)  # Limit 10
        end_time = time.time()
        solution_found = result_dls is not None
        states_explored = len(result_dls[1]) if solution_found else 0
        cost_e1 = len(result_dls[1]) if solution_found else 0
        cost_e2 = 0  # Si solo se está usando un costo en DLS
        results['dls']['explored'].append(states_explored)
        results['dls']['cost_e1'].append(cost_e1)
        results['dls']['cost_e2'].append(cost_e2)
        results['dls']['time'].append(end_time - start_time)
        results['dls']['solution_found'].append(solution_found)
        writer.writerow(["DLS", i + 1, states_explored, cost_e1, cost_e2, end_time - start_time, solution_found])

        # Ejecutar Uniform Cost (escenario 1)
        
        start_time = time.time()
        result_uc_e1 = uniform_cost(env_uniform_cost_e1, cost=0)
        end_time = time.time()
        solution_found = result_uc_e1 is not None
        states_explored = len(result_uc_e1[1]) if solution_found else 0
        cost_e1 = result_uc_e1[2] if solution_found else 0
        cost_e2 = 0  # Lo ajustaremos en el segundo escenario
        results['uniform_cost_e1']['explored'].append(states_explored)
        results['uniform_cost_e1']['cost_e1'].append(cost_e1)
        results['uniform_cost_e1']['time'].append(end_time - start_time)
        results['uniform_cost_e1']['solution_found'].append(solution_found)
        writer.writerow(["UCS e1", i + 1, states_explored, cost_e1, cost_e2, end_time - start_time, solution_found])

        # Ejecutar Uniform Cost (escenario 2)
        print("-----------------------------------------------")
        start_time = time.time()
        result_uc_e2 = uniform_cost(env_uniform_cost_e2, cost=2) 
        end_time = time.time()
        solution_found = result_uc_e2 is not None
        states_explored = len(result_uc_e2[1]) if solution_found else 0
        cost_e1 = 0  # Se ajustó en el primer escenario
        cost_e2 = result_uc_e2[2] if solution_found else 0
        results['uniform_cost_e2']['explored'].append(states_explored)
        results['uniform_cost_e2']['cost_e2'].append(cost_e2)
        results['uniform_cost_e2']['time'].append(end_time - start_time)
        results['uniform_cost_e2']['solution_found'].append(solution_found)
        writer.writerow(["UCS e2", i + 1, states_explored, cost_e1, cost_e2, end_time - start_time, solution_found])

        # Ejecutar A*
        start_time = time.time()
        result_a_star = a_star(env_a_star_e1, cost=0)
        end_time = time.time()
        solution_found = result_a_star is not None
        states_explored = len(result_a_star[1]) if solution_found else 0
        cost_e1 = len(result_a_star[1]) if solution_found else 0
        cost_e2 = 0   # Si solo se está usando un costo en A*
        results['a_star']['explored'].append(states_explored)
        results['a_star']['cost_e1'].append(cost_e1)
        results['a_star']['cost_e2'].append(cost_e2)
        results['a_star']['time'].append(end_time - start_time)
        results['a_star']['solution_found'].append(solution_found)
        writer.writerow(["A*_e1", i + 1, states_explored, cost_e1, cost_e2, end_time - start_time, solution_found])

        # Ejecutar A env2*
        start_time = time.time()
        result_a_star2 = a_star(env_a_star_e1, cost=2)
        end_time = time.time()
        solution_found = result_a_star2 is not None
        states_explored = len(result_a_star2[1]) if solution_found else 0
        cost_e2 = result_a_star2[2] if solution_found else 0
        cost_e1 = 0   # Si solo se está usando un costo en A*
        results['a_star_e2']['explored'].append(states_explored)
        results['a_star_e2']['cost_e1'].append(cost_e1)
        results['a_star_e2']['cost_e2'].append(cost_e2)
        results['a_star_e2']['time'].append(end_time - start_time)
        results['a_star_e2']['solution_found'].append(solution_found)
        writer.writerow(["A*_e2", i + 1, states_explored, cost_e1, cost_e2, end_time - start_time, solution_found])

        # Ejecutar aleatorio*
        start_time = time.time()
        result_aleat = aleatorio(env_aleat)
        end_time = time.time()
        solution_found = result_aleat is not None
        states_explored = len(result_aleat[1]) if solution_found else 0
        cost_e1 = result_aleat[2] if solution_found else 0
        cost_e2 = 0   # Si solo se está usando un costo en A*
        results['aleat']['explored'].append(states_explored)
        results['aleat']['cost_e1'].append(cost_e1)
        results['aleat']['cost_e2'].append(cost_e2)
        results['aleat']['time'].append(end_time - start_time)
        results['aleat']['solution_found'].append(solution_found)
        writer.writerow(["aleatorio", i + 1, states_explored, cost_e1, cost_e2, end_time - start_time, solution_found])

# Calcular estadísticas (media y desviación estándar)
for alg in results:
    print(f"Resultados para {alg}:")
    if alg != "uniform_cost_e2":
        metricas = ['explored', 'cost_e1', 'time']
    else:
        metricas = ['explored', 'cost_e2', 'time']
    for metric in metricas:
        if results[alg][metric]:

            mean_val = mean(results[alg][metric])
            stdev_val = stdev(results[alg][metric])
            print(f"  {metric.capitalize()}: Media = {mean_val:.2f}, Desviación Estándar = {stdev_val:.2f}")

# Gráficos de caja y bigotes (boxplots)
fig, ax = plt.subplots(figsize=(6, 6))

# Gráfico para estados explorados
ax.boxplot([results['bfs']['explored'], results['dfs']['explored'], results['dls']['explored'],
                results['uniform_cost_e1']['explored'], results['a_star']['explored'], results['aleat']['explored']])
ax.set_title('Estados Explorados (Escenario 1 y 2)')
ax.set_xticklabels(['BFS', 'DFS', 'DLS', 'UCS e1', 'A*',  'ALEATORIO'])

plt.savefig("estados_explorados.png")

fig, ax = plt.subplots(figsize=(6, 6))
# Gráfico para costo total (escenario 1 )
ax.boxplot([results['bfs']['cost_e1'], results['dfs']['cost_e1'], results['dls']['cost_e1'],
                results['uniform_cost_e1']['cost_e1'], results['a_star']['cost_e1'], results['aleat']['cost_e1']])
ax.set_title('Costo Total (Escenario 1)')
ax.set_xticklabels(['BFS', 'DFS', 'DLS', 'UCS e1', 'A* e1', 'ALEATORIO'])

plt.savefig("costo_total_e1.png")

fig, ax = plt.subplots(figsize=(6, 6))
# Gráfico para costo total (escenario2)
ax.boxplot([results['bfs']['cost_e2'], results['dfs']['cost_e2'], results['dls']['cost_e1'],
                results['uniform_cost_e2']['cost_e2'], results['a_star_e2']['cost_e2']])
ax.set_title('Costo Total (Escenario 2)')
ax.set_xticklabels(['BFS e2', 'DFS e2', 'DLS','UCS e2', 'A* e2'])

plt.savefig("costo_total_e2.png")

fig, ax = plt.subplots(figsize=(6, 6))
# Gráfico para tiempo empleado
ax.boxplot([results['bfs']['time'], results['dfs']['time'],
                results['uniform_cost_e2']['time'], results['a_star_e2']['time']])
ax.set_title('Tiempo Empleado (Escenario 2)')
ax.set_xticklabels(['BFS e2', 'DFS e2', 'UCS e2', 'A* e2', ])

plt.savefig("tiempo_empleado_e2.png")

# Gráficos de caja y bigotes (boxplots)
fig, ax = plt.subplots(figsize=(6, 6))

# Gráfico para estados explorados sin dfs
ax.boxplot([results['bfs']['explored'],  results['dls']['explored'],
                results['uniform_cost_e1']['explored'], results['a_star']['explored'], results['aleat']['explored']])
ax.set_title('Estados Explorados sin DFS')
ax.set_xticklabels(['BFS', 'DLS', 'UCS e1', 'A*',  'ALEATORIO'])

plt.savefig("estados_explorados_sin_DFS.png")

fig, ax = plt.subplots(figsize=(6, 6))
# Gráfico para costo total (escenario 1 y 2)
ax.boxplot([results['bfs']['cost_e1'], results['bfs']['cost_e2'], results['uniform_cost_e1']['cost_e1'], results['uniform_cost_e2']['cost_e2'], results['a_star']['cost_e1'], results['a_star_e2']['cost_e2']])
ax.set_title('Costo Total (Escenario 1 y 2) BFS UCS A*' )
ax.set_xticklabels(['BFS e1', 'BFS e2', 'UCS e1', 'UCS e2', 'A* e1', 'A* e2'])

plt.savefig("costo_total_BFS_UCS_A.png")