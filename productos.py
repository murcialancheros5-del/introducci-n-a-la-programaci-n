
nombres_productos = []
cantidades_stock = []


cantidad = int(input("¿Cuántos productos desea registrar?: "))


for i in range(cantidad):
    print(f"\nProducto #{i + 1}")

    nombre = input("Nombre del producto: ")
    stock = int(input("Cantidad en stock: "))

    nombres_productos.append(nombre)
    cantidades_stock.append(stock)

print("\n--- REPORTE DE STOCK ---")

# Evaluar stock
for i in range(cantidad):
    nombre = nombres_productos[i]
    stock = cantidades_stock[i]

    if stock == 0:
        print(f"{nombre}: CRÍTICO")

    elif stock < 5:
        print(f"ALERTA -> {nombre} stock bajo ({stock})")

    elif stock > 20:
        print(f"{nombre}: Stock excedente")

    else:
        print(f"{nombre}: Stock saludable")

# Total de productos
print(f"\nTotal de productos: {cantidad}")

# Promedio del stock
promedio = sum(cantidades_stock) / cantidad

print(f"Promedio del stock: {promedio:.end=f}")
