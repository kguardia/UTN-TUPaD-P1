CORTE = "*"
NOMBRE_INVALIDO = "XXXXXXXXXXXXX"
edad_minima = float("inf")
nombre_mas_joven = NOMBRE_INVALIDO

nombre = input(f"Ingrese un nombre ({CORTE} para cortar): ")
while nombre != CORTE:
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    if edad < edad_minima:
        edad_minima = edad
        nombre_mas_joven = nombre
    nombre = input(f"Ingrese otro nombre ({CORTE} para cortar): ")

if nombre_mas_joven == NOMBRE_INVALIDO:
    print("No se ingresaron personas.")
else:
    print(f"La persona más joven ({edad_minima} años) es {nombre_mas_joven}.")