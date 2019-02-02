#Importamos todas la clases que vamos a utilizar
from ordenamientotipo.Seleccion import *
from ordenamientotipo.Insercion import *
datos = [77, 27,2, 10, 8, 29, 38, 4, 26, 98,88]#Creamos una lista con los datos 
OrS = OrdenamientoS(datos)#Creamos objeto tipo OrdenamientoS
OrI = OrdenamientoI(datos)#Creamos objeto tipo OrdenamientoI
print("Arreglo desordenado")
print(datos,"\n");#Se imprime los valores
print("[1]Ordenamiento Seleccion\n"+#Menu
	  "[2]Ordenamiento Insercion")
op = int(input("Ingrese opcion"))
if (op == 1):#Opcion 1 para presentar ordenado por seleccion 
    print("Datos ordenados por selección")
    OrS.ordenamientoSeleccion()
    print("\nArreglo Ordenado")
    print(OrS)#Se imprime el objeto
if (op == 2):#Opcion 2 para presentar ordenado por inserccion 
	print("Datos ordenamiento por inserción")
	OrI.ordenamientoInsercion()
	print("\nArreglo Ordenado")
	print(OrI)#Se imprime el objeto 