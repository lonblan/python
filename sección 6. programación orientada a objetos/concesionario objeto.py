
class Coche:
    def __init__ (self, marca, color, motor):
        self.marca = marca
        self.motor = motor
        self.color = color
        
        
    def __str__(self):
        return("Marca: " + self.marca+". Color: " + self.color+". Motor: " + self.motor)
        
class Concesionario:
    def __init__(self,coches =[]):
        self.coches = coches
    
    def mostrar_coches(self):
        for auto in self.coches:
            print("Marca: " + auto.marca+". Color: " + auto.color+". Motor: " + auto.motor)
            
coche_1 = Coche("audi","rojo","gasolina")
coche_2 = Coche("ford","naranja","acpm")
coche_3 = Coche("mazda","verde","gas")

concesionario_1 = Concesionario(coches = [coche_1,coche_2,coche_3])
concesionario_1.mostrar_coches()





        
            
