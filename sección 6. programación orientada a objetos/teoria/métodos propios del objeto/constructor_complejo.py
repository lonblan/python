class Coche:
    pass

    def __init__(self, marca, color, motor):
        self.marca = marca
        self.color = color
        self.motor = motor

    def __str__(self):
        return ("Marca: " +self.marca+" Color: "+self.color+ " Motor: " +self.motor)

coche_1 = Coche("Ford", "Verd", "Gasolina")

print(coche_1)
