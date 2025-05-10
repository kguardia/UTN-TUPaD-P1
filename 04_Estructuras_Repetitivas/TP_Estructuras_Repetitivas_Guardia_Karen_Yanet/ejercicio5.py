"""
Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
import random

# Genera un número aleatorio entre 0 y 9.

numero_secreto = random.randint(0,9)

print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 0 y 9. ¿Puedes adivinar cuál es?")

intentos = 0  # Variable para contar los intentos del usuario
acertado = False  # Bandera que indica si el usuario ya adivinó el número

# Ciclo que se ejecuta hasta que el usuario adivine
while not acertado:
    # Pedir al usuario que ingrese un número
    intento = int(input("Ingresa tu intento: "))
    intentos += 1  # Incrementar el contador de intentos

    # Comparar el número ingresado con el número secreto
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        acertado = True  # Cambiar la bandera a True para salir del bucle
    elif intento < numero_secreto:
        print("El número es mayor. ¡Inténtalo de nuevo!")  # Dar una pista
    else:
        print("El número es menor. ¡Inténtalo de nuevo!")  # Dar otra pista

# Mostrar cuántos intentos fueron necesarios
print(f"Lo lograste en {intentos} intentos. ¡Buen trabajo!")