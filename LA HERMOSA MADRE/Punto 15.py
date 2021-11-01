#15.	Escribe un algoritmo o el respectivo diagrama de flujo que dadas coordenadas x1, y1 y x2, y2 en el plano cartesiano calcule la distancia entre ellos(considere todos los valores positivos)
import math
#Datos de entrada
punto1 = input('Ingrese la coordenada del primer punto: ')
punto2 = input('Ingrese la coordenada del segundo punto: ')
#Utilizando la función split () para separar los datos por espacios y asignarlos a la variable p1 y p2
p1 = punto1.split((","))
p2 = punto2.split((","))
#Utilizando la función eval () para convertir el tipo de cadena a tipo de datos;

x1 = eval(p1[0])
y1 = eval(p1[1])
x2 = eval(p2[0])
y2 = eval(p2[1])

distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)
# Imprimir datos; donde 2f significa retener dos decimales
print('La distancia entre los dos puntos es= {:.2f}'.format(distancia))