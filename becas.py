promedio = float(input("Ingrese su promedio: "))
deporte = input ("Realizas deporte: ").upper() 

deporte = (deporte == "SI")
beca = promedio >= 4.5 or (deporte and promedio >= 4.0)

if beca: 
    resultado = "SI"
else:
    resultado = "NO"

if promedio > 4.5:
    print("Nota superior")
elif promedio > 4.0:
    print("Nota alta")
elif promedio > 3.0:
    print("Nota aceptable")
else:
    print("Reprobo")

print ("El resultado es:", resultado)




