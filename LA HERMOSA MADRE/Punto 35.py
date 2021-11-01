#35.	Escribe un algoritmo o el respectivo diagrama de flujo que dado un número entre 0 y 10, imprima el nombre del número. Ejemplo: 1 - - -> UNO

numeros={0:"CERO",1:"UNO",2:"DOS",3:"TRES",4:"CUATRO",5:"CINCO",6:"SEIS",7:"SIETE",8:"OCHO",9:"NUEVE",10:"DIEZ"}
numero=int(input("Ingrese un número entre el 0 y 10: "))
nombre=numeros.get(numero)
print("{} ---> {}".format(numero,nombre))