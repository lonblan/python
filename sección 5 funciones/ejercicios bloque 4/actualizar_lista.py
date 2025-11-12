
def multiplicar(a):
    for index,numero in enumerate(a):
        a[index] *= 2
    return a
        
lista = [5,23,56,4,8]

resultado = multiplicar(lista)

print(resultado)
