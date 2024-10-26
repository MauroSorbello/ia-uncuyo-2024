import heapq
import random
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
    # print(desc_str)
    # Crear la cola FIFO de frontera usando deque
    acts = []
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
        # print(frontier)
        node = frontier.pop(0)
        # print(frontier)
        explored.add(node)
        # Devuelve las posibles acciones
        actions = choose_action(node[0], node[1], len_desc)
        for act in actions:
            child_node = action(act, node)
            if desc_str[child_node[0]][child_node[1]] != "H":
                if (child_node not in explored) and (child_node not in frontier):
                    parent[child_node] = (node, act)
                    if desc_str[child_node[0]][child_node[1]] == "G":
                        # print(child_node)
                        solution = child_node
                        check = True
                        break
                    else:
                        frontier.append(child_node)
    if solution == None:
        return None
    else:
        path = []
        acts = []
        sol = solution
        while sol is not None:
            path.append(sol)
            if parent[sol] is not None:
                sol, action_taken = parent[sol]
                acts.append(action_taken)  # Agregar la acción al camino
            else:
                sol = None
        path.reverse()
        return solution, path, acts

def dfs(env):
    desc = env.unwrapped.desc
    desc_str = [[cell.decode('utf-8') for cell in row] for row in desc]
    # print(desc_str)
    # Crear la cola LIFO de frontera usando deque
    frontier = []
    explored = set()
    len_desc = len(desc)
    parent = {}
    acts = []
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
        # print(frontier)
        node = frontier.pop()
        # print(frontier)
        explored.add(node)
        # Devuelve las posibles acciones
        actions = choose_action(node[0], node[1], len_desc)
        for act in actions:
            child_node = action(act, node)
            if desc_str[child_node[0]][child_node[1]] != "H":
                if (child_node not in explored) and (child_node not in frontier):
                    parent[child_node] = (node, act)
                    if desc_str[child_node[0]][child_node[1]] == "G":
                        # print(child_node)
                        solution = child_node
                        check = True
                        break
                    else:
                        frontier.append(child_node)
    if solution == None:
        return None
    else:
        path = []
        acts = []
        sol = solution
        while sol is not None:
            path.append(sol)
            if parent[sol] is not None:
                sol, action_taken = parent[sol]
                acts.append(action_taken)  # Agregar la acción al camino
            else:
                sol = None
        path.reverse()
        return solution, path, acts

# depth limited search
def dls(env,limit): 
    desc = env.unwrapped.desc
    desc_str = [[cell.decode('utf-8') for cell in row] for row in desc]
    # print(desc_str)
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
        # print(frontier)
        node = frontier.pop()
        # print(frontier)
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
                            # print(child_node)
                            solution = child_node
                            check = True
                            break
                        else:
                            frontier.append(child_node)
    if solution == None:
        return None
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

    # Crear la cola de prioridad de frontera usando heapq
    frontier = []
    explored = set()
    len_desc = len(desc)
    parent_priority = {}

    # Buscar el punto de inicio "S" y el punto objetivo "G"
    for i in range(len_desc):
        for j in range(len_desc):
            if desc_str[i][j] == "S":
                heapq.heappush(frontier, (0, (i, j)))  # Prioridad inicial 0
                parent_priority[(i, j)] = (None, 0)

    check = False
    solution = None

    while not check:
        if not frontier:
            break

        # Extraemos el nodo con menor costo acumulado (heap)
        priority, node = heapq.heappop(frontier)
        # Si llegamos al objetivo, terminamos
        if desc_str[node[0]][node[1]] == "G":
            solution = node
            check = True
            break

        explored.add(node)
        actions = choose_action(node[0], node[1], len_desc)

        for act in actions:
            child_node = action(act, node)

            # Verificar si el nodo hijo está dentro de los límites y no es obstáculo
            if 0 <= child_node[0] < len_desc and 0 <= child_node[1] < len(desc_str[0]):
                if desc_str[child_node[0]][child_node[1]] != "H":  # No es obstáculo
                    # Calcular el costo:
                    if cost == 0:
                        # Si el costo es constante, sumar 1 por cada movimiento
                        child_priority = priority + 1
                    else:
                        # Asignar un costo diferente basado en la dirección (act)
                        if act == 0:  # Arriba
                            move_cost = 2
                        elif act == 1:  # Abajo
                            move_cost = 1
                        elif act == 2:  # Izquierda
                            move_cost = 3
                        elif act == 3:  # Derecha
                            move_cost = 1

                        child_priority = priority + move_cost

                    # Si el nodo hijo no está explorado o encontramos un mejor costo, lo añadimos a la frontera
                    if child_node not in explored and all(child_node != f[1] for f in frontier):
                        heapq.heappush(frontier, (child_priority, child_node))
                        parent_priority[child_node] = (node, child_priority)
                    elif child_node in parent_priority and parent_priority[child_node][1] > child_priority:
                        # Actualizamos la prioridad del nodo si encontramos un mejor costo
                        parent_priority[child_node] = (node, child_priority)
                        heapq.heappush(frontier, (child_priority, child_node))

    if solution is None:
        return None
    else:
        # Reconstruir el camino de solución
        path = []
        sol = solution
        total_cost = parent_priority[sol][1] 
        while sol is not None:
            path.append(sol)

             # Actualiza el costo total acumulado
            sol = parent_priority[sol][0]

        path.reverse()
        return solution, path, total_cost

