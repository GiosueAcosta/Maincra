#8.	Escribe un algoritmo o el respectivo diagrama de flujo que calcule el área de un hexágono.
lado=int(input("Ingrese la medida de los lados del hexágono: "))
apotema=float(input("Ingrese la medidida del apotema del hexágono, recuerda que el apotema es la distancia desde el centro a cualquiera de sus lados: "))
perimetro=6*lado
area=(perimetro*apotema)/2
print("El área es = {:.2f}".format(area))