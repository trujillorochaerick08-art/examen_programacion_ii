

class Estacionamiento:
    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):
        if 1 <= self.horas <= 2:
            tarifa = 15.00
        elif 3 <= self.horas <= 5:
            tarifa = 12.00
        else:
            tarifa = 10.00
        return self.horas * tarifa

    def mostrarRecibo(self):
        total = self.calcularPago()
        print(f"Horas estacionadas: {self.horas}")
        print("RECIBO DE ESTACIONAMIENTO")
        print(f"Horas: {self.horas}")
        print(f"Total a pagar: ${total:.2f}")


horas = int(input("Ingrese las horas estacionadas: "))
if horas > 0:
    estacionamiento = Estacionamiento(horas)
    estacionamiento.mostrarRecibo()
else:
    print("Por favor, ingrese un número entero mayor que cero.")
