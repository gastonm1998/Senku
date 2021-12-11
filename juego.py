#El estado del juego, que representaremos: BLOQUEO, GANA, JUGANDO, ABANDONO.
from tablero import Tablero
from ficha import Ficha
from helper import Helper
from color import Color
import json
from json.decoder import JSONDecodeError
from estadoEnum import Estado
from os.path import exists

class Juego (object):

    def __init__(self, tablero = [], numeroMovimientos = 0, estado = ''):
        self.__tablero = tablero
        self.__numeroMovimientos = numeroMovimientos
        self.__estado = estado

    def nuevoJuego(self, dimension):
        self.__tablero = Tablero(dimension)
        self.__tablero.colocarFichas()
        self.__numeroMovimientos = 0
        self.__estado = Estado.JUGANDO.value
        
    def setTablero(self, tablero):
        self.__tablero = tablero

    def getTablero(self):
        return self.__tablero
                
    def setNumeroMovimientos(self, numeroMovimientos):
        self.__numeroMovimientos = numeroMovimientos

    def getNumeroMovimientos(self):
        return self.__numeroMovimientos

    def setEstado(self, estado):
        self.__estado = estado

    def getEstado(self):
        return self.__estado
    
    def mostrar(self, ficha = None):
        Helper.limpiarPantalla()
        lineaArriba = '┌' + '┬'.join('───' for i in range(self.__tablero.getDimension())) + '┐'
        #lineaArriba = '┌───┬───┬───┬───┬───┬───┬───┐'
        
        lineaMedio  = '├' + '┼'.join('───' for i in range(self.__tablero.getDimension())) + '┤'
        #lineaMedio = '├───┼───┼───┼───┼───┼───┼───┤'
        
        lineaAbajo = '└' + '┴'.join('───' for i in range(self.__tablero.getDimension())) + '┘'
        #lineaAbajo = '└───┴───┴───┴───┴───┴───┴───┘'

        print(" MOVIMIENTOS:", self.__numeroMovimientos,"FICHAS:", self.__tablero.getCantidadFichas())
        print(" ", end="")
        for i in range(self.__tablero.getDimension()):
            print("   " + str(i + 1), end="")
        print("\n ",lineaArriba)
                
        for i in range(self.__tablero.getDimension()):
            fila = '│'
            for j in range(self.__tablero.getDimension()):

                numero = self.__tablero.getMatriz()[i][j]
                celda = ' '
                if numero == 10: 
                    celda =  Color.VERDE + '⬤' + Color.FIN
                if numero == 2:
                    celda =  Color.VERDE + '⦾' + Color.FIN
                if numero == 0:
                    celda = ' '
                    
                if ficha != None and i == ficha.fila and j == ficha.columna:
                    celda = Color.AZUL + '⬤' + Color.FIN
                    
                fila += ' '+ celda + ' │'
                
            print(i + 1, fila)
            
            if i != self.__tablero.getDimension() - 1: 
                print(" ",lineaMedio)
            else: 
                print(" ",lineaAbajo) 
    
    def serializar(self):  
        self.__tablero.setMatriz(self.__tablero.getMatrizToList())
        datos = {}
        datos['Juego'] = []
        datos['Juego'].append(
            {
                'tablero' : {
                    'dimension' : self.__tablero.getDimension(),
                    'matriz' : self.__tablero.getMatriz(),
                    'cantidadFichas' : self.__tablero.getCantidadFichas() 
                },
                'numeroMovimientos' : self.__numeroMovimientos,
                'estado' : self.__estado
            }
        )
        return datos
        
    def leerMovimiento(self):
        salir = False
        direccion = 0
        
        fila, columna = Helper.leerFilaColumna(self.__tablero.getDimension())
        
        #Si ingresa un 0 sale de la partida
        if fila == 0:
            salir = True
        
        #Si la fila y columna estan fuera del tablero
        elif self.__tablero.getCelda(fila - 1, columna - 1).esNula():
            print(Color.ERROR + "Esa posición está fuera del tablero" + Color.FIN)
            Helper.pulsarTecla()
        
        #Si la fila y columna corresponden a una ficha
        elif self.__tablero.getCelda(fila - 1, columna - 1).esFicha():            
            
            ficha = Ficha(fila - 1, columna - 1, self.__tablero.getMatrizToList())
            self.mostrar(ficha)
            
            if ficha.movimientos == [False, False, False, False]:
                print(Color.ERROR + "Esa ficha no puede moverse" + Color.FIN)
                Helper.pulsarTecla()
                
            else:
                print("¿Hacia dónde se moverá la ficha?")  

                if ficha.movimientos[0]:
                    print(Color.VERDE + "1 - Arriba" + Color.FIN)
                else:
                    print(Color.ERROR + "1 - Arriba (No Disponible)" + Color.FIN)
                
                if ficha.movimientos[1]:
                    print(Color.VERDE + "2 - Abajo" + Color.FIN)
                else:
                    print(Color.ERROR + "2 - Abajo (No Disponible)" + Color.FIN)
                
                if ficha.movimientos[2]:
                    print(Color.VERDE + "3 - Izquierda" + Color.FIN)
                else:
                    print(Color.ERROR + "3 - Izquierda (No Disponible)" + Color.FIN)
                
                if ficha.movimientos[3]:
                    print(Color.VERDE + "4 - Derecha" + Color.FIN)
                else:
                    print(Color.ERROR + "4 - Derecha (No Disponible)" + Color.FIN)
                            
                direccion = Helper.leerDireccion()
        
        #Si la fila y columna ingresadas no corresponden a una ficha            
        elif self.__tablero.getCelda(fila - 1, columna - 1).esVacia():
            print(Color.ERROR + "No hay ficha en esa posición" + Color.FIN)
            Helper.pulsarTecla()
            
        return fila - 1, columna - 1, direccion, salir

    
    def ejecutarMovimiento(self, fila, columna, direccion):
        exito = self.getTablero().moverFicha(fila, columna, direccion)
        if exito: 
            #Si se realizó el movimiento con exito, se incrementa el contador de movimientos
            self.__numeroMovimientos += 1

    def guardar(self):
        with open('game.json', 'w') as archivo:
            json.dump(self.serializar(), archivo)
            
    def cargar(self):        
        if not exists('game.json'):
            return False
        
        exito = False

        with open('game.json') as json_file:
            try:                
                datos = json.load(json_file)
                    
                if len(datos['Juego']) != 0:
                    for registro in datos['Juego']:                    
                        self.__numeroMovimientos = registro['numeroMovimientos']

                        self.__estado = registro['estado']    
                                          
                        dimension = registro['tablero']['dimension']
                        cantidadFichas = registro['tablero']['cantidadFichas']
                        matrizCargada = registro['tablero']['matriz']
                        self.__tablero = Tablero(dimension)
                        self.__tablero.cargarTablero(matrizCargada, cantidadFichas)
                    exito = True

            except JSONDecodeError:
                pass

        if self.__estado == Estado.ABANDONO.value:
            if self.__tablero.estaJugando():
                self.setEstado(Estado.JUGANDO.value)

        return exito
    
    def nuevoEstado(self):
        if(self.__tablero.esGanador()):
            self.setEstado(Estado.GANA.value)
        
        elif(self.__tablero.estaJugando()):
            self.setEstado(Estado.JUGANDO.value)
        
        else:
            self.setEstado(Estado.BLOQUEO.value)

