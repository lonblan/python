print("Bienvenido al menú\n")
while True:
    print("Escriba una opcion:\n 1. Comparar dos números  \n 2. Introducir un número impar \n 3. Terminar Programa\n ")
    opcion = input()
    if opcion == "1":
        print("Introduzca un número")
        a = int(input())
        print("Introduzca otro número")
        b = int(input())
        if a == b:
            print("\ a es igual a b\n")
        elif a > b:
            print("\na es mayor que b\n")
        else:
            print("\nb es mayor que a\n")
            
    elif opcion == "2":
        print("Introduzca un número")
        a = int(input())
        while a % 2 == 0:
             print("\nNúmero par, introduzca otro número\n")
             a = int(input())
        print("\na es impar\n")
    elif opcion == "3":
        break
    else:
        print("Opcion incorrecta")
        
print("Programa terminado")
        
    
       

