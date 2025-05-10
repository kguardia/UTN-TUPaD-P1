"""
Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
# Programa para invertir el orden de los dígitos de un número ingresado por el usuario usando bucles
numero = int(input("Ingrese un número entero: "))

# Convertir el número a positivo para manejar números negativos
numero_absoluto = abs(numero)

# Inicializar la variable para almacenar el número invertido
numero_invertido = 0

while numero_absoluto > 0:
    digito = numero_absoluto % 10  # Obtener el último dígito
    numero_invertido = numero_invertido * 10 + digito  # Agregar el dígito al número invertido
    numero_absoluto //= 10  # Eliminar el último dígito del número

# Si el número original era negativo, hacer que el número invertido también sea negativo
if numero < 0:
    numero_invertido = -numero_invertido

# Mostrar el número invertido
print(f"El número invertido es: {numero_invertido}")
