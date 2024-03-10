lista = list(["hola","karol"])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("abby")

#agregando un elemento a la lista en un indice especifico
lista.insert(4,"juliana")

#agregamos varios elementos a la lista 
lista.extend([False,2024])

#eliminar elementos de la lista
lista.pop(0)#-1 para eliminar el ultimo, -2 eliminar el anteultimo, y asi sucesivamente

#remover un elemento de la lista por su valor 
lista.remove("abby")

#eliminar todos los elementos de la lista
lista.clear()

#ordenar elementos de forma ascendente
lista.sort

#invierte los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(2024)


print(lista)