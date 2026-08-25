class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def subir_salario(self, porcentaje):
        self.salario += self.salario * porcentaje / 100


gerente = Empleado("Carlos", 100000.000)
gerente.subir_salario(20)
print(gerente.salario)
