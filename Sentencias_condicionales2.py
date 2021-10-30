print("Sistema para calcular el promedio de un alumno.")
nombre=input("Cual es tu nombre? ")
notamat=int(input(nombre + " Cual es tu nota en Matematicas? "))
notaQuimi=int(input(nombre + " Cual es tu nota en Quimica? "))
notaBiologia=int(input(nombre + " Cual es tu nota en Biologia? "))

promedioNotas=(notamat + notaQuimi + notaBiologia)//3

if promedioNotas >= 6:
    print("Felicidades " + nombre + " Aprobaste!!! " "Con un promedio de:",promedioNotas )
    
    
print("Fin.")

       

