
# Online Python - IDE, Editor, Compiler, Interpreter

class Coche:
    pass

    def __init__ (self, marca, motor, color):
        self.marca = marca
        self.motor = motor
        self.color = color
        
        
    def __str__(self):
        return(" marca "+self.marca+" color " + self.color + " motor " +self.motor)
        
            
coche_1 = Coche("audi", "gasolina", "verde")

print(coche_1)