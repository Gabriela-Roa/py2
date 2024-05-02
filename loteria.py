conjunto = {"celular", "termo", "mouse", "teclado", "saco"}

for i in range(len(conjunto)-1):
    numero=int(input("Ingresa 1 para elegir un premio "))
    if numero == 1:
        nuevo_conjunto = conjunto.pop()
        print(nuevo_conjunto)



