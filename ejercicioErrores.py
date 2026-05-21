try:
    edad = int(input("Ingrese su edad:\n"))
    lenguaje = input("Ingrese su lenguaje de programacion (java/python)").capitalize()

    if edad >= 18:
        experiencia = int(input("Ingrese años de experiencia:"))
        
        if lenguaje =="Java" or lenguaje == "Python":
            if experiencia > 5:
                print("Eres senior, te pagaremos:" ,4000000)
            else:
                print("Eres junior, te pagaremos:",2500000)
        else:
            print("No es apto")
    else:
        print("Eres menor de edad")
except:
    print("Hubo un error")
finally:
    print("Finalizo el programa")