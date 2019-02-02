class OrdenamientoS:
    def __init__(self, listado):#Contructor que recibe un listado
        self.datos = listado

    def __str__(self):
        tem = "" #Concatenamos una cadena 
        for n in self.datos:#Recorremos un for la lista
            tem = "%s %s" % (tem, n)
        tem = ("%s" % tem) 

        return tem#Retonamos la cadena
    def ordenamientoSeleccion(self):
    	masPequeño = 0
    	for  i in range( 0, (len(self.datos)-1)):#for que marca el rango de la lista de datos - 1
            masPequeño = i#primer indice del resto del arreglo
            for indice in range((i+1),len(self.datos)):#for que itera para buscar el indice del elemento mas pequeño del listado
                if (self.datos[indice] < self.datos[masPequeño]):#If para preguntamos si la lista en la posicion indice es menor que la lista en la posicion masPequeño
                    masPequeño = indice#si se cumple la condicion masPequeño toma el valor de indice
            self.intercambio(i, masPequeño)#Enviamos al metodo intercambio la posiciones i y el indice mas pequeño
            print(self.__str__())#Se imprime el str para cada interacion del for

    def intercambio(self, primero, segundo):
    	temp = self.datos[primero]#Creamos una variable temporal para almacenar la posiones primero del listado para intercambar los datos
    	self.datos[primero] = self.datos[segundo]
    	self.datos[segundo] = temp