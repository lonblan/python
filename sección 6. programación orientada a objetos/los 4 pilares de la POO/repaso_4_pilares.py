# Repaso de los 4 pilares con otro ejemplo: empleados de una empresa.
# Encapsulamiento, herencia, polimorfismo y abstracción.

from abc import ABC, abstractmethod


# --- Abstracción: Empleado es la IDEA, no un empleado real. ---
# En una empresa no contratas "un empleado genérico": eliges fijo o por horas.
class Empleado(ABC):

    def __init__(self, nombre):
        self.nombre = nombre
        self._pago = 0  # Encapsulamiento: el pago está protegido (un guion bajo).

    def obtener_pago(self):  # Forma segura de consultar el pago, sin tocarlo directo.
        return self._pago

    @abstractmethod
    def calcular_pago(self):
        # Contrato: todo empleado DEBE saber calcular su pago.
        # Aquí no hay fórmula. Cada hija escribe CÓMO.
        pass

    def __str__(self):
        return f"{self.nombre}, pago: {self._pago}"


# --- Herencia: EmpleadoFijo ES UN Empleado. ---
class EmpleadoFijo(Empleado):

    def __init__(self, nombre, sueldo_mensual):
        super().__init__(nombre)  # El padre guarda el nombre y el pago inicial.
        self.sueldo_mensual = sueldo_mensual

    def calcular_pago(self):  # Obligatorio por ser abstracto en el padre.
        self._pago = self.sueldo_mensual
        print(f"{self.nombre} (fijo) cobra {self._pago} al mes.")


# --- Herencia: EmpleadoPorHoras ES UN Empleado. ---
class EmpleadoPorHoras(Empleado):

    def __init__(self, nombre, horas, precio_hora):
        super().__init__(nombre)
        self.horas = horas
        self.precio_hora = precio_hora

    def calcular_pago(self):  # Misma orden, otra fórmula.
        self._pago = self.horas * self.precio_hora
        print(f"{self.nombre} (por horas) cobra {self._pago} este mes.")


# --- 1. Abstracción: no se puede crear un empleado genérico ---
print("--- Intento 1: contratar un empleado 'genérico' ---")
try:
    generico = Empleado("Carlos Ruiz")
except TypeError:
    print("No se puede: Empleado es solo la idea. Hay que elegir fijo o por horas.\n")

# --- 2. Cuentas concretas (aquí: empleados concretos) ---
print("--- Intento 2: contratar empleados concretos ---")
ana = EmpleadoFijo("Ana Perez", 2000)
juan = EmpleadoPorHoras("Juan Carlos Londono", 80, 15)
print(ana)
print(juan)
print()

# --- 3. Polimorfismo: la misma orden, distinto resultado ---
print("--- Misma orden para todos: calcular_pago ---\n")
nomina = [ana, juan]

for empleado in nomina:
    empleado.calcular_pago()  # No preguntamos "¿tú eres fijo o por horas?"
    print(f"Consulta segura del pago: {empleado.obtener_pago()}")
    print()

# Encapsulamiento: el pago se consulta con obtener_pago(), no se cambia a mano.
# Herencia: fijo y por horas reutilizan nombre y _pago del padre.
# Polimorfismo: calcular_pago() responde distinto según el tipo.
# Abstracción: Empleado es el plano; no se puede contratar "a medias".
