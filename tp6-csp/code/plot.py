import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from backtracking import resolverReinas
from forward_checking import resolver_reinas_f

def run_experiment(num_queens, num_runs, algorithm):
    results = []
    optimal_solutions = 0
    total_time = []
    total_states = []

    for _ in range(num_runs):
        start_time = time.time()
        if algorithm == 'backtracking':
            solution, heu, states_visited = resolverReinas(num_queens)
        elif algorithm == 'forward_checking':
            solution, heu, states_visited = resolver_reinas_f(num_queens)
        end_time = time.time()

        execution_time = end_time - start_time
        total_time.append(execution_time)
        total_states.append(states_visited)

        if solution is not False and heu == 0:  # Check for optimal solution
            optimal_solutions += 1
        
        results.append((num_queens, execution_time, states_visited, solution is not False and heu == 0))

    return results, optimal_solutions, total_time, total_states

def save_results_to_csv(all_results, filename='tp6-Nreinas.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Algorithm', 'Num Queens', 'Execution Time', 'States Visited', 'Optimal Solution'])
        for algorithm, results in all_results.items():
            for result in results:
                writer.writerow([algorithm] + list(result))

def plot_results(data, algorithm):
    plt.figure(figsize=(12, 6))

    # Boxplot for execution time
    plt.subplot(1, 2, 1)
    plt.boxplot(data['execution_time'], labels=data['num_queens'])
    plt.title(f'Execution Time for {algorithm}')
    plt.xlabel('Number of Queens')
    plt.ylabel('Time (seconds)')

    # Boxplot for states visited
    plt.subplot(1, 2, 2)
    plt.boxplot(data['states_visited'], labels=data['num_queens'])
    plt.title(f'States Visited for {algorithm}')
    plt.xlabel('Number of Queens')
    plt.ylabel('States Visited')

    plt.tight_layout()
    plt.savefig(f'{algorithm}_boxplots.png')
    plt.show()

def main():
    num_runs = 30
    num_queens_cases = [4, 8, 10]
    algorithms = ['backtracking', 'forward_checking']

    all_results_csv = {algorithm: [] for algorithm in algorithms} 

    for algorithm in algorithms:
        all_results = {}
        all_optimal_solutions = {}
        all_execution_times = {}
        all_states_visited = {}

        for num_queens in num_queens_cases:
            results, optimal_solutions, total_time, total_states = run_experiment(num_queens, num_runs, algorithm)
            all_results_csv[algorithm].extend(results)
            

            # Store metrics for later analysis
            all_results[num_queens] = results
            all_optimal_solutions[num_queens] = optimal_solutions
            all_execution_times[num_queens] = total_time
            all_states_visited[num_queens] = total_states

            # Calculate percentages and statistics
            percentage_optimal = (optimal_solutions / num_runs) * 100
            avg_execution_time = np.mean(total_time)
            std_execution_time = np.std(total_time)
            avg_states_visited = np.mean(total_states)
            std_states_visited = np.std(total_states)

            print(f"{algorithm} with {num_queens} queens:")
            print(f"  Optimal solutions: {optimal_solutions} ({percentage_optimal:.2f}%)")
            print(f"  Avg execution time: {avg_execution_time:.4f} seconds (std: {std_execution_time:.4f})")
            print(f"  Avg states visited: {avg_states_visited:.2f} (std: {std_states_visited:.2f})\n")

        # Prepare data for boxplots
        plot_data = {
            'num_queens': num_queens_cases,
            'execution_time': [all_execution_times[nq] for nq in num_queens_cases],
            'states_visited': [all_states_visited[nq] for nq in num_queens_cases],
        }
        plot_results(plot_data, algorithm)
        save_results_to_csv(all_results_csv)
if __name__ == "__main__":
    main()
