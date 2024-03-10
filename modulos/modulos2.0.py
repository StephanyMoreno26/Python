#si el modulo estuviera dentro de una carpeta en la misma ruta, import funciones_buenas.saludar as m_saludar

import sys

sys.path.append("D:\USUARIO\Documents\Campus\grupoj3\Ejercicios2.0\python\\funciones_buenas")
print(sys)

import saludar as modulo_saludo

print(modulo_saludo.saludar("Dalto"))