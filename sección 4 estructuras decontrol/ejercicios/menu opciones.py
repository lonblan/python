
# Menú de opciones

print("Bienvenido al menú\n")

# Bucle infinito para mostrar el menú hasta que el usuario decida terminar
while True:
    print("Escriba una opcion:\n 1. Comparar dos números \n 2. Introducir un número impar \n 3. Terminar programa\n")
    opcion = input()
    if opcion == "1":
# Opción 1: Comparar dos números
        
        print("Introduzca un número:")
        a = int(input())
        print("Introduzca otro número")
        b = int(input())
        if a == b:
            print("Los números son iguales")
        elif a > b:
            print(f"El número {a} es mayor que {b}")
        else:
            print(f"El número {b} es mayor que el número {a}")

# Opción 2: Introducir un número impar

    elif opcion == "2":
        print("Introduzca un número impar:")
        num = int(input())
        if num % 2 == 0:
            print(f"El número {num} es par")
        else:
            print(f"El número {num} es impar") 

    elif opcion == "3":
        print("Programa terminado")

# Salir del bucle y terminar el programa
        break



        
    
        
        