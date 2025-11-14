# En este caso, hacemos un programa sencillo donde despues de introducir los dos 
# números, la condicion que escribimos nos determinará el mensaje a enviar al usuario


print("Introduzca el primer número")
numero1 = input()

print("Introduzca el segundo nñumero")
numero2 = input()

if numero1 > numero2:
    print("El primer número es mayor que el segundo número")
else:
    print("El segundo número es mayor que el primero, o son iguales")