# Ejercicio operacions 
print("===Ejercicio de calculos===")
total_cuenta = float(input("ingrese el valor de la cuenta"))
porcentaje = int(input("Ingrese un valor para propina (Ej: 10)"))

monto_propina = total_cuenta * (porcentaje/ 100) # porcetanje en decimales 
total_pago = total_cuenta + monto_propina

print("El total a pagar es:",total_pago)