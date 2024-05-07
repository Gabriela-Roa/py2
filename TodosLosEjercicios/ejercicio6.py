edad_cliente = int(input("Escriba su edad "))

if edad_cliente <4:
    print("Puede entrar gratís")
elif edad_cliente == 4 or 18:
    print("Debe pagar 5 euros")
elif edad_cliente > 18:
    print("Debe pagar 10 euros")