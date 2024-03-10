#considere dos variables de tipo N llamadas temperatura y presión. Escriba una sentencia si o sino que muestre
#en patalla la palabra Alarma si la variable presión mayor a 200 o si la variable temperatura es mayor a 100
#En caso contrario debe mostrar la palabra Normal

temperatura=0
presión=0


temperatura=int(input("ingresa por favor la temperatura: "))
presión=int(input("ingresa por favor la presión: "))

if presión <200 or temperatura <100:
   print("NORMAL")
elif presión >200 or temperatura >100: 
    print("ALARMA")

