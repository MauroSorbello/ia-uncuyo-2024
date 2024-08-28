import random

class Agent:
    def __init__(self, env, seed):
        #Inicializo su posicion
        if seed != None:
            random.seed(seed)
        self.env = env
        self.posX = random.randint(0, self.env.sizeX-1)
        self.posY = random.randint(0, self.env.sizeY-1)
        #Inicializo los movimientos en 0
        self.mov = 0

# Las acciones permitidas son:
# • Arriba
# • Abajo
# • Izquierda
# • Derecha
# • Limpiar (aspirar)
# • NoHacerNada

    def up(self):
        if self.env.accept_action(1,self.posX, self.posY - 1):
            self.posY -= 1
            self.mov +=1
        return
    def down(self):
        if self.env.accept_action(2,self.posX, self.posY + 1):
            self.posY += 1 
            self.mov +=1
        return
    def left(self):
        if self.env.accept_action(3,self.posX - 1, self.posY):
            self.posX -= 1
            self.mov +=1 
        return
    def right(self):
        if self.env.accept_action(4,self.posX + 1, self.posY):
            self.posX += 1
            self.mov +=1
        return
    def suck(self):
        if self.env.accept_action(5,self.posX, self.posY):
            self.mov +=1
        return
    def idle(self):
        self.mov +=1
        return