cantidad = int(input(" Ingrese la cantidad de productos:  "))
total = 0
for i in range ( 1, cantidad +1 ):
    precio = int (input (f"Ingrea el precio del producto {i}: $"))
    total = precio
    print("El total de los productos es: ", total)