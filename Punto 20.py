#20.	Escribe un algoritmo o el respectivo diagrama de flujo que, dada un numero de 4 cifras, reordene sus dígitos de manera inversa. Por ejemplo 3245 ---> 5423
numero = int(input("Ingrese un número: "))
nume_inv = 0
while numero > 0:
    residuo = numero % 10
    nume_inv = (nume_inv * 10) + residuo
    numero //= 10
print('El inverso del número ingresado es: ', nume_inv)