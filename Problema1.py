import random
import time

class SemaforoInteligente:
    def __init__(self):
        self.estado = "rojo"

    def cambiar_estado(self, vehiculos):
        if vehiculos > 10:
            self.estado = "verde"
            duracion = 30  # 30 segundos en verde
        elif vehiculos > 0:
            self.estado = "amarillo"
            duracion = 5  # 5 segundos en amarillo
        else:
            self.estado = "rojo"
            duracion = 20  # 20 segundos en rojo
        
        print(f"Estado del semáforo: {self.estado} (duración: {duracion} segundos)")
        time.sleep(duracion)

    def simular_trafico(self):
        while True:
            vehiculos = random.randint(0, 20)  # Simulación de vehículos detectados
            self.cambiar_estado(vehiculos)

# Crear el agente de semáforo y simular el tráfico
semaforo = SemaforoInteligente()
semaforo.simular_trafico()
