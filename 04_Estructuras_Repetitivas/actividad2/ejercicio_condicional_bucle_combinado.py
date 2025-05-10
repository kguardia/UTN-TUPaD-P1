sueldo_anual = 0
cont_meses = 1

print(f"Ingrese su sueldo para el mes nro {cont_meses}: ")
sueldo_mensual = float(input())

while cont_meses <= 11 and sueldo_mensual > 0:
    sueldo_anual += sueldo_mensual
    cont_meses += 1
    print(f"Ingrese su sueldo para el mes nro {cont_meses}: ")
    sueldo_mensual = float(input())

if sueldo_mensual > 0:
    sueldo_anual += sueldo_mensual

print(f"Tu sueldo anual es ${sueldo_anual}.")