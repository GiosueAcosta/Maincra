#10.	Escribe un algoritmo o el respectivo diagrama de flujo que intercambie el valor de dos variables e imprima los valores antes y después del intercambio. Por ejemplo, si a = 1 y b = 3, al intercambiar sus valores serán a = 3 y b = 1 (Consejo: usar variable auxiliar).
print("Ingrese dos números: ")
a = int(input())
b = int(input())
print("a = ", a, " b =", b)
c = a
a = b
b = c
print("a = ", a, " b =", b)