class Producto(object): 
    def __init__(self, nombre, precio): 
        self.nombre = nombre 
        self.precio = precio 
        self.total = 0 
        
    def calcularTotal(self, cantidad): 
        self.total = self.precio * cantidad 

    def mostrarTotal(self): 
        print(f"Producto: {self.nombre}") 
        print(f"Total: ${self.total:.2f}") 

producto1 = Producto("Cuaderno", 35) 
producto1.calcularTotal(3) 
producto1.mostrarTotal()

 #¿Cuál es el nombre de la clase? 
 #Producto

 #¿Cuáles son sus propiedades? 
 #nombre, precio, total

 #¿Cuáles son sus métodos? 
 #__init__, calcularTotal,mostrarTotal

 #¿Qué función cumple __init__? 
 #inicia las propiedades de la clase 

 #¿Para qué se utiliza self? 
 #se usa para referirse a la instancia actual de la clase y poder entrar a sus propiedades y metodos

 #¿En qué instrucción se crea un objeto? 
 #producto1 = Producto("Cuaderno", 35) 

 #¿Cuál es el nombre del objeto? 
 #producto 1

 #¿Cómo se llama a calcularTotal()? 
 #producto1.calcularTotal(3) 

 #¿Qué valores recibe el constructor cuando se crea el objeto? 
 #"cuaderno", 35

 #¿Qué resultado mostrará el programa?
 #producto: cuaderno
 #total: $105.00


class Rectangulo(object): 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        # COMPLETAR: guardar las propiedades
        pass

    def calcularArea(self):
        # COMPLETAR: regresar el área
        return self.base * self.altura

    def mostrarArea(self):
        # COMPLETAR: mostrar el resultado
        print(f"El área del rectángulo es: {self.calcularArea()}")

# COMPLETAR: crear un objeto con base 8 y altura 5
rectangulo1 = Rectangulo(8, 5)

# COMPLETAR: llamar al método para mostrar el área
rectangulo1.mostrarArea()


class Operacion(object): 
    def __init__(self, numero1, numero2): 
        self.numero1 = numero1 
        self.numero2 = numero2 
  
    def calcular(self): 
        return self.numero1 + self.numero2 
  
class Multiplicacion(Operacion): 
    def calcular(self): 
        return self.numero1 * self.numero2

operacion1 = Operacion(8, 4) 
operacion2 = Multiplicacion(8, 4) 
print(operacion1.calcular()) 
print(operacion2.calcular())     

 #¿Cuál es la clase padre? 
 #Operacion
 #¿Cuál es la clase hija? 
 #Multiplicacion
 #¿Cómo se indica la herencia? 
 #Se pone colocando el nombre de la clase padre entre parentesis en la defincion de La Clase hija
 #¿Qué propiedades utiliza la clase hija? 
 #nuero1, numero2
 #¿Por qué puede utilizarlas sin definir su propio __init__? 
 #porque hereda el constructor de la clase padre
 #¿Por qué los métodos calcular() tienen resultados distintos? 
 #porque la clase hija multiplicacion redefine el metodo calcular()
 #¿Qué valores se imprimen? 
 #12
 #¿Qué sucedería si eliminamos calcular() de Multiplicacion?
 #se ejecutaria el metodo calcular()de la clase padre Operacion y el resultado seria 12 
 