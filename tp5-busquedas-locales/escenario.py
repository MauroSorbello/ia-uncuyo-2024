import random

def esc(num_queens, seed):

    if seed != None:
        random.seed(seed)
    current = [random.randint(0, num_queens - 1) for _ in range(num_queens)]
    while len(set(current)) < num_queens:
        current = [random.randint(0, num_queens - 1) for _ in range(num_queens)]
    return current