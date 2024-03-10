#el docente no asiste hoy, sus alumnos daran la clase hoy

#pedir nombre y edad de los presentes

def obtener_estudiantes(cantidad_estudiantes):
    estudiantes = []
    for i in range(cantidad_estudiantes):
        nombre = input("Ingresa el nombre del estudiante: ")
        edad = int(input("ingrese la edad del estudiante: "))
        estudiante = (nombre,edad)
        estudiantes.append(estudiante)
    estudiantes.sort(key=lambda x:x[1])#ordenar por el segundo parametro"edad"
    representante = estudiantes[0][0]
    docente = estudiantes[-1][0]
    return representante,docente
representante,docente = obtener_estudiantes (5)

print(f"El docente es: {docente} y el representante de su clase es: {representante}")
