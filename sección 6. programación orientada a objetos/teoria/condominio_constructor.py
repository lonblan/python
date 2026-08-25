class Apartamento:
    def __init__ (self,tamaño, precio, habitaciones, ubicacion):
        self.tamaño = tamaño
        self.precio = precio
        self.habitaciones = habitaciones
        self.ubicacion = ubicacion

class Condominio:
    def __init__ (self, apartamentos = []):
        self.apartamentos = apartamentos


    def mostrar_apartamentos(self):
        for apartamento in self.apartamentos:
            print("Tamaño: " + apartamento.tamaño+". Precio: " + apartamento.precio+". Habitaciones: " + apartamento.habitaciones+". Ubicacion: " + apartamento.ubicacion)

apartamento_1 = Apartamento("120 mtrs", "100.000.000", "4", "Torre 4 101")
apartamento_2 = Apartamento("110 mtrs", " 90.000.000", "5", "Torre 4 201")
apartamento_3 = Apartamento("140 mtrs", "180.000.000", "6", "Torre 6 301")

condominio_reserva = Condominio(apartamentos = [apartamento_1, apartamento_2, apartamento_3])
condominio_reserva.mostrar_apartamentos()

































