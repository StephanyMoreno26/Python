#creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Stephany"
numeros = [3,14,16,32]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'comeré una {fruta}')
    
#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f'comeré una {fruta}')
    if fruta == 'pera':
        break
else: 
    print("terminado")
    
#recorer una cadena de texto
for letra in cadena:
    print(letra)
    

#for en una sola linea de còdigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)