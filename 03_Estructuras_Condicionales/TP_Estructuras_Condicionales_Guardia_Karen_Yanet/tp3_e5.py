"""
Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
"""
# Solicitar una contraseña al usuario
contrasena = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

# Verificar la longitud de la contraseña
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

"""
NOTA: len(contrasena) calcula cuántos caracteres tiene la contraseña.
"""