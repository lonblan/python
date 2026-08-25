from abc import ABC, abstractmethod

# 1. Definimos la clase abstracta (el "contrato")
class SistemaPago(ABC):
    
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass  # No tiene implementación aquí, las hijas obligatoriamente deben implementarlo

# 2. Clases concretas que heredan de la abstracción
class TarjetaCredito(SistemaPago):
    def procesar_pago(self, cantidad):
        # Aquí iría la lógica compleja de conexión con el banco
        print(f"Pagando ${cantidad} usando Tarjeta de Crédito.")

class PayPal(SistemaPago):
    def procesar_pago(self, cantidad):
        # Lógica específica de PayPal
        print(f"Pagando ${cantidad} usando PayPal.")

# --- Uso ---
# Si intentaras hacer: pago = SistemaPago(), Python daría un error porque
# no se pueden instanciar clases abstractas directamente.

# Usamos las clases concretas:
pagos = [TarjetaCredito(), PayPal()]

for funcion in pagos:
    funcion.procesar_pago(100)