"""
Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
import random

# Genera un número aleatorio entre 0 y 9.

numero_secreto = random.randint(0,9)

intentos = 0
adivinanza = -1 #Inicializamos con un número distinto del secreto

# Bucle hasta que el usuario adivine el número
while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    print("Número incorrecto, elige otro número")

# Mostrar mensaje final
print(f"¡Correcto! El numero era: {numero_secreto}.")
print(f"Lo adivinaste en {intentos} intento(s).")