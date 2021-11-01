#30Escribe un algoritmo o el respectivo diagrama de flujo que lea tres números y determine si la suma del primero y el segundo es mayor o menor que el tercero.

print("Ingrese tres números: ")
n1=int(input())
n2=int(input())
n3=int(input())
if n1+n2>n3:
    print("La suma del primero y el segundo es mayor que el tercero")
else:
    print("La suma del primero y segundo es menor que el tercero")