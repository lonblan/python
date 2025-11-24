
# Iniciamos imprimiendo un mensaje de bienvenida.El cual estará fuera del bucle.
print("Bienvenido al menú\n")

# Con while True iniciamos el bucle que mostrará las opciones del menú hasta que el usuario decida terminar el programa.
while True:

# Mostramos las opciones del menú y solicitamos al usuario que elija una opción.

    print("Escriba una opcion:\n 1. Comparar dos números \n 2. Introducir un número impar \n 3. Terminar programa\n")

# Leemos la opción elegida por el usuario.

    opcion = input()

# Usamos una estructura condicional para ejecutar la acción correspondiente según la opción elegida.
    if opcion == "1":

# Solicitamos al usuario que introduzca dos números.
        print("Introduzca un número:")
        a = int(input())
        print("Introduzca otro número")
        b = int(input())

# Comparamos los dos números e imprimimos el resultado.
        if a == b:
            print("Los números son iguales")
        elif a > b:
            print(f"El número {a} es mayor que el número {b}")
        else:
            print(f"El número {b} es mayor que el número {a}")

# Si la opción es 2, solicitamos al usuario que introduzca un número impar y verificamos si es impar o par.

    elif opcion == "2":
        print("Introduzca un número impar:")
        num = int(input())
        if num % 2 == 0:
            print(f"El número {num} es par")
        else:
            print(f"El número {num} es impar")

# Si la opción es 3, imprimimos un mensaje de despedida y terminamos el programa usando break. 

    elif opcion == "3":
        print("Programa terminado")

# Usamos break para salir del bucle y terminar el programa.
        break
        
    



        
    
        
        