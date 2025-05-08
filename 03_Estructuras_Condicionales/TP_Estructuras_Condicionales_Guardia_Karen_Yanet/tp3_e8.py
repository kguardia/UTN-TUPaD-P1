"""
Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""
# Solicitar el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Solicitar la opción deseada
print("Seleccione una opción:")
print("1 - Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2 - Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3 - Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = input("Ingrese 1, 2 o 3 según la opción que desee: ")

# Aplicar la transformación según la opción elegida
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")

"""
Nota:
.upper(): convierte todo el texto a mayúsculas.

.lower(): convierte todo el texto a minúsculas.

.title(): pone la primera letra en mayúscula (y el resto en minúsculas).
"""