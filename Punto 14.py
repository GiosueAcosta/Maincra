#14.	Escribe un algoritmo o el respectivo diagrama de flujo que determine la energía (en Julios) de un objeto si se conoce la masa de un objeto (en kg) y la velocidad de la luz (en m/s).
masa=float(input("Ingrese la masa del objeto en kg: "))
velocidad = float(input("Ingrese la velocidad del objeto: "))
Energia=(masa*velocidad)/2
print(format(Energia,"J"))  