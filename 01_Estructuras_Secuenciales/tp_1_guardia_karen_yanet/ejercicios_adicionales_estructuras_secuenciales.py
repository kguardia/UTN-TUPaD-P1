"""
Ejercicio 1: Cálculo del área y el perímetro de un rectángulo

    Objetivo: Calcular el área y el perímetro a partir de medidas dadas por el usuario.

    Instrucciones:
1. Pedir al usuario que ingrese el ancho y el alto de un rectángulo.
2. Calcular el área usando la fórmula: ancho * alto.
3. Calcular el perímetro con la fórmula: (ancho * 2) + (alto * 2).
4. Mostrar ambos resultados en pantalla.
"""
# Solicitar datos de entrada al usuario
ancho_rectangulo = float(input("Por favor ingrese el ancho del rectángulo: "))
alto_rectangulo = float(input("Por favor ingrese el alto del rectángulo: "))

# Calcular el área y el perímetro
area = ancho_rectangulo * alto_rectangulo
perimetro = 2 * (ancho_rectangulo + alto_rectangulo)

# Mostrar los resultados, es decir, los datos de salida
print(f"El área del rectángulo es de {area}.")
print(f"El perímetro del rectángulo es de {perimetro}.")

"""
Preguntas de reflexión:

• ¿Qué sucede si se ingresan valores negativos?

Si el usuario ingresa valores negativos, el cálculo se hace igual, pero los resultados no tendrían sentido en geometría.
Un ancho o alto no puede ser negativo en una figura real.
Podés agregar validaciones para evitar eso. Ejemplo:
if ancho < 0 or alto < 0:
    print("Error: Las medidas deben ser positivas.")
else:
    # cálculos y prints

• ¿Podría adaptarse este cálculo a otras figuras geométricas?

¡Sí! Solo tendrías que cambiar las fórmulas según la figura:
Triángulo: área = (base * altura) / 2
Círculo: área = π * radio², perímetro = 2 * π * radio
Cuadrado: como el rectángulo pero con lados iguales
Podés hacer un programa que pregunte qué figura querés calcular y usar distintas fórmulas según la respuesta.

"""

"""
Ejercicio 2: Conversión de grados Celsius a Fahrenheit

    Objetivo: Realizar la conversión de temperatura de Celsius a Fahrenheit.

    Instrucciones:
1. Solicitar al usuario una temperatura en grados Celsius.
2. Convertirla a Fahrenheit con la fórmula: F = (C * 9/5) + 32.
3. Mostrar el resultado en pantalla.
"""
# Solicitar al usuario los datos de entrada: temperatura en grados °c
temperatura_celsius = float(input("Por favor, ingrese la temperatura en grados Celsius: "))
# Calcular los grados Fahrenheit
temperatura_fahrenheit = round((temperatura_celsius * (9/5)) + 32, 2)

# Mostrar los resultados, los datos de salida al usuario: grados fahrenheit.
print(f"{temperatura_celsius}°C equivalen a {temperatura_fahrenheit}°F.")

"""
Preguntas de reflexión:

• ¿Qué resultado se obtiene al ingresar 0°C?

Usando la fórmula:
F = (0 * 9/5) + 32 = 0 + 32 = 32
0°C equivalen a 32°F
Este es el punto de congelación del agua en la escala Fahrenheit.

• ¿Cómo se adaptaría este ejercicio para convertir a Kelvin?

La fórmula para pasar de Celsius a Kelvin es:
K = C + 273.15
Podés agregar eso al mismo código:
temperatura_kelvin = temperatura_celsius + 273.15
print(f"{temperatura_celsius}°C equivalen a {temperatura_kelvin} K")
"""

"""
Ejercicio 3: Uso de booleanos
    Objetivo: Manipular variables booleanas y aplicar operadores lógicos.
    Instrucciones:
1. Declarar dos variables booleanas: a = True, b = False.
2. Realizar e imprimir los resultados de las operaciones:
a and b
a or b
not a, not b
"""
# Declaramos las variables booleanas
a = True
b = False

# Realizamos las operaciones y les asignamos una variable para luego mostrar al usuario
c = a and b
d = a or b
e = not a, not b

# Mostrar los resultados por pantalla
print(f"a and b = {c}") # Solo es True si ambos son True
print(f"a or b = {d}") # Es True si al menos uno es True
print(f"not a, not b = {e}") # Invierte los valores de a y b

