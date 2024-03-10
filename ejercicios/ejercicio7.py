planta=0
administrativa=0
print("Buen día")

Empleado=str(input("digite A si traba en planta o digite B si trabaja en el area administrativa: "))
Horas=int(input("numero de horas trabajadas: "))

if(Empleado=="A"):
    PAGO=Horas*10000
    print(f"el pago total es {PAGO}")

if(Empleado=="B"):
    PAGO=Horas*20000
    print(f"el pago total es {PAGO}")