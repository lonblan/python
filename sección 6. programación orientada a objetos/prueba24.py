class Gaseosa:

    def __init__ (self, marca, sabor, dulzor):
        self.marca = marca
        self.sabor = sabor
        self.dulzor = dulzor

    def __str__(self):
        return("Marca: " + self.marca+". Sabor: " + self.sabor+". Dulzor: " + self.dulzor)

cocacola = Gaseosa("Femsa", "Original", "Medio")
tehatsu = Gaseosa("Postobón", "Toronja", "Alto")

print(cocacola)
print(tehatsu)
    
