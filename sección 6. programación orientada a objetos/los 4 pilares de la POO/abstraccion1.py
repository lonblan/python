
# Online Python - IDE, Editor, Compiler, Interpreter

from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial
        
    @abstractmethod
    def retirar(self, cantidad):
        # Aquí NO hay reglas. Solo el contrato:
        # "Toda cuenta debe saber retirar. Cada hija escribe CÓMO."
        pass
    
    def __str__(self):
        return f"Cuenta de {self.titular}. Saldo : {self._saldo}"
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Deposito de {cantidad} Nuevo saldo {self._saldo}")
        else:
            print("La cantidad debe ser mayor a cero")
            
class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular,saldo_inicial)
        self.interes = tasa_interes
        
    def retirar(self, cantidad):  # Obligatorio: si no está, Python no deja crear la cuenta.
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
        elif cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro de {cantidad}. Nuevo saldo: {self._saldo}")
        else:
            print("Saldo insuficiente.")
        
ahorro = CuentaAhorros("Juan", 30.000, 0.05)
print(ahorro)
ahorro.depositar(50.000)
ahorro.retirar(25.000)
        
        
            
            
            
            
            
            
    
            
            
            
    
