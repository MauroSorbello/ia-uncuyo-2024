import random

class Environment:
    #init_posX,init_posY,
    #Quite la posicion inicial a environment, dado a que esta va cuando se inicializa el cliente
    def __init__(self,sizeX,sizeY,dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        #Crear matriz environment
        self.env = [[0 for _ in range(sizeY)] for _ in range(sizeX)]
        self.dirt_rate = dirt_rate
        #Largo de celdas sucias
        self.dirty_celds = round(sizeX * sizeY * dirt_rate)
        # print(dirty_celds)
        #Inicializar las celdas sucias
        for i in range(self.dirty_celds):
            check = False
            while check != True:
                rx = random.randint(0, (sizeX) - 1)
                ry = random.randint(0, (sizeY) - 1)
                # print(rx,ry)
                if self.env[rx][ry] != 1:
                    self.env[rx][ry] = 1
                    check = True
        # print("____________")
        self.cleaned_celds = 0

    #x,y para recibir la posicion del agente
    def accept_action(self,action,x,y):
        if action == 1: #Arriba
            if x < self.sizeX and y >= 0:
                return True
        elif action == 2: #Abajo
            if x < self.sizeX and y < self.sizeY:
                return True
        elif action == 3: #Izquierda
            if x >= 0 and y >= 0:
                return True
        elif action == 4: #Derecha
            if x < self.sizeX and y >= 0:
                return True 
        elif action == 5: #limpiar
            if x < self.sizeX and y < self.sizeY:
                if self.is_dirty(x,y):
                    self.env[x][y] = 0
                    self.cleaned_celds += 1
        
    #retorna true si esta sucio
    def is_dirty(self, x, y):
        
        if self.env[x][y] == 1:
            return True
        else:
            return False
         
    def get_performance(self):
        performance = self.cleaned_celds
        return (performance,self.dirty_celds)

    def print_environment(self):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                print(self.env[x][y], end = " ")
            print("") 

# envprueba = Environment(2,2,0.5)
# envprueba.print_environment()