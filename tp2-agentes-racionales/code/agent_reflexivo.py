import random
import agent
class Agent_reflexivo(agent.Agent):
    def __init__(self,env):
        # Llamada al constructor de la clase base
        super().__init__(env)
    def idle(self): # no hace nada
        self.mov = self.mov
        return
    def perspective(self): # sensa el entorno
        if self.env.is_dirty(self.posX, self.posY):
            self.suck()
            return 1
        else:
            self.idle()
            return 0
    def think(self): # implementa las acciones a seguir por el agente
        for i in range(0, 1000): #Frena despues de los mil movimientos
            #Analiza su entorno
            pers=self.perspective()
            if pers == 0:
                i -= 1
            #Realiza un movimiento ramdon
            move = random.randint(1,4)
            if move == 1: self.up()
            elif move == 2: self.down()
            elif move == 3: self.left()
            elif move == 4: self.right()

