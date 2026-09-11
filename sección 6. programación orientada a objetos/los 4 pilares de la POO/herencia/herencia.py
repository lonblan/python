# Clase padre: lo que todos los animales tienen en común
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")


# Clase hija: Perro hereda de Animal
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")


# Clase hija: Gato hereda de Animal
class Gato(Animal):
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")


# Creamos objetos
mi_perro = Perro("Max")
mi_gato = Gato("Luna")

# Lo que heredan del padre
mi_perro.comer()      # Max está comiendo.
mi_gato.dormir()      # Luna está durmiendo.

# Lo que cada uno tiene de propio
mi_perro.ladrar()     # Max dice: ¡Guau!
mi_gato.maullar()     # Luna dice: ¡Miau!