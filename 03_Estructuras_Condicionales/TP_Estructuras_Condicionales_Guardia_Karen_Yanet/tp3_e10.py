"""
Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
Periodo del año                                                | Estación en el hemisferio norte | Estación en el hemisferio sur
Desde el 21 de diciembre hasta el 20 de marzo (incluidos)      | Invierno                        | Verano
Desde el 21 de marzo hasta el 20 de junio (incluidos)          | Primavera                       | Otoño
Desde el 21 de junio hasta el 20 de septiembre (incluidos)     | Verano                          | Invierno
Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) | Otoño                           |Primavera
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
"""
# Solicitar datos al usuario
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

# Calcular el día del año (sin considerar años bisiestos)
dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dia_del_anio = sum(dias_por_mes[:mes]) + dia

# Determinar estación según el hemisferio
if hemisferio == "N":
    if dia_del_anio >= 355 or dia_del_anio <= 79:
        estacion = "Invierno"
    elif 80 <= dia_del_anio <= 172:
        estacion = "Primavera"
    elif 173 <= dia_del_anio <= 266:
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif hemisferio == "S":
    if dia_del_anio >= 355 or dia_del_anio <= 79:
        estacion = "Verano"
    elif 80 <= dia_del_anio <= 172:
        estacion = "Otoño"
    elif 173 <= dia_del_anio <= 266:
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

# Mostrar el resultado
print("Estación del año:", estacion)