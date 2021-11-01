#36.	Escribe un algoritmo o el respectivo diagrama de flujo que dado un número menor a un 100.000 determine la cantidad de dígitos que tiene. Por ejemplo 1093 tiene 4 dígitos.
cantidad=0
cond="si"
while cond=="si":
    numero = int(input("Ingrese un número menor a 100000: "))
    numero1 = numero
    if numero <= 100000:
        while numero != 0:
           residuo = numero % 10
           numero //= 10
           cantidad += 1
        print("{} tiene {} digitos".format(numero1, cantidad))
        break
    else:
        print("El número no es permitido...¿quiere volver a intentarlo? (si o no): ")
        cond = input()
print("El programa ha terminado....:)")