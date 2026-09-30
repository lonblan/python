class Figura:
    def __init__(self, area_base, area_lateral):    
        self.area_base = area_base
        self.area_lateral = area_lateral

    def hallar_perimetro(self):
        return self.num_lados * self.longitud

    def area_total_piramide(self):
        return self.area_base + self.area_lateral

piramide = Figura(8, 30)
res=piramide.area_total_piramide()
print(res)