def multiplicacion(a ,b = 1):
    print(a*b)
    
def puede_entrar(nombre, edad= 0):
    if edad < 18:
        return "No puede entrar "+ nombre
    return "Puede entrar " + nombre

print(puede_entrar("Juan", 15))
