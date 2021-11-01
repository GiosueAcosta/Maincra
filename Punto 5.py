#5.	Escribe un algoritmo o el respectivo diagrama de flujo que lea un número decimal e imprima su parte entera y su parte decimal por aparte.
num=input("Ingrese un número decimal: ")
if "." in num:
    punto = num.index(".")
    entera = num[:punto]
    decimal = num[punto+1:]
    print("La parte entera=", entera)
    print("La parte decimal=", decimal)
else:
    punto = num.index(",")
    entera = num[:punto]
    decimal = num[punto+1:]
    print("La parte entera=", entera)
    print("La parte decimal=", decimal)