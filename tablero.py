import numpy as np
from ficha import Ficha
from celda import Celda

ARRIBA = 1
ABAJO = 2
IZQUIERDA = 3
DERECHA = 4

class Tablero (object):
    def __init__(self, dimension):
        self.__dimension = dimension
        self.__matriz = []
        self.__cantidadFichas = 0

    def setDimension(self, dimension):
        self.__dimension = dimension

    def getDimension(self):
        return self.__dimension
        
    def setCantidadFichas(self, cantidadFichas):
        self.__cantidadFichas = cantidadFichas
    
    def getCantidadFichas(self):
        return self.__cantidadFichas 

    def setMatriz(self, matriz):
        self.__matriz = matriz
        
    def getMatriz(self):
        return self.__matriz

    def getMatrizToList(self):
        matrixlist = []
        for i in range(self.__dimension):
            fila = []
            for j in range(self.__dimension):
                celda = self.__matriz[i][j]
                fila.append(int(celda))
            matrixlist.append(fila)
        return matrixlist
    
    def colocarFichas(self):
        matrizFichas = []
        cantidadFichas = 0

        if self.__dimension == 5:
            matrizFichas = np.zeros((5,5),dtype=int)
            matrizFichas[0] = 10
            matrizFichas[1] = 10
            matrizFichas[2] = 10
            matrizFichas[2][2] = 2 
            matrizFichas[3] = 10
            matrizFichas[4] = 10
            cantidadFichas = np.count_nonzero(matrizFichas) - 1

        if self.__dimension == 7:
            matrizFichas = np.zeros((7,7),dtype=int)
            matrizFichas[0][2:5] = 10
            matrizFichas[1][2:5] = 10
            matrizFichas[2] = 10
            matrizFichas[3] = 10
            matrizFichas[3][3] = 2
            matrizFichas[4] = 10
            matrizFichas[5][2:5] = 10
            matrizFichas[6][2:5] = 10            
            cantidadFichas = np.count_nonzero(matrizFichas) - 1
        
        if self.__dimension == 9:
            matrizFichas = np.zeros((9,9),dtype=int)
            matrizFichas[0][4] = 10
            matrizFichas[1][3:6] = 10
            matrizFichas[2][2:7] = 10
            matrizFichas[3][1:8] = 10
            matrizFichas[4] = 10
            matrizFichas[4][4] = 2
            matrizFichas[5][1:8] = 10
            matrizFichas[6][2:7] = 10
            matrizFichas[7][3:6] = 10
            matrizFichas[8][4] = 10
            cantidadFichas = np.count_nonzero(matrizFichas) - 1

        self.__matriz = matrizFichas
        self.__cantidadFichas = cantidadFichas

    def cargarTablero(self, matrizCargada, cantidadFichas):
        matrizFichas = np.zeros((self.__dimension,self.__dimension),dtype=int)
        for i in range(self.__dimension):
            matrizFichas[i] = np.array(matrizCargada[i])
        
        self.__matriz = matrizFichas
        self.__cantidadFichas = cantidadFichas

    def mostrarMatriz(self):
        print(np.matrix(self.__matriz))
    
    def contadorDeFichasSinMovimiento(self):
        contador = 0
        for i in range(self.__dimension):
            for j in range (self.__dimension):
                if self.getCelda(i, j).esFicha():
                    ficha = Ficha (i,j, self.getMatrizToList())
                    if ficha.movimientos == [False, False, False, False]:
                        contador += 1
        return contador
    
    def contadorDeFichas(self):
        contador = 0
        for i in range(self.__dimension):
            for j in range(self.__dimension):
                if self.__matriz[i,j] == 10:
                    contador += 1
        return contador
    
    def estaJugando(self):
        return self.__cantidadFichas - self.contadorDeFichasSinMovimiento() >= 1
            
    def estaBloqueado(self):
        return self.contadorDeFichasSinMovimiento() == self.__cantidadFichas and self.__cantidadFichas > 1
        
    def esGanador(self):
        return self.__cantidadFichas == 1
    
    def getCelda(self, fila, columna):
        return Celda(fila, columna, self.__matriz[fila,columna])
            
    def moverFicha(self, fila, columna, direccion):    
        exito = False        

        if direccion == ABAJO:
            try:
                if self.__matriz[fila + 1, columna] == 10 and self.__matriz[fila + 2, columna] == 2:
                    self.__matriz[fila, columna] = 2 
                    self.__matriz[fila + 1, columna] = 2 
                    self.__matriz[fila + 2, columna] = 10
                    self.__cantidadFichas -= 1
                    exito = True
            except IndexError:
                pass
        
        elif direccion == DERECHA:
            try:
                if self.__matriz[fila, columna + 1] == 10 and self.__matriz[fila, columna + 2] == 2:
                    self.__matriz[fila, columna] = 2 
                    self.__matriz[fila, columna + 1] = 2 
                    self.__matriz[fila, columna + 2] = 10
                    self.__cantidadFichas -= 1
                    exito = True
            except IndexError:
                pass
        
        elif direccion == IZQUIERDA:
            try:
                if columna - 1 == -1 or columna - 2 == -1: 
                    exito = False
                elif self.__matriz[fila, columna - 1] == 10 and self.__matriz[fila, columna - 2] == 2:
                    self.__matriz[fila, columna] = 2 
                    self.__matriz[fila, columna - 1] = 2 
                    self.__matriz[fila, columna - 2] = 10
                    self.__cantidadFichas -= 1
                    exito = True
            except IndexError:
                pass
        
        elif direccion == ARRIBA:
            try:
                if fila - 1 == -1 or fila - 2 == -1: 
                    exito = False
                elif self.__matriz[fila - 1, columna] == 10 and self.__matriz[fila - 2, columna] == 2:
                    self.__matriz[fila, columna] = 2 
                    self.__matriz[fila - 1, columna] = 2 
                    self.__matriz[fila - 2, columna] = 10
                    self.__cantidadFichas -= 1
                    exito = True
            except IndexError:
                pass

        return exito
