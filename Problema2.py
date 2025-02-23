import random

class BuscadorObjeto:
    def __init__(self):
        self.matriz = [[0 for _ in range(5)] for _ in range(5)]
        self.posicion = [0, 0]
        self.objeto = [random.randint(0, 4), random.randint(0, 4)]
        self.matriz[self.objeto[0]][self.objeto[1]] = 1  # Colocar el objeto

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(fila)
        print()

    def mover_hacia_objeto(self):
        while self.posicion != self.objeto:
            self.mostrar_matriz()
            if self.posicion[0] < self.objeto[0]:
                self.posicion[0] += 1  # Mover hacia abajo
            elif self.posicion[0] > self.objeto[0]:
                self.posicion[0] -= 1  # Mover hacia arriba
            elif self.posicion[1] < self.objeto[1]:
                self.posicion[1] += 1  # Mover hacia la derecha
            elif self.posicion[1] > self.objeto[1]:
                self.posicion[1] -= 1  # Mover hacia la izquierda
            
            print(f"Moviendo a la posición: {self.posicion}")

# Crear el agente buscador y buscar el objeto
buscador = BuscadorObjeto()
buscador.mover_hacia_objeto()
