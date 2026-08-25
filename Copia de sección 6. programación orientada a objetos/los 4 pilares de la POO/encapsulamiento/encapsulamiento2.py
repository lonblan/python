class CuentaBancaria: # Clase CuentaBancaria.

    def __init__(self, titular, saldo_inicial): # Constructor de la clase.
        self.titular = titular # Atributo público.
        self._saldo = saldo_inicial  # El guion bajo indica que el atributo es privado. Está protegido.

    def depositar(self, cantidad): # Método para depositar dinero.
        if cantidad > 0: # Si la cantidad es mayor a 0, se deposita el dinero.
            self._saldo += cantidad # Se deposita el dinero.
            print(f"Deposito de {cantidad} realizado. Nuevo saldo: {self._saldo}") # Se imprime el nuevo saldo.
        else:  # Si la cantidad es menor a 0, se imprime un mensaje de error.
            print("La cantidad a depositar debe ser mayor a 0.")  # Se imprime un mensaje de error.
            
    def retirar(self, cantidad): # Método para retirar dinero.
        if cantidad > 0: # Si la cantidad es mayor a 0, se retira el dinero.
            if cantidad <= self._saldo: # Si la cantidad es menor o igual al saldo, se retira el dinero.
                self._saldo -= cantidad # Se retira el dinero.
                print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self._saldo}") # Se imprime el nuevo saldo.
            else: # Si la cantidad es mayor al saldo, se imprime un mensaje de error.
                print("Saldo insuficiente.") # Se imprime un mensaje de error.
        else: # Si la cantidad es menor a 0, se imprime un mensaje de error.
            print("La cantidad a retirar debe ser mayor a 0.") # Se imprime un mensaje de error.

    def obtener_saldo(self): # Método para obtener el saldo.
        return self._saldo # Se retorna el saldo.
    
    def obtener_titular(self): # Método para obtener el titular.
        return self.titular # Se retorna el titular.
    
    def obtener_detalles(self): # Método para obtener los detalles de la cuenta.
        return f"Titular: {self.titular}, Saldo: {self._saldo}" # Se retorna los detalles de la cuenta.
    
    def __str__(self): # Método para imprimir la cuenta.
        return f"Cuenta de {self.titular}, Saldo: {self._saldo}" # Se retorna la cuenta.


cuenta1 = CuentaBancaria("Juan Carlos Londono", 1000) # Se crea una instancia de la clase CuentaBancaria.
print(cuenta1)
cuenta1.depositar(500) # Se deposita 500 en la cuenta.
cuenta1.retirar(200)    # Se retira 200 de la cuenta.
print(cuenta1.obtener_saldo())  # Se imprime el saldo de la cuenta.
print(cuenta1.obtener_titular())    # Se imprime el titular de la cuenta.
print(cuenta1.obtener_detalles())   # Se imprime los detalles de la cuenta.



 # 1. Encapsulamiento: Es el proceso de ocultar los detalles de la implementación de una clase y exponer solo la interfaz pública.





