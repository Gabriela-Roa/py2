import json

def cargar_datos(archivo):
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos

def guargar_datos(datos, archivo):
    dato = dict(datos)
    
    diccionario=json.dumps(datos)
    file=open(archivo, "w")
    file.write(diccionario)
    file.close()
    