# Herencia + super(): la hija reutiliza al padre y puede cambiar un método.

# Clase padre: lo que todas las cuentas tienen en común.
class CuentaBancaria:

    def __init__(self, titular, saldo_inicial):  # Constructor de la clase padre.
        self.titular = titular  # Atributo público.
        self._saldo = saldo_inicial  # Atributo protegido (un guion bajo).

    def depositar(self, cantidad):  # Método para depositar dinero.
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")

    def retirar(self, cantidad):  # Método del padre: no permite saldo negativo.
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
        elif cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("Saldo insuficiente.")

    def obtener_saldo(self):
        return self._saldo

    def __str__(self):
        return f"Cuenta de {self.titular}, Saldo: {self._saldo}"


# Clase hija: CuentaAhorro ES UNA CuentaBancaria, y además genera intereses.
class CuentaAhorro(CuentaBancaria):

    def __init__(self, titular, saldo_inicial, tasa_interes):
        # super() llama al constructor del padre.
        # Así no repetimos titular y saldo: el padre ya sabe crearlos.
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes  # Lo propio de esta hija.

    def generar_intereses(self):  # Método nuevo, solo de la cuenta de ahorro.
        intereses = self._saldo * self.tasa_interes
        self._saldo += intereses
        print(f"Intereses de {intereses}. Nuevo saldo: {self._saldo}")


# Clase hija: CuentaCorriente ES UNA CuentaBancaria, y permite un descubierto.
class CuentaCorriente(CuentaBancaria):

    def __init__(self, titular, saldo_inicial, limite_descubierto):
        super().__init__(titular, saldo_inicial)  # Reutiliza al padre.
        self.limite_descubierto = limite_descubierto  # Lo propio de esta hija.

    def retirar(self, cantidad):  # CAMBIA el método del padre (se llama override).
        # La hija decide otra regla: se puede retirar más del saldo,
        # siempre que no se pase del límite de descubierto.
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
            return

        saldo_despues = self._saldo - cantidad
        if saldo_despues >= -self.limite_descubierto:
            self._saldo = saldo_despues
            print(f"Retiro de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("No se puede retirar: se supera el límite de descubierto.")


# --- Prueba: cuenta de ahorro hereda depositar/retirar y añade intereses ---
print("--- Cuenta de ahorro ---")
deposito = CuentaAhorro("Juan Carlos Londono", 1000, 0.05)
print(deposito)                 # Viene del padre (__str__).
deposito.depositar(500)         # Método heredado del padre.
deposito.generar_intereses()    # Método propio de la hija.
deposito.retirar(200)           # Método heredado del padre (sin cambios).
print(deposito)

# --- Prueba: cuenta corriente CAMBIA retirar ---
print("\n--- Cuenta corriente ---")
corriente = CuentaCorriente("Ana Perez", 1000, 300)
print(corriente)
corriente.retirar(1200)       # El padre diría "saldo insuficiente".
                              # La hija lo permite: 1000 - 1200 = -200 (dentro del límite 300).
corriente.retirar(200)        # Esto sí lo rechaza: -200 - 200 = -400 (pasa el límite).
print(corriente)