#39.	Escribe un algoritmo o el respectivo diagrama de flujo que lea un número del día de la semana (entre 1 y 7) e indique el nombre del día. Por ejemplo:  1 ---> Lunes ; 5 ---> Viernes

semana={1:"Lunes",2:"Martes",3:"Miércoles",4:"Jueves",5:"Viernes",6:"Sábado",7:"Domingo"}
numero=int(input("Ingrese el número del día de la semana que quiere encontrar: "))
dia=semana.get(numero)
print("{} ---> {}".format(numero,dia))