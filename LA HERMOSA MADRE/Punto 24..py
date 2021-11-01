#24.	Escribe un algoritmo o el respectivo diagrama de flujo que determine el IVA (19%) de una venta, si esta es mayor o igual 150.000 aplicar un descuento del 5%

valventa=int(input("Ingrese el valor de la venta: "))
valor_IVA=int(valventa*0.19)
if valor_IVA>=150000:
    valor_IVA=int(valventa*0.14)
    total=int(valventa+valor_IVA)
    print("El valor del IVA= ",valor_IVA,"\nPrecio total de la compra= ",total)
else:
    total=int(valventa+valor_IVA)
    print("El valor del IVA= ", valor_IVA,"\nPrecio total de la compra= ", total)