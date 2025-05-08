"""
Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
Periodo del año                                                | Estación en el hemisferio norte | Estación en el hemisferio sur
Desde el 21 de diciembre hasta el 20 de marzo (incluidos)      | Invierno                        | Verano
Desde el 21 de marzo hasta el 20 de junio (incluidos)          | Primavera                       | Otoño
Desde el 21 de junio hasta el 20 de septiembre (incluidos)     | Verano                          | Invierno
Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) | Otoño                           |Primavera
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
"""
# Pedimos al usuario que ingrese el hemisferio
hemisferio = input("Por favor, ingrese el hemisferio (N/S): ")
# Estandarizamos la respuesta del usuario convirtiéndola en minúscula
hemisferio = hemisferio.lower()

# Pedimos al usuario que ingrese el mes del año
mes = int(input("Por favor, ingrese el mes del año en números: "))

# Pedimos al usuario que ingrese el día del mes
dia = int(input("Por favor, ingrese el día del mes en números: "))

# Hacemos un condicional anidado, primero colocamos todo lo relativo al hemisferio sur
if hemisferio == "s":
    # Si es después del 21/12, en cualquier momento de enero o febrero, o antes del 20/3 imprimimos "Verano"
    if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
        print("Verano")
# Si es después del 21/3, en cualquier momento de abril o mayo, o antes del 20/6 imprimimos "Otoño"
    elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
        print("Otoño")
# Si es después del 21/6, en cualquier momento de julio o agosto, o antes del 20/9 imprimimos "Invierno"
    elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
        print("Invierno")
# Si es después del 21/9, en cualquier momento de octubre o noviembre, o antes del 20/12 imprimimos "Primavera"
    elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
        print("Primavera")
# Luego colocamos lo relativo al hemisferio norte
elif hemisferio == "n":
    # Si es después del 21/12, en cualquier momento de enero o febrero, o antes del 20/3 imprimimos "Invierno"
    if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
        print("Invierno")
    # Si es después del 21/3, en cualquier momento de abril o mayo, o antes del 20/6 imprimimos "Primavera"
    elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
        print("Primavera")
    # Si es después del 21/6, en cualquier momento de julio o agosto, o antes del 20/9 imprimimos "Verano"
    elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
        print("Verano")
    # Si es después del 21/9, en cualquier momento de octubre o noviembre, o antes del 20/12 imprimimos "Otoño"
    elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
        print("Otoño")