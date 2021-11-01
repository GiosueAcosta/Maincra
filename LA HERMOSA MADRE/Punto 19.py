#19.	Escribe un algoritmo o el respectivo diagrama de flujo que, dada una cantidad de dinero, determine la menor cantidad de billetes de cada denominación que se puede entregar.

dinero=int(input("Ingrese una cantidad de dinero: "))
cantidad=1

def cantidad_mil(cantidad):
    cantidad = dinero//1000
    return cantidad
if cantidad_mil(cantidad) >= 1:
    def cantidad_dos(cantidad):
        cantidad=dinero//2000
        return cantidad
    def cantidad_cinco(cantidad):
        cantidad=dinero//5000
        return cantidad
    def cantidad_diez(cantidad):
        cantidad=dinero//10000
        return cantidad
    def cantidad_veinte(cantidad):
        cantidad=dinero//20000
        return cantidad
    def cantidad_cincuenta(cantidad):
        cantidad=dinero//50000
        return cantidad
    print("Billetes de $1000: ",cantidad_mil(cantidad)," billetes\nBilletes $2000: ",cantidad_dos(cantidad)," billetes\nBilletes de $5000:",cantidad_cinco(cantidad),"billetes\nBilletes de $10000: ",cantidad_diez(cantidad)," billetes\nBilltes de $20000: ",cantidad_veinte(cantidad),"billetes\nBilletes de $50000: ",cantidad_cincuenta(cantidad)," billetes")
else:
    print("La cantidad de dinero no es suficiente para contar en billetes")