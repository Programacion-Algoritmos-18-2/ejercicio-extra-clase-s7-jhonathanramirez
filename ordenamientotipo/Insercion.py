class OrdenamientoI:
    def __init__(self, listado):#Contructor que recibe un listado
        self.datos = listado

    def __str__(self):
        tem = "" #Concatenamos una cadena 
        for n in self.datos:#Recorremos un for la lista
            tem = "%s %s" % (tem, n)
        tem = ("%s" % tem) 

        return tem#Retonamos la cadena
    def ordenamientoInsercion(self):
    	insercion = 0
    	for siguiente in range( 1, (len(self.datos))):#for que marca el rango de la lista de datos
            insercion = self.datos[siguiente]#Almacenamos el valor en el elemento actual                
            moverElemento = siguiente;#Inicializamos la ubicacion para colocar el siguiente elemento
            while ( moverElemento > 0 and  self.datos[ moverElemento - 1 ] > insercion):#while para buscar el lugar para colocar el elemento actual
            	self.datos[ moverElemento ] = self.datos[ moverElemento - 1 ]#Desplazamos el elemento una posicion en la derecha
            	moverElemento-=1
            self.datos[moverElemento] = insercion#Coloca el elemento insertado
            print(self.__str__())#Se imprime al str para que presente el cambio del arreglo