

libros = []


a = {"Titulo" : "El hombre y la tierra", "Año": "1897", "Autor" : "Joseph Startesd"}
b = {"Titulo" : "Cien años de soledad", "Año": "1987", "Autor" : "Gabriel Garcia Márque"}
c = {"Titulo" : "El dorado", "Año": "2005", "Autor" : "Steven thurdson"}

libros.append(a)
libros.append(b)
libros.append(c)

contador = 0

for libro in libros:
    if contador == 2:
        print(libro["Titulo"], libro["Año"], libro["Autor"])
    contador += 1






    
    
