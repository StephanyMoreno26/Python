otros_cursos_minimo = 2.5
otros_cursos_maximo = 7
otros_cursos_promedio = 4 
este_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_este_curso = 3.5


#diferencias de duracion

diferencias_min = 100 - este_curso / otros_cursos_minimo * 100
diferencias_max = 100 - este_curso * 1000 // otros_cursos_maximo / 10
diferencias_con_promedio = 100 - este_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo removido
tiempo_vacion_promedio = 100 -otros_cursos_promedio * 100 // crudo_promedio / 10
tiempo_vacio_este_curso = 100 - este_curso * 1000 // crudo_este_curso / 10

#mostrando las diferencias de duracion (ejercicio a)
print("--------------")
print(f'este curso dura un {diferencias_min}% menos que el más rapido')
print(f'este curso dura un {diferencias_max}% menos que el más lento')
print(f'este curso dura un {diferencias_con_promedio}% menos que el promedio')
print("---------------")

#mostrando la cantidad de espacios vacios que se remueva (ejercicio b)
print(f'Un curso promedio elimina un {tiempo_vacion_promedio}% de tiempo vacio')
print(f'este curso elimino el {tiempo_vacio_este_curso}% de tiempo vacio')
print("---------------")

#mostrando diferencias si los cursos duraran 10 horas
print(f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // este_curso / 10}horas de otros cursos')
print(f'ver 10 horas de este curso equivale a ver {este_curso * 100 // otros_cursos_promedio / 10}horas de otros cursos')
print("-----------------")

