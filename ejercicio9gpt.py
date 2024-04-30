   # Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo "))

# Validar si el número ingresado es positivo
if numero > 0:
    # Inicializar una lista para almacenar los números impares
    impares = []

    # Iterar desde 1 hasta el número ingresado (inclusive)
    for i in range(1, numero + 1):
        # Verificar si el número es impar
        if i % 2 != 0:
            impares.append(str(i))  # Agregar el número impar a la lista como una cadena

    # Mostrar los números impares separados por comas
    print("Números impares hasta", numero, ":", ", ".join(impares))
else:
    print("El número ingresado no es válido. Debe ser un entero positivo.")