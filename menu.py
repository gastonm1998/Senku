from helper import Helper
from color import Color

def menuPrincipal():
    while True:
        Helper.limpiarPantalla()
        print(Color.VERDE + 

    '''
                                                                 
      ,MMMMMMM,  MMMMMMMMMMM  NMMMM     +MMM   MMMM    ZMMMM MMMM     7MMM      
     MMMMMMMMM   MMMMMMMMMMM  NMMMMM    ?MMM   MMMM   MMMM7  MMMM     IMMM 
    MMMM         MMMM         NMMMMMD   ?MMM   MMMM  MMMM,   MMMM     IMMM 
    MMMM~        MMMM         NMMMMMMI  ?MMM   MMMM MMMM~    MMMM     IMMM 
    OMMMMMMMD    MMMMMMMMMM   NMMM MMMI ?MMM   MMMMMMMM      MMMM     IMMM 
      7MMMMMMMI  MMMMMMMMMM   NMMM  MMMDIMMM   MMMMDMMMM     MMMM     IMMM 
          ~MMMM  MMMM         NMMM   MMMMMMM   MMMM ZMMMM    MMMM     OMMM 
    :8     MMMM  MMMM         NMMM    MMMMMM   MMMM  8MMMM    MMMM    MMMZ
    MMMMMMMMMM   MMMMMMMMMMM  NMMM     MMMMM   MMMM   MMMMM   =MMMMMMMMMM
     MMMMMMMI    MMMMMMMMMMM  MMMM      MMMM   MMMM    MMMMM    8MMMMM8 


    1 - NUEVO JUEGO
    2 - CARGAR ULTIMO JUEGO                      
    0 - SALIR                    
                                                                          
    '''+ Color.FIN)
        
        try:
            opcion = int(input("    SELECCIONE UNA OPCION: "))
            if opcion == 1 or opcion == 2 or opcion == 0:
                return opcion
        except ValueError:
            pass

def menuTablero():
    while True:
        print('''
    1 - CUADRADO: 5x5
    2 - STANDARD: 7x7
    3 - DIAMANTE: 9x9                      
    0 - SALIR
        ''')
        try:
            opcion = int(input("    SELECCIONE EL TABLERO: "))
            if opcion >= 0 and opcion <= 3:
                return opcion
        except ValueError:
            pass