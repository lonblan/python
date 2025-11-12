nombre = "Ana"
edad = 28

if nombre == "Carlos" and edad == 28:
    print("Se llama Carlos y tiene 28 años")
elif nombre != "Carlos" and edad == 28:
    print("No se llama Carlos, pero si tiene 28 años")
elif nombre == "Carlos" and edad != 28:
    print("Se llama Carlos, pero no tine 28 años")
else:
    print("No se llama Carlos ni tiene 28 años")
    