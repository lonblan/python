class Coche :
    def __init__(self, marca, modelo): # Método
        self.marca = marca  # Atributo
        self.modelo = modelo

    
        
miCoche = Coche("Toyota", "Corolla")

print(f"MiCoche es un {miCoche.marca} {miCoche.modelo}")

