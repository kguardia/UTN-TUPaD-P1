"""
Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
"""
# Solicitar al usuario un número entero:
numero = int(input("Ingrese un número entero: "))

# Convierte el número a positivo en caso de que sea negativo
numero_abs = abs(numero)

# Convierte el número a cadena y cuenta la cantidad de caracteres
cantidad_digitos = len(str(numero_abs))

# Muestra el resultado
print(f"El número tiene {cantidad_digitos} dígito(s).")