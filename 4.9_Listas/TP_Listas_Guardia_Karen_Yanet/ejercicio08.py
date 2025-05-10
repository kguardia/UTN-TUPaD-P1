"""
Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
"""
def calcular_imc(peso, altura):
    imc=peso/altura**2
    print(imc)

peso=float(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su altura en Metros: "))

calcular_imc(peso,altura)

