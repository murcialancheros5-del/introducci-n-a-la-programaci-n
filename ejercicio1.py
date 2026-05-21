
velocidad = int(input("Ingrese velocidad registrada: "))
limite = int(input("Ingrese limite de velocidad: "))
tipo = input("Tipo de vehiculo (carro/moto/camion): ").lower()
alcoholemia = int(input("Nivel de alcoholemia (0-3): "))

if alcoholemia < 0 or alcoholemia > 3:
    print("Error: el nivel de alcoholemia debe estar entre 0 y 3")
else:
    multa = 0

   
    tiene_alcohol = alcoholemia > 0
    supera_limite = velocidad > limite

    if tiene_alcohol:
        multa = 1000000
        print("Multa: $", multa)
        print("Licencia suspendida")
    else:
        if not supera_limite:
            print("Felicitaciones, no tiene multa")
        else:
            exceso = velocidad - limite

            if exceso <= 20:
                multa = 300000
            else:
                multa = 600000

            if tipo == "camion":
                multa *= 2

            print("Multa: $", multa)