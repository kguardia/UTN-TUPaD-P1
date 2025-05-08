"""
Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
"""
# Solicitar su edad al usuario
edad = int(input("Ingrese su edad por favor: "))

# Verificar a qué categoría pertenece 
# Si la edad es menor que 0, imprimimos "Por favor, ingrese un número positivo"
if edad < 0:
    print("Por favor, ingrese un número positivo")
# Si la edad es menor que 12, imprimimos "Niño/a"
elif edad < 12:
    print("Niño/a")
# Si la edad es mayor o igual que 12 y menor que 18, imprimimos "Adolescente"
elif 12 <= edad < 18:
    print("Adolescente")
# Si la edad es mayor o igual que 18 y menor que 30, imprimimos "Adulto/a joven"
elif 18 <= edad < 30:
    print("Adulto/a joven")
# En cualquier otro caso, imprimimos "Adulto/a". Esto en este caso equivale a decir elif edad >= 30 porque es el único caso que no está cubierto hasta el momento
else:
    print("Adulto/a")
