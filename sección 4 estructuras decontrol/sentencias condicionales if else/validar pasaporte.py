nombre = (input("Ingrese su nombre\n"))
edad = int(input("Ingrese su edad\n"))

if edad >= 18:
    pasaporte = input("¿Tiene pasaporte? (si/no): \n").lower()
    if pasaporte == "si":
        print("Puede trabajar en otro país.")
    else:
        print("No es posible trabajar en otro país.")
else:
    print("Debes de ser mayor de edad.")