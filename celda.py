NULA = 0
VACIA = 2
FICHA = 10

class Celda(object):
    def __init__(self, fila, columna, valor):
        self.__fila = fila
        self.__columna = columna
        self.__valor = valor
    
    def getFila(self):
        return self.__fila
    
    def getColumna(self):
        return self.__columna
    
    def esFicha(self):
        return self.__valor  == FICHA
    
    def esVacia(self):
        return self.__valor  == VACIA
    
    def esNula(self):
        return self.__valor  == NULA

if __name__ == '__main__':
    celda = Celda(1,2)
    print(celda.getFila())