"""numero = int(input("Escribe un numero entero positivo "))

for i in range(numero):
    print(i, ",")"""
    
    # Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validar si el número ingresado es positivo
if numero > 0:
    # Crear una lista para almacenar los números en la cuenta regresiva
    cuenta_regresiva = []

    # Iterar desde el número ingresado hasta 0 (inclusive), con paso -1
    for i in range(numero, -1, -1):
        cuenta_regresiva.append(str(i))  # Agregar el número a la lista como una cadena

    # Mostrar la cuenta regresiva separada por comas
  
else:
    print("El número ingresado no es válido. Debe ser un entero positivo.")