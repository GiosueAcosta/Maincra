#6.	Escribe un algoritmo o el respectivo diagrama de flujo que determine el IVA (19%) de una venta realizada, indicando el valor original, el valor del IVA y el valor de la venta con IVA incluido.

op1=100000
op2=50000
op3=200000
total=op1+op3+op2
totalIva=(total*0.19)+total
print("{:^20} {:^20} ".format("PRODUCTO", "PRECIO SIN IVA"))
print("{:^20} {:^20} ".format("Bolso",op1 ))
print("{:^20} {:^20} ".format("Cartera",op2))
print("{:^20} {:^20} ".format("Vestido",op3 ))
print("{:^20} {:^20} {:^20}".format("TOTAL DE LA VENTA", "VALOR DEL  IVA", "TOTAL CON IVA"))
print("{:^20} {:^20} {:^20}".format(total,"19%",totalIva))