import environment
import agent_reflexivo
import agent_random
list_cleaned = []

def taza_acierto(promedio, dirty_celds):
    if dirty_celds != 0:
        taza = promedio / dirty_celds
    else:
        taza = 0
    return taza

xy = [2,4,8,16,32,64,128]
dirty_rate = [0.1,0.2,0.4,0.8]
for dirt in dirty_rate:
    print("------------------")
    print(dirt)
    print("------------------")
    for long in xy:
        list_cleaned = []
        for i in range (0,10):
            # Uso como semillas i
            envprueba = environment.Environment(long,long,dirt,i)
            # envprueba.print_environment()
            # agent_ref= agent_reflexivo.Agent_reflexivo(envprueba,i)
            # agent_ref.think()
            agent_ran = agent_random.Agent_random(envprueba,i)
            agent_ran.think()
            list_cleaned.append(envprueba.get_performance())
        promedio = sum(list_cleaned)/10
        taza = taza_acierto(promedio, envprueba.get_dirty_selds())
        s = str(envprueba.get_dirty_selds()) + "," + str(promedio) + "," + str(taza)
        print(s)

