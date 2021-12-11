from juego import Juego
from helper import Helper
from color import Color
import menu
from estadoEnum import Estado

def partida(juego):
    salir = False
    #Muestra el número de movimientos realizados y el tablero con la partida. 
    juego.mostrar()
    
    while juego.getEstado() == Estado.JUGANDO.value:                         
        filaFicha, columnaFicha, direccion, salir = juego.leerMovimiento()   
             
        if salir:
            break
        else:
            juego.ejecutarMovimiento(filaFicha,columnaFicha, direccion) 
                   
        #Recalcula el estado del juego
        juego.nuevoEstado()
        #Actualiza la visualización del tablero
        juego.mostrar()

    if juego.getEstado() == Estado.JUGANDO.value:         
        juego.setEstado(Estado.ABANDONO.value)
    
    if juego.getEstado() == Estado.GANA.value:     
        print(Color.VERDE + "GANASTE EL JUEGO" + Color.FIN)
        Helper.pulsarTecla()
    
    if juego.getEstado() == Estado.BLOQUEO.value:     
        print(Color.VERDE + "PERDISTE, ESTÁS BLOQUEADO" + Color.FIN)
        Helper.pulsarTecla()

    if salir and Helper.leerSiONo(Color.NEGRITA + "¿QUIERE GUARDAR SU PROGRESO? S/N: " + Color.FIN) == 'S':
        juego.guardar()
    
def jugar():
    while True:
        juego = Juego()        
        opcion = menu.menuPrincipal()
        
        if opcion == 1:
            miniMenuOpcion = menu.menuTablero()

            if miniMenuOpcion == 1:                    
                juego.nuevoJuego(5)
                partida(juego)

            elif miniMenuOpcion == 2:
                juego.nuevoJuego(7) 
                partida(juego)
        
            elif miniMenuOpcion == 3:
                juego.nuevoJuego(9) 
                partida(juego)

        if opcion == 2:
            exito = juego.cargar()
            if exito: 
                partida(juego)
            else:
                print(Color.ADVERTENCIA + "NO SE PUDO CARGAR EL JUEGO, INICIE UNO NUEVO" + Color.FIN)
                Helper.pulsarTecla()
        
        if opcion == 0:
            print("\nFIN DEL PROGRAMA")
            break
        
if __name__ == '__main__':
    jugar()    

