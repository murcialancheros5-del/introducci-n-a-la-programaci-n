esAdmin = False
tiene_tarjeta = True
tiene_huella = True 

if esAdmin or (tiene_huella and tiene_tarjeta):
    print("Acceso concedido")
else:
    print("Acceso denegado")