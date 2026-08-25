class Zapato:
    def __init__ (self, marca, color, precio, tallas):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.tallas = tallas

class Calzado:
    def __init__(self, zapatos = []):
        self.zapatos = zapatos


    def mostrar_zapatos(self):
        for zapato in self.zapatos:
            print("Marca: " + zapato.marca+". Color: " + zapato.color+". Precio: " + zapato.precio+". Tallas: " + zapato.tallas)


zapato_1 = Zapato("Nike", "Azul", "650.000", "34 35 36")
zapato_2 = Zapato("Nort Star", "verde", "610.000", "34 35 36 39")
zapato_3 = Zapato("Reebook", "blanco", "950.000", "33 37 36")

chancla_1 = Zapato("MIramar", "marron", "650.000", "34 35 36")
chancla_2 = Zapato("Still", "blanco", "610.000", "34 35 36 39")
chancla_3 = Zapato("Leonor", "Lila", "950.000", "33 37 36")


zapatos_lujozos = Calzado(zapatos = [zapato_1, zapato_2, zapato_3])
zapatos_lujozos.mostrar_zapatos()

chanclas_varias = Calzado(zapatos = [chancla_1, chancla_2, chancla_3])
chanclas_varias.mostrar_zapatos()





























