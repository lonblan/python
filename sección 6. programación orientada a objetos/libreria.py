



class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio


class Libreria:
    def __init__(self, libros=[]):
        self.libros = libros

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.titulo)

    def vender_libro(self, titulo):
        for index, libro in enumerate(self.libros):
            if libro.titulo == titulo:
                del(self.libros[index])
                print(f"Se ha vendido el libro {titulo}")
                return
        print(f"El libro {titulo} no se encuentra en la libreria")

libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 10.00)
libro2 = Libro("1984", "George Orwell", 14.00)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 20.00)

libreria = Libreria([libro1, libro2, libro3])

libreria.mostrar_libros()
libreria.vender_libro("principitp")
libreria.vender_libro("Cien años de soledad")





        

