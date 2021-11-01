#25.	Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y si este es mayor o igual a 10 devuelva el triple de este, de lo contrario la cuarta parte de este.
numero=int(input("Ingrese un número: "))
if numero>=10:
    print(numero*3)
else:
    print(numero/4)