#47.	Escribe un algoritmo o el respectivo diagrama de flujo que determine la suma de los números naturales contenidos entre dos números n y m (verificar que m>n)
print("*****Suma de los números naturales*****")
print("Ingrese dos núemeros (recuerde que el primer número debe ser menor al segundo)")
n=int(input())
m=int(input())
sum=0
if m>n:
    for i in range(n+1,m):
        sum=i+sum
    print(f"La suma de los números entre ellos: {sum}")
else:
    print("Los números no son válidos..:(")