"""
Preguntas de reflexión:

• ¿Cuál es la utilidad de los operadores lógicos en programas más
complejos?

Los operadores lógicos (and, or, not) permiten tomar decisiones condicionales en los programas. Se usan, por ejemplo, para:
Verificar múltiples condiciones antes de ejecutar algo (como permisos de usuario).
Validar formularios.
Controlar el flujo de un algoritmo.
Combinar varias condiciones para que el código sea más claro y flexible.

• ¿Qué representa cada operación?

a and b: True solo si ambos son True. Representa una condición que necesita que se cumplan las dos cosas.

a or b: True si al menos uno es True. Representa una condición donde basta con que una de las dos se cumpla.

not a: Invierte el valor booleano. Si era True, pasa a False, y viceversa. Sirve para negar condiciones.
"""

"""
Ejercicio 4: Prueba de escritorio
    Objetivo: Analizar el funcionamiento del código y predecir su resultado.
    Instrucciones:
1. Leer el siguiente código:
a = 5         # línea 1 | variable a = 5 | b = sin definir | c = sin definir
b = 3         # línea 2 | a = 5          | b = 3           | c = sin definir
c = a + b     # línea 3 | a = 5          | b = 3           | c = 8
a = 2         # línea 4 | a = 2          | b = 3           | c = 8
print(c)      # línea 5 | a = 2          | b = 3           | c = 8
2. Realizar una prueba de escritorio paso a paso.
3. Determinar qué imprime el programa y por qué.
"""
a = 5
b = 3
c = a + b
a = 2
print(c)

"""
Preguntas de reflexión:

• ¿Por qué el cambio en a no afecta al valor de c?

Porque c se calcula una sola vez en la línea 3. Después de eso, aunque cambies a, c ya tiene guardado su valor (8). No se actualiza automáticamente.

Las variables no están conectadas dinámicamente: una vez que se hace la suma, se guarda el resultado, no la fórmula.

• ¿Qué pasa si se imprime a y b al final?

Agregando esta línea al final:
print(a, b)

El resultado sería:
8
2 3

Porque:
a fue reasignado a 2
b sigue siendo 3
"""

"""
Ejercicio 5: Diagrama de flujo – Cuadrado de un número
    Objetivo: Representar visualmente un algoritmo sencillo.
    Instrucciones:
1. Dibujar un diagrama de flujo para un programa que:
-Pide al usuario un número.
-Calcula su cuadrado.
-Muestra el resultado.
2. Implementar el programa en código si lo deseás.

Diagrama:
INICIO -> Se le indica a la máquina que a través de un input le pida al usuario un número entero positivo cuyo valor se asignará a la variable num -> El usuario ingresa un número por consola -> la máquina lo guarda en la variable num -> Se le pide a la máquina que calcule su cuadrado a través de = num ** 2 -> Finalmente se le indica a la máquina que imprima el resultado a traves de un print para mostrar el resultado por pantalla -> FIN.
"""
# Solicitar datos de entrada:
num = int(input("Por favor ingrese un número entero positivo: "))

# Calcular su cuadrado
cuadrado = num ** 2

# Mostrar resultados
print(f"El cuadrado de {num} es {cuadrado}.")

"""
Preguntas de reflexión:

• ¿Qué ventajas tiene el uso de diagramas de flujo?

-Ayudan a visualizar el algoritmo antes de escribir código.
-Permiten detectar errores lógicos tempranamente.
-Son útiles para explicar procesos a otros, incluso sin conocimientos de programación.
-Organizan el pensamiento de forma secuencial y lógica.

• ¿Cómo se representa una operación matemática en un diagrama?
Se representa con un rectángulo que indica que se está realizando un proceso. Ejemplo:
[cuadrado = num ** 2]
A veces también se usa el símbolo * si no hay potencias, o pow(num, 2) en otros lenguajes.
"""

"""
Ejercicio 6: Intercambio de variables
    Objetivo: Intercambiar valores sin usar una variable temporal.
    Instrucciones:
1. Declarar dos variables: x = 10, y = 20.
2. Intercambiar sus valores usando operaciones aritméticas.
3. Mostrar los valores antes y después del intercambio.
"""
# Declarar variables
x = 10
y = 20

print(f"Antes del intercambio: x = {x}, y = {y}")

# Intercambiar sus valores sin usar variable auxiliar
x = x + y
y = x - y
x = x - y

