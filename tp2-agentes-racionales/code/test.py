import environment
import agent_reflexivo
import agent_random
for i in range (0,10):
    envprueba = environment.Environment(128,128,0.8)
    agent_ref = agent_reflexivo.Agent_reflexivo(envprueba)
    agent_ref.think()
    print(envprueba.get_performance())

# for i in range (0,10):
#     envprueba = environment.Environment(128,128,0.8)
#     agent_ran = agent_random.Agent_random(envprueba)
#     agent_ran.think()
#     print(envprueba.get_performance())