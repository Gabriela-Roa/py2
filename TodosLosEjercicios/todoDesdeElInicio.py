#ejercicio 1

"""contraseña = "gaby123"
usuario = str(input("Escriba su contraseña "))

if usuario == contraseña:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")"""
    
#ejercicio 2

"""num1 = int(input("Escriba el primer numero "))
num2 = int(input("Escriba el segundo numero "))

if num2 == 0:
    print("Error")
else:
    print(num1 % num2)"""
    
#ejercicio 3

"""numero_entero=int(input("Escriba un numero entero "))

primo_o_par = "El numero es par" if numero_entero % 2 == 0 else "El numero es primo"
print(primo_o_par)"""

#ejercicio 4

"""edad = int(input("Escriba su edad "))
ingresos = int(input("Escriba sus ingresos mensuales "))

tributar = "Debe tributar" if edad > 16 and ingresos >= 1000 else "No debe tributar"

print(tributar)"""

#ejercicio 5

"""nombre = str(input("Escriba su nombre "))
sexo = str(input("Escriba su sexo "))

abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","ñ", "o", "p", "q", "r", "s","t","u","v","w","x","y","z"]

inicial_nombre = nombre[0]

while True:
    if sexo == "femenino":
        for i in range(0, 12, 1):
            if inicial_nombre in abecedario[i]:
                print("El grupo es: ", "Grupo A")     
    elif sexo == "masculino":
        for i in range(14, 27):
            if inicial_nombre in abecedario[i]:
                print("El grupo es: ", "Grupo B")
        break
    break"""

#ejercicio 6

"""cliente = int(input("Escriba su edad "))

if cliente < 4:
    print("Puede entrar gratis")
elif cliente == 4 or 18:
    print("Debe pagar 5 euros")
elif  cliente > 18:
    print("Debe pagar 10 euros")"""

#ejercicio 7

"""palabra = str(input("Escriba una palabra "))

for i in range(10):
    print(palabra)"""
    
#ejercicio 8

"""edad = int(input("Escriba su edad "))

for i in range(edad):
    print(i)"""
    
#ejercicio 9
#falta terminar 

"""numero = int(input("Escriba un numero entero positivo "))"""

#ejercicio 10

"""numero = int(input("Escriba un numero entero positivo "))

if numero > 0:
    hacia_atras = []
    
for i in range(numero, -1, -1):
    hacia_atras.append(str(i))

print("Cuenta regresiva desde", numero, "hasta 0:", ", ".join(hacia_atras))"""

#ejercicio 11
#falta terminar 

"""cantidad = int(input("Ingrese la cantidad que desea invertir "))
interes_anual = int(input("Escriba el interes anual "))
años = int(input("Ingrese la cantidad de años "))

capital_obtenido = cantidad * interes_anual"""

#ejercicio 12




#ejercicio 13
#faltan correjir unas cosas
"""contraseña = ["holamundo47"]

while True:
    usuario = str(input("Digite su contraseña: "))
    if usuario == contraseña:
        print("Contraseña correcta")
    else:
        print("contraseña incorrecta")"""

#ejercicio 14
#falta arreglar algunas cosas

"""usuario = int(input("Escriba un número entero "))

if usuario % usuario == 1 and usuario % 1 == usuario:
    print("El numero es primo")
else:
    print("El numero no es primo")"""
    
#ejercicio 15  
    
"""palabra = str(input("Escriba una palabra: "))

for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])"""
    
#ejercicio 16

"""letra = str(input("Escriba una letra: "))
palabra = str(input("Escriba una palabra: "))

for letra in palabra:
    print(palabra.count(letra))"""
    
#ejercicio 17

#FUNCIONES
#ejercicio 1

"""def factorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

numero = int(input("Digite un numero: "))
print("El factorial de", numero, "es:", factorial(numero))"""

#ejercicio 2



    


    





    

      

        
  
    
