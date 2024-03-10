Precio_base=0
Precio_base = float(input("Ingresa el precio del producto: "))
if Precio_base>=150000:
    Precio_base=Precio_base*1.19
    print("el precio total con el impuesto es: ",Precio_base)
elif Precio_base<150000:
    Precio_base=Precio_base*1.16
    print("el precio total con el impuesto es: ",Precio_base)
    



