#46.	Escribe un algoritmo o el respectivo diagrama de flujo que imprima los números naturales contenidos entre dos números n y m (verificar que m>n)
print("Ingrese un rango de números: ")
n=int(input())
m=int(input())
if m>n:
    for i in range(n+1,m):
        print(i)
else:
    print("Números no válidos")