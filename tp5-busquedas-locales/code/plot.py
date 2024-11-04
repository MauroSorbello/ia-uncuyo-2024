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
from genetic import genetics  # Importar el algoritmo genético

def plot_all_scenarios_variation(scenarios_with_heuristics, algorithm_name):
    plt.figure(figsize=(15, 8))
    heuristics = [h for _, h in scenarios_with_heuristics]
    plt.scatter(range(1, len(heuristics) + 1), heuristics, color='b', alpha=0.7)

    plt.title(f"Heuristic Variation for All Scenarios - {algorithm_name}")
    plt.ylabel("H()")
    plt.xlabel("Iterations")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.savefig(f"{algorithm_name}_all_scenarios_variation.png")
    plt.show()

def plot_optimal_solution_percentage(optimal_counts):
    num_queens_list = list(optimal_counts.keys())
    algorithms = ['Hill Climb', 'Simulated Annealing', 'Genetic']
    
    plt.figure(figsize=(12, 6))
    
    for i, num_queens in enumerate(num_queens_list):
        percentages = [
            optimal_counts[num_queens][alg] / 30 * 100 if alg != "Genetic" else optimal_counts[num_queens][alg] * 100 
            for alg in algorithms
        ]  # Calcula el porcentaje # Calcula el porcentaje
        plt.subplot(1, len(num_queens_list), i + 1)  # Crea un subplot para cada cantidad de reinas
        plt.bar(algorithms, percentages, color='b', alpha=0.7)
        plt.title(f"Optimal Solution Percentages for {num_queens} Queens")
        plt.ylabel("Percentage of Optimal Solutions")
        plt.ylim(0, 100)
        plt.grid(axis='y', linestyle='--', linewidth=0.5)

    plt.tight_layout()
    plt.savefig("optimal_solution_percentage_bar_plots.png")
    plt.show()

def run_experiments(num_queens_list, iterations, temp_initial, cooling_rate, output_file):
    headers = ["Algorithm", "Queens", "Seed", "Final Heuristic", "Iterations", "Execution Time"]
    optimal_counts = {nq: { "Hill Climb": 0, "Simulated Annealing": 0, "Genetic": 0 } for nq in num_queens_list}  # Contador de soluciones óptimas por cantidad de reinas

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
                if final_heu == 0:  # Consideramos 0 como solución óptima
                    optimal_counts[num_queens]["Hill Climb"] += 1

                # Simulated Annealing
                current = esc(num_queens, seed)
                start_time = time.time()
                final_solution, final_heu, num_iterations, _ = simulate_annealing(current, iterations, temp_initial, cooling_rate)
                end_time = time.time()
                execution_time = end_time - start_time
                writer.writerow(["Simulated Annealing", num_queens, seed, final_heu, num_iterations, execution_time])
                if final_heu == 0:  # Consideramos 0 como solución óptima
                    optimal_counts[num_queens]["Simulated Annealing"] += 1

            # Generar 30 escenarios para el algoritmo genético
            escenarios = [esc(num_queens, s) for s in range(30)]

            # Genetic Algorithm
            start_time = time.time()
            final_solution, num_iterations, scenarios_with_heuristics = genetics(escenarios, iterations)
            final_heu = final_solution[1]
            end_time = time.time()
            execution_time = end_time - start_time
            writer.writerow(["Genetic Algorithm", num_queens, "N/A", final_heu, num_iterations, execution_time])  # Semilla como "N/A"
            plot_all_scenarios_variation(scenarios_with_heuristics, f"Genetic Algorithm {num_queens} reinas")
            if final_heu == 0:  # Consideramos 0 como solución óptima
                optimal_counts[num_queens]["Genetic"] += 1

    print(f"Results saved to {output_file}")

    # Graficar porcentajes de soluciones óptimas
    plot_optimal_solution_percentage(optimal_counts)

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
    if algorithm_name == "Hill Climb":
        plt.figure(figsize=(15, 8))
    else:
        plt.figure(figsize=(10, 6))
    x_values = range(len(heuristic_values))

    # Dibujar los puntos con un tamaño más pequeño
    plt.scatter(x_values, heuristic_values, c='b', marker='o', s=10)  
    plt.title(f"Heuristic Function Variation - {algorithm_name}")
    plt.ylabel("H()")
    plt.xlabel("Iteration")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig(f"{algorithm_name}_heuristic_variation.png")
    plt.show()

def main():
    num_queens_list = [4, 8, 10]
    iterations = 1000
    temp_initial = 1000
    cooling_rate = 0.95
    output_file = "tp5-Nreinas.csv"

    # Ejecutar experimentos
    run_experiments(num_queens_list, iterations, temp_initial, cooling_rate, output_file)

    # Generar boxplots
    create_boxplots(output_file)

    # Ejecución específica para graficar la variación de H
    current = esc(8, 5)  # Escenario con 8 reinas y semilla 5
    _, _, _, hill_climb_heuristics = hill_climb(current, iterations)
    plot_heuristic_variation(hill_climb_heuristics, "Hill Climb")

    current = esc(8, 5)
    _, _, _, annealing_heuristics = simulate_annealing(current, iterations, temp_initial, cooling_rate)
    plot_heuristic_variation(annealing_heuristics, "Simulated Annealing")

# Ejecutar la función principal
main()
