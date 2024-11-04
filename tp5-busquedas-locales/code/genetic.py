#Utilizare Elitismo

from simulate_annealing import calc_heu
from escenario import *

def calc_ord_esc(escenarios):
    esc_rend = []
    n = len(escenarios[0])
    for esc in escenarios:
        h = calc_heu(esc)
        esc_rend.append((esc, h))
    # Ordena la lista de escenarios por la heurística, en orden ascendente, utiliza TimSort
    esc_rend = sorted(esc_rend, key=lambda x: x[1])
    return esc_rend

def genetics(escenarios, limit):
    check = False
    count = 0
    escena = escenarios
    while check != True:
        esc_ord = calc_ord_esc(escena)
        solo_esc = [esc[0] for esc in esc_ord]
        for i in range(0,len(solo_esc)):
            if esc_ord[i][1] == 0:   
                return esc_ord[i] , count, esc_ord
        if count == limit:
            return esc_ord[0] , limit, esc_ord
        elite = solo_esc[:6]
        resto = solo_esc[6:]
        hijos_cruce = cruce(elite, resto, len(escena) - len(elite))
        hijos_mut = mutacion(hijos_cruce)  
        new = elite + [list(hijo) for hijo in hijos_mut]
        escena = new
        count += 1

#Cruce de corte unico
def cruce(elite, resto, num_hijos):
    hijos = []
    n = len(elite[0])
    for _ in range(num_hijos // 2):
        corte = random.randint(1, n - 1)
        padre_elite = elite[random.randint(0, len(elite) - 1)]
        padre_resto = resto[random.randint(0, len(resto) - 1)]
        
        # Crear copias de los padres para evitar modificaciones no deseadas
        hijo1 = padre_elite[:corte] + padre_resto[corte:]  # Combinar hasta el corte de padre_elite y el resto de padre_resto
        hijo2 = padre_resto[:corte] + padre_elite[corte:]  # Combinar hasta el corte de padre_resto y el resto de padre_elite
        
        hijos.append(hijo1)
        hijos.append(hijo2)
        
    return hijos[:num_hijos]
        
#Mutación de Intercambio de Posiciones
def mutacion(hijos):
    n = len(hijos[0])
    new = []
    for hijo in hijos:
        pos1, pos2 = random.sample(range(n), 2)
        val = hijo[pos1]
        hijo[pos1] = hijo[pos2]
        hijo[pos2] = val
        new.append(hijo)
    return new







