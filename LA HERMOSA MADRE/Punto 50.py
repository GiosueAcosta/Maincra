#50.	Escribe un algoritmo o el respectivo diagrama de flujo para leer una cantidad variable de números e indicar el promedio de los números pares y el promedio de los números impares.
n = int(input("Ingrese la cantidad de números que quiera ingresar: "))
pares = 0
sumpares = 0
impares = 0
sumimpares = 0
for i in range(n):
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        pares = pares+1
        sumpares = sumpares+numero
    else:
        impares = impares+1
        sumimpares = sumimpares+numero

print("La el promedio de los números pares = ", sumpares/pares)
print("La el promedio de los números impares = ", sumimpares/impares)