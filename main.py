from alumno import *
from materia import *
from universidad import *

p1 = Alumno(input("Escribe tu nombre: "), input("Escribe tu # de cuenta: "))

p2 = Materia(input("Escribe la materia que quieras registrar: "), input("Escribe el codigo de la materia: "))

p3 = Universidad(input("Escribe el nombre de la universidad: "), input("Escribe el nombre del pais: "))

print(p1.name + "(" + str(p1.cuenta) + "), la materia: " + str(p2.name) +" con el codigo " + str(p2.codigo) + " ha quedado registrada.")
print("Bienvenido a la " + str(p3.name)  + " en " + str(p3.pais))
