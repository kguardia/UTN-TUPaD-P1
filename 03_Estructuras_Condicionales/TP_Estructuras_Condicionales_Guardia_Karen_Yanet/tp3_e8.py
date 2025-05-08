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
print("En este programa puede realizar cualquiera de las siguientes operaciones:")
print("1 - Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2 - Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3 - Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("Ingrese 1, 2 o 3 según la opción que desee: "))

# Si el usuario eligió la opción 1, imprimimos su nombre en mayúsculas
if opcion == 1:
    nombre_mayuscula = nombre.upper()
    print(nombre_mayuscula)
# Si el usuario eligió la opción 2, imprimimos su nombre en minúsculas
elif opcion == 2:
    nombre_minuscula = nombre.lower()
    print(nombre_minuscula)
# Si el usuario eligió la opción 3, imprimimos su nombre con la primera letra en mayúscula
elif opcion == 3:
    nombre_title = nombre.title()
    print(nombre_title)
# Si el usuario eligió otro número de opción, imprimimos "Por favor, ingrese únicamente 1, 2 o 3"
else:
    print("Por favor, ingrese únicamente 1, 2 o 3")

"""
Nota:
.upper(): convierte todo el texto a mayúsculas.

.lower(): convierte todo el texto a minúsculas.

.title(): pone la primera letra en mayúscula (y el resto en minúsculas).
"""