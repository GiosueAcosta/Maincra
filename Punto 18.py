#18.	Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de segundos indique cuántos horas minutos y segundos representan. Por ejemplo si el valor es 86399, imprimirá el siguiente resultado - -> 23: 59: 59

segundos=int(input("Ingrese la cantidad de segundos: "))
horas=segundos//3600
sobrante1=segundos%3600
minutos=sobrante1//60
sobrante2=sobrante1%60

print(horas,":",minutos,":",sobrante2)