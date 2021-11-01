#12.	Escribe un algoritmo o el respectivo diagrama de flujo que determine la distancia recorrida por un objeto luego de una cantidad de tiempo, si se sabe que va en línea recta y además se conoce su aceleración y su velocidad.
#d=(vi*t)+((a(t)^2)/2)
tiempo=45 #segundos
velocidad=9 #m/s
aceleracion=0.2 #m/s^2
distancia=(tiempo*velocidad)+((aceleracion*(tiempo**2))/2)
print(distancia)