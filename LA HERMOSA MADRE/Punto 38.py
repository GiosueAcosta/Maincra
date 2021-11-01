#38.	Escribe un algoritmo o el respectivo diagrama de flujo que, dados dos números, verifique si ambos están entre 0 y 5 o retorne false sino es cierto. Por ejemplo 1 y 2 ---> true ; 1 y 8 ---> false
print("Ingrese dos números entre 0 y 5:")
num1=int(input())
num2=int(input())
if 0<num1<5 and 0<num2<5:
    print("{} y {} ----> True".format(num1,num2))
else:
    print("{} y {} ----> False".format(num1,num2))