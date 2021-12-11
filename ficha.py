class Ficha:
    def __init__(self, fila, columna, tablero):

        #atributos
        self.fila = fila
        self.columna = columna
        # movimientos [arriba,abajo,izquierda,derecha]
        self.movimientos = []
        self.tablero = tablero
        
        #se inicializa el metodo en el construcctor para que movimientos siempre este cargado
        self.movimientosDisponibles() 

    #getter
    @property
    def mostrarMovimientos(self):
        return self.movimientos[0], self.movimientos[1],self.movimientos[2], self.movimientos[3]

    @property
    def mostrarFila(self):
        return self.fila

    @property
    def mostrarColumna(self):
        return self.columna

    #setter

    @mostrarFila.setter
    def mostrarFila(self,nuevaFila):
        self.fila = nuevaFila

    @mostrarColumna.setter
    def mostrarColumna(self,nuevaColumna):
        self.fila = nuevaColumna

    
    def hayFichaCapturable(self):
        return self.tablero[self.fila - 1][self.columna] == 10

    #metodos
    def esMovibleArriba(self):
        try:
            if self.fila - 1 == -1 or self.fila - 2 == -1: 
                return False
                
            if (self.tablero[self.fila - 1][self.columna] == 10 and self.tablero[self.fila - 2][self.columna] == 2):                              
                return True
            else:
                return False                
        except IndexError:
            return False

    def esMovibleAbajo(self):
        try:
            if (self.tablero[self.fila + 1][self.columna] == 10 and self.tablero[self.fila + 2][self.columna] == 2):
                return True
            else:
                return False
        except IndexError:
            return False

    def esMovibleIzquierda(self):
        try:
            if self.columna - 1 == -1 or self.columna - 2 == -1: 
                return False
            if self.tablero[self.fila][self.columna - 1] == 10 and self.tablero[self.fila][self.columna - 2] == 2:
                return True
            else:
                return False
        except IndexError:
            return False

    def esMovibleDerecha(self):
        try:
            if self.tablero[self.fila][self.columna + 1] == 10 and self.tablero[self.fila][self.columna + 2] == 2:
                return True
            else:
                return False
        except IndexError:
            return False

    def movimientosDisponibles(self):
       self.movimientos.append(self.esMovibleArriba())
       self.movimientos.append(self.esMovibleAbajo())
       self.movimientos.append(self.esMovibleIzquierda())
       self.movimientos.append(self.esMovibleDerecha())

