"""
1. Declaración y asignación de variables
Una variable es como una caja donde guardamos un valor. En Python, no es necesario indicar el tipo de dato (como en otros lenguajes).
"""

edad = 20 # Guarda un número
nombre = "Ana" # Guarda una cadena de texto (string)
pi = 3.14 # Guarda un número decimal

# Podés cambiar el contenido de una variable en cualquier momento:

edad = 25

"""
2. Operadores aritméticos
Son símbolos que usamos para realizar operaciones matemáticas:
Operador    Función             Ejemplo
+           Suma                a + b
-           Resta               a - b
*           Multiplicación      a * b
/           División            a / b
//          División Entera     a // b
%           Módulo (resto)      a % b
**          Potencia            a ** b
"""

a = 10
b = 3

print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.3333333333333335
print(a // b) # 3
print(a % b) # 1
print(a ** b) # 1000

"""
3. Entrada y Salida en Python
input(): permite ingresar datos por teclado.

importante: input() siempre devuelve un string. Si necesitás un número, convertí el tipo:

print(): muestra datos en la pantalla
"""

name = input("¿Cómo te llamás? ")
age = int(input("¿Qué edad tenés? "))
print("Hola",name)

"""
4. Strings con formato (f-strings)
Permiten insertar variables dentro de un texto de manera simple y clara.
Mucho más práctico que concatenar con +!
"""
nombre_4 = "Sofia"
edad_4 = 22

print(f"Hola, me llamo {nombre_4} y tengo {edad_4} años.")

"""
5. Introducción a Secuenciales
Un programa secuencial ejecuta las instrucciones una detrás de otra, en el orden en que están escritas.
En el siguiente ejemplo, cada línea se ejecuta de forma secuencial: primero pide el nombre, luego muestra el saludo, y después un mensaje de bienvenida.
"""
nombre_5 = input("¿Tu nombre? ")
print(f"Hola {nombre_5}")
print("¡Bienvenido a Python!")

"""
Recomendaciones
• Hacé los ejercicios propuestos mientras ves los videos.
• Usá print() para comprobar el valor de tus variables.
• Probá distintas entradas en input() y modificá tus variables.
• Experimentá con f-strings para practicar formatos más expresivos.

Resumen Rápido:
Concepto    Ejemplo
Variable    nombre = "Juan"
Operador    a * b, a % b
Entrada     input("Ingresá tu edad")
Salida      print("Hola")
f-string    f"Hola {nombre}"
Secuencia   Código que se ejecuta de arriba a abajo
"""
