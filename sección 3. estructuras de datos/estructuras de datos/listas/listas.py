a = [6, 18, "Carlos", 8, 43]

print(a)
print(a[2])
print(a[2:4])

b = [3, 45,8]
c = (a + b)

print(c)

a[2] = "Hola"

print(a)

a.append("adios")

print(a)
print(4 in a)
print(18 in a)
print(5 not in b)