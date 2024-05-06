Empresas = {

"Empresa 1": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 4}, {"departamento": "Ventas", "empleados": 10}, {"departamento": "Operaciones", "empleados": 25}],

"Empresa 2": [{"departamento": "Recursos Humanos", "empleados": 10}, {"departamento": "Contabilidad", "empleados": 15}, {"departamento": "Ventas", "empleados": 25}, {"departamento": "Operaciones", "empleados": 41}],

"Empresa 3": [{"departamento": "Recursos Humanos", "empleados": 8}, {"departamento": "Contabilidad", "empleados": 20}, {"departamento": "Ventas", "empleados": 32}, {"departamento": "Operaciones", "empleados": 56}],

"Empresa 4": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 8}, {"departamento": "Ventas", "empleados": 15}, {"departamento": "Operaciones", "empleados": 29}],

"Empresa 5": [{"departamento": "Recursos Humanos", "empleados": 20}, {"departamento": "Contabilidad", "empleados": 35}, {"departamento": "Ventas", "empleados": 58}, {"departamento": "Operaciones", "empleados": 97}],

}

print("**************************************************")
print("Mostrar cuántas empresas tienen más de 10 empleados en Recursos Humanos")
print("Mostrar el promedio de empleados por departamento (teniendo en cuenta todas las empresas para cada calculo)")
print("Mostrar cuántas empresas tienen el doble o más del doble de empleados en operaciones con respecto a ventas")
print("Mostrar una nueva estructura de datos reorganizada donde las llaves del diccionario principal no sea empresas sino por departamento.")
print("Digite 1 para iniciar o 0 para terminar")
print("**************************************************")

iniciar_terminar = int(input("Ingrese 1 o 0: ")) 

while iniciar_terminar == 1:
    for i in Empresas:
        for j in Empresas.get(i):
            if j['departamento'] == "RH" and j["empleados"] >10:
                print(i)
        break
                
            

    
