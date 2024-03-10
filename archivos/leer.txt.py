archivo = open("archivos\\texto.txt")

#leer archivo completo 
cosa = archivo.read()

#leer linea por linea
linea1 = archivo.readlines()

#leer una sola linera
linea = archivo.readline(10)

#cerrar el archivo
archivo.close()

print(linea)

