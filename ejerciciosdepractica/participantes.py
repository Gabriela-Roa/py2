def registrar_participantes(datos):
    datos = dict(datos)
    participantes={}
    participantes["nombre"]=input("Ingrese el nombre: ")
    participantes["documento"]=input("Ingrese el documento: ")
    participantes["cargo"]=input("Ingrese el cargo: ")
    try:
        participantes["edad"] = int(input("Ingrese la edad: "))
    except Exception:
        participantes["edad"] = 0
    print("Ingrese 1 si el participante paga o 2 de lo contrario")
    opc = -1
    try:
        opc = int(input("Ingrese la opcion: "))
    except Exception:
        opc = 2
        