# Mostrar el resultado después del intercambio
print(f"Después del intercambio: x = {x}, y = {y}.")

"""
Preguntas de reflexión:

• ¿Cómo funciona el intercambio sin variable auxiliar?

Utiliza operaciones matemáticas para almacenar ambos valores en una misma variable (en este caso, x) y luego extraer cada valor por diferencia.

Esto funciona porque estamos aprovechando que:
-La suma contiene información de ambos valores, y
-Con la diferencia podemos recuperar uno sabiendo el otro.

• ¿Qué pasa si los valores iniciales son iguales?

Ejemplo: x = 10, y = 10

x = x + y → x = 20

y = x - y → y = 10

x = x - y → x = 10

El resultado es que ambos siguen siendo 10, porque son iguales al principio.
No hay ningún problema: el intercambio se realiza igual, aunque no se note el cambio.
"""

"""
Ejercicio 7: Cálculo del IMC (Índice de Masa Corporal)
    Objetivo: Aplicar fórmulas con variables numéricas ingresadas por el usuario.
    Instrucciones:
1. Solicitar al usuario su peso en kg y su altura en metros.
2. Calcular el IMC con la fórmula: IMC = peso / (altura ** 2).
3. Mostrar el resultado con un mensaje como: "Tu IMC es: 22.5".
"""
# Solicitar al usuario los datos de entrada: peso y altura
peso = float(input("Por favor ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
IMC = round(peso / (altura ** 2), 2)

# Mostrar el resultado
print(f"Tu IMC es : {IMC}.")

"""
Preguntas de reflexión:

• ¿Qué rango se considera saludable para el IMC?

Según la Organización Mundial de la Salud (OMS):
IMC	Clasificación
Menor a 18.5	Bajo peso
18.5 a 24.9	Peso normal / saludable
25.0 a 29.9	Sobrepeso
30.0 o más	Obesidad

• ¿Cómo podrías dar una recomendación según el resultado?

Podemos agregar una condición al código que diga en qué rango está la persona y dé una pequeña sugerencia:
# Recomendación según IMC
if imc < 18.5:
    print("Estás por debajo del peso saludable. Consultá con un profesional de salud.")
elif 18.5 <= imc < 25:
    print("Estás en un rango de peso saludable. ¡Seguí así!")
elif 25 <= imc < 30:
    print("Estás en sobrepeso. Podrías considerar cambios en la alimentación o actividad física.")
else:
    print("Tu IMC indica obesidad. Es recomendable consultar a un médico o nutricionista.")
"""

"""
Ejercicio 8: Contador de caracteres en un nombre
    Objetivo: Aplicar operaciones con cadenas de texto.
    Instrucciones:
1. Pedir al usuario que ingrese su nombre completo.
2. Calcular y mostrar:
- La cantidad total de letras (sin contar espacios).
- Las primeras 3 letras del nombre.
- El nombre con letras en mayúsculas y minúsculas alternadas
(ejemplo: "JuAn PeReZ").
"""
# Solicitar al usuario los datos de entrada: su nombre completo
nombre = input("Ingrese su nombre completo: ")

# Procesar nombre
sin_espacios = nombre.replace(" ", "")
primeras_3 = nombre[:3]
alternado = "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(nombre))

# Mostrar resultados
print(f"La cantidad total de letras de tu nombre (sin espacios) es: {len(sin_espacios)}.")
print(f"Las primeras 3 letras son: {primeras_3}")
print(f"Nombre con mayúsculas y minúsculas alternadas: {alternado}.")

"""
Preguntas de reflexión:
• ¿Qué técnicas de manipulación de strings estás usando?
nombre.replace(" ", "") -> Elimina los espacios para contar solo letras.
nombre[:3] -> Saca las primeras 3 letras directo con slicing.
"".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(nombre)) -> Este código crea una nueva cadena de texto en la que:
-Las letras en posiciones pares (0, 2, 4, etc.) van en mayúscula.
-Las letras en posiciones impares (1, 3, 5, etc.) van en minúscula.

1. enumerate(nombre)
Convierte la cadena nombre en una secuencia de pares (índice, carácter).

Ejemplo: si nombre = "Juan", entonces enumerate(nombre) genera:
(0, 'J'), (1, 'u'), (2, 'a'), (3, 'n')

2. for i, c in enumerate(nombre)
i es el índice (posición).
c es el carácter en esa posición.

3. c.upper() if i % 2 == 0 else c.lower()
Esto es una expresión condicional.
Si el índice i es par (i % 2 == 0), se convierte c a mayúscula.
Si no, se convierte c a minúscula.

4. "".join(...)
Toma todos los caracteres generados por ese for y los une en una sola cadena.

• ¿Cómo podrías extender este ejercicio para apellidos?
Podrías dividir el nombre en partes y trabajar con cada una por separado. Por ejemplo:
partes = nombre.split()
if len(partes) >= 2:
    apellido = partes[-1]  # Última palabra como apellido
    print(f"Tu apellido es: {apellido}")
    print(f"Tu apellido tiene {len(apellido)} letras.")
También se puede analizar por separado el nombre y apellido, convertir solo el apellido a mayúsculas o aplicar formato tipo "Apellido, Nombre".
"""

"""
Ejercicio 9: Operaciones con números flotantes
    Objetivo: Realizar distintas operaciones matemáticas con decimales.
    Instrucciones:
1. Declarar:
- a = 7.5
- b = 3.2
2. Calcular y mostrar:
- La suma (a + b)
- El redondeo de la división (a / b) a 2 decimales
- La potencia (a ** b)
"""
# Declarar variables con los datos de entrada
a = 7.5
b = 3.2

# Calcular
suma = (a + b)
division = round(a / b, 2)
potencia = a ** b

# Mostrar resultados
print(f"La suma entre {a} y {b} es de = {suma}.")
print(f"La división redondeada entre {a} y {b} es de: {division}.")
print(f"La potencia de {a} por {b} es de {potencia}.")

"""
Preguntas de reflexión:

• ¿Qué ocurre si redondeás a más decimales?

Si redondeas a más decimales, obtienes un número más preciso. Por ejemplo, si redondeas a 4 decimales en lugar de 2, obtendrás 2.3438 en vez de 2.34. La precisión depende del número de decimales que elijas.

• ¿Cuándo conviene usar math.pow()?

math.pow() es útil cuando necesitas hacer cálculos con potencias en los que los exponentes son números flotantes o cuando se requiere una mayor precisión en operaciones de potencias. Sin embargo, para exponentes enteros, usar el operador ** es suficiente y más directo.

Ejemplo con math.pow():
import math
potencia_math = math.pow(a, b)
print(f"Potencia usando math.pow(): {potencia_math}")

"""

"""
Ejercicio 10: Descuento sobre precio original
    Objetivo: Aplicar porcentajes y mostrar el resultado.
    Instrucciones:
1. Pedir al usuario el precio original de un producto.
2. Pedir el porcentaje de descuento.
3. Calcular el precio final:
precio_final = precio_original * (1 - (descuento / 100))
4. Mostrar el precio con descuento.
5. (Opcional) Dibujar un diagrama de flujo del proceso.
"""
# Pedir al usuario el dato de entrada: precio original de un producto
precio_original = float(input("Por favor, ingrese el precio original del producto: $"))
porcentaje_descuento = float(input("Por favor, ingrese el porcentaje de descuento (sin el signo de %): "))

# Calcular
precio_final = precio_original * (1 - (porcentaje_descuento / 100))

# Mostrar el precio con descuento
print(f"El producto con el descuento le queda en un valor total de: ${round(precio_final, 2)}.")

"""
Preguntas de reflexión:

• ¿Qué ocurre si el descuento es mayor a 100%?

Si el descuento es mayor al 100%, el precio final será negativo, lo cual no tiene sentido en este contexto, ya que no puede haber un "descuento" mayor al valor total del producto. Podríamos agregar una validación para asegurarnos de que el descuento no sea mayor al 100%:
if descuento > 100:
    print("El descuento no puede ser mayor al 100%.")
else:
    # Calcular el precio final y mostrarlo

• ¿Cómo podrías mostrar el monto ahorrado?
El monto ahorrado es simplemente la diferencia entre el precio original y el precio final con el descuento aplicado. Ya hemos calculado esto en la variable monto_ahorrado, y la mostramos en el código con:
print(f"El monto ahorrado es: ${monto_ahorrado:.2f}")

# Diagrama de flujo (Opcional):
1. Inicio
2. Solicitar precio original y descuento al usuario.
3. Calcular precio final con la fórmula: precio_final = precio_original * (1
− (descuento/100))
4. Mostrar precio final con descuento.
5. Calcular monto ahorrado y mostrar.
6. Fin
"""