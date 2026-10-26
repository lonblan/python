class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"

nevera = Producto("Nevera", 100)
print(nevera.mostrar_info())