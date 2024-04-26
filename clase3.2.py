def es_primo(numero):
    a = True
    for i in range(int(numero/2)):
        if (i > 1 and a):
            a = numero % i != 0
    return a

print(es_primo(8))