def aleatorio(env):
    desc = env.unwrapped.desc
    desc_str = [[cell.decode('utf-8') for cell in row] for row in desc]
    # print(desc_str)
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
    step = 0
    while check == False:
        if len(frontier) == 0:
            break
        # print(frontier)
        node = frontier.pop(0)
        # print(frontier)
        explored.add(node)
        # Devuelve las posibles acciones
        act = random.randint(0,3)
        child_node = action(act, node)
        step = step + 1
        if desc_str[child_node[0]][child_node[1]] != "H":
            parent[child_node]=node
            if desc_str[child_node[0]][child_node[1]] == "G":
                solution = child_node
                check = True
                break
            else:
                frontier.append(child_node)
        else: 
            return None
        if step == 1000:
            return None
    if solution == None:
        return None
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

                

# Para problemas en una cuadrícula, como un laberinto donde solo puedes moverte en líneas rectas 
# (arriba, abajo, izquierda, derecha), la distancia de Manhattan es una buena heurística.
# h = abs(xcurrent - xgoal) + abs(ycurrent - ygoal)

def heuristic(node, goal):
    h = abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    return h

def a_star(env, cost):
    desc = env.unwrapped.desc
    desc_str = [[cell.decode('utf-8') for cell in row] for row in desc]

    # Crear la cola de prioridad de frontera usando heapq
    frontier = []
    explored = set()
    len_desc = len(desc)
    parent_priority = {}

    # Buscar el punto de inicio "S" y el punto objetivo "G"
    goal = None
    for i in range(len_desc):
        for j in range(len_desc):
            if desc_str[i][j] == "S":
                heapq.heappush(frontier, (0, (i, j)))  # Prioridad inicial 0
                parent_priority[(i, j)] = (None, 0)
            if desc_str[i][j] == "G":
                goal = (i, j)

    check = False
    solution = None

    while not check:
        if not frontier:
            break

        priority, node = heapq.heappop(frontier)  # Extraemos el nodo con menor costo

        if desc_str[node[0]][node[1]] == "G":
            solution = node
            check = True
            break

        explored.add(node)
        actions = choose_action(node[0], node[1], len_desc)

        for act in actions:
            child_node = action(act, node)

            if 0 <= child_node[0] < len_desc and 0 <= child_node[1] < len(desc_str[0]):
                if desc_str[child_node[0]][child_node[1]] != "H":  # Verificar si es un obstáculo
                    # Cálculo del costo g
                    if cost == 0:
                        g_cost = parent_priority[node][1] + 1  # Si cost == 0, costo uniforme
                    else:
                        g_cost = parent_priority[node][1] + 1  # Aquí puedes ajustar el costo dinámico si es necesario

                    # Cálculo del costo f
                    f_cost = g_cost + heuristic(child_node, goal)

                    # Si el nodo hijo no está explorado y no está en la frontera, o si encontramos un mejor costo
                    if child_node not in explored and all(child_node != f[1] for f in frontier):
                        heapq.heappush(frontier, (f_cost, child_node))
                        parent_priority[child_node] = (node, g_cost)
                    elif child_node in parent_priority and parent_priority[child_node][1] > g_cost:
                        # Si encontramos un mejor camino a este nodo, actualizamos la prioridad
                        parent_priority[child_node] = (node, g_cost)
                        heapq.heappush(frontier, (f_cost, child_node))

    if solution is None:
        return False
    else:
        # Reconstruir el camino de solución
        path = []
        sol = solution
        total_cost = parent_priority[sol][1]
        while sol is not None:
            path.append(sol)
            sol = parent_priority[sol][0]

        path.reverse()
        return solution, path, total_cost
