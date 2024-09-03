import random
import gymnasium as gym
# Arme una nueva funci´on generate_random_map_custom que permita definir el tama˜no de
# la grilla, la probabilidad que una casilla sea de hielo, y ubique de forma aleatoria la posici´on
# inicial del agente y del objetivo (el entorno creado a partir de dicha funci´on podr´ıa no tener
# soluci´on).

# desc=["SFFF", "FHFH", "FFFH", "HFFG"]
# S = Start, F = Frozen, H = Hole, G = Goal
def generate_random_map_custom(size_desc, hole_prob, seed = None, slippery = False):
    if seed != None:
        random.seed(seed)
    desc = [['F' for _ in range(size_desc)] for _ in range(size_desc)]
    hole_celds = round(size_desc * size_desc * hole_prob)
    for i in range(hole_celds):
        check = False
        while check != True:
            rx = random.randint(0, (size_desc) - 1)
            ry = random.randint(0, (size_desc) - 1)
            # print(rx,ry)
            if desc[rx][ry] != 'H':
                desc[rx][ry] = 'H'
                check = True
    rx = random.randint(0, (size_desc) - 1)
    ry = random.randint(0, (size_desc) - 1)
    # POSICION INICIAL AGENTE
    desc[rx][ry] = "S"
    rx = random.randint(0, (size_desc) - 1)
    ry = random.randint(0, (size_desc) - 1)
    # POSICION GOAL
    desc[rx][ry] = "G"
    env = gym.make("FrozenLake-v1", desc=desc, render_mode="human", is_slippery = slippery)
    return env, desc

env, desc = generate_random_map_custom(4, 0.5, 2)
print(desc)
