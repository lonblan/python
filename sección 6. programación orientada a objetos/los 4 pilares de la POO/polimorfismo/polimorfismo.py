# Polimorfismo: la misma orden, distinto comportamiento según el tipo de cuenta.
# Las clases son las mismas de herencia_cuenta.py.

class CuentaBancaria:

    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")

    def retirar(self, cantidad):  # Regla del padre: no permite saldo negativo.
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
        elif cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("Saldo insuficiente.")

    def __str__(self):
        return f"Cuenta de {self.titular}, Saldo: {self._saldo}"


class CuentaAhorro(CuentaBancaria):

    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes

    def generar_intereses(self):
        intereses = self._saldo * self.tasa_interes
        self._saldo += intereses
        print(f"Intereses de {intereses}. Nuevo saldo: {self._saldo}")


class CuentaCorriente(CuentaBancaria):

    def __init__(self, titular, saldo_inicial, limite_descubierto):
        super().__init__(titular, saldo_inicial)
        self.limite_descubierto = limite_descubierto

    def retirar(self, cantidad):  # Misma orden "retirar", otra regla.
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
            return

        saldo_despues = self._saldo - cantidad
        if saldo_despues >= -self.limite_descubierto:
            self._saldo = saldo_despues
            print(f"Retiro de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("No se puede retirar: se supera el límite de descubierto.")


# Tres cuentas distintas, todas "son una" CuentaBancaria.
basica = CuentaBancaria("Carlos Ruiz", 1000)
ahorro = CuentaAhorro("Juan Carlos Londono", 1000, 0.05)
corriente = CuentaCorriente("Ana Perez", 1000, 300)

# Las metemos en la misma lista. No preguntamos de qué tipo es cada una.
cuentas = [basica, ahorro, corriente]

print("--- Misma orden para todas: retirar 1200 ---\n")

for cuenta in cuentas:
    print(cuenta)              # Cada una se presenta.
    cuenta.retirar(1200)      # Misma llamada. Cada una responde a su manera.
    print()

# 3. Polimorfismo: un mismo mensaje (retirar) produce un resultado distinto
#    según el objeto que lo recibe. No hace falta un if "si es ahorro... si es corriente...".
