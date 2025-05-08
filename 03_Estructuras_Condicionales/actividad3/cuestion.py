edad = int(input("Introduce tu edad: "))

if edad >= 0 and edad <= 12:
    print("Eres un niño.")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente.")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")


import random
numero_correcto = random.randint(1, 100) 
numero_usuario = int(input("Adivina el número entre 1 y 100: "))

if numero_usuario == numero_correcto: 
    print("¡Has adivinado el número!") 
elif numero_usuario < numero_correcto:
    print("Intenta con un número mayor.") 
else:
    print("Intenta con un número menor.")