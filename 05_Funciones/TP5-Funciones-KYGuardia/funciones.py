import math

#Definición de la función 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Definición de la función 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#Definición de la función 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Definición de la 4ta y 5ta función para el punto 4
def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#Definición de la 6ta función usada para el punto 5
def segundos_a_horas(segundos):
    return segundos / 3600

#Definición de la 7ma función usada para el punto 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#Definición de la 8va función para ser usada en el punto 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b  # Asumimos que b no es cero
    return (suma, resta, multiplicacion, division)

#Definición de la 9na función para ser usada en el punto 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

#Definición de la décima función para ser usada en el punto 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Definición de la última función usada en el punto 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3