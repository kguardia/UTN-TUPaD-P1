"""
Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
"""
# Solicitar una frase o palabra al usuario
texto = input("Ingrese una frase o palabra: ")

# Verificar si termina en vocal (mayúscula o minúscula)
if texto[-1].lower() in 'aeiou':
    texto += '!'

# Mostrar el resultado
print(texto)