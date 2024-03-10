diccionario = {
    "nombre" : "karol",
    "apellido" : "moreno",
    "edad" : 16
}

#nos devuelve un objeto dict_items
claves = diccionario.keys()

#obteniendo un elemento con get()si no encuentranada el programa continua
claves = diccionario.get("edad")
print("hola,el programa continua")

#eliminar todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("edad")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario)


# Materias = {"matemáticas": 4.2,
#             "fisica": 3.8,
#             "quimica": 4.8,
#             "ingles": 4.5,
#             "contabilidad": 4.3,
#             "finanzas": 4.0
#             }

# import operator

# # Ordenar el diccionario por calificaciones de forma descendente
# Materias = sorted(Materias.items(), key=operator.itemgetter(1), reverse=True)

# # Imprimir los resultados
# for indice, (materia, nota) in enumerate(Materias, 1):
#     print(f"{indice}. {materia} ha obtenido {nota} de calificación.")



Materias = {"matemáticas": 4.2,
            "fisica": 3.8,
            "quimica": 4.8,
            "ingles": 4.5,
            "contabilidad": 4.3,
            "finanzas": 4.0
            }

import operator

# Ordenar el diccionario alfabéticamente por las claves
Materias = sorted(Materias.items())

for indice, (materia, nota) in enumerate(Materias, 1):
    print(f"{indice}. {materia} tiene una calificación de {nota}.")

# import operator

# Materias= sorted(Materias.items(), key=operator.itemgetter(1), reverse=True)

# for nota in enumerate(Materias):
#     print(nota [1][0], 'has spend', Materias[nota[1][0]])
   
   
    # if "ciencias_sociales" in Materias:
    #     print(Materias["ciencias_sociales"])
    # else: 
    #     print ("esta materia no existe")

    # Materias ["fisica"] = 3.8
    # Materias ["quimica"]= 4.8

    # del Materias ["ingles"] #elimino esta materia

    # print (Materias)

 