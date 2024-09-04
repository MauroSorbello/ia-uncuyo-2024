import numpy as np
import generate_random_map_custom 
def choose_action(x,y,len_desc):
    action = []
    if x != 0: action.append(0)
    if x != (len_desc - 1): action.append(1)
    if y != 0: action.append(2)
    if y != (len_desc - 1): action.append(3)
    return action

def action(num, node):
    if num == 0: 
        new_node = (node[0] - 1, node[1])
    if num == 1:
        new_node = (node[0] + 1, node[1])
    if num == 2:
        new_node = (node[0], node[1] - 1)
    if num == 3:
        new_node = (node[0], node[1] + 1)
    return new_node

def bfs(env):
    desc = env.unwrapped.desc
    desc_str = [[cell.decode('utf-8') for cell in row] for row in desc]
    print(desc_str)
    # Crear la cola FIFO de frontera usando deque
    frontier = []
    explored = set()
    len_desc = len(desc)
    parent = {}
    # Busco el S: Start
    for i in range (len_desc):
        for j in range (len_desc):
            if desc_str[i][j] == "S":
                frontier.append((i,j))
                parent[(i,j)] = None
    check = False
    solution = None
    while check == False:
        if len(frontier) == 0:
            break
        print(frontier)
        node = frontier.pop(0)
        print(frontier)
        explored.add(node)
        # Devuelve las posibles acciones
        actions = choose_action(node[0], node[1], len_desc)
        for act in actions:
            child_node = action(act, node)
            if desc_str[child_node[0]][child_node[1]] != "H":
                if (child_node not in explored) and (child_node not in frontier):
                    parent[child_node]=node
                    if desc_str[child_node[0]][child_node[1]] == "G":
                        print(child_node)
                        solution = child_node
                        check = True
                        break
                    else:
                        frontier.append(child_node)
    if solution == None:
        return False
    else:
        path = []
        sol = solution
        while sol is not None:
            if sol == None:
                break
            path.append(sol)
            sol = parent[sol]
        path.reverse()  
        return solution, path

env, desc = generate_random_map_custom.generate_random_map_custom(4, 0.4, 3)
print(desc[2][0])

recorrido = bfs(env)
print(recorrido)