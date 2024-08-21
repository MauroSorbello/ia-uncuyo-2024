import random
import agent
class Agent_random(agent.Agent):
    def think(self): # implementa las acciones a seguir por el agente
        for i in range(0,1000): #Frena despues de los mil movimientos
            #Realiza un movimiento ramdon
            move = random.randint(1,6)
            if move == 1: self.up()
            elif move == 2: self.down()
            elif move == 3: self.left()
            elif move == 4: self.right()
            elif move == 5: self.suck()
            else: self.idle()

