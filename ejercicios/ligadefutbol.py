import os
os.system('cls')
titulo= """
***********************************
* FEDERACION COLOMBIANA DE FUTBOL *
***********************************
"""
Opciones ="1. ingresa nombre del equipo\n2.  Registro de fechas\n3. Reporte del equipo\n5. salir"
isactive=True
equipo=[]
#informacion para el reporte
TG=0
PJ=0
PG=0
PP=0
PE=0
GF=0
GC=0
TP=0

while True:
     print(titulo)
     print(Opciones)
     op = int(input("por favor selecciona una opción) "))
     # Pedir nombre del equipo
     if op == 1:
         nombre = str (input("Ingresa nombre del equipo: "))
         equipo.append([nombre,0,0,0,0,0,0,0])
         print(f"El equipo ha sido registrado")
         os.system('pause')
  # Buscar el equipo
     elif op ==2:
        equipo_local = str(input('Ingrese nombre del equipo local: '))
        marcador_local = int(input('Ingrese el número de goles anotados por el equipo local: '))
        equipo_visitante = str(input('Ingrese el nombre del equipo visitante: '))
        marcador_visitante = int(input('Ingrese el número de goles anotados por el equipo visitante: '))
        for i, item in enumerate (equipo):
            if (equipo_local in item):
                if (marcador_local > marcador_visitante):
                    equipo[i][1] += 1  # Wins
                    equipo[i][2] += 1  # Points for a win
                    equipo[i][5] += marcador_local  # Goals scored
                    equipo[i][6] += marcador_visitante  # Goals conceded
                    equipo[i][7] += 3  # Total points
        for i, item in enumerate (equipo):            
            if (equipo_visitante in item):
                if(marcador_visitante < marcador_local):
                    equipo[i][1] += 1  # Wins
                    equipo[i][3] += marcador_visitante  # Points for a loss
                    equipo[i][5] += 1  # Goals scored
                    equipo[i][6] += marcador_local  # Goals against
                    print(equipo)
                else:
                    for k, item in enumerate(equipo):
                        if (equipo_local in item) and (marcador_local==marcador_visitante):
                            item [1] += 1
                            item [3] += marcador_local
                            item [4] += marcador_visitante
                            item [6] += 1
                            item [7] += 1
                        elif (equipo_visitante in item) and (marcador_local==marcador_visitante):
                            item [1] += 1
                            item [3] += marcador_visitante
                            item [4] += marcador_local
                            item [6] += 1
                            item [7] += 1
                            print(equipo)
     elif op ==3:
        reporte = print("Reporte FEDERACION COLOMBIANA DE FUTBOL")
        from tabulate import tabulate
        print(tabulate(equipo,headers=["Equipo","PJ","PG","PP","PE","GF","GC","TP"]))
        print("")
        mas_goles = max(equipo, key=lambda n:item[5])
        equipo_mas_goles = [equipo[0] for equipo in equipo if equipo[5] == mas_goles[5]]
        if len(equipo_mas_goles) > 1:
            print("equipo con mas goles anotados:", equipo_mas_goles)
        else:
            print("El equipo que anoto mas goles: ", equipo_mas_goles[0])
            mas_puntos= max(equipo, key=lambda n:item[7])
            print("El equipo que anoto mas puntos: ",mas_puntos[0])
        print("")
        mas_victorias=max(equipo, key=lambda n:n[2])
        equipos_mas_victorias = [equipo[0] for equipo in equipo if equipo[2] == mas_victorias[2]]
        if len(equipos_mas_victorias) > 1:
            print("El equipo con mas victorias:", equipos_mas_victorias)
        else:
            print("El equipo con mas victorias: ", equipos_mas_victorias[0])
        print("")
        print("Total de goles anotados en el torneo: ",TG)
        print("")
        print("Promedio de cantidad de goles:  ",float(TG/TP))
        print("")
        os.system("pause")