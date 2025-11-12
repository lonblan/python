print("Ingrese su nombre:")
nombre = input()
print("Ingrese su edad:")
edad = int(input())

if edad >= 18:
    pasaporte = input("Tiene pasaporte (si)/no)?\n").lower()
    if pasaporte == "si":
        print("Usted puede viajar al exterior")
    else:
        print("No puede viajar al exterior")
else:
    print("Debes tener más de 18 años")

    
    
    