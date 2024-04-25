edad = int(input("Escriba su edad "))
ingresos = int(input("Escriba sus ingresos mensuales en euros "))

if edad >16 and ingresos >1000: 
    print("Debe tributar")
else:
    print("No debe tributar")