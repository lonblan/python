class Coche:
    pass

    def __init__(self, marca, color, motor):
        self.marca = marca
        self.color = color
        self.motor = motor

coche_1 = Coche("Ford","amarillo","Gasolina")

print(coche_1.motor, coche_1.color)
