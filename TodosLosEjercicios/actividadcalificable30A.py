print("Bienvenidos al juego")
print("Reglas:")
print("1.Las palabras deberan conectar unas con otras teniendo en cuanta la ultima letra de la palabra anterior")
inicio = int(input("2.Para iniciar el juego digite 1 y para finalizar 0 "))

while inicio == 1:
    cosas = ["casa", "avion", "niño", "oso", "osito","oruga", "aguacate","esfera", "arbol", "lapiz", "zapato","oso","oliva", "arcoiris","sol", "leon", "nuez", "zoologico", "oreja", "alfombra", "abanico","otoño", "oracion","nieve", "espejo"]
    
    len(cosas)

    opcion = int(input(f"Escriba un numero de 0 a {len(cosas)} "))

    palabra_predefinida = cosas[opcion]
    print("La palabra a iniciar es: ", palabra_predefinida)

    jugadores = 3

    print("jugador1")
    palabra = str(input("Escriba la palabra: "))

    palabra_predefinida[-1]
    palabra[0]

    if palabra_predefinida[-1] == palabra[0]:
        print("Las palabras se encadenan")
    else:
        print("La palabra no cumple con la regla")
    
    if palabra in cosas:
        print("La palabra se encuentra en la lista")
    else:
        print("La palabra no esta en la lista")

    if cosas.count(palabra) > 1:
        print("La palabra esta duplicada")
        print("jugador2")
        palabra = str(input("Escriba la palabra: "))
