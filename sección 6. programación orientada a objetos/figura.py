class Figura:
    def __init__(self, num_lados, longitud ):
        self.num_lados = num_lados
        self.longitud = longitud

    def hallar_perimetro(self):
        return self.num_lados * self.longitud

    def area_total_piramide(self):
        return self.num_lados * self.longitud * self.longitud / 2


piramide = Figura(4, 10)
print(piramide.hallar_perimetro())
print(piramide.area_total_piramide())

