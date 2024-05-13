import random
import math

class NeuronaArtificial:
    def __init__(self, num_entradas):
        self.num_entradas = num_entradas
        self.pesos = [random.uniform(0, 1) for _ in range(num_entradas)]
        self.sesgo = random.uniform(0, 1)

    def funcion_activacion(self, suma_ponderada):
        return 1 / (1 + math.exp(-suma_ponderada))

    def entrenar(self, entradas, salida_deseada, tasa_aprendizaje, num_iteraciones):
        for _ in range(num_iteraciones):
            for j in range(len(entradas)):
                suma_ponderada = 0
                for i in range(self.num_entradas):
                    suma_ponderada += entradas[j][i] * self.pesos[i]
                suma_ponderada += self.sesgo
                salida_calculada = self.funcion_activacion(suma_ponderada)

                error = salida_deseada[j] - salida_calculada
                ajuste = error * salida_calculada * (1 - salida_calculada)

                for i in range(self.num_entradas):
                    self.pesos[i] += tasa_aprendizaje * ajuste * entradas[j][i]
                self.sesgo += tasa_aprendizaje * ajuste

    def predecir(self, entrada):
        suma_ponderada = 0
        for i in range(self.num_entradas):
            suma_ponderada += entrada[i] * self.pesos[i]
        suma_ponderada += self.sesgo
        return self.funcion_activacion(suma_ponderada)

# Ejemplo de uso
num_entradas = 2
num_ejemplos = 4
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
salida_deseada = [0, 1, 1, 1]

tasa_aprendizaje = 0.1
num_iteraciones = 1000

neurona = NeuronaArtificial(num_entradas)
neurona.entrenar(entradas, salida_deseada, tasa_aprendizaje, num_iteraciones)

# Prueba
entrada_prueba = [1, 0]
prediccion = neurona.predecir(entrada_prueba)
print(f"Predicción: {prediccion}")
