def menu_principal():
    print("*******************************************")
    print("Ingrese la opcion que requiera")
    print("1. para registrar los participantes")
    print("2. para eliminar un participantes")
    print("3. para pagar la entrada de un participante")
    print("4. para registrar un evento")
    print("5. para modificar un evento")
    print("6. para marcar un evento como finalizado")
    print("7. saber cuantos participantes no han pagado")
    print("8. saber cuales parcipantes no han pagado")
    print("9. para conocer participantes del mes")
    print("10. para salir")
    print("*******************************************")
    
    def pedir_opcion():
        opc = 0
        
        try:
            opc = int(input("Ingrese su opción: "))
            return opc
        execept Exeception:
            print("Valor invalido")
            
        