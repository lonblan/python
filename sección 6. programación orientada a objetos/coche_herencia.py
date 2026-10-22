class Coche:
    def __init__(self, marca, color,precio):
        self.marca = marca
        self.color = color
        self.precio = precio

    def describir(self):
        print(f"{self.marca}, {self.color}, {self.precio}")

class coche_electrico(Coche):
    def __init__(self, marca, color,precio,autonomia):
        super().__init__(marca, color, precio)
        self.autonomia = autonomia

    def cargar(self):
        print(f"Cargando {self.autonomia} de autonomia")

coche1 = coche_electrico("Tesla", "Rojo", 100000, 100)
coche1.describir()
coche1.cargar()

coche2 = coche_electrico("Audi", "verde", 150000, 120)
coche2.describir()
