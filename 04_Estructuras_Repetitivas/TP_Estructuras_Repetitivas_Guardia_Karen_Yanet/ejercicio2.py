"""
Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
"""
# Programa para contar la cantidad de dígitos en un número entero
numero = int(input("Ingresa un número entero: "))  # Solicitar número al usuario y transformar a entero.
cantidad_digitos = len(str(abs(numero)))  # Convertir a positivo, luego a string, y contar caracteres
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
# Alternativa usando bucles
contador = 0
numero_absoluto = abs(numero)  # Asegurarse de trabajar con el valor absoluto del número

while numero_absoluto > 0:
    numero_absoluto //= 10  # Dividir entre 10 para eliminar el último dígito
    contador += 1  # Incrementar el contador

# Si el número es 0, tiene 1 dígito
if numero == 0:
    contador = 1

print(f"(Usando bucles) El número {numero} tiene {contador} dígitos.")