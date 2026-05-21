for i in "Hola":
    print(i)

print (" ---------")
for i in range(11):
    print(i)

    print (" ---------")

numero = int(input("Ingrese un numero: "))
for i in range (0,20,2):
    print(i)

print("===WHILE===")

num_final = int(input("Ingrese un numero : "))

contador = 100
while ( contador > 0):
    print(contador)
    contador -= 1

print("Tablas de multiplicar")

multiplicar = int(input("Ingrese el numero de tabla a generar:"))
for i in  range (11):
    res = multiplicar * i
    print(f"{multiplicar} X {i} = {res}")



