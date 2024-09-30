import csv
import time
import random
import math
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
from escenario import *

from hill_climb import hill_climb
from simulate_annealing import simulate_annealing
# Funciones previas (esc, calc_heu, generate_neighbor, hill_climb, simulate_annealing) aquí

# Función para ejecutar múltiples veces y guardar resultados
def run_experiments(num_queens_list, iterations, temp_initial, cooling_rate, output_file):
    headers = ["Algorithm", "Queens", "Seed", "Final Heuristic", "Iterations", "Execution Time"]
    
    # Crear o sobrescribir archivo CSV
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        for num_queens in num_queens_list:
            for seed in range(30):
                current = esc(num_queens, seed)
                
                # Hill Climbing
                start_time = time.time()
                final_solution, final_heu, num_iterations, _ = hill_climb(current, iterations)
                end_time = time.time()
                execution_time = end_time - start_time
                writer.writerow(["Hill Climb", num_queens, seed, final_heu, num_iterations, execution_time])
                
                # Simulated Annealing
                current = esc(num_queens, seed)
                start_time = time.time()
                final_solution, final_heu, num_iterations, _ = simulate_annealing(current, iterations, temp_initial, cooling_rate)
                end_time = time.time()
                execution_time = end_time - start_time
                writer.writerow(["Simulated Annealing", num_queens, seed, final_heu, num_iterations, execution_time])

    print(f"Results saved to {output_file}")

# Función para crear gráficos boxplot de tiempos de ejecución y estados previos
def create_boxplots(csv_file):
    data = {"Algorithm": [], "Execution Time": [], "Iterations": []}
    
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data["Algorithm"].append(row["Algorithm"])
            data["Execution Time"].append(float(row["Execution Time"]))
            data["Iterations"].append(int(row["Iterations"]))
    
    # Crear boxplot para los tiempos de ejecución
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Algorithm", y="Execution Time", data=data)
    plt.title("Execution Time Distribution by Algorithm")
    plt.ylabel("Execution Time (s)")
    plt.xlabel("Algorithm")
    plt.savefig("execution_time_boxplot.png")
    plt.show()

    # Crear boxplot para la cantidad de iteraciones
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Algorithm", y="Iterations", data=data)
    plt.title("Iterations Distribution by Algorithm")
    plt.ylabel("Iterations")
    plt.xlabel("Algorithm")
    plt.savefig("iterations_boxplot.png")
    plt.show()

# Función para graficar la variación de la función H
def plot_heuristic_variation(heuristic_values, algorithm_name):
    plt.figure(figsize=(10, 6))
    plt.plot(heuristic_values)
    plt.title(f"Heuristic Function Variation - {algorithm_name}")
    plt.ylabel("H()")
    plt.xlabel("Iteration")
    plt.savefig(f"{algorithm_name}_heuristic_variation.png")
    plt.show()

def main():
    num_queens_list = [4, 8, 10]
    iterations = 1000
    temp_initial = 1000
    cooling_rate = 0.95
    output_file = "nqueens_results.csv"

    # Ejecutar experimentos
    run_experiments(num_queens_list, iterations, temp_initial, cooling_rate, output_file)

    # Generar boxplots
    create_boxplots(output_file)

    # Ejecución específica para graficar la variación de H
    current = esc(8, 1)  # Escenario con 8 reinas y semilla 1
    _, _, _, hill_climb_heuristics = hill_climb(current, iterations)
    plot_heuristic_variation(hill_climb_heuristics, "Hill Climb")

    current = esc(8, 1)
    _, _, _, annealing_heuristics = simulate_annealing(current, iterations, temp_initial, cooling_rate)
    plot_heuristic_variation(annealing_heuristics, "Simulated Annealing")

# Ejecutar la función principal
main()