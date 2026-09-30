class Usuario:
    def __init__(self, nombre, pin, saldo):
        self.nombre = nombre
        self.pin = pin
        self.saldo = saldo

    
class Banco:
    def __init__(self,usuarios=[]):
        self.usuarios = usuarios

    def autenticar(self, nombre, pin):

        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.pin == pin:
                print("Estás logueado")
                return True
        print("Usuario no existe")
        return False


    

    


    def sacar_dinero(self, nombre, cantidad):
        for usuario in self.usuarios:
         if usuario.nombre == nombre:
            if usuario.saldo < cantidad:
                print("Saldo insuficiente")
            else:
                usuario.saldo -= cantidad
                print(f"El saldo disponible es de {usuario.saldo}")
            break
        else:
         print("Usuario no existe")
          
ana = Usuario("Ana", "1234", 1000)
juan = Usuario("Juan", "5678", 2000)
rodrigo = Usuario("Rodrigo", "9101", 3000)

banco = Banco(usuarios=[ana, juan, rodrigo])



while True:
    print("Bienvenido al Banco, por favor identifíquese")
    print("Introduzca el nombre:")
    nombre = input()
    print("Introduzca su pin")
    pin = input()
    if banco.autenticar(nombre, pin):
        while True:
            print("Por elija una de las siguientes opciones: \n 1. Sacar dinero \n 2. Terminar sesión")
            opcion = input()
            if opcion == "1":
                print("Ingrese la cantidad a sacar: ")
                saldo = int(input())
                banco.sacar_dinero(nombre, saldo)
                break

            elif opcion == "2":
              print("Sesión terminada")
              break
            else:
              print("Opción incorrecta")
              break
    








     
     





















                




