#33.	Escribe un algoritmo o el respectivo diagrama de flujo que permita resolver una ecuación cuadrática de tipo ax2 + bx + c(tenga en cuenta las todas las raíces, tanto las reales como las complejas).

from math import sqrt
print("-------------------\nLa ecuación cuadrática es de la forma: ax^2 + bx + c\n-------------------")
a = int(input("Ingrese el coeficiente de la cariable cuadrática a = "))
b = int(input("Ingrese el coeficiente de la variable lineal b = "))
c = int(input("Ingrese el término independiente c = "))
x1 = 0
x2 = 0
if ((b**2)-4*a*c) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
  x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
  print("Las soluciones de la ecuación son:")
  print("x1={:.2f}".format(x1))
  print("x2={:.2f}".format(x2))