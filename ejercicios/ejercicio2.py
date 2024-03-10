#calcule el mayor de 3 numeros, permitiendo leer 3 valores diferentes

num1=0 
num2=0
num3=0

num1=int(input("por favor digita un numero: "))
num2=int(input("por favor digita otro numero: "))
num3=int(input("por favor digita un ultimo numero: "))

if num1>=num2 and num1>=num3:
    print(f"el numero mayor de los que digitaste es {num1}")
elif num2>=num1 and num2>=num3:
    print(f"el numero mayor de los que digitaste es{num2}")
elif num3>=num1 and num3>=num3:
    print(f"el numero mayor de los que digitaste es{num3}")

    
    



