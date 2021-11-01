# 23.	Escribe un algoritmo o el respectivo diagrama de flujo que lea un número e indique si este es par-positivo, par-negativo, impar-positivo o impar-negativo.
num = int(input("Ingrese un número:"))
if num % 2 == 0:
    while num >= 0:
        print(num, "es par-positivo")
        break
    else:
        print(num, "es par-negativo")
elif num >= 0:
    print(num, "es impar-positivo")
else:
    print(num, "es impar-negarivo")
