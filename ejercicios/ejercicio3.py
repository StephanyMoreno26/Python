#calculo de areas-elige una figura geometrica triangulo o circulo
#¿que figura quiere calcular? (escriba T o C)
#Triangulo=base*altura/2
#Circulo=PI*radio*radio

Areas=0
circulo=0
Radio=0
Triangulo=0
Base=0
altura=0

import math

print("bienvenido")
print("Puede elegir a que figura desea calcularle el area")
print("escriba T para triangulo")
print("escriba C para circulo")
int(input("por favor digite una letra: "))

if circulo:
    Radio=float(input("el radio del circulo: "))
    Areas= math.pi * Radio**2
    print (f"el area del circulo es: ")
elif Triangulo:
    Base=int(input("por favor ingresa la base del triangulo"))
    altura=int(input("por favor ingresa la altura del triangulo"))
    area= (Base * altura) /2
    print (f"el area del triangulo es: ")
