Pagos=float(input("pago total"))
if(Pagos>=130000):
    descuento=Pagos*0.15
    total=Pagos-descuento
    print(f"el total a pagar más el descuento aplicado es: {total}")
else:
    print(f"El total a pagar es {Pagos}")