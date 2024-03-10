frase = input("escribeme una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

#cramos una lista con todas las palabra de la frase
separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(separadas)

#en caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("espera, no te pedi un testimonio")

#calculamos cuanto tardaria en decir las palabra y se lo decimos    
print(f'dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2}segundos en decirlo')
print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 *1.3 /100} segundos')