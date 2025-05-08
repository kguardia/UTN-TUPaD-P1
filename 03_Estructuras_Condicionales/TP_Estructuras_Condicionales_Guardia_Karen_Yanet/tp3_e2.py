"""
Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
""" 
# Solicitar la nota al usuario
nota = int(input("Por favor ingrese su nota: "))

# Verificar si la nota es aprobatoria.
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
