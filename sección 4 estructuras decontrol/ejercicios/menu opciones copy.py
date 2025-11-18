
# Online Python - IDE, Editor, Compiler, Interpreter

print("Bienvenido al menú\n")
while True:
    print("Escriba una opcion:\n 1. Comparar dos números \n 2. Introducir un número impar \n 3. Terminar programa\n")
    opcion = input()
    if opcion == "1":
        print("Introduzca un número:")
        a = int(input())
        print("Introduzca otro número")
        b = int(input())
        if a == b:
            print("Los números son iguales")
        elif a > b:
            print(f"El número {a} es mayor que {b}")
        else:
            print(f"El número {b} es mayor que {a}")

    elif opcion == "2":
        print("Introduzca un número impar:")
        num = int(input())
        if num % 2 == 0:
            print(f"El número {num} es par")
        else:
            print(f"El número {num} es impar") 

    elif opcion == "3":
        print("Programa terminado")
        break



        
    
        
        