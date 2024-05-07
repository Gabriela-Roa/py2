personas = [{"Nombre": "Pedro", "Edad": 54, "Hobbie": "Correr"}]

with open("archivo.txt", "w") as file:
    for i in personas:
        file.write(i["Nombre"]+","+str(i["Edad"])+","+i["Hobbie"]+"\n")
        
    