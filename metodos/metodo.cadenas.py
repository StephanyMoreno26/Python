cadena1= "Hola soy karol"
cadena2= "Bienvenido"

#print(dir(cadena1))
 
mayuscula = cadena1.upper()#convertir a mayusculas
 
minuscula = cadena1.lower()#convertir a minusculas

primera_letra_mayus = cadena1.capitalize()#primera letra mayuscula

busqueda_find = cadena1.find("") #buscar una cadena en otra cadena, si no hay coincidencias devuelve -1

busqueda_index = cadena1.index("")#buscar una cadena en otra cadena, si no encuentra coincidencias arroja una excepcion.

numerico = cadena1.isnumeric()#si es numerico devolvemos true, sino devolvemos false

alfanumerico = cadena1.isalpha()#si es alfanumerico devuelve true, sino devuelve false

contar_coincidencias = cadena1.count("")#contar coincidencias de una cadena dentro de otra cadena,devuelve la cantidad de coincidencias

contar_caracteres = len(cadena1)#cuenta cuantos caracteres tiene una cadena

empieza_con = cadena1.startswith("")#verificamos si una cadena empieza con otra dada, si es asi devuelve true

termina_con = cadena1.endswith("")#verificamos si una cadena termina con otra dada, si es asi devuelve true

cadena_nueva = cadena1.replace()#reemplaza un pedazo de cadena original, remplaza el valor 1 de la misma, por el valor 2 

cadena_separada = cadena1.split()#separa cadenas con la cadena que le pasemos

print()
