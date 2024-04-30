#option = int(input("Ingrese un (1) si desea verificar un numero primo, (2) si es par o impar o (3) para obtener la media de una serie de numeros"))
#verificar si un numero es primo

def primo (num):
    contador = 2
    resultado = True
    
    while (contador < num / 2 and resultado):
        resultado = num % contador != 0
        contador += 1
    
    return resultado

#verifivar si un numero es par o impar

def par (num):
    if num % 2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"
    
#obtener la media de una serie de numeros

def media(lista):
    suma=0
    for numero in lista:
        suma+=numero
    return suma/len(lista)

lista = [1,2,3,4,5,6,7]
#print(media(lista))  

#generar una lista con i valores

def generar_lista():
    cantidad = (int(input("Digite los valores que desea ingresar")))
    lista = []
    for i in range(cantidad):
        lista.append(int(input("Ingrese el valor")))
    return lista

#print(media(generar_lista()))

#verificar si una palabra contiene la letra x o z

def palabra  ():
    palabra = (input("ingrese una palabra: "))

    return palabra.count ("x") != 0 or palabra.count("z") != 0

#print(palabra())

continuar="si"
while continuar=="si":
    operacion=str(input("Ingrese el proceso que desea realizar (primo) (par) (media) (palabra)"))
    if operacion=="primo":
        print(primo(int(input("Ingrese el numero: "))))
    elif operacion=="par":
        print(par(num))
    elif operacion=="media":
        print(media(generar_lista()))
    elif operacion=="palabra":
        print(palabra())
    else:
        print("Ingreso una operacion no valida")
        
 

    
    
    continuar=str(input("Desea repetir el proceso? Ingresa (no) para cerrar el ciclo y (si) para repetir el proceso"))