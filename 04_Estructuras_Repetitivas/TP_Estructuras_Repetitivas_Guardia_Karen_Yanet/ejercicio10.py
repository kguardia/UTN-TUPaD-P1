"""
Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
# Solicita al usuario un número entero
numero = input("Ingresa un número entero: ")

# Verifica si el número es negativo
if numero[0] == '-':
    # Si es negativo, invertimos solo los dígitos (sin el signo)
    numero_invertido = '-' + numero[:0:-1]
else:
    # Si no es negativo, simplemente invertimos el número
    numero_invertido = numero[::-1]
    
# Muestra el número invertido
print(f"El número invertido es: {numero_invertido}")
