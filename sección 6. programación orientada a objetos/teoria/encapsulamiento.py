class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado (encapsulado)

    # Método "getter" para consultar el saldo de forma segura
    def obtener_saldo(self):
        return self.__saldo

    # Método para depositar dinero (controlando que sea válido)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a cero.")

    # Método para retirar dinero (con validación de fondos)
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Saldo restante: ${self.__saldo}")
        else:
            print("Fondos insuficientes o cantidad no válida.")

# --- Uso del ejemplo ---
mi_cuenta = CuentaBancaria("Ana", 500)

# 1. Podemos consultar el saldo usando el método autorizado:
print(f"Titular: {mi_cuenta.titular}")
print(f"Saldo actual: ${mi_cuenta.obtener_saldo()}")

# 2. Realizamos operaciones controladas:
mi_cuenta.depositar(200)
mi_cuenta.retirar(100)

# 3. ¿Qué pasa si intentamos acceder al saldo privado directamente?
# Esto daría un error (AttributeError):
# print(mi_cuenta.__saldo) 

# El encapsulamiento protege el dato y fuerza a usar las reglas definidas en la clase.