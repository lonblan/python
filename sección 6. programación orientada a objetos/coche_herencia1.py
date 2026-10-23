class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color


    def __str__(self):
        return f"El coche es un {self.marca} {self.modelo} de color {self.color}"

ford = Coche("Ford", "Mustang", "Verde")

print(ford.marca)
print(ford.modelo)
print(ford.color)
print(ford)

class CocheElectrico(Coche):
    def __init__(self, marca, modelo, color, bateria):
        super().__init__(marca, modelo, color)
        self.bateria = bateria

    def __str__(self):
        return f"El coche electrico es un {self.marca} {self.modelo} de color {self.color} con una bateria de {self.bateria} kWh"

tesla = CocheElectrico("Tesla", "Model S", "Blanco", 100)
print(tesla)