sueldoinicial=(144000000)
Aumentodesueldo=0
salario=0
tiempo=int(input("¿Cuanto tiempo lleva trabajando en la empresa? "))
if tiempo>10:
    salario=sueldoinicial*1.10
    print ("El aumento de tu salario sera: ",salario)
elif(tiempo<10)or(tiempo>5):
    salario=sueldoinicial*1.07
    print ("El aumento de tu salario sera: ",salario)
elif(tiempo<5)or(tiempo>3):
    salario=sueldoinicial*1.05
    print ("El aumento de tu salario sera: ",salario)
elif(tiempo<3):
    salario=sueldoinicial*1.03
    print ("El aumento de tu salario sera: ",salario)



