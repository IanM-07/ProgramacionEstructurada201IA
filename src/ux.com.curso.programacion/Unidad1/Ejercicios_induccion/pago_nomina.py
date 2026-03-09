#Ejercicio de pago de nomina

numero_horas = float (input("Ingrese el numero de horas trabajadas: "))
tarifa_horas = float (input("Ingrese la tarifa por horas: "))
nombre_empleado = input("Ingrese el nombre dle empleado: ")

#las horas superiores a 35 se pagan como extra
if numero_horas > 35:
    horas_extra = numero_horas -35
    pago_bruto = (35* tarifa_horas) + (horas_extra * tarifa_horas * 1.5)
else:
    pago_bruto = numero_horas * tarifa_horas

#calculo de impuestos
if pago_bruto <= 2000:
    impuesto = 0
elif pago_bruto <= 2220:
    impuesto = (pago_bruto - 2000) * 0.20
else:
    impuesto = (pago_bruto - 2220) * 0.30 + 220 * 0.20

pago_neto = pago_bruto - impuesto

#Mostrar resultados
print(f"Empleado: {nombre_empleado}")
print(f"Pago Bruto: ${pago_bruto:.2f}")
print(f"Impuesto: ${impuesto:.2f}")
print(f"Pago neto: ${pago_neto:.2f}")