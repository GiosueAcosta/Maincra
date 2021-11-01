#11.	Escribe un algoritmo o el respectivo diagrama de flujo que determine el tiempo de caída de un objeto que se suelta desde una altura h.
#El tiempo es igual a la ráiz cuadrada de la altyra sobre la gravedad
#El valor de la gravedad es 9.8 m/s^2
import math
h=int(input("Ingrese la altura en metros: "))
tiempo=math.sqrt(h/9.8)
print("{:.2f} segundos".format(tiempo))