
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

def dfs(env):
    desc = env.unwrapped.desc
    desc_str = [[cell.decode('utf-8') for cell in row] for row in desc]
    print(desc_str)
    # Crear la cola LIFO de frontera usando deque
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
        node = frontier.pop()
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

# depth limited search
def dls(env,limit): 
    desc = env.unwrapped.desc
    desc_str = [[cell.decode('utf-8') for cell in row] for row in desc]
    print(desc_str)
    # Crear la cola LIFO de frontera usando deque
    frontier = []
    explored = set()
    len_desc = len(desc)
    parent_profundidad = {}
    # Busco el S: Start
    for i in range (len_desc):
        for j in range (len_desc):
            if desc_str[i][j] == "S":
                frontier.append((i,j))
                parent_profundidad[(i,j)] = (None,1)
    check = False
    solution = None
    while check == False:
        if len(frontier) == 0:
            break
        print(frontier)
        node = frontier.pop()
        print(frontier)
        explored.add(node)
        # Devuelve las posibles acciones
        actions = choose_action(node[0], node[1], len_desc)
        for act in actions:
            child_node = action(act, node)
            if desc_str[child_node[0]][child_node[1]] != "H":
                if (child_node not in explored) and (child_node not in frontier):
                    if (parent_profundidad[node][1] + 1) <= limit:
                        parent_profundidad[child_node]=(node,parent_profundidad[node][1] + 1)
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
            sol = parent_profundidad[sol][0]
        path.reverse()  
        return solution, path
    
def uniform_cost(env, cost):
    desc = env.unwrapped.desc
    desc_str = [[cell.decode('utf-8') for cell in row] for row in desc]
    # Crear la cola FIFO de frontera usando deque
    frontier = []
    explored = set()
    len_desc = len(desc)
    parent_priority = {}
    # Busco el S: Start y el goal G
    for i in range (len_desc):
        for j in range (len_desc):
            if desc_str[i][j] == "S":
                frontier.append((0, (i,j)))
                parent_priority[(i,j)] = (None,0)
    check = False
    while check == False:
        if len(frontier) == 0:
            break
        priority, node = frontier.pop()
        if desc_str[node[0]][node[1]] == "G":
            print(node)
            solution = node
            check = True
            break
        explored.add(node)
        # Devuelve las posibles acciones
        actions = choose_action(node[0], node[1], len_desc)
        for act in actions:
            child_node = action(act, node)
            # Comprobar si está dentro de los límites y no es una 'H' (obstáculo)
            if 0 <= child_node[0] < len_desc and 0 <= child_node[1] < len(desc_str[0]):
                if desc_str[child_node[0]][child_node[1]] != "H":
                    #Calculamos el costo:
                    if cost == 0:
                        child_priority = priority + 1
                    else:
                        child_priority = priority + act + 1
                    if (child_node not in explored) and (child_node not in frontier):
                        frontier.append((0, child_node))
                        parent_priority[child_node] = (node, child_priority)
                    elif parent_priority[child_node][1] > child_priority:
                        i = 0
                        # Buscamos el nodo en la frontera
                        for n in frontier:
                            i += 1
                            if n[1] == child_node:
                                priority_new , elem = frontier[i-1]
                                if priority_new > priority:
                                    frontier.pop([i-1])
                                    frontier.append((child_priority, child_node))
                                    parent_priority[child_node] = (node, child_priority) 
                    parent = parent_priority[child_node][0]
                    parent_priority[child_node] = (parent, child_priority)   
    if solution == None:
        return False
    else:
        print(parent_priority)
        path = []
        sol = solution
        while sol is not None:
            if sol == None:
                break
            path.append(sol)
            sol = parent_priority[sol][0]
        path.reverse()  
        return solution, path


    
    return solution, path
                

# Para problemas en una cuadrícula, como un laberinto donde solo puedes moverte en líneas rectas 
# (arriba, abajo, izquierda, derecha), la distancia de Manhattan es una buena heurística.
# h = abs(xcurrent - xgoal) + abs(ycurrent - ygoal)

def heuristic(node, goal):
    h = abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    return h

def a_star(env, cost):
    desc = env.unwrapped.desc
    desc_str = [[cell.decode('utf-8') for cell in row] for row in desc]
    # Crear la cola FIFO de frontera usando deque
    frontier = []
    explored = set()
    len_desc = len(desc)
    parent_priority = {}
    # Busco el S: Start y el goal G
    for i in range (len_desc):
        for j in range (len_desc):
            if desc_str[i][j] == "S":
                frontier.append((0, (i,j)))
                parent_priority[(i,j)] = (None,0)
            if desc_str[i][j] == "G":
                goal = (i,j)
    check = False
    while check == False:
        if len(frontier) == 0:
            break
        priority, node = frontier.pop()
        if desc_str[node[0]][node[1]] == "G":
            print(node)
            solution = node
            check = True
            break
        explored.add(node)
        # Devuelve las posibles acciones
        actions = choose_action(node[0], node[1], len_desc)
        for act in actions:
            child_node = action(act, node)
            # Comprobar si está dentro de los límites y no es una 'H' (obstáculo)
            if 0 <= child_node[0] < len_desc and 0 <= child_node[1] < len(desc_str[0]):
                if desc_str[child_node[0]][child_node[1]] != "H":
                    #Calculamos el costo:
                    if cost == 0:
                        child_priority = priority + heuristic(child_node, goal)
                    else:
                        child_priority = priority + act + heuristic(child_node, goal)
                    if (child_node not in explored) and (child_node not in frontier):
                        frontier.append((0, child_node))
                        parent_priority[child_node] = (node, child_priority)
                    elif parent_priority[child_node][1] > child_priority:
                        i = 0
                        # Buscamos el nodo en la frontera
                        for n in frontier:
                            i += 1
                            if n[1] == child_node:
                                priority_new , elem = frontier[i-1]
                                if priority_new > priority:
                                    frontier.pop([i-1])
                                    frontier.append((child_priority, child_node))
                                    parent_priority[child_node] = (node, child_priority) 
                    parent = parent_priority[child_node][0]
                    parent_priority[child_node] = (parent, child_priority)   
    if solution == None:
        return False
    else:
        print(parent_priority)
        path = []
        sol = solution
        while sol is not None:
            if sol == None:
                break
            path.append(sol)
            sol = parent_priority[sol][0]
        path.reverse()  
        return solution, path
    
env, desc = generate_random_map_custom.generate_random_map_custom(4, 0.4, 7)
print(desc)

recorrido = a_star(env,1)
print(recorrido)

