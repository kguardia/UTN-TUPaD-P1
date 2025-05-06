# Vamos a ver las funciones que nos habilita python para poder mostrar información al usuario a través de la consola y para poder solicitar información del usuario a través de la consola y tener una interacción con el usuario.

# Usamos la función sprint para mostrar un mensaje en la pantalla.
print("¡Hola! Vamos a a aprender cómo funciona la función sprint e input.")

# Una función de entrada es la función input, nos va a permitir poder ingresar información, que el usuario nos escriba a través de la consola.
# Esta información que el usuario puede ingresar necesitamos almacenarla en una variable.
# Para poder almacenar una variable no necesitamos más que definir el nombre de la variable = y asignarle un valor.

# Usamos la función input para pedirle al usuario que ingrese su nombre
# El texto dentro de los paréntesis es un mensaje que se muestra al usuario 
nombre = input("Por favor, escribe tu nombre: ")

# Ahora usamos print nuevamente para mostrar un mensaje personalizado 
# Combinamos texto fijo con el valor que ingresó el usuario.
print("¡Mucho gusto, " + nombre + "!") # Concatenamos con el signo + la cadena de carácteres y las variables.

# Ejemplo adicional: le pedimos al usuario su edad.
edad = input("¿Cuántos años tienes? ")

# Usamos print para mostrar otra vez un mensaje personalizado.
# Recordamos que los datos ingresados con input son texto (string), no números.
print("Wow, " + edad + " años, ¡estás listo para programar!")

# Hay un detalle que tenemos que tener en cuenta: el input cuando lo estamos utilizando de esta manera lo que está haciendo es que cualquier cosa que yo este ingresando está siendo considerado como si fuera una cadena de caracteres ¿Qué quiere decir esto? Que la edad en este caso no tiene un valor númerico sino que está almacenado como si fuera una palabra que tiene el símbolo 29.