#49.	Escribe un algoritmo o el respectivo diagrama de flujo que lea n números y calcule su suma y su promedio
print("******Suma y Promedio******")

suma=0
n=int(input("Ingrese la cantidad de números que quiera digitar para calcularles su suma y promedio: "))
print("Ingrese los números....")
for i in range(n):
    numero=int(input())
    suma=suma+numero
print("La suma de los números = {}\nEl promedio de los números es = {:.2f}".format(suma,suma/n))