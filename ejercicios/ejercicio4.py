#algoritmo que calcule el area de un rectangulo siempre y cuando los lados sean positivos

Rectangulo=0
Base=0
altura=0
area=0
lado=0

base=int(input("por favor ingresa la base del rectangulo"))
altura=int(input("por favor ingresa la altura del rectangulo"))
area=base * altura
if lado>=0:
    print("El area del rectangulo es: ",area)
elif lado>=-0:
    print("No es posible calcular el area",area) 
