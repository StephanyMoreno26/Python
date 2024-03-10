profesiones = ["doctor","programador","abogado","ing electronico"]
universidades = ["uis","unab","santoto"]

#recorriendo la lista profesiones
for profesion in profesiones:
    print(f'estas son las profesiones ofrecidas: {profesion}')

#recorriendo la lista universidades
for universidad in universidades:
    print(universidades)

#ierando dos listas del mismo tamaño al mismo tiempo
for profesion, universidad in zip (profesiones,universidades):
    print(f"recorriendo lista 1: {profesion}")
    print(f"recorriendo lista 2: {universidad}")

#forma de recorrer una lista con su indice
for pro in enumerate(profesiones):
    indice = pro[0]
    valor = pro[1]
    print(f"el indice es: {indice} y el valor es: {valor}")


#usando el for/else
for universidad in universidades:
    print(f"ejecuntando el ultimo bluce, valor actual: {universidad}")
else: 
    print("el bucle termino")