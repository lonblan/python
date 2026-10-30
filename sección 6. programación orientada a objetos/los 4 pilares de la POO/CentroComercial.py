


class Producto:
    def __init__(self, referencia, nombre, pvp):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        

    def __str__(self):
        return f"Producto: {self.referencia}, Nombre:: {self.nombre}, Precio:: {self.pvp}"

class alimento(Producto):
    def __init__(self, referencia, nombre, pvp, alimento):
     super().__init__(referencia, nombre, pvp)
     self.tipo = alimento

    def __str__(self):
        return f"Producto: {self.referencia} , Nombre:: {self.nombre}, Precio:: {self.pvp}, Tipo:: {self.tipo}"



class electrodomestico(Producto):
    def __init__(self, referencia, nombre, pvp, electrodomestico):
     super().__init__(referencia, nombre, pvp)
     self.tipo = electrodomestico

    def __str__(self):
        return f"Producto: {self.referencia}, Nombre:: {self.nombre}, Precio:: {self.pvp}, Tipo: {self.tipo}"


class moda(Producto):
    def __init__(self, referencia, nombre, pvp, moda):
     super().__init__(referencia, nombre, pvp)
     self.tipo = moda

    def __str__(self):
        return f"Producto: {self.referencia}, Nombre:: {self.nombre}, Precio:: {self.pvp}, Tipo: {self.tipo}"


manzana = alimento(1, "Manzana", 1.5, "alimento")
pera = alimento(2, "Peras", 2, "alimento")

lavadora = electrodomestico(3, "Lavadora", 100,  "Electrodomestico")
nevera = electrodomestico(4, "Nevera", 100, "Electrodomestico")

camiseta = moda(5, "Camiseta", 10, "Moda")
pantalon = moda(6, "Pantalon", 10, "Moda")

alimentos = [manzana, pera]
electrodomesticos = [lavadora, nevera]
modas = [camiseta, pantalon]


def listar_productos(productos):
    for producto in productos:
        print(f"Producto: {producto.referencia}, Nombre: {producto.nombre}, Precio: {producto.pvp}, Tipo: {producto.tipo}")

def vender_producto(productos):
    print("Elija un producto para comprar (Elija la referncia)):")
    teclado = int(input())

    for producto in productos:
        if producto.referencia == teclado:
            print(f"Producto: {producto.referencia}, Nombre: {producto.nombre}, Precio: {producto.pvp}, Tipo: {producto.tipo}")
            print("Producto vendido")

            productos.remove(producto)
            return
            
    print("Producto no encontrado")




while True:
    print("Bienvenido al Centro Comercial, elija una opción")
    
    print("1. Listar productos alimentos")
    print("2. Vender producto alimentos")
    print("3. Listar productos electrodomesticos")
    print("4. Vender producto electrodomesticos")
    print("5. Listar productos moda")
    print("6. Vender producto moda")
    print("7. Salir")

    opcion = int(input())

    if opcion == 1:
        listar_productos(alimentos)
    elif opcion == 2:
        vender_producto(alimentos)
    elif opcion == 3:
        listar_productos(electrodomesticos)
    elif opcion == 4:
        vender_producto(electrodomesticos)
    elif opcion == 5:
        listar_productos(modas)
    elif opcion == 6:
        vender_producto(modas)

    elif opcion == 7:
        print("Gracias por su visita")
        break
    else:
        print("Opcion no valida")