#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
#El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase: 

#Un constructor.
#mostrar(): Muestra los datos de la cuenta. 
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
#retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos


class Cuenta:

    #CONSTRUCTOR
    def __init__(self,titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
    def ingresar(self):
        print ("*** INGRESE EL MONTO QUE DESEA INGRESAR ***")
        cantidad = float(input("MONTO: "))
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se agregaron ${cantidad} a tu cuenta bancaria")

    def retirar(self):
        print ("*** INGRESE EL MONTO QUE DESEA RETIRAR ***")
        retirar = float(input("MONTO: "))
        if retirar > 0:
            self.cantidad -= retirar
            print(f"Se descontaron ${retirar} de tu cuenta bancaria")
    def mostrar(self):
        print ("EL TITULAR ES: ", self.titular)
        print ("EL TOTAL DE LA CUENTA ES: ", self.cantidad)
        
        
Cuenta1 = Cuenta("Mauro Sorbello")

Cuenta1.ingresar()
Cuenta1.retirar()
Cuenta1.mostrar()