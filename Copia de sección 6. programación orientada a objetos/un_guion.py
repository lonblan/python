class  Persona:
    def __init__(self, nombre):
        self.__nombre_privado = nombre


p = Persona("Carlos")

print(p.__nombre_privado) # 