# Vamos a ver ahora como procedemos para trabajar con el ingreso de números a través del mismo comando input para poder hacer por ejemplo suma, resta, multiplicación y demás.

# Usamos la función input para pedir un número entero al usuario 
numero_entero = input("Por favor, escribe un número entero: ")

# Convertimos (casteamos) el dato ingresado a un número entero con int()
numero_entero = int(numero_entero) # Ahora la variable contiene un entero, no texto

# Mostramos el número entero usando print
print("El número entero que ingresaste es: ", numero_entero)

# Pedimos al usuario un número decimal (el usuario para ingresar un decimal debe usar el punto no una coma en python)
numero_decimal = input("Ahora escribe un número decimal: ")

# Convertimos el dato ingresado a un número decimal (punto flotante) con float()
numero_decimal = float(numero_decimal) # Ahora la variable contiene un número decimal y no un string.

# Mostramos el número decimal usando sprint
print("El número decimal que ingresaste es: ", numero_decimal)

# Ejemplo: operamos con los números ingresados
suma = numero_entero + numero_decimal # Sumamos el entero y el decimal
print("La suma de ambos números es: ", suma)

# Es necesario y muy importante castear el tipo de dato string a un dato númerico porque sino los concatena, es decir los une, no los suma como queremos ya que la computadora no las identifica como tipo de dato númerico sino como string, y si haces el casteo de uno solo y otro número no tira error al realizar una operación aritmética ya que no permite al dato string...

