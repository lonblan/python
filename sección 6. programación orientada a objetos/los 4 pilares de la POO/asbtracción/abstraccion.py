# Abstracción: CuentaBancaria es la IDEA de una cuenta, no una cuenta real.
# En un banco no abres "una cuenta genérica": eliges ahorro o corriente.

from abc import ABC, abstractmethod  # Herramientas de Python para clases abstractas.


class CuentaBancaria(ABC):  # ABC = Abstract Base Class (clase base abstracta).

    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad):  # Esto SÍ está definido: todas depositan igual.
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")

    @abstractmethod
    def retirar(self, cantidad):
        # Aquí NO hay reglas. Solo el contrato:
        # "Toda cuenta debe saber retirar. Cada hija escribe CÓMO."
        pass

    def __str__(self):
        return f"Cuenta de {self.titular}, Saldo: {self._saldo}"


class CuentaAhorro(CuentaBancaria):

    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes

    def retirar(self, cantidad):  # Obligatorio: si no está, Python no deja crear la cuenta.
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
        elif cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("Saldo insuficiente.")

    def generar_intereses(self):
        intereses = self._saldo * self.tasa_interes
        self._saldo += intereses
        print(f"Intereses de {intereses}. Nuevo saldo: {self._saldo}")


class CuentaCorriente(CuentaBancaria):

    def __init__(self, titular, saldo_inicial, limite_descubierto):
        super().__init__(titular, saldo_inicial)
        self.limite_descubierto = limite_descubierto

    def retirar(self, cantidad):  # Misma orden, otra regla (descubierto).
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
            return

        saldo_despues = self._saldo - cantidad
        if saldo_despues >= -self.limite_descubierto:
            self._saldo = saldo_despues
            print(f"Retiro de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("No se puede retirar: se supera el límite de descubierto.")


# --- 1. Una cuenta genérica no existe ---
print("--- Intento 1: abrir una cuenta 'genérica' ---")
try:
    cuenta_generica = CuentaBancaria("Carlos Ruiz", 1000)
except TypeError:
    print("No se puede: CuentaBancaria es solo la idea. Hay que elegir ahorro o corriente.\n")

# --- 2. Las cuentas reales sí se pueden abrir ---
print("--- Intento 2: abrir cuentas concretas ---")
ahorro = CuentaAhorro("Juan Carlos Londono", 1000, 0.05)
corriente = CuentaCorriente("Ana Perez", 1000, 300)
print(ahorro)
print(corriente)
print()

# --- 3. Siguen entendiendo la misma orden (polimorfismo) ---
print("--- Misma orden para todas: retirar 1200 ---\n")
for cuenta in [ahorro, corriente]:
    print(cuenta)
    cuenta.retirar(1200)
    print()

# 4. Abstracción: mostrar QUÉ debe saber hacer una cuenta (depositar, retirar)
#    y ocultar el detalle de CÓMO lo hace cada tipo.
