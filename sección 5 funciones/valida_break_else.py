
def validar(a,b):
    if a == b:
        return True
    else:
        return False
        
lista = [1,2,3,4,5]
b = int(input())

for numero in lista:
    if validar(numero, b):
        print("El número b está en la lista")
        break
else:
    print("El número b no está en la lista")
    