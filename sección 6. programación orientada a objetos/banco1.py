
class Usuario:
    def __init__(self, nombre, pin, saldo):
        self.nombre = nombre
        self.pin = pin
        self.saldo = saldo


class Banco:
    def __init__(self, usuarios=[]):
        self.usuarios = usuarios

    def autenticar(self, nombre, pin):
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.pin == pin:
                print("Estas Logueado")
                return True
        print("usuario no existe")
        return False


    def sacar_dinero(self, nombre, cantidad):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if usuario.saldo < cantidad:
                    print("saldo insuficiente")
            else:
                usuario.saldo -= cantidad
                print(f"El saldo disponible se de $ {usuario.saldo}")
            break
        else:
            print("usuario no existe")



ana = Usuario("ana", "1234", 1000)
pedro = Usuario("pedro", "5678", 4000)
samuel = Usuario("samuel", "1235", 3456)

banco = Banco([ana, pedro, samuel])

while True:
    print("Bienvenio al banco; por favor identifíquese")
    print("Introduzca el nombre")
    nombre = input()
    print("Introduzca el pin")
    pin = input()
    if banco.autenticar(nombre, pin):
        while True:
            print("Por favor elija una delas siguiente sopciones: \n 1. Sacar dinero \n 2. Terminar sesión")
            opcion = input()
            if opcion == "1":
                print("Introduzca la cantidad a sacar")
                cantidad = int(input())
                banco.sacar_dinero(nombre, cantidad)
                break
            elif opcion == "2":
                print("Sesión terminada")
                break
            else:
                print("opción incorrecta")






        

    








     
     





















                




