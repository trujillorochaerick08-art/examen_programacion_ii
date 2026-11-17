
#Número 1: 20 
#Número 2: 8 
#Resultado de la suma: 28 
#Resultado de la resta: 12

class Operacion:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self):
        return self.numero1 + self.numero2

    def mostrarResultado(self):
        resultado = self.calcular()
        print(f"Resultado de la suma: {resultado}")

class Resta(Operacion):
    def calcular(self):
        return self.numero1 - self.numero2

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

suma = Operacion(numero1, numero2)
resta = Resta(numero1, numero2)

suma.mostrarResultado()
resta.mostrarResultado()