import random
#GENETIC ALGORITHM
def generate_initial_population(population_size, n):
    colors = [0, 1, 2, 3]
    return [[[random.choice(colors) for _ in range(n)] for _ in range(n)] for _ in range(population_size)]

def calculate_cost(board):
    cost = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if i < n - 1 and board[i][j] == board[i + 1][j]:
                cost += 1
            if j < n - 1 and board[i][j] == board[i][j + 1]:
                cost += 1
    return cost

def fitness_func(board):
    return -calculate_cost(board)

def crossover(parentA, parentB):
    n = len(parentA)
    crossover_point = random.randint(0, n - 1)
    child = [parentA[i][:crossover_point] + parentB[i][crossover_point:] for i in range(n)]
    return child

def to_mutate(board, mutation_rate):
    n = len(board)
    colors = [0, 1, 2, 3]
    for i in range(n):
        for j in range(n):
            if random.uniform(0, 1) < mutation_rate:
                board[i][j] = random.choice(colors)
    return board

def genetic_algorithm(population_size, n, gens, mutation_rate):
    population = generate_initial_population(population_size, n)
    for _ in range(gens):
        population = sorted(population, key=lambda x: fitness_func(x), reverse=True)
        parents = population[:2]
        child = crossover(parents[0], parents[1])
        child = to_mutate(child, mutation_rate)

        population[-1] = child
    return population[0]

#HILL CLIMBING

def generate_initial_state(n):
    colors = [0, 1, 2, 3]
    return [[random.choice(colors) for _ in range(n)] for _ in range(n)]



def hill_climbing_search(n, max_iterations):
    current_state = generate_initial_state(n)
    current_cost = calculate_cost(current_state)

    for _ in range(max_iterations):
        neighbors = []
        for i in range(n):
            for j in range(n):
                for color in [0, 1, 2, 3]:
                    if current_state[i][j] != color:
                        new_state = [row[:] for row in current_state]
                        new_state[i][j] = color
                        neighbors.append((new_state, calculate_cost(new_state)))

        neighbors.sort(key=lambda x: x[1])
        best_neighbor, neighbor_cost = neighbors[0]

        if neighbor_cost >= current_cost:
            break
        else:
            current_state, current_cost = best_neighbor, neighbor_cost

    return current_state

n= 10


population_size = 1000
generations = 100
mutation_rate = 0.3
solution_genetic = genetic_algorithm(population_size, n, generations, mutation_rate)
print("\nGenetic Algorithm ")
for row in solution_genetic:
    print(row)



max_iterations = 1000
solution = hill_climbing_search(n, max_iterations)
print("\nHill Climbing")
for row in solution:
    print(row)