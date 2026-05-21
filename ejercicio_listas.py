print("--- CALCULADORA DESCUENTOS---")
precio1 = float(input("Ingrese el valor libro"))
precio2 = float(input("Ingrese el valos de la libreta"))
precio3 = float(input("Ingrese el valos de los colores"))

precios = [ precio1, precio2, precio3]

respuesta = input("Eres estudiante? (SI/NO )"). upper()

if respuesta == "SI":
    es_estudiante = True
else:
    es_estudiante = False

subtotal = sum(precios)


descuento = 0.0 

if subtotal > 50 and es_estudiante:
    descuento = subtotal * 0.20 #20%
elif subtotal > 50 and es_estudiante == False:
    descuento = subtotal * 0.10
else:
    descuento = 0 

total = subtotal - descuento

print ("---TICKET COMPRA---")
print ("Subtotal $", subtotal)
print (f" Descuento aplicado: $ {descuento}")
print ("Total a pagar: $, total")
