class Coche:
    def __init__(self,marca, color, motor):
        self.marca = marca
        self.color = color
        self.motor = motor

    def __str__(self):
        return("Marca: " + self.marca + ". Color: " + self.color + ". Motor: " + self.motor)

coche1 = Coche("Ford", "Verde", "Gasolina")
print(coche1)
