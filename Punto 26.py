#26.	Escribe un algoritmo o el respectivo diagrama de flujo que lea las cinco notas obtenidas por un estudiante y calcule su nota final, sabiendo que las cada nota tiene el siguiente valor: n1 (15%), n2 (20%), n3 (15%), n4 (30%), n5 (20%). Si la nota obtenida es menor a 2,0 deberá indicarle al estudiante que no puede habilitar, si la nota obtenida es menor a 3 deberá indicar que reprobó, si la nota es mayor o igual a 3 deberá indicar que aprobó y si es mayor a 4,5 extenderá un mensaje de felicitación al estudiante.
print("Ingrese las cinco  notas del estudiante:")
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
notas=[n1*0.15,n2*0.2,n3*0.15,n4*0.3,n5*0.2]
promedio=sum(notas)
if promedio > 2.0:
    if promedio <=3.0:
        print("Rebrobó, pero aún la puede pasar...Nos vemos cuando la recupere")
    elif 3.0 <= promedio < 4.5:
        print("Abrobó...:)")
    else:
        print("Felicitaciones.....Me llenas de orgullo")
else:
    print("Reprobó y no puede habilitar..:(")