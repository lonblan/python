def multiplicar(a,b):
    return a * b
    
def dividir(a,b):
    return a / b

def sumar(a,b):
    return a + b
    
def restar(a,b):
    return a - b
    
print("Introduzca un número")
numero1 = int(input())
print("Introduzca otro número")
numero2 = int(input())

while True:
    print("Menú")
    print("Elija la opción para operar\n1. multiplicar\n2. dividir\n3. sumar\n4. restar\n5. apagar la calculadora ")
    opcion = input()
    if opcion == "1":
        resultado = multiplicar(numero1, numero2)
        print(resultado)
        break
    
    elif opcion == "2":
        resultado = dividir(numero1, numero2)
        print(resultado)
        break
    
    elif opcion == "3":
        resultado = sumar(numero1, numero2)
        print(resultado)
        break
    
    elif opcion == "4":
        resultado = restar(numero1, numero2)
        print(resultado)
        break
    
    elif opcion == "5":
        print("Apagando la calculadora")
        
    else:
        print("opcion Incorrecta")
    
    
    
    




