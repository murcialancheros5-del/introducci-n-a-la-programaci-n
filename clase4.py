try:
    nombre = input("Ingrese su nombre:").capitalize()
    edad = int(input("Ingrese su edad"))

    if nombre =="Admin" and edad >=18:

        password = input("Ingrese su contraseña:")

        if password == "Cesde2026":
            print("Acceso condedido")
        else:
            print("contraseña incorrecta")

    else:
        print("Usuario incorrecto")
except ValueError as e:
    print ("Se ingreso texto en un campo numero", e)
except KeyboardInterrupt as e:
    print("El usuario detuvo el programa ")
except:
    print("Ocurrio un error desconocido")
finally:
    print("Se acabo el programa")
    