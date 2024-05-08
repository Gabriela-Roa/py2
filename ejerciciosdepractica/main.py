from datos import *
from menu import *

#Constants 
RUTA_BASE_DE_DATOS ="eventos.json"

datos= cargar_datos(RUTA_BASE_DE_DATOS)

while True:
    menu_principal()
    opc = pedir_opcion()
    if opc == 1:
        print("Opcion 1")
    elif opc == 2:
        print("Opcion 2")
    elif opc == 3:
        print("Opcion 3")
    elif opc == 4:
        print("Opcion 4")
    elif opc == 5:
        print("Opcion 5")
    elif opc == 6:
        print("Opcion 6")
    elif opc == 7:
        print("Opcion 7")
    elif opc == 8:
        print("Opcion 8")
    elif opc == 9:
        print("Opcion 9")
    elif opc == 10:
        print("Opcion 10")
    elif opc == 11:
        print("Salió!!")
        break 
    
datos= cargar_datos(RUTA_BASE_DE_DATOS)

print(datos)
   
guargar_datos(datos, RUTA_BASE_DE_DATOS)