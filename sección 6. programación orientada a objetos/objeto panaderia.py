class Pan:
    def __init__ (self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class Tarta:
    def __init__ (self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion



class Panaderia:
    def __init__ (self,panes = []):
        self.panes = panes


    def mostrar_panes(self):
        for pan in self.panes:
            print("Nombre: " + pan.nombre+". Precio: " + pan.precio+". Descripcion: " + pan.descripcion)


    def mostrar_tartas(self):
        for pan in self.panes:
            print("Nombre: " + pan.nombre+". Precio: " + pan.precio+". Descripcion: " + pan.descripcion)



pan_1 = Pan("croissant","4.600","de mantequilla")
pan_2 = Pan("deditodequeso", "5.678", "con queso costeño")
pan_3 = Pan("pasteldepollo", "7.890", "con pollo desmechado")


tarta_1 = Tarta("casera","7.600","con vainilla")
tarta_2 = Tarta("piña", "7.678", "piña dulce")
tarta_3 = Tarta("nuez", "7.890", "con nueces y almendras")


panes_de_sal = Panaderia(panes = [pan_1, pan_2, pan_3])
panes_de_sal.mostrar_panes()

tartas = Panaderia(panes = [tarta_1, tarta_2, tarta_3])
tartas.mostrar_tartas()













