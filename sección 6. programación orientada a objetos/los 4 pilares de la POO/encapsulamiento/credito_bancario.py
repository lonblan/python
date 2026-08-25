class CreditoBancario: # Clase CreditoBancario.

    def __init__(self, saldo_inicial, tasa_interes, cuota_mensual): # Constructor de la clase.
        self.saldo_inicial = saldo_inicial # Atributo público.
        self.__tasa_interes = tasa_interes # Atributo público.
        self.cuota_mensual = cuota_mensual # Atributo público.

    def calcular_interes(self): # Método para calcular el interés.
        return self.saldo_inicial * self.__tasa_interes # Se retorna el interés.

    def calcular_cuota_mensual(self): # Método para calcular la cuota mensual.
        return self.saldo_inicial / self.cuota_mensual # Se retorna la cuota mensual.

    def calcular_saldo_final(self): # Método para calcular el saldo final.
        return self.saldo_inicial + self.calcular_interes() - self.calcular_cuota_mensual() # Se retorna el saldo final.

mi_Credito = CreditoBancario(1000, 0.05, 100) # Se crea una instancia de la clase CreditoBancario.
print(mi_Credito.calcular_interes()) # Se imprime el interés.
print(mi_Credito.calcular_cuota_mensual()) # Se imprime la cuota mensual.
print(mi_Credito.calcular_saldo_final()) # Se imprime el saldo final.

credito_juan = CreditoBancario(10000, 0.06, 50) # Se crea una instancia de la clase CreditoBancario.
print(credito_juan.calcular_interes()) # Se imprime el interés.
print(credito_juan.calcular_cuota_mensual()) # Se imprime la cuota mensual.
print(credito_juan.calcular_saldo_final()) # Se imprime el saldo final.
print(credito_juan.__tasa_interes) # Se imprime la tasa de interés.






