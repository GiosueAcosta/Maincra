#40.	Escribe un algoritmo o el respectivo diagrama de flujo que lea 3 números e indique si al menos 2 de ellos son iguales

print("Ingrese tres números: ")
lista = []
for i in range(3):
    numero=int(input())
    lista.append(numero)
if len(lista) != len(set(lista)):  # Se convierte en verdadero porque hay dos elementos iguales
    print("Hay almenos dos números iguales...:)")
else:
    print("Todos los elementos son diferentes...:(")