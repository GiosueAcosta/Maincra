#37.	Escribe un algoritmo o el respectivo diagrama de flujo que dados 3 números, determine si los números se están incrementando, disminuyendo o ninguno de lo anterior de acuerdo con el orden de digitación. Por ejemplo: 1 , 4, 19 --> está incrementando  ;  33, 10 ,1 --> está disminuyendo;   3 , 18 , 10 --> Ni se incrementa ni se disminuyendo

print("Ingrese tres números: ")
num1=int(input())
num2 = int(input())
num3 = int(input())

if num1<num2<num3:
    print("{},{},{} ----> está incrementando".format(num1,num2,num3))
elif num1>num2>num3:
    print("{},{},{} ----> está disminuyendo".format(num1, num2, num3))
else:
    print("{},{},{} ----> Ni se incrementa ni se disminuye".format(num1, num2, num3))