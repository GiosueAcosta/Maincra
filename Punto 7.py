#7.	Escribe un algoritmo o el respectivo diagrama de flujo que imprima el área y el perímetro de un círculo.
import math
radio=int(input("Ingrese el radio del circulo para calcularle el área y el perímetro: "))
areaCir=(radio**2)*math.pi
perimetro=2*radio*math.pi
print("El área del circulo es = {:.2f}".format(areaCir))
print("El perímetro del circulo es = {:.2f}".format(perimetro))