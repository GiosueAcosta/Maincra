#31.	Escribe un algoritmo o el respectivo diagrama de flujo que determine el valor de un pasaje en avión, conociendo la distancia a recorrer, el número de días de estancia, y sabiendo que, si la distancia a recorrer es superior a 1000 Km y el número de días de estancia es superior a 7, la línea aérea le hace un descuento del 15%. (el precio por km. es de $5.000 aunque el mínimo a cobrar siempre es $100.000).

print("********Costo de pasaje de avión********")

dist=int(input("¿Cuál es la dintancia que recorrerá su vuelo? "))
dias=int(input("¿Cuántos días sera su estancia?"))

precio=dist*5000
if dist<=20:
    precio=100000

if precio>100000:
    dist-=20
    precio=100000+dist*5000

if dist>1000 and dias>7:
    precio=precio*0.15

print(f"Su pasaje tendra valor de ${precio}")