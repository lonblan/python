class Coche:
    def __init__(self, marca, color, motor):
        self.marca = marca
        self.color = color
        self.motor = motor

    def __str__(self):
        return("Marca: " + self.marca + ". Color: " + self.color + ". Motor: " + self.motor)

class Concesionario:
    def __init__(self, coches = []):
        self.coches = coches


    def mostrarCoches(self):
        for coche in self.coches:
            print("Marca "+ coche.marca+ " Color " +coche.color+ " Motor " +coche.motor)

coche1 = Coche("Ford", "Azul", "Diesel")
coche2 = Coche("Audi", "Naranja","Gasolina")
coche3 = Coche("Mercedes", "Blanco","Eléctrico")

concesionario1 = Concesionario(coches = [coche1, coche2, coche3])
concesionario1.mostrarCoches()



