class Pan:
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

pan_1 = Pan("croissant","4.600","de mantequilla")
pan_2 = Pan("deditodequeso", "5.678", "conquesocosteño")
pan_3 = Pan("pasteldepollo", "7.890", "conpollodesmechado")

panaderia_1 = Panaderia(panes = [pan_1, pan_2, pan_3])
panaderia_1.mostrar_panes()

