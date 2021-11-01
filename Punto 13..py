#13.	Escribe un algoritmo o el respectivo diagrama de flujo que determine la velocidad final de un objeto luego de un tiempo, si se sabe que va en línea recta y además se conoce su aceleración.
#velocidadfinal= velocidadinicial+aceleración*tiempo
#Vamos a suponer que el objeto se encuentra en reposo, por lo tanto la velocidad inical es cero

tiempo=float(input("Ingrese el tiempo: ")) #tiempo en segundos
aceleracion=float(input("Ingrse la aceleración del objeto: "))#aceleracion m/s^^2
velo_fin=aceleracion*tiempo
print("La velocidad final es= {:.2f} m/s^2 ".format(velo_fin))