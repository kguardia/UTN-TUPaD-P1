# Necesitmaos importar la librería math para usar el PI
import math

"""
1) Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".
"""
print("Hola Mundo!")

"""
2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado: Por ejemplo: si el usuario ingresa "Marcos", el programa debe imprimir por pantalla "Hola Marcos!". Consejo: esto será más sencillo si utilizas print(f...) para realizar la impresión por pantalla.
"""
nombre = input("Ingrese su nombre por favor: ")

print(f"Hola {nombre}!")

"""
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
"""
nombre = input("Ingrese su nombre por favor: ")
apellido = input("Gracias, ahora ingrese su apellido: ")
edad = int(input("Y ahora, por favor, ingrese su edad: "))
lugar_de_residencia = input("Por último, ingrese el país de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

"""
4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
"""
radio = float(input("Ingrese el radio del círculo: "))

area = round(math.pi * (radio) ** 2, 2)
perimetro = round(2 * math.pi * radio, 2)

print(f"El área del círculo es de {area} y su perímetro es de {perimetro}.")

"""
5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
"""
segundos = float(input("Por favor, ingrese la cantidad de segundos: "))
horas = round(segundos / 3600, 2)

print(f"Los {segundos} segundos equivalen a {horas} horas.")

"""
6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
"""
num = int(input("Ingrese un número entero por favor: "))

multiplicado_por_0 = num * 0
multiplicado_por_1 = num * 1
multiplicado_por_2 = num * 2
multiplicado_por_3 = num * 3
multiplicado_por_4 = num * 4
multiplicado_por_5 = num * 5
multiplicado_por_6 = num * 6
multiplicado_por_7 = num * 7
multiplicado_por_8 = num * 8
multiplicado_por_9 = num * 9

print(f"{num} * 0 = {multiplicado_por_0}")
print(f"{num} * 1 = {multiplicado_por_1}")
print(f"{num} * 2 = {multiplicado_por_2}")
print(f"{num} * 3 = {multiplicado_por_3}")
print(f"{num} * 4 = {multiplicado_por_4}")
print(f"{num} * 5 = {multiplicado_por_5}")
print(f"{num} * 6 = {multiplicado_por_6}")
print(f"{num} * 7 = {multiplicado_por_7}")
print(f"{num} * 8 = {multiplicado_por_8}")
print(f"{num} * 9 = {multiplicado_por_9}")

"""
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
"""
num_1 = float(input("Ingrese el primer número distinto de 0: "))
num_2 = float(input("Ingrese el segundo número distinto de 0: "))
suma = num_1 + num_2
resta = num_1 - num_2
division = round(num_1 / num_2, 2)
multiplicacion = num_1 * num_2
print(f"{num_1} + {num_2} = {suma}")
print(f"{num_1} - {num_2} = {resta}")
print(f"{num_1} / {num_2} = {division}")
print(f"{num_1} * {num_2} = {multiplicacion}")

"""
8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso en kg / (altura en m)^2
"""
altura = float(input("Ingrese su altura (Ejemplo: 1.62 = 1,62m): "))
peso = float(input("Ingrese su peso (Ejemplo: 72.8 = 72,8kg): "))

imc = round(peso / (altura) ** 2, 2)

print(f"Su índice de masa corporal es de {imc}")

"""
9) Crear un programa que pida al usuario una temperatura en grados celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
Temperatura en Fahrenheit = 9/5 * Temperatura en celsius + 32
"""
temperatura_celsius = float(input("Ingrese la temperatura en grados celsius: "))
temperatura_fahrenheit = round((9/5) * temperatura_celsius + 32, 2)

print(f"Si la temperatura en celsius es de {temperatura_celsius} grados. La temperatura en grados Fahrenheit es de {temperatura_fahrenheit} grados.")

"""
10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
"""
nota_1 = float(input("Ingrese la primera nota númerica del 1 al 10: "))
nota_2 = float(input("Ingrese la segunda nota númerica del 1 al 10: "))
nota_3 = float(input("Ingrese la tercera nota númerica del 1 al 10: "))

promedio = round((nota_1 + nota_2 + nota_3) / 3, 2)

print(f"El promedio entre {nota_1}, {nota_2} y {nota_3} es de {promedio}")