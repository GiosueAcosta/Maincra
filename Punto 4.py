#Escribe un algoritmo o el respectivo diagrama de flujo para imprimir la suma, resta, multiplicación, división y residuo de dos números dados.
print("Ingrese dos números")
num_1 = int(input())
num_2 = int(input())
suma = num_1+num_2
resta= num_1-num_2
multi=num_1*num_2
div=num_1/num_2
print("La suma es=", suma)
print("La resta es=", resta)
print("La multiplicación es=", multi)
print("La división es= {:.2f}".format(div))